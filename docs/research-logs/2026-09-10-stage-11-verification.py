#!/usr/bin/env python3
"""Validate Stage 11 design records and synthetic policy controls, not provider quality."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath, PureWindowsPath

PREFIX = '2026-09-10-stage-11-'
DIMENSIONS = {'source ecology','search strategy','inclusion / exclusion rules','source appraisal','research methods','synthesis structure','quality criteria','reporting conventions'}
COMMANDS = {'frame','plan','discover','extract-evidence','analyse-evidence','follow-up-search','synthesise','refresh','audit','diagnose-research-failure'}
PRECEDENCE = ['explicit research instructions','approved / locked research decisions','selected Extension Pack','core Deep Research defaults']
FAMILIES = ['scholarly-evidence','market-intelligence','technology-landscape','open-source-ecosystem','trend-and-signal','creative-reference-research','investigative-osint']
INPUTS = {
 '2026-09-07-deep-research-skills-new-project-bootstrap-process.md':'8ff62c92bada2861ece3684a9e73a83da75d9d94',
 '2026-09-10-stage-10-core-skills.md':'4e2dddcd703c5aca8c4d396fcfac71144d5ca811',
 '2026-09-10-stage-10-command-contracts.md':'cadc18a61efcafb21f55f6cfb870b8c4f230cdcb',
}

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def selection(requested: list[str], known: set[str], compatible: bool = True) -> str:
    if not requested: return 'CORE'
    if len(requested)!=1 or requested[0] not in known or not compatible: return 'BLOCKED'
    return requested[0]

def value(explicit, locked, pack, core, reopen=False):
    if explicit is not None and locked is not None and explicit!=locked and not reopen:
        return 'BLOCKED'
    if explicit is not None: return explicit
    if locked is not None: return locked
    if pack is not None: return pack
    return core

def local_path(path: str) -> bool:
    p=PurePosixPath(path)
    return bool(path) and not p.is_absolute() and not PureWindowsPath(path).is_absolute() and '..' not in p.parts and '\\' not in path and ':' not in path

def outputs(text: str) -> dict[str,str]:
    matches=list(re.finditer(r'^## (SCH core|SCH pack|OSS core|OSS pack)\n',text,re.M))
    result={}
    for i,m in enumerate(matches):
        stop=matches[i+1].start() if i+1<len(matches) else text.index('\n## Performed review')
        result[m.group(1)]=text[m.start():stop]
    return result

def check(docs: dict[str,str], data: dict) -> dict[str,bool]:
    main=docs['extension-packs.md']; proto=docs['comparison-protocol.md']; comp=docs['comparisons.md']; src=docs['sources.md']
    profiles=data.get('profiles',[])
    out=outputs(comp)
    known_sources=set(re.findall(r'\bS\d{2}\b',src))
    results={}
    results['six complete output responsibilities']=all(f'## {i}.' in main for i in range(1,7))
    results['seven candidate dispositions']=all(re.search(r'^\| '+re.escape(f)+r' \|',main,re.M) for f in FAMILIES)
    results['two selected profiles']=len(profiles)==2 and {x.get('id') for x in profiles}=={'scholarly-evidence','open-source-ecosystem'}
    results['all eight dimensions']=all(set(x.get('dimensions',{}))==DIMENSIONS and all(len(v)>35 for v in x['dimensions'].values()) for x in profiles)
    results['operational command effects']=all(len(x.get('effects',[]))>=1 and all(e.get('command') in COMMANDS and len(e.get('change',''))>40 and len(e.get('observable',''))>30 for e in x['effects']) for x in profiles)
    results['precedence and core preservation']=all(x.get('precedence')==PRECEDENCE and len(x.get('preserved',[]))==7 and 'explicit' in x.get('activation','') for x in profiles)
    results['authoring contract twelve steps']=all(re.search(r'^\| A'+f'{i:02}'+r' \|',main,re.M) for i in range(1,13))
    results['evaluation sixteen cases']=all(re.search(r'^\| E'+f'{i:02}'+r' \|',main,re.M) for i in range(1,17))
    prompts=re.findall(r'```text\n(.*?)\n```',proto,re.S)
    results['four complete condition prompts']=len(prompts)==4 and all(len(t.split())>=95 and 'source' in t.lower() and 'Write a separate' in t and 'Do not' in t for t in prompts)
    results['all actual output conditions']=set(out)=={'SCH core','SCH pack','OSS core','OSS pack'} and all(len(t.split())>=170 for t in out.values())
    results['baseline does not hide known findings']='seventeen' in out.get('SCH core','') and 'ten models' in out.get('SCH core','') and '85.6%' in out.get('SCH core','') and 'or True' in out.get('OSS core','')
    results['scholarly observable consequences']='one research-work identity' in out.get('SCH pack','') and 'twenty-seven' in out.get('SCH pack','') and 'acceptance criterion unset' in out.get('SCH pack','')
    results['repository observable consequences']='Python >=3.10' in out.get('OSS pack','') and 'Python 3.11' in out.get('OSS pack','') and 'Inject a controlled non-token' in out.get('OSS pack','')
    results['no fabricated runtime or independent trial']=all('not' in t.lower() for t in out.values()) and 'not blinded' in proto and 'not a demonstrated ready-to-deploy' in comp and 'no executed engine results' in comp
    referenced=set(re.findall(r'\bS\d{2}\b',main+proto+comp+json.dumps(data)))
    results['source identifier closure']=referenced<=known_sources and {f'S{i:02}' for i in range(1,18)}<=known_sources
    results['precise pinned repository']='1b7d2e80db9faa586165c60e09096dbbfd483a64' in proto and '279dbffd9e49e07962fb4e1cfeff79e45adc43e9' in src
    results['design versus installation status']=all('not installed' in x.get('status','') for x in profiles) and 'design projection' in main and 'pack-root-local' in main
    # Earlier references were remotely read at the accepted predecessor; this check does not claim a local clone exists.
    allowed={PREFIX+n for n in docs}|{PREFIX+'profiles.json',PREFIX+'verification.py',PREFIX+'verification.json'}|set(INPUTS)
    links=re.findall(r'\]\(([^)]+)\)',main+proto+comp+src)
    local=[x.split('#')[0] for x in links if not re.match(r'https?://',x)]
    results['local document and accepted-input link closure']=all(not x or (local_path(x) and x in allowed) for x in local)
    results['all profile showcase references']=all(local_path(x['showcase']['prompt_location'].split('#')[0]) and x['showcase']['prompt_location'].split('#')[0]==PREFIX+'comparison-protocol.md' and x['showcase']['output_location'].split('#')[0]==PREFIX+'comparisons.md' for x in profiles)
    results['substantive recorded review']='## Performed review' in comp and 'No artificially defective baseline' in comp and 'causal superiority' in comp
    return results

def policy_cases():
    known={'scholarly-evidence','open-source-ecosystem'}
    cases=[
      ('unrequested',selection([],known),'CORE'),
      ('scholarly requested',selection(['scholarly-evidence'],known),'scholarly-evidence'),
      ('repository requested',selection(['open-source-ecosystem'],known),'open-source-ecosystem'),
      ('unknown selection',selection(['unknown'],known),'BLOCKED'),
      ('incompatible',selection(['scholarly-evidence'],known,False),'BLOCKED'),
      ('two selections',selection(sorted(known),known),'BLOCKED'),
      ('explicit field',value('local',None,'web','core'),'local'),
      ('locked field',value(None,'approved','other','core'),'approved'),
      ('pack default',value(None,None,'pack','core'),'pack'),
      ('core default',value(None,None,None,'core'),'core'),
      ('ambiguous lock conflict',value('new','old','pack','core'),'BLOCKED'),
      ('authorised reopening',value('new','old','pack','core',True),'new'),
      ('false remains explicit',value(False,None,True,True),False),
      ('valid local path',local_path('references/method.md'),True),
      ('parent traversal',local_path('../private.md'),False),
      ('absolute path',local_path('/tmp/input'),False),
      ('windows absolute',local_path('C:\\private.txt'),False),
      ('URL is not bundled entry',local_path('https://example.com/code'),False),
    ]
    return [{'case':n,'observed':a,'expected':b,'result':'PASS' if a==b else 'FAIL','kind':'synthetic design policy'} for n,a,b in cases]

def run(folder: Path, negatives: bool):
    names=['extension-packs.md','comparison-protocol.md','comparisons.md','sources.md']
    docs={n:(folder/(PREFIX+n)).read_text(encoding='utf-8') for n in names}
    data=json.loads((folder/(PREFIX+'profiles.json')).read_text())
    before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.glob(PREFIX+'*') if not p.name.endswith('verification.json')}
    checks=check(docs,data); policies=policy_cases(); controls=[]
    if negatives:
        mutations=[
          ('missing output section',lambda d,x:d.update({'extension-packs.md':d['extension-packs.md'].replace('## 2. Format','## Removed Format')})),
          ('missing family',lambda d,x:d.update({'extension-packs.md':d['extension-packs.md'].replace('| trend-and-signal |','| other-name |')})),
          ('missing dimension',lambda d,x:x['profiles'][0]['dimensions'].pop('source ecology')),
          ('unknown command',lambda d,x:x['profiles'][0]['effects'][0].update({'command':'deploy'})),
          ('wrong precedence',lambda d,x:x['profiles'][0]['precedence'].reverse()),
          ('missing authoring step',lambda d,x:d.update({'extension-packs.md':d['extension-packs.md'].replace('| A10 |','| A00 |')})),
          ('missing evaluation case',lambda d,x:d.update({'extension-packs.md':d['extension-packs.md'].replace('| E16 |','| E00 |')})),
          ('missing exact prompt',lambda d,x:d.update({'comparison-protocol.md':d['comparison-protocol.md'].replace('```text','```example',1)})),
          ('baseline suppressed source fact',lambda d,x:d.update({'comparisons.md':d['comparisons.md'].replace('seventeen','many',1)})),
          ('baseline suppressed code warning',lambda d,x:d.update({'comparisons.md':d['comparisons.md'].replace('or True','unknown condition',1)})),
          ('no actual scholarly consequence',lambda d,x:d.update({'comparisons.md':d['comparisons.md'].replace('acceptance criterion unset','acceptance criterion accepted')})),
          ('unresolved source',lambda d,x:d.update({'comparisons.md':d['comparisons.md']+'\n[S99]'})),
          ('false installed status',lambda d,x:x['profiles'][0].update({'status':'installed and operational'})),
          ('escaping showcase path',lambda d,x:x['profiles'][0]['showcase'].update({'prompt_location':'../secret.md'})),
          ('broken local reference',lambda d,x:d.update({'extension-packs.md':d['extension-packs.md']+'\n[missing](missing.md)'})),
        ]
        for name,mutate in mutations:
            d=copy.deepcopy(docs);x=copy.deepcopy(data);mutate(d,x)
            try: failed=[k for k,v in check(d,x).items() if not v]
            except (KeyError,ValueError,TypeError) as e: failed=[type(e).__name__]
            controls.append({'mutation':name,'detected_by':failed,'result':'PASS' if failed else 'FAIL'})
    after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.glob(PREFIX+'*') if not p.name.endswith('verification.json')}
    checks['validation preserves submitted files']=before==after
    manifest={p.name:{'bytes':p.stat().st_size,'git_blob':git_blob(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in folder.glob(PREFIX+'*') if not p.name.endswith('verification.json')}
    condition_hashes={k:hashlib.sha256(v.encode()).hexdigest() for k,v in outputs(docs['comparisons.md']).items()}
    passed=all(checks.values()) and all(x['result']=='PASS' for x in policies+controls)
    return {'stage':11,'checked_at':datetime.now(timezone.utc).isoformat(),'kind':'design-document, source-backed output integrity and synthetic policy verification; no installed/provider test','parent':'27b2714b306cab0362e69af21deddd2d3106c6f7','accepted_remote_input_blobs':INPUTS,'checks':{k:'PASS' if v else 'FAIL' for k,v in checks.items()},'policy_cases':policies,'negative_controls':controls,'output_sha256':condition_hashes,'files':manifest,'result':'PASS' if passed else 'FAIL'}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--negative-controls',action='store_true');ap.add_argument('--output',type=Path);args=ap.parse_args()
    result=run(Path(__file__).resolve().parent,args.negative_controls)
    payload=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    if args.output: args.output.write_text(payload,encoding='utf-8')
    print(json.dumps({'result':result['result'],'checks':len(result['checks']),'policy_cases':len(result['policy_cases']),'negative_controls':len(result['negative_controls']),'failed':[k for k,v in result['checks'].items() if v!='PASS']}))
    raise SystemExit(0 if result['result']=='PASS' else 1)
