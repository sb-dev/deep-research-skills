# Deep Research Skills Extension Pack Catalogue

**Status:** Canonical design catalogue  
**Version:** 1.0  
**Date:** 11 September 2026  
**Catalogue state:** Two initial packs selected at design stage. Neither is yet production-bundle or clean-install validated.

## 1. Purpose

This catalogue records the curated initial research Extension Packs selected by the accepted bootstrap work.

A catalogue entry answers:

- what the pack specialises;
- when it should and should not be used;
- what research grammar it changes;
- which core operations it affects;
- what remains invariant;
- why it was selected;
- its exact showcase prompt;
- pack-specific evaluation expectations;
- its actual maturity/evidence state.

Pack semantics and qualification are defined in [05 — Customisation Packs](05-deep-research-skills-customisation-packs-spec.md).

## 2. Catalogue summary

| Pack | Purpose | Selected because | Current state |
|---|---|---|---|
| `scholarly-evidence` | Research bounded scholarly questions with explicit work/report/version units and method-specific appraisal. | Publication-unit identity and method-transfer rules materially change counting, appraisal and synthesis. | Designed; source-backed procedure-demonstrated; not installed-tested. |
| `open-source-ecosystem` | Assess open-source adoption evidence using exact revisions, code/package/licence/maintenance evidence and executed-validation boundaries. | Repository research requires cross-file reconciliation and static-versus-executed assurance that core should not universalise. | Designed; source-backed procedure-demonstrated; not installed-tested. |

Both use core contract `stage-10-2026-09-10`, design version `0.0.1`, and explicit activation only.

## 3. Pack: `scholarly-evidence`

### 3.1 Production profile

**Purpose:** Research a bounded scholarly question with explicit work/report/version units and method-specific appraisal.

**Use when:**

- scholarly works, reports or revisions can be double-counted;
- publication/status matters;
- the research needs study/report linkage;
- domain method changes source appraisal;
- benchmark or study findings must be transferred carefully to another use.

**Do not use as automatic:**

- systematic-review certification;
- clinical or professional advice;
- proof that dual screening occurred;
- a universal model-accuracy or confidence method.

### 3.2 Specialisation dimensions

| Dimension | Profile |
|---|---|
| Source ecology | Use suitable scholarly identifiers, author/publisher originals and status records. Supplied-paper tasks need not search every database. |
| Search strategy | Expand vocabulary/citation paths only within the brief; preserve whether work is bounded or formal-review-like. |
| Inclusion/exclusion | Declare eligibility by question/design; retain adverse/null evidence; inaccessible full text differs from exclusion. |
| Source appraisal | Appraise actual design, metrics and transfer limits. Do not indiscriminately apply clinical tools to computing benchmarks. |
| Research methods | Link reports and revisions to the underlying work/study before counting or synthesis. |
| Synthesis structure | Present findings with unit linkage, method limits and unresolved applicability. |
| Quality criteria | Check support, status, report linkage, counting, uncertainty and completeness claim. |
| Reporting conventions | Use exact work/version locators and declare the actual review type. |

### 3.3 Core operation effects

| Operation | Specialised behaviour | Observable consequence |
|---|---|---|
| `plan` | Define scholarly unit, eligibility and appraisal method. | Plan states which report/study/version is counted. |
| `discover` | Resolve scholarly identities and status. | Candidates, eligible records, unavailable records and superseded representations are distinct. |
| `extract-evidence` | Capture method, task/population, measure, units and exact locators. | Abstract-only access cannot supply unseen methods. |
| `analyse-evidence` | Link reports/revisions before counting; assess transfer of thresholds/findings. | A revision cannot become an independent study merely through a new version. |
| `synthesise` | Expose design limits and unit structure; keep implications conditional. | Benchmark thresholds are not universal application acceptance values. |
| `refresh` | Check corrections/revisions and repair only affected claims. | Unchanged historical findings retain their original basis. |
| `audit` | Add report-linkage, status and method-transfer criteria. | Bibliographic identity and substantive support have separate verdicts. |

### 3.4 Preserved core invariants

The pack does not change:

- question/consumer authority;
- permitted source/processor boundary;
- evidence/claim separation;
- bounded effort;
- uncertainty requirements;
- revision history;
- required independent/human review.

### 3.5 Selection rationale

This pack was selected because scholarly evidence contains specialist identity and appraisal problems that cannot be reduced to ordinary URL-level provenance.

The accepted comparison used RULER as one research work with multiple versions. The pack made publication-unit handling and threshold transfer explicit while preserving the core conclusion and uncertainty.

The comparison demonstrates a procedural effect on a real public-source task. It does not estimate a general improvement rate, run models, or establish systematic-review competence.

