# Stage 9: Gap Analysis and Over-Engineering Guardrails

Date: 10 September 2026. Repository: `sb-dev/deep-research-skills`. Branch: `feat/bootstrap`.

## Authority and accepted inputs

The acceptance contract is section 15 of the [original bootstrap](2026-09-07-deep-research-skills-new-project-bootstrap-process.md). Its source blob is `8ff62c92bada2861ece3684a9e73a83da75d9d94`. The research principles in section 5 and the relevant section 29 acceptance gates remain constraints, not optional improvements.

This design continues after the accepted [Stage 7 landscape](2026-09-10-stage-07-ai-tool-landscape.md), [candidate matrix](2026-09-10-stage-07-capability-matrix.md), and [Stage 8 execution architecture](2026-09-10-stage-08-execution-layer.md). Their content commits are `3d687208088d102179b1e3ed35be8b95e1f1c8fd` and `c3118cafc41ea0b93025c197e5fab48216d3fc37`. The [Stage 7 receipt](2026-09-10-stage-07-publication-receipt.md) and [Stage 8 receipt](2026-09-10-stage-08-publication-receipt.md) record their publication verification. The last accepted receipt revision at the start of this continuation is `affc8e7effff2270e29aed3fee1af7ed81873738`.

The [Stage 1 boundary](2026-09-10-stage-01-project-goal-and-boundary.md), [Stage 2 professional comparison](2026-09-10-stage-02-method-comparison.md), [Stage 3 information model](2026-09-10-stage-03-question-evidence-claim-model.md), [Stage 4 acquisition strategy](2026-09-10-stage-04-source-ecology.md), [Stage 5 workflow](2026-09-10-stage-05-workflow-and-artifacts.md) and [Stage 6 effort policy](2026-09-10-stage-06-effort-and-stopping.md) define the requirements being compared. This stage does not replace those accepted outputs or use a contradictory local publication receipt as evidence about the branch.

This is an architectural gap analysis of the inspected candidate landscape, not a new performance benchmark or exhaustive claim about every tool on the market. Candidate identifiers C01–C35 resolve in the Stage 7 matrix. Capability statements below refer to that dated investigation. Proposed native responsibilities and proof requirements are project decisions, not claims that they are already implemented.

## Acceptance checklist

| ID | Required result | Specification reference |
|---|---|---|
| R01 | Compare the accepted end-to-end workflow with the selected execution approaches. | Section 15 Purpose; accepted Stages 5, 7 and 8. |
| R02 | Define and apply covered, partially covered and missing without confusing documentation with tested integration. | Section 15 Classify. |
| R03 | Address every one of the thirteen named research gap areas. | Section 15 focus list. |
| R04 | Produce a native capability shortlist justified by actual residual responsibilities. | Section 15 Outputs. |
| R05 | Preserve concrete reuse decisions and the boundary between tool execution and research acceptance. | Section 15 Outputs; Stage 8 ownership. |
| R06 | Assess every one of the twelve named premature infrastructure proposals. | Section 15 Defer list. |
| R07 | Define candidate-specific evidence and a common decision gate before expensive architecture can be added. | Section 15 proof output and real-example/benchmark requirement. |
| R08 | Preserve uncertainty, provenance, authority, bounded effort, private project ownership and smallest-sufficient repair. | Sections 5 and 29; accepted Stages 1–8. |
| R09 | Review all five outputs against the original contract and persist this stage without modifying accepted earlier content. | Section 15 Outputs and Exit; staged execution instructions. |

The mandatory inventories are thirteen focus gaps and twelve deferred architecture ideas. The additional eight-row workflow mapping provides end-to-end coverage. No native skill count, provider performance threshold, new dependency or implementation surface is prescribed here. Stage 10 owns skill packaging; the shortlist below therefore names responsibilities rather than prematurely declaring installable skills.

## 1. Gap matrix

### Classification semantics

**Covered** means an inspected, reusable capability supplies the specified bounded operation, subject to the Stage 8 eligibility and result-intake checks. It does not mean an integration has been installed, tested or accepted in this repository.

**Partially covered** means tools provide useful inputs or some behaviour, but a required production responsibility, guarantee or test remains outside that capability. The residual must identify an owner and an observable acceptance condition.

