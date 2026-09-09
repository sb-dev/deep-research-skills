# Deep Research Skills — Stage 2: Professional Deep Research Practice

**Status:** Bootstrap research log  
**Stage:** 2 — Research Professional Deep Research Practice  
**Date:** 9 September 2026

## 1. Purpose

This stage investigates how established research disciplines perform strong evidence work before `deep-research-skills` defines an AI workflow, skill architecture, command set or provider layer.

The goal is not to select one professional discipline and rename it “Deep Research”. It is to identify:

- behaviours that recur across materially different research traditions;
- behaviours that are specific to one epistemic task or evidence class;
- controls that become stricter as consequence, uncertainty or evidentiary burden rises;
- failure modes that a reusable research production system should prevent or expose;
- terminology that later stages need in order to model evidence without collapsing important distinctions.

Stage 1 established the boundary:

```text
Deep Research
→ produces traceable evidence, analysis, synthesis, uncertainty and research artefacts

Consuming domain
→ owns downstream specialist interpretation and production commitments
```

Stage 2 tests what professional practice implies for the research side of that boundary.

---

# 2. Research Basis

The investigation compares nine complementary traditions:

1. systematic review;
2. scoping review and evidence mapping;
3. research synthesis and evidence appraisal;
4. market and competitive intelligence;
5. technology landscape and horizon-scanning research;
6. investigative / digital open-source research;
7. journalistic verification;
8. intelligence analytical tradecraft;
9. policy / decision-support analysis;
10. archival / historical research as a provenance discipline.

The list contains ten entries because evidence synthesis is treated separately from systematic-review retrieval: synthesis quality and retrieval completeness are related but not identical concerns.

Primary or professional-standard sources were preferred. Important sources include:

- PRISMA 2020;
- the current Cochrane Handbook for Systematic Reviews of Interventions;
- the current JBI Manual for Evidence Synthesis;
- ICD 203 / ODNI analytic standards;
- UK Government Functional Standard GovS 010: Analysis;
- the Berkeley Protocol on Digital Open Source Investigations;
- Associated Press verification standards;
- Reuters journalistic standards;
- the 2025 ICC/ESOMAR International Code;
- Strategic Consortium of Intelligence Professionals resources;
- WIPO patent-analytics and patent-landscape practice;
- OECD technology horizon-scanning guidance;
- US National Archives archival principles.

These sources differ in authority and purpose. A professional code, reporting guideline, operational handbook and methodology manual are not interchangeable. This stage uses each for the behaviour it actually governs.

---

# 3. Executive Findings

## 3.1 There is no universal research-depth mode

The strongest finding is that professional disciplines vary the retrieval posture according to the epistemic task.

```text
systematic review
→ high-recall, protocol-defined, intentionally comprehensive

scoping review
→ broad and transparent mapping, comprehensive within declared constraints

competitive intelligence
→ decision-led, purposive collection around intelligence requirements

technology horizon scanning
→ broad, diverse, recurring weak-signal discovery

journalism
→ sufficient corroboration for an accurate, timely publishable account

open-source investigation
→ evidentiary acquisition plus authenticity, preservation, safety and legal/ethical controls

policy analysis
→ proportionate analytical work matched to decision risk and value

archival research
→ context- and provenance-led discovery through records and their relationships
```

A reusable Deep Research system therefore should not equate “deep” with “retrieve as much as possible”. It should choose an evidence strategy appropriate to the question, consequence and source ecology.

## 3.2 Framing precedes expensive acquisition

Across systematic review, competitive intelligence, policy analysis and patent landscaping, strong practice defines the question, scope, intended use and important boundaries before large-scale collection.

Poorly framed retrieval can be both comprehensive and useless.

The reusable principle is:

> Depth is downstream of a defined research need.

## 3.3 Search breadth and claim strength are separate

Scoping-review practice demonstrates this especially clearly. A review can search broadly and transparently to map what exists without having sufficient critical appraisal to support strong practice or policy recommendations.

Conversely, a narrowly bounded factual verification can support a strong conclusion when the evidence is direct and authoritative.

Therefore:

```text
retrieval breadth ≠ evidence quality ≠ claim strength
```

## 3.4 Source count is not independence

Cochrane treats the **study**, not each report, as the unit of interest. Patent analytics commonly collapses multiple jurisdictional filings into a patent family representing one invention. Journalism requires independent corroboration rather than multiple repetitions of one claim. Archival provenance ties records to a creator and chain of custody.

This yields a cross-domain rule:

> Corroboration must be assessed against the underlying evidentiary origin, not the number of URLs or documents.

Later stages should model evidence lineage explicitly enough to detect repeated reporting, syndicated articles, copied claims, multiple reports of one study, multiple filings of one invention and other false independence.

## 3.5 Provenance is part of meaning

Archival practice shows that provenance is not merely citation metadata. The origin, custody, original order and relationship of records can determine what a document means and how much evidentiary weight it deserves.

Digital investigation reaches the same conclusion from another direction: preservation, authenticity and the path by which digital material was obtained affect whether it can support an investigation.

Deep Research should therefore treat provenance as an evidentiary property, not as a bibliography generated after synthesis.

## 3.6 Contradictions and alternatives are first-class analytical inputs

ODNI analytic standards require contrary information, analysis of alternatives, explicit uncertainty and visibility when analytic judgments change or materially differ. Cochrane retains discrepant reports and requires resolution or explanation. Journalism seeks multiple sides and additional checking when a claim does not fit the evidence.

A contradiction is not primarily a nuisance to be averaged away. It can reveal:

- differing populations or scopes;
- temporal change;
- measurement differences;
- methodological weaknesses;
- source incentives;
- incompatible definitions;
- a genuine unresolved state of the world.

## 3.7 Uncertainty must be explained, not cosmetically scored

ODNI links confidence to the evidentiary base and logic and requires causes of uncertainty to be described. UK government analysis requires uncertainty to be handled at a level proportionate to the decision and communicated without unwarranted confidence. Evidence-synthesis methods distinguish risk of bias, inconsistency, indirectness and imprecision rather than hiding them inside one source score.

The transferable pattern is explanatory uncertainty:

```text
what is uncertain
why it is uncertain
how material the uncertainty is
what evidence would reduce it
whether the conclusion depends on an assumption
```

## 3.8 QA should be proportional, independent where material and continuous

Cochrane requires independent eligibility decisions for consequential inclusion judgments and expert peer review of searches. UK government analysis uses proportionate assurance, verification, validation and independent peer review. Journalism uses editorial verification throughout production rather than only at the end.

The reusable pattern is not “a human checks everything”. It is:

> Apply stronger and more independent review to decisions where an error would materially alter the research result or downstream decision.

## 3.9 Research should be updateable

Professional research assumes evidence changes.

Systematic reviews define update behaviour; journalism corrects and evolves stories; horizon scanning is inherently recurrent; analytic tradecraft surfaces changes in judgments; policy analysis records assumptions and versions so work can be reassessed.

The research artefact therefore should preserve enough state to answer:

```text
what changed?
which claim does it affect?
which evidence is now stale or superseded?
does the synthesis need local repair or full reconsideration?
```

## 3.10 Decision-ready does not mean decision-owning

ODNI explicitly distinguishes intelligence analysis from policy recommendation. Cochrane cautions against converting evidence findings directly into context-dependent decisions that also require values, resources and preferences. UK government analysis is designed to inform commissioners and decision makers, who retain approval authority.

