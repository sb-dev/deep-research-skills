#!/usr/bin/env python3
"""Check the Stage 3 design snapshot, not general research truth or agent quality.

Run from a complete stage checkout, or pass --baseline-manifest to check locally
created stage files against a separately inspected remote parent-file inventory.
The latter is explicitly not a local clone or an automatic remote hash check.
"""
from __future__ import annotations

import argparse
import copy
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Any

PREFIX = '2026-09-10-stage-03-'
DOC = PREFIX + 'question-evidence-claim-model.md'
EXAMPLES = PREFIX + 'traceability-examples.json'
REPORT = PREFIX + 'verification.json'
SCRIPT = PREFIX + 'verification.py'
PARENT = '5edbff2f7859c27c2a9689a30ada55972c0c83fd'
OUTPUTS = [
    'Research information model', 'Provenance rules', 'Source-quality dimensions',
    'Uncertainty model', 'Temporal-validity rules', 'Evidence-to-claim traceability contract',
]
FIELDS = {'BR': 10, 'SR': 12, 'EI': 6, 'CL': 7}
BRIEF = {'objective','downstream_use','scope','out_of_scope','questions','freshness',
         'source_restrictions','quality_threshold','effort_constraints','output_form'}


def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def trace_errors(trace: dict[str, Any]) -> list[str]:
    """Check selected explicit record invariants; no citation-entailment judgement."""
    errors: list[str] = []
    if not BRIEF <= trace.get('brief', {}).keys():
        errors.append('brief-concerns')
    groups = {name: trace.get(name, []) for name in ('sources','evidence','claims')}
    ids = [r.get('id') for group in groups.values() for r in group]
    if None in ids or len(ids) != len(set(ids)):
        errors.append('duplicate-or-missing-id')
    sources = {r['id']: r for r in groups['sources'] if 'id' in r}
    evidence = {r['id']: r for r in groups['evidence'] if 'id' in r}
    claims = {r['id']: r for r in groups['claims'] if 'id' in r}
    question_ids = {q['id'] for q in trace.get('brief', {}).get('questions', [])}
    for e in evidence.values():
        if e.get('source_id') not in sources:
            errors.append('evidence-source-reference')
        if not str(e.get('locator', '')).strip():
            errors.append('evidence-locator')
        if not str(e.get('direct_support', '')).strip():
            errors.append('empty-extraction')
        if any(q not in question_ids for q in e.get('question_ids', [])):
            errors.append('evidence-question-reference')
        if any(x not in evidence for x in e.get('contrary_evidence_ids', [])):
            errors.append('evidence-contrary-reference')
    for c in claims.values():
        for field in ('supporting_evidence_ids','contrary_evidence_ids'):
            if any(e not in evidence for e in c.get(field, [])):
                errors.append('claim-evidence-reference')
        if any(p not in claims for p in c.get('premise_claim_ids', [])):
            errors.append('claim-premise-reference')
        if any(q not in question_ids for q in c.get('question_ids', [])):
            errors.append('claim-question-reference')
        if not c.get('confidence_rationale') or not c.get('temporal_validity'):
            errors.append('claim-context')
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(cid: str) -> None:
        if cid in visiting:
            errors.append('claim-cycle')
            return
        if cid in visited or cid not in claims:
            return
        visiting.add(cid)
        for premise in claims[cid].get('premise_claim_ids', []):
            visit(premise)
        visiting.remove(cid)
        visited.add(cid)
    for cid in claims:
        visit(cid)
    covered: set[str] = set()
    for finding in trace.get('report', {}).get('findings', []):
        cid = finding.get('claim_id')
        if cid not in claims:
            errors.append('report-claim-reference')
            continue
        c = claims[cid]
        covered.update(c.get('question_ids', []))
        if finding.get('asserted') and c.get('support_status') in ('unsupported','unassessed'):
            errors.append('unsupported-assertion')
        if finding.get('asserted') and not c.get('supporting_evidence_ids') and not c.get('premise_claim_ids'):
            errors.append('ungrounded-assertion')
        if finding.get('asserted') and c.get('support_status') in ('qualified','contested') and not finding.get('qualification'):
            errors.append('lost-qualification')
        temporal = c.get('temporal_validity', {})
        if finding.get('asserted') and temporal.get('mode') == 'operative-state':
            try:
                if date.fromisoformat(temporal['effective_from']) > date.fromisoformat(temporal['target_as_of']):
                    errors.append('future-operative-state')
            except (KeyError, TypeError, ValueError):
                errors.append('operative-time-context')
    required = {q['id'] for q in trace.get('brief', {}).get('questions', []) if q.get('required')}
    gaps = set(trace.get('report', {}).get('unresolved_question_ids', []))
    if not required <= covered | gaps:
        errors.append('required-question-coverage')
    return sorted(set(errors))