**Missing** means the inspected landscape does not establish a reusable implementation satisfying the defined requirement. It does not prove that no solution exists anywhere, or justify building a platform before testing a smaller response.

Coverage concerns the exact responsibility named in a row. For example, bibliographic formatting can be covered while citation entailment remains partially covered. No aggregate score averages a critical provenance or permission defect against formatting quality. Deployment assurance remains unmeasured until the assigned implementation and installation stages execute it. [Stage 7 evidence limits; Stage 8 selection gates S01–S08.]

### End-to-end workflow coverage

| Workflow responsibility | Classification | Reusable assistance | Residual production responsibility and acceptance condition |
|---|---|---|---|
| W01 Frame and authorise | partially covered | Research engines and procedural skills can propose questions and obtain context. | Preserve the actual requester objective, exclusions and decision owner. A consequential ambiguity is resolved before acquisition; an engine-generated brief cannot grant authority. |
| W02 Plan method and source strategy | partially covered | C01/C34/C35 provide relevant procedural comparisons; engines suggest decomposition and searches. | Select the method, evidence units, eligibility, source restrictions and finite work envelope. Acceptance checks method fit rather than presence of a plan-shaped document. |
| W03 Discover and triage | partially covered | Native search, C10/C12, scholarly services and C19 provide discovery; exact record retrieval is covered for supported interfaces. | Record query scope, partial results, inclusion/exclusion and actual source access. Search ranking does not settle relevance, independence or completeness. |
| W04 Acquire, extract and establish origin | partially covered | Native retrieval, C20/C21/C22 and appropriate browser/data operations acquire or transform identified material. | Preserve exact representation, passage or data locator, material transformations and report/unit/origin relationships. A parsed document is not automatically faithful evidence. |
| W05 Map and challenge claims | partially covered | Citation metadata, reference contexts and appraisal guidance help locate and challenge support. | Bind actual propositions to inspected evidence, contrary evidence, assumptions, uncertainty and temporal scope. Neither URL existence nor an engine's narrative establishes support. |
| W06 Resolve a bounded gap | partially covered | Native queries and optional engines can execute a targeted follow-up. | Select a discriminating next action, reserve aggregate capacity, record its actual result and preserve unresolved gaps. A retry or another agent must not reset the budget or imply success. |
| W07 Synthesise and audit | partially covered | Generative engines draft; C24 formats; C30/C31 execute evaluation harnesses; C32/C33 supply benchmark references. | Audit the exact report against evidence, coverage, limitations and required review. Separate structural checks, semantic support and specialist assurance. |
| W08 Deliver and hand off | partially covered | Existing host/file/repository/application capabilities can deliver an authorised artefact. | Check audience, issued revision, source-access limits, validity and actual delivery receipt. Consumer production decisions remain outside research ownership. |

All eight workflow groups are partially covered as complete production responsibilities. This is not a claim that all execution is missing: the narrow operations in section 3 are reusable. It explains why wrapping a report engine in a new name would not satisfy the full accepted workflow. [Stage 5 W01–W08; Stage 7 I01–I11; Stage 8 O01–O12 and E01–E10.]

### All thirteen focus gaps

