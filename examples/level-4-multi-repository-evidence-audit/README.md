# L4-03 — Multi-repository evidence audit

[All research examples](../../README.md#learn-by-researching)

## Problem

Trace capability evidence across a bounded repository set and repair only the affected evidence chain.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate with open-source-ecosystem explicitly selected and its revision recorded. Build an evidence map for twelve repositories: langchain-ai/open_deep_research; assafelovic/gpt-researcher; stanford-oval/storm; docling-project/docling; grobidOrg/grobid; adbar/trafilatura; microsoft/playwright-cli; microsoft/playwright-mcp; github/github-mcp-server; duckdb/duckdb; UKGovernmentBEIS/inspect_ai; promptfoo/promptfoo. Pin the actual inspected refs. Limit the first pass to identity, role, documentation and the original code/configuration needed for one consequential claim per repository. Follow no more than 36 selected source artefacts overall.

Distinguish wrappers/shared engines from independent capability evidence. Audit two consequential cross-source claims and perform targeted follow-up on the most material unresolved one. Demonstrate repair on an observed defect, or on a clearly labelled single broken-locator mutation of a copy if no natural defect is found. Preserve original sources and unrelated accepted claims. Allow 20 searches and 64 source reads/actions total, with review reserved. No new paid runs, installations, purchases or external communications are authorised.

Write research/l4-03/research.md, ecosystem-map.md, claim-audit.md, change-record.md and evaluation/audit.md beneath research/l4-03/. Record source access, evidence/support, unresolved contradictions, exact revisions and affected rechecks. Return actual paths and a traceable ecosystem assessment, not a popularity ranking, vulnerability certificate or claim that all tools were installed.
```

## Expected artefacts

- `research/l4-03/research.md`
- `research/l4-03/ecosystem-map.md`
- `research/l4-03/claim-audit.md`
- `research/l4-03/change-record.md`
- `research/l4-03/evaluation/audit.md`

## Evaluation contract

Evaluate multi-hop provenance, independence and targeted follow-up at source-set scale.

Shared engines, sampled histories, bounded follow-up and locator repair; FX01/FX10/BG02, PD02. OSS pack.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L4-03`; L02/L03/L06/L08; K02/K06/K16. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).

## Recorded execution

[Progressive run](../../benchmarks/progressive/research/l4-03/research.md) contains the actual source-checkout output and its stated support and access limits. See the [separate review](../../benchmarks/progressive/research/l4-03/evaluation/audit.md) for assessed claims and remaining gaps.
