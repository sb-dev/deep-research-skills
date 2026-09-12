# L3-01 — Long-context research evidence

[All research examples](../../README.md#learn-by-researching)

## Problem

Use the `scholarly-evidence` profile to assess what benchmark evidence does and does not justify.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate. Explicitly select scholarly-evidence and record the actual profile revision; do not call a core-only run a pack run if it is unavailable. Research what evidence does and does not justify about using a long-context model instead of retrieval in an evidence-led research workflow. Begin with the original RULER, Lost in the Middle and LongBench works, resolve their official publication/version records and relevant original implementations, and follow only primary studies needed to close material gaps. Distinguish evaluated models, task design, conditions, reported observations and your transfer inferences. Link related reports without inflating study counts. Determine whether the studies measure retrieval, multi-hop use, position sensitivity or the whole research workflow.

Produce a conditional software-team decision report and task-specific evaluation proposal, not an unsupported production-suitability verdict or exhaustive systematic-review claim. Allow 12 searches and 36 source reads/actions across the whole task; no paid model runs or purchases. Reserve finalisation and separate audit effort. Stop optional collection when support is adequate, not when every budget unit is spent.

Write research/l3-01/research.md, study-report-map.md, evaluation-proposal.md and evaluation/audit.md beneath that same directory. Preserve exact sources, locators, method limits, counterevidence, uncertainty and fixed-input review. Read existing records before revision and retain valid evidence. Return actual paths, findings and missing support without inventing benchmark execution or specialist approval.
```

## Expected artefacts

- `research/l3-01/research.md`
- `research/l3-01/study-report-map.md`
- `research/l3-01/evaluation-proposal.md`
- `research/l3-01/evaluation/audit.md`

## Evaluation contract

Evaluate scholarly appraisal and transfer limits separately from citation syntax.

Scholarly unit/status and limited transfer; FX05/FX06/FX09, PD01. Explicit scholarly-evidence.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L3-01`; L02–L05/L08; K05/K08/K10. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).
