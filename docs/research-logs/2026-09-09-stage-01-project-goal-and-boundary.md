# Deep Research Skills — Stage 1: Project Goal and Boundary

**Status:** Bootstrap research log  
**Stage:** 1 — Define Project Goal and Boundary  
**Date:** 9 September 2026

## 1. Purpose

This research log defines the initial domain boundary for `deep-research-skills` before skills, commands, providers, execution architecture or repository production surfaces are designed.

The project exists to encode **reusable evidence-led research production intelligence** as installable Agent Skills.

Its responsibility is not merely to search for information or generate long reports. It is to make research work traceable from a research need through evidence acquisition and analysis to a bounded synthesis whose uncertainty, provenance and temporal validity remain visible.

The Stage 1 boundary is intentionally domain-level. It does not propose a skill count or implementation architecture.

---

## 2. Governing Boundary

The governing Production Skills contracts establish four relevant ownership layers:

```text
production-skills
→ family-wide contracts and reusable cross-domain abstractions

deep-research-skills
→ reusable research production expertise

consuming Production Skills family / consuming project
→ domain interpretation, production decisions and downstream artefacts

Pactwright / project orchestrator, when used
→ lifecycle, responsibility, integration and project-governance semantics
```

`deep-research-skills` must remain independently useful without Pactwright.

Project-specific learned knowledge belongs to the consuming project's Project Intelligence or equivalent knowledge system rather than being absorbed into reusable Deep Research skills.

---

# 3. Project Charter

## 3.1 Mission

Enable AI agents to perform **defensible, evidence-led deep research as a production discipline** across domains.

A successful research process should be able to:

```text
understand what needs to be known
→ frame the research problem
→ find appropriate evidence
→ distinguish useful evidence from noise
→ preserve provenance
→ compare and triangulate sources
→ expose contradictions and gaps
→ synthesise without overstating certainty
→ produce a decision-ready research deliverable
→ update only the affected research when evidence changes
```

## 3.2 Repository-owned outcomes

The repository owns reusable behaviour for producing:

- clearly framed research questions and research briefs;
- defensible source strategies;
- evidence discovery and source triage;
- source verification and appraisal;
- evidence extraction with provenance;
- distinction between source statements, evidence, claims, inference and synthesis;
- triangulation and source-independence analysis;
- contradiction and alternative-explanation analysis;
- targeted gap research;
- calibrated uncertainty;
- temporally valid findings;
- traceable synthesis;
- citation and material-claim verification;
- bounded research refreshes when underlying evidence changes;
- research outputs suitable for handoff to a consuming domain.

The repository also owns research-domain quality criteria, failure modes, repair behaviour and benchmark semantics once later bootstrap stages define them.

## 3.3 Intended result

The result of Deep Research is an **evidence package plus synthesis**, not the final downstream product decision.

A research deliverable should make it possible for a consumer to understand at least:

```text
what was investigated
why it was investigated
what evidence was considered
which evidence was relied upon
what material claims are supported
what evidence conflicts
what remains uncertain or unknown
how current the findings are
what conclusions can defensibly be drawn
```

The exact artefact structure is deferred to Stages 3 and 5.

---

# 4. Intended Users

## 4.1 Primary users

### AI agents performing research

Agents need reusable research intelligence that is more rigorous than ad-hoc browsing and more domain-independent than a specialist production workflow.

Representative uses:

- research before implementing a software capability;
- technology or tool landscape analysis;
- gathering evidence for product and UX work;
- research supporting game/world simulation design;
- investigating precedent, market behaviour or case studies;
- evidence gathering for legal, policy or standards work;
- researching real-world systems before creative or technical production;
- refreshing previous research when its evidence may have changed.

### Production Skills families

Other Production Skills families are first-class consumers of research artefacts.

Deep Research provides the evidence substrate; the consuming family applies its specialist production expertise.

## 4.2 Secondary users

### Human researchers, engineers, designers, analysts and decision-makers

Humans may use the skills directly, supervise an agent, review research outputs or consume the resulting evidence package.

The project should improve auditability and decision quality for human reviewers without assuming a human must manually approve every low-risk research operation.

### Orchestrators and delivery systems

Systems such as Pactwright may invoke Deep Research as specialist execution expertise, but orchestration semantics remain outside this repository.

---

# 5. In-Scope Research Classes

Stage 1 accepts the bootstrap hypothesis that the core domain must be capable of supporting the following general research classes.

## 5.1 Fact finding

Resolve bounded factual questions while preserving source authority, temporal validity and uncertainty.

Examples:

```text
What does the current specification require?
When did a particular event occur?
Which feature is supported by the current release?
```

## 5.2 Landscape research

Map a domain, ecosystem, technology space, provider space, body of work or class of approaches.

The goal is useful coverage and structure rather than an unbounded list of search results.