| ID | Focus area and classification | What existing capability contributes | Residual, smallest native response and acceptance evidence |
|---|---|---|---|
| G01 | Source independence: partially covered | Identifiers, source URLs, scholarly relations and reference contexts expose possible connections. | Record claim-relative originating observations separately from publication and event identity. A copied report must not add independent support; distinct observers of one event must not be falsely merged. Accept through labelled repeated-origin and independent-account cases, with the relationship rationale inspectable. |
| G02 | Primary-source preference: partially covered | Native/direct retrieval and C15–C19 can locate originating records; search filters narrow discovery. | Decide directness relative to the claim, pursue a required original, and label inaccessible-original gaps. A company's statement may establish its announced policy without establishing the policy's effectiveness. Test that a secondary summary is not promoted to inspected primary evidence. |
| G03 | Claim-level provenance: partially covered | Tools return source IDs, text, page coordinates, citations or operation records in varying forms. | Preserve the Stage 3 report-to-claim-to-evidence-to-representation path, with locators and transformations. Use compact records and reference-closure checks, not a new evidence service. Test relocation, missing IDs, changed representations and restricted-source handoffs. |
| G04 | Citation entailment: partially covered | C02/C15 check bibliographic identity; C21 exposes citation contexts; generic judges can assist semantic review. | Check the actual proposition, qualifiers, scope, negation, quantity and inference against inspected support. A valid DOI for a neighbouring claim fails. Acceptance requires known supported, partially supported and unsupported examples; model-judge agreement alone is not ground truth. |
| G05 | Contradiction handling: partially covered | Engines can retrieve conflicting text; C34/C35 and professional methods provide challenge guidance. | Retain eligible opposing/null findings, diagnose differing definitions or periods, and preserve genuine unresolved conflict. Use a contradiction record only when useful, linked to affected claims. Test both apparent and real disagreement and its effect on final wording. |
| G06 | Uncertainty calibration: missing for a validated general calibration guarantee | Tools provide confidence language or scores; specialist methods define context-specific assessment. None of the accepted evidence establishes a calibrated, cross-domain guarantee for this system. | Implement explained claim-level uncertainty and review first, not a fabricated percentage or truth score. Any later calibrated predictor needs a defined event/population, labelled outcomes, held-out assessment and drift monitoring. Until then, numerical calibration remains explicitly unmeasured; uncertainty must survive synthesis. |
| G07 | Temporal validity: partially covered | Services expose publication, version, retrieval and update information, sometimes with interface-specific filtering limits. | Preserve event, publication, effective, retrieval and valid-as-of meanings. Recheck only the changing basis and never advance validity merely by rerunning a request. Test old retrieved evidence, announced future changes, revised records and unchanged historical claims. |
| G08 | Inclusion / exclusion traceability: partially covered | APIs expose query/filter parameters and records; procedural review guidance describes screening. | Preserve declared eligibility, consequential exclusions and bounded search scope. Access failure, ineligibility, no match and lack of support remain different. Accept through cases where an adverse result remains eligible and a capped response is not called complete. |
| G09 | Research stopping criteria: partially covered | Engines expose selected call/iteration limits; providers and hosts impose quotas. | Apply Stage 6 evidence, review, authority and resource-stop distinctions. Use a finite next-action record and parent budget rather than a scheduler. Test diminishing duplicates with a known decisive gap, sufficient evidence with unused budget, and budget exhaustion without sufficient support. |
| G10 | Incremental refresh: partially covered | Versioned source retrieval and conditional or updated queries can acquire changed material. | Classify correction, freshness check, changed brief and relocation; update dependent evidence/claims without silently replacing the old basis. Test a new source that changes one conclusion and another that confirms unchanged findings. A check date alone does not refresh evidence. |
| G11 | Smallest-sufficient repair: partially covered | Tools can re-fetch, re-parse, recompute or revise a bounded item. | Diagnose the defective unit and follow material dependencies through claims, synthesis and review. Preserve unaffected records; expand the review boundary when dependency scope is uncertain. Acceptance compares before/after records and verifies that needed downstream changes occur without unrelated regeneration. |
| G12 | Cross-source deduplication: partially covered | Stable identifiers and bibliographic tools help identify duplicate records; hashes identify equal bytes. | Separate exact duplicate representations, multiple reports of a study, shared datasets and independent event observations. Ambiguous identity remains unresolved instead of forced merging. Test supplementary reports that must be retained, copies that must not inflate counts, and false-merge counterexamples. |
| G13 | Research benchmarkability: partially covered | C30/C31 provide harnesses; C32/C33 provide domain benchmark approaches and task-specific rubrics. | Define project-owned fixtures, input snapshots, support expectations and separate failure dimensions. Include source restrictions, provenance, repair, fresh/stale context, budgets and clean installation. Pin evaluator/data versions and permitted use. No upstream leaderboard score establishes these omitted production behaviours. |

These classifications do not authorize implementation of every possible missing feature. G06 explicitly limits the promise: the repository must communicate justified uncertainty, but it does not need to invent a universal calibrated probability engine. G13 concerns a demonstrable evaluation contract, not a requirement to run every external benchmark. The remaining gaps are responsibilities that later skill design must cover or explicitly constrain. [Stage 3 uncertainty and traceability; Stage 6 stopping/refresh; Stage 7 X01–X12; Stage 8 acceptance boundaries.]

## 2. Native capability shortlist

