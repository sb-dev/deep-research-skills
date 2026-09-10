# Stage 13: Evals, Benchmarks and Regression Fixtures

Date: 10 September 2026. Repository: `sb-dev/deep-research-skills`. Branch: `feat/bootstrap`.

## Authority, inputs and acceptance checklist

The acceptance contract is section 19 of the [original bootstrap](2026-09-07-deep-research-skills-new-project-bootstrap-process.md), read from main, blob `8ff62c92bada2861ece3684a9e73a83da75d9d94`. Sections 5 and 29 preserve evidence-first research, independent failure dimensions, bounded work, pack behaviour, repair and truthful maturity. Sections 23–26 assign production scaffolding and actual local/external product installation to Stages 17–20. This stage supplies the evaluation design and executable reference fixtures, not a premature installed-product claim.

Accepted parent: `24bc5755cd769587e367792ba17f892116542551`, the remotely verified Stage 12 progress correction. Stage 12's actual published document, blob `c4584c688940f05898d9522a1480e60417905fde`, was read in full; the stale local work packages were not used. Its fifteen selected prompts remain unchanged. Other accepted inputs are the Stage 1 domain boundary; Stage 2 [quality dimensions](2026-09-10-stage-02-quality-dimensions.md) and [failure taxonomy](2026-09-10-stage-02-failure-taxonomy.md); Stage 3 [evidence/claim model](2026-09-10-stage-03-question-evidence-claim-model.md); Stage 4 source access; Stage 5 workflow/artefact ownership; Stage 6 stopping/refresh policy; Stage 7 benchmark/tool candidates; Stage 8 execution boundaries; Stage 9 infrastructure guardrails; Stage 10 [command contracts](2026-09-10-stage-10-command-contracts.md); and Stage 11 [profiles](2026-09-10-stage-11-profiles.json) and [performed comparisons](2026-09-10-stage-11-comparisons.md). Their responsibilities are preserved rather than replaced by a general scoring system.

| ID | Requirement and specification reference | Required evidence |
|---|---|---|
| R01 | Section 19 Purpose and all ten evaluation layers | Architecture with input, oracle, method, verdict and distinct execution boundary per layer. |
| R02 | Section 19 external references | Inspect all five named benchmark families, identify usable lessons and rejected transfers. |
| R03 | Section 19 failure-fixture list | All twelve specified failures represented as identifiable reproducible cases, not just labels. |
| R04 | Section 19 temporal and preservation clauses | Cases for supersession, event/effective dates, partial cache validity and dependent repair. |
| R05 | Section 19 Outputs: taxonomy and dimensions | Preserve and operationalise Stage 2 F01–F20 and K01–K16; no universal quality score. |
| R06 | Section 19 case-format output | Complete case/submission/review contracts and runnable positive/negative examples. |
| R07 | Section 19 end-to-end and progressive coverage | Map all fifteen EX identifiers and create independent-topic hold-out case contracts. |
| R08 | Section 19 pack evaluation and differential suite | Both selected profiles, actual behavioural criteria, activation/precedence controls and honest paired-run evidence. |
| R09 | Section 19 regression and release outputs | Root-cause-to-fixture policy, versioned baselines and non-compensable release gates. |
| R10 | Section 19 Exit; execution instructions verification | Execute feasible reference checks, demonstrate four independently failing layers, inspect substance and publish stage-only changes. |

The original specifies ten layers, twelve priority fixture classes, three temporal situations and eight output responsibilities. It does not prescribe a benchmark score, replicate count, cash allowance or external dataset size. This design adds six supporting synthetic cases, two original research hold-out contracts and two pack pair contracts for justified coverage. These counts are current design choices, not universal future quotas. No current requirement is replaced by an illustrative future target: the fixtures, case contracts, map and executed reference checks exist in this stage; installed agent measurements remain explicitly unmeasured.

## 1. Benchmark architecture

### Decision and alternatives

Adopt a small, file-based evaluation boundary around the existing skill commands. A case defines a question, authorised evidence universe, execution envelope and acceptance criteria before a candidate runs. An executor produces a frozen submission and observable operation record. Structural checks and a separate semantic review create new verdict files. Diagnosis identifies the smallest repair; a producer changes only the authorised submission and dependent records. Evaluation never quietly fixes the input it grades.