This strongly confirms the Stage 1 boundary: Deep Research can expose implications and decision-relevant evidence without absorbing the consuming domain's final authority.

---

# 4. Professional Practice by Research Tradition

## 4.1 Systematic review

### Primary purpose

Answer a pre-specified evidence question by identifying and synthesising eligible studies while minimising selection, publication and other review biases.

### Representative professional roles

- review authors;
- subject experts;
- information specialists / librarians;
- independent screeners;
- data extractors;
- statisticians / methodologists;
- peer reviewers.

### Protocol and framing

Systematic review practice starts with scope, question and eligibility criteria. Search methods are planned in advance rather than improvised after results are seen.

PRISMA 2020 primarily governs transparent **reporting** through its checklist and flow diagrams; it should not be mistaken for the whole conduct methodology. The Cochrane Handbook provides the stronger conduct model.

### Source discovery

Cochrane searches are deliberately high-sensitivity. Multiple relevant bibliographic sources, registers and other evidence sources may be required. Search restrictions can create language or publication bias, so restrictions should be justified rather than silently applied.

### Inclusion / exclusion

Eligibility criteria are defined before final selection. Full-text inclusion decisions are consequential enough to require at least two independent reviewers in Cochrane intervention reviews, with a defined disagreement-resolution process.

### Source appraisal

Included evidence is not treated as equally reliable merely because it passed eligibility. Risk of bias, methodological quality and certainty affect interpretation.

### Extraction and provenance

Structured extraction should faithfully represent source material. Different reports of one study may contribute different information and must be linked.

### Deduplication and independence

This tradition provides one of the strongest reusable lessons for Deep Research:

```text
record duplicate
≠
report duplicate
≠
underlying study duplicate
```

A single study may have several articles, abstracts, registry entries and regulatory reports. Multiple reports must be collated so the study, not the document count, is the analytical unit.

### Contradictions

Conflicting results across reports are retained and resolved where possible. A primary report may be selected and justified, but secondary reports are not discarded merely because they conflict or are less convenient.

### Uncertainty

Certainty is driven by the evidence base, not by rhetorical confidence. Risk of bias, inconsistency, indirectness, imprecision and missing evidence can weaken what can be concluded.

### QA

Search strategies receive expert peer review. Material inclusion decisions receive independent duplication. Data and analysis are subject to methodological review.

### Reporting

PRISMA-style flow reporting makes records identified, excluded and included visible, including reasons for exclusion at relevant stages.

### Update behaviour

Review searches can be rerun and previously included evidence checked for retractions, corrections or new information. Update methodology recognises that old evidence may become invalid without making every update a clean-room restart.

### Characteristic failures

- question drift after seeing results;
- narrow database coverage;
- over-precise search that misses relevant evidence;
- unjustified language/publication restrictions;
- duplicate study counted more than once;
- selective outcome extraction;
- ignored retractions or corrections;
- “no evidence of effect” misreported as “evidence of no effect”;
- recommendation strength exceeding evidence certainty.

### Transferable core lessons

- define eligibility before expensive retrieval;
- optimise recall when the task requires completeness;
- distinguish underlying evidence from reports about that evidence;
- keep exclusion decisions auditable;
- preserve corrections/retractions and contradictory reports;
- match conclusion strength to evidence quality.

---

## 4.2 Scoping review and evidence mapping

### Primary purpose

Map the breadth, characteristics, concepts, evidence types and gaps in a field rather than necessarily answer a narrowly causal or practice question.

### Protocol

JBI recommends explicit, transparent and reproducible searching with a protocol and declared constraints.

### Discovery posture

Scoping reviews often cast a wider source net than conventional systematic reviews, including grey literature, reports, websites and emerging-field material.

The objective is broad landscape coverage, but real search systems such as Google can return effectively unbounded result sets. JBI therefore recommends deciding during protocol design how many results will be screened and how “searched enough” will be judged. This converts an otherwise arbitrary stopping decision into a declared method.

### Appraisal

JBI does not generally require critical appraisal of each included source in a scoping review because the purpose is usually mapping rather than deriving practice-changing conclusions.

This matters for Deep Research because it proves that **coverage and appraisal intensity are independent parameters**.

### Synthesis

Scoping synthesis identifies patterns, categories, evidence concentrations and gaps. It can answer “what is known and where?” without pretending to answer “what should be done?”

### Reporting

Search strategies, databases, dates, limits and selection should be sufficiently documented to make the map transparent and auditable.

### Characteristic failures

- claiming completeness from a few convenient databases;
- ad-hoc Google stopping;
- weak tracking of grey literature;
- treating mapped evidence as if it had been critically appraised;
- converting descriptive gaps into strong causal or policy claims;
- hiding search constraints.

### Transferable core lessons

- choose retrieval breadth based on the research objective;
- predefine stopping behaviour for effectively infinite source spaces;
- record grey-literature acquisition explicitly;
- do not let a broad evidence map imply stronger evidence quality than was actually assessed.

---

## 4.3 Evidence synthesis and evidence appraisal

### Primary purpose

Turn heterogeneous evidence into defensible conclusions while preserving methodological limitations, inconsistency and uncertainty.

### Key distinction

Evidence synthesis is not simply “summarise every included source”. Strong synthesis asks whether evidence can legitimately be combined and what degree of confidence is warranted.

### Appraisal dimensions

Professional evidence synthesis distinguishes dimensions such as:

- methodological bias;
- inconsistency across evidence;
- indirectness to the actual question;
- imprecision;
- publication / availability bias;
- source conflicts or incentives.

### Negative and null findings

Negative or null evidence must remain visible. Absence of evidence is not automatically evidence that an effect or phenomenon is absent.

### Contradiction handling

Contradictions should trigger analysis of population, method, definition, timeframe, outcome measurement and bias rather than a mechanical majority vote.

### Recommendation boundary

A defensible synthesis can establish what the evidence supports while leaving context-dependent choices to decision owners who also consider cost, preferences, feasibility, ethics or risk.

### Characteristic failures

- vote counting sources;
- averaging incomparable studies;
- hiding null findings;
- treating publication volume as certainty;
- collapsing evidence quality into publisher prestige;
- deriving recommendation certainty from prose fluency.

### Transferable core lessons

- synthesis is a reasoning layer above extraction;
- compatibility of evidence matters before aggregation;
- uncertainty should have an evidence-based rationale;
- evidence findings and downstream recommendations should remain distinguishable.

---

## 4.4 Market research and competitive intelligence

### Primary purpose

Produce timely intelligence that supports a concrete market, competitor, customer or strategic decision.

### Professional roles

- intelligence client / decision maker;
- competitive-intelligence analyst;
- market researcher;
- primary-research specialist;
- subject-matter expert;
- strategy consumer.

### Framing

SCIP practice emphasises identifying organisational intelligence requirements and connecting research to strategy. The collection plan follows the information need rather than collecting everything first and deciding what it might mean later.

### Discovery

Source strategy commonly mixes:

- primary research;
- internal organisational sources;
- company and competitor material;
- filings;
- events and trade shows;
- market databases;
- industry specialists;
- customer evidence;
- secondary reporting.

The source mix is selected for the intelligence requirement.

### Appraisal

Source position, access, incentives and directness matter. Information collected from a competitor, a customer, a reseller and an analyst report can describe the same market from materially different vantage points.

