#!/usr/bin/env python3
"""Check Stage 8 architecture and synthetic policy cases; not a provider runtime."""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit

PARENT='bc5e53344104400373b84fc2183977817023f16a'
PREFIX='docs/research-logs/'
STEM=PREFIX+'2026-09-10-stage-08-'
DOC=STEM+'execution-layer.md'
CASES=STEM+'policy-cases.json'
SCRIPT=STEM+'verification.py'
RESULT=STEM+'verification.json'
PROGRESS=PREFIX+'bootstrap-progress.md'
EXPECTED={DOC,CASES,SCRIPT,RESULT,PROGRESS}
OWNERS=['question framing','research planning semantics','source strategy','quality / provenance rules',
        'evidence extraction semantics','triangulation','contradiction handling','uncertainty',
        'claim support','synthesis requirements','research repair','research-quality evaluation']
OPERATIONS=['web search','browsing','specialist database search','GitHub retrieval','PDF retrieval / parsing',
            'OCR / multimodal inspection','code / statistical analysis','provider deep-research runs',
            'citation metadata lookup','archiving']
OUTPUTS=['Execution architecture','Tool-selection policy','Provider-boundary rules','Fallback behaviour','Offline and local opportunities']

def blob(data: bytes)->str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def policy(kind: str, data: dict)->str:
    """A deliberately small, synthetic model of the documented gates, not tool dispatch."""
    if kind=='eligibility':
        required=data['required']; obs=data['observations']
        if not required or not isinstance(obs,dict):
            return 'INELIGIBLE'
        return 'ELIGIBLE' if all(obs.get(key) is True for key in required) else 'INELIGIBLE'
    if kind=='intake':
        if data.get('disclosure_allowed') is not True:
            return 'BLOCKED'
        if data.get('source_locators') is not True or data.get('source_extent_known') is not True:
            return 'NEEDS_EVIDENCE'
        return 'READY_FOR_HANDOFF' if data.get('review_passed') is True else 'NEEDS_REVIEW'
    if kind=='fallback':
        failure=data['failure']
        if failure=='unknown_job':
            return 'INSPECT_STATE'
        if failure=='quota':
            return 'RESPECT_LIMIT'
        if data.get('has_permitted_alternative') is True:
            return 'CHECK_ALTERNATIVE'
        return 'BLOCKED' if failure=='permission' else 'RECORD_GAP'
    raise ValueError(f'Unknown case kind: {kind}')

def table_rows(text: str)->list[list[str]]:
    return [[c.strip() for c in line.strip().strip('|').split('|')]
            for line in text.splitlines() if line.startswith('|')]