Reject a single report score: a persuasive report can cite the wrong source. Reject an end-to-end-only suite: a broken locator should not need a full investigation to reproduce. Reject a purely synthetic suite: typed fixtures do not demonstrate real retrieval or research judgement. Reject a mandatory multi-agent judge platform or universal evidence database: neither is needed to run bounded commands and preserve case files. The optional existing evaluation harness selected in Stage 7 can execute these contracts later; it does not own research acceptance.

### Four complementary suites

| Suite | Responsibility | Evidence mode and limitation |
|---|---|---|
| Contract and regression | Fast exact checks of identifiers, dates, permissions, counting, typed support, stopping and preservation. | Explicit synthetic fixtures and known mutations. Proves bounded checker behaviour, not arbitrary prose entailment or agent quality. |
| Frozen research replay | Repeat research against an identified permitted corpus, keeping task, sources and expected support stable. | Actual source snapshots/locators and gold evidence. A changed corpus requires a new case version; live network access is disabled or scoped. |
| Live-source research | Test current discovery, actual source access and truthful temporal updates. | Re-establish the answer from current originals. Separate environmental/source change from a model regression; log access gaps and do not reuse obsolete gold facts. |
| Installed product | Exercise selected installed skills, commands, packs and a real research handoff from a clean consumer. | Actual installation and operation transcripts. A copied directory or a policy fixture cannot substitute for the required external installation. |

Do not pool these suites into one reliability number. Each run names its mode, scope, source/host/model/configuration, permission boundary and limitations. Replays and live runs have different reproducibility claims. A source can be traceable without redistributable raw bytes; retain lawful references and disclose restricted access instead of leaking private material.

The [external investigation](2026-09-10-stage-13-benchmark-research.md) examines BrowseComp, DeepResearch Bench, BrowseComp-Plus, ResearchRubrics and FINDER/DEFT. It supports hard-discovery checks, controlled corpora, atomic report criteria and separate citation/report verdicts. Our authority, repair, pack and installation requirements still come from the accepted project contracts, not those benchmarks.

### Test taxonomy: all ten layers

