"""Reproduce complete-file, weighted ORDS unpowered provider comparison (stdlib only)."""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, default=Path(__file__).parent/'sources/OpenRepairData_v0.3_unpowered_202507.csv')
    p.add_argument('--output-dir', type=Path, default=Path(__file__).parent)
    a = p.parse_args()
    raw = a.input.read_bytes()
    with a.input.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    assert rows and set(rows[0]) == {'data_provider','product_category','repair_status','total'}
    keys = [(r['data_provider'], r['product_category'], r['repair_status']) for r in rows]
    assert len(keys) == len(set(keys)), 'Repeated summary key requires investigation'
    assert all(int(r['total']) >= 0 for r in rows)
    providers = sorted({r['data_provider'] for r in rows})
    statuses = sorted({r['repair_status'] for r in rows})
    assert len(providers) >= 2
    a.output_dir.mkdir(parents=True, exist_ok=True)
    with (a.output_dir/'results.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['data_provider','repair_status','count','denominator_all_statuses','share'])
        for provider in providers[:2]:
            counts=collections.Counter()
            for r in rows:
                if r['data_provider']==provider: counts[r['repair_status']]+=int(r['total'])
            denominator=sum(counts.values())
            for status in statuses: w.writerow([provider,status,counts[status],denominator,format(counts[status]/denominator,'.12f')])
    with (a.output_dir/'category-coverage.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['data_provider','product_category','count','provider_denominator','share'])
        for provider in providers[:2]:
            counts=collections.Counter()
            for r in rows:
                if r['data_provider']==provider: counts[r['product_category']]+=int(r['total'])
            for category,count in sorted(counts.items()):w.writerow([provider,category,count,sum(counts.values()),format(count/sum(counts.values()),'.12f')])
    meta={'input_sha256':hashlib.sha256(raw).hexdigest(),'input_bytes':len(raw),'summary_rows':len(rows),'all_providers_lexicographic':providers,'selected_providers':providers[:2],'observed_statuses':statuses,'all_provider_attempts':sum(int(r['total']) for r in rows),'unit':'repair attempt count represented by total, not summary rows','transformations':'literal Unicode lexicographic provider sort; first two; sum integer total over all product categories; retain every observed status including Unknown; share=count/all-status provider count'}
    (a.output_dir/'observed.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(meta,ensure_ascii=False))

if __name__=='__main__':main()