def assess(files: dict[str,str], paths: set[str], baseline: dict[str,str], old_progress: str)->list[dict]:
    results=[]
    def check(name: str, ok: bool, evidence: object)->None:
        results.append({'check':name,'result':'PASS' if ok else 'FAIL','evidence':evidence})
    doc=files.get(DOC,''); rows=table_rows(doc)
    check('original authority and accepted parent', PARENT in doc and '8ff62c92bada2861ece3684a9e73a83da75d9d94' in doc, PARENT)
    headings=re.findall(r'^## [1-5]\. (.+)$',doc,re.M)
    check('five complete output responsibilities',headings==OUTPUTS,headings)
    for prefix,names,title in [('O',OWNERS,'twelve ownership responsibilities'),('E',OPERATIONS,'ten execution operations')]:
        rr=[r for r in rows if len(r)==4 and re.fullmatch(prefix+r'\d{2}',r[0])]
        actual=[(r[0],r[1]) for r in rr]
        expected=[(f'{prefix}{i:02}',name) for i,name in enumerate(names,1)]
        check(title,actual==expected and all(len(c)>20 for r in rr for c in r[2:]),actual)
    counts={prefix:[r[0] for r in rows if r and re.fullmatch(prefix+r'\d{2}',r[0])] for prefix in ['S','B','F','L']}
    check('selection boundary fallback and local inventories', all(counts[p]==[f'{p}{i:02}' for i in range(1,n+1)] for p,n in [('S',8),('B',12),('F',12),('L',6)]), counts)
    candidates=set(re.findall(r'\bC\d{2}\b',doc))
    check('accepted candidate references',not(candidates-{f'C{i:02}' for i in range(1,36)}),sorted(candidates))
    data=json.loads(files.get(CASES,'{}')); case_list=data.get('cases',[])
    ids=[c.get('id') for c in case_list]
    required_ids=[f'S{i:02}' for i in range(1,15)]+[f'I{i:02}' for i in range(1,6)]+[f'F{i:02}' for i in range(1,7)]
    check('25 explicitly synthetic policy cases',ids==required_ids and 'synthetic' in data.get('evidence_kind',''),ids)
    actual=[]
    for c in case_list:
        answer=policy(c['kind'],c['input'])
        actual.append({'id':c['id'],'expected':c['expected'],'actual':answer,'passed':answer==c['expected']})
    check('policy case outcomes',bool(actual) and all(c['passed'] for c in actual),actual)
    known=paths|set(baseline)|{RESULT}; broken=[]; shape=[]
    for p in (DOC,PROGRESS):
        text=files.get(p,'')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            resolved=str(Path(p).parent/target.split('#')[0])
            if resolved not in known:
                broken.append({'from':p,'target':target})
        width=None
        for i,line in enumerate(text.splitlines(),1):
            if line.startswith('|'):
                current=len(line.strip().strip('|').split('|'))
                if width is not None and current!=width: shape.append(f'{p}:{i}')
                width=current
            else: width=None
    check('documentation links and table consistency',not broken and not shape,{'broken_links':broken,'table_errors':shape})
    guards=['A soft preference cannot pass a hard access constraint','Unknown is not affirmative evidence',
            'Generated plans, extractions, confidence labels, citations and reports must pass',
            'A lost response is not proof that nothing happened','No vector database, graph service or synchronisation daemon',
            'not observed provider results, installed-skill demonstrations or measured performance']
    check('critical boundary distinctions retained',all(g in doc for g in guards),{g:g in doc for g in guards})
    allowed_missing=EXPECTED-{RESULT}; missing=allowed_missing-paths; extras=paths-set(baseline)-EXPECTED
    changed=[p for p,t in files.items() if p in baseline and p!=PROGRESS and blob(t.encode())!=baseline[p]]
    stable_prefix=old_progress.partition('## Stage 7:')[0]
    progress=files.get(PROGRESS,'')
    preserved=bool(stable_prefix) and progress.startswith(stable_prefix) and '2026-09-10-stage-07-publication-receipt.md' in progress
    check('stage-only delta and earlier progress preserved',not missing and not extras and not changed and preserved,
          {'missing':sorted(missing),'extras':sorted(extras),'changed_prior':changed,'preserved_progress':preserved})
    conf=[r[0] for r in rows if len(r)==5 and re.fullmatch(r'R\d{2}',r[0]) and r[-1]=='PASS']
    check('substantive conformance and separate publication gate',conf==[f'R{i:02}' for i in range(1,10)] and 'R10 is the publication gate' in doc,conf)
    return results

def git(root: Path,*args: str)->str:
    run=subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,check=False)
    if run.returncode: raise RuntimeError(run.stderr.strip())
    return run.stdout

