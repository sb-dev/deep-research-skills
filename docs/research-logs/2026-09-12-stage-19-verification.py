#!/usr/bin/env python3
"""Verify the recorded L1-01 revisions, not the truth of their research claims."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / 'benchmarks/core-vertical/l1-01'
REPAIRED = CASE / 'revisions/run-2026-09-12-02'
PARENT = '0d708a7fee2ec95effb345d10677b2c53f292155'


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def record(path: Path) -> dict:
    return json.loads(path.read_text())


def fixed_errors(base: Path) -> list[str]:
    errors = []
    for name, expected in record(base / 'fixed-input.json')['files'].items():
        path = (base / name).resolve()
        if not path.is_relative_to(base.resolve()):
            errors.append('fixed input escapes submission: ' + name)
        elif not path.is_file() or digest(path.read_bytes()) != expected:
            errors.append('fixed input identity changed: ' + name)
    return errors


def prompt_metadata_errors(base: Path) -> list[str]:
    execution = record(base / 'execution.json')
    return ([] if execution['prompt_sha256'] == digest((base / 'prompt.txt').read_bytes())
            else ['execution prompt_sha256 does not identify raw prompt.txt bytes'])


def review_table_errors(text: str) -> list[str]:
    """Bind the displayed previous/current digest columns by file name."""
    errors = []
    names = list(record(CASE / 'fixed-input.json')['files']) + ['fixed-input.json']
    for name in names:
        row = re.search(r'^\| `' + re.escape(name) + r'` \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|', text, flags=re.M)
        expected = (digest((CASE / name).read_bytes()), digest((REPAIRED / name).read_bytes()))
        if row is None or row.groups() != expected:
            errors.append('review table identity mismatch: ' + name)
    return errors


def verify() -> dict:
    errors = fixed_errors(CASE) + fixed_errors(REPAIRED)
    public_page = (ROOT / 'examples/level-1-prov-primer-publication-status/README.md').read_text()
    public_prompt = re.search(r'```text\n(.*?)\n```', public_page, flags=re.S)
    if public_prompt is None or (CASE / 'prompt.txt').read_bytes() != public_prompt.group(1).encode() + b'\n':
        errors.append('executed prompt differs from exact accepted public prompt plus terminal LF')
    for name, expected in record(CASE / 'original-review-integrity.json')['files'].items():
        if digest((CASE / name).read_bytes()) != expected:
            errors.append('original failed review changed: ' + name)
    historical = prompt_metadata_errors(CASE)
    if historical != ['execution prompt_sha256 does not identify raw prompt.txt bytes']:
        errors.append('recorded historical hash-normalization defect no longer reproduced')
    errors += prompt_metadata_errors(REPAIRED)

    original = record(CASE / 'execution.json')
    repaired = record(REPAIRED / 'execution.json')
    preserved = ['prompt.txt', 'brief-and-plan.md', 'research/l1-01/research.md']
    for name in preserved:
        if (CASE / name).read_bytes() != (REPAIRED / name).read_bytes():
            errors.append('repair changed preserved content: ' + name)
    if repaired['accepted_prompt_text_sha256'] != digest((REPAIRED / 'prompt.txt').read_bytes().removesuffix(b'\n')):
        errors.append('explicit accepted-prompt text identity is incorrect')
    if original['actual_acquisition'] != repaired['actual_acquisition']:
        errors.append('inherited acquisition record changed during metadata repair')
    if original['tool_calls'] != repaired['tool_calls']:
        errors.append('inherited source operations changed during metadata repair')
    if repaired['producer_output_sha256'] != digest((REPAIRED / 'research/l1-01/research.md').read_bytes()):
        errors.append('repaired execution does not identify its actual preserved report')

    required_reviews = [CASE / 'research/l1-01/evaluation', REPAIRED / 'research/l1-01/evaluation']
    for directory in required_reviews:
        for filename in ['audit.md', 'review.json']:
            path = directory / filename
            if not path.is_file() or not path.read_text().strip():
                errors.append('missing actual review artifact: ' + str(path.relative_to(ROOT)))
    actual_table = (REPAIRED / 'research/l1-01/evaluation/audit.md').read_text()
    errors += review_table_errors(actual_table)
    table_negative = review_table_errors((CASE / 'fixtures/audit-table-before-qa.md').read_text())
    if len(table_negative) != 3:
        errors.append('observed draft table mislabelling is not detected in all three affected rows')

    parent_readme = subprocess.check_output(['git', 'show', PARENT + ':README.md'], cwd=ROOT)
    if (ROOT / 'README.md').read_bytes() != parent_readme:
        errors.append('root README changed from accepted Stage 18 bytes')

    checks = runpy.run_path(str(ROOT / 'tests/check_repository.py'))
    new_markdown = list(CASE.rglob('*.md')) + [ROOT / 'docs/research-logs/2026-09-12-stage-19-core-vertical.md', ROOT / 'docs/research-logs/2026-09-12-stage-19-public-claims-ledger.md']
    for path in new_markdown:
        errors += checks['links'](ROOT, path)

    return {
        'result': 'FAIL' if errors else 'PASS',
        'errors': errors,
        'fixed_submission_count': 2,
        'fixed_file_identities_checked': 8,
        'historical_review_identities_checked': 2,
        'accepted_public_prompt_identity_checked': True,
        'historical_negative_control': {'result': 'DETECTED', 'observed_defects': historical},
        'observed_review_table_negative_control': {'result': 'DETECTED', 'observed_defects': table_negative},
        'final_review_table_checked_by_filename': True,
        'repaired_raw_prompt_identity': 'PASS' if not prompt_metadata_errors(REPAIRED) else 'FAIL',
        'preserved_between_revisions': preserved,
        'root_readme_unchanged': (ROOT / 'README.md').read_bytes() == parent_readme,
        'markdown_files_checked': len(new_markdown),
        'scope': 'Artifact integrity, actual historical provenance defect, preservation and local navigation only; semantic support comes from the separate actual audits.'
    }


if __name__ == '__main__':
    result = verify()
    print(json.dumps(result, indent=2))
    raise SystemExit(int(result['result'] != 'PASS'))
