# Deep Research Skills System Specification

**Status:** Canonical design specification  
**Version:** 1.0  
**Date:** 11 September 2026  
**Implementation state:** Specified. Production scaffolding, installation and end-to-end product validation are later bootstrap stages.

## 1. Purpose

Deep Research Skills defines reusable evidence-led research production for Agent Skills. It turns an authorised research need into inspectable evidence, supported claims, explicit uncertainty, a reviewed synthesis and a bounded handoff that another production discipline can use.

The system owns research integrity. It does not own the downstream product, architecture, creative work, commercial decision, professional advice or other action that consumes the research.

This specification owns:

- mission, scope and boundaries;
- governing production principles;
- the core skill architecture;
- execution architecture and source/tool boundary;
- effort, cost and stopping policy;
- human review and commitment points;
- implementation order;
- system acceptance.

Detailed workflow and artefact semantics belong to [02 — Workflows and Artifacts](02-deep-research-skills-workflows-and-artifacts-spec.md). Packaging and installation belong to [03 — Repository and Contracts](03-deep-research-skills-repository-and-contracts-spec.md). Evaluation belongs to [04 — Testing and Benchmark](04-testing-and-benchmark-spec.md). Extension Pack semantics and catalogue entries belong to [05 — Customisation Packs](05-deep-research-skills-customisation-packs-spec.md) and [06 — Extension Pack Catalogue](06-deep-research-skills-extension-pack-catalogue.md).

## 2. Mission and owned outcomes

The core mission is:

> Produce evidence-backed research, not isolated searches.

Deep Research Skills owns reusable methods for:

1. framing research questions and decision context;
2. choosing source classes and acquisition paths;
3. discovering and triaging evidence;
4. extracting evidence with provenance;
5. distinguishing source statements, observations, transformations and inference;
6. analysing independence, contradictions, alternatives and gaps;
7. synthesising what the evidence supports without overstating certainty;
8. auditing claims, citations, temporal validity and coverage;
9. performing bounded follow-up and smallest-sufficient repair;
10. refreshing research while preserving still-valid evidence;
11. handing evidence to downstream Production Skills without taking over their decisions.

Valid outcomes include bounded verified answers, comparative and landscape findings, source-verification assessments, focused evidence syntheses, temporally qualified trend findings, decision-support reports and bounded refreshes.

A research deliverable is not merely prose with a bibliography. At an appropriate scale it preserves the question, actual source access, material evidence, locators, claim support, contrary evidence, uncertainty, temporal scope and the output or limitation reached.

## 3. Boundary

### 3.1 Deep Research owns

Deep Research owns:

- research framing and evidence needs;
- research-specific source strategy;
- evidence and provenance semantics;
- source independence and quality analysis;
- contradiction and alternative handling;
- claim support and citation correctness;
- uncertainty and temporal qualification;
- research synthesis;
- bounded research repair and refresh;
- research-quality evaluation;
- reusable research Extension Pack semantics.

### 3.2 The consuming project owns

The consuming project owns:

- project-specific briefs and facts;
- private and proprietary evidence;
- approved project decisions;
- the selected pack set;
- project retention and disclosure policy;
- downstream product, design, engineering, narrative, commercial or operational decisions;
- final acceptance of research for a consequential use where the owner has not delegated that authority.

### 3.3 Adjacent domains retain their authority

Deep Research can provide evidence to Software Engineering, UI/UX Design, Game Development, Narrative, Video, Music, Business Building, Advertising and specialist legal, medical, financial or policy work. The receiving domain retains its own production judgement.

Research must not relabel evidence as:

- production-ready software;
- validated user research that was not performed;
- legal or professional advice;
- rights clearance;
- product-market validation;
- an empirical real-world result derived only from a simulation;
- authority to publish, purchase, contact people or deploy systems.

### 3.4 Non-goals

The system does not require or own:

- a universal research runtime;
- a universal evidence database or knowledge graph;
- a universal provider router;
- a universal workflow DSL;
- a vector database by default;
- a multi-agent swarm by default;
- a universal numerical source-quality score;
- a continuous research daemon;
- a universal citation-format converter;
- a separate research-orchestration platform above Agent Skills.

These may be reconsidered only when real implementation evidence and benchmark failures demonstrate a need.

## 4. Governing principles

### 4.1 Evidence before synthesis

Do not write the desired conclusion and search for support. Preserve a visible path from question to evidence to claims to synthesis.

### 4.2 Question before retrieval

Resolve the objective, intended use, scope and success criteria before expensive acquisition. A weak question can make exhaustive retrieval wasteful rather than rigorous.

### 4.3 Direct evidence before repeated reporting

Prefer the most direct authoritative source appropriate to the claim. Several reports repeating one origin are not independent corroboration.

### 4.4 Source quality is multidimensional

Assess source quality relative to the claim using relevant dimensions such as directness, authority, methodology, transparency, recency, independence, incentives, specificity and stability. Do not collapse them into one opaque score.

