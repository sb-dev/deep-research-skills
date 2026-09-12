# Stage 17 — Cross-Project Review

**Date:** 12 September 2026  
**Repository:** `sb-dev/deep-research-skills`  
**Branch:** `feat/bootstrap`  
**Accepted parent:** `8a7670fe1d9a18bbab6a61330ba15c6be3a2607e`  
**Status:** COMPLETE BEFORE PUBLICATION GATE

## Authority

Stage 17 is governed by the amended Deep Research bootstrap contract:

- `docs/research-logs/2026-09-11-deep-research-bootstrap-stage-amendment.md`, Stage 17;
- the original Stage 16 Cross-Project Review responsibility preserved by that amendment;
- the accepted Stage 16 public README contract and internal claims ledger;
- the accepted Stage 14 canonical Deep Research specifications.

Stages 1–15 remain immutable historical work. Stage 16 is the accepted predecessor and already repaired the public README surface.

The current Production Skills README contract was reviewed from `sb-dev/production-skills` branch `feat/public-readme-bootstrap-contract`, head `da7bea1d79013de584e7d53addb7f410b6521e3f`, PR #3. The PR is open, not merged, at review time. Stage 16 already adopted its public-surface rules locally, so this review uses the central branch as a compatibility reference rather than making Deep Research execution depend on that PR merging. Stage 22/23 must re-check the then-current family contract before final publication.

## Completion requirements

Stage 17 must:

1. compare the independently derived Deep Research architecture with the current Production Skills family contracts;
2. review relevant sibling Production Skills implementations without copying domain-specific semantics;
3. identify reusable family patterns and rejected imports;
4. verify the Stage 16 README contract still matches the current public pattern;
5. verify bootstrap/maturity evidence remains outside the public README;
6. verify the public claims ledger remains internal;
7. preserve the complete L1-01 quick-start prompt;
8. preserve the accepted 5 × 3 progression;
9. preserve substantive public sections for all three Deep Research skills;
10. record cross-domain handoff/abstraction candidates without prematurely centralising them;
11. give Stage 18 explicit preservation/scaffold guidance;
12. make no changes to completed Stage 1–16 evidence or canonical Deep Research semantics unless the review finds a genuine conflict.

## Sources inspected

| Source | Ref | Identity used | Review purpose |
|---|---|---|---|
| Production Skills public README process | `feat/public-readme-bootstrap-contract` | blob `dbc83ed446f5b177a5bcd6cf7623120f53932699` | public/private surface separation, migration and conformance |
| Production Skills public README template | same | blob `cf5d2a81fa3cd027950af6b0c665e9cb1c7394b7` | target public structure |
| Production Skills project contract | same | blob `2ea82df6e268cbb2a4191c979296012af14ce320` | family packaging, examples, skills and README contract |
| Production Skills cross-domain integration | same | blob `2be3cdecaf8e326d1c1076bb6044d60bbbe14616` | ownership, handoff, evaluation and no-shared-runtime rules |
| Video Production Skills README | `main` | blob `878ee7df6ad8f5f7ad1e8aa62f7014844ac78724` | cheap-first production, approval/cost control, targeted repair |
| Narrative Production Skills README | `main` | blob `b44e73b11449994d3b45149677325e81420838c3` | decision preservation, planned-vs-established distinction, bounded reopening |
| Music Production Skills README | `main` | blob `b4e94d6f6350a522f73f7867b2881620f75f7934` | fidelity escalation, local repair, external execution boundary |
| UI/UX Design Skills README | `main` | blob `41e77239ccfffe9f02ac60de573014c8e28b5b22` | evidence-grounded workflow, lowest-useful fidelity, 5 × 3 public examples |
| UI/UX Extension Pack spec | `main` | blob `a63cd081d00517b819bf8e77c335196be87613d6` | optional coherent packs, precedence and differential evaluation |
| Software Engineering Skills README | `main` | blob `e1c8629ff57115a504a3d786f47b7903195510e6` | availability check only; still bootstrap workspace |
| Game Development Skills README | `main` | blob `8d50f0c454cbb7dafd3d6a843d12bd9d92eca177` | availability check only; still bootstrap workspace |
| Deep Research System spec | `feat/bootstrap` | blob `8a2ada2a627e1755e9d522986363cbf6b1ea5336` | compare family patterns against domain semantics |
| Deep Research Extension Pack spec | `feat/bootstrap` | blob `22decdddaddc0358137b74806c27bc2ba769179e` | compare pack model against proven family behaviour |
| Stage 16 public README contract | `feat/bootstrap` | blob `be63a999e7ec9fae7c0585985c567d934f9dfd3e` | public-surface conformance |
| Stage 16 public claims ledger | `feat/bootstrap` | blob `cfe76b78f4d1c92413044df65e573d2dcc94e0d0` | evidence-gate separation |
| Current root README | `feat/bootstrap` | blob `122dae53c254c563d7042e2d20539af3774f62c0` | final public-surface readback |

