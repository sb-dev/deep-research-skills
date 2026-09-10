# Stage 5: Artifact Contracts

Authority: original bootstrap section 11. These contracts retain all eleven candidate information responsibilities; the [workflow log](2026-09-10-stage-05-workflow-and-artifacts.md) defines compact/expanded placement and the state, handoff and repair rules. Each contract has the eight concerns required by the source, not merely an intended filename.

## Candidate disposition and physical placement

| Contract | Candidate surface | Decision and justification |
|---|---|---|
| A01 | `brief.md` | Retain as a brief section or file; owns approved scope rather than a duplicate plan. |
| A02 | `plan.md` | Retain as plan/search sections or file; separates intention from performed discovery. |
| A03 | `sources/source-register.*` | Retain source register; source identity/access needs independent repair from claims. |
| A04 | `evidence/` | Retain identifiable evidence records; a section/table suffices before a directory is useful. |
| A05 | `claim-source-matrix.*` | Retain one authoritative claim/support record; render extra matrices only as views. |
| A06 | `contradictions.md` | Retain conflict/alternative records; merge physically into analysis.md when separate updates do not justify a file. |
| A07 | `gaps.md` | Retain gaps with actual outcomes; share analysis.md without losing distinct gap authority. |
| A08 | `synthesis.md` | Retain synthesis and separate recommendation semantics; share analysis.md if practical. |
| A09 | `report.md` | Retain actual report/revision; it can be the report section of a compact note. |
| A10 | `provenance.*` | Retain provenance at the owning record by default; separate file only for material transformations that warrant it. |
| A11 | `evaluation/` | Retain actual review and decision receipts; use a section or review.md instead of an empty evaluation directory. |

No empty candidate surface is created just to mirror the diagram. A record can explicitly state that a concern is not applicable and why, such as no material transformation, but must not disguise unperformed work as a completed check. Compact records need no global registry. The consuming project owns these run-specific artifacts; the bootstrap contains their reusable contracts only.

A source, evidence item, claim, synthesis and recommendation remain distinct even when placed in one document. One field has one authority. Cross-references and views never acquire permission to alter approved facts, source text or consumer decisions.

## A01: Research brief

| Concern | Contract |
|---|---|
| Purpose | The authorised evidence need and its boundaries; prevent a topic or preferred conclusion replacing the actual question. |
| Creator | Requester supplies intent; researcher records and clarifies it without taking over consequential scope decisions. |
| Consumer | Planner, acquisition executor, analyst, reviewer and downstream owner use the same brief revision. |
| Authoritative fields | Stage 3 BR01–BR10: objective, use, scope/exclusions, questions, freshness, source restrictions, quality, effort constraints and output. Also identify owner and material decision revisions. |
| Update behaviour | Correct clerical errors visibly when meaningful; reopen material scope, criteria or authority with the owner. Link the revision to affected plan and findings. |
| Approval / review behaviour | Explicit user instructions can authorise ordinary work. A material ambiguity or additional commitment blocks until the appropriate owner resolves it. |
| Retention | Retain the authorised brief and relevant change decisions with the delivered evidence package under the consuming project’s policy; protect sensitive intent. |
| Smallest repair scope | One question or decision when isolated; revalidate all dependent work if purpose or scope changes. Preserve still-applicable evidence rather than obsolete conclusions. |

## A02: Research plan and search record

| Concern | Contract |
|---|---|
| Purpose | Declare method and source strategy; distinguish intended search/selection from operations actually performed and their coverage. |
| Creator | Researcher/planner creates the plan; each executor records the material operation it actually performed. |
| Consumer | Acquisition, analysis and review use it to assess eligibility, coverage, method fit and legitimate continuation. |
| Authoritative fields | Brief revision, method, question-to-source/path map, eligibility, intended analysis, required review, authorised bounds; actual queries, filters, time, continuation/completeness and deviations. Selection identities refer to A03. |
| Update behaviour | Append or revise actual discovery records without relabelling them as prior intentions. Material method/coverage departures carry rationale and needed authority. |
| Approval / review behaviour | Researcher checks method fit before acquisition; a reviewer checks whether actual search supports the coverage claimed. Specialist methods retain their required review. |
| Retention | Keep meaningful search/selection evidence sufficient to audit the declared method; do not retain every irrelevant click or secret query parameter by default. |
| Smallest repair scope | One query, source-path assignment or criterion, followed by its affected selections and conclusions; a wrong method can require broader reconsideration. |

