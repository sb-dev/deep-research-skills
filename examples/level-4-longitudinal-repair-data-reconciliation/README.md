# L4-02 — Longitudinal repair-data reconciliation

[All research examples](../../README.md#learn-by-researching)

## Problem

Reconcile large snapshots without double-counting or hiding schema drift.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate with no Extension Pack. Compare the 202407 and 202507 Open Repair Data releases at https://github.com/openrepair/data. Read schemas, category definitions and release documentation before choosing compatible numeric comparisons. Retain powered/unpowered coverage, provider identity, Unknown status and changed category mappings. Acquire no more than 150 MB of data and use bounded-memory or streaming analysis. Preserve exact source identities, input hashes, code and observed outputs. Do not add snapshot totals as independent events or infer changing household repairability from changed reporting coverage.

Produce a provisional comparison, diagnose any denominator, schema or repeated-record problem actually observed, and repair only affected calculations, claims and review dependencies. If no natural defect is found, use a clearly labelled copy with one deliberate denominator error to demonstrate repair, preserving the unmodified original. Never call that mutation an observed dataset defect. Allow at most 20 searches and 64 source reads/actions across the task, with review effort reserved, no new payment and no external contact.

Write research/l4-02/research.md, input-manifest.json, calculation.py, results.csv, change-record.md and evaluation/audit.md beneath research/l4-02/. Report actual coverage, arithmetic, uncertainty, before/after identity and preserved work. Audit fixed submissions. Return actual paths and truthful completion; neither a dataset download nor file presence establishes a passing longitudinal analysis.
```

## Expected artefacts

- `research/l4-02/research.md`
- `research/l4-02/input-manifest.json`
- `research/l4-02/calculation.py`
- `research/l4-02/results.csv`
- `research/l4-02/change-record.md`
- `research/l4-02/evaluation/audit.md`

## Evaluation contract

Evaluate calculation fidelity, snapshot dependence and repair preservation.

Snapshot double counting, schema/denominator repair, preserved calculations; FX06/PR01/TM03. Core, bounded data acquisition.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L4-02`; L03/L06/L07; K04/K07/K16. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).
