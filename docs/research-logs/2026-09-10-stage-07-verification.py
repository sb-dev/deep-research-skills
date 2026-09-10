#!/usr/bin/env python3
"""Validate Stage 7 documents; does not execute providers or prove citation entailment."""
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
from urllib.parse import urlsplit, unquote

PARENT = '18b0c365d0e845bdcdf22308606c2cfe1fa76bca'
SPEC_BLOB = '8ff62c92bada2861ece3684a9e73a83da75d9d94'
PREFIX = 'docs/research-logs/'
STEM = '2026-09-10-stage-07-'
LOG = PREFIX + STEM + 'ai-tool-landscape.md'
MATRIX = PREFIX + STEM + 'capability-matrix.md'
SOURCES = PREFIX + STEM + 'sources.md'
SCRIPT = PREFIX + STEM + 'verification.py'
RESULT = PREFIX + STEM + 'verification.json'
PROGRESS = PREFIX + 'bootstrap-progress.md'
EXPECTED = {LOG, MATRIX, SOURCES, SCRIPT, RESULT, PROGRESS}
FIELDS = ['Capability', 'Source', 'Licence / terms', 'Maturity',
          'Installation / access', 'Research role', 'Source control',
          'Citation behaviour', 'Deterministic vs generative', 'Provider coupling',
          'Cost / latency', 'Composability', 'Maintenance', 'Gaps', 'Decision']
CATEGORIES = ['Agent Skills for research / browsing / literature review / fact checking',
              'Provider deep-research agents', 'Search APIs', 'Browser automation',
              'Academic search APIs', 'GitHub research tools', 'PDF / document extraction',
              'Web extraction / crawling', 'Citation tooling', 'Reference managers',
              'Data analysis / code sandboxes', 'Knowledge / note tools',
              'MCPs and connectors', 'Benchmark / eval frameworks']
OUTPUTS = ['AI/tool landscape', 'Shortlist and selection rationale', 'Capability matrix',
           'Integration decisions', 'Explicit gaps']

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def blocks(text: str, prefix: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r'^## (' + prefix + r'\d{2}):[^\n]*\n', text, re.M))
    return [(m.group(1), text[m.end():matches[i+1].start() if i+1 < len(matches) else len(text)])
            for i, m in enumerate(matches)]

def rows(text: str) -> list[list[str]]:
    return [[v.strip() for v in line.strip().strip('|').split('|')]
            for line in text.splitlines() if line.startswith('|')]

