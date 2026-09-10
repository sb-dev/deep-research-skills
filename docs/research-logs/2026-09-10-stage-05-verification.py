#!/usr/bin/env python3
"""Validate Stage 5 design records and synthetic contract cases, not agent quality."""
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

PARENT = '4ad81f95f4d7a603c27d3f1ded7e9af215ccdfe7'
PREFIX = 'docs/research-logs/2026-09-10-stage-05-'
FILES = {'workflow':'workflow-and-artifacts.md','artifacts':'artifact-contracts.md',
         'cases':'contract-cases.json','script':'verification.py','result':'verification.json'}
CONCERNS = ['Purpose','Creator','Consumer','Authoritative fields','Update behaviour',
            'Approval / review behaviour','Retention','Smallest repair scope']
CANDIDATES = ['brief','frame questions','plan research','define source strategy','discover broadly',
              'triage','retrieve','extract evidence','deduplicate underlying sources/events/studies',
              'map evidence to questions / claims','analyse contradictions and alternatives','identify gaps',
              'run targeted follow-up research','synthesise','audit material claims and citations',
              'produce deliverable','record unresolved gaps / valid-as-of state']


def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def affected(dependencies: dict[str,list[str]], changed: list[str]) -> set[str]:
    result=set(changed)
    while True:
        more={target for target,inputs in dependencies.items() if result.intersection(inputs)}
        if more <= result:
            return result
        result |= more


def violations(case: dict[str,Any]) -> list[str]:
    """Check a bounded fixture contract; boolean assertions are fixture premises, not measured facts."""
    errors:set[str]=set()
    brief=case.get('brief',{})
    operation=case.get('operation',{})
    if not brief.get('authorised'): errors.add('G01-brief-authority')
    for field,code in [('within_scope','scope'),('processor_authorised','processor-authority'),
                       ('expense_authorised','expense-authority'),('bounded','unbounded-operation')]:
        if not operation.get(field): errors.add('G01-'+code)
    action=case.get('action')
    if action=='acquire': return sorted(errors)
    if action not in {'issue','confirm-delivery','close-repair'}:
        errors.add('unknown-action')
    sources=case.get('sources',{}); evidence=case.get('evidence',{}); claims=case.get('claims',{})
    for eid,e in evidence.items():
        source=sources.get(e.get('source'))
        if source is None: errors.add('T02-source-reference'); continue
        if not e.get('locator') or not e.get('inspected') or source.get('access')=='metadata-only':
            errors.add('T03-inspected-support')
        if source.get('revision')!=e.get('source_revision'): errors.add('T03-source-revision')
    for cid,c in claims.items():
        if any(e not in evidence for e in c.get('evidence',[])): errors.add('T02-evidence-reference')
        if any(p not in claims for p in c.get('premises',[])): errors.add('T02-premise-reference')
        if not c.get('evidence') and not c.get('premises'): errors.add('T06-empty-support')
        if not c.get('contrary_status'): errors.add('T05-contrary-status')
    # Cycle detection concerns only declared premise links, not a universal claim graph.
    def visit(cid:str,stack:set[str],done:set[str])->None:
        if cid in stack: errors.add('T06-circular-support'); return
        if cid in done or cid not in claims: return
        for parent in claims[cid].get('premises',[]): visit(parent,stack|{cid},done)
        done.add(cid)
    done:set[str]=set()
    for cid in claims: visit(cid,set(),done)
    report=case.get('report',{}); review=case.get('review',{})
    for q in brief.get('required_questions',[]):
        state=case.get('questions',{}).get(q)
        if state not in {'answered','limitation'}: errors.add('G02-question-coverage')
        if state=='limitation' and not brief.get('limited_output_authorised'):
            errors.add('G02-unapproved-limitation')
    for gap in case.get('gaps',[]):
        if gap.get('state')=='resolved' and not gap.get('evidence'): errors.add('G02-gap-resolution')
        if gap.get('material') and gap.get('state')!='resolved':
            if not (gap.get('state')=='accepted-limitation' and gap.get('decision') and brief.get('limited_output_authorised')):
                errors.add('G02-material-gap')
            if gap.get('id') not in report.get('gap_ids',[]): errors.add('G02-hidden-gap')
    if not report.get('audience_authorised'): errors.add('G03-disclosure-authority')
    if review.get('result')!='checked' or review.get('report_revision')!=report.get('revision'):
        errors.add('G03-report-review')
    if review.get('required_specialist') and not review.get('specialist_completed'):
        errors.add('G03-specialist-review')
    for cid in report.get('material_claims',[]):
        c=claims.get(cid)
        if c is None: errors.add('T02-claim-reference'); continue
        if c.get('support') in {'unsupported','unassessed'}: errors.add('G03-unsupported-assertion')
        if c.get('support') in {'qualified','contested'} and (not c.get('qualifier') or report.get('qualifiers',{}).get(cid)!=c.get('qualifier')):
            errors.add('T07-qualification-loss')
        if review.get('claim_revisions',{}).get(cid)!=c.get('revision'): errors.add('G03-claim-review')
        for eid in c.get('evidence',[]):
            if eid in evidence and review.get('evidence_revisions',{}).get(eid)!=evidence[eid].get('revision'):
                errors.add('G03-evidence-review')
    if action=='confirm-delivery':
        delivery=case.get('delivery',{}); receipt=delivery.get('receipt') or {}
        if delivery.get('status')!='confirmed' or not receipt.get('observed') or receipt.get('report_revision')!=report.get('revision'):
            errors.add('G04-unverified-delivery')
    if action=='close-repair':
        repair=case.get('repair',{}); dependencies=repair.get('dependencies',{})
        closure=affected(dependencies,repair.get('changed',[]))
        if closure != set(repair.get('expected_affected',[])): errors.add('G05-dependency-closure')
        if not closure <= set(repair.get('rechecked',[])): errors.add('G05-dependent-review')
        before=repair.get('before',{}); after=repair.get('after',{})
        if set(before)!=set(after) or any(after.get(k)!=v for k,v in before.items() if k not in closure):
            errors.add('G05-preservation')
    return sorted(errors)