Native means reusable research production logic owned by this repository. It does not imply a new executable, service, database, agent role or separate installed skill. Stage 10 will determine the smallest packaging that can perform these responsibilities and remain selectively installable.

| ID | Native responsibility | Gap / workflow coverage | Smallest sufficient form and what it must not rebuild |
|---|---|---|---|
| N01 | Question, method and evidence-need framing | W01–W03; G02, G08, G09. | Skill guidance with an authorised brief, source map and method-relative acceptance criteria. Reuse source discovery; do not build a planning engine or force every task through a systematic-review protocol. |
| N02 | Evidence intake and relationship integrity | W03–W05; G01–G03, G07, G08, G12. | Instructions and proportionate local record checks for identity, access, locators, transformations and origin relationships. Reuse parsers and identifiers. A central evidence database is not required. |
| N03 | Claim analysis, contradiction and uncertainty | W05/W07; G01, G04–G07. | Claim-to-evidence review, alternative analysis and bounded uncertainty wording, with specialist escalation where required. Do not call a metadata validator a fact checker or a model score calibrated truth. |
| N04 | Bounded follow-up, stopping and incremental repair | W06 with re-entry to relevant operations; G09–G12. | Existing plan/gap/review records track next actions, resource reservations, changed dependencies and stop reasons. Reuse executor status queries and target readback. No daemon or mandatory swarm. |
| N05 | Research-specific evaluation and regression | W07; G03–G13. | Domain criteria, diagnosable cases, structural checks and semantic review using a suitable existing harness where needed. Keep fixture expectations independent from the implementation under test. Do not reimplement a general evaluation platform. |
| N06 | Evidence-bound synthesis and consumer handoff | W07/W08; G03–G07, G10, G11. | A reviewed report linked to support, gaps, temporal limits and a verified authorised delivery reference. Reuse formatters and destination tools. Do not own downstream strategy, implementation or public release decisions. |

N01–N06 intentionally overlap at boundaries: source independence must be established during evidence intake and respected during claim analysis. This is shared responsibility around one authoritative record, not duplication of its value. A later skill split must give each update one owner and explicit handoffs. The six responsibilities do not prescribe six skills.

A native implementation is justified only when an identified residual changes research behaviour, reduces an observed failure or preserves an acceptance invariant. Generic helper utilities that merely wrap an already-adequate host operation have no current justification. [Stage 5 artefact ownership; Stage 7 I01/I05/I06; Stage 8 native-first architecture.]

## 3. Reuse decisions

| ID | Bounded operation | Coverage / decision | Selected reuse direction and retained limit |
|---|---|---|---|
| U01 | Known repository and application retrieval | covered at the supported operation level; USE | Prefer existing authorised native access, including C19 for exact GitHub revisions. Read the actual action contract and result scope. Do not add a second connector simply to duplicate available access. |
| U02 | General web discovery | covered for indexed discovery; USE | Use adequate host search; C10/C12 are conditional alternatives when enabled and justified. Search results remain leads, with index and filter limits. No custom search engine. |
| U03 | Scholarly identifier lookup and corpus discovery | covered for documented record retrieval; USE | C15/C16/C18 serve distinct metadata, broad discovery and biomedical needs; C17 is a gap-specific alternative. Neither one DOI nor several databases establishes independent studies or full-text access. |
| U04 | Ordinary HTML extraction | covered for the selected transformation; USE | C22 is the lightweight augmentation when native reading is inadequate. Preserve original context and check consequential extraction. Do not create a general crawler to parse one page. |
| U05 | Advanced document extraction and reference contexts | partially covered for faithful research evidence; USE selectively | C20 handles justified document conversion; C21 is specialist for scientific reference/coordinate needs. Fidelity still needs inspection. C03 is not suitable for vendoring under its inspected restrictive terms. |
| U06 | Dynamic browser interaction | covered for supported bounded actions; USE selectively | C13 is the chosen direct-action route where native/direct access is inadequate; C14 remains conditional for actual autonomous navigation needs. Browser operation is not permission to bypass access controls. |
| U07 | Broad iterative research | partially covered as full research production; USE as optional engine | C05 hosted and C08 self-hosted are alternatives under Stage 8 eligibility. Preserve run identity, scope, bounds and source output; accept no report without evidence intake and audit. C06/C07/C09 remain researched alternatives, not simultaneous core dependencies. |
| U08 | Citation identity and rendering | covered for identity lookup / formatting; ADAPT or USE by subtask | C02 may supply useful bibliographic procedures and C24 renders references. Preserve exact licences and self-containment before reuse. Entailment remains N03/N05, not a formatter responsibility. |
| U09 | Local calculations and isolated execution | covered for configured computation; USE selectively | Existing simple calculation is preferred; C26 addresses a real structured-data need. C27 is conditional on isolation requirements and authorised processing. Local analysis does not mandate a persistent database. |
| U10 | Existing reference libraries and notes | covered only within the authorised app surface; USE optionally | C25/C28/C29 expose consumer-owned material when already relevant. Preserve maintenance, permission, index and access limitations. They are not required evidence stores. |
| U11 | Evaluation harness and external benchmark methods | partially covered for project acceptance; USE / REFERENCE | C30 is the selected harness direction; C31 an alternative. C32/C33 are references with version and data-use constraints. Add domain cases rather than replacing acceptance with an upstream aggregate score. |
| U12 | Useful procedural research semantics | partially covered for the cross-domain contract; ADAPT selectively | C01/C34/C35 offer specific method and evidence-binding ideas. Evaluate their specialist assumptions, external dependencies and review requirements. Do not import universal figure quotas, source quotas or a development helper as the complete research workflow. |

