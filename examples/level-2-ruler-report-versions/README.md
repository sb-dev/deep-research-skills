# L2-02 — RULER report versions

[All research examples](../../README.md#learn-by-researching)

## Problem

Compare revisions of one work without counting them as independent studies.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research and research-evaluate with no Extension Pack. Compare versions 2 and 3 of “RULER: What's the Real Context Size of Your Long-Context Language Models?” Resolve the official arXiv work and version history, then inspect the two versioned originals. Compare model population, task coverage, effective-context definition and limits of transfer to a research workflow. Preserve each version's bibliographic identity and exact supporting locators. Do not count the versions as independent studies or silently combine their model populations. Inspect decisive figures/tables in their original representation. Separate stable, revised and unresolved findings, and do not convert a benchmark-specific threshold into a universal acceptance rule.

Use a bounded comparison plan, extraction, evidence analysis, synthesis and separate audit. Allow at most 6 searches and 18 source reads/actions, with effort reserved for support checks. Use already-authorised access only; do not buy papers or execute a model benchmark. Missing full text remains an explicit limitation.

Write research/l2-02/research.md and research/l2-02/evaluation/audit.md. Include report/work relationships, contrary or changed passages, uncertainty and the actual inspected scope. Keep the audit submission fixed. Preserve existing revisions and valid evidence on resumption. Return actual paths and findings, not a claimed replication or installed-skill performance result.
```

## Expected artefacts

- `research/l2-02/research.md`
- `research/l2-02/evaluation/audit.md`

## Evaluation contract

Evaluate work/report linkage, revised scope and threshold applicability.

Work/report/version linkage and changed population; FX06/FX09. Producer and evaluator.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L2-02`; L03/L05; K04/K05/K06. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).

## Recorded execution

[Progressive run](../../benchmarks/progressive/research/l2-02/research.md) contains the actual source-checkout output and its stated support and access limits. See the [separate review](../../benchmarks/progressive/research/l2-02/evaluation/audit.md) for assessed claims and remaining gaps.