def document_checks(texts:dict[str,str],baseline:dict[str,str],local_paths:set[str])->list[dict[str,Any]]:
    checks=[]
    def add(name:str,ok:bool,evidence:Any)->None:
        checks.append({'check':name,'result':'PASS' if ok else 'FAIL','evidence':evidence})
    workflow=texts['workflow']; artifacts=texts['artifacts']
    add('five required output responsibilities',all(f'## {n}. {h}' in workflow for n,h in enumerate(
        ['Workflow map','Artifact architecture','State and decision semantics','Handoff contracts','Repair routes'],1)),
        'Five source-defined responsibilities, not only file existence')
    ops=re.findall(r'^\| (W\d{2}) ([^|]+)\|',workflow,re.M)
    add('eight complete workflow operation rows',[x[0] for x in ops]==[f'W{i:02}' for i in range(1,9)],ops)
    candidates=re.findall(r'^\| (C\d{2}) \| ([^|]+) \| (.+) \|$',workflow,re.M)
    add('all seventeen source candidate operations disposed',
        [x[0] for x in candidates]==[f'C{i:02}' for i in range(1,18)] and
        [x[1].strip() for x in candidates]==CANDIDATES and all('W0' in x[2] for x in candidates),candidates)
    sections=list(re.finditer(r'^## (A\d{2}): (.+)$',artifacts,re.M))
    counts={}; problem=[]
    for i,m in enumerate(sections):
        section=artifacts[m.end():sections[i+1].start() if i+1<len(sections) else len(artifacts)]
        rows=re.findall(r'^\| ([^|]+) \| ([^|]+) \|$',section,re.M)
        rows=[(key.strip(),value.strip()) for key,value in rows if key.strip() in CONCERNS]
        counts[m[1]]=len(rows)
        if [key for key,_ in rows]!=CONCERNS or any(len(value.split())<9 for _,value in rows): problem.append(m[1])
    add('eleven artifact contracts and all eighty-eight concerns',
        [m[1] for m in sections]==[f'A{i:02}' for i in range(1,12)] and sum(counts.values())==88 and not problem,
        {'counts':counts,'invalid':problem})
    dispositions=re.findall(r'^\| (A\d{2}) \| `([^`]+)` \|',artifacts,re.M)
    add('all eleven candidate artifact dispositions',[x[0] for x in dispositions]==[f'A{i:02}' for i in range(1,12)],dispositions)
    handoffs=re.findall(r'^\| (H\d{2}) \|',workflow,re.M)
    repairs=re.findall(r'^\| (F\d{2}) \|',workflow,re.M)
    add('handoff and repair inventories',handoffs==[f'H{i:02}' for i in range(1,7)] and repairs==[f'F{i:02}' for i in range(1,14)],{'handoffs':handoffs,'repairs':repairs})
    unknown=[]
    for category,limit in [('W',8),('A',11),('H',6),('F',13),('C',17)]:
        for value in re.findall(r'\b'+category+r'(\d{2})\b',workflow+'\n'+artifacts):
            if not 1<=int(value)<=limit: unknown.append(category+value)
    add('local contract references resolve',not unknown,unknown)
    missing=[]; tables=0; shape=[]
    existing=set(baseline)|local_paths
    for name,text in [('workflow',workflow),('artifacts',artifacts)]:
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
            if '://' in target or target.startswith('#'): continue
            candidate='docs/research-logs/'+target.split('#')[0]
            if candidate not in existing: missing.append({'from':name,'target':target})
        expected=None; fenced=False
        for number,line in enumerate(text.splitlines(),1):
            if line.startswith('```'): fenced=not fenced
            if not fenced and line.startswith('|') and line.endswith('|'):
                count=len(re.split(r'(?<!\\)\|',line))-2
                if expected is None: expected=count; tables+=1
                elif count!=expected: shape.append({'file':name,'line':number,'expected':expected,'actual':count})
            else: expected=None
    add('documentation links resolve',not missing,missing)
    add('Markdown tables are rectangular',not shape,{'tables':tables,'errors':shape})
    # Report file may be generated only after the final checks, so it is excluded from exact input delta.
    expected={PREFIX+FILES[k] for k in ['workflow','artifacts','cases','script']}
    actual=local_paths-set(baseline)-{PREFIX+FILES['result']}
    add('stage-only new files',actual==expected,{'expected':sorted(expected),'actual':sorted(actual)})
    semantic=re.findall(r'^\| (R\d{2}) \|.*\| (PASS|FAIL|BLOCKED|NOT APPLICABLE) \|$',workflow,re.M)
    add('ten conformance entries and honest evidence labels',
        semantic==[(f'R{i:02}','PASS') for i in range(1,11)] and 'synthetic' in workflow and 'not live installed-skill runs' in workflow,
        semantic)
    return checks


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-manifest',type=Path)
    parser.add_argument('--negative-controls',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    if args.baseline_manifest:
        manifest=json.loads(args.baseline_manifest.read_text(encoding='utf-8'))
        if manifest.get('parent')!=PARENT: raise ValueError('Unexpected parent inventory')
        baseline=manifest['files']; mode='new local files plus previously inspected remote inventory'
    else:
        run=subprocess.run(['git','ls-tree','-r',PARENT],cwd=root,text=True,capture_output=True,check=True)
        baseline={line.split('\t')[1]:line.split()[2] for line in run.stdout.splitlines()}
        mode='Git parent tree and local files'
    texts={key:(root/(PREFIX+FILES[key])).read_text(encoding='utf-8') for key in ['workflow','artifacts']}
    paths={str(path.relative_to(root)) for path in root.rglob('*') if path.is_file() and '.git' not in path.parts and '__pycache__' not in path.parts}
    paths|={PREFIX+FILES['result']} # Declared output location, not a claim that the report existed before running.
    checks=document_checks(texts,baseline,paths)
    data=json.loads((root/(PREFIX+FILES['cases'])).read_text(encoding='utf-8'))
    results=[{'id':case['id'],'expected':case['expected_violations'],'observed':violations(case),
              'result':'PASS' if case.get('synthetic') is True and violations(case)==case['expected_violations'] else 'FAIL'} for case in data['cases']]
    checks.append({'check':'six synthetic gate and repair cases','result':'PASS' if len(results)==6 and all(x['result']=='PASS' for x in results) else 'FAIL','evidence':results})
    controls=[]
    if args.negative_controls:
        def mutate(name,case,index,update,expected):
            value=deepcopy(case[index]); update(value); observed=violations(value)
            controls.append({'mutation':name,'expected_failure':expected,'actual_failures':observed,'result':'PASS' if expected in observed else 'FAIL'})
        cases=data['cases']
        for name,index,fn,code in [
          ('unapproved brief',0,lambda c:c['brief'].update(authorised=False),'G01-brief-authority'),
          ('unbounded action',0,lambda c:c['operation'].update(bounded=False),'G01-unbounded-operation'),
          ('unseen source',0,lambda c:c['sources']['S1'].update(access='metadata-only'),'T03-inspected-support'),
          ('stale review',0,lambda c:c['review'].update(report_revision='old'),'G03-report-review'),
          ('unsupported finding',0,lambda c:c['claims']['C1'].update(support='unsupported'),'G03-unsupported-assertion'),
          ('lost qualification',1,lambda c:c['report'].update(qualifiers={}),'T07-qualification-loss'),
          ('gap closed by attempt',1,lambda c:c['gaps'][0].update(state='resolved',evidence=[]),'G02-gap-resolution'),
          ('hidden material gap',1,lambda c:c['report'].update(gap_ids=[]),'G02-hidden-gap'),
          ('missing specialist review',0,lambda c:c['review'].update(required_specialist=True),'G03-specialist-review'),
          ('unverified delivery',2,lambda c:c['delivery'].update(receipt=None),'G04-unverified-delivery'),
          ('unrelated evidence changed',3,lambda c:c['repair']['after'].update(E2='unnecessary replacement'),'G05-preservation'),
          ('dependent review skipped',3,lambda c:c['repair'].update(rechecked=['E1']),'G05-dependent-review')]:
            mutate(name,cases,index,fn,code)
        for name,key,old,new,check in [
          ('candidate omitted','workflow','| C17 | record unresolved gaps / valid-as-of state |','| X17 | record unresolved gaps / valid-as-of state |','all seventeen source candidate operations disposed'),
          ('artifact concern omitted','artifacts','| Retention |','| Deleted concern |','eleven artifact contracts and all eighty-eight concerns')]:
            altered=dict(texts); altered[key]=altered[key].replace(old,new,1)
            failures=[x['check'] for x in document_checks(altered,baseline,paths) if x['result']=='FAIL']
            controls.append({'mutation':name,'expected_failure':check,'actual_failures':failures,'result':'PASS' if check in failures else 'FAIL'})
    ok=all(x['result']=='PASS' for x in checks+controls)
    result={'stage':5,'executed_at':datetime.now(timezone.utc).isoformat(),'parent':PARENT,'input_mode':mode,
      'verification_kind':'document integrity and synthetic design-contract checks, not research quality or installed behaviour',
      'baseline_inventory':baseline,'checks':checks,'negative_controls':controls,
      'file_blobs':{PREFIX+FILES[k]:blob((root/(PREFIX+FILES[k])).read_bytes()) for k in ['workflow','artifacts','cases','script']},
      'result':'PASS' if ok else 'FAIL'}
    (root/(PREFIX+FILES['result'])).write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps({'result':result['result'],'checks':len(checks),'negative_controls':len(controls),'failures':[x for x in checks+controls if x['result']=='FAIL']},indent=2))
    return 0 if ok else 1

if __name__=='__main__':
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,subprocess.CalledProcessError) as error:
        print(f'Validation could not complete: {error}',file=sys.stderr)
        raise SystemExit(2)
