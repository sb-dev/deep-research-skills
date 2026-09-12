#!/usr/bin/env python3
"""Preserve the submitted L1-01 run and create its metadata-only revision."""
import datetime
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
case = root / 'benchmarks/core-vertical/l1-01'
revision = 'run-2026-09-12-02'
target = case / 'revisions' / revision
fixed = json.loads((case / 'fixed-input.json').read_text())
sha = lambda data: hashlib.sha256(data).hexdigest()
for name, expected in fixed['files'].items():
    assert sha((case / name).read_bytes()) == expected, name
if target.exists():
    raise SystemExit('Refusing to replace an existing submission revision.')
target.mkdir(parents=True)
preserved = ['prompt.txt', 'brief-and-plan.md', 'research/l1-01/research.md']
for name in preserved:
    destination = target / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes((case / name).read_bytes())
execution = json.loads((case / 'execution.json').read_text())
original_revision = execution['revision']
completed = datetime.datetime.now(datetime.timezone.utc).isoformat()
execution.update({
    'revision': revision,
    'producer_output_revision': original_revision,
    'acquisition_inherited_from_revision': original_revision,
    'prompt_sha256': sha((target / 'prompt.txt').read_bytes()),
    'prompt_sha256_basis': 'Exact prompt.txt file bytes, including its terminal LF.',
    'accepted_prompt_text_sha256': sha((target / 'prompt.txt').read_bytes().removesuffix(b'\n')),
    'accepted_prompt_text_sha256_basis': 'Remove exactly one terminal LF from prompt.txt; no other normalization. This identifies the accepted prompt text.',
    'repair': {'operation': 'execution-record provenance metadata repair', 'completed_at': completed,
               'owner': 'run execution metadata; no skill, source, report or expected outcome change',
               'source_actions': 0, 'search_queries': 0, 'producer_operation_rerun': False}
})
(target / 'execution.json').write_text(json.dumps(execution, indent=2) + '\n')
revised_fixed = {
    'case': fixed['case'], 'submission_revision': revision,
    'producer_output_revision': original_revision, 'fixed_at': completed,
    'files': {name: sha((target / name).read_bytes()) for name in fixed['files']},
    'review_output': 'research/l1-01/evaluation/audit.md',
    'review_metadata_output': 'research/l1-01/evaluation/review.json',
    'review_source_action_allocation': 0,
    'review_scope': 'reproducibility; preservation and dependency impact of metadata-only revision'
}
(target / 'fixed-input.json').write_text(json.dumps(revised_fixed, indent=2) + '\n')
receipt = {
    'case': fixed['case'], 'observed_defect': 'Unlabelled normalized prompt digest in execution.json.prompt_sha256',
    'reported_by': '/root/l1_01_fixed_audit', 'producer_confirmed_by': 'Exact local raw-file and single-terminal-LF hash comparison',
    'owning_layer': 'execution-record provenance metadata', 'operation': 'metadata-only revision',
    'original_submission': original_revision, 'repaired_submission': revision,
    'producer_report_revision_preserved': original_revision, 'completed_at': completed,
    'command': 'python docs/research-logs/2026-09-12-stage-19-repair.py',
    'source_actions': 0, 'search_queries': 0,
    'preserved_files': {name: sha((target / name).read_bytes()) for name in preserved},
    'original_fixed_files_unchanged': all(sha((case / name).read_bytes()) == expected for name, expected in fixed['files'].items()),
    'new_execution_sha256': sha((target / 'execution.json').read_bytes()),
    'dependency_assessment': 'No source, extraction, claim, citation or synthesis dependency changed. The new submission explicitly inherits the original acquisition and report revision.',
    'rerun_scope': 'Separate reproducibility audit of actual repaired fixed input; no source reacquisition is necessary.'
}
(case / 'repair.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