### Triangulation

Competitive intelligence commonly compares multiple source classes before converting raw information into strategic intelligence. Corroboration matters because individual sources often have commercial incentives or partial visibility.

### Ethics

SCIP treats ethical collection as a professional requirement. Legitimate intelligence gathering is not espionage, deception without limits or “anything publicly reachable is fair game”.

### Synthesis

Strong competitive intelligence is selective and decision-relevant. It identifies implications, signals, likely competitor behaviour and material uncertainty rather than producing a maximal market dump.

### Update behaviour

Competitive conditions change continuously. Important assumptions, indicators and competitor movements are monitored and the assessment updated when a relevant signal changes.

### Characteristic failures

- collect-everything behaviour;
- research disconnected from a decision;
- competitor marketing repeated as fact;
- source incentives ignored;
- circular trade-press reporting mistaken for corroboration;
- stale market statistics;
- impressive landscape with no implications;
- unethical primary collection.

### Transferable core lessons

- define intelligence requirements from the downstream decision;
- select sources by the question they can actually observe;
- triangulate incentive-bearing sources;
- distinguish collection volume from strategic relevance;
- preserve indicators that can trigger later refresh.

---

## 4.5 Technology landscape research and horizon scanning

This stream combines two related but distinct practices.

### Patent / technology landscaping

WIPO patent landscaping begins by defining the technology boundary and translating that definition into a search strategy. Effective searches combine terminology, synonyms, classification systems and exclusions and explicitly trade precision against recall.

Patent documents introduce a crucial lineage issue: several filings in different jurisdictions can represent one underlying invention. WIPO analyses commonly use patent families to avoid counting the same invention repeatedly.

Technology landscape work can also go beyond patents by incorporating non-patent evidence, expert contributions and case studies.

### Horizon scanning

OECD describes technology horizon scanning as a way to detect and interpret emerging and converging technologies, including weak signals. Its 2026 review of 129 international exercises highlights methodological diversity, AI-enabled analysis, difficulty interpreting early signals and the need for robust standards.

Horizon scanning is intentionally future-facing and recurrence-oriented. A weak signal may be worth tracking without being strong enough to support a confident forecast.

### Source discovery

Typical source ecologies can include:

- patents;
- scientific literature;
- standards;
- company announcements;
- investment and market data;
- expert interviews;
- conference activity;
- government programmes;
- repositories and technical artefacts;
- specialist news;
- community signals.

### Uncertainty

Emerging technology has unusually high uncertainty because terminology, classifications, actors and capabilities evolve quickly. Many early signals do not mature into durable trends.

### Update behaviour

Monitoring and refresh are intrinsic, not optional. The landscape should carry a valid-as-of state and ideally identify monitored indicators.

### Characteristic failures

- keyword lock-in;
- classification blind spots;
- patent-document count mistaken for invention count;
- company announcement treated as deployed capability;
- hype volume treated as adoption;
- weak signal promoted directly to forecast;
- geographical/language source bias;
- stale technology taxonomy.

### Transferable core lessons

- translate a domain definition into a deliberate retrieval strategy;
- preserve precision/recall trade-offs;
- normalise source lineage before counting;
- distinguish observation, weak signal, trend and forecast;
- design landscape research for refresh.

---

## 4.6 Investigative / digital open-source research

### Primary purpose

Identify, collect, preserve, verify and analyse publicly accessible digital information so it can support a defensible investigation.

### Professional model

The Berkeley Protocol establishes minimum professional standards for digital open-source investigations, including preparation, identification, collection, preservation, verification and analysis. It also treats legal, ethical, digital, physical and psychosocial safety as part of the investigation method rather than an afterthought.

### Preparation

Before collection, investigators may need:

- threat and risk assessment;
- digital-landscape assessment;
- investigation plan;
- data-retention and access policy;
- appropriate tools and security posture.

The available digital landscape itself can be biased: different populations use different platforms, languages and technologies, so online visibility is not equivalent to real-world prevalence.

### Discovery and acquisition

Investigation may combine search engines, social platforms, maps, satellite imagery, archives, metadata services, specialist databases and direct web retrieval.

Bellingcat's tool practice adds a pragmatic operational lesson: a useful research tool catalogue records not only capability but cost, difficulty, requirements, limitations and ethical considerations. Tools should be selected for a problem, not worshipped as universal evidence engines.

### Verification

Digital material is tested for authenticity and contextual fit. Typical operations include geolocation, chronolocation, metadata inspection, reverse-image work, source contact and comparison with independent evidence.

### Preservation

For evidence with legal or investigative significance, preservation and chain-of-custody-like concerns can be as important as discovery because web material can change or disappear.

### Safety and ethics

Investigators must consider harm to subjects, witnesses, sources and themselves. A technically possible acquisition may still be professionally inappropriate.

### Characteristic failures

- trusting platform metadata without verification;
- reusing reposts as independent evidence;
- losing original content after deletion;
- screenshot without origin/context;
- geolocation based on one ambiguous clue;
- coverage bias from dominant-language platforms;
- tool capability overclaim;
- unsafe or unethical collection;
- destructive or non-reproducible acquisition.

### Transferable core lessons

- acquisition method is part of provenance;
- source availability can itself be biased;
- multimodal evidence requires modality-specific verification;
- preserve volatile material when the evidentiary need warrants it;
- tool limitations and ethical constraints belong in the research decision.

---

## 4.7 Journalistic verification

### Primary purpose

Publish a timely, accurate and fair account that can withstand scrutiny while correcting errors transparently.

### Verification model

AP states that verification is embedded from assignment through publication. Reporters and editors corroborate with documents and on-the-record sources; visual material receives metadata, timing and location checks; user-generated content is traced to its creator and checked through reverse image search, geolocation, contextual comparison and manipulation review.

Reuters places accuracy and balance above speed, prefers named sources, requires honest sourcing and transparent correction, and instructs journalists to cross-check information where possible.

### Independence

AP explicitly describes the use of several independent reliable sources. This is a more useful Deep Research rule than an arbitrary source-count threshold.

### Contradiction and fairness

Reuters practice requires seeking relevant sides of a dispute and being explicit about what remains unknown. A surprising or weakly supported claim should trigger more checking, not stronger prose.

### Corrections

Errors are corrected openly. Research quality therefore includes repair behaviour after publication, not only pre-publication confidence.

### AI acceleration boundary

AP's July 2026 newsroom standards provide a concrete modern precedent. AI may assist early-stage research, document summarisation, transcription, translation and other bounded operations, but editorial judgment, sourcing, verification and accountability remain with journalists, and generated output is reviewed before publication.

This does not imply Deep Research should require human editorial review universally. It demonstrates a broader principle:

> Automate bounded operations where the evidence can be checked; retain accountable review where an interpretation or publication decision carries material consequence.

### Characteristic failures

- speed displacing accuracy;
- anonymous-source weakness hidden;
- repeated reports mistaken for independent sources;
- visual content stripped of origin/context;
- single-source allegation presented as settled fact;
- correction buried rather than propagated;
- AI summary treated as source evidence.

### Transferable core lessons

- verification begins during acquisition, not after prose generation;
- source identity and direct knowledge matter;
- independent corroboration is claim-dependent;
- correction is a first-class research operation;
- AI output is not evidence merely because it is fluent.