def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--baseline-manifest',type=Path);p.add_argument('--parent-progress',type=Path)
    p.add_argument('--negative-controls',action='store_true');a=p.parse_args();root=a.root.resolve()
    if a.baseline_manifest:
        if not a.parent_progress: raise ValueError('Partial workspace requires --parent-progress')
        baseline=json.loads(a.baseline_manifest.read_text());old=a.parent_progress.read_text()
        mode='new stage files plus connector-verified parent inventory'
    else:
        baseline={l.split('\t',1)[1]:l.split()[2] for l in git(root,'ls-tree','-r',PARENT).splitlines()}
        old=git(root,'show',f'{PARENT}:{PROGRESS}');mode='identified Git parent and checkout'
    if blob(old.encode())!=baseline.get(PROGRESS): raise ValueError('Parent progress hash mismatch')
    paths={str(f.relative_to(root)) for f in root.rglob('*') if f.is_file() and '.git' not in f.parts and '__pycache__' not in f.parts}
    files={p:(root/p).read_text() for p in paths if p.endswith(('.md','.json','.py')) and p!=RESULT}
    checks=assess(files,paths,baseline,old);negative=[]
    if a.negative_controls:
        mutations=[('missing ownership',DOC,'| O12 |','| OMIT |','twelve ownership responsibilities'),
                   ('missing execution operation',DOC,'| E10 |','| OMIT |','ten execution operations'),
                   ('unknown candidate',DOC,'C22 for ordinary','C99 for ordinary','accepted candidate references'),
                   ('soft filter falsely hardened',DOC,'A soft preference cannot pass a hard access constraint','A soft preference passes a hard access constraint','critical boundary distinctions retained'),
                   ('broken link',DOC,'(2026-09-10-stage-07-ai-tool-landscape.md)','(missing-stage.md)','documentation links and table consistency'),
                   ('damaged prior progress',PROGRESS,'## Stage 1:','## Missing Stage 1:','stage-only delta and earlier progress preserved')]
        for label,path,before,after,target in mutations:
            fs=copy.deepcopy(files)
            if before not in fs[path]: raise ValueError(f'Missing negative-control target {label}')
            fs[path]=fs[path].replace(before,after,1)
            failures=[r['check'] for r in assess(fs,paths,baseline,old) if r['result']=='FAIL']
            negative.append({'mutation':label,'expected_failure':target,'actual_failures':failures,'result':'PASS' if target in failures else 'FAIL'})
        for label,cid,expected in [('allow soft-only source restriction','S13','ELIGIBLE'),('retry unknown expensive job','F01','CHECK_ALTERNATIVE')]:
            fs=copy.deepcopy(files);data=json.loads(fs[CASES]);next(c for c in data['cases'] if c['id']==cid)['expected']=expected
            fs[CASES]=json.dumps(data);failures=[r['check'] for r in assess(fs,paths,baseline,old) if r['result']=='FAIL'];target='policy case outcomes'
            negative.append({'mutation':label,'expected_failure':target,'actual_failures':failures,'result':'PASS' if target in failures else 'FAIL'})
        target='stage-only delta and earlier progress preserved';failures=[r['check'] for r in assess(files,paths|{'tools/provider-router.py'},baseline,old) if r['result']=='FAIL']
        negative.append({'mutation':'premature provider runtime','expected_failure':target,'actual_failures':failures,'result':'PASS' if target in failures else 'FAIL'})
    ok=all(r['result']=='PASS' for r in checks+negative)
    report={'stage':8,'run_at':datetime.now(timezone.utc).isoformat(),'parent':PARENT,'input_mode':mode,
            'verification_kind':'document and synthetic policy checks; no installed provider test',
            'baseline_inventory':baseline,'checks':checks,'negative_controls':negative,
            'file_blobs':{p:blob((root/p).read_bytes()) for p in sorted(EXPECTED-{RESULT}) if (root/p).exists()},'result':'PASS' if ok else 'FAIL'}
    (root/RESULT).write_text(json.dumps(report,ensure_ascii=False,separators=(',',':'))+'\n')
    print(json.dumps({'result':report['result'],'checks':len(checks),'policy_cases':25,'negative_controls':len(negative),'failures':[r['check'] for r in checks if r['result']=='FAIL']},indent=2))
    return 0 if ok else 1

if __name__=='__main__':
    try: sys.exit(main())
    except (OSError,ValueError,KeyError,RuntimeError) as e:
        print(f'Verification error: {e}',file=sys.stderr);sys.exit(2)
