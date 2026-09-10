#!/usr/bin/env python3
"""Inventory/link/control checks; never a semantic research or installation judge."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, re
from datetime import datetime, timezone
from pathlib import Path

PREFIX='2026-09-10-stage-13-'
ACCEPTED={
 '2026-09-07-deep-research-skills-new-project-bootstrap-process.md',
 '2026-09-10-stage-02-quality-dimensions.md', '2026-09-10-stage-02-failure-taxonomy.md',
 '2026-09-10-stage-03-question-evidence-claim-model.md',
 '2026-09-10-stage-10-command-contracts.md', '2026-09-10-stage-11-profiles.json',
 '2026-09-10-stage-11-comparisons.md', '2026-09-10-stage-12-progressive-examples.md'}

def checks(text: str, research: str, cases: dict, fixture_source: str) -> dict:
    expected_examples={f'EX-L{l}-{i:02}' for l in range(1,6) for i in range(1,4)}
    outputs={1:'Benchmark architecture',2:'Domain quality',3:'Case, submission',4:'Priority regression',
             5:'Progressive-example',6:'Pack differential',7:'Regression policy',8:'Release and maturity'}
    result={
      'eight output sections': all(f'## {n}. {value}' in text for n,value in outputs.items()),
      'ten layer rows': set(re.findall(r'^\| (L\d\d) ',text,re.M))=={f'L{i:02}' for i in range(1,11)},
      'sixteen quality rows':set(re.findall(r'^\| (K\d\d) ',text,re.M))=={f'K{i:02}' for i in range(1,17)},
      'twelve priority rows':set(re.findall(r'^\| (FX\d\d) ',text,re.M))=={f'FX{i:02}' for i in range(1,13)},
      'fifteen individual example rows':set(re.findall(r'^\| (EX-L\d-\d\d) ',text,re.M))==expected_examples,
      'five external families': all(n in research for n in ('BrowseComp','DeepResearch Bench','BrowseComp-Plus','ResearchRubrics','FINDER / DEFT')),
      'seven primary source entries':set(re.findall(r'(?:## |\*\*)(S\d\d)[:.]',research))=={f'S{i:02}' for i in range(1,8)},
      'two disjoint holdout contracts': {h['id'] for h in cases.get('heldout',[])}=={'HO01','HO02'},
      'holdout prompts and sourced criteria':all(h.get('prompt','').startswith('Use ') and h.get('source',{}).get('url','').startswith('https://') and len(h.get('oracle',[]))==3 and h.get('judge_separation') and h.get('repair') for h in cases.get('heldout',[])),
      'two profile pairs': {p['profile'] for p in cases.get('pack_differential_suite',[])}=={'scholarly-evidence','open-source-ecosystem'},
      'behavioural differential criteria':all(len(p.get('differential_criteria',[]))==3 and all(c.get('mandatory') and len(c.get('expected',''))>30 for c in p.get('differential_criteria',[])) and len(p.get('nonregression',[]))==7 for p in cases.get('pack_differential_suite',[])),
      'unexecuted agent results not invented':all(p.get('observed_installed_result') is None for p in cases.get('pack_differential_suite',[])) and all(h.get('execution_state')=='not run through a candidate agent' for h in cases.get('heldout',[])),
      'six support-case responsibilities':all(n in fixture_source for n in ['TM02','TM03','BG01','BG02','PR01','AU01']),
      'four-layer separate detection':all(n in fixture_source for n in ('orthogonality','scorer_mutation_controls','retrieval','evidence','citations','synthesis')),
      'limits stated':all(n in text for n in ('not live-agent scores','not a generic natural-language entailment','not secret','same question','NOT APPLICABLE')),
      'conformance rows':set(re.findall(r'^\| (R\d\d) \|',text.split('## Verification, limitations and conformance',1)[-1],re.M))=={f'R{i:02}' for i in range(1,11)},
    }
    local={PREFIX+s for s in ('evaluation-design.md','benchmark-research.md','case-contracts.json','fixture-check.py','verification.json','document-check.py','document-verification.json')}
    links=re.findall(r'\]\(([^)]+)\)',text+'\n'+research)
    result['relative link closure']=all(x.split('#')[0] in local|ACCEPTED for x in links if not x.startswith(('https://','http://','#')))
    return result

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);args=ap.parse_args()
    root=Path(__file__).resolve().parent
    source_names=['evaluation-design.md','benchmark-research.md','case-contracts.json','fixture-check.py']
    raw={n:(root/(PREFIX+n)).read_text() for n in source_names}
    inputs=(raw[source_names[0]],raw[source_names[1]],json.loads(raw[source_names[2]]),raw[source_names[3]])
    before=hashlib.sha256(json.dumps(raw,sort_keys=True).encode()).hexdigest()
    observed=checks(*inputs)
    negatives=[]
    for name,old,new in [('missing layer','| L04 Citation','| X04 Citation'),('missing quality','| K06 Independent','| X06 Independent'),('missing example','| EX-L5-03 |','| EX-X5-03 |'),('broken link','2026-09-10-stage-11-profiles.json','missing-file.json')]:
        altered=inputs[0].replace(old,new)
        verdict=checks(altered,*inputs[1:])
        negatives.append({'mutation':name,'detected':[k for k,v in verdict.items() if not v],'result':'PASS' if not all(verdict.values()) else 'FAIL'})
    for name,mutator in [('holdout removed',lambda c:c['heldout'].pop()),('prompt removed',lambda c:c['heldout'][0].update(prompt='')),('cosmetic pair',lambda c:c['pack_differential_suite'][0].update(differential_criteria=[])),('invented run',lambda c:c['pack_differential_suite'][0].update(observed_installed_result='PASS'))]:
        c=copy.deepcopy(inputs[2]);mutator(c);verdict=checks(inputs[0],inputs[1],c,inputs[3])
        negatives.append({'mutation':name,'detected':[k for k,v in verdict.items() if not v],'result':'PASS' if not all(verdict.values()) else 'FAIL'})
    after=hashlib.sha256(json.dumps({n:(root/(PREFIX+n)).read_text() for n in source_names},sort_keys=True).encode()).hexdigest()
    result={'stage':13,'kind':'executed document inventories and corrupted-control detection; not semantic agent quality','checked_at':datetime.now(timezone.utc).isoformat(),
            'checks':{k:'PASS' if v else 'FAIL' for k,v in observed.items()},'negative_controls':negatives,
            'input_preservation':'PASS' if before==after else 'FAIL',
            'files':{PREFIX+n:hashlib.sha256(raw[n].encode()).hexdigest() for n in source_names}}
    result['result']='PASS' if all(observed.values()) and all(n['result']=='PASS' for n in negatives) and before==after else 'FAIL'
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':result['result'],'checks':len(observed),'negative_controls':len(negatives),'failures':[k for k,v in observed.items() if not v]}))
    return 0 if result['result']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