---

## 4.8 Intelligence analytical tradecraft

### Primary purpose

Provide timely, objective, decision-relevant analysis under incomplete and sometimes deceptive evidence conditions.

### Standards

ODNI's ICD 203 framework requires analysis to be objective, independent of political consideration, timely and based on available relevant sources. Its tradecraft standards require analysts to:

- describe source/data/method quality and credibility;
- explain uncertainty around major judgments;
- distinguish underlying information from assumptions and judgments;
- analyse alternatives;
- address customer relevance and implications;
- use clear logical argumentation;
- explain changed judgments and significant analytic differences;
- strive for accurate assessments.

### Source appraisal

Credibility assessment is multidimensional. Relevant factors include accuracy, completeness, age/currency, possible deception, access and methodology.

### Alternatives and contradictions

Analysts must actively consider contrary information and alternative explanations rather than merely collect confirming evidence for an initial judgment.

### Uncertainty

Confidence is connected to evidentiary quality and logic. Knowledge gaps and assumptions should be visible because a conclusion may depend on them.

### Consumer boundary

The Intelligence Community describes its role as informing decisions rather than making policy recommendations. This is a strong analogue for the Stage 1 Deep Research boundary.

### QA

Analytic products are reviewed against explicit tradecraft standards, and institutional mechanisms exist to challenge politicisation or loss of objectivity.

### Characteristic failures

- confirmation bias;
- inherited judgment not reconsidered after new evidence;
- evidence and inference blended together;
- confidence language without rationale;
- alternative hypothesis omitted;
- customer relevance confused with advocacy;
- contrary evidence suppressed;
- changing assessment not explained.

### Transferable core lessons

- evidence, assumption and judgment must remain distinguishable;
- alternatives are part of analysis, not an optional appendix;
- uncertainty requires a causal explanation;
- decision relevance should not become advocacy;
- changed conclusions need an evidence trail.

---

## 4.9 Policy and decision-support analysis

### Primary purpose

Provide fit-for-purpose analysis that supports a defined public decision with assurance proportional to risk, value and consequence.

### Framing and roles

GovS 010 distinguishes the analysis commissioner, analyst and analytical assurer. The commissioner and analyst define the brief, context, scope, boundaries, criticality and required quality/certainty before the work is fully designed.

### Analytical cycle

The current standard describes an iterative cycle:

```text
customer engagement / scoping
→ design
→ conduct + checking
→ delivery
→ sign-off
```

The analysis can be amended as relevant information or circumstances change.

### Verification and validation

A particularly useful distinction is:

```text
verification
→ was the analysis carried out correctly?

validation
→ was the right analysis used for the stated need?
```

Deep Research will need an analogous distinction between correct execution of a research plan and whether the plan was appropriate to the question.

### Assurance

QA is proportionate to complexity, risk and impact. It is applied throughout the lifecycle and can include independent peer review. Important assurance questions include whether the problem, requirements, boundaries, assumptions and viewpoints have been adequately challenged.

### Record keeping

Plans, deviations, data, assumptions, verification/validation activity and other records should be versioned and retrievable in proportion to the work.

### Uncertainty

Uncertainty should be analysed at the level needed by the decision and communicated in balanced form without implying confidence that the evidence does not justify.

### Reporting

Decision-ready outputs include assumptions, limitations, uncertainty, applicability and links back to data, code or references where relevant.

### Characteristic failures

- technically correct analysis of the wrong question;
- QA added only at the end;
- disproportionate process for low-risk work;
- insufficient challenge of assumptions;
- uncertainty hidden from decision maker;
- no audit trail;
- results presented without applicability constraints.

### Transferable core lessons

- validate the research design, not only the final citations;
- scale QA to consequence;
- preserve assumptions and plan deviations;
- include applicability and uncertainty in the handoff;
- optimise for a decision need while leaving the decision with its owner.

---

## 4.10 Archival / historical research as a provenance discipline

### Primary purpose

Understand evidence in relation to its creator, context, custodial history and surrounding record structure.

### Provenance

The US National Archives describes provenance as both the principle of keeping records associated with their creating unit and information about chain of ownership/custody.

### Original order

Records are often most intelligible when their original organisational relationships are preserved. Removing a document from its surrounding record context can obscure its evidentiary significance.

### Source discovery

Historical research may therefore work through archive, record group, series, fonds, finding aid and related records rather than treating every document as an isolated keyword-search hit.

### Appraisal

Authenticity, creator, purpose, custody, context, uniqueness and relationship to other records can all affect interpretation.

### Characteristic failures

- document interpreted outside original context;
- later copy treated as equivalent to original without checking lineage;
- custodial gap ignored;
- isolated quote preferred over surrounding record series;
- absence from an incomplete archive treated as proof of non-existence.

### Transferable core lessons

- provenance can change interpretation;
- source relationships should survive extraction;
- absence of a retrieved record must not be confused with absence in reality;
- the “primary source” label alone does not establish authenticity or meaning.

---

# 5. Research-Method Comparison Matrix

## 5.1 Retrieval and evidence posture

| Tradition | Primary objective | Retrieval posture | Selection / stopping | Source / evidence unit | Appraisal emphasis |
|---|---|---|---|---|---|
| Systematic review | Answer defined evidence question | High recall / as extensive as feasible | Predefined eligibility; explicit flow; search-update rules | Underlying study, not report | Bias, method, applicability, certainty |
| Scoping review | Map field / concepts / gaps | Broad and transparent | Protocol constraints; declared stopping for grey/web search | Evidence source, with deduplication | Usually descriptive rather than full risk-of-bias appraisal |
| Evidence synthesis | Determine what body of evidence supports | Depends on supplying review method | Stop when evidence set defined and synthesis question answerable | Evidence body / study | Compatibility, bias, inconsistency, indirectness, imprecision |
| Competitive intelligence | Support strategic decision | Purposive, multi-source | Intelligence requirement satisfied / material gaps bounded | Decision-relevant observation or signal | Directness, access, incentive, recency, corroboration |
| Technology landscape | Map activity and direction | Broad but taxonomy-driven | Coverage/precision-recall threshold; refresh expected | Invention / technology signal, not raw document count | Classification validity, lineage, recency, adoption evidence |
| Horizon scanning | Detect emerging change | Deliberately broad, diverse and recurrent | Periodic cycle / weak-signal threshold | Signal / cluster / emerging issue | Novelty, plausibility, relevance, source diversity |
| OSINT investigation | Establish defensible facts/events | Targeted, multimodal | Evidentiary sufficiency plus safety/legal constraints | Original digital artefact / event | Authenticity, provenance, preservation, context |
| Journalism | Publish accurate timely account | Targeted and corroborative | Publish when material claims sufficiently verified | Original source / document / witnessed event | Direct knowledge, independence, identity, fairness |
| Analytic tradecraft | Inform decision under uncertainty | All relevant available evidence, gap-driven | Decision-timeliness and bounded uncertainty | Source information plus explicit analytic judgment | Source credibility, alternatives, assumptions, deception risk |
| Policy analysis | Support defined decision | Proportionate | Fit for purpose relative to impact/risk | Data/evidence appropriate to method | Validation, verification, assumptions, uncertainty |
| Archival research | Establish historical evidence in context | Provenance/context-led | Holdings and question determine depth | Record within creator/custodial context | Authenticity, origin, custody, original context |

