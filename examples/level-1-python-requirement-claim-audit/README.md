# L1-02 — Python requirement claim audit

[All research examples](../../README.md#learn-by-researching)

## Problem

Audit a frozen proposition against package, server and README evidence without rewriting it.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use only the installed research-evaluate skill, operation audit, scopes claims and citations, with no Extension Pack. Audit this submitted proposition without rewriting it: “Open Deep Research requires Python 3.11 in every supported use.” Use langchain-ai/open_deep_research at commit 1b7d2e80db9faa586165c60e09096dbbfd483a64, especially pyproject.toml, langgraph.json and README.md. Distinguish the package's declared Python constraint from an example or server configuration and any separately documented requirements. Cite the exact fields. Do not install the project, execute its code or infer runtime compatibility from metadata alone.

Allow at most 3 search queries and 8 source reads/actions, aggregated across the task. Use only already-authorised read/file tools; no new paid service, credential disclosure or external communication. Reserve effort for source-to-proposition checking. A missing original remains a blocked criterion, not a pass.

Write a new research/l1-02/evaluation/audit.md. Preserve the submitted claim verbatim in the assessment, identify the frozen source revisions, give criterion-level findings and state omitted audit scopes. Do not modify original inputs or silently apply a repair. Read and preserve an existing audit before creating a new revision. Return the actual output path, supported finding and limitations; do not label documentary inspection as an installed compatibility test.
```

## Expected artefacts

- `research/l1-02/evaluation/audit.md`

## Evaluation contract

Evaluate claim scope, source entailment and input preservation.

Package/deployment conflation and unchanged audit submission; FX10/AU01. Evaluator only.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L1-02`; L01/L04; K05/K12. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).

## Recorded execution

[Progressive run](../../benchmarks/progressive/research/l1-02/evaluation/audit.md) contains the actual source-checkout output and its stated support and access limits. Review scope is labelled in the output.
