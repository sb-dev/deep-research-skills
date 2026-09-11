# Deep Research Skills Workflows and Artifacts Specification

**Status:** Canonical design specification  
**Version:** 1.0  
**Date:** 11 September 2026  
**Implementation state:** Specified. This file defines research semantics, not a mandatory workflow runtime or physical file tree.

## 1. Purpose

This specification owns the Deep Research production workflow and the information that must survive it:

- the research workflow;
- research brief;
- source register;
- evidence and claim models;
- provenance;
- contradictions and gaps;
- synthesis and report semantics;
- refresh behaviour;
- failure taxonomy;
- repair routes;
- internal and cross-domain handoffs.

The system boundary and skill architecture are defined in [01](01-deep-research-skills-system-spec.md). Repository packaging belongs to [03](03-deep-research-skills-repository-and-contracts-spec.md). Evaluation belongs to [04](04-testing-and-benchmark-spec.md).

## 2. Workflow

The canonical workflow is eight responsibility groups:

```text
W01 Frame and authorise
  → W02 Plan method, source strategy and evidence needs
  → W03 Discover and triage
  → W04 Acquire, extract and establish identity/origin
  → W05 Map claims, contradictions, alternatives and gaps
       ↔ W06 Resolve one bounded gap through the responsible earlier operation
  → W07 Synthesise and audit the exact proposed deliverable
  → W08 Deliver the reviewed revision and handoff

A required owner decision blocks.
A defect re-enters its owning responsibility.
A refresh starts from the last accepted research state.
```

A bounded fact check can compress several responsibilities into one document and a few operations. A formal review may need a much more explicit protocol. The semantics remain the same without forcing every task through identical file count, source count or research method.

### W01 Frame and authorise

Inputs:

- actual request;
- existing approved decisions;
- project restrictions and intended use.

Resolve:

- objective;
- scope and exclusions;
- questions and required subquestions;
- freshness;
- permitted sources/processors;
- quality/review requirements;
- effort/commitment boundaries;
- output form and audience.

Exit: an authorised A01 brief supports the next operation. Material ambiguity or authority conflict returns to the owner.

### W02 Plan method, source strategy and evidence needs

Map each required question to:

- evidence unit;
- appropriate method;
- source classes and acquisition paths;
- inclusion/exclusion;
- transformations;
- expected analysis;
- review needs;
- finite effort.

Exit: A02 distinguishes intended work from actual search and states what evidence would be adequate.

### W03 Discover and triage

Perform the declared discovery or supplied-candidate triage. Record:

- queries or corpus;
- filters and continuation;
- result boundary;
- eligibility;
- actual access state;
- exclusions and reasons;
- identifiable duplicate records and suspected relationships.

Exit: selected sources are registered for acquisition, and incomplete coverage remains visible.

### W04 Acquire, extract and establish identity/origin

Retrieve the authorised representation and inspect the required passage, data region, code revision or media interval.

Preserve:

- exact source/version identity;
- access extent;
- locator;
- material context;
- units and denominators;
- transformations;
- representation/report/unit/origin relationships.

Exit: A03/A04/A10 can be revisited without trusting later prose.

### W05 Map and challenge claims

For each material claim:

- link support;
- preserve contrary evidence;
- assess inference and applicability;
- inspect source independence;
- retain assumptions and alternatives;
- determine temporal validity;
- record unresolved gaps.

Exit: A05–A07 distinguish supported, qualified, contested, unsupported and unassessed propositions.

### W06 Resolve a bounded gap

Choose one unresolved A07 gap, then re-enter only the necessary earlier operation.

The attempt must have:

- discriminating evidence sought;
- permitted route;
- finite resource reservation;
- actual result;
- effect on the gap.

An unsuccessful attempt does not close the gap. A legitimate limitations outcome links the owner's accepted boundary.

### W07 Synthesise and audit

Integrate compatible claims into A08. Render the exact proposed A09 report. Register new inferential bridges as claims before they are asserted.

Audit, as applicable:

- coverage;
- citation support and placement;
- source quality and independence;
- contradictions;
- uncertainty;
- temporal validity;
- reproducibility;
- fit for use.

Structural validation and substantive support remain separate.

### W08 Deliver and hand off

Check:

- exact reviewed revision;
- audience and disclosure authority;
- support access;
- current temporal basis;
- unresolved limitations;
- actual delivery authority.

Record actual issue/delivery state. A generated file path or completed provider job is not automatically a confirmed delivery receipt.

## 3. Research information model

The minimum distinct responsibilities are:

