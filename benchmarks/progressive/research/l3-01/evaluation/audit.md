# L3-01 — Fixed-input audit and scoped repair review

2026-09-13. Primary assistant separately reviewed producer L3-01-r1, then fixed r2 after the producer's scoped correction. Actual research-evaluate/audit and diagnose-research-failure; scholarly-evidence0.1.0/core0.1; source-checkout execution. Exact r1 files retained under revisions/r1/. Audit did not modify them.

**A1/D1.** C1's wording that Gemini exceeds the tested maximum risked promoting Table3's >128K label to measured beyond-grid performance. Parent inspected the original table: performance is above85.6 through the maximum tested128K. Diagnosis: narrow only that inference. G3's original LongBench implementation route was also unresolved. Five actual GitHub review reads recovered root contents, main ref, original-benchmark subtree, pinned LongBench/README.md and LongBench/pred.py at2e00731f8d0bff23dc4325161044d0ed8af94c1e. README links2308.14508 and21tasks/sixcategories. get_pred visibly retains first/last token halves for overlength inputs before chat wrapping and uses nonsampling, one-beam generation. This is retained original-benchmark code at the inspected current commit, not proven historical experimental bytes or a run.

**A2.** Producer r2 preserves all three r1 copies and narrows C1, updates G3/source map and the dependent proposal limitation. Parent reread r2: those changes correctly reflect D1; unrelated methods and conditional decisions remain. Aggregate4queries/32sourceactions, leaving4of36; no optional acquisition beyond the discriminating gap. RULER table support was already inspected directly in this session; no new model/code execution.

| Scope | Verdict | Evidence / limits |
|---|---|---|
| Source quality | PASS for inspected originals | Author/publisher sources and pinned retained implementation appropriately scoped. |
| Independence | PASS | Work/report/study identities distinguish revisions, benchmark generations and dataset reuse. |
| Coverage | PASS for named-work comparison; application conclusion conditional | Required works and implementations addressed; current team task evidence remains a proposed evaluation. |
| Claims | PASS for corrected C1/G3 and inference boundaries; BLOCKED for complete independent verification of every C2–C4 method detail | No blanket LC/retrieval winner; favorable LC counterevidence retained. Parent did not independently inspect every cited paper passage. |
| Citations | PASS for inspected RULER/LongBench implementation dependencies; remaining paper-level entailment only partially checked | Exact newcommit/symbol locators are substantive; source-map listings alone do not prove all extraction. |
| Freshness | PASS as historical study comparison | Empirical2023–2024configurations not promoted to2026performance; OpenReview/direct later-comparator status gaps disclosed. |
| Contradictions | PASS | LongBench-generation distinction, Gemini range qualification and optional comparator's narrative/table discrepancy retained. |
| Uncertainty | PASS | Proposal is unexecuted; no whole-workflow benchmark or universal threshold inferred. |
| Reproducibility | LIMITED | Exact queries/actions and newly pinned code are recoverable; other mutable implementation READMEs and underlying experimental environments unpinned. |

Pack-aware checks: PASS for explicit compatible activation, work/report/version linkage, eligible counterevidence and method-transfer limits. Core invariants retained. Scoped repair is independently rechecked; the audit is complete with its stated support limits, and is not a report-wide unrestricted PASS or a claim that the proposed evaluation ran.