Software Engineering and Game Development are not used as production-pattern evidence because their public `main` surfaces are still bootstrap workspaces. Their presence is recorded so “when available” was checked rather than assumed.

## Cross-project findings

### 1. Cheap-first work is a family pattern; Deep Research already expresses it natively

Video, Music and UI/UX all resolve uncertainty at the cheapest useful representation before increasing fidelity. Deep Research has the same production invariant in research-native form:

```text
question framing
→ metadata / exact-source triage
→ source map
→ focused retrieval
→ evidence extraction
→ targeted follow-up
→ synthesis
```

**Decision: RETAIN.** Keep `Use the cheapest adequate authorised operation`. Do not import creative-media notions of visual/audio fidelity into research.

### 2. Preservation and smallest-sufficient repair are shared; approval semantics remain domain-specific

Video, Narrative, Music and UI/UX preserve accepted decisions and repair the smallest owning layer. Deep Research already preserves verified evidence and refreshes only affected evidence, claims and dependent synthesis.

Narrative's planned-versus-established distinction is conceptually useful because it reinforces Deep Research's stronger existing distinction:

```text
source ≠ evidence ≠ claim ≠ synthesis ≠ recommendation
```

**Decision: RETAIN THE INVARIANT, REJECT THE CREATIVE VOCABULARY.** Deep Research does not adopt narrative canon, shot approval, music locking or UI selection state as research semantics. Research review/authority remains defined by its own evidence and fixed-input evaluation model.

### 3. Independent evaluation is a strong Deep Research specialisation

Sibling projects commonly separate production from evaluation and route failures to the owning layer. Deep Research goes further by making `research-evaluate` independently installable and fixed-input.

**Decision: RETAIN.** The evaluator must continue to write a new review rather than silently editing producer evidence. This is compatible with the family pattern and is not over-specialisation.

### 4. Self-contained skills and bounded commands align with the family contract

The Production Skills project contract requires self-contained skills; commands exist for composition, isolated evaluation, diagnosis and targeted repair rather than as a universal lifecycle engine.

Deep Research's three independently installable skills and eleven semantic operations already satisfy that design direction.

**Decision: RETAIN.** Stage 18 must package each skill without hidden repository-root or sibling dependencies.

### 5. Extension Packs are optional coherent production profiles, not tags

UI/UX provides strong current evidence for the family pattern: packs specialise core behaviour, remain optional, rank below explicit instructions/approved work and require observable differential behaviour. Deep Research's pack model already requires material changes to source ecology/method/evaluation, explicit activation, precedence and core-vs-pack comparison.

**Decision: RETAIN.** `scholarly-evidence` and `open-source-ecosystem` remain the accepted initial research profiles. Do not import platform/provider names as packs and do not add a universal pack runtime.

### 6. The current family progression is 5 × 3, not the legacy Video count

Video's older README exposes four examples per level. Narrative, Music and UI/UX use three examples per level, and the current Production Skills contract explicitly requires five levels × three complementary primary examples.

**Decision: REJECT THE LEGACY VIDEO COUNT.** Preserve the accepted Deep Research fifteen-example identity exactly.

### 7. Public examples belong under stable product paths

Narrative, Music and UI/UX route learning examples through `examples/...` surfaces. The current family README process forbids using bootstrap research logs as primary product navigation.

Deep Research Stage 16 intentionally lists the 15 example names without links until the production scaffold exists.

**Decision: RETAIN THE STAGE 16 EXCEPTION; APPLY THE FAMILY PATTERN IN STAGE 18.** Stage 18 creates one public `examples/.../README.md` per primary example, then mechanically links the root README to those paths.

### 8. External tools remain below domain semantics