def assess(docs: dict[str, str], paths: set[str], baseline: dict[str, str],
           parent_progress: str) -> list[dict]:
    out = []
    def check(name: str, condition: bool, evidence: object) -> None:
        out.append({'check': name, 'result': 'PASS' if condition else 'FAIL', 'evidence': evidence})
    log, matrix, sources = (docs.get(p, '') for p in (LOG, MATRIX, SOURCES))
    check('authority and accepted parent recorded', PARENT in log and SPEC_BLOB in log,
          {'parent': PARENT, 'spec_blob': SPEC_BLOB})
    headings = re.findall(r'^## [1-5]\. (.+)$', log, re.M)
    check('all five output responsibilities', headings == OUTPUTS and all(docs.get(p) for p in (LOG, MATRIX, SOURCES)), headings)
    cats = [(r[0], r[1]) for r in rows(log) if len(r) == 3 and re.fullmatch(r'G\d{2}', r[0])]
    expected_cats = [(f'G{i:02}', title) for i, title in enumerate(CATEGORIES, 1)]
    check('all fourteen named categories', cats == expected_cats, cats)
    cb = blocks(matrix, 'C')
    ids = [c for c, _ in cb]
    check('35 distinct candidate records', ids == [f'C{i:02}' for i in range(1, 36)], ids)
    records = {}
    field_errors = []
    memberships = {}
    for cid, body in cb:
        rr = [r for r in rows(body) if len(r) == 2 and r[0] not in ('Field', '---')]
        if [r[0] for r in rr] != FIELDS or any(len(r[1]) < 10 for r in rr):
            field_errors.append(cid)
        records[cid] = dict(rr)
        membership = re.search(r'^Categories: (.+)\.$', body, re.M)
        memberships[cid] = re.findall(r'G\d{2}', membership.group(1)) if membership else []
    check('all 525 required field assessments', not field_errors and sum(len(v) for v in records.values()) == 525,
          {'assessments': sum(len(v) for v in records.values()), 'invalid_candidates': field_errors})
    invalid_decisions = [cid for cid, rec in records.items()
                         if not re.match(r'^(USE|ADAPT|REFERENCE|REJECT): .+', rec.get('Decision', ''))]
    check('decisions have allowed labels and rationale', not invalid_decisions, invalid_decisions)
    cat_ids = {c for c, _ in expected_cats}
    used = {g for gs in memberships.values() for g in gs}
    membership_errors = [c for c, gs in memberships.items() if not gs or set(gs) - cat_ids]
    check('candidate category coverage', used == cat_ids and not membership_errors,
          {'covered': sorted(used), 'invalid_candidates': membership_errors})
    sb = blocks(sources, 'S')
    source_ids = [s for s, _ in sb]
    provenance_errors = [s for s, b in sb if not re.search(r'\]\(https://[^)]+\)', b)
                         or 'Inspected' not in b or len(b) < 150]
    check('36 distinct source bundles with provenance', source_ids == [f'S{i:02}' for i in range(1, 37)] and not provenance_errors,
          {'count': len(source_ids), 'invalid_sources': provenance_errors})
    references = set(re.findall(r'\bS\d{2}\b', log + matrix))
    unknown_sources = sorted(references - set(source_ids))
    check('source references resolve', not unknown_sources, unknown_sources)
    shortlist = log.partition('## 2. Shortlist and selection rationale')[2].partition('## 3.')[0]
    short_ids = [c for r in rows(shortlist) if len(r) == 3
                 for c in re.findall(r'\bC\d{2}\b', r[1])]
    invalid_short = [c for c in short_ids if c not in records or
                     not re.match(r'^(USE|ADAPT):', records.get(c, {}).get('Decision', ''))]
    all_c_refs = set(re.findall(r'\bC\d{2}\b', log))
    check('shortlist and candidate references resolve', bool(short_ids) and not invalid_short and not (all_c_refs - set(ids)),
          {'shortlisted': sorted(set(short_ids)), 'invalid': sorted(set(invalid_short) | (all_c_refs - set(ids)))})
    integration = [r[0] for r in rows(log) if r and re.fullmatch(r'I\d{2}', r[0])]
    gaps = [r[0] for r in rows(log) if r and re.fullmatch(r'X\d{2}', r[0])]
    check('integration decisions and explicit gaps complete',
          integration == [f'I{i:02}' for i in range(1, 12)] and gaps == [f'X{i:02}' for i in range(1, 13)],
          {'integration_decisions': integration, 'gaps': gaps})
    guard_tests = {
        'soft inclusion remains soft': 'preference, not a strict allowlist' in records.get('C04', {}).get('Source control', ''),
        'ignored crawl filters remain explicit': 'deprecated and ignored' in records.get('C12', {}).get('Source control', ''),
        'proprietary skill not adopted': records.get('C03', {}).get('Decision', '').startswith('REJECT:'),
        'unmaintained local MCP remains explicit': 'no longer actively maintained' in records.get('C29', {}).get('Maturity', ''),
        'human verification not relabelled': 'human-owned' in records.get('C35', {}).get('Citation behaviour', ''),
        'no candidate installation claimed': 'No candidate was installed or benchmarked' in matrix,
    }
    check('known constraint distinctions retained', all(guard_tests.values()), guard_tests)
    known_paths = paths | set(baseline) | {RESULT}
    bad_links = []
    table_errors = []
    for name in (LOG, MATRIX, SOURCES, PROGRESS):
        text = docs.get(name, '')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            clean = unquote(target.split('#')[0])
            resolved = str((Path(name).parent / clean).as_posix())
            if resolved not in known_paths:
                bad_links.append({'from': name, 'target': target})
        width = None
        for n, line in enumerate(text.splitlines(), 1):
            if line.startswith('|'):
                w = len(line.strip().strip('|').split('|'))
                if width is not None and width != w:
                    table_errors.append(f'{name}:{n}')
                width = w
            else:
                width = None
    check('local documentation links resolve', not bad_links, bad_links)
    check('Markdown table columns consistent', not table_errors, table_errors)
    extra = paths - set(baseline) - EXPECTED
    modified_prior = [p for p, data in docs.items() if p in baseline and p != PROGRESS
                      and blob(data.encode()) != baseline[p]]
    missing_outputs = sorted((EXPECTED - {RESULT}) - paths)
    prefix = parent_progress.partition('## Remaining stages')[0]
    preserved = bool(prefix) and docs.get(PROGRESS, '').startswith(prefix)
    check('stage-only delta and accepted progress preserved', not extra and not modified_prior and not missing_outputs and preserved,
          {'extra': sorted(extra), 'modified_prior': modified_prior, 'missing_outputs': missing_outputs,
           'accepted_progress_prefix_preserved': preserved})
    conformance = [r[0] for r in rows(log) if len(r) == 5 and re.fullmatch(r'R\d{2}', r[0]) and r[-1] == 'PASS']
    check('content conformance and separate publication gate',
          conformance == [f'R{i:02}' for i in range(1, 11)] and 'R11 is the separate publication gate' in log,
          conformance)
    return out