### 3.6 Showcase

**Premise:** A team needs evidence about advertised long-context capacity, not a model purchasing recommendation.

**Source boundary:** The authors' arXiv record 2404.06654 and its v2/v3 representations.

**Expected specialist behaviour:** Link versions to one work identity and separate benchmark-specific effective-context criteria from an application acceptance rule.

**Exact generation prompt:**

```text
Use the accepted deep-research procedure with the scholarly-evidence profile specified in the Stage 11 profiles file. Answer: what does RULER establish, and not establish, about relying on an advertised context window for a research assistant? Use only the authors' arXiv record 2404.06654 and its v2/v3 paper representations. Distinguish versions, direct findings, inference and unknowns. Give a supported answer, source locators, temporal limits and the next justified verification step. Do not run a model, claim an exhaustive literature review, infer current product rankings or approve a product. Preserve any valid finding even if it also appears in another representation. Use the supplied Stage 11 source register; new retrieval is limited to this same source universe. Record actual access. Stop when this bounded question is answered and review the exact wording. Write a separate pack output without editing the core output.
```

This is the accepted design-stage showcase prompt. Production implementation must copy required method knowledge into pack-local files rather than depend on the research-log path named by this historical prompt.

### 3.7 Pack-specific evaluation

Required cases include:

- requested activation;
- unrequested non-activation;
- same-work revision linkage;
- adverse evidence remains eligible;
- abstract-only access boundary;
- threshold-transfer limitation;
- explicit/locked precedence;
- scoped refresh preservation.

Differential acceptance requires an observable effect on unit counting, appraisal, inference or follow-up. Additional headings or pack-name metadata alone fail.

### 3.8 Maturity

```text
designed: PASS
procedure-demonstrated on bounded public source task: PASS
production pack bundle: NOT YET IMPLEMENTED
clean installed activation: NOT YET MEASURED
fresh isolated differential reliability: NOT YET MEASURED
catalogue-ready production state: NOT YET CLAIMED
```

## 4. Pack: `open-source-ecosystem`

### 4.1 Production profile

**Purpose:** Assess open-source adoption evidence using revision, licence, code, package, maintenance and actually executed validation as distinct evidence classes.

**Use when:**

- comparing or adopting repositories/tools;
- README claims need source-code/configuration verification;
- package and deployment requirements differ;
- licence and dependency/service terms need separation;
- static findings must be translated into real required tests;
- maintenance evidence needs bounded interpretation.

**Do not use as:**

- security certification;
- legal/licence advice;
- authority for unrequested code changes;
- automatic dependency/cloud deployment;
- a popularity-based approval system.

### 4.2 Specialisation dimensions

| Dimension | Profile |
|---|---|
| Source ecology | Repository files, commits, releases and issues as relevant; maintainer statements, code and execution evidence stay distinct. |
| Search strategy | Resolve immutable refs/source paths first; bound history/issues and disclose sampling. |
| Inclusion/exclusion | Select projects against stated need and licence; popularity is only a discovery signal. |
| Source appraisal | Evaluate ownership, maintenance evidence, licence scope and test relevance separately. |
| Research methods | Compare README/package/deployment facts at the same revision; classify documented, inspected, executed and unknown. |
| Synthesis structure | Produce revision-bound suitability with environment, evidence kind, missing tests and adoption conditions. |
| Quality criteria | Check code-to-claim traceability, maintenance inference, dependency boundaries and truthful runtime status. |
| Reporting conventions | Cite file/ref/line or immutable item; do not promote stars or badges to assurance. |

### 4.3 Core operation effects

| Operation | Specialised behaviour | Observable consequence |
|---|---|---|
| `plan` | Set task-fit criteria, pinned revision and execution authority. | Static-only research cannot acquire install/run authority. |
| `discover` | Inspect native repository evidence and bounded history/issues. | Coverage/sampling limits stay explicit. |
| `extract-evidence` | Record path/ref/locator and evidence kind. | README, package declaration and executed result remain different. |
| `analyse-evidence` | Reconcile configuration and bind static risk to specific missing tests. | Suspicious code is a static finding, not a measured failure rate. |
| `synthesise` | Present evidence-qualified reuse conditions. | Dependency rights, environment and runtime gaps remain visible. |
| `refresh` | Compare changed revision/files and reopen affected claims only. | Documentation change does not invalidate unrelated source checks. |
| `audit` | Check revision identity, licence scope, maintenance inference and static-versus-executed wording. | Unexecuted installation cannot pass readiness. |

### 4.4 Preserved core invariants

The pack does not change:

