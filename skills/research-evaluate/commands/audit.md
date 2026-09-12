# audit

Apply the [common command contract](../references/command-contract.md).

**Purpose.** Independently inspect research quality against an explicit brief and fixed evidence/report revisions. Default scope covers all nine audit dimensions; a declared focus runs selected dimensions only.

**Inputs and preconditions.** The actual brief, exact target revision, permitted support package and applicable criteria/pack version. Input may come from any producer. The evaluator has source-reading permission and a separate output location, not authority to edit the research under review. Record actual reviewer identity/role and method without inventing human independence.

**Operation.** Run structural reference checks separately from substantive support checks. Examine source quality, independence, coverage, claims, citations, freshness, contradictions, uncertainty and reproducibility as requested. Compare propositions with sources and method requirements, not with the author’s verdict. Identify omitted scopes and inaccessible evidence. An agent’s second pass can be independent of authoring responsibilities without being an independent human expert.

**Outputs and write scope.** Write a new A11 review with target revisions, criterion-level PASS/FAIL/BLOCKED/NOT APPLICABLE, evidence, severity, exact defect locations, assessed/unassessed scope and smallest repair route. Do not modify A01–A10, input fixtures, expected outcomes or prior reviews. Audit results never create publication authority.

**Completion and review.** Every requested criterion has a supported result; NOT APPLICABLE includes rationale and missing evidence is not PASS. A focused audit cannot claim whole-report acceptance. No averaged score compensates for a mandatory failure. Record whether the process was a producer self-check, separate agent review or actual qualified human review.

**Failure and smallest repair.** Return diagnostic findings for the owning producer; do not silently correct them during audit. If sources or mandatory expertise are unavailable, mark the affected criterion BLOCKED and state the exact need. After repair, audit the changed revision and dependent scope anew.

**Independent use and evaluation reason.** Can review a third-party report without installing deep-research. Test a plausible report with a valid but non-entailing citation, hidden counterevidence, stale review hash and an author-provided PASS claim. Verify input bytes remain unchanged and scope limitations remain visible.

**Example invocation.** Use research-evaluate, operation audit, scope claims,citations,freshness. Read the exact report and permitted supporting records in research/. Write evaluation/audit.md without modifying the inputs. Report unassessed dimensions and do not use the author’s self-check as ground truth.

## Audit focus semantics

The `audit` command accepts a declared scope of source-quality, source-independence, coverage, claims, citations, freshness, contradictions, uncertainty or reproducibility. Omitting scope requests all nine. Each focus is independently callable and scored; grouping related checks under one command does not merge their verdicts. For example, citations checks bibliographic identity, placement and the specific supported proposition; claims additionally checks inference, scope and assumptions. A DOI syntax pass cannot satisfy either semantic concern by itself.

A reviewer may inspect linked evidence beyond the targeted claim to understand a dependency, but records actual scope and does not silently expand acquisition, publication or repair authority. Report-wide acceptance requires every applicable mandatory dimension and required review; a focused successful check is never relabelled an overall PASS. Use the local audit-criteria reference and task-specific oracle; do not invent numeric acceptance thresholds.