- **brief**: authorised evidence need;
- **source**: identified material and inspected representation/access;
- **evidence**: bounded observation or extraction from a source;
- **claim**: proposition and its inferential/support basis;
- **synthesis**: integration of claims answering the question;
- **recommendation**: proposed action using evidence plus values/trade-offs.

These responsibilities can be sections in one file or separate records. Distinct semantics do not require a database or graph node per object.

### 3.1 Research brief

A01 must preserve, where applicable:

- research objective;
- downstream use and decision owner;
- scope;
- out-of-scope;
- questions/subquestions;
- required freshness;
- source and processor restrictions;
- quality and review threshold;
- budget/effort constraints;
- output form and audience.

A changed material purpose or criterion is a revision requiring the appropriate owner.

### 3.2 Source register

A03 records:

- source identity;
- source type;
- original locator such as URL, DOI, repository ref or connector item;
- publisher/author/responsibility;
- publication date where known;
- retrieved-at time;
- primary/secondary relationship relative to the question;
- method where relevant;
- included/excluded/undecided status;
- exclusion reason;
- dimension-specific quality observations;
- known limitations;
- actual access extent;
- meaningful version/representation;
- rights or disclosure limits when relevant;
- known or suspected relation to other sources.

A source can be primary for its own announcement and secondary for an external claim. Access, selection, truth and support polarity are different properties.

### 3.3 Evidence item

A04 preserves:

- what the inspected source directly supports;
- exact locator;
- source/representation link;
- relevance to the question/claim;
- contrary or conflicting relation where applicable;
- extraction/access uncertainty;
- units, denominators and qualifiers;
- transformation character such as quotation, paraphrase, OCR, transcription, calculation or normalisation.

Calculated or transformed evidence retains input identities and transformation details.

### 3.4 Claim

A05 preserves:

- actual proposition including material qualifiers;
- type: source statement, observation, extracted data, inference, interpretation, forecast, assumption or unknown;
- supporting evidence;
- contrary evidence;
- inferential level and necessary premises;
- temporal validity;
- confidence rationale;
- question reference;
- support and review state;
- revision/dependency relationships where useful.

Material compound claims should be split when their support differs.

## 4. Relationship integrity

Keep three questions separate:

1. Are two representations the same bytes, format variants or versions of one work?
2. Do several reports describe the same underlying study, event, dataset or observation period?
3. Do the claim-relevant observations have independent evidential origins?

Different URLs do not prove independence. One event can have several independent observers. Several publications can report one study.

Material relationships identify:

- endpoints;
- relation such as copy-of, revised-from, reports-on, quotes, derived-from, corrects/retracts;
- basis;
- established, suspected or unresolved state.

Ambiguous duplicates stay unresolved until evidence justifies merging.

## 5. Provenance contract

Provenance must preserve:

1. **identity and access**: what was actually inspected;
2. **locatable support**: where the support appears;
3. **attribution**: source assertion, bounded observation or generated analysis;
4. **context**: conditions, population, period, units, qualifiers;
5. **transformations**: OCR, translation, filtering, calculation or other material change;
6. **revisions**: old basis and reason for material change;
7. **responsibility**: useful actor/tool/reviewer role without unnecessary personal data;
8. **origin/dependence**: known upstream source and evidence-unit relationships;
9. **selection**: consequential inclusion/exclusion and criteria;
10. **bounded preservation**: enough authorised support for audit without copying restricted/private works into public artefacts;
11. **integrity limits**: hashes prove byte identity, not truth, rights or event authenticity;
12. **untrusted source content**: source instructions never grant tool authority.

Locator expectations:

| Material | Locator |
|---|---|
| Web/document prose | representation/version, section/heading and distinguishing passage |
| PDF/report/book | edition, page scheme, section/table/figure |
| Repository/code | repository, immutable ref, path and lines/symbol |
| Dataset/calculation | edition/snapshot, columns/rows/filter, units and transformation inputs |
| Image/video/audio | file identity and region/frame/time interval |
| Private source | authorised stable reference and permissible local locator |
| Abstract/snippet | the abstract/snippet itself, never unseen full text |

## 6. Source quality

Quality is claim-relative. Assess applicable dimensions separately:

- directness;
- authority/expertise;
- methodological quality;
- transparency;
- recency/temporal validity;
- independence;
- conflicts/incentives;
- specificity to the claim;
- stability/archivability.

Do not produce one universal source score.

A source can be poor for one inference but authoritative for its own version number or announcement. An old source can be correct for a historical question.

## 7. Uncertainty and support

### 7.1 Support state

Useful support states are:

