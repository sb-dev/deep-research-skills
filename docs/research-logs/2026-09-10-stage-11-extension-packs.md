# Stage 11: Extension Packs and Pack Authoring

Date: 10 September 2026. Branch: `feat/bootstrap`. This is the complete pack design and procedural comparison, not a claim of clean installed execution or repository maturity.

## Authority and prerequisites

The contract is [bootstrap section 17](2026-09-07-deep-research-skills-new-project-bootstrap-process.md#17-stage-11--design-extension-packs-and-pack-authoring), read from `main` at blob `8ff62c92bada2861ece3684a9e73a83da75d9d94`, with sections 5 and 29 and the family Evaluation and Extension Packs specification, sections 9–19, blob `b021c438396b6073f08c09619bbd619c2a4aa601`. The accepted predecessor is Stage 10 content `565996be247db7e6534900be82dbc8de1c41c254` and receipt `27b2714b306cab0362e69af21deddd2d3106c6f7`.

The accepted [Stage 10 responsibility map](2026-09-10-stage-10-core-skills.md) and [create-pack/audit contracts](2026-09-10-stage-10-command-contracts.md) were re-read. They retain `deep-research`, `research-evaluate` and `research-extension-pack-creator`, with no mandatory sibling dependency. The earlier Stage 1 boundary, Stage 2 method comparison, Stage 3 information model, Stage 4 acquisition strategy, Stage 5 records and repair rules, Stage 6 budget/refresh rules, Stage 7 tool landscape, Stage 8 executor boundary and Stage 9 infrastructure guardrails remain the accepted inputs. The progress index and Stage 10 receipt verify their accepted status; this stage changes none of their substantive files.

The requested removal of the continuation-only tip was performed before work: `d3b30340f0e10cad89533d5423787b09e347e275` had only the continuation note and parent `27b2714b306cab0362e69af21deddd2d3106c6f7`. The branch was read back at that parent. No completed stage was removed. No historical, unavailable Stage 11 test count is treated as an executed result in this continuation.

### Acceptance checklist

| ID | Required activity or output | Contract |
|---|---|---|
| R01 | Verify predecessor, read original stage and applicable authority; preserve accepted boundaries. | Execution sections 3/9; bootstrap sections 5/17/29. |
| R02 | Define pack qualification and all eight possible specialisation dimensions. | Section 17 qualification list; family section 11. |
| R03 | Investigate and narrow all seven named candidate families using real method/source evidence. | Section 17 candidate catalogue. |
| R04 | Define activation, precedence, conflict, compatibility and core independence. | Section 17 precedence; family sections 10–13/18. |
| R05 | Define a usable format and self-contained packaging, with honest design/installation status. | Section 17 packaging output; Stage 10 self-containment. |
| R06 | Specify the complete twelve-step authoring workflow and its acceptance/mutation boundaries. | Section 17 authoring workflow; Stage 10 create-pack. |
| R07 | Define showcases and provide exact prompts for both selected profiles. | Section 17 showcase/exact-prompt requirement; family section 14. |
| R08 | Perform core-versus-pack comparisons showing substantive effects, retaining actual outputs and limitations. | Section 17 Required differential evaluation and Exit. |
| R09 | Define pack-aware activation, fidelity, precedence, preservation and negative-case evaluation. | Section 17 evaluation-plan output; family section 15. |
| R10 | Verify six outputs, record conformance and commit/verify only this stage. | Execution sections 5–8; section 17 Outputs/Exit. |

The required inventories are eight dimensions, seven candidate families, twelve authoring responsibilities and six output responsibilities. The source does not prescribe a pack count. Two are selected by complementary evidence units and demonstrated behaviour, not a predetermined quota. The fifteen primary examples and six canonical specifications belong to Stages 12/14; installed packages and clean installation belong to Stages 17–20. The current comparisons are actual in-session applications on real sources, not substitutes for those later installation gates.

## Research and decision basis

The [source register](2026-09-10-stage-11-sources.md) records primary method evidence and the real comparison sources, including partial-access limits. The investigation combines accepted professional-method distinctions with fresh checks of scholarly version linkage, ethical collection, horizon scanning, primary-source interpretation and repository evidence. It does not use a provider report to define the domain.

The selected profiles in [profiles.json](2026-09-10-stage-11-profiles.json) contain the exact behavioural content used in the [comparison protocol](2026-09-10-stage-11-comparison-protocol.md). That protocol was recorded before the four outputs were written. The source-backed [comparison record](2026-09-10-stage-11-comparisons.md) preserves both conditions without intentionally hiding known findings from core. Source observations, generated analysis, synthetic controls and installed-agent evidence remain distinct.

## 1. Pack semantics

A research Extension Pack is reusable, domain-owned specialist knowledge that changes how the core researches a coherent class of questions. It is not a project brief, private evidence collection, provider preset, mandatory workflow runtime or another family's pack interpreter. Qualification requires a real reusable context; meaningful behavioural changes; an explanation of why those rules are inappropriate as universal defaults; an observable showcase; and an evaluation capable of distinguishing the intended effect without unacceptable regressions.

A pack does not make the core careless. Core already requires provenance, source independence, qualified claims, counterevidence and bounded work. The specialist adds concrete source units, methodological tests and reporting expectations for its context. It cannot claim sole ownership of a core safety or quality invariant. If a proposed change merely repairs a general core defect, repair core instead of creating a pack.

### All eight dimensions

| Dimension | Permitted specialisation | Boundary that remains invariant |
|---|---|---|
| Source ecology | Identify specialist corpora, identifiers, source classes and evidence units. | Access and processor authority, original-source fidelity and honest limits. |
| Search strategy | Specialist vocabulary, citation chaining, corpus and temporal methods. | Question-relative scope, actual search records and finite effort. |
| Inclusion / exclusion rules | Study/design, repository/use-case or period-specific eligibility. | No exclusion merely because a result is inconvenient; unavailable differs from ineligible. |
| Source appraisal | Method-specific checks or repository evidence classification. | No universal truth score, prestige shortcut or invented expertise. |
| Research methods | Work/report linkage, cross-file reconciliation or longitudinal comparison. | Source statements and interpretation remain distinct and transformations inspectable. |
| Synthesis structure | Evidence-unit grouping and context-appropriate comparison. | Answer the actual question; preserve contrary findings and uncertainty. |
| Quality criteria | Add independently reported specialist criteria. | Core failures cannot be averaged away; structural and semantic checks remain separate. |
| Reporting conventions | Publication identifiers, code locators, appropriate terminology and method declaration. | No certification of unperformed methods, execution, review or rights clearance. |

Each profile explicitly states its treatment of each dimension; a future pack may mark a dimension unchanged with justification. One material change can qualify, but a different label, template or verbosity alone cannot.

### Activation and precedence

Selection is explicit. Mentioning a topic, reading a catalogue or having files installed does not activate a pack. The run records selected ID, exact version/content identity, scope, compatible core contract and any overridden defaults. A core-only request leaves no selected pack. A requested unknown, unreadable or incompatible pack produces an explicit blocker for that selection; it is not silently ignored or replaced. Suggesting a pack does not activate it.

Precedence is: explicit research instructions → approved / locked research decisions → selected Extension Pack → core Deep Research defaults. Permissions, safety boundaries, truthful evidence and required review are not weakenable defaults. When explicit instructions unambiguously authorise changing an owned locked decision, record that change before applying it. When the instruction merely conflicts with a lock, ask the owner; do not infer an override. A pack never reopens approved work by itself.

For an individual field, apply an authorised explicit value first, otherwise the approved decision, otherwise the selected pack's relevant default, otherwise core. Record material overrides and why the resulting method remains coherent. For example, an explicit supplied-corpus-only instruction prevents a scholarly pack from contacting additional databases; the output may be a bounded review but cannot call itself exhaustive if its required method was not performed.

One profile is selected per investigation in the initial format. Multiple subinvestigations may select different profiles and hand off evidence under the existing Stage 5 contracts. Two packs requested for the same investigation require a deliberate scoped choice or a documented compatible split; there is no silent last-loaded-wins merge. No new cross-domain interpreter is introduced. This decision prevents unresolved method conflicts, not cross-domain research.

Changing or deactivating a pack affects future operations and dependent outputs, not the historical basis of issued research. Preserve evidence still applicable under the new method, identify what must be rechecked and obtain approval before reopening a locked consumer decision. Pack absence does not remove a previously required review.

## 2. Format and packaging

Use a small data-and-Markdown bundle. No loader service, lifecycle engine or executable configuration language is required.

```text
extension-packs/<pack-id>/
  pack.json
  PACK.md
  references/method.md
  examples/showcase.md
  evals/cases.json
```

These are the required responsibilities of an installable bundle, not empty folders to create during this design stage. `PACK.md` owns procedural instructions and command effects. `pack.json` owns identity, version, compatibility, activation and local entry points. `method.md` supplies reusable source-backed expertise and limits, not copies of proprietary works or private project evidence. `showcase.md` includes premise, constraints, exact prompt, expected effects and actual-output/evaluation status. `cases.json` records observable behaviours, fixed input references and explicit expected results. Files may be consolidated only when the same responsibilities and unambiguous local navigation are preserved.

### Manifest contract

| Field | Required meaning and validation |
|---|---|
| format_version | Integer identifying the local pack contract. Unknown versions fail selection rather than best-effort interpretation. |
| id, version | Stable lowercase-hyphen identifier and semantic content version. Duplicate identities with different bytes require explicit reconciliation. |
| core_contract | Compatible research contract or bounded version range, checked before activation. Compatibility cannot be inferred from a similar skill name. |
| status | Separate designed, procedure-demonstrated, installed-tested and behavioural-evaluation state; never imply a later state from an earlier one. |
| purpose, not_for | Coherent reusable use case and explicit exclusions. A single customer's facts cannot substitute. |
| dimensions | Every one of the eight dimensions, each changed or unchanged with rationale. |
| effects | Target core command/focus, operational change and observable consequence. Unknown command/focus is invalid. |
| preserved | Core, authority, evidence, uncertainty, effort and repair invariants. These may not be weakened. |
| method_sources | Locatable sources with version/access limits, distinguishing evidence from the author's adaptation. |
| activation, precedence, composition | Explicit selection and non-activation, stronger instructions/locks and conflict resolution. |
| showcase, evaluation | Exact prompt and behaviour expectations, actual output/result references and limitations. |
| entry points / dependencies | Pack-root-local files; declared optional tools/services and processors. Missing required content fails validation. |

The current profiles JSON is a design projection containing the full profile rules plus research-log-relative demonstration locators. It is labelled not installed. The production bundle must copy the necessary content into pack-local files and use pack-root-local entry points; it must not depend on this research-log path or a source checkout. This is an explicit packaging acceptance rule, not a claim that the design projection is already an installed pack.

Resolve relative paths against the known pack root, not the process working directory. Reject path traversal, absolute file paths and symlinks escaping that root for bundled dependencies. Research inputs are separately authorised consumer paths. External scholarly/GitHub URLs are evidence links, not implicit load-time execution. Validate exact fields and local references, but do not mistake JSON validation for method correctness.

Installing or reading a pack must not execute scripts, acquire credentials, contact sources, spawn workers or alter a research record. Optional tool use follows Stage 8 eligibility and Stage 6 resource limits. A specialist procedure requiring a new processor, payment or human input must obtain that authority before the commitment. A pack cannot make an unavailable source available by declaring a dependency.

Version changes that affect behaviour, sources, precedence, compatibility or evaluation interpretation require an identifiable revision and affected tests. Historical reports retain the profile identity actually used. A corrected profile does not retroactively validate their results.

## 3. Initial catalogue strategy

### Investigation of all seven candidate families

| Candidate | Source-backed opportunity | Distinctness / cost analysis | Decision and condition for reconsideration |
|---|---|---|---|
| scholarly-evidence | Study/report linkage from S04; real publication/version and benchmark-method issues in S01–S03. | Different evidential units and design-specific appraisal materially affect counting and applicability; generic source checks alone do not prescribe them. | SELECT. Keep bounded research and formal review modes distinct; do not promise clinical or systematic-review certification. |
| market-intelligence | Accepted Stage 2 M3 and S06 distinguish decision needs, ethical collection and honest conclusions. | Useful, but a consumer brief plus existing core comparative research covers many initial tasks. A broad business-decision pack risks absorbing Business Building ownership. | DEFER. Require a repeatable market-measurement/sample or syndicated-estimate comparison that changes research behaviour without owning strategy. |
| technology-landscape | Accepted Stage 2 M4/S20 and S09 identify specialist technology/patent corpus methods. | Overlaps scholarly and repository research for ordinary tool comparisons; patent-family and coverage methods need a sharper supported specialist scope. | DEFER. Demonstrate a bounded corpus/family or technology-maturity method not already satisfied by selected profiles plus instructions. No patent-rights advice. |
| open-source-ecosystem | S10 separates repository-risk signals; S11–S17 expose documentation, code, package and maintenance evidence. | Cross-file environment reconciliation and static-versus-executed assurance materially change adoption research. It is complementary to scholarly work rather than a provider adapter. | SELECT. Static assessment can be complete while installed readiness remains untested; do not turn stars into approval. |
| trend-and-signal | S05 distinguishes weak signals, scope and time horizons. | A useful future specialisation, but current core temporal/refresh rules already support a one-time update. Real longitudinal behaviour is needed to justify more than a template. | DEFER. Demonstrate comparable time windows, changing definitions, signal/noise and leading/lagging interpretation on a genuine longitudinal task. No daemon or calibrated forecast by default. |
| creative-reference-research | S07 supports separating observations, interpretation and further questions; Stage 1 retains creative-production ownership elsewhere. | Research can feed creative work, but a style/genre label alone is not a research pack. Rights, cultural context and source-purpose differences need a concrete reusable method. | DEFER. Show a reference brief where provenance/context handling changes research while story, design and assets remain consumer-owned. |
| investigative-osint | S08 requires verifiable evidence, privacy/harm attention and literal human editorial responsibilities. | Sensitive collection, authenticity, rights of reply and specialist review make a broad initial pack risky. Generic agents cannot claim those institutional roles. | DEFER / specialist later. Require a bounded legitimate source method, actual expert review route, privacy tests and a non-sensitive showcase. Do not inherit permission to contact or investigate people. |

Selection minimises overlap in *evidence units*, not merely topic names: scholarly work handles related publications and empirical-method applicability; repository work handles code/package/version evidence and operational assurance. The two selected profiles have complete dimension/effect maps and exact prompts. Deferred entries are not advertised as available catalogue packs and have no implied successful comparison.

A catalogue entry records ID/version, coherent use case, grammar, changed commands, preserved boundaries, source basis, exact showcase, actual comparison result and separate installation/maturity state. The design catalogue consists only of the two selected profiles. It does not promote repository maturity. A future entry must satisfy the same qualification and comparison gates rather than being added because its name sounds useful.

## 4. Pack authoring contract

Use the existing `research-extension-pack-creator`, operation `create-pack`. Inputs are an explicitly requested reusable context, authorised catalogue snapshot, current core/pack contracts, method evidence, any existing draft, permitted source/processor scope and bounded resources. Output is a justified reuse/rejection decision, a requested draft, or an accepted package only to the level actually demonstrated.

| Step | Authoring responsibility | Durable output and completion condition |
|---|---|---|
| A01 | Inspect catalogue | Read actual existing IDs/versions, use cases, limits and comparison results. Missing catalogue access is not proof no pack exists. |
| A02 | Determine whether a pack is justified | Apply reusable/material/irrelevant-to-core/showcase/evaluable tests; compare existing pack plus brief, core repair and a new pack. Record rejected alternatives. |
| A03 | Research specialist method / source ecology | Inspect primary method sources and realistic evidence units, with dates, access limits and applicability. Do not substitute a provider feature list for professional practice. |
| A04 | Define boundaries and production grammar | State input units, permissible relationships, method operations, findings and handoff. This is domain procedure, not a workflow DSL. Identify specialist or human limits. |
| A05 | Define changed core behaviour | Map each change to a Stage 10 command/audit focus, activation condition, records affected, invariants and observable effect. Repair core for general defects. |
| A06 | Define pack-aware evaluation | Freeze comparable tasks, invariant checks, intended differences, failure/negative cases and review before evaluating outputs. No post hoc moving threshold. |
| A07 | Implement | Write the requested self-contained instruction/data bundle in its authorised working area. Validate identity and paths. Do not modify core defaults or publish automatically. |
| A08 | Create showcase | Use a realistic task with lawful accessible evidence. Keep recorded observations separate from generated reports and synthetic counterexamples. |
| A09 | Include exact generation prompt | Include all scope, source, pack-selection, authority, output and evaluation instructions. No missing placeholder or reliance on private chat context. |
| A10 | Compare core versus core+pack | Execute both conditions under recorded comparable inputs; preserve outputs and actual review. A predicted difference or extra metadata alone fails. |
| A11 | Validate | Check structure, selection, precedence, fidelity, evidence support, preservation, negative cases and the requested acceptance level. Run required tests; repair and rerun failures. |
| A12 | Catalogue | Only publish/update the authorised catalogue entry with evidence-backed status. A valid draft can remain a draft; acceptance cannot invent clean installation or independent review. |

The creator writes only the authorised pack working area and new review records. It cannot edit a consumer's report, alter evidence, install tools, publish to another repository or reopen locked decisions without corresponding authority. The evaluator reads fixed inputs and writes separate findings; the creator applies authorised repairs, then changed content is reviewed again. A shared assistant demonstration must be labelled as such, not independent assurance.

The smallest repair is the defective rule, method reference, compatibility declaration, prompt, fixture or local path. Preserve valid methods and outputs; rerun affected activation/comparison checks and any dependent installation check. Reject a cosmetic pack rather than inventing a new comparison designed to favour it. If core already meets every proposed specialist requirement with no meaningful difference, choose core/reuse rather than forcing pack survival.

## 5. Showcase contract

Every selected profile has a realistic premise, pack-specific constraints, complete copyable prompt, source-access declaration, expected operational effect and relevant evaluation criteria. Current exact prompts for both conditions are in the comparison protocol; outputs are retained in the comparison record. There are two showcases, one per selected profile. They are not the fifteen primary progressive examples.

A showcase identifies the core/profile revision, source scope, evidence units, allowed tools, processor/expense authority, requested output, stopping conditions, actual operation record and limitations. Keep source material lawful and minimal. Public demonstration does not require making confidential supporting evidence public. A source-backed narrative is generated output; the underlying source observation remains separately locatable.

The scholarly showcase uses RULER to test publication linkage and transfer of a benchmark conclusion. It must not masquerade as a systematic review or an independent model experiment. The repository showcase assesses the pinned Open Deep Research source. It must not masquerade as an installed smoke test, security assessment or deployment approval. Both have useful complete research outcomes at their bounded scopes.

A claimed result must point to an actual output and review. Showcases whose sources become inaccessible retain historical evidence and disclose the limitation; a new currentness claim requires the appropriate delta check. Exact prompts pin the research purpose and source identities so they can be rerun, but later results may differ when the prompt deliberately asks for current information.

## 6. Pack evaluation plan and performed comparison

Evaluation has separate layers: manifest/local-reference validity; activation and non-activation; stronger-instruction/lock precedence; method/evidence fidelity; meaningful differential behaviour; preservation/repair; domain boundary; and installed execution. A failure at one layer remains visible even when another passes. The last layer is a later Stage 18/20 gate; no result here claims to have run it.

### Required behavioural cases

| ID | Case | Observable acceptance |
|---|---|---|
| E01 | Explicit compatible selection | Apply only the selected profile and record exact identity/scope. |
| E02 | No selection / explicit core only | No pack effects or silent activation from a topic or filename. |
| E03 | Unknown/incompatible profile | Explicit selection blocker; no fallback labelled as the requested pack. |
| E04 | Explicit source restriction versus pack default | Preserve allowed corpus/processor before acquisition; report method limitations. |
| E05 | Locked decision versus pack default | Preserve the lock; require its owner to reopen it when necessary. |
| E06 | Ambiguous explicit/locked conflict | Block the affected decision; do not silently infer an override. |
| E07 | Multiple profiles for one investigation | Require coherent scope/split; never last-loaded-wins. |
| E08 | Cosmetic profile | Reject claimed differential success where only labels/formatting change. |
| E09 | Scholarly duplicated reports or revision | Correct unit linkage/counting while retaining useful changed content. |
| E10 | Scholarly insufficient access / threshold transfer | No unseen method claim, universal threshold or fabricated status clearance. |
| E11 | Repository licence/popularity/readiness | Separate licence scope, maintenance signals and actual executed validation. |
| E12 | Repository static failure observation | Identify exact code and a justified test, without declaring that runtime test passed or failed. |
| E13 | Scoped correction / deactivation | Preserve unaffected evidence and historical profile identity; re-review dependent findings. |
| E14 | Unsafe package path or load-time side effect | Reject traversal/escaping dependency and automatic execution. |
| E15 | Evaluator mutation or stale verdict | Fixed input bytes and exact reviewed revisions; no repair hidden inside scoring. |
| E16 | Cross-domain or specialist overreach | No downstream deployment, legal/clinical advice, personal investigation or fabricated expert approval. |

The four actual outputs are reviewed against the prespecified protocol. The comparison records observable consequences, including where core already supplied the same caution. Demonstrated specialisation is not measured causal superiority: the same assistant wrote and reviewed both conditions in a shared context. Fresh isolated invocations and stronger independent review remain necessary before a claim of reliable improvement. No numerical research-quality score or speed/cost claim is produced.

The [verification script](2026-09-10-stage-11-verification.py) checks design inventories, profile effects, prompt completeness, source and local-reference closure, policy counterexamples, result evidence and integrity of the four outputs. Synthetic tests exercise the design rules only. Its [results file](2026-09-10-stage-11-verification.json) is generated by actual execution, not written as an assumed PASS. The comparison review is substantive but not independent human validation.

Executed on 10 September 2026: the verifier returned exit status 0 with 21 passing checks, 18 passing synthetic design-policy cases and 15 detected negative-control mutations. It preserved every submitted file. These counts are from this continuation, not from the removed checkpoint. The final run was repeated after recording the observed results so the result manifest identifies the final content.

## Conformance and exit

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 | Execution 3/9; sections 5/17/29 | Authority, accepted predecessor and source register | Read original section and relevant accepted contracts; inspect tip/parent and removal. | PASS |
| R02 | Section 17 qualification | Section 1 and both profiles | Check eight dimensions and five qualification conditions; core invariants retained. | PASS |
| R03 | Section 17 candidate families | Seven-row catalogue analysis | Trace source basis, overlap, selection and reopening conditions for every candidate. | PASS |
| R04 | Section 17 precedence | Activation/precedence rules and policy cases | Challenge no-selection, lock, explicit restriction, incompatibility and multi-selection. | PASS |
| R05 | Section 17 packaging | Section 2 manifest/bundle contract | Check local dependencies, path rules, optional tools and separate design/installation status. | PASS |
| R06 | Section 17 authoring | A01–A12; Stage 10 create-pack | Match every source step to output, authority and completion condition. | PASS |
| R07 | Section 17 showcase | Two showcases and four exact condition prompts | Inspect complete scope, sources, permission, output and evaluation details. | PASS |
| R08 | Section 17 comparison/Exit | Four source-backed outputs and criterion review | Compare actual operations and consequences without weakening baseline; expose shared-session bias. | PASS |
| R09 | Section 17 evaluation | E01–E16, verifier and executed results | Run documented checks and adversarial mutations; keep installed tests unclaimed. | PASS |
| R10 | Section 17 Outputs; execution 5–8 | Six output sections, comparisons, sources and verification | Re-read original contract; inspect stage-only delta; remote publication verified separately. | PASS |

Publication is a separate post-commit gate: R10 above records content conformance only. Stage completion is not declared until the branch, commit, stage files and preservation of accepted predecessors have been read back and matched. The publication receipt records those observations after they occur.

Content exit: a valid pack is defined, the catalogue is narrowed, authoring/showcase/evaluation contracts are complete, and both selected profiles have actual bounded source-backed demonstrations of meaningful effects without a claimed runtime or installation result. No current design question requires a requester decision. Stage 12 consumes these selected profiles and their limitations when designing the five-by-three progression. No deferred family is advertised as implemented, and no release, PR readiness or maturity promotion follows from this stage.