## 5.3 Comparative research

Compare alternatives against explicit criteria using evidence that is sufficiently comparable and current.

The research layer establishes the evidence and analysis. The consuming domain owns the final selection when that selection requires domain production judgement.

## 5.4 Case-study research

Investigate relevant examples, implementations, incidents, organisations, products or historical cases and extract transferable evidence without treating anecdote as universal proof.

## 5.5 Evidence synthesis

Combine evidence from multiple sources while preserving source independence, disagreement, methodological limitations and uncertainty.

## 5.6 Trend research

Analyse change over time while distinguishing actual trend evidence from isolated novelty, repeated reporting or provider marketing.

Temporal validity is part of the research result.

## 5.7 Source verification

Determine whether a source, claim, quotation, statistic, event or referenced underlying source can be substantiated and correctly attributed.

## 5.8 Research updates and refreshes

Revisit previously researched questions when source conditions or evidence may have changed.

Refresh should preserve verified work and target stale, contradicted or newly relevant portions rather than automatically restarting the entire investigation.

---

# 6. Specialist Research Methods — Not Yet Core

The repository may eventually support specialist research methods, but Stage 1 does **not** promote them into the core merely because they involve research.

Examples requiring later evidence include:

- formal systematic reviews;
- scoping reviews;
- meta-analysis;
- specialist academic literature review protocols;
- legal research methodology;
- investigative OSINT operations;
- archival and historical methods;
- formal competitive-intelligence tradecraft;
- market sizing and forecasting;
- financial due diligence;
- scientific evidence grading;
- patent and prior-art research;
- specialist data acquisition or statistical analysis.

Later stages must determine whether a specialist method belongs in:

```text
core reusable Deep Research behaviour
or
an Extension Pack / specialisation
or
a consuming Production Skills family
or
an external specialist tool / provider
```

The default is **not** to expand core until evidence demonstrates that the behaviour is broadly reusable.

---

# 7. Boundary Map

## 7.1 Core ownership rule

```text
Deep Research
→ produces traceable evidence, analysis, synthesis, uncertainty and research artefacts

Consuming domain
→ interprets the research inside its own production responsibility and owns downstream commitments
```

## 7.2 Examples

### Software engineering

```text
Deep Research owns
→ evidence about libraries, architectures, standards, incidents, benchmarks and alternatives

Software Engineering Skills owns
→ architecture selection, implementation design, coding and engineering validation
```

### UI/UX design

```text
Deep Research owns
→ research evidence, prior studies, behavioural findings, product examples and source synthesis

UI/UX Design Skills owns
→ interaction design, design decisions, prototypes and UX validation strategy
```

### Game development

```text
Deep Research owns
→ evidence about real-world systems, references, technologies, historical examples and relevant mechanics

Game Development Skills owns
→ game-system design, implementation, balancing and runtime integration
```

### Legal work

```text
Deep Research owns
→ locating, verifying, comparing and synthesising legal sources and surrounding evidence

Legal Skills owns
→ legal interpretation, legal-risk analysis, legal-document production and domain-specific legal advice workflows
```

Deep Research must not convert generic evidence synthesis into an implicit claim of legal authority.

### Narrative / media production

```text
Deep Research owns
→ factual background, references, source evidence, precedent and contextual synthesis

Narrative / Video / Music Production Skills owns
→ creative interpretation and production decisions
```

### Product or business decision

```text
Deep Research owns
→ decision-relevant evidence, alternatives, uncertainties and supported implications

Consuming project / decision owner owns
→ strategic choice, prioritisation, investment or acceptance of risk
```

## 7.3 Project-specific knowledge boundary

Reusable behaviour:

```text
Prefer the direct primary source for a material claim when available.
```

Belongs in `deep-research-skills`.

Project-specific knowledge:

```text
Provider X failed the Kakeibo ingestion benchmark because its CSV parser corrupted this project's known export format.
```

Belongs in the consuming project's research logs or Project Intelligence unless later generalised and independently validated.

---

# 8. What Is a Research Deliverable?

A research deliverable is a **bounded, traceable answer to a defined research need**.

It is not synonymous with a polished prose report.

Depending on the request, the deliverable may be:

- a factual finding;
- a source-verification result;
- a comparison;
- a landscape map;
- a case-study synthesis;
- an evidence review;
- a trend assessment;
- a research dossier;
- an update to an earlier research result;
- a decision-support report.

Regardless of presentation, material conclusions should remain connected to their evidence.

A high-quality deliverable should preserve enough research state to permit review, targeted correction and later refresh without requiring every execution detail to become a permanent event log.

---

# 9. What Counts as Sufficient Evidence?

There is no universal minimum source count.

Evidence is sufficient when it is **proportionate to the claim, decision and risk** and the remaining uncertainty is made explicit.