## 5.2 Contradiction, QA and update posture

| Tradition | Contradictions / alternatives | QA / review | Update behaviour | Typical overreach to avoid |
|---|---|---|---|---|
| Systematic review | Preserve discrepant results; investigate heterogeneity | Independent selection; specialist search/method review | Formal update and retraction/correction checks | Strong recommendation from weak/uncertain evidence |
| Scoping review | Map disagreement without necessarily resolving causality | Protocol and transparent selection | Can be updated as field changes | Treating map as critically appraised answer |
| Evidence synthesis | Explain incompatibility and uncertainty | Methodological appraisal | Re-synthesise when evidence materially changes | Vote counting or false precision |
| Competitive intelligence | Triangulate competing accounts and motives | Client challenge / analyst review | Indicator-driven continuous refresh | Market narrative presented as fact |
| Technology landscape | Compare classifications, datasets and signals | Search/analysis validation | Recurring refresh essential | Patent/hype volume treated as deployment |
| Horizon scanning | Preserve competing futures and weak signals | Expert challenge and diversity | Continuous / periodic | Weak signal promoted to confident forecast |
| OSINT investigation | Seek alternative explanations for digital evidence | Method-specific verification; expert/legal review where needed | Re-verify when new artefacts/context emerge | Tool output treated as self-authenticating evidence |
| Journalism | Seek relevant sides, check surprising claims | Reporter/editor verification | Ongoing story updates; transparent correction | Speed or virality replacing corroboration |
| Analytic tradecraft | Required alternatives and contrary evidence | Product review against tradecraft standards | Explain changed judgments | Advocacy, hidden assumptions, inherited conclusions |
| Policy analysis | Challenge assumptions/options/views | Proportionate independent assurance | Revisit as circumstances/inputs change | Correct calculation applied to wrong decision problem |
| Archival research | Compare records and contexts | Archival/source criticism | New records/provenance can revise interpretation | Decontextualised primary-source certainty |

---

# 6. Answers to Stage 2 Questions

## 6.1 When is exhaustive search required versus purposive coverage?

### Exhaustive or near-exhaustive search is justified when

- the research claim depends on identifying the whole eligible evidence base;
- missing negative or unpublished evidence could materially bias the conclusion;
- a formal systematic-review or regulatory-style evidence burden applies;
- prevalence/counting claims require a defensible denominator;
- the downstream consequence warrants the cost.

Systematic review is the strongest exemplar.

### Broad but bounded search is appropriate when

- mapping a field or evidence ecology;
- identifying categories, gaps or terminology;
- exploring an emerging area with heterogeneous grey literature;
- building a technology landscape.

Scoping review and landscape research are exemplars.

### Purposive search is appropriate when

- supporting a specific strategic choice;
- verifying a bounded factual claim;
- investigating one event or artefact;
- filling an identified evidence gap;
- monitoring indicators or changes;
- the cost of exhaustive retrieval exceeds its likely effect on the decision.

Competitive intelligence, journalism and targeted OSINT are exemplars.

### Recurring scanning is appropriate when

- the objective is early detection rather than retrospective completeness;
- sources and signals change rapidly;
- a weak signal may become important later.

Horizon scanning is the exemplar.

**Stage 2 conclusion:** retrieval posture should be an explicit research-plan decision, not a hard-coded property of Deep Research.

---

## 6.2 How do experts decide a source is sufficiently direct and credible?

Professional practice repeatedly uses multiple dimensions rather than one source score:

```text
directness to event / phenomenon
identity and authority
method used to obtain the information
access to the underlying fact
evidentiary specificity
accuracy / track record
independence
possible incentive, conflict or deception
completeness
recency / temporal validity
provenance / custody
authenticity
applicability to the actual question
```

A prestigious publisher may still be secondary to an original filing. A primary source may still be deceptive, self-interested or methodologically weak. A direct eyewitness can be wrong. A high-quality study can be indirect to the population of interest.

**Stage 2 conclusion:** source quality should remain multidimensional and claim-relative.

---

## 6.3 How is source independence assessed?

Independence requires lineage reasoning.

Examples:

```text
five articles quoting the same press release
→ one underlying source

three papers reporting one trial
→ one underlying study

patents for the same invention in several jurisdictions
→ one patent family / invention for counting purposes

reposted social video on ten accounts
→ one original artefact unless separate capture is demonstrated

two analysts using the same vendor dataset
→ partially dependent evidence
```

The relevant unit varies by domain, but the reusable requirement is to identify the **underlying evidentiary origin** when independence matters.

---

## 6.4 How are multiple reports of the same underlying study/event handled?

Strong practice:

1. links reports to the same underlying entity;
2. keeps the individual reports available because each may contain unique information;
3. prevents them from being counted as independent corroboration;
4. records discrepancies;
5. selects or justifies the authoritative representation where one is needed;
6. preserves the lineage so a later correction can propagate.

This is directly demonstrated by Cochrane study/report handling and WIPO patent-family reduction.

---

## 6.5 How are negative, null and contradictory findings preserved?

They should remain visible at the evidence and synthesis layers.

Negative evidence can change:

- confidence;
- identified alternatives;
- scope of applicability;
- stopping decisions;
- recommended follow-up work.

The system should avoid converting:

```text
not found
→ disproven

not statistically established
→ no effect exists

one contrary high-quality source
→ outlier to delete
```

Contradictions should be classified and investigated before synthesis.

---

## 6.6 What can be safely accelerated and what needs specialist review?

### Strong candidates for acceleration

Subject to later validation, professional practice supports automation or AI assistance for operations such as:

- query expansion;
- metadata collection;
- candidate-source discovery;
- duplicate-record detection;
- report/study lineage suggestions;
- first-pass triage;
- transcription and translation;
- document summarisation for navigation;
- structured extraction drafts;
- citation-format preparation;
- change detection;
- indicator monitoring;
- preliminary contradiction flagging;
- search-gap suggestions.

### Operations requiring stronger review when material

- changing the research question or eligibility logic;
- final inclusion/exclusion in formal evidence synthesis;
- methodological quality or risk-of-bias judgment;
- authentication of consequential digital evidence;
- legal/ethical collection decisions;
- adjudicating material contradictory evidence;
- converting evidence into a high-consequence analytic judgment;
- publication or professional advice decisions;
- accepting unresolved uncertainty;
- overriding a known conflict or methodological weakness.

AP's 2026 AI standards are a useful concrete example: AI may assist early research, summarisation, transcription and translation, while editorial judgment, sourcing, verification and accountability remain human responsibilities in AP journalism.

**Stage 2 conclusion:** automate evidence operations more readily than consequential epistemic judgments.

---

## 6.7 What makes a report decision-ready rather than merely comprehensive?

A decision-ready research output:

- answers the actual decision question;
- identifies the material findings first;
- distinguishes facts, evidence, assumptions, judgments and recommendations;
- exposes source quality and relevant limitations;
- shows meaningful alternatives and contradictions;
- explains uncertainty;
- states what is unknown;
- identifies applicability and temporal validity;
- links material claims to evidence;
- avoids forcing the consumer to reconstruct provenance;
- presents implications without silently taking ownership of the consuming decision;
- identifies what future evidence would trigger refresh or reconsideration.

A comprehensive document that lacks these properties can increase cognitive load without improving the decision.

---

# 7. Terminology Glossary

