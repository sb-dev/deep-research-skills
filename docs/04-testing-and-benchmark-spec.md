# Deep Research Skills Testing and Benchmark Specification

**Status:** Canonical design specification  
**Version:** 1.0  
**Date:** 11 September 2026  
**Implementation state:** Evaluation architecture specified. Reference/design checks exist from Stage 13; installed-product measurements remain pending later stages.

## 1. Purpose

This specification owns:

- evaluation layers;
- benchmark suites;
- case contracts;
- domain quality dimensions;
- retrieval evaluation;
- source/evidence evaluation;
- citation/provenance evaluation;
- synthesis evaluation;
- preservation/repair and temporal evaluation;
- progressive-example coverage;
- Extension Pack differential evaluation;
- regression policy;
- release gates;
- measured-evidence reporting.

Research production semantics belong to [01](01-deep-research-skills-system-spec.md) and [02](02-deep-research-skills-workflows-and-artifacts-spec.md). Packaging/installability belongs to [03](03-deep-research-skills-repository-and-contracts-spec.md).

## 2. Evaluation principles

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

## 3. Benchmark suites

### 3.1 Contract and regression suite

Purpose: fast, deterministic checks of exact typed properties such as IDs, dates, relationships, permissions, counting, stopping and preservation.

Evidence: explicit synthetic and mutation fixtures.

Limit: passing these checks does not establish arbitrary prose entailment, current retrieval quality or installed-agent performance.

### 3.2 Frozen research replay suite

Purpose: replay research against an identified permitted source corpus with fixed evidence and expected support.

Records:

- exact source/corpus version;
- case version;
- gold evidence where lawfully established;
- allowed operations;
- expected claim/support behaviour.

A changed source snapshot requires a new case version.

### 3.3 Live-source research suite

Purpose: test current discovery, primary-source recovery, access limits and temporal truthfulness.

A current-web case re-establishes the answer from originals. A changed fact is not automatically a regression. The benchmark records:

- source changes;
- access failures;
- current versions;
- valid-as-of basis.

### 3.4 Installed-product suite

Purpose: execute the actual installed skills from a clean consumer project.

It covers:

- skill discovery;
- skill-local references;
- Level 1 quick start;
- research artefacts;
- evaluator operation;
- selective installation;
- at least one implemented pack.

This suite is the product gate owned by the later installation stages. A copied repository or design checker cannot substitute for it.

## 4. Evaluation layers

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

## 5. Domain quality dimensions

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

## 6. Failure taxonomy

The benchmark and regression suite preserves F01–F20 from [02](02-deep-research-skills-workflows-and-artifacts-spec.md).

Priority regression fixtures include the twelve explicitly required classes:

1. three articles repeating one original source presented as triangulation;
2. search-result snippet contradicts the full source;
3. stale official page versus current official page;
4. high-ranking SEO summary versus primary documentation;
5. retracted/corrected scholarly source;
6. multiple reports of one study treated as several studies;
7. paywalled primary source with accessible secondary reporting;
8. conflicting high-quality sources;
9. unsupported confident synthesis;
10. citation supports an adjacent fact but not the stated claim;
11. broad report misses a required subquestion;
12. research loop continues after useful stopping criteria are met.

Each fixture identifies the owning layer and smallest repair.

## 7. Temporal and repair cases

Required temporal cases cover:

- old authoritative source conflicts with newer official source;
- publication date differs from event/effective date;
- cached evidence remains valid for some claims but not others.

Required preservation cases verify that:

- a weak claim is identified;
- unaffected evidence remains unchanged;
- only necessary retrieval is rerun;
- dependent synthesis changes;
- unrelated report sections are not regenerated without reason.

When a natural defect is unavailable for a benchmark, a deliberate mutation is allowed only if labelled as synthetic and the original remains intact.

## 8. Case contract

Every benchmark case records:

### Identity

- case ID and version;
- split: development, regression, teaching or hold-out;
- synthetic versus real-source character;
- owning layer/requirement;
- licensing/exposure limits.

### Task

- exact prompt;
- required output;
- intended use;
- mandatory subquestions;
- selected skills/commands/packs;
- prior approved decisions;
- allowed sources/processors;
- prohibited side effects.

### Evidence universe

- source identity/version;
- actual locators/access;
- snapshots where lawful;
- gold evidence where established;
- mutable-source mode;
- known unavailable material.

### Oracle

- atomic criterion ID;
- mandatory/optional state;
- expected behaviour/proposition;
- source/logic;
- tolerances if justified;
- disallowed behaviour;
- reviewer competence requirement.

The target model's self-verdict is never the oracle.

### Execution envelope

- bounded searches/reads/data/compute;
- parent aggregate;
- outstanding jobs;
- finalisation reserve;
- permitted retry/stopping behaviour.

### Repair contract

- defect;
- owning operation;
- expected affected dependencies;
- records that must remain unchanged;
- allowed new acquisition;
- recheck scope.

### Provenance

- case author/source inspection dates;
- source/corpus identities;
- case/oracle revisions;
- changes and rationale.

## 9. Submission and review contract

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

## 10. Retrieval evaluation

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

## 11. Source and evidence evaluation

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

## 12. Citation and provenance evaluation

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

## 13. Synthesis evaluation

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

## 14. Progressive-example coverage

The fifteen primary examples are canonical teaching and eventual end-to-end cases:

