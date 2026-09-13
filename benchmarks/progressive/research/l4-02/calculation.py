"""Stream pinned ORDS releases; disk-backed identity reconciliation; stdlib only.

python calculation.py --output-dir /tmp/reproduction --work-db /tmp/ords.sqlite
Input overrides: --powered-202407 PATH --powered-202507 PATH --unpowered-202507 PATH
No downloads, no added snapshot totals; row count and summary total use distinct units.
"""
import argparse, collections, csv, hashlib, json, sqlite3
from pathlib import Path

BASE=Path(__file__).parent

def hashfile(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while block:=f.read(1024*1024): h.update(block)
    return h.hexdigest()

def writecsv(path,fields,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(fields);w.writerows(rows)

def main():
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=BASE)
    p.add_argument('--work-db',type=Path,default=Path('/workspace/scratch/b99193148918/openrepair-inputs/reconciliation.sqlite'))
    for name in ['powered-202407','powered-202507','unpowered-202507']:p.add_argument('--'+name,type=Path)
    a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((BASE/'input-manifest.json').read_text())
    assert manifest['total_acquired_data_bytes']<=150000000
    inputs={}
    for x in manifest['inputs']:
        key=('unpowered' if x['coverage']=='unpowered-summary' else 'powered')+'_'+x['snapshot']
        path=getattr(a,key) or Path(x['local_path'])
        assert path.stat().st_size==x['bytes'] and hashfile(path)==x['sha256'],str(path)
        inputs[key]=path
    if a.work_db.exists():raise SystemExit('Choose a new work DB path; existing work is preserved')
    db=sqlite3.connect(a.work_db);db.execute('PRAGMA cache_size=-8192');db.execute('PRAGMA temp_store=FILE')
    results=[];coverage=[];cats=[];meta={'headers':{},'event_date_range':{},'mapping_mismatches':{},'missing_keys':{},'input_hashes':{x['path']:x['sha256'] for x in manifest['inputs']}}
    allowed={r['product_category_id']:r['product_category'] for r in csv.DictReader((BASE/'sources/categories.csv').open())}
    for snap in ['202407','202507']:
        db.execute(f'CREATE TABLE r{snap}(provider TEXT,id TEXT,category_id TEXT,category TEXT,status TEXT,event_date TEXT,digest TEXT)')
        counts=collections.Counter();category=collections.Counter();dates=[];batch=[];mismatch=0;missing=0
        with inputs['powered_'+snap].open(encoding='utf-8-sig',newline='') as f:
            reader=csv.DictReader(f);meta['headers'][snap]=reader.fieldnames
            for r in reader:
                assert None not in r, 'Extra CSV fields'
                provider,status=r['data_provider'],r['repair_status'];counts[(provider,status)]+=1;category[(provider,r['product_category_id'],r['product_category'])]+=1
                if r['event_date']:dates.append(r['event_date'])
                if len(dates)>2:dates=[min(dates),max(dates)]
                mismatch+=allowed.get(r['product_category_id'])!=r['product_category']
                missing+=not provider or not r['id']
                digest=hashlib.sha256(json.dumps(r,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
                batch.append((provider,r['id'],r['product_category_id'],r['product_category'],status,r['event_date'],digest))
                if len(batch)==1000:
                    db.executemany(f'INSERT INTO r{snap} VALUES (?,?,?,?,?,?,?)',batch);batch=[]
            db.executemany(f'INSERT INTO r{snap} VALUES (?,?,?,?,?,?,?)',batch)
        db.execute(f'CREATE INDEX k{snap} ON r{snap}(provider,id)');db.commit()
        providers=sorted({k[0] for k in counts});statuses=sorted({k[1] for k in counts})
        for provider in ['ALL']+providers:
            c=collections.Counter()
            for (pr,st),n in counts.items():
                if provider=='ALL' or pr==provider:c[st]+=n
            den=sum(c.values());coverage.append([snap,'powered',provider,den,'individual rows'])
            for st in statuses:results.append([snap,'powered',provider,st,c[st],den,format(c[st]/den,'.12f')])
        cats.extend([snap,pr,catid,label,n] for (pr,catid,label),n in sorted(category.items()))
        meta['event_date_range'][snap]=[min(dates),max(dates)]
        meta['mapping_mismatches'][snap]=mismatch;meta['missing_keys'][snap]=missing
    un=collections.Counter();uncells=0
    with inputs['unpowered_202507'].open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f):un[(r['data_provider'],r['repair_status'])]+=int(r['total']);uncells+=1
    for provider in ['ALL']+sorted({k[0] for k in un}):
        c=collections.Counter()
        for (pr,st),n in un.items():
            if provider=='ALL' or provider==pr:c[st]+=n
        den=sum(c.values());coverage.append(['202507','unpowered-summary',provider,den,'sum(total)'])
        for st in sorted({k[1] for k in un}):results.append(['202507','unpowered-summary',provider,st,c[st],den,format(c[st]/den,'.12f')])
    meta['unpowered_summary_cells']=uncells
    meta['duplicate_keys']={}
    for snap in ['202407','202507']:
        meta['duplicate_keys'][snap]=db.execute(f'SELECT count(*),coalesce(sum(n-1),0) FROM (SELECT count(*) n FROM r{snap} GROUP BY provider,id HAVING count(*)>1)').fetchone()
        db.execute(f'CREATE TABLE u{snap} AS SELECT * FROM r{snap} GROUP BY provider,id HAVING count(*)=1')
        db.execute(f'CREATE UNIQUE INDEX uk{snap} ON u{snap}(provider,id)')
    join='FROM u202407 a JOIN u202507 b ON a.provider=b.provider AND a.id=b.id'
    meta['shared_unambiguous_keys']=db.execute('SELECT count(*) '+join).fetchone()[0]
    meta['identical_full_rows']=db.execute('SELECT count(*) '+join+' WHERE a.digest=b.digest').fetchone()[0]
    meta['changed_full_rows']=db.execute('SELECT count(*) '+join+' WHERE a.digest!=b.digest').fetchone()[0]
    meta['changed_status']=db.execute('SELECT count(*) '+join+' WHERE a.status!=b.status').fetchone()[0]
    meta['changed_category']=db.execute('SELECT count(*) '+join+' WHERE a.category_id!=b.category_id OR a.category!=b.category').fetchone()[0]
    meta['only_202407_keys']=db.execute('SELECT count(*) FROM u202407 a WHERE NOT EXISTS(SELECT 1 FROM u202507 b WHERE a.provider=b.provider AND a.id=b.id)').fetchone()[0]
    meta['only_202507_keys']=db.execute('SELECT count(*) FROM u202507 b WHERE NOT EXISTS(SELECT 1 FROM u202407 a WHERE a.provider=b.provider AND a.id=b.id)').fetchone()[0]
    writecsv(a.output_dir/'category-transitions.csv',['data_provider','old_category_id','old_category','new_category_id','new_category','shared_record_count'],db.execute('SELECT a.provider,a.category_id,a.category,b.category_id,b.category,count(*) '+join+' WHERE a.category_id!=b.category_id OR a.category!=b.category GROUP BY 1,2,3,4,5 ORDER BY 1,2,4'))
    writecsv(a.output_dir/'provider-overlap.csv',['data_provider','shared_keys','identical_rows','changed_rows','changed_status','changed_category'],db.execute('SELECT a.provider,count(*),sum(a.digest=b.digest),sum(a.digest!=b.digest),sum(a.status!=b.status),sum(a.category_id!=b.category_id OR a.category!=b.category) '+join+' GROUP BY a.provider ORDER BY a.provider'))
    old=json.loads((BASE/'sources/tableschema-202407.json').read_text());new=json.loads((BASE/'sources/tableschema-202507.json').read_text())
    meta['powered_schema_fields_equal']=old['resources'][0]['schema']==new['resources'][0]['schema']
    meta['resource_names']={s:[r['name'] for r in d['resources']] for s,d in [('202407',old),('202507',new)]}
    meta['category_codelist_same_git_blob']='7dccfc83b37ad210cafc2eb429e0f6072d69b2d7'
    writecsv(a.output_dir/'results.csv',['snapshot','coverage','data_provider','repair_status','count','denominator_all_statuses','share'],results)
    writecsv(a.output_dir/'coverage.csv',['snapshot','coverage','data_provider','attempt_count','unit'],coverage)
    writecsv(a.output_dir/'category-counts.csv',['snapshot','data_provider','product_category_id','product_category','count'],cats)
    (a.output_dir/'observed.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
    db.close();print(json.dumps(meta,ensure_ascii=False))

if __name__=='__main__':main()