- research purpose and consumer authority;
- source/processor permissions;
- evidence/claim distinctions;
- bounded work;
- uncertainty;
- revision history;
- mandatory review.

### 4.5 Selection rationale

This pack was selected because open-source adoption research has a specialist evidence ecology.

At the accepted pinned Open Deep Research revision, the source-backed comparison reconciled package Python requirements with deployment configuration and converted a static exception-path observation into a concrete missing test. The pack did not turn that observation into a fabricated production failure or hide that no installation was run.

### 4.6 Showcase

**Premise:** A team is considering an existing research engine instead of building one.

**Pinned subject:** `langchain-ai/open_deep_research` at commit `1b7d2e80db9faa586165c60e09096dbbfd483a64`.

**Expected specialist behaviour:** Reconcile cross-file environment statements, distinguish documented/static/executed evidence, and translate static risk into explicit validation obligations.

**Exact generation prompt:**

```text
Use the accepted deep-research procedure with the open-source-ecosystem profile specified in the Stage 11 profiles file. Assess langchain-ai/open_deep_research at commit 1b7d2e80db9faa586165c60e09096dbbfd483a64 as a candidate optional execution engine for an evidence-led research skill. Use only that revision's README.md, LICENSE, pyproject.toml, langgraph.json, src/open_deep_research/configuration.py, src/open_deep_research/deep_researcher.py and its Git commit metadata. Explain capabilities, setup, licence scope, important limitations and the next verification step. Distinguish documentary claims, static inspection and unexecuted tests. Do not install or run the engine, change code, spend money, contact maintainers, infer security from popularity or approve deployment. Use the supplied Stage 11 source register and only this source universe for any follow-up. Preserve qualifications and review the exact answer. Write a separate pack output without editing the core output.
```

As with the scholarly showcase, production packaging must remove hidden research-log dependencies.

### 4.7 Pack-specific evaluation

Required cases include:

- explicit activation and non-activation;
- immutable revision handling;
- licence scope versus dependencies/services;
- documented/inspected/executed separation;
- bounded maintenance sampling;
- static-risk-to-test mapping;
- explicit/locked precedence;
- targeted repair after repository change.

Differential success requires a real change in repository evidence handling or validation requirements, not a star count, badge or cosmetic table.

### 4.8 Maturity

```text
designed: PASS
procedure-demonstrated on bounded pinned repository task: PASS
production pack bundle: NOT YET IMPLEMENTED
clean installed activation: NOT YET MEASURED
fresh isolated differential reliability: NOT YET MEASURED
catalogue-ready production state: NOT YET CLAIMED
```

## 5. Deferred catalogue candidates

These are **not** current catalogue packs.

| Candidate | Why deferred | Reopening evidence required |
|---|---|---|
| `market-intelligence` | Core comparative research plus a consumer brief covers many initial needs; broad specialisation risks owning business strategy. | Repeated market-measurement/sample or syndicated-estimate method that materially changes research behaviour. |
| `technology-landscape` | Ordinary technology/tool comparisons overlap selected scholarly/repository methods; patent-family work needs sharper specialist evidence. | Bounded corpus/family or maturity method not adequately handled by core plus selected packs. |
| `trend-and-signal` | Core temporal/refresh semantics cover one-off updates. | Genuine longitudinal case showing specialist window, signal/noise and leading/lagging behaviour. |
| `creative-reference-research` | A style/genre label alone is not research specialisation. | Reusable provenance/context/rights method that changes research while creative production remains consumer-owned. |
| `investigative-osint` | Sensitive collection, privacy/harm, authenticity and editorial responsibilities exceed a safe generic initial pack. | Bounded legitimate method, non-sensitive showcase, privacy tests and actual specialist/editorial review route. |

No deferred entry should appear as installable or implemented until it passes [05](05-deep-research-skills-customisation-packs-spec.md).

## 6. Catalogue maintenance

A catalogue change records:

- pack ID/version;
- status;
- core compatibility;
- selection rationale;
- source-method revision;
- showcase revision;
- differential-evaluation evidence;
- installation state;
- known limitations.

A pack can be removed or downgraded when evidence no longer supports it. Historical research retains the exact profile identity used.

## 7. Catalogue acceptance

An entry is production catalogue-ready only when:

- the pack bundle is self-contained;
- explicit activation works;
- non-activation works;
- precedence works;
- exact showcase prompt is included;
- core-versus-pack behaviour is demonstrably different in the intended way;
- no core invariant regresses;
- pack-aware evaluation passes;
- selective/clean installation has been actually verified for the supported path;
- maturity status matches evidence.

The two initial entries currently stop before the clean-install/product-evaluation gates.