The glossary is provisional. Stage 3 should tighten object definitions and avoid importing discipline-specific terms where a simpler cross-domain term is sufficient.

| Term | Working meaning for bootstrap | Important distinction |
|---|---|---|
| Research objective | What the investigation needs to establish and why | Broader than a search query |
| Research question | Answerable question derived from the objective | May have subquestions |
| Research protocol / plan | Predeclared method, scope and decision rules | Formality varies by research class |
| Eligibility criteria | Rules for including/excluding evidence | Strongly formal in systematic review; may be lighter elsewhere |
| Source | Origin or carrier from which information is obtained | Source is not automatically evidence |
| Report / record | A representation of an underlying study, event, artefact or source | Several reports can share one origin |
| Primary source | Source close to the event, data or creator | “Primary” does not guarantee truth or quality |
| Secondary source | Source interpreting or reporting other evidence | Can be valuable for context/discovery |
| Grey literature | Evidence outside conventional peer-reviewed publishing | Includes reports, theses, websites, registers and other forms depending on discipline |
| Evidence item | Specific information used to support or contradict a claim | Later Stage 3 object |
| Claim | Proposition asserted by the research output | Must remain distinguishable from source text |
| Assumption | Proposition provisionally accepted to permit analysis | Should be visible when material |
| Analytic judgment | Conclusion derived from evidence plus reasoning | Not the same as an observed fact |
| Inference | Reasoned step beyond what a source states directly | Needs provenance to supporting evidence |
| Provenance | Origin, acquisition history and context of evidence | More than URL metadata |
| Chain of custody | Documented control/history of evidence possession or preservation | Strongest requirement in forensic/investigative contexts |
| Source independence | Degree to which evidence has a distinct underlying origin | URL count is not sufficient |
| Deduplication | Removal/linking of repeated records or underlying evidence | Must distinguish record-level from origin-level duplicates |
| Corroboration | Independent evidence supporting the same material proposition | Repetition is not corroboration |
| Triangulation | Comparing evidence from different sources/methods/vantage points | Can expose rather than eliminate disagreement |
| Contradiction | Materially incompatible evidence or claims | Requires explanation or preserved uncertainty |
| Alternative hypothesis | Plausible competing explanation | Core analytic-tradecraft concept |
| Recall / sensitivity | Fraction of relevant material successfully retrieved | High recall often reduces precision |
| Precision | Fraction of retrieved material that is relevant | High precision can miss evidence |
| Screening / triage | Reviewing candidates for relevance or eligibility | Final eligibility may require stronger review |
| Critical appraisal | Structured evaluation of methodological credibility / bias | Not mandatory in every research class |
| Risk of bias | Likelihood that evidence generation is systematically distorted | Different from mere source reputation |
| Certainty / confidence | Strength warranted by evidence and reasoning | Should have rationale rather than cosmetic score |
| Verification | Checking that something is correct/authentic or that analysis was executed correctly | GovS 010 distinguishes from validation |
| Validation | Checking that the chosen method/analysis is appropriate to the stated need | Correct execution can still answer the wrong question |
| Horizon scanning | Systematic search for emerging changes and weak signals | Not a forecast by itself |
| Weak signal | Early, limited indication of possible emerging change | Should not be promoted directly to trend certainty |
| Intelligence requirement | Decision-linked information need in CI/intelligence practice | Useful analogue to research subquestion |
| Patent family | Related patent filings representing the same/similar invention lineage | Prevents jurisdictional double counting |
| Original order | Archival preservation of records' creator-defined relationships | Context can carry evidentiary meaning |
| Valid-as-of | Date/time through which a research conclusion is intended to be current | Distinct from publication or retrieval date |
| Refresh / update | Re-research affected parts when evidence changes | Should preserve unaffected verified work |
| Assurance | Confidence generated through proportionate checks/review | Can include independent review |
| Correction | Explicit repair of a published/delivered research error | Should propagate to affected synthesis |

---

# 8. Draft Domain Failure Taxonomy

This taxonomy is intentionally diagnostic. Later stages should map failures to artefacts, evaluation fixtures and smallest repair units.

## 8.1 Framing failures

- ambiguous objective;
- decision context missing;
- wrong research class selected;
- scope too broad to resolve;
- material boundary unstated;
- success criterion absent;
- answer assumed before investigation;
- question changes silently after evidence appears.

## 8.2 Retrieval failures

- source ecology too narrow;
- search engine ranking mistaken for evidence ranking;
- keyword lock-in;
- terminology/classification drift missed;
- geographical or language blind spot;
- grey literature omitted without justification;
- too much precision causing relevant evidence loss;
- excessive recall creating unaffordable noise;
- stopping opportunistically when convenient evidence appears;
- broad crawling where targeted gap search would suffice.

## 8.3 Source-fitness failures

- indirect source used where direct evidence exists;
- authority inferred from branding alone;
- methodology not examined;
- source incentive/conflict ignored;
- anonymous/unknown-origin evidence over-weighted;
- stale source presented as current;
- jurisdiction/population/version mismatch;
- “primary source” treated as automatically truthful.

## 8.4 Independence and lineage failures

- syndicated news counted as corroboration;
- several reports of one study counted separately;
- several patent filings of one invention counted separately;
- reposted media counted as independent eyewitnesses;
- circular citations;
- two analyses using the same underlying dataset counted as independent;
- lineage lost during extraction.

## 8.5 Acquisition and preservation failures

- volatile source not preserved when required;
- original unavailable and copy provenance not recorded;
- authentication metadata discarded;
- archive snapshot/date omitted;
- access method changes evidence context;
- chain of custody broken for consequential investigative evidence;
- terms/licence/access constraints ignored.

## 8.6 Extraction and provenance failures

- quotation detached from context;
- statistic copied without denominator/method;
- evidence location not recorded;
- source, evidence and claim collapsed into one object;
- model summary substituted for source content;
- table/figure interpreted incorrectly;
- translation uncertainty hidden;
- inference recorded as if directly sourced.

## 8.7 Analysis and synthesis failures

- confirmation bias;
- contradiction suppression;
- alternative explanation omitted;
- incompatible evidence averaged;
- majority-source voting;
- null/negative evidence dropped;
- absence of evidence converted to evidence of absence;
- false precision;
- causal claim from correlational evidence;
- context-specific result universalised;
- uncertainty reduced during prose polishing.

## 8.8 Decision-support failures

- research comprehensive but not relevant;
- critical finding buried;
- implications omitted;
- recommendation exceeds research ownership boundary;
- assumptions/limitations hidden from consumer;
- no valid-as-of state;
- consumer cannot tell what would change the conclusion.

## 8.9 QA failures

- no challenge of question or plan;
- correctness checked but fitness-for-purpose not validated;
- high-impact judgment receives no independent review;
- reviewer repeats analyst's assumptions rather than challenges them;
- citation points to source that does not support claim;
- material claim lacks evidence;
- review intensity unrelated to consequence.

## 8.10 Update and correction failures

- stale evidence remains authoritative;
- retraction/correction not propagated;
- new contradictory evidence appended without re-synthesis;
- entire investigation rerun when one claim changed;
- local update performed when the changed evidence invalidates the framing;
- previous conclusion changed without explanation;
- historical research state lost.

## 8.11 Ethical, legal and safety failures