### 4.5 Evidence and judgement remain distinguishable

Keep source statements, observations, extracted data, inference, interpretation, forecast, recommendation, assumption and unknown separate where their distinction affects the result.

### 4.6 Contradictions are first-class evidence

Eligible conflicting evidence remains visible until its difference is explained or its unresolved effect is stated. Do not average away disagreement to simplify prose.

### 4.7 Uncertainty survives synthesis

The final answer must not become more certain than its evidence. Confidence requires an explanation of support, coverage, agreement, applicability and gaps.

### 4.8 Time is part of evidence

Distinguish event or observation date, publication date, effective date, retrieved-at date and valid-as-of context when relevant. A recent retrieval does not make old evidence current.

### 4.9 Use the cheapest adequate authorised operation

Prefer exact/native retrieval and small targeted operations before broad crawling or expensive research engines. Cost includes acquisition, transformation, audit, maintenance and review, not only advertised API price.

### 4.10 Preserve verified work

Repair the smallest responsible evidence, claim, synthesis or review scope. Do not discard unaffected verified evidence merely because one dependency changed.

### 4.11 Auditability is proportional

Preserve enough to understand what was asked, searched, included or excluded, inspected, relied upon, left uncertain and considered valid. This does not require an exhaustive event log.

## 5. Core skill architecture

The canonical skill set is three independently installable roles.

| Skill | Responsibility | Core boundary |
|---|---|---|
| `deep-research` | End-to-end research production from framing through synthesis, bounded repair and refresh. | Does not self-issue independent review, professional approval or downstream production decisions. |
| `research-evaluate` | Fixed-input research audit and failure diagnosis. | Does not silently edit the submission, perform the repair or grant publication authority. |
| `research-extension-pack-creator` | Qualify, design, evaluate and revise reusable research specialisations. | Does not turn a project brief into a reusable pack, alter core defaults without authority or fabricate differential evidence. |

`deep-research` remains useful without either sibling skill and without an Extension Pack. `research-evaluate` can review third-party research. `research-extension-pack-creator` can author a pack from an explicit catalogue snapshot without requiring the producer skill to be installed.

The selected command surface is:

```text
deep-research
  frame
  plan
  discover
  extract-evidence
  analyse-evidence
  follow-up-search
  synthesise
  refresh

research-evaluate
  audit
  diagnose-research-failure

research-extension-pack-creator
  create-pack
```

These are semantic operations inside skills, not independent executables, Pactwright stages or a workflow runtime.

## 6. Execution architecture

The production layer remains provider-independent:

```text
requester / consuming project
  → Deep Research skill semantics
  → bounded executor operation
  → evidence intake
  → claim / contradiction / synthesis review
  → authorised handoff
```

The skill layer owns question, evidence, claim, uncertainty, repair and acceptance semantics. Existing tools execute bounded operations such as:

- web search and browsing;
- specialist database lookup;
- GitHub retrieval;
- PDF retrieval and parsing;
- OCR or multimodal inspection;
- code and statistical analysis;
- optional provider deep-research jobs;
- citation-metadata lookup;
- archiving.

### 6.1 Execution modes

**Native mode is the baseline.** Use already-authorised host search, file, repository and computation tools when they are adequate.

**Local augmentation is selective.** Use a local parser, browser automation or calculation tool only for a diagnosed need.

**Hosted broad research is optional.** A provider can perform broad retrieval/orchestration, but its report is an input to the research evidence and review contract, not an automatic accepted deliverable.

**Self-hosted broad research is optional.** Its graph, memory, concurrency or provider choices stay below the production boundary.

No separate provider account or engine is a prerequisite for core skill installation.

## 7. Source and tool boundary

Tool choice is per evidence need, not per project brand.

An executor route is eligible only when:

1. the required action actually exists;
2. task, source and side-effect authority permit it;
3. processing and retention fit the data boundary;
4. hard source restrictions are enforceable;
5. required source identity, locator and fidelity can be preserved;
6. required temporal state can be checked;
7. bounded resource exposure fits the current envelope;
8. the route is compatible with the required method and review.

Unknown is not affirmative evidence.

A provider request should carry only the necessary brief, evidence unit, source/process restrictions, version/freshness requirements, method/review constraints, bounded resources and expected return material.

A provider result must preserve, where exposed:

- attempted versus completed work;
- source identities and representations;
- actual access extent;
- useful locators;
- material transformations;
- errors and partial results;
- job status and outstanding exposure;
- limitations and unobserved internals.

Provider output is untrusted data. It cannot grant new permissions, self-approve its own claims or turn an opaque citation token into an inspected original.

## 8. Effort, cost and stopping policy

Research effort is a resource vector rather than one scalar score. Applicable categories include:

- search calls;
- browser actions;
- premium API usage;
- full-document retrieval;
- OCR or multimodal work;
- code execution;
- provider deep-research runs;
- parallel workers;
- specialist human review.