def git_output(root: Path, *args: str) -> str:
    run = subprocess.run(['git', '-C', str(root), *args], text=True, capture_output=True, check=False)
    if run.returncode:
        raise RuntimeError(run.stderr.strip() or 'Git command failed')
    return run.stdout

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--baseline-manifest', type=Path)
    parser.add_argument('--parent-progress', type=Path)
    parser.add_argument('--negative-controls', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    if args.baseline_manifest:
        baseline = json.loads(args.baseline_manifest.read_text())
        if not args.parent_progress:
            raise ValueError('--parent-progress is required with a partial-workspace baseline')
        parent_progress = args.parent_progress.read_text()
        mode = 'stage files plus connector-inspected parent inventory'
    else:
        raw = git_output(root, 'ls-tree', '-r', '--full-tree', PARENT)
        baseline = {line.split('\t', 1)[1]: line.split()[2] for line in raw.splitlines()}
        parent_progress = git_output(root, 'show', f'{PARENT}:{PROGRESS}')
        mode = 'Git checkout with identified parent'
    if blob(parent_progress.encode()) != baseline.get(PROGRESS):
        raise ValueError('Parent progress does not match the inspected parent blob')
    paths = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
             and '.git' not in p.parts and '__pycache__' not in p.parts}
    docs = {p: (root / p).read_text() for p in paths if p.endswith(('.md', '.py'))}
    checks = assess(docs, paths, baseline, parent_progress)
    controls = []
    if args.negative_controls:
        mutations = [
            ('missing category', LOG, '| G14 |', '| OMITTED |', 'all fourteen named categories'),
            ('missing field', MATRIX, '| Maturity |', '| Missing maturity |', 'all 525 required field assessments'),
            ('duplicate candidate identity', MATRIX, '## C35:', '## C34:', '35 distinct candidate records'),
            ('unknown source', MATRIX, 'S01: inspected', 'S99: inspected', 'source references resolve'),
            ('unknown decision', MATRIX, 'REFERENCE: retain', 'ADOPT: retain', 'decisions have allowed labels and rationale'),
            ('unknown shortlist item', LOG, '| C19 |', '| C99 |', 'shortlist and candidate references resolve'),
            ('soft filter falsely strengthened', MATRIX, 'preference, not a strict allowlist', 'strict allowlist', 'known constraint distinctions retained'),
            ('broken documentation link', LOG, '(bootstrap-progress.md)', '(absent.md)', 'local documentation links resolve'),
            ('accepted progress damaged', PROGRESS, '## Stage 1:', '## Removed stage 1:', 'stage-only delta and accepted progress preserved'),
        ]
        for label, path, before, after, target in mutations:
            mutated = copy.deepcopy(docs)
            if before not in mutated[path]:
                raise ValueError(f'Negative control has no target: {label}')
            mutated[path] = mutated[path].replace(before, after, 1)
            fails = [c['check'] for c in assess(mutated, paths, baseline, parent_progress) if c['result'] == 'FAIL']
            controls.append({'mutation': label, 'expected_failure': target, 'actual_failures': fails,
                             'result': 'PASS' if target in fails else 'FAIL'})
        bad_paths = paths | {'skills/unjustified.txt'}
        fails = [c['check'] for c in assess(docs, bad_paths, baseline, parent_progress) if c['result'] == 'FAIL']
        target = 'stage-only delta and accepted progress preserved'
        controls.append({'mutation': 'premature production file', 'expected_failure': target,
                         'actual_failures': fails, 'result': 'PASS' if target in fails else 'FAIL'})
    passed = all(c['result'] == 'PASS' for c in checks + controls)
    report = {'stage': 7, 'run_at': datetime.now(timezone.utc).isoformat(), 'parent': PARENT,
              'input_mode': mode, 'verification_kind': 'document structure and declared-constraint checks; semantic review recorded separately',
              'baseline_inventory': baseline, 'checks': checks, 'negative_controls': controls,
              'file_blobs': {p: blob((root/p).read_bytes()) for p in sorted(EXPECTED - {RESULT}) if (root/p).exists()},
              'result': 'PASS' if passed else 'FAIL'}
    (root / RESULT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'result': report['result'], 'checks': len(checks), 'negative_controls': len(controls),
                      'failures': [c['check'] for c in checks if c['result'] == 'FAIL']}, indent=2))
    return 0 if passed else 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, RuntimeError, json.JSONDecodeError) as error:
        print(f'Verification error: {error}', file=sys.stderr)
        sys.exit(2)
