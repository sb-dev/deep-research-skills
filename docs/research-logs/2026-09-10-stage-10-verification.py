#!/usr/bin/env python3
"""Validate Stage 10 design documents, not installed skills or agent performance."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

PRODUCTION = ['frame','plan','build-source-strategy','discover','triage-sources','retrieve',
              'extract-evidence','deduplicate','triangulate','analyse-contradictions',
              'identify-gaps','follow-up-search','synthesise','refresh']
EVALUATION = ['audit-source-quality','audit-source-independence','audit-coverage','audit-claims',
              'audit-citations','audit-freshness','audit-contradictions','audit-uncertainty',
              'audit-reproducibility','diagnose-research-failure']
SKILLS = ['deep-research','research-evaluate','research-extension-pack-creator']
SELECTED = [(SKILLS[0],s) for s in ['frame','plan','discover','extract-evidence','analyse-evidence',
            'follow-up-search','synthesise','refresh']] + [(SKILLS[1],s) for s in ['audit','diagnose-research-failure']] + [(SKILLS[2],'create-pack')]
FIELDS = ['Purpose','Inputs and preconditions','Operation','Outputs and write scope',
          'Completion and review','Failure and smallest repair','Independent use and evaluation reason','Example invocation']
FILES = ['2026-09-10-stage-10-core-skills.md','2026-09-10-stage-10-command-contracts.md','2026-09-10-stage-10-skill-outlines.md']
BASE_LINKS = {'2026-09-07-deep-research-skills-new-project-bootstrap-process.md',
 '2026-09-10-stage-01-project-goal-and-boundary.md','2026-09-10-stage-02-method-comparison.md',
 '2026-09-10-stage-03-question-evidence-claim-model.md','2026-09-10-stage-04-source-ecology.md',
 '2026-09-10-stage-05-workflow-and-artifacts.md','2026-09-10-stage-05-artifact-contracts.md',
 '2026-09-10-stage-06-effort-and-stopping.md','2026-09-10-stage-07-ai-tool-landscape.md',
 '2026-09-10-stage-08-execution-layer.md','2026-09-10-stage-09-gap-analysis.md',
 '2026-09-10-stage-09-publication-receipt.md'}

def check(docs):
    log, contracts, outlines = [docs[k] for k in FILES]
    result={}
    def put(name, condition): result[name]='PASS' if condition else 'FAIL'
    headings=['Skill responsibility map','Command selection and contracts','Self-containment rules','Skill dependency rules','Initial SKILL.md outlines']
    put('five required outputs',all(f'## {i}. {h}' in log for i,h in enumerate(headings,1)))
    put('five design questions', all(log.count(f'**Q{i}:')==1 for i in range(1,6)))
    for label, expected in [('production',PRODUCTION),('evaluation',EVALUATION)]:
        actual=[m for m in re.findall(r'^\| ([a-z][a-z-]+) \|',log,re.M) if m in expected]
        put(label+' candidate dispositions',actual==expected)
    matches=list(re.finditer(r'^## ([a-z-]+): ([a-z-]+)$',contracts,re.M))
    names=[(m[1],m[2]) for m in matches]
    put('eleven distinct command contracts',names==SELECTED and len(set(names))==11)
    complete=True
    for i,m in enumerate(matches):
        block=contracts[m.end():matches[i+1].start() if i+1<len(matches) else contracts.find('## Audit focus semantics')]
        for f in FIELDS:
            found=re.findall(r'\*\*'+re.escape(f)+r'\.\*\* ([^\n]+)',block)
            complete &= len(found)==1 and len(found[0])>60
    put('all eight contract fields for each command',complete and len(matches)==11)
    index=re.findall(r'^\| `([^`]+)` \| `([^`]+)` \| \[[^]]+\]\(#[^)]+\) \|',contracts,re.M)
    put('command index matches contracts',index==SELECTED)
    yaml_blocks=re.findall(r'```yaml\n---\n(.*?)\n---\n```',outlines,re.S)
    valid=len(yaml_blocks)==3
    for expected,b in zip(SKILLS,yaml_blocks):
        name=re.search(r'^name: (.+)$',b,re.M)
        description=re.search(r'^description: (.+)$',b,re.M)
        compatibility=re.search(r'^compatibility: (.+)$',b,re.M)
        valid &= bool(name and name[1]==expected and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name[1]) and len(name[1])<=64)
        valid &= bool(description and 1<=len(description[1])<=1024 and compatibility and 1<=len(compatibility[1])<=500)
        valid &= '  contract-version: "0.1"' in b and 'allowed-tools:' not in b
    put('three valid initial outline frontmatters',valid)
    put('all eight workflow groups covered',all(f'| W{i:02} |' in log for i in range(1,9)))
    put('read-only independent review boundary','Do not modify A01–A10' in contracts and 'No mandatory dependency edge connects the three skill packages.' in log and 'producer self-check' in outlines)
    known=BASE_LINKS|set(FILES)|{'2026-09-10-stage-10-verification.py','2026-09-10-stage-10-verification.json'}
    bad=[]
    for filename,text in docs.items():
        outside=re.sub(r'```.*?```','',text,flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)',outside):
            if '://' not in target and not target.startswith('#') and target.split('#')[0] not in known:
                bad.append((filename,target))
    put('documentation links in inspected inventory',not bad)
    table_errors=[]
    for filename,text in docs.items():
        width=None
        for lineno,line in enumerate(text.splitlines(),1):
            if line.startswith('|'):
                n=len(line.split('|'))
                if width is None: width=n
                if n!=width: table_errors.append((filename,lineno))
            else: width=None
    put('Markdown table structure',not table_errors)
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); folder=Path(__file__).parent
    docs={f:(folder/f).read_text(encoding='utf-8') for f in FILES}
    checks=check(docs); controls=[]
    mutations=[
        ('missing candidate',FILES[0],'| refresh |','| removed |','production candidate dispositions'),
        ('missing evaluation scope',FILES[0],'| audit-freshness |','| removed |','evaluation candidate dispositions'),
        ('missing question',FILES[0],'**Q5:','**Removed:','five design questions'),
        ('wrong command name',FILES[1],'## deep-research: refresh','## deep-research: broken','eleven distinct command contracts'),
        ('missing contract field',FILES[1],'**Completion and review.**','**Removed field.**','all eight contract fields for each command'),
        ('invalid outline name',FILES[2],'name: research-evaluate','name: Research-Evaluate','three valid initial outline frontmatters'),
        ('missing read-only rule',FILES[1],'Do not modify A01–A10','Modify all inputs','read-only independent review boundary'),
        ('broken link',FILES[0],'(2026-09-10-stage-10-command-contracts.md)','(absent.md)','documentation links in inspected inventory'),
    ]
    for label,f,old,new,expected in mutations:
        if old not in docs[f]: raise ValueError('Control not applied: '+label)
        changed=docs.copy(); changed[f]=changed[f].replace(old,new,1)
        outcome=check(changed)
        controls.append({'mutation':label,'expected_failed_check':expected,'result':'PASS' if outcome[expected]=='FAIL' else 'FAIL'})
    report={'stage':10,'checked_at':datetime.now(timezone.utc).isoformat(),
      'verification_kind':'design-document and outline validation; no installed-agent execution',
      'parent':'318e61cd55b736730f0830b26334d677228eecb7','checks':checks,
      'negative_controls':controls,'counts':{'skills':3,'command_contracts':11,'production_candidates':14,'evaluation_candidates':10,'design_questions':5},
      'file_blobs':{f:hashlib.sha1(b'blob '+str(len((b:=t.encode()))).encode()+b'\0'+b).hexdigest() for f,t in docs.items()},
      'result':'PASS' if all(v=='PASS' for v in checks.values()) and all(c['result']=='PASS' for c in controls) else 'FAIL'}
    text=json.dumps(report,indent=2)+'\n'
    if args.output: args.output.write_text(text,encoding='utf-8')
    print(text); raise SystemExit(0 if report['result']=='PASS' else 1)

if __name__=='__main__': main()
