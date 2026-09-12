# L4-01 — API-policy reconstruction and refresh

[All research examples](../../README.md#learn-by-researching)

## Problem

Reconstruct dated policy states and update only affected claims.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate with no Extension Pack. Reconstruct and then refresh the documented access-policy history of Crossref and OpenAlex. Begin with official API documentation and dated provider announcements; inspect wrapper documentation/code as a secondary view. Distinguish announcement, proposed effective date, actual implementation, publication and your retrieval date. Create an explicitly retrospective baseline only from dated originals you obtain, then a separately identified current-documentation revision. Inaccessible historical states remain gaps; never invent an earlier policy.

Use audit and diagnose-research-failure to identify affected claims, then refresh to update their evidence, interpretation and review dependencies. Preserve still-valid historical statements and unaffected records. Do not treat an accepted request parameter or a recent request date as proof of enforcement. Allow 20 searches and 64 source reads/actions across the entire task, with finalisation reserved and no new paid access, provider runs or external communications.

Write research/l4-01/research.md, baseline.md, temporal-table.md, change-record.md and evaluation/audit.md beneath research/l4-01/. Record exact source versions and locators, support/contrary evidence, actual changes, preserved records and valid-as-of limits. Keep audit inputs fixed and make subsequent rechecks revision-specific. Read an existing run before modifying it. Return actual paths and truthful findings; distinguish retrospective reconstruction, current inspection and a measured service test.
```

## Expected artefacts

- `research/l4-01/research.md`
- `research/l4-01/baseline.md`
- `research/l4-01/temporal-table.md`
- `research/l4-01/change-record.md`
- `research/l4-01/evaluation/audit.md`

## Evaluation contract

Evaluate temporal semantics and smallest-sufficient refresh.

Retrospective versus current policy, announcement and implementation; FX03/TM02/TM03. Producer/evaluator refresh and diagnosis.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L4-01`; L06/L07; K11/K16. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).