| Layer | Required concerns and actual inspection method | Oracle, result and smallest repair |
|---|---|---|
| L01 Structural integrity | Required research metadata; source identities/timestamps; citation target resolution; claim/source references; missing records; invalid structure; duplicate IDs; selective-install integrity; self-containment. Validate the selected representation, resolve IDs and local paths, distinguish syntactic dates from semantically correct dates. Check actual installation separately. | Schema/record contract and exact submitted bytes. Missing mandatory record FAILS structural integrity; inaccessible external target is an access limit, not proof of falsity. Repair the missing field/link/package dependency. |
| L02 Retrieval behaviour | Known-answer source recall, reformulation, persistence, diversity, primary recovery, specialist selection and duplicate avoidance. Inspect queries, returned/inspected originals, result caps and continuation. A remembered correct answer without evidence does not prove retrieval. | Gold evidence within the declared corpus and method/source obligations. Measure distinct required sources found, not URL count. Repair the responsible query, route or access operation; respect the finite envelope. |
| L03 Source/evidence quality | Directness, relevant authority/method, independence, freshness, temporal fit, inclusion/exclusion and contrary material. Review source-to-extraction context and evidence units, not publisher prestige. | Source representations and claim-relative appraisal. Typed fixtures check their exact facts; natural-source fidelity and method fit need semantic review. Repair extraction, relation or eligibility without rewriting originals. |
| L04 Citation/claim support | Existence, entailment, material-claim completeness, placement, source/claim mismatch and unsupported inference. Split compound claims and inspect qualifiers, negation, units, population and premises. | Exact report proposition and inspected support. Bibliographic correctness may PASS while entailment FAILS. Missing access can BLOCK a required check. Fix the owning locator, extraction, claim or inference, then the rendered sentence. |
| L05 Synthesis quality | Question coverage, logic, cross-source integration, contradiction handling, uncertainty calibration, alternatives, scope, decision relevance and clarity without lost evidence. Read the exact report against A01/A02 and its claims; do not infer quality from length. | Task-specific supported findings and explicit limits. K10 evaluates justified uncertainty, not a claimed calibrated probability without outcome data. Repair grouping, argument or wording; new factual bridges require evidence. |
| L06 Preservation/diagnosis/repair | Identify the weak claim/missing evidence; preserve verified unaffected records; retrieve only the needed delta; update dependent synthesis; avoid unnecessary whole-report regeneration. Compare before/after identities, dependency scope and actual operations. | Diagnosed defect and explicit expected changed/preserved sets. Byte equality proves preservation, not semantic correctness; related changed wording still needs review. Broaden the repair when dependencies are uncertain instead of falsely claiming isolation. |
| L07 Temporal/refresh | Old/new official conflicts; publication versus event/effective dates; cached support valid for some claims but not others. Evaluate applicability at the stated time, not retrieval date alone. | Frozen time/version table and actual update evidence. Preserve historical truth while updating current claims. Repair only affected temporal basis, claims and review dependencies. |
| L08 Extension Packs | Requested activation, non-activation, precedence, changed source strategy, changed criteria, core-versus-pack behaviour and pack-aware quality. Inspect the selected version and actual plan/evidence/audit differences. | Core invariants plus selected profile-specific criteria. A pack name in output is insufficient. Incompatible selection or missing mandatory access BLOCKS; an overriding or cosmetic-only pack FAILS. Repair the owning pack rule or its packaging, not the core default. |
| L09 End-to-end research | All fifteen progressive examples plus independent-topic hold-outs. Inspect produced brief, actual evidence, supported report, exact review and consumer handoff at the intended responsibility scale. | Full task contract. A limitations conclusion is valid only if the brief permits it and all required behaviours actually occurred. One quick start is not proof of every example. Repair through the responsible command rather than automatically restart. |
| L10 External installation | Clean consumer projects, selected skill discovery, local commands/references, real quick-start outputs/evaluation, selective installation and at least one implemented pack. Run the actual documented remote install with no source checkout paths. | Observed install and task records at the exact repository revision, agent and package version. Local structural PASS cannot pass this layer. Missing dependency or wrong installation route is fixed in packaging/documentation and rerun. |

L01–L08 have executable design/reference controls now where their properties are representable. L09's case definitions are complete; real candidate execution remains a later product gate. L10's protocol is fully specified here, but its actual execution requires the Stage 17–18 packages and is assigned to Stage 20. This is not a waiver of clean installation or a claim that it passed.

## 2. Domain quality dimensions and diagnostic mapping

Retain all sixteen accepted dimensions without renaming their identifiers. Their evidence and counterexamples in Stage 2 remain applicable. Assess only justified concerns, but never omit a mandatory one silently.

| Dimension | Primary layers and observable acceptance |
|---|---|
| K01 Question and use fit | L05/L09: all required questions addressed at the authorised level; a neighbouring answer fails. |
| K02 Coverage honesty | L02/L03: performed selection supports the stated scope; no selective scan called exhaustive. |
| K03 Source access and provenance | L01/L03/L04: exact representation, access extent, locator and material transformation remain inspectable. |
| K04 Evidence-unit integrity | L03: distinguish duplicate files, reports, versions, studies and observations before counting. |
| K05 Applicability and methodological fitness | L03/L05: the method supports this kind of inference; specialist requirements remain real. |
| K06 Independent support | L03: shared origins do not create additional corroboration. |
| K07 Extraction fidelity | L03/L04: units, negation, denominator, context and uncertainty survive extraction. |
| K08 Counterevidence treatment | L03/L05: eligible null/adverse/conflicting evidence stays represented. |
| K09 Inferential validity | L04/L05: explicit premises and reasoning support the actual conclusion. |
| K10 Uncertainty communication | L05: limitations and unresolved claims survive prose; no unjustified confidence percentage. |
| K11 Temporal applicability | L07: event/publication/effective/retrieval/valid-as-of contexts are not substituted. |
| K12 Review adequacy | L04/L05/L09: exact revisions, actual scope and competent process; a producer self-check is not independent approval. |
| K13 Reconstructability and reporting | L01/L04/L09: another authorised reader can inspect the chain and its limits without this chat. |
| K14 Proportionality | L02/L06: useful bounded next actions, parent reservations and finalisation; capacity exhaustion is not sufficiency. |
| K15 Responsible authority | All layers: allowed sources/processors/audiences and genuine review/commitment owners. |
| K16 Repairability and continuity | L06/L07: correct dependent records and preserve unaffected valid work. |

