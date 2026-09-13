# L1-03 — Repair-data count scope

[All research examples](../../README.md#learn-by-researching)

## Problem

Distinguish the published count, unit, release date and observation period.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use the installed deep-research skill with no Extension Pack. Determine what the published Open Repair Data headline count refers to and which observation period it covers. Begin with https://github.com/openrepair/data and https://openrepair.org/open-data/downloads/. Resolve the repository ref to a commit before citing its README. Distinguish powered items, unpowered items, release/publication date and the last period represented by the records. Do not assume a currently retrieved page describes current-year observations. Treat disagreements as version or scope questions until original definitions resolve them.

This is a documentation-level unit/count-scope check. Do not download or claim to count the large aggregate CSV. Use frame, extract-evidence and synthesise as needed. Allow at most 3 searches and 8 source reads/actions, with review effort reserved. Use existing authorised tools only, with no new payment or external contact. Reaching a bound does not establish an answer.

Write research/l1-03/research.md with the question, actual sources and locators, inspected evidence, supported claim, answer, temporal distinctions and labelled producer self-check. State any unresolved count or access limitation. Preserve an existing run and make material revisions identifiable. Return the actual file path and findings without claiming a data-analysis or installation benchmark.
```

## Expected artefacts

- `research/l1-03/research.md`

## Evaluation contract

Evaluate unit definition and release/observation/read dates.

Count unit and observation versus retrieval date; FX03/TM02. Producer only.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L1-03`; L03/L07; K04/K11. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).

## Recorded execution

[Progressive run](../../benchmarks/progressive/research/l1-03/research.md) contains the actual source-checkout output and its stated support and access limits. Review scope is labelled in the output.
