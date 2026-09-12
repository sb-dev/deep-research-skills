# Fixed-input audit criteria

Contents: Evaluation principles; Evaluation layers; Domain quality dimensions; Submission and review contract; Retrieval evaluation; Source and evidence evaluation; Citation and provenance evaluation; Synthesis evaluation.

## Evaluation principles

1. Structural correctness is not research quality.
2. Retrieval, evidence quality, citation support and synthesis can fail independently.
3. A material mandatory failure is never averaged away.
4. Evaluators read fixed submissions and write separate results.
5. Expected outcomes are defined independently of the candidate output.
6. Synthetic fixtures remain explicitly synthetic.
7. Mutable-source cases distinguish environmental change from model regression.
8. Approved evidence is preserved during repair.
9. A benchmark score never grants source, budget, publication or professional authority.
10. External benchmarks inform design but do not define this project's complete quality model.

Verdicts are:

```text
PASS
FAIL
BLOCKED
NOT APPLICABLE
```

`NOT APPLICABLE` requires a case-grounded reason. Missing mandatory evidence is `BLOCKED` or `FAIL` as defined by the criterion, not PASS.

## Evaluation layers

| Layer | Scope | Oracle and repair |
|---|---|---|
| L01 Structural integrity | Required metadata, IDs, source/citation references, valid structure, duplicate IDs, self-containment and selective-package integrity. | Exact schema/reference expectations. Repair the broken field/path/package dependency. |
| L02 Retrieval behaviour | Known-source recall, reformulation, persistence, source diversity, primary recovery, specialist-source choice and duplicate avoidance. | Defined gold evidence/corpus where available plus method requirements. Repair query/route/access, not final prose. |
| L03 Source/evidence quality | Directness, authority/method, independence, freshness, temporal fit, selection, contrary evidence and extraction fidelity. | Original sources and claim-relative method. Repair source relation, extraction or eligibility. |
| L04 Citation/claim support | Citation existence, entailment, completeness, placement, source-claim mismatch and unsupported inference. | Exact report proposition versus inspected evidence. Repair locator/extraction/claim/inference. |
| L05 Synthesis quality | Question coverage, logic, cross-source integration, contradiction handling, uncertainty, alternatives, scope, decision relevance and evidence-preserving clarity. | Task-specific supported findings and limits. Repair grouping/argument/wording; new facts require support. |
| L06 Preservation/diagnosis/repair | Root-cause diagnosis, preserved unaffected work, necessary delta retrieval and dependent updates. | Expected changed/preserved sets and actual operation record. Broaden if dependency isolation is uncertain. |
| L07 Temporal/refresh | Supersession, publication/event/effective dates and partially valid cached evidence. | Frozen temporal table plus actual update evidence. Preserve historical truth and repair affected current claims. |
| L08 Extension Packs | Activation, non-activation, precedence, source/method change, quality criteria, differential behaviour and repair. | Core invariants plus selected profile criteria. Cosmetic or overriding pack behaviour fails. |
| L09 End-to-end research | Fifteen progressive examples and independent-topic hold-outs. | Full prompt, source/evidence/output contract and required review. Limitations outcomes pass only when allowed and actual required behaviours occurred. |
| L10 External installation | Clean install, discovery, local references, real quick-start outputs, evaluation, selective install and implemented pack. | Observed installation/execution at an exact repository revision and agent version. |

L01–L08 can include design/reference controls before the product exists. L09/L10 require actual candidate execution to make behavioural/product claims.

## Domain quality dimensions

Retain K01–K16 as separate dimensions:

| ID | Dimension | Primary evidence |
|---|---|---|
| K01 | Question and use fit | Brief-to-answer mapping and intended-use boundary |
| K02 | Coverage honesty | Actual search/selection boundary versus coverage claim |
| K03 | Source access and provenance | Exact representation, access extent, locator and transformations |
| K04 | Evidence-unit integrity | Duplicate/report/version/study/origin relationships |
| K05 | Applicability and methodological fitness | Method appropriate to the inference |
| K06 | Independent support | Distinct evidential origins |
| K07 | Extraction fidelity | Context, units, denominator, negation and qualifications |
| K08 | Counterevidence treatment | Eligible negative/null/conflicting evidence retained |
| K09 | Inferential validity | Explicit premises and justified reasoning |
| K10 | Uncertainty communication | Limits survive synthesis without fake precision |
| K11 | Temporal applicability | Event/publication/effective/retrieval/valid-as-of integrity |
| K12 | Review adequacy | Exact revision and competent review process |
| K13 | Reconstructability and reporting | Inspectable path from question to evidence to conclusion |
| K14 | Proportionality | Bounded useful work; resource exhaustion is not sufficiency |
| K15 | Responsible authority | Source/processor/audience/review/commitment permissions |
| K16 | Repairability and continuity | Smallest sufficient repair and preserved valid work |

No global numeric score replaces these dimensions.

## Submission and review contract

A submission identifies:

- case/revision;
- candidate skill/repository commit;
- host/model/tool versions actually known;
- source/corpus identities;
- actual queries and relevant inspected sources;
- operation outcomes and limits;
- output paths/content identities;
- actual resource use and outstanding reservations where known;
- actual date precision.

A review identifies:

- exact submission revision;
- criterion;
- evidence;
- verdict;
- severity;
- assessed/unassessed scope;
- smallest repair;
- actual reviewer/process.

Evaluation does not silently repair its input.

## Retrieval evaluation

Use controlled known-answer cases to measure, where meaningful:

- required source recall within a defined corpus;
- primary-source recovery;
- query reformulation;
- continuation handling;
- specialist-source selection;
- duplicate avoidance;
- unnecessary acquisition;
- bounded stopping.

Do not report global web recall without a defined gold universe.

Correct final text without retrieval evidence does not pass a retrieval case whose purpose is source recovery.

## Source and evidence evaluation

Check:

- source type and directness;
- relevant authority/method;
- actual access;
- eligibility;
- relationship to underlying study/event/data;
- independence;
- temporal fit;
- contrary evidence;
- extraction fidelity.

A citation syntax pass cannot establish these properties.

## Citation and provenance evaluation

Evaluate independently:

- citation target resolution;
- proposition entailment;
- completeness for material claims;
- placement;
- source/claim mismatch;
- transformation provenance;
- exact version/locator;
- audience/access restrictions.

Bibliographic correctness can PASS while entailment FAILS.

## Synthesis evaluation

Assess:

- coverage of the actual question;
- logical argument;
- compatible integration;
- contradiction handling;
- alternatives;
- uncertainty;
- scope discipline;
- decision relevance;
- clarity without losing evidence.

Length, source count and confidence tone are not quality proxies.