## A03: Source register

| Concern | Contract |
|---|---|
| Purpose | Identify candidate and inspected sources, source versions, eligibility and actual access; prevent a lead being treated as a read original. |
| Creator | Discoverer registers candidates; acquirer updates the actual representation/access; reviewer records source-appraisal observations. |
| Consumer | Extractor, analyst, reviewer and authorised consumer need resolvable original references and access/quality limits. |
| Authoritative fields | Stage 3 SR01–SR12 plus meaningful representation/version, access extent, restrictions and established/suspected origin relations. Inclusion is independent of access and support polarity. |
| Update behaviour | Preserve useful prior representations. Add a new version when material source content changes; do not silently repoint old evidence. Record selection changes and relation corrections with reasons. |
| Approval / review behaviour | Check source identity and access before extraction; appraise quality relative to the claim, not publisher prestige. Ambiguous origin links remain unresolved. |
| Retention | Retain permitted identity, locators, access context and appraisal; keep source bytes only when authorised and useful. Required deletion is recorded with its support/audit consequence. |
| Smallest repair scope | One source locator, version, selection or relation; recheck all dependent evidence/claims when identity, context, rights or currentness changes. |

## A04: Evidence records

| Concern | Contract |
|---|---|
| Purpose | Preserve the bounded observation/extraction and its context so claims can be checked without trusting synthesis alone. |
| Creator | Extractor produces the record from actually inspected material; a tool can assist but its output remains identified as such. |
| Consumer | Analyst, reviewer and later refresh/repair work follow it back to the exact source representation. |
| Authoritative fields | Stage 3 EI01–EI06; evidence ID, source/locator, exact relevant support, units/qualifiers, extraction character, question relevance, contrary links and extraction uncertainty. Record origin/unit at evidence level where one source contains several. |
| Update behaviour | Correct or supersede material extractions with the old basis identifiable. Add an A10 transformation link where relevant. Never rewrite the original source statement to match a conclusion. |
| Approval / review behaviour | Verify context and fidelity before material use; required specialist transcription, interpretation or data appraisal remains a separate qualified review obligation. |
| Retention | Retain the smallest permitted support/context and transformation references needed for audit and reuse; restrictions can require a private locator instead of public excerpts. |
| Smallest repair scope | One passage, table cell with its context, media interval, observation or transformation result; propagate changes only through materially dependent claims. |

## A05: Claim and support record / claim-source matrix

| Concern | Contract |
|---|---|
| Purpose | Own the actual proposition and its supporting/contrary evidence, making report support inspectable and repairable. |
| Creator | Analyst creates claims and premises; reviewer records support judgements for the relevant revision. |
| Consumer | Synthesiser, report author, reviewer and consumer trace findings and changed evidence through it. |
| Authoritative fields | Stage 3 CL01–CL07; claim/question IDs, materiality, supporting/contrary evidence, premises, assumption labels, inference, applicability, support status and confidence rationale. Review points to A11. A derived matrix is not a competing authority. |
| Update behaviour | Version material wording, support or premise changes. Mark affected prior checks needs-recheck. Preserve still-valid historical scope and identify replacement claims. |
| Approval / review behaviour | Semantic entailment and inferential validity require actual review; nonempty citations alone do not establish support. Qualified/contested claims retain those constraints in every rendering. |
| Retention | Retain issued claim/support revisions and permitted prior basis as needed for corrections; protect restricted source relationships from unauthorised audiences. |
| Smallest repair scope | One claim, evidence edge, premise or qualifier and its dependent synthesis/report/review; follow transitive dependencies where the inference changes. |