The failure taxonomy stays F01–F20. Map F01/F19 to L05/L09; F02/F03/F15 to L02/L03; F04/F07/F13 to L03/L04; F05/F06 to L03; F08/F10/F11 to L03/L05; F09/F12 to L03/L05; F14 to L07; F16/F20 to L05/L09; F17 to authority in every layer; F18 to L06/L07. Several may co-occur. A visible prose symptom cannot identify the upstream cause without the relevant source/operation record. Model-generated failure labels are hypotheses until checked.

### Metrics and verdicts

A criterion records PASS, FAIL, BLOCKED or NOT APPLICABLE with an explicit reason and scope. A focused audit leaves other scopes unassessed; required unassessed criteria make overall acceptance BLOCKED, never implicitly PASS. An applicable partially supported mandatory proposition is narrowed/repaired or fails; explanatory partial-support labels do not weaken this rule. A NOT APPLICABLE reason must be valid under the case and method, not merely nonempty text.

Optional diagnostic measures remain separate: recall of gold evidence within a known corpus; material-claim citation coverage; supported citation proportion; errors by quality dimension; necessary versus unnecessary acquisition; preserved-record identity; resource consumption including outstanding exposure; and task-specific rubric satisfaction. Every denominator, exclusion, access failure and uncertainty is recorded. No aggregate average compensates for a material permission, support, coverage or review failure. Unknown recall on the open web remains unknown.

For calibrated probability claims, specify the forecast event, population, resolution rule, outcome sample and calibration analysis before evaluation. The current project promises explained uncertainty, not a universal calibration guarantee. A model's confidence phrase or another model's agreement cannot supply empirical calibration. K10 can pass faithful uncertainty communication while numerical calibration remains unmeasured.

## 3. Case, submission and review formats

A benchmark is a set of bounded task contracts, not a required research runtime. JSON is used for machine-checkable fixtures; Markdown remains a valid research submission when an adapter preserves semantics. The [case-contract file](2026-09-10-stage-13-case-contracts.json) contains two complete original hold-out tasks and two pack pair contracts. The [reference checker](2026-09-10-stage-13-fixture-check.py) embeds eighteen complete synthetic positive/negative cases. Their inputs and expected outcomes are explicit and reproducible.

| Case responsibility | Required information |
|---|---|
| Identity and split | Case ID/version; development, regression, teaching or hold-out role; synthetic versus real-source character; owning requirement/layer; licensing and exposure limits. |
| Task | Exact prompt, required output and intended use; mandatory subquestions; selected skills/commands/packs; prior approved decisions; allowed sources/processors; prohibited side effects. |
| Evidence universe | Original source identity/edition, actual access/locator, material snapshots and lawful retention; gold evidence only where actually established; mutable-source mode; known unavailable material. |
| Oracle | Atomic criterion ID, mandatory/optional status, expected proposition or behaviour, supporting source/logic, tolerance where justified, negative conditions and required reviewer competence. No target-model self-verdict as truth. |
| Execution envelope | Finite search/read/data/compute limits, parent aggregate, outstanding jobs and finalisation reserve, allowed retries and stopping conditions. A benchmark label does not grant expenditure. |
| Repair contract | Injected or observed defect, owning command, expected affected dependencies, unchanged records, permitted new acquisition and recheck scope. Label injected mutations explicitly. |
| Provenance | Authoring and source inspection dates, case/oracle version, changes and rationale. Do not fabricate capture hashes, dates, independent reviewers or expected values. |

The candidate receives the prompt, permitted inputs and ordinary task constraints. Evaluation-only expected answers, negative specimens and other-condition outputs stay outside its context. Freeze the case before a candidate run. A submitted answer cannot modify the oracle. If the source or oracle is wrong, an authorised reviewer corrects it in a new version and reruns affected baselines; do not retroactively alter a failing record.