At Stage 1, sufficiency is defined by the following conditions.

## 9.1 Claim support

Every material factual claim relied upon by the synthesis should have identifiable supporting evidence.

## 9.2 Source fitness

The evidence should be sufficiently direct, authoritative, methodologically credible, specific and current for the claim being made.

No single opaque source-quality score is assumed.

## 9.3 Independence

When corroboration matters, apparently separate sources should not be counted as independent when they merely repeat one underlying source, study, announcement or event.

## 9.4 Coverage

Research should cover the important parts of the question rather than optimise for raw source volume.

Known coverage gaps must survive into the deliverable.

## 9.5 Contradiction handling

Material contrary evidence must be represented and investigated rather than silently discarded.

## 9.6 Temporal validity

Evidence must be current enough for the question.

Where relevant, event date, publication date, effective date, retrieval date and valid-as-of date should not be conflated.

## 9.7 Uncertainty calibration

The synthesis must not claim more certainty than the evidence supports.

## 9.8 Proportionate verification

Higher-consequence claims require stronger verification than low-impact exploratory findings.

Sufficiency therefore depends on:

```text
claim importance
×
decision consequence
×
evidence quality
×
coverage
×
agreement / contradiction
×
freshness requirement
```

The exact quality model and stopping rules are deferred to later stages.

---

# 10. Quality Definition

Deep Research quality is multidimensional.

The project should eventually evaluate at least the following dimensions independently rather than collapsing them into one universal quality score.

## 10.1 Relevance

The research answers the actual question and supports the intended downstream use.

## 10.2 Factual grounding

Material claims are supported by evidence rather than generated from unsupported model priors.

## 10.3 Provenance and traceability

A reviewer can trace important claims back to the sources and evidence that support or contradict them.

## 10.4 Source fitness

The research uses sources appropriate to the type and importance of the claim.

## 10.5 Coverage

The investigation addresses the important subquestions and meaningful alternatives without mistaking source volume for completeness.

## 10.6 Source independence

The synthesis distinguishes genuinely independent corroboration from repeated reporting of the same underlying evidence.

## 10.7 Contradiction integrity

Conflicting evidence is preserved, analysed and reflected in the conclusion.

## 10.8 Uncertainty calibration

Confidence, limitations, assumptions and unknowns are represented proportionately.

## 10.9 Temporal correctness

Claims are valid for the requested time horizon and do not present stale evidence as current.

## 10.10 Analytical integrity

Evidence, inference, interpretation and recommendation remain distinguishable.

## 10.11 Citation correctness

Citations support the claims they are attached to and point to the intended underlying evidence.

## 10.12 Decision usefulness

The deliverable is structured so that a consuming domain can act on the research without needing to reconstruct the investigation from scratch.

Decision usefulness does **not** mean Deep Research owns the final decision.

## 10.13 Auditability and reproducibility

Enough information is retained to understand how the research result was produced and to repeat or refresh material parts when needed.

## 10.14 Efficiency

The process uses proportionate effort and preserves valid verified work rather than performing unnecessary exhaustive retrieval or full reruns.

---

# 11. Human Decision Points

Human ownership should be based on consequence and delegated authority rather than inserted as a mandatory approval after every research operation.

## 11.1 Human-owned or explicitly delegated decisions

Humans or consuming systems retain authority over:

- the underlying business, product, legal, creative or engineering commitment;
- risk acceptance;
- budget or resource commitment outside delegated limits;
- publication of high-impact or externally consequential conclusions;
- domain-specific professional judgement where specialist accountability is required;
- overriding material unresolved uncertainty;
- changing an approved research objective when the change materially alters the decision being supported.

## 11.2 Research decisions that may be agent-owned

Within an authorised research brief, an agent may ordinarily decide:

- search-query formulation;
- source-discovery routes;
- source triage;
- retrieval ordering;
- evidence extraction;
- deduplication;
- targeted follow-up searches;
- citation checks;
- local repair of weak claims;
- stopping when the defined evidence threshold is satisfied.

Later stages should define escalation conditions for ambiguity, high consequence, conflicting evidence, source-access constraints and budget exhaustion.

## 11.3 No universal manual gate

The project should not encode a universal rule that all research requires human approval before synthesis.

Such a rule would make low-risk autonomous research unnecessarily expensive and would conflate research quality with workflow bureaucracy.

---

# 12. Downstream Handoffs

Deep Research can support any Production Skills family that needs external evidence.

Representative handoffs include:

```text
Deep Research
→ Software Engineering
→ technology, standard, architecture and implementation evidence

Deep Research
→ UI/UX Design
→ behavioural, product, interaction and research evidence

Deep Research
→ Game Development
→ real-world system, historical, technical and design-reference evidence

Deep Research
→ Legal Skills
→ verified authorities, sources, comparisons and surrounding evidence

Deep Research
→ Narrative / Video / Music Production
→ factual context, precedent, references and research constraints

Deep Research
→ consuming project / strategy function
→ landscape, trend, comparative and decision-support evidence
```