Video and Music use external generation skills/tools; UI/UX uses browser, accessibility, design and mobile automation tools. In each case the Production Skill decides what work is needed while existing tools execute specialist operations.

Deep Research already applies the same separation to search, browsing, GitHub retrieval, scholarly APIs, documents, multimodal inspection, code/statistics and optional broad-research engines.

**Decision: RETAIN.** Do not create a mandatory provider router, browser framework, search engine, vector database or orchestration layer.

### 9. Cross-domain composition belongs to the consuming project

The family cross-domain contract assigns reusable domain expertise to each Production Skills repository while the consuming project owns actual composition. Deep Research's boundary already sends evidence, uncertainty and unresolved owner decisions downstream without taking over engineering, UX, creative, business or professional judgement.

**Decision: RETAIN.** A research handoff can define minimum evidence metadata but must not become a universal cross-domain artefact graph.

### 10. Evaluation layers remain separate

The family contract separates specialist-domain evaluation, orchestration/integration evaluation and consuming-project QA. Deep Research separately evaluates retrieval, evidence, citation support, synthesis, refresh, packs and installation.

**Decision: RETAIN.** No universal research-quality score or family-wide quality judge is introduced.

### 11. Legacy README conventions are not authoritative over the current family contract

Three legacy sibling conventions must not be imported:

- Video's four-example-per-level public progression;
- Narrative/Music `<org>/<repo>` or publication-placeholder wording;
- research-log links used by older projects as public onboarding/navigation.

**Decision: REJECT.** The current family contract and accepted Stage 16 Deep Research contract control.

### 12. Software Engineering and Game Development are not yet production evidence

Both `main` READMEs remain minimal bootstrap workspaces. Their current bootstrap/process branches are not treated as evidence of implemented family behaviour.

**Decision: NOT APPLICABLE AS PRODUCTION PATTERN EVIDENCE.** Revisit only when those projects have actual production artefacts or benchmark evidence relevant to a shared abstraction.

## README conformance review

The current root README was checked against the Stage 16 contract and current family template.

| Requirement | Result | Review |
|---|---|---|
| Product-facing positioning and capabilities | PASS | Opens with research-production promise, not bootstrap state. |
| Domain control model | PASS | `Research effort and evidence control` exposes question/evidence/resource/preservation invariants. |
| Installation surface | PASS | Canonical project-local forms are present; evidence is tracked privately in the claims ledger. |
| Complete L1-01 prompt inline | PASS | Full W3C prompt remains in the root README. |
| Five levels × three examples | PASS | L1-01 through L5-03 preserved exactly. |
| Public example navigation | PASS WITH STAGE-16 EXCEPTION | No research-log onboarding links remain; Stage 18 must create/link `examples/...` surfaces. |
| Substantive skill sections | PASS | All three skills explain responsibility, use and boundaries. |
| Extension Packs | PASS | Two accepted profiles and material-difference rule preserved. |
| Execution boundary | PASS | Research semantics remain provider-independent. |
| Evaluation/benchmark surface | PASS | Layered evaluation retained without one universal score. |
| Canonical documentation | PASS | Six canonical specifications linked. |
| Boundary / contributing / licence | PASS | Product-facing sections present; Stage 18 may add real file links mechanically. |
| Bootstrap/maturity leakage | PASS | No Stage/branch/SHA/progress/not-run scheduling is exposed in public copy. |
| Claims ledger remains internal | PASS | Ledger is under research logs and is not linked from public onboarding. |

No substantive README change is justified by Stage 17.

## Cross-domain handoff candidates

Stage 17 records the following as **domain-owned candidates**, not shared family abstractions:

### Research evidence package

Candidate minimum handoff:

```text
research question / downstream use
source identities and inspected representations
material evidence + locators
claims and inference level
contrary evidence
uncertainty / limitations
temporal scope / valid-as-of
method or pack identity when material
access / disclosure restrictions
unresolved owner decisions
```

The receiving domain owns interpretation inside its own production discipline.

### Research brief handoff

A consuming domain may provide a research need with:

```text
decision to inform
scope / exclusions
freshness
source restrictions
quality threshold
resource / authority constraints
expected return
```

### Valid-as-of metadata

Temporal validity is a strong candidate for reuse across evidence-producing domains, but Stage 17 does not centralise it. Stage 25 may reconsider only with independent implementation evidence from another domain.

