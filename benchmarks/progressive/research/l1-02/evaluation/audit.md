# L1-02 — Frozen Python requirement audit

Audit A1, 2026-09-13. Submitted proposition, unchanged:

> Open Deep Research requires Python 3.11 in every supported use.

Actual operation: research-evaluate/audit, scopes **claims and citations**, no Extension Pack. Primary assistant acting as evaluator of the user-supplied proposition; no producer report was rewritten. Source-checkout skill contract0.1 at b9d262b4bd2ffa73d35b520f98629e7eae0b7da7. Exact task: examples/level-1-python-requirement-claim-audit/README.md at that revision. No prior audit existed.

All three originals were fetched through GitHub at the same frozen Open Deep Research commit **1b7d2e80db9faa586165c60e09096dbbfd483a64** and inspected on 2026-09-13:

| Source and exact locator | Observed declaration | Scope |
|---|---|---|
| [pyproject.toml](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/pyproject.toml), `[project].requires-python` | `>=3.10` | Package declaration |
| [langgraph.json](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/langgraph.json), `python_version` | `3.11` | This server/deployment configuration |
| [README.md](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/README.md), Quickstart step4 | Local LangGraph command explicitly selects `--python 3.11` | Documented example invocation |

| Criterion | Verdict | Finding and smallest repair |
|---|---|---|
| Claims: universal scope | FAIL, material | Server/example settings do not establish every supported use. The package declares a broader constraint. Narrow the proposition to the actual documented environment if the owner later authorises a revision. |
| Citations: identity and entailment | FAIL for universal entailment; identity verified | All three same-commit originals resolve, but neither the server setting nor example entails the universal claim. Cite exact fields with their separate scopes. |
| Submission preservation | PASS | Proposition retained verbatim; no source or submission edited. |

The documentary claim is unsupported as written. This audit does **not** establish that any particular Python version successfully runs the package: nothing was installed or executed. Other supported environments and transitive dependency compatibility were not tested.

Omitted audit scopes: source-quality, source-independence, coverage, freshness, contradictions, uncertainty and reproducibility. Scope-related qualifications above support the requested claim/citation assessment; they are not seven additional completed audits or whole-project acceptance.

Execution: bounds of 3 queries/8 reads set in Stage20 plan before acquisition; actual 0 queries/3 same-commit file reads. Original fields and README context were compared during local review; remaining allowance unused. Tools: GitHub connector and local file tools, ChatGPT Work Mode. Output research/l1-02/evaluation/audit.md; audit complete with FAIL finding, no compatibility-test claim.
