#!/usr/bin/env python3
"""Validate Stage 4 documents, not source truth or provider performance.

Run at the completed Stage 4 snapshot. In a complete checkout the parent
inventory is read from Git. A partial recovery workspace must supply the
connector-inspected parent inventory with --baseline-manifest. No network,
third-party dependency, source mutation or credential is required.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from datetime import datetime, timezone
from urllib.parse import unquote, urlparse

PARENT = 'b1a2c31545d8814202d1bf3147aa17e979ef9f0c'
PREFIX = 'docs/research-logs/'
STEM = PREFIX + '2026-09-10-stage-04-'
LOG, MATRIX, SOURCES = (STEM + n for n in ('source-ecology.md', 'retrieval-matrix.md', 'sources.md'))
SCRIPT, REPORT = STEM + 'verification.py', STEM + 'verification.json'
PROGRESS = PREFIX + 'bootstrap-progress.md'
NEW = {LOG, MATRIX, SOURCES, SCRIPT, REPORT}
PATHS = ['Search engine', 'Site-restricted search', 'Provider deep-research agent',
         'Browser / browser automation', 'Specialist API', 'GitHub API',
         'Scholarly APIs: Crossref / OpenAlex / Semantic Scholar / PubMed-like',
         'RSS / feeds', 'Archive services', 'Direct document retrieval',
         'MCP / connector', 'Local file search', 'Code / data analysis']
DIMS = ['Coverage', 'Precision', 'Cost', 'Latency', 'Rate limits', 'Authentication',
        'Licence / terms', 'Reproducibility', 'Data quality', 'Freshness',
        'Multimodal support', 'Failure modes']
CLASSES = ['Official websites and documentation', 'Scholarly literature',
           'Books, reports and PDFs', 'News and trade press',
           'Company and regulator filings', 'GitHub repositories, issues, releases and code',
           'Standards and specifications', 'Datasets and APIs', 'Social and community sources',
           'Archives and historical snapshots', 'Uploaded and private project files',
           'Connected applications and internal sources', 'Images, video and other multimodal evidence']
OUTPUTS = ['Source ecology', 'Retrieval-path matrix', 'Source-selection heuristics',
           'Fallback strategy', 'Access, cost and licence constraints']


def blob(data: bytes) -> str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def seq(prefix: str, count: int) -> list[str]:
    return [f'{prefix}{i:02}' for i in range(1, count + 1)]


def tables(text: str) -> list[list[list[str]]]:
    result, current = [], []
    for line in text.splitlines() + ['']:
        if line.startswith('|') and line.endswith('|'):
            current.append([c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]])
        elif current:
            result.append(current)
            current = []
    return result


def evaluate(files: dict[str, str], baseline: dict[str, str]) -> list[dict]:
    log, matrix, sources = (files.get(n, '') for n in (LOG, MATRIX, SOURCES))
    checks = []

    def add(name: str, ok: bool, evidence) -> None:
        checks.append({'check': name, 'result': 'PASS' if ok else 'FAIL', 'evidence': evidence})

    headings = re.findall(r'^## [1-5]\. (.+)$', log, re.M)
    add('five output responsibilities', headings == OUTPUTS and all(files.get(n) for n in (LOG, MATRIX, SOURCES, SCRIPT, PROGRESS)), headings)
    classes = re.findall(r'^\| (C\d{2}) \| \*\*(.+?)\.\*\*', log, re.M)
    add('thirteen named source classes', classes == list(zip(seq('C', 13), CLASSES)), classes)
    path_headers = re.findall(r'^## (A\d{2}): (.+)$', matrix, re.M)
    add('thirteen named acquisition paths', path_headers == list(zip(seq('A', 13), PATHS)), path_headers)
    chunks = re.split(r'^## A\d{2}: .*\n', matrix, flags=re.M)[1:]
    cells, dimension_errors = [], []
    for i, chunk in enumerate(chunks, 1):
        rows = re.findall(r'^\| (D\d{2}) (.+?) \| (.+?) \|$', chunk, re.M)
        if [(a, b) for a, b, _ in rows] != list(zip(seq('D', 12), DIMS)):
            dimension_errors.append(f'A{i:02}')
        cells.extend((f'A{i:02}', a, b, c) for a, b, c in rows)
    add('156 correctly distributed dimension assessments', len(cells) == 156 and not dimension_errors, {'count': len(cells), 'invalid_paths': dimension_errors})
    invalid = [f'{a}/{d}' for a, d, _, c in cells if not re.match(r'^(?:E|A|E/A|A/E): ', c) or len(c) < 65]
    add('assessment labels and substantive text', len(cells) == 156 and not invalid, invalid)
    source_ids = re.findall(r'^### (S\d{2}):', sources, re.M)
    add('43 unique source records', source_ids == seq('S', 43), source_ids)
    source_chunks = re.split(r'^### (S\d{2}):', sources, flags=re.M)
    records = dict(zip(source_chunks[1::2], source_chunks[2::2]))
    fields = ['**Publisher:**', '**Edition/date:**', '**Original:**', '**Access:**', '**Inspected scope:**', '**Evidence used:**', '**Limits:**']
    bad_metadata = [sid for sid, text in records.items() if not all(f in text for f in fields) or not re.search(r'\]\(https://[^)]+\)', text)]
    add('source provenance metadata', len(records) == 43 and not bad_metadata, bad_metadata)
    cited = set(re.findall(r'\bS\d{2}\b', log + '\n' + matrix))
    add('source reference closure', bool(cited) and cited <= set(source_ids), sorted(cited - set(source_ids)))
    limited = {'S23', 'S24', 'S36'}
    observed = {sid for sid, text in records.items() if '**Access:** primary-search-excerpt ' in text}
    bad_access = [sid for sid, text in records.items() if ('SEARCH EXCERPT ONLY' in text) != (sid in observed)]
    add('limited access remains explicit', observed == limited and not bad_access, {'limited': sorted(observed), 'inconsistent': bad_access})
    services = re.findall(r'^\| (Crossref|OpenAlex|Semantic Scholar|PubMed-like / NCBI E-utilities) \|', matrix, re.M)
    add('four scholarly-service comparisons', services == ['Crossref', 'OpenAlex', 'Semantic Scholar', 'PubMed-like / NCBI E-utilities'], services)
    inventories = {p: re.findall(r'^\| (' + p + r'\d{2}) \|', log, re.M) for p in ('H', 'F', 'Q')}
    add('heuristics fallbacks and synthetic challenges', all(inventories[p] == seq(p, n) for p, n in [('H', 12), ('F', 16), ('Q', 8)]) and '**synthetic design scenarios**' in log, inventories)
    references = {p: set(re.findall(r'\b' + p + r'\d{2}\b', log)) for p in ('A', 'C')}
    add('source-path references resolve', references['A'] <= set(seq('A', 13)) and references['C'] <= set(seq('C', 13)), {p: sorted(v) for p, v in references.items()})
    known = set(baseline) | set(files) | {REPORT}
    broken = []
    for path in (LOG, MATRIX, SOURCES, PROGRESS):
        for target in re.findall(r'\]\(([^)]+)\)', files.get(path, '')):
            if urlparse(target).scheme or target.startswith('#'):
                continue
            item = str(PurePosixPath(path).parent / unquote(target.split('#')[0]))
            if item not in known:
                broken.append({'file': path, 'target': target})
    add('local documentation links resolve', not broken, broken)
    bad_tables, table_count = [], 0
    for path in (LOG, MATRIX, SOURCES, PROGRESS):
        for ti, table in enumerate(tables(files.get(path, '')), 1):
            table_count += 1
            widths = {len(row) for row in table}
            if len(widths) != 1:
                bad_tables.append({'file': path, 'table': ti, 'widths': sorted(widths)})
    add('Markdown table shape', not bad_tables and table_count > 0, {'tables': table_count, 'errors': bad_tables})
    changed = {p for p, s in files.items() if p != REPORT and (p not in baseline or blob(s.encode()) != baseline[p])}
    expected = (NEW - {REPORT}) | {PROGRESS}
    add('exact stage-scoped local delta', changed == expected, {'expected': sorted(expected), 'actual': sorted(changed), 'basis': 'Unmaterialised parent files are verified by remote tree comparison, not a local checkout claim.'})
    conformance = log.split('## Verification and conformance', 1)[-1]
    rows = re.findall(r'^\| (R\d{2}) \|.*\| (PASS|FAIL|BLOCKED|NOT APPLICABLE) \|$', conformance, re.M)
    add('complete conformance and bounded claims', rows == [(s, 'PASS') for s in seq('R', 12)] and 'Content acceptance: PASS.' in log and 'Remote publication verification is the final progression gate.' in log, rows)
    return checks


def controls(files: dict[str, str], baseline: dict[str, str]) -> list[dict]:
    scenarios = [
        ('missing class', LOG, lambda s: re.sub(r'^\| C13 .*\n', '', s, flags=re.M), 'thirteen named source classes'),
        ('missing path', MATRIX, lambda s: s.replace('## A13:', '## removed:'), 'thirteen named acquisition paths'),
        ('missing dimension', MATRIX, lambda s: re.sub(r'^\| D12 .*\n', '', s, count=1, flags=re.M), '156 correctly distributed dimension assessments'),
        ('unknown source', MATRIX, lambda s: s.replace('[S03.]', '[S99.]', 1), 'source reference closure'),
        ('duplicate source ID', SOURCES, lambda s: s.replace('### S43:', '### S42:'), '43 unique source records'),
        ('upgraded access', SOURCES, lambda s: s.replace('**Access:** primary-search-excerpt ', '**Access:** opened-selected-sections ', 1), 'limited access remains explicit'),
        ('unlabelled assessment', MATRIX, lambda s: s.replace('| E: Retrieves', '| Retrieves', 1), 'assessment labels and substantive text'),
        ('broken link', LOG, lambda s: s + '\n[broken](missing-stage04.md)\n', 'local documentation links resolve'),
        ('premature production file', 'skills/unjustified.txt', lambda s: 'synthetic negative control\n', 'exact stage-scoped local delta'),
    ]
    results = []
    for name, path, transform, expected in scenarios:
        mutated = copy.deepcopy(files)
        mutated[path] = transform(mutated.get(path, ''))
        failures = [c['check'] for c in evaluate(mutated, baseline) if c['result'] == 'FAIL']
        results.append({'mutation': name, 'expected_failure': expected, 'actual_failures': failures, 'result': 'PASS' if expected in failures else 'FAIL'})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-manifest', type=Path)
    parser.add_argument('--negative-controls', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    if args.baseline_manifest:
        manifest = json.loads(args.baseline_manifest.read_text())
        if manifest.get('parent') != PARENT:
            raise ValueError('Baseline manifest is not the accepted Stage 3 receipt')
        baseline = manifest['files']
        input_mode = 'recovered stage files plus connector-inspected parent inventory'
    else:
        output = subprocess.check_output(['git', 'ls-tree', '-rz', '--full-tree', PARENT], cwd=root)
        baseline = {}
        for entry in output.decode().split('\0'):
            if entry:
                metadata, path = entry.split('\t', 1)
                baseline[path] = metadata.split()[2]
        input_mode = 'complete Git checkout'
    files = {}
    for path in root.rglob('*'):
        relative = path.relative_to(root).as_posix()
        if path.is_file() and '.git' not in path.parts and '__pycache__' not in path.parts:
            files[relative] = path.read_text(encoding='utf-8')
    checks = evaluate(files, baseline)
    negative = controls(files, baseline) if args.negative_controls else []
    success = all(c['result'] == 'PASS' for c in checks + negative)
    result = {'stage': 4, 'run_at': datetime.now(timezone.utc).isoformat(), 'parent': PARENT,
              'verification_kind': 'document structure/reference validation; semantic review is in the stage log',
              'recovery': 'Reconstructed validator and newly executed results; prior unpublished results were not recovered.',
              'input_mode': input_mode, 'baseline_inventory': baseline,
              'checks': checks, 'negative_controls': negative,
              'file_blobs': {p: blob(s.encode()) for p, s in sorted(files.items()) if p in NEW | {PROGRESS} and p != REPORT},
              'result': 'PASS' if success else 'FAIL'}
    (root / REPORT).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'result': result['result'], 'checks': len(checks), 'negative_controls': len(negative),
                      'failures': [c['check'] for c in checks if c['result'] == 'FAIL']}, indent=2))
    return 0 if success else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'Verification could not run: {exc}', file=sys.stderr)
        sys.exit(2)