```text
Level 1: EX-L1-01, EX-L1-02, EX-L1-03
Level 2: EX-L2-01, EX-L2-02, EX-L2-03
Level 3: EX-L3-01, EX-L3-02, EX-L3-03
Level 4: EX-L4-01, EX-L4-02, EX-L4-03
Level 5: EX-L5-01, EX-L5-02, EX-L5-03
```

The exact prompts and expected artefacts remain in the accepted progressive-example design until Stage 17 materialises public example files. This specification maps them to benchmark responsibilities:

| Level | Main evaluation responsibility |
|---|---|
| 1 | bounded source recovery, exact claim support and truthful temporal scope |
| 2 | comparison criteria, evidence relationships and reproducible small calculations |
| 3 | complete focused report, decision relevance and pack-aware method where selected |
| 4 | contested/large/mutable evidence plus repair and preservation |
| 5 | research programme consistency, pack qualification and cross-domain handoff |

The three examples per level are complementary rather than cosmetic variants.

## 15. Extension Pack differential suite

Both initial profiles require paired evaluation:

```text
core
vs
core + selected pack
```

Comparable conditions fix:

- research question;
- permitted source universe;
- consumer purpose;
- authority;
- output purpose;
- core invariants.

A pack must create an observable specialist behaviour, not only metadata or extra headings.

### 15.1 `scholarly-evidence`

Required observable changes include one or more of:

- work/report/version linkage affecting unit counting;
- method-specific appraisal;
- status/eligibility handling;
- correct boundary on benchmark-threshold transfer.

Core findings and uncertainty must not regress.

### 15.2 `open-source-ecosystem`

Required observable changes include one or more of:

- cross-file package/config/environment reconciliation;
- maintenance evidence separated from readiness;
- static failure-path observation linked to a specific required execution test;
- immutable revision and licence-scope handling.

Popularity cannot substitute for task suitability.

### 15.3 Pack controls

Test:

- explicit activation;
- non-activation;
- unknown/incompatible selection;
- explicit instructions over pack defaults;
- locked decisions over pack defaults;
- ambiguous conflicts;
- multi-pack scope conflict;
- cosmetic-only pack;
- unsafe pack path;
- evaluator mutation;
- scoped deactivation/repair;
- domain overreach.

Pack comparison evidence from Stage 11 is a source-backed procedural demonstration, not an installed isolated-agent reliability estimate.

## 16. External benchmark references

Use lessons, not leaderboard thresholds:

| Family | Adopted lesson | Not adopted |
|---|---|---|
| BrowseComp | Hard discovery with readily checkable answers; retrieval trace separate from answer. | Its task set, unlimited attempt assumptions or answer accuracy as report quality. |
| DeepResearch Bench | Separate report criteria from citation support and record evaluator configuration. | Relative leaderboard score as a release threshold. |
| BrowseComp-Plus | Controlled corpus/retrieval separation. | A claim of open-web recall or redistribution of its corpus by default. |
| ResearchRubrics | Fine-grained mandatory/optional/negative criteria. | Averaging away a mandatory material failure. |
| FINDER/DEFT | Diagnosable requirement/failure categories. | Model-assigned causal diagnosis without source/operation evidence. |

External benchmarks are optional supplemental evidence. The domain benchmark remains owned here.

## 17. Regression policy

```text
escaped research defect
  → diagnose owning layer
  → create smallest reproducible fixture
  → add deterministic or semantic evaluation
  → verify the repair
  → retain fixture as regression protection
```

A regression fixture records the original defect character without exposing prohibited data. When private evidence cannot be retained, create the smallest lawful surrogate that reproduces the responsible mechanism and label it as a surrogate.

Do not mutate expected outcomes to fit a new model. If the oracle/source was wrong, version the case and rerun affected baselines.

## 18. Release gates

Release readiness is a conjunction of applicable mandatory gates, not an average.

### Specified

Requires:

- accepted canonical specifications;
- no claim of implemented behaviour.

### Scaffolded

Requires:

- production surfaces actually exist;
- package/spec/reference structure is coherent;
- no claim of working end-to-end behaviour.

### Working

Requires:

- a real installed end-to-end research example;
- actual skill outputs;
- required evaluation;
- no source-checkout dependency for the demonstrated path.

### Benchmarked

Requires:

- executable domain benchmark;
- reproducible fixtures;
- separable retrieval/evidence/citation/synthesis failures;
- at least one regression detectable;
- implemented pack evaluation where packs are implemented.

### Mature

Requires:

- family contract conformance;
- six canonical specs;
- five levels × three primary examples with prompts;
- operational evaluation/regression;
- pack contract/catalogue and pack authoring;
- core usable without packs;
- clean external installation;
- quality claims backed by measured evidence or explicitly unmeasured.

A severe permission, provenance, unsupported-claim or required-review failure blocks release regardless of other scores.

## 19. Measured evidence status

As of this specification:

**Actually executed design/reference evidence:**

- Stage 11 source-backed core-versus-pack procedural comparisons on two public source sets;
- Stage 13 synthetic/reference case checker with positive, negative, orthogonality, package, pack and scorer-mutation controls;
- Stage 13 document/inventory checker with corrupted-control detection.

**Not yet measured:**

- installed skill research quality;
- clean external installation;
- end-to-end success rate across the fifteen examples;
- provider speed/cost advantage;
- general citation-entailment accuracy;
- empirical calibration;
- independent human review reliability;
- isolated pack effect size.

Do not convert design evidence into product benchmark claims.

## 20. Acceptance

This testing specification is implemented faithfully when failures in retrieval, evidence quality, citation support and synthesis can be observed separately, repair preserves valid work, pack behaviour can be compared against core, and release status is derived only from actual applicable evidence.