A **submission record** identifies case/revision, candidate skill commit, host/model/tool versions actually known, corpus/capture identities, actual queries and relevant returned/inspected sources, operation outcomes/limits, output paths and content identities, resource consumption/reservations and actual start/end or available date precision. Never fabricate hidden tool traces. A timeout retains unknown status until reconciled. Separate environmental failure, invalid case, invalid submission and substantive research failure.

A **review record** identifies fixed submission hashes, criterion results, evidence locators, reviewer method/role, applicable competence and independence limits, errors, skipped scopes, diagnosis and smallest repair. Review outputs are new files. Re-audit repaired revisions; earlier verdicts remain historical. A release summary lists mandatory failures and limitations before optional metrics.

### Original hold-outs

HO01 checks a bounded HTTP semantics question; HO02 checks missing-value processing under an explicitly named data-specification version using synthetic cells. Their original-source locators, exact prompts, oracle criteria, task bounds, output paths, adversarial variants and repair requirements are in the case file. Both topics are separate from all fifteen teaching examples. Neither was used to tune the reference scorer or run through a candidate agent in this stage.

These public authored contracts are held out from teaching/development examples, not secret from the present author or demonstrably absent from a model's pretraining. Future evaluators must keep their oracles out of candidate context, freeze candidate instructions before evaluation and record exposure. Once a failure drives tuning, move that case into regression and replenish the evaluation hold-out. Generalisation claims require independent tasks and reviewers beyond these two cases.

## 4. Priority regression and temporal fixtures

Each FX fixture has fixed synthetic input, independent rule, positive submission, negative submission and repair owner in the checker. The scorer derives a verdict from the submitted fields and fixed facts, not from a stored expected verdict. The negative specimen is used to test that scorer, not passed to a browsing agent as real evidence.

| Case | Governing failure | Observable defect and smallest owner |
|---|---|---|
| FX01 | Three articles repeat one original | Inflated origin count; analyse-evidence corrects independence and dependent confidence. |
| FX02 | Snippet contradicts full source | Lost negation despite full access; extract-evidence restores actual passage meaning. |
| FX03 | Old versus current official page | Wrong applicable version; refresh corrects current basis without rewriting historical truth. |
| FX04 | High-ranking SEO versus primary | Required original absent from inspected set; follow-up-search recovers direct support. |
| FX05 | Retracted/corrected scholarly source | Withdrawn result treated as active; analyse-evidence revisits status and affected reliance. |
| FX06 | Reports treated as several studies | False study inflation or loss of useful reports; analyse-evidence repairs work/report relation. |
| FX07 | Paywall plus accessible secondary | Unread original declared inspected; extract-evidence narrows access and attribution. |
| FX08 | Conflicting high-quality sources | Eligible contrary source omitted; analyse-evidence restores conflict and consequence. |
| FX09 | Unsupported confident synthesis | Association becomes causal guarantee; synthesise restores supported scope and uncertainty. |
| FX10 | Adjacent-fact citation | Correct source ID, wrong supported field; synthesise fixes citation/proposition or returns to extraction. |
| FX11 | Missing required subquestion | Report omits Q2; analyse-evidence identifies and resolves or honestly records the gap. |
| FX12 | Research continues after sufficiency | Extra optional duplicate collection after support/review gates pass; follow-up-search stops. |

TM02 separately tests publication before effective date; TM03 preserves a cached historical claim while updating another claim. BG01 tests multi-dimensional aggregate reservations; BG02 requires useful follow-up despite low yield when a known material gap remains. PR01 tests propagation from corrected denominator to result/claim, preserving unrelated work. AU01 prevents producer self-check from satisfying required independent assurance. These complement, rather than replace, the original twelve.

Four **orthogonality controls** mutate one otherwise identical submission: a retrieval reformulation, origin count, citation field or question coverage. Each must produce a failure only in its designated retrieval, evidence, citations or synthesis layer. Four scorer mutations suppress one of those layers; known bad cases must reveal the defective scorer. This demonstrates separable bounded detectors, not four perfectly independent real-world causes.