### Cross-domain evidence provenance

Source/evidence identity and transformation metadata may become a family abstraction if at least one independent domain demonstrates substantially the same implementation need. Until then they remain Deep Research semantics plus explicit handoff documentation.

## Stage 18 preservation contract

Stage 18 should consume this review as follows:

1. preserve the Stage 16 README positioning, complete L1-01 prompt, 5 × 3 progression and three skill sections;
2. create stable public surfaces for all fifteen examples and only then add the links to the README;
3. create `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md` and production directories only when they contain justified material;
4. package each skill self-contained, with skill-local commands/references and no hidden sibling/root dependency;
5. preserve fixed-input evaluator independence;
6. implement deterministic README checks from the Stage 16 contract;
7. keep external search/browser/provider execution optional and below research semantics;
8. do not introduce a shared runtime, universal provider router, evidence database, knowledge graph or pack interpreter;
9. link `LICENSE` and `CONTRIBUTING.md` mechanically once those files genuinely exist;
10. treat the Production Skills PR #3 status as non-blocking for Stage 18, but re-check the current family contract during Stage 22/23 before publication.

## Accepted decisions

| ID | Decision | Status |
|---|---|---|
| D17-01 | Stage 16 public README contract remains valid without substantive change. | ACCEPTED |
| D17-02 | Deep Research canonical system/workflow/pack semantics remain unchanged. | ACCEPTED |
| D17-03 | Preserve cheap-first work, artifact/evidence preservation and smallest-responsible repair as family-compatible invariants. | ACCEPTED |
| D17-04 | Preserve fixed-input independent evaluation as a Deep Research specialisation. | ACCEPTED |
| D17-05 | Preserve three self-contained installable skills and bounded semantic commands. | ACCEPTED |
| D17-06 | Preserve optional coherent Extension Packs with explicit activation, precedence and differential evaluation. | ACCEPTED |
| D17-07 | Preserve the accepted 5 × 3 example set; do not import Video's legacy four-example levels. | ACCEPTED |
| D17-08 | Stage 18 must create stable public example paths and mechanically link them. | ACCEPTED |
| D17-09 | Do not import creative approval/canon/locking semantics as research state. | ACCEPTED |
| D17-10 | Do not import one provider/runtime or create a universal research execution layer. | ACCEPTED |
| D17-11 | Keep cross-domain composition and final decisions with the consuming project/receiving domain. | ACCEPTED |
| D17-12 | Keep handoff/valid-as-of/provenance ideas domain-owned candidates until Stage 25 evidence supports sharing. | ACCEPTED |

## Conformance table

| Requirement | Evidence | Status |
|---|---|---|
| Re-read amended Stage 17 contract | Governing amendment inspected at accepted Stage 16 branch | PASS |
| Preserve completed Stages 1–16 | Review changes no completed stage artefact or canonical spec | PASS |
| Review Production Skills family contracts | README process/template, project contract and cross-domain spec inspected | PASS |
| Review mature sibling patterns | Video, Narrative, Music and UI/UX inspected | PASS |
| Check Software/Game availability | Both public main surfaces inspected; bootstrap-only, not used as implementation evidence | PASS |
| Reuse family patterns without domain distortion | Accepted/rejected decisions D17-01..D17-12 | PASS |
| Verify README public-surface contract | README conformance table above | PASS |
| Keep claims ledger internal | Stage 16 ledger inspected; no public navigation to it | PASS |
| Preserve complete quick start | L1-01 prompt read back in root README | PASS |
| Preserve 5 × 3 progression | Fifteen accepted identities read back | PASS |
| Preserve substantive skill sections | Three skill sections read back | PASS |
| Record abstraction candidates without promotion | Candidate section above; no central abstraction created | PASS |
| Give Stage 18 explicit guidance | Stage 18 preservation contract above | PASS |

## Exit assessment

Stage 17 passes its content acceptance criteria.

The review finds no cross-project conflict requiring changes to the Deep Research system specifications, Stage 16 README contract, public claims ledger or root README. The useful family patterns are already represented in Deep Research-native terms, while legacy or domain-specific sibling conventions are explicitly rejected.

Stage 18 is the next authorised stage. This log does not start repository scaffolding.

Remote commit/tree/ref verification occurs after the single Stage 17 commit is created and is reported externally rather than recursively embedded into the commit itself.
