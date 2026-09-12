# L2-01 — Scholarly metadata routes

[All research examples](../../README.md#learn-by-researching)

## Problem

Compare Crossref, OpenAlex and Semantic Scholar against explicit evidence-access criteria.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate, with no Extension Pack. Compare Crossref, OpenAlex and Semantic Scholar for a small literature-metadata workflow needing identifier resolution, title/author/date metadata, transparent pagination, applicable access restrictions and explicit missing-data handling. Use official service API documentation as authority; wrapper documentation is a secondary implementation view. Separate discovery, identifier lookup, abstracts and full-text access. Compare source constraints, publication/update-status information, authentication, documented limits and reproducibility. Do not copy remembered rates, assume keyless access or report measured latency. Preserve conflicting official/wrapper passages and the distinct claims each supports.

Use a criterion-led plan and relevant production commands, followed by a fixed-input audit. Bound discovery to 6 queries and acquisition to 18 reads/actions across the task. No new paid calls, purchases or credentials are authorised. Reserve finalisation and audit effort; do not spend the allowance merely because it remains.

Write research/l2-01/research.md with brief, criteria, searches, source/evidence/claim records, comparison, limitations and a role-specific recommendation. Write the separate review to research/l2-01/evaluation/audit.md without editing its submission. Preserve exact source dates, original locators, uncertainty and any unresolved enforcement question. Read existing outputs before revising them. Return actual paths and truthful completion; a feature table is not proof of installed integration.
```

## Expected artefacts

- `research/l2-01/research.md`
- `research/l2-01/evaluation/audit.md`

## Evaluation contract

Evaluate criteria, currentness, primary authority and metadata/full-text limits.

Official API evidence versus wrapper/metadata substitution; FX04/FX07. Producer and evaluator, core only.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L2-01`; L02/L03/L04; K02/K05. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).