- avoidable harm to research subjects/sources;
- privacy violation;
- deceptive or prohibited collection;
- copyright/licensing ignored;
- investigator security neglected;
- confidential/private source mishandled;
- source identity exposed unnecessarily;
- synthetic data used without disclosure where disclosure is material.

## 8.12 Automation / AI failures

- provider answer treated as a source;
- generated citation hallucinated;
- AI synthesis hides conflicting evidence;
- tool confidence substituted for verification;
- automation bias in screening;
- model cannot access a source but implies it did;
- generated extraction loses qualifiers;
- AI provider limitations not represented;
- specialist judgment silently delegated to a generic model.

---

# 9. Candidate Quality Dimensions

These are **candidates**, not the final benchmark schema. Later stages should determine which are independently measurable and which belong to particular research classes.

## 9.1 Framing fidelity

Does the investigation answer the actual objective, scope and downstream decision need?

## 9.2 Method fitness

Was the research class, retrieval posture and analytical method appropriate to the question?

## 9.3 Source-ecology coverage

Were the important source classes represented, including direct/primary evidence where appropriate?

## 9.4 Retrieval adequacy

Did the search achieve the necessary balance of recall, precision, diversity and cost for this research class?

## 9.5 Source fitness

Are material claims supported by sources with adequate directness, authority, methodology, specificity and temporal validity?

## 9.6 Provenance integrity

Can evidence be traced to its origin, acquisition context and relevant location within the source?

## 9.7 Independence / lineage correctness

Does the research distinguish independent evidence from repeated representations of one origin?

## 9.8 Evidence coverage

Are important subquestions and material claims supported, and are known gaps visible?

## 9.9 Extraction fidelity

Does extracted evidence preserve qualifiers, context, units, denominators and source meaning?

## 9.10 Contradiction integrity

Are material conflicts represented, investigated and reflected in synthesis?

## 9.11 Alternative-analysis quality

Were plausible competing explanations considered where the task requires them?

## 9.12 Uncertainty calibration

Does confidence match evidence quality, agreement, directness, coverage and known gaps?

## 9.13 Temporal validity

Are event, publication, effective, retrieval and valid-as-of dates handled appropriately?

## 9.14 Analytical integrity

Are source statements, observed facts, evidence, assumptions, inference, judgments and recommendations distinguishable?

## 9.15 Synthesis coherence

Do conclusions follow logically from the evidence without incompatible aggregation or rhetorical overreach?

## 9.16 Citation correctness

Does each material citation actually support the attached claim and identify the intended underlying evidence?

## 9.17 Decision relevance

Can the consumer understand implications, limitations and what matters without reconstructing the entire investigation?

## 9.18 Auditability / reproducibility

Is enough information retained to understand what was searched, selected, excluded, relied upon and changed?

## 9.19 Updateability / repairability

Can stale or incorrect evidence and affected claims be repaired without discarding unrelated verified work?

## 9.20 Ethical, legal and safety fitness

Were collection, use, preservation and disclosure appropriate to the evidence and context?

## 9.21 Efficiency / proportionality

Was the research effort proportionate to uncertainty, consequence and expected information gain?

No single total score is justified at this stage.

---

# 10. Cross-Domain Production Model — Provisional

The evidence supports a provisional process shape, but Stage 2 does not yet freeze it as the canonical workflow.

```text
research need / decision context
→ frame objective and questions
→ choose research class + depth
→ define source strategy and constraints
→ discover evidence
→ triage / screen
→ acquire and preserve where necessary
→ appraise source fitness
→ extract evidence with provenance
→ resolve lineage / deduplicate underlying origins
→ map evidence to questions and candidate claims
→ analyse contradictions and alternatives
→ identify material gaps
→ targeted follow-up research
→ synthesise with uncertainty
→ verify claims, citations and applicability
→ proportionate assurance / review
→ deliver decision-ready evidence package
→ retain valid-as-of state + update triggers
```

The most important qualification is that not every research class needs every operation at the same intensity.

Examples:

```text
simple factual verification
→ may need direct authoritative source + independent check, not formal eligibility screening

systematic evidence question
→ needs high-recall retrieval, protocol, eligibility, lineage and methodological appraisal

technology horizon scan
→ needs source diversity, weak-signal tracking and recurring refresh more than exhaustive retrospective retrieval

consequential OSINT investigation
→ needs acquisition/preservation/authentication controls that ordinary landscape research does not
```

The eventual system should therefore encode a **research control plane that can vary method intensity**, not a single monolithic pipeline that always performs maximum ceremony.

---

# 11. Core vs Specialist Behaviour Hypothesis

Stage 2 provides enough evidence to classify behaviours provisionally without designing skills.

## 11.1 Strong cross-domain core candidates

Observed across several independent traditions:

- objective / decision framing;
- question decomposition;
- source-strategy selection;
- proportionate retrieval depth;
- source fitness assessment;
- evidence provenance;
- evidence/source/claim separation;
- source-lineage and independence reasoning;
- contradiction preservation;
- alternative analysis where material;
- uncertainty explanation;
- temporal validity;
- targeted gap search;
- citation/claim verification;
- proportionate QA;
- decision-ready synthesis;
- bounded correction and refresh;
- preservation of verified unaffected work.

## 11.2 Likely method-specific or Extension Pack candidates

Require further evidence before placement:

- formal PRISMA reporting;
- Cochrane/MECIR-style eligibility and dual screening;
- GRADE-style certainty methodology;
- specialist scoping-review protocol;
- patent classification and family analytics;
- technology weak-signal scoring;
- formal competitive-intelligence collection techniques;
- digital-forensic preservation / chain of custody;
- geolocation / chronolocation methods;
- archival fonds/series methods;
- jurisdiction-specific legal research;
- specialist market sizing / forecasting;
- meta-analysis.

## 11.3 Strong consuming-domain boundaries

The following should not migrate into generic Deep Research merely because research supplies evidence for them:

- legal interpretation;
- clinical decision making;
- software architecture selection;
- UX design decisions;
- game design;
- product strategy commitment;
- investment decision;
- policy choice;
- editorial publication authority.

---

# 12. AI Implications — Bounded Stage 2 Conclusion

This stage intentionally does **not** research current AI research providers in depth; that belongs to Stage 7.

Professional practice nevertheless establishes constraints any execution layer must satisfy.

An AI execution mechanism is useful only if it can operate inside research discipline such as:

```text
question before retrieval
source before generated assertion
provenance before polished synthesis
lineage before source counting
contradiction before confidence
uncertainty before recommendation
verification before consequential use
bounded repair before full regeneration
```

AI capabilities should therefore be evaluated later against professional research requirements rather than used to define those requirements.

The 2025 ICC/ESOMAR code and AP's 2026 AI standards reinforce the need for transparency and accountable oversight when AI materially participates in research or published analysis. They do not justify universal manual review; they justify explicit responsibility proportional to the use and consequence.

---

# 13. Stage 2 Decisions

## Accepted