## A06: Contradictions and alternatives

| Concern | Contract |
|---|---|
| Purpose | Keep material disagreement and plausible alternative explanations visible rather than forcing consensus. |
| Creator | Analyst records apparent conflicts and alternatives; acquirers/reviewers can raise them as findings. |
| Consumer | Follow-up researcher, synthesiser, reviewer and decision owner inspect what remains unresolved. |
| Authoritative fields | Conflict/alternative ID, linked evidence/claims, shared context, distinction between genuine conflict and scope/time difference, checks performed, explanation, outcome and consequence. No-conflict-found is bounded by the inspected scope. |
| Update behaviour | Add new opposing evidence or revise a reconciliation with its supporting basis. A resolved discrepancy is not erased; distinguish historical resolution from renewed conflict. |
| Approval / review behaviour | Reviewer checks that reconciliation is supported, alternatives were not excluded for convenience, and unresolved disagreement survives synthesis. |
| Retention | Retain material competing interpretations and their disposition with the evidence package; do not copy prohibited source content to prove that it was considered. |
| Smallest repair scope | One conflict or explanatory premise, then the affected claims/confidence/synthesis. A restored null result can alter more than one comparison. |

## A07: Gaps and follow-up needs

| Concern | Contract |
|---|---|
| Purpose | Distinguish missing knowledge, source access, coverage, appraisal, permission and review so follow-up targets the responsible uncertainty. |
| Creator | Researcher or reviewer opens a gap; its action owner records actual attempts and outcomes. |
| Consumer | Planner, follow-up executor, reviewer and requester use the gap to choose bounded continuation, a decision or an honest limitation. |
| Authoritative fields | Gap ID, affected question/claim, type, material consequence, required evidence/decision, owner, proposed bounded action, actual attempts and state. State distinguishes open, attempted, resolved-with-evidence and accepted-limitation with an explicit decision. |
| Update behaviour | An attempt does not close a gap. Resolution links new evidence; accepting a limitation links the owner decision and changes permitted output scope, not the underlying fact. |
| Approval / review behaviour | Check whether the unresolved need blocks the required conclusion or mandatory prerequisite. A researcher cannot self-authorise a lower-quality substitute. |
| Retention | Keep material unresolved and resolved gaps plus their consequences; retain only permitted details of inaccessible/private sources. |
| Smallest repair scope | One gap or next action; update its linked claims and output-limit statements. Do not restart every search because one source is missing. |

## A08: Synthesis and recommendations

| Concern | Contract |
|---|---|
| Purpose | Integrate supported findings into a coherent answer while preserving alternatives, uncertainty and the boundary between evidence and action. |
| Creator | Analyst/synthesiser composes it; the consuming owner supplies values and decision criteria for any recommendation. |
| Consumer | Report author, reviewer and downstream specialist use it to understand the argument and its limits. |
| Authoritative fields | Question-to-claim mapping, reasoning, grouping/compatibility, assumptions, alternatives, gaps and overall applicability. New factual inferences become A05 claims. Recommendations identify values, supporting claims, conditions and decision owner separately. |
| Update behaviour | Revise only the arguments affected by changed evidence, scope or assumptions; preserve valid sections. New narrative wording cannot silently add unsupported factual bridges. |
| Approval / review behaviour | Review question coverage, logic, consistency and fitness for use, separately from citation existence. Required expert review cannot be replaced by stylistic editing. |
| Retention | Retain the argument behind issued conclusions and material revisions subject to project restrictions; unnecessary intermediate prose need not be preserved. |
| Smallest repair scope | One argument, evidence grouping or recommendation condition plus dependent output; unsuitable synthesis methods return to the plan. |

## A09: Report and delivery record