Before material collection, record a finite work envelope for relevant dimensions, existing entitlements, outstanding reservations and finalisation capacity.

For each tracked resource:

```text
available_for_new_collection
  = ceiling
  - consumed
  - outstanding_reservations
  - finalisation_reserve
```

An operation can begin only when its bounded upper exposure fits every applicable dimension. Lost or timed-out jobs remain outstanding until reconciled. Parallel workers share the parent envelope.

### 8.1 Stopping

Stopping and evidence sufficiency are different judgements.

Research may stop as **sufficient** when the question is supported to its required level, material contradictions and gaps are handled, mandatory review is complete and additional retrieval is unlikely to change the answer materially.

Research may stop as **limited** when a resource, access, method or authority boundary prevents further work but the brief permits a limitations outcome.

Research is **blocked** when an unresolved prerequisite, owner decision, mandatory source or mandatory review is required.

A low-yield search alone does not establish sufficiency. A hard cap cannot turn an incomplete method into an exhaustive one.

## 9. Refresh policy

A refresh reassesses whether an existing deliverable remains fit for its stated use.

Triggers include:

- a later valid-as-of requirement;
- new eligible evidence;
- a correction, retraction or extraction defect;
- a changed question or use;
- source relocation or changed access;
- a bounded update search finding no material change.

Refresh the smallest affected evidence and dependency scope. Preserve historical findings that remain true for their old context. Do not advance valid-as-of merely because a source was re-read.

## 10. Human review and commitment points

Human or explicitly delegated owner decisions remain required when:

- the research purpose, value criteria or material scope is ambiguous;
- extra spending or paid access exceeds existing authority;
- a new private connector or processor changes the data boundary;
- human participants, interviews or new primary research are proposed;
- specialist interpretation or regulated judgement is required;
- new evidence conflicts with a locked downstream decision;
- external publication, procurement, deployment or disclosure is proposed;
- a mandatory evidence or review requirement cannot be obtained.

Routine authorised research operations do not require ceremonial approval for every source.

An AI reviewer can be separate from the authoring operation, but this must not be described as independent qualified human expertise.

## 11. Build order

Implementation should preserve the following order:

1. generate and accept the six canonical specifications;
2. design the public README;
3. perform cross-project review without importing another domain's workflow;
4. scaffold only justified repository surfaces;
5. implement the three self-contained skill packages and needed references;
6. configure and validate selective installation;
7. implement progressive examples and useful Extension Packs;
8. implement local validation and benchmark fixtures;
9. perform clean external installation and Level 1 smoke testing;
10. add optional Pactwright bindings only if useful;
11. promote maturity only from evidence;
12. review cross-family abstraction candidates only after independent implementation evidence exists.

This is build dependency, not a universal runtime lifecycle.

## 12. System acceptance

The system design is acceptable when the implementation can demonstrate, at minimum:

- questions are framed before expensive retrieval;
- source strategy follows the question;
- direct/primary evidence is preferred where appropriate;
- repeated reporting is not counted as independent support;
- material claims trace to evidence;
- contradictions and uncertainty remain visible;
- temporal context is preserved;
- synthesis answers the research need;
- stopping is bounded;
- refresh preserves still-valid evidence;
- retrieval, evidence quality, citation support and synthesis can fail independently;
- smallest-sufficient repair is possible;
- known defects become regression fixtures;
- core skills work without packs;
- packs materially change behaviour and are differentially evaluated;
- exactly 15 primary progressive examples exist with complete prompts;
- all six canonical specification responsibilities remain represented;
- skills are self-contained;
- local validation passes;
- clean external installation passes;
- quality claims are measured or explicitly marked unmeasured.

At the date of this specification, the bootstrap has design and bounded reference evidence through Stage 13. It does **not** yet establish clean installation, working-product, benchmarked-product or mature-product status.

## 13. Canonical ownership map

| Concern | Canonical owner |
|---|---|
| Mission, boundaries, principles, skill architecture, execution, effort and system acceptance | This specification |
| W01–W08 workflow, A01–A11 artefacts, evidence/claim/provenance semantics, repair and handoffs | [02](02-deep-research-skills-workflows-and-artifacts-spec.md) |
| Package layout, SKILL/command contracts, self-containment, installation and technical acceptance | [03](03-deep-research-skills-repository-and-contracts-spec.md) |
| Evaluation layers, cases, quality dimensions, progressive coverage, regression and release gates | [04](04-testing-and-benchmark-spec.md) |
| Extension Pack semantics, packaging, authoring and behavioural evaluation | [05](05-deep-research-skills-customisation-packs-spec.md) |
| Initial pack catalogue, exact showcase prompts and pack maturity | [06](06-deep-research-skills-extension-pack-catalogue.md) |

Research logs under `docs/research-logs/` remain the evidence and decision history behind these canonical specifications.