Exact typed `entails-field` checking applies only to its declared synthetic field semantics. It is not a generic natural-language entailment model. Future semantic tests must include faithfully paraphrased support, negation, misleading adjacent passages, compound claims, quantitative qualifiers and genuinely unresolved cases. A reviewer checks both false acceptance and false rejection; string identity alone is not the research-quality oracle.

## 5. Progressive-example coverage map

The exact prompts remain in the accepted [Stage 12 design](2026-09-10-stage-12-progressive-examples.md); do not maintain divergent shortened prompts here. EX identifiers are stable references to those complete contracts. The following map covers every selected example, not representative levels only.

| Example | Primary layers / quality emphasis | Required diagnostic link and installed selection |
|---|---|---|
| EX-L1-01 | L02/L04/L05; K01/K03/K11 | Exact official status versus conformance overclaim; FX04/FX10. Producer only, no pack; canonical keyless quick start. |
| EX-L1-02 | L01/L04; K05/K12 | Package/deployment conflation and unchanged audit submission; FX10/AU01. Evaluator only. |
| EX-L1-03 | L03/L07; K04/K11 | Count unit and observation versus retrieval date; FX03/TM02. Producer only. |
| EX-L2-01 | L02/L03/L04; K02/K05 | Official API evidence versus wrapper/metadata substitution; FX04/FX07. Producer and evaluator, core only. |
| EX-L2-02 | L03/L05; K04/K05/K06 | Work/report/version linkage and changed population; FX06/FX09. Producer and evaluator. |
| EX-L2-03 | L03/L06; K07/K09/K13 | Complete denominator including Unknown and reproducible calculation; PR01. Producer/evaluator with actual local data execution. |
| EX-L3-01 | L02–L05/L08; K05/K08/K10 | Scholarly unit/status and limited transfer; FX05/FX06/FX09, PD01. Explicit scholarly-evidence. |
| EX-L3-02 | L03/L05/L09; K01/K05/K15 | Activity does not prove demand or willingness to pay; FX09/FX11. Core only. |
| EX-L3-03 | L03/L04/L08; K03/K12/K15 | Static observations versus actual installation readiness; AU01/FX10, PD02. Explicit open-source-ecosystem. |
| EX-L4-01 | L06/L07; K11/K16 | Retrospective versus current policy, announcement and implementation; FX03/TM02/TM03. Producer/evaluator refresh and diagnosis. |
| EX-L4-02 | L03/L06/L07; K04/K07/K16 | Snapshot double counting, schema/denominator repair, preserved calculations; FX06/PR01/TM03. Core, bounded data acquisition. |
| EX-L4-03 | L02/L03/L06/L08; K02/K06/K16 | Shared engines, sampled histories, bounded follow-up and locator repair; FX01/FX10/BG02, PD02. OSS pack. |
| EX-L5-01 | L05/L08/L09; K01/K15/K16 | Catalogue-first create-pack qualification and research-before-architecture; FX11/AU01, pack precedence suite. All three skills; creator-only qualification also tested selectively. |
| EX-L5-02 | L03/L05/L06/L09; K05/K09/K15 | Scientific units and empirical/model/simulation distinction; FX09/PR01/TM03. Core, three domain handoffs. |
| EX-L5-03 | L03/L05/L07/L09; K01/K10/K15 | Conditional opportunity, permitted use and scoped refresh; FX09/FX11/TM03. Core, business/software/editorial handoffs. |

Every example also requires source/claim closure, uncertainty, permission and finite effort. L10 checks their installation routes rather than pretending every large programme must run on each formatting-only change. Selective checks must include producer-only, evaluator-only, creator qualification, producer/evaluator, all-three and a selected pack. Release coverage records exactly which example/agent combinations actually ran; omitted combinations stay unmeasured.

## 6. Pack differential suite

PD01 and PD02 in the case file define paired trials for scholarly-evidence and open-source-ecosystem. Freeze task, core version, source universe, tool access, baseline known facts, review requirements and resource bounds. Both conditions answer the same question. Change only pack selection and intended specialist rules. Use separate candidate contexts and keep the other answer and evaluation oracle hidden. Record actual tool/corpus/model state, all trials and any nondeterminism. Prespecify repetitions and budget before claiming an effect estimate; this design invents neither an unexecuted sample nor a universal significance threshold.