USE here is a design reuse decision, not a claim that installation has occurred. ADAPT requires inspecting the exact selected material, preserving applicable notices and testing the behavioural change. REFERENCE permits analysis without importing code or claiming integration. All routes retain Stage 8 authority, processing, source-control, fidelity, temporal, resource and method gates. [Stage 7 shortlist and I01–I11; Stage 8 execution modes.]

## 4. Deferred-improvement register

Every proposal below remains deferred. The simpler alternative is the current default. A future proposal must provide its row-specific evidence plus the common proof record in section 5. A tool failure caused by wrong configuration, a missing permission or a misunderstood schema is not evidence that new infrastructure is necessary.

| ID | Deferred proposal | Current simpler alternative | Specific evidence required to reopen it |
|---|---|---|---|
| D01 | Custom general web crawler | Native/direct retrieval, C22 extraction, and an authorised existing crawler only for a demonstrated coverage need. | Representative allowed-source tasks repeatedly fail because existing acquisition cannot expose required evidence; compare source coverage, fidelity, time, operational cost and maintenance against at least the adequate existing routes. A single blocked page or forbidden access route does not justify circumvention. |
| D02 | Custom search engine | Existing host search and relevant specialist indexes with explicit corpus limits. | A defined, permitted corpus has important retrieval requirements unmet by existing indexes or a small local search solution. Measure recall/precision against independently labelled tasks and account for indexing freshness, licence and ongoing operations before proposing an engine. |
| D03 | Universal provider registry | A short skill-local compatibility/reference table and direct tool-contract inspection. | Several implemented integrations repeatedly duplicate the same necessary selection metadata, and a smaller shared record removes demonstrated defects without hiding meaningful endpoint differences. Brand lists or hoped-for providers are not evidence. |
| D04 | Universal research workflow DSL | Domain instructions, explicit operation handoffs and ordinary artefact records. | Real distinct workflows need repeatable automation that simpler instructions or an existing host cannot support. Demonstrate a bounded representation preserving specialist variation, interruption and repair; compare cognitive and operational cost. Do not encode another domain's lifecycle as universal research semantics. |
| D05 | Persistent cross-project evidence database | Consumer-owned files or an already-authorised project repository/library. | Multiple real consuming projects require permitted cross-project reuse, with demonstrated identity, access, deletion, versioning and provenance needs that project-local records cannot meet. Show rights and tenancy isolation before any sharing. Duplicate public citations alone are insufficient. |
| D06 | Universal knowledge graph | Local IDs, explicit source/origin relations and scoped dependency references. | Real examples require queries or dependency analysis that simpler records cannot safely perform at the observed scale. Benchmark the useful operations and update correctness, including ambiguous identity and deletion. A diagram of relations is not proof that a graph store is needed. |
| D07 | Vector database by default | Exact/semantic search already supplied by the authorised host, or scoped local file retrieval. | A defined large corpus and query set demonstrate that existing retrieval or a smaller local index is inadequate; compare semantic recall, false matches, stale-index behaviour, access isolation and operating cost. Evidence may justify an optional index, not an unconditional default for every task. |
| D08 | Multi-agent swarm by default | One accountable research process with optional disjoint, bounded delegated tasks. | Controlled task comparisons show meaningful benefit after counting duplicate work, coordination, source dependence, review and aggregate cost. Test lost workers and outstanding reservations. More parallel outputs cannot substitute for independent evidence or expert human review. |
| D09 | Fully automated numeric source-quality score | Separate claim-relative quality dimensions and explained uncertainty. | The original universal-score proposal conflicts with the accepted multidimensional quality rule and cannot be promoted unchanged. A narrower method-specific assessor would need explicit constructs, competent labels, held-out evaluation, uncertainty and failure analysis; it must not erase adverse dimensions or impersonate calibrated truth. |
| D10 | Continuous research daemon | A bounded refresh operation invoked by the consumer's existing scheduling arrangements. | A real recurring research use has documented freshness/service needs and a measured benefit over user-triggered or existing scheduled runs. Demonstrate budget ceilings, source rights, deduplication, change relevance, safe shutdown and ownership of review/notification. No daemon is justified merely because facts can change. |
| D11 | Universal citation format converter | C24/C25 or another suitable existing bibliographic processor. | Actual required formats or identifiers remain unsupported after evaluating existing processors and a narrow adapter. Provide fixture-based correctness and round-trip/loss analysis. Presentation gaps do not justify conflating citation conversion with support verification. |
| D12 | Research orchestration platform separate from Agent Skills | Portable skills using existing host operations and consumer-owned records. | Independently implemented production use demonstrates necessary scheduling, state or coordination that cannot be met by the current host or small components. Compare full lifecycle cost, failure recovery and adoption burden. Any justified service remains optional and must not become the owner of core research judgement or downstream decisions. |