def document_checks(text: str, records: dict[str, Any], root: Path, baseline: dict[str,str]) -> list[dict[str,Any]]:
    checks: list[dict[str,Any]] = []
    def check(name: str, ok: bool, evidence: Any) -> None:
        checks.append({'check': name, 'result': 'PASS' if ok else 'FAIL', 'evidence': evidence})
    outputs = re.findall(r'^## ([1-6])\. (.+)$', text, re.M)
    check('six required output responsibilities', [x[1] for x in outputs] == OUTPUTS, outputs)
    field_inventory = {p: re.findall(r'^\| ('+p+r'\d{2}) \|', text, re.M) for p in FIELDS}
    check('all 35 original field concerns', all(field_inventory[p] == [f'{p}{i:02d}' for i in range(1,n+1)] for p,n in FIELDS.items()), field_inventory)
    dimensions = re.findall(r'^\| (SQ\d{2}) \|', text, re.M)
    check('nine original source-quality dimensions', dimensions == [f'SQ{i:02d}' for i in range(1,10)], dimensions)
    conformance = text.split('## Verification, conformance and exit',1)[-1]
    rows = re.findall(r'^\| (R\d{2}) \|.*\| (PASS|FAIL|BLOCKED|NOT APPLICABLE) \|$', conformance, re.M)
    check('twelve conformance entries present', [r[0] for r in rows] == [f'R{i:02d}' for i in range(1,13)], rows)
    xids = re.findall(r'^\| (X\d{2}) ', text, re.M)
    synthetic = records.get('synthetic_challenges', [])
    expected_x = [f'X{i:02d}' for i in range(1,13)]
    check('twelve explicitly synthetic semantic challenges', xids == expected_x and [c.get('id') for c in synthetic] == expected_x and all(c.get('kind') == 'synthetic design counterexample' and c.get('premise') and c.get('expected_semantics') for c in synthetic), xids)
    actual = records.get('actual_trace', {})
    errs = trace_errors(actual)
    check('actual trace structural closure and context', not errs, errs)
    actual_claim = actual.get('claims', [{}])[0]
    actual_finding = actual.get('report', {}).get('findings', [{}])[0]
    same = actual_claim.get('text') == actual_finding.get('text') and actual_claim.get('text', 'ABSENT') in text
    same = same and all(x in text for x in ['Q-NOTE','S-PROV','E-NOTE','C-NOTE'])
    check('compact and structured actual attribution agree', same, {'claim_id': actual_claim.get('id'), 'claim_text': actual_claim.get('text')})
    known = set(baseline) | {'docs/research-logs/'+x for x in (DOC,EXAMPLES,REPORT,SCRIPT,'bootstrap-progress.md')}
    broken = []
    for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        path = target.split('#',1)[0]
        resolved = str(PurePosixPath('docs/research-logs') / path)
        if not (root / path).is_file() and resolved not in known:
            broken.append(target)
    check('relative links resolve locally or in inspected parent', not broken, broken)
    paths = sorted(str(p.relative_to(root.parents[1])) for p in root.parents[1].rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts)
    permitted = set(baseline) | {'docs/research-logs/'+x for x in (DOC,EXAMPLES,REPORT,SCRIPT,'bootstrap-progress.md')}
    extra = [p for p in paths if p not in permitted]
    check('no unrelated local production surfaces', not extra, extra)
    malformed = []
    width = None
    tables = 0
    for line_no, line in enumerate(text.splitlines(),1):
        if line.startswith('|'):
            cols = len(re.split(r'(?<!\\)\|', line))
            if width is None:
                width = cols
                tables += 1
            elif width != cols:
                malformed.append(line_no)
        else:
            width = None
    check('Markdown table column consistency', not malformed, {'tables':tables, 'bad_lines':malformed})
    check('explicit capability and maturity scope disclosure', 'not research-agent benchmarks' in text and 'No production skill, benchmark score, clean installation, release or maturity promotion is claimed here.' in text, 'Explicit scope and maturity disclaimer inspected.')
    return checks