The three mandatory differential criteria per pair inspect **plan/source strategy, evidence handling and audit criteria**, not the appearance of metadata. PD01 demands explicit scholarly work/report units and appropriate applicability/status handling. PD02 demands cross-file revision/environment reconciliation and separation of static observations from executed assurance. Correct conclusions may remain unchanged: method and assurance can improve without changing truth. Mere extra headings or verbose restatement FAIL the differential requirement.

Every pair must preserve mandatory core support, uncertainty, permissions, locked decisions and valid evidence. Test requested activation, no request, explicit disablement, locked conflict, authorised reopening, incompatibility, unsafe paths, missing package and cosmetic-only changes. The existing checker executes sixteen selection/precedence controls across the two profiles; those controls are **not** the whole differential suite. Source-strategy and semantic changes additionally require actual output review.

The accepted Stage 11 four source-backed outputs were re-read. SCH pack makes work/version counting and threshold applicability explicit while retaining core cautions; OSS pack reconciles package/server scopes and maps observed code risks to specific unperformed tests. Their fixed output pairs and authored review are existing procedural evidence, with shared acquisition/context and no independent installed trial. They are not reported as new agent runs or statistical proof. A later changed profile must repeat the affected actual comparisons rather than inherit its predecessor's PASS.

The authoring test also passes a redundant or purely project-specific proposal to create-pack. Acceptance requires catalogue inspection and a justified reuse/reject decision, not compulsory new files. A genuinely new draft remains labelled draft until its own showcase, differential behaviour and installed tests meet their contracts. Cross-family packs never acquire authority to interpret other domains' semantics.

## 7. Regression policy

For each escaped defect: preserve the failing submission and allowed evidence; diagnose the owning layer using actual traces; reduce to the smallest reproducer that preserves the cause; establish expected behaviour from sources or an explicit invariant; add a positive contrast and failing specimen; run the owning command/semantic check; then rerun dependent integration and release checks. Keep the original defect, mutation provenance, source/case version and repair identity linked. Do not replace a real failure with a fictional simplified account that changes its cause.

The evaluator has a read-only submission boundary. A producer applies the approved repair, preserving unaffected inputs and earlier issued revisions. Review the new target and dependent claims; do not edit an old passing timestamp to cover new prose. A bad oracle, changed live source, environment failure, permission failure and candidate regression are distinct diagnoses. Reclassifying a defect requires evidence and a versioned explanation, not making a test green by lowering its threshold.

Quarantining a flaky live-source case preserves the failure and prevents a reliability claim about the omitted behaviour. It never removes a mandatory release obligation silently. Replay sources may be legally unavailable or require deletion; retain permitted metadata, disclose lost reconstructability and select an authorised replacement in a new case version. Do not evade source terms to keep a benchmark convenient.

After a model/host/provider/parser change, rerun affected source fidelity, semantic and integration cases using comparable inputs. Report both regressions and improvements. After tuning against a hold-out, mark it exposed and replenish that split. After a material escaped defect, add regression coverage even if the broad example previously passed.

## 8. Release and maturity gates

| Gate | Required observed evidence | Failure treatment |
|---|---|---|
| G01 Repository/contract | Real package structure, valid SKILL.md and command discovery, local references, case consistency, all fifteen complete prompts and accurate README. | Fix the owner; no packaging PASS from a planned tree. |
| G02 Bounded command regression | Applicable positive/negative contract cases and known escaped defects detect the intended failure without changing inputs. | Broken scorer or missing required case blocks release assurance. |
| G03 Research quality | Actual source-backed retrieval, evidence, citation and synthesis assessment with material propositions checked; required specialist review performed. | Any mandatory FAIL remains FAIL; missing mandatory review/support is BLOCKED. |
| G04 Preservation and stopping | Observed scoped repair/refresh, parent resource bounds and untouched valid records, plus sufficient versus limited stops. | Full regeneration or unbounded retry cannot be excused by a good-looking final report. |
| G05 Packs | Core works without packs; requested/non-requested behaviour, precedence and actual paired specialist effects pass for implemented catalogue entries. | Do not advertise a cosmetic, conflicting, untested or unavailable pack as accepted. |
| G06 Clean external install | Actual documented GitHub installation from a clean consumer; selected skills/commands/references; EX-L1-01 outputs and evaluation; selective install; at least one implemented pack. | Local source checkout success does not pass this gate. Preserve logs and repair the exact dependency/route. |
| G07 Publication and maturity | Exact revision, completed mandatory gates, accurate measurement scope and required owner authorisation. | No merge, release, ready PR or registry promotion follows automatically from design or a score. |

