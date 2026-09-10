#!/usr/bin/env python3
"""Check Stage 9 inventories. These checks do not evaluate research-agent quality."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

GAPS = ('Source independence', 'Primary-source preference', 'Claim-level provenance',
        'Citation entailment', 'Contradiction handling', 'Uncertainty calibration',
        'Temporal validity', 'Inclusion / exclusion traceability', 'Research stopping criteria',
        'Incremental refresh', 'Smallest-sufficient repair', 'Cross-source deduplication',
        'Research benchmarkability')
DEFERRED = ('Custom general web crawler', 'Custom search engine', 'Universal provider registry',
            'Universal research workflow DSL', 'Persistent cross-project evidence database',
            'Universal knowledge graph', 'Vector database by default', 'Multi-agent swarm by default',
            'Fully automated numeric source-quality score', 'Continuous research daemon',
            'Universal citation format converter', 'Research orchestration platform separate from Agent Skills')
OUTPUTS = ('Gap matrix', 'Native capability shortlist', 'Reuse decisions',
           'Deferred-improvement register', 'Proof required before expensive architecture')
# Paths directly read in the accepted parent chain, not a fabricated local checkout.
ACCEPTED_LINKS = {
 '2026-09-07-deep-research-skills-new-project-bootstrap-process.md',
 '2026-09-10-stage-01-project-goal-and-boundary.md',
 '2026-09-10-stage-02-method-comparison.md',
 '2026-09-10-stage-03-question-evidence-claim-model.md',
 '2026-09-10-stage-04-source-ecology.md',
 '2026-09-10-stage-05-workflow-and-artifacts.md',
 '2026-09-10-stage-06-effort-and-stopping.md',
 '2026-09-10-stage-07-ai-tool-landscape.md',
 '2026-09-10-stage-07-capability-matrix.md',
 '2026-09-10-stage-07-publication-receipt.md',
 '2026-09-10-stage-08-execution-layer.md',
 '2026-09-10-stage-08-publication-receipt.md',
}

def check(text):
    rows = [line.split('|')[1:-1] for line in text.splitlines() if line.startswith('|')]
    indexed = {r[0].strip(): r for r in rows}
    result = {}
    for prefix, terms in [('G', GAPS), ('D', DEFERRED)]:
        actual = [r[0].strip() for r in rows if re.fullmatch(prefix+r'\d{2}', r[0].strip())]
        expected = [f'{prefix}{i:02}' for i in range(1, len(terms)+1)]
        result[prefix+' inventory and wording'] = actual == expected and all(
            term.casefold() in indexed[key][1].casefold() for key, term in zip(expected, terms))
    result['five outputs'] = all(f'## {i}. {name}' in text for i, name in enumerate(OUTPUTS, 1))
    result['eight workflow groups'] = all(f'| W{i:02} ' in text for i in range(1, 9))
    result['all three classifications'] = all(f'**{x}**' in text for x in ['Covered', 'Partially covered', 'Missing'])
    result['native reuse and proof records'] = all(
        [r[0].strip() for r in rows if re.fullmatch(p+r'\d{2}', r[0].strip())]
        == [f'{p}{i:02}' for i in range(1, n+1)] for p,n in [('N',6),('U',12),('P',7)])
    links = re.findall(r'\]\(([^)]+)\)', text)
    result['local links resolve in inspected parent'] = all(
        link.split('#')[0] in ACCEPTED_LINKS for link in links if '://' not in link)
    result['substantive table cells'] = all(all(c.strip() for c in r) for r in rows)
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    path = Path(__file__).with_name('2026-09-10-stage-09-gap-analysis.md')
    data = path.read_bytes(); text = data.decode('utf-8')
    checks = check(text)
    controls = []
    for label, old, new, expected in [
        ('missing gap', '| G13 |', '| REMOVED |', 'G inventory and wording'),
        ('wrong deferred proposal', 'Custom search engine', 'Unrelated proposal', 'D inventory and wording'),
        ('missing output', '## 3. Reuse decisions', '## Removed output', 'five outputs'),
        ('broken reference', '(2026-09-10-stage-07-capability-matrix.md)', '(absent.md)', 'local links resolve in inspected parent'),
        ('missing proof', '| P07 |', '| REMOVED |', 'native reuse and proof records'),
    ]:
        if old not in text:
            raise ValueError(f'Control not applied: {label}')
        observed = check(text.replace(old, new, 1))
        controls.append({'mutation': label, 'expected_failed_check': expected,
                         'result': 'PASS' if not observed[expected] else 'FAIL'})
    result = {'stage':9, 'checked_at':datetime.now(timezone.utc).isoformat(),
        'verification_kind':'document inventory checks; semantic review is recorded separately',
        'source_commit':'4c26bfd26a87130751594f96ef8042ae68012f7f',
        'source_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
        'checks':{k:'PASS' if v else 'FAIL' for k,v in checks.items()},
        'negative_controls':controls,
        'result':'PASS' if all(checks.values()) and all(c['result']=='PASS' for c in controls) else 'FAIL'}
    output = json.dumps(result, indent=2)+'\n'
    if args.output: args.output.write_text(output, encoding='utf-8')
    print(output)
    raise SystemExit(0 if result['result']=='PASS' else 1)

if __name__ == '__main__': main()