A handoff may include reusable metadata requirements, but the consuming domain owns what it subsequently produces.

---

# 13. Explicit Non-Goals

`deep-research-skills` is not intended to become:

- a universal reasoning framework;
- a generic autonomous-agent runtime;
- a universal web-browsing wrapper;
- a search-engine replacement;
- a provider-specific Deep Research API client disguised as a production workflow;
- a universal knowledge graph;
- a central database for every consuming project's research;
- a project-management or lifecycle engine;
- a replacement for Pactwright;
- a replacement for Project Intelligence;
- a generic note-taking or document-management system;
- a downstream product strategy skill;
- a software architecture or coding skill;
- a UI/UX design skill;
- a game-design skill;
- a legal interpretation or legal-document production skill;
- a narrative, video or music production skill;
- an oracle that hides disagreement or uncertainty behind one answer;
- an exhaustive-crawl system that assumes more sources always mean better research;
- a mandatory human-approval workflow;
- a repository of project-specific facts simply because those facts were learned through research.

The project may call external tools, agents, APIs and models to execute research operations, but those capabilities remain below the research production layer.

---

# 14. Core Boundary Tests

A proposed responsibility belongs in `deep-research-skills` when all of the following are substantially true:

1. it is reusable across multiple research domains;
2. it improves how evidence is framed, discovered, evaluated, traced, synthesised, verified or refreshed;
3. it does not require ownership of the consuming domain's final production judgement;
4. it can be expressed independently of one model or provider;
5. it is research production expertise rather than one project's learned fact.

A proposed responsibility should remain elsewhere when one of these tests applies:

```text
Is it mainly a consuming project's fact, preference or decision?
→ consuming-project knowledge

Is it specialist production judgement such as coding, UX design or legal interpretation?
→ relevant Production Skills family

Is it lifecycle, orchestration or project-governance behaviour?
→ Pactwright / orchestrator

Is it a provider-specific retrieval or execution capability?
→ execution layer / tool integration

Is it a method only one specialist research tradition needs?
→ investigate as a specialisation before adding to core
```

---

# 15. Stage 1 Decisions

The following hypotheses are accepted as the working boundary for subsequent bootstrap stages.

## Accepted

1. **Deep Research is a production discipline, not a search feature.**
2. **The core product is traceable evidence plus calibrated synthesis.**
3. **The repository owns reusable research behaviour, not consuming-project knowledge.**
4. **The consuming domain owns downstream interpretation and production commitments.**
5. **Fact finding, landscape research, comparative research, case-study research, evidence synthesis, trend research, source verification and bounded refreshes are all within the general Deep Research domain.**
6. **No specialist research methodology is automatically part of core.**
7. **Evidence sufficiency is contextual and risk-proportionate; there is no universal source-count threshold.**
8. **Quality is multidimensional and must preserve provenance, contradictions, uncertainty and temporal validity.**
9. **Human review is consequence-based rather than a mandatory gate for every research run.**
10. **Provider-specific deep-research systems are execution candidates, not definitions of the domain.**
11. **Deep Research should preserve verified research and support targeted refresh/repair rather than defaulting to full reruns.**
12. **The project must remain standalone and useful without Pactwright.**

## Deferred

The following remain intentionally unresolved until later stages provide evidence:

- exact research workflow;
- information and provenance schema;
- source taxonomy;
- source-quality model details;
- stopping rules;
- cost and effort tiers;
- execution providers and tools;
- core skill count;
- command decomposition;
- Extension Pack dimensions;
- benchmark design;
- repository production scaffold.

---

# 16. Exit Assessment

Stage 1 exit criterion:

> A defensible domain boundary exists without a proposed skill count.

**Result: satisfied.**

The project now has a working charter, ownership boundary, user/use-case map, quality definition, human decision model and explicit non-goals.

Stage 2 can therefore investigate professional deep-research practice without allowing current AI-provider capabilities to define the research discipline.

---

# 17. Governing References

- `production-skills/docs/bootstrap/README.md`
- `production-skills/docs/bootstrap/new-project-process.md`
- `production-skills/docs/bootstrap/domain-research-process.md`
- `production-skills/docs/bootstrap/shared-abstraction-process.md`
- `production-skills/docs/specs/01-production-skills-family-system.md`
- `production-skills/docs/specs/02-production-skills-project-contract.md`
- `production-skills/docs/specs/03-production-skills-evaluation-and-extension-packs.md`
- `production-skills/docs/specs/04-cross-domain-orchestration-and-integration.md`
- `deep-research-skills/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md`
