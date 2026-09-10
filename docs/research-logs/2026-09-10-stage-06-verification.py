#!/usr/bin/env python3
"""Check Stage 6 documents and synthetic policy mechanics; not research quality."""
from __future__ import annotations
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

PARENT='b31ea6243d7a6fdb0da43646d2a20a10d955e901'
PREFIX='docs/research-logs/2026-09-10-stage-06-'
NAMES=['effort-and-stopping.md','policy-cases.json','verification.py','verification.json']
EVIDENCE=['question_fit','material_support','source_coverage','contradictions','freshness','inference']
COSTS=['search calls','browser actions','premium API usage','full-document retrieval','OCR / multimodal analysis','code execution','provider deep-research runs','parallel agents','human specialist review']
STEPS=['question framing','metadata / quick-source scan','source map','focused retrieval','evidence table','targeted verification','full synthesis','specialist / exhaustive research only when justified']
STOPS=['all required subquestions have evidence','material claims have adequate direct support','major source classes are represented','new searches yield diminishing relevant evidence','important contradictions are explained or explicitly unresolved','freshness requirement is satisfied','budget / time ceiling reached with limitations reported']


def git_blob(data:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def number(value:Any)->bool:
    # Fixture units are integers. Real monetary records require their declared precision/currency.
    return type(value) is int and value>=0


def admit(resources:dict[str,dict[str,int]],workers:list[dict[str,int|None]],purpose:str)->bool:
    if purpose not in {'collection','finalisation'} or not workers or not resources:
        return False
    requested:dict[str,int]={}
    for worker in workers:
        if not worker or set(worker)!=set(resources): return False
        for unit,amount in worker.items():
            if unit not in resources or not number(amount): return False
            requested[unit]=requested.get(unit,0)+amount
    for unit,state in resources.items():
        if any(not number(state.get(key)) for key in ['ceiling','consumed','outstanding','reserve']): return False
        headroom=state['ceiling']-state['consumed']-state['outstanding']
        if purpose=='collection': headroom-=state['reserve']
        if headroom<requested.get(unit,0): return False
    return True


def decide(case:dict[str,Any])->str:
    if case.get('decision_required') is not False:
        return 'BLOCKED'
    evidence=case.get('evidence',{})
    ready=all(evidence.get(key) is True for key in EVIDENCE)
    review=case.get('review',{})
    if ready:
        if review.get('passed') is True: return 'STOP_SUFFICIENT'
        if review.get('authorised') is True and review.get('feasible') is True:
            return 'CONTINUE_REVIEW'
        return 'BLOCKED'
    action=case.get('next',{})
    if action.get('useful') is True:
        if action.get('authorised') is not True or action.get('bounded') is not True or not action.get('target_gap'):
            return 'BLOCKED'
        if admit(case.get('resources',{}),[action.get('reservation',{})],'collection'):
            return 'ESCALATE' if action.get('higher_tier') is True else 'CONTINUE'
    limited=case.get('limited',{})
    if all(limited.get(k) is True for k in ['authorised','scope_explicit','finalisation_feasible']):
        return 'STOP_LIMITED'
    return 'BLOCKED'


def settle(case:dict[str,Any])->dict[str,Any]:
    consumed,outstanding,reservation=(case[k] for k in ['consumed','outstanding','reservation'])
    if not all(number(v) for v in [consumed,outstanding,reservation]): raise ValueError('Invalid settlement unit')
    actual=case.get('actual')
    if not case.get('confirmed') or actual is None:
        return dict(consumed=consumed,outstanding=outstanding,unresolved=True,overrun=False)
    if not number(actual) or reservation>outstanding: raise ValueError('Invalid confirmed settlement')
    # Record actual liability even if a supposed bound was exceeded; do not hide an overrun.
    return dict(consumed=consumed+actual,outstanding=outstanding-reservation,unresolved=False,overrun=actual>reservation)


def refresh(case:dict[str,Any])->dict[str,Any]:
    if case.get('scope_changed'): return {'route':'reframe','affected':[]}
    affected=set(case['changed'])
    while True:
        new={key for key,inputs in case['dependencies'].items() if affected.intersection(inputs)}
        if new<=affected: break
        affected|=new
    route='record-check' if not affected else 'delta'
    return {'route':route,'affected':sorted(affected)}


def check_docs(text:str,known_paths:set[str],local_paths:set[str],baseline:dict[str,str])->list[dict[str,Any]]:
    checks=[]
    def add(name,ok,evidence):
        checks.append({'check':name,'result':'PASS' if ok else 'FAIL','evidence':evidence})
    headings=['Research effort tiers','Escalation rules','Stopping rules','Budget controls','Refresh and incremental-update policy']
    add('five required output responsibilities',all(f'## {i}. {h}' in text for i,h in enumerate(headings,1)),headings)
    for prefix,wanted,label in [('E',STEPS,'eight candidate effort steps'),('S',STOPS,'seven stopping criteria'),('K',COSTS,'nine cost categories')]:
        rows=re.findall(r'^\| ('+prefix+r'\d{2}) \| ([^|]+) \|',text,re.M)
        add(label,[row[0] for row in rows]==[f'{prefix}{i:02}' for i in range(1,len(wanted)+1)] and [row[1].strip() for row in rows]==wanted,rows)
    tiers=re.findall(r'^\| (T[1-4]) ([^|]+) \|',text,re.M)
    add('four complete tiers',len(tiers)==4 and [v[0] for v in tiers]==['T1','T2','T3','T4'],tiers)
    escalation=re.findall(r'^\| (X\d{2}) \|',text,re.M)
    updates=re.findall(r'^\| (U\d{2}) \|',text,re.M)
    add('escalation and refresh inventories',escalation==[f'X{i:02}' for i in range(1,10)] and updates==[f'U{i:02}' for i in range(1,7)],{'escalation':escalation,'refresh':updates})
    sources=re.findall(r'^\| (N\d{2}) \| (.+) \|$',text,re.M)
    add('four identified accessed primary sources',len(sources)==4 and all('https://' in row[1] and '10 September 2026' in row[1] for row in sources),[row[0] for row in sources])
    missing=[]
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
        if '://' in target or target.startswith('#'): continue
        path='docs/research-logs/'+target.split('#')[0]
        if path not in known_paths: missing.append(target)
    add('relative document targets resolve',not missing,missing)
    shapes=[]; expected=None; tables=0; fenced=False
    for lineno,line in enumerate(text.splitlines(),1):
        if line.startswith('```'): fenced=not fenced
        if not fenced and line.startswith('|') and line.endswith('|'):
            count=len(re.split(r'(?<!\\)\|',line))-2
            if expected is None: expected=count; tables+=1
            elif count!=expected: shapes.append(lineno)
        else: expected=None
    add('Markdown table structure',not shapes,{'tables':tables,'bad_lines':shapes})
    conformance=re.findall(r'^\| (R\d{2}) \|.*\| (PASS|FAIL|BLOCKED|NOT APPLICABLE) \|$',text,re.M)
    add('complete conformance and no unfinished draft markers',conformance==[(f'R{i:02}','PASS') for i in range(1,10)] and '<!--' not in text,conformance)
    expected_new={PREFIX+name for name in NAMES}
    actual_new=local_paths-set(baseline)
    add('stage-only new files',actual_new==expected_new,{'expected':sorted(expected_new),'actual':sorted(actual_new)})
    return checks


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-manifest',type=Path)
    parser.add_argument('--negative-controls',action='store_true')
    args=parser.parse_args(); root=Path(__file__).resolve().parents[2]
    if args.baseline_manifest:
        manifest=json.loads(args.baseline_manifest.read_text(encoding='utf-8'))
        if manifest.get('parent')!=PARENT: raise ValueError('Unexpected parent revision')
        baseline=manifest['files']; mode='new local files and inspected remote parent inventory'
    else:
        p=subprocess.run(['git','ls-tree','-r',PARENT],cwd=root,text=True,capture_output=True,check=True)
        baseline={line.split('\t')[1]:line.split()[2] for line in p.stdout.splitlines()}
        mode='Git parent and local files'
    text=(root/(PREFIX+NAMES[0])).read_text(encoding='utf-8')
    local={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}
    local.add(PREFIX+NAMES[3]) # The output location is declared, not evidence of prior execution.
    checks=check_docs(text,set(baseline)|local,local,baseline)
    data=json.loads((root/(PREFIX+NAMES[1])).read_text(encoding='utf-8'))
    sizes={'decision_cases':12,'budget_cases':9,'settlement_cases':4,'refresh_cases':4}
    funcs={'decision_cases':lambda c:decide(c['input']),
           'budget_cases':lambda c:admit(c['resources'],c['workers'],c['purpose']),
           'settlement_cases':settle,'refresh_cases':refresh}
    for key,count in sizes.items():
        rows=[{'id':c['id'],'expected':c['expected'],'observed':funcs[key](c)} for c in data[key]]
        passed=len(rows)==count and len({r['id'] for r in rows})==count and all(r['expected']==r['observed'] for r in rows)
        checks.append({'check':key,'result':'PASS' if passed else 'FAIL','evidence':rows})
    controls=[]
    if args.negative_controls:
        def control(name,observed,expected):
            controls.append({'mutation':name,'observed':observed,'expected':expected,'result':'PASS' if observed==expected else 'FAIL'})
        c=deepcopy(data['decision_cases'][0]['input']); c['evidence']['material_support']=False
        control('insufficient evidence cannot use sufficient-stop',decide(c),'CONTINUE')
        c=deepcopy(data['decision_cases'][4]['input']); c['limited']['authorised']=False
        control('remove limited-output authority',decide(c),'BLOCKED')
        c=deepcopy(data['decision_cases'][5]['input']); c['next']['bounded']=False
        control('unbounded next action',decide(c),'BLOCKED')
        c=deepcopy(data['decision_cases'][5]['input']); c['next']['authorised']=False
        control('unapproved escalation operation',decide(c),'BLOCKED')
        c=deepcopy(data['decision_cases'][0]['input']); c['review'].update(passed=False,feasible=False)
        control('missing mandatory review',decide(c),'BLOCKED')
        c=deepcopy(data['budget_cases'][0]); c['workers'][0]['units']=31
        control('one-unit over collection capacity',admit(c['resources'],c['workers'],c['purpose']),False)
        for prefix,name in [('E08','eight candidate effort steps'),('K09','nine cost categories')]:
            altered=text.replace('| '+prefix+' |','| REMOVED |',1)
            failed=[r['check'] for r in check_docs(altered,set(baseline)|local,local,baseline) if r['result']=='FAIL']
            control('remove '+prefix,name in failed,True)
    ok=all(c['result']=='PASS' for c in checks+controls)
    result={'stage':6,'executed_at':datetime.now(timezone.utc).isoformat(),'parent':PARENT,'input_mode':mode,
            'verification_kind':'document integrity and synthetic policy/accounting/revision checks, not research-agent performance',
            'baseline_inventory':baseline,'checks':checks,'negative_controls':controls,
            'file_blobs':{PREFIX+name:git_blob((root/(PREFIX+name)).read_bytes()) for name in NAMES[:3]},
            'result':'PASS' if ok else 'FAIL'}
    (root/(PREFIX+NAMES[3])).write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps({'result':result['result'],'checks':len(checks),'negative_controls':len(controls),
                      'failures':[r for r in checks+controls if r['result']=='FAIL']},indent=2))
    return 0 if ok else 1

if __name__=='__main__':
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,subprocess.CalledProcessError) as error:
        print(f'Validation could not complete: {error}',file=sys.stderr)
        raise SystemExit(2)