def run_controls(text: str, records: dict[str,Any], root: Path, baseline: dict[str,str]) -> list[dict[str,Any]]:
    outcomes = []
    missing = text.replace('| SR07 |', '| REMOVED |', 1)
    failed = [x['check'] for x in document_checks(missing, records, root, baseline) if x['result'] == 'FAIL']
    outcomes.append({'mutation':'remove a required source-field concern','expected_failure':'all 35 original field concerns','actual_failures':failed,'result':'PASS' if 'all 35 original field concerns' in failed else 'FAIL'})
    def control(name: str, code: str, mutate: Any) -> None:
        trace = copy.deepcopy(records['actual_trace'])
        mutate(trace)
        actual = trace_errors(trace)
        outcomes.append({'mutation':name,'expected_failure':code,'actual_failures':actual,'result':'PASS' if code in actual else 'FAIL'})
    control('reference absent evidence','claim-evidence-reference',lambda t: t['claims'][0].update(supporting_evidence_ids=['E-MISSING']))
    control('duplicate evidence identity','duplicate-or-missing-id',lambda t: t['evidence'].append(copy.deepcopy(t['evidence'][0])))
    control('remove exact support locator','evidence-locator',lambda t: t['evidence'][0].update(locator=''))
    control('introduce circular premise','claim-cycle',lambda t: t['claims'][0].update(premise_claim_ids=['C-NOTE']))
    control('assert unsupported result','unsupported-assertion',lambda t: t['claims'][0].update(support_status='unsupported'))
    control('erase required qualification','lost-qualification',lambda t: t['claims'][0].update(support_status='qualified'))
    control('treat a future effective date as operative','future-operative-state',lambda t: t['claims'][0].update(temporal_validity={'mode':'operative-state','effective_from':'2026-10-01','target_as_of':'2026-09-10'}))
    return outcomes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-manifest', type=Path)
    parser.add_argument('--negative-controls', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    try:
        text = (root/DOC).read_text()
        records = json.loads((root/EXAMPLES).read_text())
        if args.baseline_manifest:
            baseline = json.loads(args.baseline_manifest.read_text())
            mode = 'Local stage outputs plus separately inspected remote parent inventory; not a clone.'
        else:
            # A complete snapshot must contain the governing spec and accepted prior outputs.
            prior = list(root.glob('2026-09-10-stage-0[12]-*'))
            if not (root/'2026-09-07-deep-research-skills-new-project-bootstrap-process.md').is_file() or not prior:
                raise ValueError('Supply --baseline-manifest or run from a complete stage snapshot.')
            baseline = {str(p.relative_to(root.parents[1])):blob(p.read_bytes()) for p in prior}
            for p in (root/'README.md', root/'2026-09-07-deep-research-skills-new-project-bootstrap-process.md', root.parents[1]/'README.md'):
                if p.exists():
                    baseline[str(p.relative_to(root.parents[1]))] = blob(p.read_bytes())
            mode = 'Complete local snapshot; remote publication is verified separately.'
        checks = document_checks(text, records, root, baseline)
        controls = run_controls(text, records, root, baseline) if args.negative_controls else []
        result = {'stage':3,'parent_revision':PARENT,'generated_at':datetime.now(timezone.utc).isoformat(),
                  'mode':mode,'scope':'Document/model checks only; manual semantic review in the stage log; no agent benchmark.',
                  'checks':checks,'negative_controls':controls,
                  'content_blobs':{name:blob((root/name).read_bytes()) for name in (DOC,EXAMPLES,SCRIPT)},
                  'parent_file_inventory':baseline}
        (root/REPORT).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
        failed = [x for x in checks+controls if x['result']!='PASS']
        print(json.dumps({'checks':len(checks),'negative_controls':len(controls),'failures':failed},indent=2))
        return int(bool(failed))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Verification failed: {error}', file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
