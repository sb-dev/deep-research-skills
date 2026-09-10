# Stage 3: Question, Evidence, Claim and Provenance Model

Date: 10 September 2026. Working branch: `feat/bootstrap`.

## Authority, inputs and acceptance checklist

The acceptance contract is section 9 of the [original bootstrap](2026-09-07-deep-research-skills-new-project-bootstrap-process.md), read from `main`, together with sections 1–5 and the applicable research and preservation gates in section 29. The original specification still has blob `8ff62c92bada2861ece3684a9e73a83da75d9d94`. The family `main` revision was checked and remains `d109b1f5f085f9493711803c0c801b9812427d57`; its governing documents are identified in the accepted Stage 1 log.

This stage resumes the same authorised execution, not a different bootstrap attempt. The remote `feat/bootstrap` reference was read back at `5edbff2f7859c27c2a9689a30ada55972c0c83fd`, the Stage 2 publication receipt. Its complete recursive tree contains the accepted Stage 1–2 outputs and no Stage 3 file. At resumption, the local environment contained no surviving Stage 3 draft. No other branch was used.

The accepted inputs were re-read from that revision:

- [Stage 1 charter and boundary](2026-09-10-stage-01-project-goal-and-boundary.md): research integrity is owned here; downstream decisions, private project knowledge and specialist authority are not.
- [Stage 2 professional practice](2026-09-10-stage-02-professional-practice.md), [method comparison](2026-09-10-stage-02-method-comparison.md) and [source register](2026-09-10-stage-02-sources.md): the nine traditions do not reduce to one method; access, units, transformations and inference must stay distinguishable.
- [Stage 2 glossary](2026-09-10-stage-02-glossary.md), [failure taxonomy](2026-09-10-stage-02-failure-taxonomy.md) and [quality dimensions](2026-09-10-stage-02-quality-dimensions.md): preserve the vocabulary and the distinctions behind F04–F14, F16–F19 and K01–K16.
- [Progress record](bootstrap-progress.md) and [Stage 2 verification](2026-09-10-stage-02-verification.json): previous content and remote publication passed. Earlier validation results are inspected records, not newly rerun research benchmarks.

The six substantive Stage 2 files and the Stage 1 boundary file match the accepted blobs in the progress record. Container cloning again failed because `github.com` could not be resolved. New-file checks therefore run against locally created stage outputs; existing-path and preservation checks use the connector-inspected remote tree. This is not represented as a complete local Git checkout.

| ID | Required activity / acceptance condition | Governing reference |
|---|---|---|
| R01 | Re-read original stage, constraining principles and accepted prerequisites; establish branch provenance. | Execution instructions §3; bootstrap §§2, 5, 9, 29. |
| R02 | Model every listed research-brief concern and question/downstream-use relationship. | §9 Research brief: ten concerns. |
| R03 | Assess all twelve candidate source-record fields and define their meaning and applicability. | §9 Source record. |
| R04 | Model all six listed evidence-item concerns. | §9 Evidence item. |
| R05 | Model all seven listed claim concerns. | §9 Claim. |
| R06 | Preserve source, evidence, claim, synthesis and recommendation as different responsibilities without a mandatory universal graph or schema. | §9 Required distinctions and Exit. |
| R07 | Define provenance rules that identify inspected material and meaningful transformations. | §9 Outputs; §5 evidence before synthesis and auditability. |
| R08 | Define multidimensional source quality and claim-relative applicability. | §9 Outputs; §5 Source quality. |
| R09 | Define uncertainty and distinguish source information, observation, extraction, inference, interpretation, forecast, recommendation, assumption and unknown. | §9 Outputs; §5 Evidence and judgement / Uncertainty. |
| R10 | Define event, publication, effective, retrieval and valid-as-of semantics, including unknown and changing evidence. | §9 Outputs; §5 Time. |
| R11 | Define and demonstrate evidence-to-claim traceability through a final report, including contradictions and repair. | §9 Outputs and Exit; §5 Preservation; §29 Research/Evaluation behaviour. |
| R12 | Complete all six output responsibilities; verify substance, references and consistency; preserve prior work; commit only this stage and verify publication. | §9 Outputs/Exit; execution instructions §§5–8. |

Counts and applicability: four minimum object definitions, 35 explicitly listed field concerns (10 + 12 + 6 + 7), and six output responsibilities. The source-field list is expressly a candidate list, so the table below records applicability rather than inventing unknown values. There is no mandated file-per-output, source quota, example count or serialization. Sections 1–6 are the six completed design outputs. The worked records test this model; they are not the fifteen primary examples assigned to Stage 12. Provider selection, retrieval-path research, workflow/file-lifecycle architecture, cost/stopping mechanics, skills, packs, benchmark implementation, canonical specifications and installation remain assigned to Stages 4–20. Those later deliverables are NOT APPLICABLE to Stage 3; none is substituted for a current requirement.

## Research and design basis

The main evidence basis is the accepted professional comparison, not a new claim to have repeated all 42 source investigations. Three targeted primary-source checks resolved modelling details. Access date for all three: 10 September 2026.

