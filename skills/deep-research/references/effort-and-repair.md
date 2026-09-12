# Effort, stopping and repair

Contents: Effort, cost and stopping policy; Refresh policy; Refresh trigger classification; Failure taxonomy and repair; Repair routes; Refresh semantics.

## Effort, cost and stopping policy

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

### Stopping

Stopping and evidence sufficiency are different judgements.

Research may stop as **sufficient** when the question is supported to its required level, material contradictions and gaps are handled, mandatory review is complete and additional retrieval is unlikely to change the answer materially.

Research may stop as **limited** when a resource, access, method or authority boundary prevents further work but the brief permits a limitations outcome.

Research is **blocked** when an unresolved prerequisite, owner decision, mandatory source or mandatory review is required.

A low-yield search alone does not establish sufficiency. A hard cap cannot turn an incomplete method into an exhaustive one.

## Refresh policy

A refresh reassesses whether an existing deliverable remains fit for its stated use.

Triggers include:

- a later valid-as-of requirement;
- new eligible evidence;
- a correction, retraction or extraction defect;
- a changed question or use;
- source relocation or changed access;
- a bounded update search finding no material change.

Refresh the smallest affected evidence and dependency scope. Preserve historical findings that remain true for their old context. Do not advance valid-as-of merely because a source was re-read.

## Refresh trigger classification

| ID | Trigger | Minimum justified response |
|---|---|---|
| U01 | The consumer asks for a later valid-as-of state or the planned freshness boundary is reached. | Inspect the required changing source/version or relevant update channel; retain verified stable historical claims. The check date is not automatically the new validity date. |
| U02 | New eligible evidence or a newly accessible original may affect a material claim. | Triage relevance and origin, then acquire only the needed support; re-evaluate dependent claims, uncertainty and any affected source coverage. |
| U03 | A correction, retraction, failed extraction or source-integrity concern appears. | Investigate the defect and its dependency scope promptly within authority; distinguish an erroneous extraction from an invalid source or changed applicability. |
| U04 | The question, population, criteria, method or downstream use materially changes. | Reopen the brief/method decision. Reuse applicable evidence, but do not label a fundamentally different task as a routine refresh or silently apply obsolete eligibility. |
| U05 | An unchanged source moves or access/retention permissions change. | Repair the locator/access record and check permitted use; unchanged byte content need not be re-analysed solely because the URL moved. Lost evidence can reduce auditability. |
| U06 | No material new information is found in the defined update search. | Record the actual scope and date of the check and the unchanged findings. Do not claim a global absence of new evidence or silently strengthen confidence. |

Select the trigger's smallest evidence unit and follow the local evidence-contract dependency rules through claims, synthesis, report and review. If dependencies are uncertain, expand the relevant review boundary explicitly. A shared denominator, eligibility change or flawed original method can require a broad rerun; preservation protects valid work, not an artificially narrow correction.

## Failure taxonomy and repair

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

## Repair routes

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

## Refresh semantics

A refresh:

1. reads the last accepted report and support;
2. classifies the change trigger;
3. identifies affected claims/source classes;
4. reuses still-authorised stable evidence;
5. acquires the smallest necessary delta;
6. updates support, contradictions, uncertainty and temporal basis;
7. rechecks affected reviews and handoffs.

A changed brief is not disguised as a routine refresh. A source relocation can be a locator-only repair. A retraction can require broad reconsideration. “No material change found” states the actual update scope, not global absence.