`working` needs a real installed end-to-end research example. `benchmarked` additionally needs reproducible domain cases with isolated failures and operational regression protection, including implemented-pack coverage. `mature` also requires the six canonical responsibilities, accurate fifteen-example product surface, self-contained standalone use and clean external installation under the governing gates. These definitions are evidence requirements, not labels conferred in Stage 13.

A finite release matrix is declared before running: exact candidate revision, supported agents/execution modes, required cases, rationale for exclusions, budget, judge configuration and reviewer authority. Compare like with like. Any case-specific measured threshold must be justified and fixed beforehand; no arbitrary universal accuracy/latency percentage is introduced. Structural exact invariants have exact expectations; semantic uncertainty and unavailable observations are not rounded into a passing score.

## Verification, limitations and conformance

The executable reference suite was run, not merely written. Its [actual result](2026-09-10-stage-13-verification.json) records twelve priority cases, six additional cases, four independent-layer controls, nine packaging controls, sixteen pack-selection controls, six acceptance controls and four scorer-mutation controls. Positive and negative specimens were both checked; input preservation passed. These are tests of bounded typed reference rules and design controls, not live-agent scores, installation evidence, arbitrary-language entailment or independent human validation.

The document review checked the full original section 19 against the actual files and source inspection. It retains all ten layers and every listed concern, all twelve priority failures, the three temporal situations, the five external benchmark families, K01–K16/F01–F20, all fifteen examples, both packs, two independently sourced research topics, regression and release gates. Hold-out agent results remain null rather than fabricated. The package-control suite checks simulated path records; actual host discovery and installed references remain G06 obligations.

| Requirement | Specification reference | Deliverable / verification | Result |
|---|---|---|---|
| R01 | Section 19 evaluation layers | Sections 1 and 8 map all ten layers and every specified concern to an oracle, operation and gate. | PASS |
| R02 | Section 19 external references | Companion investigation records five original families, inspected scope, comparative reuse and limits. | PASS |
| R03 | Section 19 failure list | FX01–FX12 contain actual fixed inputs and positive/negative submissions; reference execution detects each. | PASS |
| R04 | Section 19 preservation/temporal clauses | FX03, TM02/TM03 and PR01 plus four-layer controls preserve separate temporal/dependency semantics. | PASS |
| R05 | Section 19 taxonomy/dimensions outputs | Section 2 retains every K01–K16 dimension and F01–F20 diagnostic class, with inspectable layer mapping. | PASS |
| R06 | Section 19 case-format output | Section 3 and companion case file separate task/oracle/submission/review and contain complete original research and pack contracts. | PASS |
| R07 | Section 19 end-to-end/progressive clauses | All fifteen EX IDs mapped individually; HO01/HO02 have complete disjoint-topic prompts, sourced oracles and explicit exposure limits. | PASS |
| R08 | Section 19 pack differential output | PD01/PD02 define actual method/source/audit differences, preservation and controls; accepted Stage 11 pairs were substantively re-read. | PASS |
| R09 | Section 19 regression/release outputs | Sections 7–8 define minimal reproducer, oracle correction, source drift, exposure and non-compensable actual-evidence gates. | PASS |
| R10 | Section 19 Exit; execution instructions | Executed reference suite demonstrates separable retrieval/evidence/citation/synthesis detection; actual results and limitations retained. Publication is verified after commit. | PASS |

No unresolved Stage 13 design decision requires requester input. No source/candidate research score, installed integration, clean external run or maturity promotion is claimed. After stage-scoped publication and readback, Stage 14 consumes these accepted contracts to generate all six canonical specifications. Nothing in this stage permits lowering their later implementation or verification obligations.