| ID | Source actually inspected | Evidence used and limit |
|---|---|---|
| N1 | W3C, [PROV Model Primer](https://www.w3.org/TR/prov-primer/), Working Group Note, 30 April 2013; header and §§1, 2.1–2.9. | Separates things, production activities, responsibility, derivation and revisions. This is a conceptual reference, not evidence that this project implements PROV or needs RDF. |
| N2 | W3C, [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/), Recommendation, 23 February 2017; §§4.2, 4.2.4–4.2.5 and 4.3. Date cross-checked against its [official publication history](https://www.w3.org/standards/history/annotation-model/). | Distinguishes selecting a passage from identifying the representation containing it. Position-only selection is vulnerable to changed content. No JSON-LD or selector implementation is adopted. |
| N3 | Li, Higgins and Deeks, [Cochrane Handbook, Chapter 5](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-05), chapter updated October 2019, online edition inspected; §§5.2.1, 5.4.3, 5.5.4–5.5.5. | Links reports to studies, retains useful supplementary reports, records discrepant extraction and its resolution. Clinical-review conduct is not made universal. This rechecks Stage 2 S03 rather than adding an independent research tradition. |

Discovery used searches for W3C provenance derivation/revision, W3C text selectors, and Cochrane multiple-report linkage. The current official documents were opened; an older PROV working-draft search result and an annotation diff/older draft were not used as the final authority. Relevant sections were inspected directly. These sources inform small distinctions; all field names, support states, repair rules and representation choices below are this project's explicit design synthesis constrained by the bootstrap, not quotations from those sources.

### Alternatives and decisions

| Alternative | What it preserves | Defect or cost | Decision |
|---|---|---|---|
| Report with bibliography only | Readable prose and source list. | Cannot reliably identify which passage supports which material proposition or what was actually inspected. | Reject as a sufficient research record. |
| Compact Markdown with identifiable questions, sources, evidence and claims | Human-readable support chain, including uncertainty and limitations. | Large comparisons become hard to inspect if kept in prose alone. | Adopt for bounded work where all required semantics remain explicit. |
| Separate tables or structured records with a derived report | Repeatable reference checks and manageable larger evidence sets. | Can create duplicate authorities or unnecessary empty fields. | Permit when scale/repair warrants it; preserve one authoritative value per concern. |
| Universal graph, central evidence database or mandatory RDF/JSON-LD interchange | Potential querying across many domains. | Introduces infrastructure and a rigid integration boundary not required by current evidence. | Reject as a core prerequisite. Record only a future hypothesis, not a dependency. |

Adopt semantic contracts with flexible containers. Reject a single source truth score, automatic independence from distinct URLs, forced merges of similar records, and a global confidence default. A stable source label is useful, but a label alone cannot establish content, access, rights, independence or truth.

## 1. Research information model

### Objects and ownership

A **research brief** describes the authorised evidence need. A **source record** identifies the material considered and the representation/access actually available. An **evidence item** records a bounded source-supported observation or extraction. A **claim** is a proposition the research asks the reader to consider, with its inferential basis. **Synthesis** combines claims to answer the question. A **recommendation** adds a proposed course of action and explicit value assumptions; it is not automatically entailed by the synthesis.

These can occupy sections in one file or separately addressable records. Distinct responsibility does not require a file, database table or graph node for each object. The model describes information that must survive; it does not impose a universal research schema or choose the run directory layout owned by Stage 5.

A material claim is one whose error, omission or changed qualification could alter the answer, comparison, uncertainty or downstream use. Key quantities, attributed assertions, decisive comparisons and causal or predictive statements are material. Ordinary connective prose does not require an invented evidence record. Method decisions and assumptions are labelled as such rather than disguised as externally observed facts.

### Brief: all ten concerns

| ID | Required concern | Meaning and admissible representation |
|---|---|---|
| BR01 | Research objective | The evidence need or uncertainty to resolve, not merely a broad topic or desired conclusion. |
| BR02 | Decision / downstream use | Who will use the answer and for what; a bounded informational purpose is valid without a business decision. Action authority remains separate. |
| BR03 | Scope | Relevant entities, definitions, geography, time window, population/version and comparison criteria where applicable. |
| BR04 | Out-of-scope | Explicit exclusions preventing neighbouring questions from silently replacing the task; explain consequential exclusions. |
| BR05 | Questions / subquestions | Addressable questions linked to the objective; dependencies and required versus supplementary questions where needed. A hypothesis is labelled, not assumed answered. |
| BR06 | Required freshness | Target evidence period/as-of date and which facts must be checked for change. Stable historical questions can state that contemporary currency is not required. |
| BR07 | Source restrictions | Authorised/forbidden source classes, private-data boundaries and access limits; a citation request does not authorise new external disclosure. |
| BR08 | Quality threshold | Claim/use-relative minimum support and review expectations, including specialist requirements and unacceptable unresolved gaps; not a universal score. |
| BR09 | Budget / effort constraints | Known ceilings, permitted operations and commitment authority; an unspecified budget is explicitly unspecified, not unlimited permission. Stage 6 selects effort mechanics. |
| BR10 | Output form | Audience, form, level of detail, language and necessary supporting records; the brief may require a short answer rather than a report. |

The brief may express several concerns in one sentence. Its contents must still be recoverable without inference from a desired answer. A changed material question or decision criterion requires an identified revision and the appropriate owner's authority. Recording a subquestion does not imply authority to conduct a study, contact a person or purchase access.

### Source record: all twelve candidate concerns

| ID | Candidate concern | Decision and semantics |
|---|---|---|
| SR01 | Source identity | Required. Stable local ID plus enough title/identity to distinguish the item. Identify the inspected edition, version or representation where it matters. |
| SR02 | Source type | Required at useful granularity: documentation, article, report, code, dataset, archive record, private document, media or another stated type. Not a credibility ranking. |
| SR03 | URL / DOI / repository reference | Retain an available original locator; use a precise collection/file/connector reference when there is no public URL. A DOI or catalogue record is not evidence that full text was read. |
| SR04 | Publisher / author | Record identified responsibility; distinguish publisher, author, editor and host when relevant. Unknown or withheld identity is explicit; do not invent it. |
| SR05 | Publication date | Record the source's stated date and its meaning/precision. Unknown is admissible with a reason; retrieval date must not fill the gap. |
| SR06 | Retrieved-at | Record when the actually inspected representation was accessed, with available precision; for failed access record the attempt separately, not as successful full retrieval. |
| SR07 | Primary / secondary relationship | Record relative to the question/evidence, including known originating sources and report/unit relations. A source can be primary for its own announcement and secondary for a quoted finding. |
| SR08 | Methodology where relevant | Record the described method, design, measurement or production context needed to appraise the claim. A normative source may state that empirical methodology is not applicable. |
| SR09 | Included / excluded | Record an explicit selection decision; allow undecided and included-for-context. Selection is distinct from access, trustworthiness and support polarity. |
| SR10 | Exclusion reason | Required when excluded: the applied criterion and relevant scope. Not applicable when included. Inconvenient results are not a legitimate unstated exclusion rule. |
| SR11 | Quality observations | Preserve relevant dimension-specific observations, who/what assessed them, and their limits. Unassessed does not mean good. |
| SR12 | Known limitations | Record source and access limitations affecting interpretation, including missing methods, incomplete text, conflicts, corrections and restricted disclosure. |

Additional source information is conditional, not a universal mandatory envelope: access scope, content language, meaningful edition/revision, rights/access constraints, related-source references and publication-status checks. For a used source, access scope is always explicit: metadata-only, abstract-only, named passages, full text, inspected data subset, or specified media region. A source may be substantively included while still inaccessible; it then cannot support unseen content. Conversely, an excluded source may remain in the register to explain coverage.

A logically changing work and the inspected representation must be distinguishable. A source ID may identify a fixed representation directly or pair a stable work ID with an explicit revision. The choice must be consistent within the research. A materially changed representation receives a new versioned identity; it must not silently replace the basis of an old extraction. An unchanged re-access need only add a meaningful check date when freshness or auditability requires it.

### Relationship integrity

Relationships can be short entries rather than new object classes. Each material relationship identifies its endpoints, its meaning, its basis and whether it is established, suspected or unresolved. Useful meanings include copy-of, revised-from, quotes, derived-from, reports-on and corrects/retracts. Equality of URLs, titles, hashes or subject matter is not a universal relation test.

Keep these three concerns separate:

1. **Representation identity:** are these identical bytes, different formats, or different versions of one work?
2. **Underlying unit:** do the reports describe the same study, event, dataset, experiment, organisation or observation period?
3. **Evidential origin:** do the observations relevant to this claim actually have an independent basis?

One report can describe several studies; several reports can describe one study. Several independent observers can describe one event. Accordingly, a shared event is not automatically one evidential origin, and different publishers are not automatically independent. Store the relevant unit/origin association on the evidence item or support relation when a source contains several origins. An unresolved possible duplicate is not merged as a fact. There is no requirement to create a cross-project entity registry. [Design synthesis preserving Stage 2 Q3–Q4 and N3.]

### Evidence item: all six concerns

| ID | Required concern | Meaning and admissible representation |
|---|---|---|
| EI01 | What the source directly supports | A faithful bounded extraction or description of an inspected observation. Preserve negation, units, denominators, qualifiers and attribution. Do not insert the researcher's wider conclusion. |
| EI02 | Location / passage / data reference | An unambiguous locator within the inspected representation, with necessary surrounding context or selection criteria. See §2. |
| EI03 | Source link | Resolve to the exact source record/representation, not only a bibliography label or provider citation token. |
| EI04 | Claim relevance | Identify the question/claim and the extent to which this item bears on it. An item can be relevant without supporting the proposed answer. |
| EI05 | Contradictions | Identify contrary or apparently incompatible items and the context requiring comparison; no requirement to manufacture a contradiction when none is found. |
| EI06 | Confidence notes | State extraction/access uncertainty and limitations of the observation. Distinguish confidence in faithful transcription from confidence in the source's real-world assertion. |

Give each reusable or cross-referenced evidence item a stable ID. Identify extraction character where needed: quotation, paraphrase, transcription, visual observation, extracted number or calculated result. Calculated/translated/normalised material records the input references and transformation, rather than masquerading as the source's exact wording. Prefer one atomic evidence item for one auditable assertion; a table row can carry its attached denominator and context without being artificially fragmented.

### Claim: all seven concerns

| ID | Required concern | Meaning and admissible representation |
|---|---|---|
| CL01 | Claim text | The actual proposition, including material qualifiers and applicability. Split compound claims when their support differs. |
| CL02 | Claim type | Identify source-statement, observed fact, extracted data, inference, interpretation, forecast, assumption or unknown as appropriate; recommendation records remain distinct. |
| CL03 | Supporting evidence | Resolve material support to evidence IDs with an explanation of what is supported. Inferences also identify necessary premises or upstream claims. |
| CL04 | Contrary evidence | Preserve relevant opposition, null findings and qualifications separately from supporting material. State unsearched/none found/not applicable accurately. |
| CL05 | Inference level | Explain direct attribution/observation, transformation, cross-source inference, interpretation or prediction. This is not a numbered ladder of truth. |
| CL06 | Temporal validity | State the period, version or as-of context supported and any freshness limitation. A source's date alone is not the claim's validity. |
| CL07 | Confidence rationale | Explain strength and gaps in support, applicability, independence, agreement and review. Any label supplements this explanation. |

Conditional metadata includes claim ID, question reference, materiality, support status, review status, and revision/dependency links. These may be expressed in prose for a small answer. Support status, review status and confidence are distinct; their semantics are defined in §4. A claim registry may retain unsupported hypotheses for investigation, but a report must not assert them as established findings.

### Synthesis and recommendation remain distinct

Synthesis identifies the questions answered, the claims combined, alternatives/contradictions, limitations and what the combined evidence does and does not establish. It must not introduce an unsupported factual bridge between otherwise supported claims. New inferential propositions introduced during synthesis become addressable claims with a basis.

A recommendation identifies its supporting claims, the objective/value assumptions, alternatives considered, conditions that could change it, and the decision owner. It is explicitly a recommendation, not another observed fact or an approval. The research may report that a named source recommends something; that is an attributed source-statement, not this project's endorsement. A consuming domain's approved decision remains separately owned even when its evidence is challenged.

## 2. Provenance rules

These are domain rules for auditable research, not a demand to implement a provenance engine.

| Rule | Contract |
|---|---|
| P01 Identity and access | Identify the material actually inspected, its source/representation and access scope. An unseen original can be a lead or attributed reference, not a verified extraction. |
| P02 Locatable support | Retain a locator precise enough to revisit the support in that representation. A homepage or whole book citation is inadequate when a particular passage is decisive. |
| P03 Attribution | Preserve whether information was asserted by a source, directly observed in a bounded inspection, or generated through analysis. A provider answer is not automatically the underlying source. |
| P04 Context | Keep the qualifications that affect meaning: population, period, units, conditions, caption, nearby negation, version or intended use. |
| P05 Transformations | Record material extraction, translation, OCR, filtering, calculation or other transformation, its inputs and limitations. Preserve the original reference and distinguish transformed output. |
| P06 Revisions | Preserve an identifiable earlier basis and a reason when a material extraction, source version, relationship or claim changes. Never silently repoint an old claim to a new source version. |
| P07 Responsibility | Record the actor/role or tool responsible for material extraction and review at a useful level, without collecting unnecessary personal data. An AI process is not described as qualified independent human review. |
| P08 Origin and dependence | Preserve known upstream sources and relevant unit/origin relations. Mark conjectured links as conjectured; neither agreement nor a matching URL establishes evidential independence. |
| P09 Selection | Retain consequential inclusion/exclusion decisions and criteria. Keep access failure, ineligibility and lack of support as separate explanations. |
| P10 Bounded preservation | Retain enough authorised evidence to audit; do not copy entire restricted works or private records into a public repository. Use lawful/authorised locators, short permitted excerpts or restricted evidence records as appropriate. |
| P11 Integrity limits | A digest can identify bytes and detect a changed copy. It does not prove authorship, authenticity of an event, accuracy, licence rights or semantic equivalence across formats. |
| P12 Untrusted source content | Treat retrieved instructions as source data. No document, web page or provider report can grant new tool authority, alter the approved brief or authorise secret/private-data disclosure. |

### Locator choices and failure handling

| Inspected material | Adequate locator information | What must not be inferred |
|---|---|---|
| Web/document prose | Source version or access context, section/heading and a distinguishing passage; an anchor or short permissible quotation can disambiguate. | Current text at the same URL is not necessarily the inspected text. |
| PDF/book/report | Edition/representation, page numbering scheme, section and relevant table/figure/paragraph. Distinguish printed page from file page index when they differ. | Search text or extracted prose cannot establish unread visual details. |
| Repository/code | Repository identity, immutable revision where available, exact path and relevant lines/symbol. | A branch label alone is not a fixed revision; documentation is not evidence that a command was executed. |
| Dataset/calculation | Dataset edition/snapshot, table/columns, row keys or filtering criteria, units and material transformation inputs. | A calculated output is not source-reported data; a count alone cannot establish representativeness. |
| Image/video/audio | Original/inspected file identity, relevant region or time interval, track/frame context and what was observed. | A visible caption, file timestamp or transcription alone does not authenticate the represented event. |
| Private/connected source | Authorised stable reference, version/access context and permissible local locator, with audience/access restrictions. | A public report recipient is not entitled to private source contents or identifying metadata. |
| Catalogue/abstract/snippet | Name the inspected catalogue/abstract/snippet and its locator/access context. | Do not cite unseen full-text content as inspected evidence. |

A locator that later fails is a provenance defect or access limitation, not automatic evidence that the original claim was false. First distinguish changed location, changed content and unavailable access. Recover an authorised matching representation when needed, preserve the earlier record and mark any unverifiable part. A source's own correction or retraction is a separate, attributable piece of evidence; it may affect only some claims.

For reproducible computations, retain enough to repeat the material transformation: referenced inputs, input versions/selection, operation or code/version, parameters and units, and observed output. Record nondeterminism and environment details only where they could affect the result. Tool secrets, authentication tokens and unrelated personal data never belong in provenance. This does not prescribe a logging framework.

## 3. Source-quality dimensions

Quality is assessed relative to the proposed use of evidence, not once for an entire publisher. These nine dimensions preserve the original bootstrap's full list. They complement, rather than replace, the broader Stage 2 K01–K16 research-quality dimensions.

| ID | Dimension | Inspectable assessment | Consequence of an adverse or unknown assessment |
|---|---|---|---|
| SQ01 | Directness / primary versus secondary | How close is this item to the observation or authoritative statement relevant to this claim? | Qualify attribution or seek a closer source when the claim requires it; do not erase useful secondary context. |
| SQ02 | Authority / expertise | Is the identified author/institution competent and authorised to speak about this particular fact? | A title, institution or official domain alone cannot establish every assertion it hosts. |
| SQ03 | Methodological quality | Are the collection, measurement, study design or analytical methods fit for this inference? | State missing methods or obtain required specialist appraisal; do not infer quality from prestige. |
| SQ04 | Transparency | Are evidence, methods, assumptions and material limitations inspectable? | Explain the effect of opaque or inaccessible support; a fluent summary cannot fill the gap. |
| SQ05 | Recency / temporal validity | Does the evidence concern the required period, version and effective state? | Limit the currentness claim or recheck the affected evidence, not every stable historical fact. |
| SQ06 | Independence | Is there a distinct relevant originating observation, or shared data, sponsorship, method or transmission? | Record the specific dependence and avoid inflated corroboration. A common event does not itself settle this. |
| SQ07 | Conflicts / incentives | What disclosed or observable incentives could affect selection or presentation? | Treat as a dimension to examine, not automatic proof of falsity or permission to invent motives. |
| SQ08 | Specificity to the claim | Do scope, definitions, population, conditions and measurement match the proposition? | Narrow or split the claim; general background cannot carry a specific numerical or causal conclusion. |
| SQ09 | Stability / archivability | Can the inspected representation and relevant support be identified again within permitted access? | Record fragility and preservation limits; absence of an archive is not evidence of inaccuracy. |

Record observations, basis, assessor/role and relevant date; use explicit not-assessed/not-applicable/unknown explanations where appropriate. A quick fact about a document's publication label does not require an empirical risk-of-bias rubric. A claim about an intervention's effect cannot avoid methodological appraisal merely because its source is official.

Separate source-level concerns from evidence-item and claim-level consequences. A document can have unreliable speculation but accurately state its own version. A transparent source may report a null result that weakens a preferred hypothesis. An old primary record can be exactly right for a historical question. No dimension can be averaged away by a large number of citations. Specialist systems such as GRADE or CERQual retain their own method and scope; this design does not rename its generic confidence notes as those assessments.

## 4. Uncertainty model

### Epistemic distinctions

| Kind | Required distinction in the record and final wording |
|---|---|
| Source statement | Attribute the assertion to its identified source; faithful reporting is not independent confirmation of its truth. |
| Observed fact | State exactly what was directly inspected or measured and by whom/what. Observing a document's statement is not observing the external event it describes. |
| Extracted data | Preserve the source value, definition, unit, denominator and context; distinguish a transformed or calculated value. |
| Inference | Identify evidence/premises, reasoning and material assumptions; do not present the conclusion as a quotation. |
| Interpretation | Identify the explanatory framing and plausible alternatives; distinguish an author's interpretation from the researcher's synthesis. |
| Forecast | State horizon, conditions, basis and uncertainty. Likelihood of an event is different from confidence in the assessment. |
| Recommendation | Keep proposed action, values/trade-offs and decision authority separate from the evidential claim record. |
| Assumption | Label a premise accepted for analysis and explain why; unsupported assumptions must not become observed facts downstream. |
| Unknown | Identify what is not established and why: missing search coverage, missing evidence, inaccessible evidence, unresolved contradiction or unassessed support. |

### Three independent assessment concerns

**Support status** answers what the inspected evidence establishes for the claim as worded:

- `supported`: the stated scope is supported with its necessary qualifications;
- `qualified`: only a narrower or explicitly conditional proposition is supported;
- `contested`: material opposing evidence remains unresolved;
- `unsupported`: the available record does not justify asserting the proposition;
- `unassessed`: support has not yet been substantively checked.

These are design semantics, not mandatory literal keywords for every output format. A report can communicate the equivalent in clear prose. None implies the source is certainly true. `Supported` requires an accountable support judgement, not merely one nonempty evidence reference. Material claims marked unsupported or unassessed cannot be rendered as established results. A contested claim may be reported only with the unresolved disagreement and its consequence visible. A qualified claim's reported wording must contain the limiting condition; changing only an internal label is insufficient.

**Review status** records whether the relevant extraction/support judgement was checked, by what process and with what outcome. Useful states are unchecked, checked and needs-recheck. A checked claim may remain contested or unsupported. Changed source content, material wording or necessary premises invalidates the relevant earlier check; unchanged records need not be relabelled indiscriminately. Required qualified human review is not satisfied by a second AI pass.

**Confidence rationale** explains source quality, coverage, independence, applicability, agreement, inferential distance and known gaps. Optional qualitative labels must be interpreted within the stated method; there is no universal conversion into percentages or a numerical source score. Confidence in extraction, confidence in an external assertion and forecast probability are recorded separately when they differ. A method-specific confidence scale requires its method and limitations, not an unexplained number.

### Missing, negative, null and contrary information

A reported null result is an evidence item with its test/measurement context. An adverse or negative result is not an exclusion reason. Missing evidence is not a null result. A failed search is evidence about that bounded search, not universal evidence of absence. An inaccessible original is an access gap, not a disproved claim. A statement that no contradiction was found must be bounded by the search actually conducted; it is not a claim that no contradiction exists.

Contradiction records identify the propositions/evidence, common context under which they conflict, possible scope/definition/time explanations, checks performed and the remaining consequence. Apparent disagreement across different periods or populations may be reconciled by separating claims; genuine conflict must not be hidden through averaging or majority voting. Record a reconciliation as analysis with its evidence, not as an edited source statement.

An inference must inherit every material unresolved premise and limitation; it may reduce uncertainty only by an explicit, justified combination of evidence. No report is made more certain merely by shortening it. Corrections can narrow a proposition while preserving the valid part. A failure of a consequential assumption can legitimately require broad reconsideration; preservation protects valid work, not invalid conclusions.

## 5. Temporal-validity rules

Time concerns attach to the source, evidence or claim whose meaning they describe. Do not populate one generic date field and reuse it for different meanings.

| Concern | Meaning | Required treatment |
|---|---|---|
| Event date / observation period | When the described event occurred or the measurement was taken; may be a range. | Keep separate from publication and the time the researcher inspected a report. Unknown or disputed event time remains explicit. |
| Publication date | When the source says the inspected work/version was published. | Preserve precision and stated basis; distinguish original publication, revision and host upload dates where material. |
| Effective date / interval | When a rule, policy, versioned behaviour or stated condition applies. | Future effective dates are allowed as announced future states; they must not be reported as already effective. |
| Retrieved-at | When the researcher accessed the specific representation or subset. | Record actual access precision/timezone where relevant. A recent access does not make old content current. |
| Valid-as-of | The time or version for which the claim has been assessed as applicable, with its basis. | It is a bounded research judgement, not a guarantee through an unspecified future period and not automatically the retrieval date. |

Use the most precise reliable value available, not the most precise storage format available. A known year can remain a year; a disputed interval can remain a disputed interval. A timestamp with a timezone is appropriate for an actual timed operation, but midnight UTC must not be invented for a day-only source date. Record unknown versus not applicable explicitly. Do not infer publication dates from arbitrary URL paths, file modification metadata, search-engine dates or archive upload directories without attribution and justification.

### Temporal decisions and checks

A claim about a dated historical document can remain valid despite a newer publication. A claim about the current policy cannot be supported solely by an obsolete page. A newer unofficial assertion does not automatically override an older authoritative source; compare authority, actual change, effective period and applicability. Explain unresolved currentness rather than choosing by date alone.

When publication precedes an effective change, distinguish the announcement claim from the operative-state claim. A source accessed on 10 September can announce a change effective 1 October; the announcement is current evidence, while the future policy is not yet operative. An event may legitimately precede publication by years. A correction may be published after the event and revise what can now be concluded about it. No universal ordering between all five dates is imposed.

For a reused claim, identify its required freshness and the specific checks that justify continued use. Cached evidence may remain adequate for one historical claim but inadequate for a current version or price. If a needed recheck cannot be performed, preserve the earlier as-of claim, mark its currentness limit and do not silently advance its date. The refresh operation, effort allocation and stopping rules are designed in Stages 5–6; this stage supplies their temporal semantics.

A material temporal update links the old and new evidence/claims, the reason for the change and the dependent findings affected. Preserve an old claim as historical when still true for its old context. Withdraw only the unsupported applicability, not unrelated verified facts. A proposed update that changes an approved downstream decision is a handoff to its owner, not automatic authority to change that decision.

## 6. Evidence-to-claim traceability contract

The minimum support path is:

```text
report proposition
→ identifiable claim with scope, type and uncertainty
→ supporting / contrary evidence and inferential premises
→ inspected source representation plus locator and access scope
→ meaningful transformation / origin information where needed
```

An inference may depend on other claims, but following its support must eventually reach inspected evidence and explicitly declared assumptions. Circular citation between reports or between claims is not grounding. A source that merely repeats a target claim cannot supply independent confirmation simply because the chain has several links.

### Contract rules

| Rule | Obligation and failure consequence |
|---|---|
| T01 Question coverage | Each material reported finding relates to an agreed question; each required question has an answer or an explicit unresolved gap. A neighbouring answer does not satisfy the original question. |
| T02 Reference closure | Every reported material claim and every referenced evidence/source/premise resolves within the package or through an authorised, stable external reference. Unknown IDs are defects, not empty evidence. |
| T03 Exact inspected support | Evidence points to its inspected source representation and locatable support. Metadata-only access cannot ground an unseen passage. |
| T04 Semantic support | A substantive review checks whether the cited item supports the actual proposition, qualifiers, quantity and context. Reference existence alone cannot pass this rule. |
| T05 Contrary coverage | Material contrary items remain linked and discussed. An empty list carries an explicit search status: unsearched, none found within the stated search, or not applicable. Unsearched is a gap, never evidence that no contradiction exists; assess its consequence for the proposed claim. |
| T06 Inferential transparency | Identify reasoning, material assumptions and upstream premises. No evidence-free factual bridge may be introduced by synthesis or a recommendation. |
| T07 Wording fidelity | The report preserves claim type, scope, time and uncertainty. A qualified/contested record cannot be rendered as an unconditional finding. |
| T08 Citation placement | Place support close enough to identify the proposition it supports. Split compound statements whose parts have different support. Bibliography membership is not claim coverage. |
| T09 Authority and disclosure | Respect source-access and audience restrictions throughout the chain. A public citation must not leak a private title, identity or excerpt merely to improve apparent traceability. |
| T10 Preservation and repair | Identify the defective source, extraction, relation, premise, claim or rendering; update dependent findings and preserve unrelated valid records. Recheck changed semantic links. |
| T11 One authoritative value | A claim-source matrix or rendered citation list is a view of the same support record, not a second conflicting truth. Moving from Markdown to a table must preserve IDs, relationships and qualifiers. |
| T12 Bounded portability | A consumer can inspect the handoff without this chat or a source checkout, subject to legitimate source access. Provider-only citation tokens must be resolved into useful original or authorised local references. |

A citation style may be chosen for the audience. This contract does not mandate DOI availability, a bibliography format, an evidence database, or making confidential material public. When a recipient cannot access necessary private evidence, state the review limitation and authorised access route; do not call the result publicly reproducible.

### Worked trace: actual inspected source metadata

This is an actual bounded source observation from the N1 inspection, not a synthetic research result. It tests the traceability of an attributed source-metadata claim, not the substantive quality of an entire research programme.

**Brief Q-NOTE.** Objective: classify the publication identity of the inspected PROV Model Primer. Downstream use: correct source classification in this design log. Scope: that document's header; out-of-scope: every other PROV document and implementation conformance. Freshness: inspect the identified official page on 10 September 2026, while reporting its stated historical publication identity. Sources: official W3C page only. Quality threshold: direct header inspection with faithful attribution and explicit scope. Effort: bounded metadata check; no paid or specialist operation. Output: one attributed finding with traceable evidence and the stated scope.

**Source S-PROV.** N1 above; source type: official technical note; publisher: W3C; editors: Yolanda Gil and Simon Miles as identified in the document. Stated publication date: 30 April 2013. Retrieved-at: 10 September 2026, day precision. Access: header and named prose sections, not a claim to inspect every linked document. Primary for its own publication label. Included for Q-NOTE; exclusion reason not applicable. Empirical methodology not applicable to this metadata claim. Limitation: document status does not establish implementation correctness or current status of every PROV specification.

**Evidence E-NOTE.** S-PROV, document header immediately below the title; short exact text: “Working Group Note 30 April 2013”. Extraction: quotation from the visible header, with the W3C title context. Supports the document's self-described publication label/date, not the truth of external examples in it. No material transformation. Extraction confidence: direct text inspection; independent empirical validation is not claimed.

**Claim C-NOTE.** The inspected PROV Model Primer identifies itself as a W3C Working Group Note dated 30 April 2013. Type: source-statement; supporting evidence: E-NOTE; inferential level: direct attribution. Contrary evidence: none observed within the bounded header check; no broad contradiction search claimed. Support: supported for that attribution. Temporal validity: the inspected document's stated 2013 publication identity, checked on 10 September 2026. Confidence rationale: explicit official header; no inference about the status of other documents. Review: source-to-wording check performed in this stage.

**Report.** The inspected PROV Model Primer identifies itself as a W3C Working Group Note dated 30 April 2013. [N1, header; C-NOTE → E-NOTE → S-PROV.] This classification does not establish conformance of any implementation. No recommendation or downstream approval is implied.

The companion [traceability examples](2026-09-10-stage-03-traceability-examples.json) express the same factual chain in a structured record and contain explicitly synthetic contract challenges. The record format belongs to these design checks, not to a mandatory research runtime. A deterministic check confirms reference closure and agreement of the identifiers/attribution across representations; the separate manual review checks actual support.

### Semantic challenge review

These are design counterexamples, not claims that a deployed agent encountered or repaired them. The distinctions are reviewed against the original Stage 3 obligations and the Stage 2 failure taxonomy.

| Case | Defect or boundary tested | Required model behaviour and review finding |
|---|---|---|
| X01 Repeated press reports | Three publications repeat one measurement. | Keep three source records if useful, link one relevant origin, and do not claim three independent measurements. §§1–3 and T06 support this distinction. |
| X02 Independent event accounts | Two genuinely distinct observations concern one event. | Link the shared event without forcing one origin. Independence remains an evidenced claim-relative assessment. §1 relationship integrity avoids over-merging. |
| X03 Snippet versus body | A snippet appears to assert a result but full text adds a decisive limitation. | Record actual access; after body inspection, preserve the context and qualify the claim. P01/P04 and T03/T07 prevent access laundering. |
| X04 Correction in one report | One numerical extraction is corrected; an unrelated historical fact remains valid. | Version the affected evidence/claim and update dependants; preserve the unrelated chain. P06 and T10 prevent indiscriminate regeneration. |
| X05 Future effective state | A current announcement describes a future policy. | Separate announcement from operative-state claims; effective date cannot be replaced by retrieval date. §5 forbids asserting future operation as current. |
| X06 Honest uncertainty | An original source is unavailable and its reported result cannot be checked. | Preserve the attributed secondary evidence and access gap; no unseen-original extraction or definitive verdict. §§1, 4 and T03 apply. |
| X07 Calculated estimate | A result is derived from a filtered table. | Preserve input edition, selection, units, operation and output; label it calculated rather than source-reported. P05 and CL05 apply. |
| X08 Opposing or null result | Relevant negative evidence weakens the preferred answer. | Keep it eligible and distinguish null, adverse and missing information; explain the effect on synthesis. EI05, CL04, §4 and T05 apply. |
| X09 Recommendation leap | Supported technical facts are turned into “therefore deploy this option”. | Expose value assumptions and decision authority in a separate recommendation; factual support does not authorise action. §1 and T06/T09 apply. |
| X10 Private evidence handoff | An external reader cannot access a cited internal record. | Preserve a restricted locator and disclose the access/review limit without leaking private contents or claiming public reproducibility. P10 and T09/T12 apply. |
| X11 Inference cycle | Claim A relies on B, while B only restates A. | No terminal inspected evidence exists; mark unsupported and repair the grounding, not the wording. §6 and T02/T06 apply. |
| X12 False precision | A day-only retrieval record becomes a fabricated second-level timestamp and confidence percentage. | Preserve actual temporal precision and explained uncertainty; neither storage convenience nor formatting creates evidence. §§4–5 apply. |

## Verification, conformance and exit

The original section 9 is the verification authority. The [verification script](2026-09-10-stage-03-verification.py) checks this document's complete field/section coverage, reference closure in the worked records, the declared challenge inventory, local/known-baseline links and the research-log-only file delta. Its executed [results](2026-09-10-stage-03-verification.json) record actual checks and deliberately corrupted controls. These are document/model checks, not research-agent benchmarks or measurements of citation entailment quality.

The original current-stage section was re-read after drafting. On 10 September 2026, `python3 docs/research-logs/2026-09-10-stage-03-verification.py --baseline-manifest <inspected-parent-inventory.json> --negative-controls` returned exit status 0: eleven checks passed and all eight deliberately corrupted in-memory controls triggered their intended failures. The controls removed a required field, referenced missing evidence, duplicated an ID, removed a locator, introduced a premise cycle, asserted an unsupported claim, lost a qualification and asserted a future-effective state as already operative. No control mutation was retained in the published records. A complete stage checkout can run the same script with `--negative-controls` and without the separate inventory argument.

During semantic review, the initial wording of T05 was corrected to permit an explicitly unsearched contrary-evidence record while prohibiting its presentation as evidence of absence. This resolves a mismatch with CL04; it does not reduce the requirement to examine material contradictions. The final validation was rerun after that correction. The source-history check above verifies N2's publication date; it is not another independent methodological study.

The semantic review additionally inspects every field's meaning, not just its ID: access and eligibility differ; underlying event and origin differ; source/extraction confidence and claim confidence differ; dates have separate meanings; synthesis cannot erase qualifications; recommendation ownership remains with the consumer. The actual N1 header was compared to C-NOTE and its report rendering. The synthetic cases challenge the model's defined semantics without being presented as empirical evidence.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 | §§2, 5, 9, 29; execution §3 | Authority and accepted-input record | Read original/prior outputs; inspect branch/tree and unchanged family revision. | PASS |
| R02 | §9 Research brief | §1 BR01–BR10; Q-NOTE brief | Inspect all ten concerns and their use in a bounded real-source example. | PASS |
| R03 | §9 Source record | §1 SR01–SR12 and relationship integrity | Review all candidate dispositions, unknown values, access and identity semantics. | PASS |
| R04 | §9 Evidence item | §1 EI01–EI06; E-NOTE | Review context, locator, relevance, contradiction and extraction confidence. | PASS |
| R05 | §9 Claim | §1 CL01–CL07; C-NOTE | Review actual proposition, support/premises, contrary evidence, inference, time and rationale. | PASS |
| R06 | §9 distinctions/Exit | §1 objects; alternatives; §6 | Check five responsibilities remain separate in compact and structured forms; no graph dependency. | PASS |
| R07 | §9 provenance output; §5 | §2 P01–P12 and locator table | Review inspection, transformation, attribution, revision, authority and retention boundaries. | PASS |
| R08 | §9 source-quality output; §5 | §3 SQ01–SQ09 | Match all nine original dimensions; preserve question-relative, non-aggregate appraisal. | PASS |
| R09 | §9 uncertainty output; §5 | §4 epistemic/assessment distinctions | Review all nine epistemic kinds, missing/null/contrary differences and report constraints. | PASS |
| R10 | §9 temporal output; §5 Time | §5 dates and validity rules | Review all five time concerns, future/historical examples, unknowns and honest precision. | PASS |
| R11 | §9 traceability output/Exit | §6 T01–T12; actual trace; X01–X12 | Trace actual report to inspected source; review semantic counterexamples and targeted repairs. | PASS |
| R12 | §9 six outputs; execution §§5–8 | §§1–6; verification files; progress | Inspect complete deliverables and stage-only delta; record actual local checks and remote readback before progression. | PASS |

### Exit assessment

The six required design outputs are present. A bounded real report proposition can be traced to inspected evidence through both compact and structured representations. Source statements, research judgement, contradictions, temporal validity and downstream action remain distinguishable without a mandatory universal schema.

No unresolved Stage 3 design question requires a user decision. Stage 4 must consume these semantic requirements when researching source/acquisition paths; a path must not claim access depth, provenance or currentness it cannot deliver. Stage 5 owns concrete workflow and artifact lifecycle, Stage 6 owns effort/stopping/refresh policy, and Stage 13 owns implemented evaluation architecture. No production skill, benchmark score, clean installation, release or maturity promotion is claimed here.

Publication gate: the complete stage and executed verification must be committed and the remote reference, parent and intended file blobs read back before Stage 4 starts. The resulting commit identity is recorded in the subsequent publication receipt, not invented inside its own content.