1. **No single professional tradition defines Deep Research.**
2. **Research depth must vary by epistemic task and consequence.**
3. **Exhaustive retrieval is a specialised requirement, not the default definition of rigor.**
4. **Broad mapping, purposive investigation and recurring scanning are all legitimate research modes when explicitly selected.**
5. **Source count is not evidence independence.**
6. **Evidence lineage must reach the underlying study, event, artefact, dataset, invention or origin when independence matters.**
7. **Provenance is part of evidence meaning and credibility.**
8. **Source quality is multidimensional and claim-relative.**
9. **Retrieval breadth, evidence quality and permitted claim strength are separate.**
10. **Contradictions, null findings and alternatives must survive into synthesis.**
11. **Uncertainty should be explained through evidence quality, gaps, assumptions and disagreement rather than fake precision.**
12. **Verification and validation are different: a correctly executed method can still be the wrong method for the question.**
13. **QA should be proportionate to consequence and independent at material judgment points.**
14. **Decision-ready research exposes implications while leaving downstream authority with the consuming domain.**
15. **Research correction and refresh are first-class operations.**
16. **Automation is safer for bounded evidence operations than for high-consequence epistemic or professional judgments.**
17. **Professional research practice, not AI provider features, remains the domain authority for subsequent workflow design.**

## Deferred

The following remain intentionally open:

- exact research information schema;
- claim/evidence/provenance object design;
- final source-quality dimensions and representation;
- exact confidence model;
- final research-class taxonomy;
- formal stopping algorithm;
- workflow artefact set;
- skill count;
- command boundaries;
- specialist-method Extension Packs;
- execution providers and tools;
- benchmark weighting and pass thresholds.

These should be resolved by Stages 3–13 rather than smuggled into Stage 2.

---

# 14. Exit Assessment

Stage 2 exit criterion:

> The production model is grounded in real research practice rather than AI provider features.

**Result: satisfied.**

The evidence from systematic review, scoping review, evidence synthesis, competitive intelligence, technology landscaping, horizon scanning, digital investigation, journalism, analytic tradecraft, government decision-support analysis and archival practice is sufficiently diverse to identify robust cross-domain research controls without treating one discipline as universal.

Stage 3 can now define the question, source, evidence, claim and provenance model using these professional distinctions as constraints.

---

# 15. Source Register

## Evidence synthesis and review methodology

1. PRISMA Executive. **PRISMA 2020 statement**. Reporting checklist and flow-diagram framework for systematic reviews.  
   https://www.prisma-statement.org/prisma-2020

2. Cochrane. **Handbook for Systematic Reviews of Interventions — Chapter 4: Searching for and selecting studies**. Current chapter updated March 2025.  
   https://training.cochrane.org/handbook/current/chapter-04

3. Cochrane. **Handbook — Chapter 5: Collecting data**. Study/report lineage and structured extraction guidance.  
   https://training.cochrane.org/handbook/current/chapter-05

4. JBI. **JBI Manual for Evidence Synthesis — Searching for the evidence**. Explicit, transparent, reproducible evidence searching.  
   https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/652967957/2.4.1+An+Introduction+to+Evidence+Synthesis+Searching

5. JBI. **Scoping Reviews — Searching for the evidence**. Grey literature, transparent web-search limits and protocol-stage stopping decisions.  
   https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862749/10.2.6+Searching+for+the+evidence

6. JBI. **Scoping Reviews — Critical appraisal or risk-of-bias assessment**. Explains why broad evidence mapping does not automatically justify practice/policy recommendations.  
   https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862791/10.2.8+Critical+appraisal+or+risk-of-bias+assessment

## Analytical tradecraft and decision support

7. Office of the Director of National Intelligence. **Objectivity / ICD 203 Analytic Standards**. Source quality, uncertainty, evidence-vs-judgment separation, alternatives, customer relevance and review.  
   https://www.dni.gov/index.php/how-we-work/objectivity

8. UK Government Analysis Function. **Government Functional Standard GovS 010: Analysis, version 2.2**. Updated 26 August 2025. Scoping, design, conduct/check, delivery, sign-off, proportionate assurance, uncertainty, verification, validation and record keeping.  
   https://www.gov.uk/government/publications/government-analysis-functional-standard--2/government-functional-standard-govs-010-analysis

## Investigative and journalistic verification

9. Berkeley Human Rights Center and UN OHCHR. **Berkeley Protocol on Digital Open Source Investigations**. Professional, legal and ethical identification, collection, preservation, verification and analysis of digital open-source information.  
   https://humanrights.berkeley.edu/publications/berkeley-protocol-on-digital-open-source-investigations/

10. Associated Press. **Verification at AP**. Independent corroboration, document/source verification and visual/UGC verification practices.  
    https://www.ap.org/solutions/verify/

11. Associated Press. **AP updates newsroom standards for artificial intelligence**, 23 July 2026. Bounded AI assistance with editorial judgment, sourcing, verification and accountability retained by journalists.  
    https://www.ap.org/the-definitive-source/announcements/ap-updates-newsroom-standards-for-artificial-intelligence/

12. Reuters. **Journalistic Standards**. Accuracy over speed, transparent corrections, source credibility and honest sourcing.  
    https://reutersagency.com/about/standards-values/

13. Bellingcat. **Online Investigation Toolkit**. Operational tool-selection practice including capability, cost, difficulty, requirements, limitations and ethical considerations.  
    https://bellingcat.gitbook.io/toolkit

## Market, competitive and technology research

14. ICC/ESOMAR. **International Code on Market, Opinion and Social Research and Data Analytics**, 2025. Fit-for-purpose research, transparent method/limitations, distinction between findings and interpretation, AI disclosure and human oversight.  
    https://standards.esomar.org/assets/documents/icc-esomar-code-2025.pdf

15. Strategic Consortium of Intelligence Professionals. **Competitive Intelligence Resources**. Current professional resource model covering ethics, collection/research, strategy/analytics, impact and benchmarking.  
    https://www.scip.org/general/custom.asp?page=resources

16. Strategic Consortium of Intelligence Professionals. **Best Practices in Establishing a Competitive Intelligence Function**. Intelligence requirements and organisational priorities as inputs to CI design.  
    https://www.scip.org/page/webinar-access--Best-Practices-Establishing-a-Competitive-Intelligence-Function

17. WIPO. **Patent Analytics**. Patent-landscape standards, technology-trend research and patent-analytics practice.  
    https://www.wipo.int/en/web/patent-analytics/

18. WIPO. **Patent Landscape Report: Decarbonizing Heavy-Duty Road Transport — Appendix**, 2026. Practical precision/recall search design and patent-family reduction to underlying inventions.  
    https://www.wipo.int/web-publications/patent-landscape-report-decarbonizing-heavy-duty-road-transport/en/appendix.html

19. OECD. **Building capacity in technology horizon scanning: A guide for policymakers**, 14 April 2026. Analysis of 129 international horizon-scanning exercises and challenges in interpreting early signals.  
    https://www.oecd.org/en/publications/building-capacity-in-technology-horizon-scanning_b4f0d383-en.html

## Archival provenance

20. US National Archives and Records Administration. **Archives and Records Management Resources — Terminology**. Provenance, chain of ownership/custody and original order.  
    https://www.archives.gov/research/alic/reference/archives-resources/terminology.html

21. US National Archives and Records Administration. **Principles of Arrangement**. Explains why creator context and original relationships preserve evidentiary meaning.  
    https://www.archives.gov/research/alic/reference/archives-resources/principles-of-arrangement.html

---

# 16. Relationship to Bootstrap

This log is the durable Stage 2 evidence record for:

- `docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md`;
- `docs/research-logs/2026-09-09-stage-01-project-goal-and-boundary.md`.

Later stages should consume this file rather than reconstructing Stage 2 from conversation history.
