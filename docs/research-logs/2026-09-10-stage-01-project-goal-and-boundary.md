# Stage 1: Project Goal and Boundary

Date: 10 September 2026  
Branch: `feat/bootstrap`  
Stage content acceptance: PASS  
Maturity: bootstrap workspace; no implementation or installation claim

## Authority and inspected inputs

The governing contract is [Deep Research bootstrap, section 7](2026-09-07-deep-research-skills-new-project-bootstrap-process.md#7-stage-1--define-project-goal-and-boundary), constrained by sections 1, 2, 5 and 29. It was read from `main`, not from a previous bootstrap branch. Its baseline commit is `80b209968b366662c01a8ded5ecb6c30bb6beb0b`; its Git blob is `8ff62c92bada2861ece3684a9e73a83da75d9d94`.

The following governing family sources were accessed through the GitHub connector on 10 September 2026. The family `main` revision inspected was `d109b1f5f085f9493711803c0c801b9812427d57`. References F1-F8 below identify repository-relative paths at that revision; their links are revision-pinned.

| ID | Source | Applicable evidence |
|---|---|---|
| F1 | [Bootstrap README](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/bootstrap/README.md) | Minimal workspace, domain-first design, durable research, no premature scaffold. |
| F2 | [New-project process](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/bootstrap/new-project-process.md) | Governing rules and Stages 0-1: workspace, short charter, outcomes, adjacent ownership, human commitment and quality. |
| F3 | [Domain-research process](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/bootstrap/domain-research-process.md) | Define the discipline before provider capabilities; distinguish reusable and provider-specific knowledge. |
| F4 | [Shared-abstraction process](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/bootstrap/shared-abstraction-process.md) | Independent implementation evidence is required before promotion. |
| F5 | [Family system](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/specs/01-production-skills-family-system.md) | Sections 4-5: central/domain/consumer/Pactwright ownership and production principles. |
| F6 | [Project contract](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/specs/02-production-skills-project-contract.md) | Sections 2, 4, 10-15: durable workspace, standalone use, project knowledge, execution and integration boundaries. |
| F7 | [Evaluation and Extension Packs](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/specs/03-production-skills-evaluation-and-extension-packs.md) | Sections 3, 9-16 and 20: quality is not structural correctness; specialist packs require behavioural justification; no universal score. |
| F8 | [Cross-domain integration](https://github.com/sb-dev/production-skills/blob/d109b1f5f085f9493711803c0c801b9812427d57/docs/specs/04-cross-domain-orchestration-and-integration.md) | Sections 2-5, 8-14: consumers own composition and project knowledge; producers retain domain responsibility. |

The complete current-stage section and applicable global principles were inspected. The applicable portions of the generic bootstrap recipes were inspected; this is not a claim to have researched professional methods or later-stage provider capabilities.

### Baseline and prerequisite verification

The remote `main` tree was inspected recursively. Its only files were `README.md`, `docs/research-logs/README.md` and the governing bootstrap specification. Both READMEs were read: the root states bootstrap-workspace status, and the research-log README identifies durable staged research rather than implementation. This satisfies the already-existing Stage 0 workspace requirement in F2.

The branch listing showed no `feat/bootstrap`. It was created directly from the baseline commit above. The other existing stage branches were neither read nor reused. No earlier stage output is required: this is a clean Stage 1 execution. GitHub branch creation succeeded, establishing repository write access. Direct container cloning failed because the container could not resolve `github.com`; document validation therefore uses local output files and connector-inspected Git trees, not a claimed local clone.

### Evidence character and method

Source-derived requirements are identified by bootstrap section or F-number. The charter and boundary decisions below are generated design synthesis from those requirements, not empirical findings about practitioners. No external professional-practice research was required or claimed for this stage; that investigation belongs to Stage 2. No mature family implementation was compared.

Method: extract each Stage 1 question; examine the governing ownership constraints; compare three boundary alternatives; assess all eight required research classes; define the six outputs; challenge the boundary with concrete cases; re-read section 7; audit each requirement and the proposed repository delta.

## Stage-specific acceptance checklist

| ID | Requirement before completion | Specification reference |
|---|---|---|
| R01 | Verify the clean workspace and authorised branch; do not reuse previous attempts. | F2 Stage 0; execution instructions sections 1-3. |
| R02 | Define the discipline, owned outcomes and reusable value before proposing skills. | Bootstrap section 7 Purpose and Resolve; F5 sections 4-5. |
| R03 | Identify intended users. | Bootstrap section 7 Resolve. |
| R04 | Investigate every listed research class and separate general from specialist responsibility. | Bootstrap section 7, eight-class list and specialist-method warning. |
| R05 | Define what constitutes a research deliverable. | Bootstrap section 7 Resolve; section 1 boundary. |
| R06 | Define sufficient evidence without inventing a universal source count or opaque score. | Bootstrap section 7 Resolve; section 5 source quality, independence and uncertainty. |
| R07 | Identify decisions that remain human-owned. | Bootstrap section 7 Resolve; F5 deliberate commitment. |
| R08 | Separate reusable expertise from consuming-project knowledge. | Bootstrap section 7 Resolve; F5 section 4; F8 section 14. |
| R09 | Identify downstream Production Skills and handoff ownership. | Bootstrap section 7 Resolve and boundary hypothesis; F8 sections 4-5. |
| R10 | Define explicit non-goals. | Bootstrap section 7 Resolve and Outputs. |
| R11 | Produce all six required outputs. | Bootstrap section 7 Outputs. |
| R12 | Preserve evidence/judgement, uncertainty, temporal context, bounded effort and verified work. | Bootstrap section 5; applicable design implications of section 29. |
| R13 | Produce a defensible boundary without a proposed skill count. | Bootstrap section 7 Exit. |
| R14 | Persist decisions, alternatives, source limitations, verification and next-stage inputs. | F1 workspace principle; execution instructions sections 3, 5-7. |
| R15 | Add no premature production surfaces or unsupported maturity claims. | F6 section 4; bootstrap sections 6 and 29. |

Applicability details: the stage requires nine resolved questions, consideration of all eight named classes, and six output responsibilities. It prescribes no separate filenames for those six outputs; sections 1-6 below implement them in one complete research log. No example-generation prompt, candidate-pool count, level distribution, installed skill, canonical specification, benchmark execution or measured provider comparison belongs to Stage 1. Those are NOT APPLICABLE here under the later-stage assignments in bootstrap sections 13-26. The boundary alternatives and eight-class analysis below are the current stage's required investigation, not substitutes for later research.

## 1. Project charter

### Mission and owned outcome

Deep Research Skills owns reusable evidence-led research production: turning an authorised research need into evidence, supported synthesis, explicit uncertainty and a traceable handoff that another person or production discipline can inspect and use. It owns the integrity of that research, not the downstream commitment made from it. This adopts the governing boundary hypothesis rather than expanding the repository into a general decision-making platform. [Bootstrap sections 1 and 7; F5 section 4; F8 sections 2-5.]

The repository's reusable value is the practice for framing questions, selecting evidence, checking sources, distinguishing support from interpretation, examining contradictions, synthesising proportionately and repairing research when evidence changes. The particular company's facts, a project's approved strategy, its stakeholder preferences and its continuing evidence archive remain with the consuming project. [Bootstrap sections 1 and 5; F5 section 4.4.]

Owned outcomes include bounded verified answers; comparative and landscape findings; evidence-led case analyses; focused syntheses; temporally qualified trend findings; source-verification assessments; and updates identifying which conclusions changed and which remain supported. These are research outcome classes, not installable skill names or a fixed workflow.

### What constitutes a research deliverable

A deliverable is an inspectable answer to the agreed research need, not simply prose with a bibliography. At the appropriate scale it provides: the question and scope; the evidence actually accessed; locators for material support; analysis distinguishing source statements from inference; relevant contrary evidence and limitations; temporal context; and a clear answer or an explicit explanation of what remains unknown. It must say how its findings are relevant to the requested downstream use without taking over that use. [Bootstrap sections 1, 5 and 7.]

A brief verified answer can satisfy this contract without a large report. A comparative decision-support report may require a fuller evidence record. The field schema, file layout and command/state mechanics are deliberately not chosen here; Stages 3 and 5 own those decisions.

### Scope investigation: all eight required classes

The decision below concerns reusable core responsibility, not a promise that every specialist methodology will be implemented in core. Stage 2 must test the method assumptions before a workflow is selected.

| ID | Research class | Core responsibility and useful outcome | Specialist or consuming-domain boundary | Why retain this class |
|---|---|---|---|---|
| C1 | Fact finding | Resolve a bounded factual question using direct support, its applicable context and a stated uncertainty where unresolved. | Producing a fact does not authorise the action a consumer takes from it; sensitive or high-stakes interpretation needs the appropriate owner. | The smallest useful research outcome, and a necessary building block for broader work. |
| C2 | Landscape research | Map relevant actors, approaches or evidence clusters against a defined scope, with omissions and coverage limits visible. | Comprehensive patent, clinical or other specialist landscapes may require specialist methods and access; product positioning belongs to the consumer. | Answers what exists and what remains uncovered without pretending a ranked web list is complete. |
| C3 | Comparative research | Compare alternatives against explicit criteria, preserve differences in evidence strength and identify unresolved trade-offs. | The consumer sets value judgements, acceptable risk and the final selection; procurement or implementation is not research. | Provides structured evidence for choices while keeping the choice with its owner. |
| C4 | Case-study research | Reconstruct bounded cases with source context, alternative explanations and limits on transfer to other settings. | Do not infer causality or general validity from a compelling narrative alone; specialist causal methods need separate justification. | Makes contextual evidence reusable without turning examples into universal rules. |
| C5 | Evidence synthesis | Integrate what the available evidence supports across sources, retaining provenance, conflicting results and applicability limits. | A formal systematic review, meta-analysis or discipline-specific appraisal cannot be claimed merely by using a structured report. | Cross-source integration is central to research, while specialist evidential standards must remain explicit. |
| C6 | Trend research | Separate observations over time from interpretations and forecasts; state time windows and evidence gaps. | Forecasting commitments, trading, policy or commercial bets belong to the consumer; specialised forecasting methods are not automatically core. | Temporal change is a research responsibility, but predictive certainty is not a by-product of recency. |
| C7 | Source verification | Check what a source actually supports, its origin and context, temporal applicability, and apparent dependence on other sources. | Verification of difficult media, identities or authenticity can require specialist tools and review; lack of access cannot be reported as a verified source. | Citation and independence checks protect every other outcome class. |
| C8 | Research updates / refreshes | Identify changed evidence, reconsider affected claims and preserve supported, unaffected findings. | Continuous surveillance, scheduled execution and the consumer's durable knowledge infrastructure are not core research ownership. | Research becomes useful over time without requiring a persistent research platform. |

Decision: retain all eight classes as general research outcome responsibilities. Do not put all methods used within them into core. A reusable specialist context may later justify an Extension Pack only when it changes research behaviour and can be demonstrated and evaluated; Stage 11 owns that selection. A project-specific brief is not a pack. [Bootstrap section 7; F7 sections 9-16.]

### Boundary alternatives considered

| Alternative | Advantage | Failure against the contract | Decision |
|---|---|---|---|
| Bounded fact-checking only | Very small scope and clear atomic answers. | Leaves landscape, comparative, synthesis, trend and research-programme needs without an owner; does not satisfy section 1's research-production purpose. | Reject as the whole project; retain bounded answering within scope. |
| Universal autonomous analyst and decision platform | Could collect evidence and act on it through one interface. | Absorbs consumer judgement, governance, persistent project knowledge and execution infrastructure; conflicts with F5 and F8 ownership. | Reject. |
| Evidence-led research production with explicit downstream handoffs | Covers the eight classes through reusable responsibilities while preserving specialist and consumer boundaries. | Requires later domain research to validate methods and proportionate effort; it cannot claim completeness from this charter alone. | Adopt as the Stage 1 boundary. |

## 2. Boundary map

| Responsibility | Deep Research owns | Adjacent owner retains | Handoff / change authority |
|---|---|---|---|
| Research request | Clarifying the evidence need, exposing ambiguity and testing whether it can be answered. | The requester owns the purpose, priorities, authorised sources and consequences. | Material changes to the request return to its owner; routine research choices may proceed within the agreed bounds. |
| Evidence and synthesis | Research-specific provenance, support, contradiction analysis, uncertainty and research QA. | A source remains responsible for its assertions; a consumer remains responsible for adopting conclusions in its domain. | Research may qualify, correct or retract its own claim with a visible reason; it cannot silently rewrite an approved consumer decision. |
| Tools and providers | Choosing and evaluating the research operation needed. | Execution mechanisms perform search, retrieval, parsing, calculation or other authorised operations. | A provider's fluent report is evidence to audit, not a transfer of research accountability. Tool selection is designed in Stages 7-8. |
| Research-specific computation | Analysing acquired data and explaining methodological and data limitations for the research question. | Software Engineering owns production code, deployment and software architecture; specialist reviewers own methods requiring their expertise. | A research calculation is not production-ready software or proof that its modelling assumptions are valid. |
| Downstream domain production | Providing source evidence, research synthesis, relevant constraints and unresolved issues. | Each consuming domain owns interpretation within its production responsibility and the resulting artefact or action. | Consumer feedback can identify a research gap; filling it must not silently expand authority or alter approved work. |
| Project knowledge | Reusable research technique and generalised, validated learning. | The consuming project owns its briefs, proprietary sources, accumulated findings, selected packs, approved decisions and retention arrangements. | No automatic copying of private/project-specific evidence into public skill references. |
| Family and integration | Domain research semantics and quality. | The central family owns family contracts and registry; an optional orchestrator/Pactwright owns lifecycle and delivery governance. | No domain workflow transfer to Pactwright and no central universal evidence store. |
| Public or consequential action | Identifying limitations and preparing research for review. | Authorised humans own publication, spending, external contact, disclosures and consequential decisions. | Research completion alone never implies authority to perform those actions. |

### Downstream Production Skills use-case handoffs

These are intended handoff relationships derived from the family boundary, not claims that integrations or the receiving repositories are implemented.

| Consumer discipline | Research contribution | What does not transfer to Deep Research |
|---|---|---|
| Software Engineering | Technical evidence, documented constraints, comparative findings and evidence gaps. | Architecture selection, production implementation, performance commitments and shipping. |
| UI/UX Design | Existing human-science or interaction evidence and its applicability limits. | Product design, actual user recruitment/studies, inference about unobserved users, and design validation in the consuming context. |
| Game Development and world/environment production | Sourced real-world mechanisms, uncertainties and competing interpretations. | Game mechanics, simulation truth claims, world design and implementation; a simulation result is not automatically real-world evidence. |
| Narrative, Video, Music and other creative production | Traceable reference research, context and relevant uncertainty. | Creative direction, story, shot, score or asset production; research does not grant rights clearance. |
| Business Building and Advertising production | Market, competitor, customer-problem and claim-support evidence within the brief. | Business strategy, offers, commercial commitments, campaign production and approval of advertising claims. |
| Specialist legal, medical, financial or policy consumers | Clearly bounded source research and questions requiring qualified interpretation. | Professional advice, privileged or regulated judgement and consequential action without the appropriate review and authority. |

For each handoff, the producer owns the integrity of research claims; the consumer owns fitness for its application and integration evaluation. A downstream finding that exposes a research defect returns to the smallest affected research claim or source relationship, not an automatic rewrite of all research. [Bootstrap section 5; F5 section 5.5; F8 sections 4 and 11.]

## 3. Intended user and use-case map

These are product-design user categories, not empirically validated personas.

| Intended user | Need / entry condition | Useful research outcome | Authority retained |
|---|---|---|---|
| Individual researcher or analyst | A bounded question, comparison or evidence gap. | An inspectable answer or synthesis with support and limitations. | Purpose, meaningful scope changes and adoption of the findings. |
| Domain practitioner consuming research | Evidence needed before design, engineering, creative or commercial production. | Domain-relevant findings with applicability conditions and traceable support. | Domain judgement and final production choices. |
| Agent operating under an approved brief | Reusable research practice rather than another generic search prompt. | Evidence-led execution within source, scope and effort constraints. | No autonomous acquisition of additional human authority; material conflicts escalate. |
| Research reviewer / evaluator | A way to check support, omissions, contradictions and misleading certainty. | Reviewable evidence and claims, with a bounded correction target. | Acceptance of a consequential deliverable where review is required. |
| Consuming-project team / orchestrator | Research that can be composed with other specialist work. | A stable, understandable handoff that does not depend on this chat. | Project knowledge, lifecycle, delivery acceptance and integration. |

A user may occupy several roles. This map does not invent a mandatory team, agent swarm, approval committee or dedicated runtime. Standalone use remains a requirement. [F5 sections 3 and 5.7; F8 sections 2-3.]

## 4. Quality definition and sufficient evidence

Quality means an answer that addresses the actual research need, is supported to the claimed level, can be checked, represents material disagreement and limits, and is useful without becoming more certain than its sources. Structural completeness, number of sources and length of the report cannot by themselves demonstrate this. [Bootstrap section 5; F7 sections 3 and 20.]

| Dimension | Stage 1 quality obligation | Inadequate condition |
|---|---|---|
| Relevance and coverage | Address the agreed question and material subquestions; expose gaps and exclusions. | A broad report that bypasses the requested decision or one inconvenient subquestion. |
| Directness and applicability | Prefer the source closest to the relevant fact, with context specific to the claim. | A primary source treated as automatically sufficient for every inference drawn from it. |
| Source quality | Explain applicable authority, method, transparency, recency, incentives and limitations separately. | One opaque quality score or prestige used as a substitute for examining evidence. |
| Independence | Identify repeated reporting or shared underlying evidence before claiming corroboration. | Several articles copying one source described as several independent confirmations. |
| Traceability and support | Provide an inspectable path from each material claim to what actually supports it. | A citation that exists but supports only a neighbouring statement. |
| Contradictions and alternatives | Preserve significant contrary evidence and explain or label unresolved disagreement. | Selecting only evidence that makes the desired conclusion easier. |
| Uncertainty and judgement | Distinguish observation, source assertion, inference, forecast and recommendation; explain uncertainty. | Confident prose that hides thin support or treats a generated interpretation as observed evidence. |
| Temporal validity | Identify the relevant event, publication/effective and as-of context where the claim can change. | Recently retrieved but outdated evidence presented as current. |
| Proportionality and auditability | Use a bounded effort appropriate to the need and preserve enough search/selection evidence to review coverage. | Unbounded search, unnecessary exhaustive work, or an unsupported claim of exhaustiveness. |
| Preservation and repair | Reconsider affected claims when evidence changes and preserve valid unaffected work. | Rewriting a whole report without diagnosing the defective evidence or inference. |

### Sufficiency decision

Sufficient evidence is relative to the claim, purpose, materiality and authorised research standard, not a fixed citation count. The researcher must ask whether the available support is direct enough, applicable, current enough and adequately independent for the intended claim; whether important alternatives or contradictions have been examined; and whether the remaining uncertainty is compatible with the intended use. [Bootstrap section 5 and section 7 Resolve.]

For a narrow fact about an authoritative document, one directly inspected passage may answer exactly that fact. It does not establish the real-world truth of every claim made by the document. A comparative or contested claim may require several genuinely distinct lines of evidence; repeated secondary coverage does not supply that independence. A claim of exhaustive review requires a justified method and documented coverage, not simply many sources. These are project quality rules to be tested and specialised through Stage 2, not measured empirical thresholds.

When the available evidence is insufficient, narrow or qualify the claim, identify the unresolved need, or report that it cannot currently be established. Reaching a budget or access limit is a legitimate stopping condition, but not evidence that the answer is now supported. An inaccessible full source may be recorded as inaccessible; accessible summaries must be attributed as summaries, not presented as independently inspected originals.

Decisions about numerical scoring, detailed evidence fields, stopping mechanisms, specialist appraisal and evaluation tooling remain with Stages 2-6 and 13. This stage establishes the obligations those designs must satisfy.

## 5. Human decision points

The requester or an explicitly delegated owner retains the following decisions. This is an authority map, not a requirement to interrupt routine authorised research for every source.

| Trigger | Decision owner and decision | Research may do without taking over that decision |
|---|---|---|
| The research purpose, value criteria or material scope is ambiguous or conflicts. | Requester resolves the purpose or changed scope. | Explain the ambiguity and its effect; do not choose a consequential interpretation on the owner's behalf. |
| Work would exceed an agreed budget, require paid access or add material expense. | Budget owner authorises the additional commitment. | Report the gap and compare already-authorised alternatives. |
| A new private connector, restricted source, sensitive data disclosure or external processing is proposed. | Data/source owner authorises access and disclosure under the applicable constraints. | Use already-authorised material; identify the missing evidence without bypassing access restrictions. |
| Contacting people, running a study or collecting new human-participant evidence is proposed. | Research sponsor and appropriate specialist owner decide the method, permissions and oversight. | Analyse existing authorised evidence and articulate unanswered questions. |
| A finding needs specialist interpretation or could drive a high-stakes action. | Appropriate domain specialist and decision owner review applicability and consequences. | Supply sources, limitations, contrary evidence and precise questions for review. |
| New evidence appears to undermine an approved or locked project decision. | The owner of that decision chooses whether to reopen it. | Flag the conflict and correct the research record; do not silently change the consuming project's approved state. |
| Publication, external disclosure, procurement, implementation or another commitment is proposed. | Authorised publisher or consuming-domain owner approves the action. | Produce the research handoff and clearly separate findings from possible recommendations. |
| Required evidence cannot be obtained or contradictions leave the proposed use unsupported. | Requester decides whether to change the question, accept a limited deliverable or authorise more work. | Report the limitation accurately rather than fabricating sufficiency. |

Within an unambiguous authorised brief, ordinary source discovery, triage, cross-checking, analysis, citation correction and proportionate follow-up remain research operations. A process should not require extra human approval merely because a later stage exists. [Bootstrap section 5; F5 sections 5.2-5.5.]

## 6. Non-goals

| ID | Explicit non-goal | Boundary reason |
|---|---|---|
| N1 | Owning product strategy, design, narrative, code, campaigns or final business decisions. | Those are the consuming domain's production responsibilities. |
| N2 | Presenting source research as professional advice, specialist certification or automatic rights clearance. | Evidence does not transfer professional judgement or authorisation. |
| N3 | Claiming all specialist research methods are universal core behaviour. | Methods require domain research and, where justified, explicit specialisation. |
| N4 | Acting as an autonomous purchasing, publishing, disclosure or decision-making agent. | Research authority is not authority for consequential external actions. |
| N5 | Owning a consuming project's knowledge base, private evidence archive, roadmap or lifecycle. | Those remain project-specific responsibilities. |
| N6 | Rebuilding search engines, crawlers, provider agents or execution tools by default. | The repository owns research production intelligence above execution. |
| N7 | Requiring a universal evidence database, knowledge graph, workflow runtime, provider registry or agent swarm. | Traceability and composition must not imply unnecessary infrastructure. |
| N8 | Ranking truth through source popularity, citation volume or one universal numerical quality score. | Research quality is multidimensional and claim-specific. |
| N9 | Treating a polished report, a large bibliography or synthetic fixtures as proof of real research capability. | Evidence and measured capability must remain distinguishable from design and generated material. |
| N10 | Requiring Pactwright or moving research workflow semantics into it. | Standalone use and domain ownership are family requirements. |
| N11 | Promoting shared abstractions from this charter alone. | Independent implementation evidence from multiple domains is required. |

## Boundary challenge review

These are reasoning checks of the design, not executed agent tasks, experiments or benchmarks.

| Case | Expected ownership result | Review result |
|---|---|---|
| Find the licence stated in a repository, then decide whether a commercial product may use all its assets. | Research can establish the stated source facts; legal applicability and rights clearance require the appropriate owner. | PASS: the source fact and downstream interpretation are separated. |
| Compare technical options, then deploy the winner. | Research compares evidence under explicit criteria; the consumer chooses and Software Engineering implements. | PASS: no deployment authority is inherited from the report. |
| Review existing interaction research, then claim that this project's users prefer a design. | Research can assess available studies; it cannot invent project-specific empirical user findings. | PASS: UI/UX and actual user-research ownership are retained. |
| Discover three articles repeating one source. | Retain the underlying-source relationship; do not treat the articles as independent support. | PASS: the quality definition forbids false corroboration. |
| Find a recent source that challenges one previously supported claim. | Reconsider the affected claim, preserve valid unrelated findings and flag any conflict with approved consumer decisions. | PASS: research repair does not silently reopen project approval. |
| Research a real-world mechanism for a game, then observe an emergent behaviour in the game. | Source research and simulation findings remain distinct; transfer back to the real world needs new evidence and domain scrutiny. | PASS: game production and empirical validity are not conflated. |

## Verification and conformance

The original section 7 was re-read after drafting. Manual verification below checks substantive coverage against that source, not merely this document's own headings. Deterministic checks in the [companion verification record](2026-09-10-stage-01-verification.json) count the output sections and research classes, validate local documentation targets against the inspected baseline, and restrict the repository delta to research logs. Those checks do not claim to evaluate professional research quality.

On 10 September 2026, the documentation validator was executed and all seven checks passed. Two negative controls were also executed: replacing the required C8 class caused exit status 1, and adding an unjustified `skills/unjustified.txt` caused exit status 1. Both mutations were removed, the original content restored, and the final validator run passed. These are document-validator checks, not installed-skill or research-behaviour benchmarks.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 Clean baseline and authorised branch | F2 Stage 0; execution instructions sections 1-3 | Baseline evidence above; remote branch/tree reads | Inspected all three baseline files and creation from exact main SHA; no previous branch content used. | PASS |
| R02 Discipline and owned outcomes | Bootstrap section 7 Purpose/Resolve | Section 1 charter and boundary alternatives | Checked ownership is research production, not provider behaviour or a skill list. | PASS |
| R03 Intended users | Bootstrap section 7 Resolve | Section 3 | Checked users, needs, outcomes and retained authority; no invented empirical personas. | PASS |
| R04 All eight research classes | Bootstrap section 7 class list | C1-C8 | Matched each original class to a disposition, specialist boundary and rationale. | PASS |
| R05 Research deliverable | Bootstrap section 7 Resolve | Section 1 deliverable definition | Checked question, evidence, support, synthesis, contrary evidence, limits, temporal context and downstream relevance. | PASS |
| R06 Sufficient evidence | Bootstrap sections 5 and 7 | Section 4 | Checked claim-relative sufficiency, independence, access limitations, uncertainty and no fixed source quota. | PASS |
| R07 Human decisions | Bootstrap section 7 Resolve | Section 5 | Checked purpose, scope, cost, access, human research, specialist review, approval changes and external actions. | PASS |
| R08 Reusable/project boundary | Bootstrap section 7 Resolve; F5 section 4.4 | Sections 1-2; N5 | Checked project facts and private evidence remain consumer-owned; no automatic public reuse. | PASS |
| R09 Downstream handoffs | Bootstrap section 7 boundary hypothesis; F8 sections 4-5 | Section 2 | Checked named consuming disciplines, research contribution and retained production authority. | PASS |
| R10 Non-goals | Bootstrap section 7 Outputs | Section 6 | Reviewed all N1-N11 against the adopted boundary and family anti-goals. | PASS |
| R11 Six complete output responsibilities | Bootstrap section 7 Outputs | Sections 1-6 | Matched charter, boundary map, user/use-case map, quality, human decisions and non-goals to source list. | PASS |
| R12 Governing research principles | Bootstrap sections 5 and 29 | Sections 1, 4-6 | Checked primary support, independence, contradictions, judgement, time, effort and preservation remain explicit. | PASS |
| R13 Defensible boundary; no proposed skill count | Bootstrap section 7 Exit | Alternatives and challenge review | Compared three scope alternatives and six boundary cases; no skills selected or counted. | PASS |
| R14 Durable research and verification | F1; execution instructions sections 3, 5-7 | This log; progress and verification records | Checked source revisions, evidence character, analysis, decisions, limitations and next-stage inputs. | PASS |
| R15 No premature scaffold or maturity claim | F6 section 4; bootstrap section 6 | Research-log-only changes; unchanged root README | Inspected proposed paths and claims; no production surface, installation result or maturity promotion added. | PASS |

### Exit assessment and deferred work

All mandatory Stage 1 content requirements pass. The selected boundary is evidence-led research production with consumer-owned decisions and specialist methods not automatically included in core. This is a completed boundary design, not a claim that the research capability has been implemented or professionally validated.

No unresolved Stage 1 question requires user input. Stage 2 must consume this charter and quality baseline, research professional practice, and test the specialist/core assumptions without treating this design synthesis as empirical evidence. Information schemas, source/acquisition architecture, workflow, stopping mechanics, providers, skills, packs, examples, benchmarks and implementation remain assigned to their original later stages; none is represented as already complete here.

Publication control: progression is permitted only after the commit containing these outputs has been read back from `feat/bootstrap` and its intended file blobs verified. The Git commit itself identifies the published revision; no self-referential commit SHA is invented inside this file.