- **supported**: the claim as worded is supported;
- **qualified**: only a narrower/conditional proposition is supported;
- **contested**: material conflict remains unresolved;
- **unsupported**: current evidence does not justify assertion;
- **unassessed**: support has not been substantively checked.

A report must not assert unsupported or unassessed material claims as established. Contested claims retain the disagreement. Qualified claims carry the qualifier into final prose.

### 7.2 Review state

Review state is separate from support:

- unchecked;
- checked;
- needs-recheck.

Changed source content, material claim wording or required premise can invalidate an earlier review.

### 7.3 Uncertainty

Confidence is explained through source quality, coverage, independence, applicability, agreement and gaps. No generic probability is inferred from model confidence or source count.

Missing, null, negative and contrary evidence remain distinct:

- a failed search is not universal absence;
- inaccessible evidence is not a null result;
- adverse evidence is not an exclusion reason;
- “no contradiction found” is bounded by the actual search.

## 8. Temporal semantics

Track only the dates that materially apply:

- event/observation date or period;
- publication date;
- effective date/interval;
- retrieved-at date;
- valid-as-of context.

Use the source's actual precision. Do not invent timestamps for day-only or year-only dates.

A later retrieval does not advance valid-as-of. A future effective date remains future until operative. A newer unofficial source does not automatically supersede an older authoritative one.

## 9. Artefact contracts A01–A11

| ID | Responsibility | Authority and update rule |
|---|---|---|
| A01 Research brief | Authorised question, scope, restrictions and intended use. Material changes require the appropriate owner and dependent review. |
| A02 Plan/search record | Method, source strategy, criteria, bounded effort and actual searches. Planned and performed work stay separate. |
| A03 Source register | Source/version/access/selection/origin relations. Changed material versions do not silently replace prior evidence. |
| A04 Evidence records | Faithful, locatable source-supported observations/extractions. Changed extraction reopens dependent claims. |
| A05 Claim/support record | Proposition, support, contrary evidence, premises, applicability and support state. It is the authority behind claim-source views. |
| A06 Contradictions/alternatives | Material conflicts, checks and reconciliations. Resolved conflict is not erased from history. |
| A07 Gaps/follow-up | Missing knowledge, access, coverage, appraisal, permission or review plus actual attempts. Attempted is not resolved. |
| A08 Synthesis/recommendations | Evidence integration and separate recommendation conditions. New factual bridges become claims. |
| A09 Report/delivery | Exact audience-facing revision, scope, citations, limitations, temporal basis and issue/delivery state. |
| A10 Material provenance | Material transformations, input revisions, parameters and outputs. No universal telemetry log required. |
| A11 Evaluation/decisions | Exact target revision, criterion, reviewer/process, result, defects, limitations and repair route. Historical reviews remain identifiable. |

The compact form can place these in one `research.md`. Expanded work can split them into separate files. Empty files are never required merely to mirror this table.

## 10. State semantics

Do not conflate:

- research activity state;
- brief authority;
- source selection;
- source access;
- claim support;
- review state;
- issue state;
- delivery state;
- outstanding operation/resource state.

A completed tool call is not completed research. A checked claim is not necessarily supported. A generated report is not necessarily issued. A delivery attempt is not necessarily confirmed.

## 11. Contradictions and gaps

A contradiction record identifies:

- affected claims/evidence;
- common context under which they conflict;
- possible population, method, definition, time or scope differences;
- checks performed;
- reconciliation or unresolved outcome;
- consequence for final wording and confidence.

A gap record identifies:

- affected question/claim;
- gap type;
- material consequence;
- evidence or decision required;
- owner;
- proposed bounded action;
- actual attempt;
- state: open, attempted, resolved-with-evidence or accepted-limitation.

A gap closes only through evidence or an explicit authorised limitation decision.

## 12. Synthesis and handoff

Synthesis maps questions to supported findings, competing explanations, assumptions, limitations and overall applicability.

Recommendations remain separate and identify:

- supporting claims;
- value assumptions;
- alternatives;
- conditions that could reverse the recommendation;
- decision owner.

A downstream handoff provides:

- exact report revision;
- source/evidence access or permissible references;
- unresolved gaps;
- temporal basis;
- review status;
- assumptions;
- change triggers.

The receiving Production Skill owns how that evidence is applied in its domain.

## 13. Failure taxonomy and repair

The canonical diagnostic classes remain F01–F20:

| ID | Failure | Primary repair direction |
|---|---|---|
| F01 | Question displacement | Correct the brief and only affected downstream work. |
| F02 | Coverage inflation | Complete justified search or narrow the coverage claim. |
| F03 | Search invisibility | Recover search provenance or rerun the missing bounded search. |
| F04 | Access laundering | Correct actual access and obtain original support if required. |
| F05 | Unit inflation | Restore representation/report/unit identity and dependent counts. |
| F06 | False corroboration | Restore origin dependence and seek truly independent support only if required. |
| F07 | Context loss | Restore population/time/unit/caption/qualifier context. |
| F08 | Appraisal mismatch | Add appropriate specialist appraisal or narrow the inference. |
| F09 | Selective-result bias | Restore eligible adverse/null evidence and recompute impact. |
| F10 | Synthesis mismatch | Separate incompatible quantities or use a justified synthesis method. |
| F11 | Significance counting | Return to effect estimates/direction/precision rather than favourable-test counts. |
| F12 | Uncertainty collapse | Split known, inferred, assumed and unresolved content. |
| F13 | Identity/preservation confusion | Reopen unsupported authenticity/event inference while retaining valid bytes/provenance. |
| F14 | Temporal substitution | Correct time labels and recheck affected currentness. |
| F15 | Blind-spot reinforcement | Surface the material challenge to the requester without silently rewriting scope. |
| F16 | Assurance theatre | Perform the missing competent review or disclose that it is absent. |
| F17 | Authority/privacy overreach | Stop unauthorised action, protect evidence and return to the owner. |
| F18 | Silent revision | Preserve change history and affected recipients/reviews. |
| F19 | Deliverable invalidity | Reassess fitness for the intended decision/use. |
| F20 | Method-label inflation | Relabel honestly or execute the missing method. |

Diagnose upstream defects first. A prose rewrite cannot repair a false evidence relationship.

## 14. Repair routes

Repair sequence:

1. identify the observed defect and exact target revision;
2. classify the owning responsibility;
3. trace material dependencies;
4. preserve unaffected verified records;
5. re-enter the smallest owning operation;
6. execute the bounded repair;
7. update dependent claims/synthesis;
8. re-review changed scope;
9. issue a new report revision only when required gates pass.

Typical re-entry:

| Defect | Re-enter |
|---|---|
| Wrong question/scope | W01 |
| Wrong method/source strategy | W02 |
| Missing or biased source discovery | W03 |
| Bad extraction/representation | W04 |
| False independence, unsupported inference, contradiction handling | W05 |
| One unresolved evidence gap | W06 |
| Unsupported synthesis/citation wording | W07 |
| Wrong audience/delivery state | W08 |

When dependency scope is uncertain, expand the review rather than claiming a falsely narrow repair.

## 15. Refresh semantics

A refresh:

1. reads the last accepted report and support;
2. classifies the change trigger;
3. identifies affected claims/source classes;
4. reuses still-authorised stable evidence;
5. acquires the smallest necessary delta;
6. updates support, contradictions, uncertainty and temporal basis;
7. rechecks affected reviews and handoffs.

A changed brief is not disguised as a routine refresh. A source relocation can be a locator-only repair. A retraction can require broad reconsideration. “No material change found” states the actual update scope, not global absence.

## 16. Cross-domain handoffs

| Consumer | Deep Research provides | Consumer retains |
|---|---|---|
| Software Engineering | Technical evidence, constraints, comparisons, unresolved risks. | Architecture, implementation, performance and shipping decisions. |
| UI/UX Design | Existing human-science/interaction evidence and applicability limits. | Design choices and actual user-research conclusions. |
| Game/world production | Real-world mechanisms, uncertainties and competing interpretations. | Simulation design, game mechanics and claims about emergent simulated behaviour. |
| Narrative/Video/Music | Traceable references and context. | Creative decisions, asset production and rights clearance. |
| Business/Advertising | Market, competitor, problem and claim-support evidence. | Strategy, offers, commercial commitments and advertising approval. |
| Legal/medical/financial/policy | Bounded source research and exact unresolved questions. | Professional or regulated judgement and consequential action. |

Cross-domain feedback may identify a research defect. It does not grant permission for research to alter the consumer's approved decision.

## 17. Acceptance

An implementation conforms to this workflow specification when it can demonstrate:

- a question-to-evidence-to-claim-to-synthesis path;
- actual source access and provenance;
- non-inflated source independence;
- explicit contradictions and gaps;
- qualified uncertainty and temporal scope;
- bounded follow-up;
- separate review and support states;
- exact report revision and handoff;
- smallest-sufficient repair;
- preservation of valid prior evidence.

No single file layout, database, agent topology or orchestration engine is required to meet this contract.
