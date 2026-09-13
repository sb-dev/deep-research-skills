# L2-03 — Small numeric repair comparison

[All research examples](../../README.md#learn-by-researching)

## Problem

Produce a reproducible descriptive comparison while retaining denominators and sampling limits.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate with no Extension Pack. Read the complete small file aggregated/202507/OpenRepairData_v0.3_unpowered_202507.csv in https://github.com/openrepair/data, plus its data standard and release documentation. Resolve a commit and retain source identity. Compare the first two distinct data_provider values in lexicographic order across the repair-status categories actually present. Show totals, denominators and shares, retaining Unknown. Save the calculation and observed result. Check category and coverage compatibility before interpreting differences. These are participating-organisation records, not representative household failure rates, provider quality rankings or willingness-to-pay evidence. Do not download the large powered-items file.

Allow at most 6 searches and 18 source reads/actions, using only authorised tools and no new paid service. Reserve review effort and bound local computation to the acquired small file. Do not infer missing groups or substitute invented rows.

Write research/l2-03/research.md, research/l2-03/calculation.py, research/l2-03/results.csv and research/l2-03/evaluation/audit.md. Record input ref/hash, transformations, units, actual output and source-to-claim support. Audit the fixed result and preserve all original inputs. On resumption, retain valid prior calculations and revise only changed dependencies. Return actual paths and the descriptive findings with their sampling limits; do not claim an unperformed benchmark.
```

## Expected artefacts

- `research/l2-03/research.md`
- `research/l2-03/calculation.py`
- `research/l2-03/results.csv`
- `research/l2-03/evaluation/audit.md`

## Evaluation contract

Evaluate reproducible arithmetic, complete denominators and bounded inference.

Complete denominator including Unknown and reproducible calculation; PR01. Producer/evaluator with actual local data execution.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L2-03`; L03/L06; K07/K09/K13. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).

## Recorded execution

[Progressive run](../../benchmarks/progressive/research/l2-03/research.md) contains the actual source-checkout output and its stated support and access limits. See the [separate review](../../benchmarks/progressive/research/l2-03/evaluation/audit.md) for assessed claims and remaining gaps.