The register is not a postponed implementation roadmap. D01–D12 are conditional questions; no stage completion automatically promotes them. When an alternative is enough, close the proposal with the evidence and keep the simpler design. If a demonstrated need is narrower than the proposal, implement only the narrow need. [Original section 15; Stage 7 rejected alternatives; Stage 8 architecture.]

## 5. Proof required before expensive architecture

### Required proposal record

A proposal must identify the exact gap IDs and a concrete consuming task. Preserve the current baseline implementation/version, authorised source set, task and expected result, observed failures and the evidence supporting the diagnosis. Separate a missing production rule from an unavailable tool, an incorrect invocation, an access restriction, a source-quality problem and an actual infrastructure limitation.

Evaluate the least complex plausible repair first. The comparison must include the existing adequate tool or host route, a narrow procedure/adapter where reasonable, and the proposed architecture. Keep inputs, source permissions, evaluation criteria and relevant resource budgets comparable. No result may be manufactured from planned tests, synthetic expected outputs or provider advertising.

| Proof ID | Required evidence | Rejection condition |
|---|---|---|
| P01 | Reproducible real-example failure, input/source revisions and an explicit unmet requirement. | A hypothetical future need, a generic popularity signal or a screenshot without the underlying task/result. |
| P02 | Diagnosis linking the failure to missing architecture rather than method, permission, configuration or fidelity. | The proposed system would merely automate an existing mistake or bypass a legitimate access boundary. |
| P03 | Comparison with the smallest adequate reuse or procedural repair. | No baseline, a deliberately weak baseline, or ignoring a currently usable existing component. |
| P04 | Prespecified acceptance criteria and independently reviewable results on representative cases. | Moving the threshold after seeing the result, only happy-path demonstrations, or treating model self-approval as substantive assurance. |
| P05 | Total resource and maintenance assessment, including migration, review, failure recovery and ongoing data freshness. | Measuring only call price or best-case latency while ignoring required review, state or maintenance costs. |
| P06 | Authority, processing, source/control, licence, retention, deletion and rollback evidence appropriate to the proposal. | Unauthorised data movement, unbounded commitments, missing ownership or no viable retreat to a coherent prior state. |
| P07 | A bounded implementation scope, owner, integration contract and regression cases for the failure being repaired. | A universal platform whose necessary boundaries and consumers cannot be specified, or a new dependency without a diagnosable acceptance test. |