| Concern | Contract |
|---|---|
| Purpose | Provide the actual audience-facing answer and identifiable issued revision, with truthful limits and verified delivery state. |
| Creator | Author renders accepted analysis; the authorised publisher performs any external delivery. These may be the same person but authority is not inferred. |
| Consumer | Requester, consuming-domain owner, reviewers and authorised recipients read it without needing this chat. |
| Authoritative fields | Actual report text, question/scope, citations/claim references, material uncertainty/limitations, temporal basis, audience/access notes, report revision, issue/supersession/withdrawal and actual delivery result. Underlying support remains A05’s authority. |
| Update behaviour | Editing a material statement invalidates its previous wording review. Issue corrections as identifiable revisions; recover destination state before retrying an uncertain publication. |
| Approval / review behaviour | G03 checks the exact rendered report and disclosure authority; G04 distinguishes attempted from confirmed delivery. Review/acceptance does not authorise procurement, deployment or downstream strategy. |
| Retention | Retain the issued revision and correction history as permitted; distinguish an authorised public report from restricted supporting evidence. |
| Smallest repair scope | One citation/rendered sentence, revision metadata or receipt when support is unchanged; otherwise repair its owning evidence/claim before reissue. |

## A10: Material provenance and transformations

| Concern | Contract |
|---|---|
| Purpose | Explain how material evidence was obtained or transformed without requiring a universal event log or evidence database. |
| Creator | Acquirer/extractor/analyst records operations they actually performed; tools provide observed inputs/outputs where exposed. |
| Consumer | Reviewer and repair/refresh executor reconstruct the relevant extraction, translation, filtering or calculation. |
| Authoritative fields | Operation identity/type, source/input revisions, necessary parameters/selection, output/evidence reference, actor/tool role, actual date precision and limitations. Ordinary source identity stays in A03; secrets never enter this record. |
| Update behaviour | Append a new operation or correct the recorded operation with its reason. Changed inputs do not retrospectively change what an earlier operation actually used. |
| Approval / review behaviour | Check input/output lineage and material transformations against originals. A hash demonstrates byte identity only, not factual accuracy or rights. |
| Retention | Keep enough authorised information to repeat or audit the material transformation; omit unrelated telemetry, credentials and reusable sessions. |
| Smallest repair scope | One operation, parameter or output relation and its dependent evidence/claims. Reacquire only when missing provenance prevents the required check. |

## A11: Evaluation, decisions and review receipts

| Concern | Contract |
|---|---|
| Purpose | Record what was actually checked, against which revision and requirement, by what process, and what still needs repair or approval. |
| Creator | Applicable structural checker, substantive reviewer or authorised decision owner creates its own observed result; author claims are not substitutes. |
| Consumer | Author, researcher, publisher, recipient and next iteration use it to determine readiness and the affected repair scope. |
| Authoritative fields | Target/revision, check or decision scope, requirement, reviewer/role and competence boundary, actual result, defects, correction links, unresolved limitations and date. Tool receipt references resolve to the issued A09 revision. |
| Update behaviour | Add review of the changed scope; retain earlier results as historical. Never update a timestamp or mark a new revision checked solely because its predecessor passed. |
| Approval / review behaviour | Structural PASS and substantive support are separate. Applicable human/specialist or independent-review requirements must be fulfilled literally. Owner decisions identify exact authority and target. |
| Retention | Retain material review/decision/receipt evidence with issued artifacts, protecting private reviewer details and source content as required. |
| Smallest repair scope | One invalidated check or missing approval and the related issue gate; retain demonstrably unaffected reviews rather than recomputing everything. |

## Shared update invariants

Stable IDs identify the record, not its truth. A materially changed source representation, extraction, claim or issued report retains an identifiable revision and change reason. References resolve to the relevant revision; a current pointer never silently changes the evidence behind a historical claim. New or changed support triggers the smallest sufficient substantive recheck.

A source’s access restriction follows extracts, summaries, transformations and handoffs. Local possession is not authority to publish. Retention follows the consuming project's authorised policy; this design invents no universal period. A required removal may reduce auditability and must be communicated honestly, rather than bypassed in the name of preservation.

The workflow can be executed by one authorised researcher when the method permits. It does not invent independent expertise from multiple model instances. Where review or approval genuinely belongs to someone else, artifact consolidation cannot waive that requirement.