The proposer states meaningful target values before the comparison where measurements are suitable. This document does not invent universal recall, accuracy, speedup or cost thresholds across unlike tasks. A severe permission, provenance or support failure cannot be compensated by a faster mean runtime. Report failed and inconclusive experiments as well as favourable ones.

A design fixture can test a control or illustrate a failure; it does not by itself satisfy P01's real-example requirement. A source that documents a feature supports a capability hypothesis, not measured effectiveness. The current bootstrap's design validators are therefore not evidence that D01–D12 have earned implementation.

### Promotion decision

The decision records one of: retain the simpler approach; implement a smaller scoped repair; conduct an authorised bounded comparison; or adopt the demonstrated component within its measured scope. Record the evidence, rejected alternatives, remaining uncertainty and conditions that would trigger reversal. A missing mandatory permission, review or supporting result prevents adoption, not completion of this gap-analysis stage.

A **family-shared abstraction has an additional requirement**: at least two independent domain implementations must demonstrate substantially the same need; useful domain variations must remain owned locally; and the shared contract must be smaller than the duplicated reasoning it replaces. This is not a requirement that every local bug fix wait for two domains. It is the additional promotion gate for shared family infrastructure. [Production Skills, `docs/bootstrap/shared-abstraction-process.md`, revision `d109b1f5f085f9493711803c0c801b9812427d57`, blob `e8c58d2544b73c06ea6b22fccc3b6ddfdbd1a11d`.]

None of the twelve proposals is promoted by this stage. The selected immediate direction is to implement meaningful research procedures and their evidence/review contracts on top of reused execution capabilities. The consumer retains project knowledge and lifecycle; optional Pactwright integration must not absorb research semantics.

## Conformance review

The review compares this document with the original Stage 9 requirements, not an arbitrary source count or a shortened replacement brief. It covers the eight accepted workflow groups, all thirteen focus areas, the six responsibility-based native directions, the twelve reuse decisions, every deferred proposal and its proof conditions.

| Requirement | Deliverable and substantive verification | Result |
|---|---|---|
| R01 | Section 1 maps W01–W08 to actual assistance, remaining responsibility and acceptance evidence. | PASS |
| R02 | Classification definitions separate bounded capability coverage, production responsibility and unmeasured deployment assurance; all three labels are applied. | PASS |
| R03 | G01–G13 match every named focus area; each identifies capability, residual and an observable test or deliberately bounded promise. | PASS |
| R04 | N01–N06 name native responsibilities with explicit gap/workflow mapping, lean form and rebuild exclusions; no skill count is fixed. | PASS |
| R05 | U01–U12 preserve the Stage 7/8 native-first and selective reuse decisions while retaining source, permission and acceptance boundaries. | PASS |
| R06 | D01–D12 cover every original infrastructure warning, with a simpler present alternative and proposal-specific reopening evidence. | PASS |
| R07 | P01–P07 define real-example diagnosis, baseline comparisons, reviewable measurements, full cost, authority and bounded scope; family promotion retains its additional independent-domain gate. | PASS |
| R08 | The analysis preserves source/evidence/claim distinctions, uncertainty, temporal validity, counterevidence, consumer authority, bounded work and targeted repair. | PASS |
| R09 | Sections 1–5 provide all five required outputs. Earlier stage files are referenced, not replaced. No implementation, benchmark score or maturity promotion is claimed. | PASS |

This conformance table is a substantive design review, not an assertion that software or live research benchmarks ran. Publication verification is a separate operation: inspect the created commit, its parent, the actual stage file and the branch before marking the stage remotely verified. Do not infer publication failure from a lost response, and do not invent a commit identity inside its own content.

## Exit assessment

The project now distinguishes reusable execution from the residual research responsibilities it must own. It has a native capability shortlist, concrete reuse decisions and explicit protection against all twelve premature infrastructure proposals. No unresolved Stage 9 design choice requires a requester decision.

Stage 10 must use these results to derive the smallest coherent, selectively installable skill set without turning N01–N06 into a predetermined number of skills. It must preserve the accepted end-to-end workflow, evidence and review semantics while reusing execution rather than rebuilding it. The deferred register remains conditional; later implementation and benchmark stages provide evidence, not automatic permission to introduce the deferred architecture.
