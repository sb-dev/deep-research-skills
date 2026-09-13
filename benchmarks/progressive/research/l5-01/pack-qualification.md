# Archival pack qualification and consolidated draft proposal

Revision r2, 2026-09-13. Operation: research-extension-pack-creator, **create-pack**, executed from the authorised source checkout. Qualification and a proposed reusable design are complete as a draft. No Extension Pack was activated during L5-01; no new production bundle, repository scaffold, installation, catalogue mutation or behavioural acceptance is claimed.

## Catalogue-first decision

The explicit initial catalogue is [the snapshot at 30c14c5b0dd22d5a63ce875f12ad7b0528183b35](https://github.com/sb-dev/deep-research-skills/blob/30c14c5b0dd22d5a63ce875f12ad7b0528183b35/docs/research-logs/2026-09-10-stage-11-profiles.json). Initial acquisition was recorded before archival collection in research.md r1; the full local snapshot was reread during completion. It contains only the following two profiles. This decision concerns that explicit snapshot, not every possible catalogue or today's separate implementation work.

| Alternative | Actual scope and maturity in supplied snapshot | Qualification |
|---|---|---|
| scholarly-evidence 0.0.1 | Bounded scholarly questions, report/work/version linkage and design-specific appraisal. Core contract stage-10-2026-09-10; design profile, source-backed procedural demonstration, not installed. | Reject as the archival default. Study/report linkage is useful for a later scholarship subinvestigation, but does not specify archival context traversal, record-status appraisal or catalogue-to-representation relations. Do not relabel it as an archival pack. |
| open-source-ecosystem 0.0.1 | Repository revision, licence, code/package/maintenance evidence and documented-versus-executed distinctions. Same core contract and design maturity. | Reject for archival evidence production. It may fit a separately scoped software adoption investigation; that does not answer the archival method need. |
| Core plus project instructions | Core already requires provenance, access, uncertainty, bounded search, source independence and review. | Adequate for this single programme; actually used here. Keep case facts, chosen archive, rights decisions and personal preferences in the project. Do not create a pack merely to restate core safeguards. |
| Repair core | Generic failure to preserve unknowns, access depth, evidence links or revisions | A general defect belongs in core repair, not an archival workaround. No core change is proposed in this task. |
| New reusable archival specialisation | Creator/function/hierarchy traversal, archival evidence units, representation and custody appraisal, differentiated missingness | **Justify a labelled draft proposal**, conditional on differential evidence. The reusable addition is a specific procedure for planning/discovery/extraction/appraisal across archival questions, rather than a source list or a ban on unsupported claims. |

The new-pack hypothesis is C11 in [research.md](research.md): recurrent archival questions benefit from this procedure. The underlying method distinctions are supported; recurrence, effectiveness and improvement over an explicit core prompt remain unmeasured. If a fair comparison finds core plus brief equally effective, or the procedure only fits this one institution, reject the standalone pack or retain it as project instructions. Catalogue absence proves only absence from this snapshot; it is not evidence of a historical event's nonoccurrence.

## Draft identity, boundary and method basis

This one document consolidates identity, procedural rules, method references, showcase and evaluation responsibilities. It is a reviewable design proposal, not a machine-loadable `pack.json` bundle. It may be promoted to the production form only by a separately authorised packaging and acceptance operation.

| Contract field | Proposed value |
|---|---|
| format_version; id; version | 1; archival-context; 0.1.0-draft.1 |
| core_contract | Source-read deep-research contract 0.1; compatibility target only. No installed compatibility test and no assertion that the supplied stage-10 profiles use this version. |
| status | Designed as a consolidated proposal. Procedure-demonstrated: no. Installed-tested: no. Behaviourally evaluated: no. Catalogue-ready: no. |
| purpose | Reusable research of archival questions where creator/custody/arrangement context and accessed representations materially affect discovery and inference. |
| not_for | Universal archival standard; preservation system; automated event authentication; legal clearance; professional certification; OCR engine; automatic absence proof; architecture or UX ownership. |
| activation | Explicit selection of archival-context 0.1.0-draft.1 and readable compatible rules only. Topic similarity or this proposal's existence never activates it. Missing/incompatible selection stops the affected run. |
| precedence | Authorised explicit research instructions, then approved/locked decisions, then selected pack, then core defaults. Permissions, evidence truthfulness, security/privacy and required review are invariant. Ambiguous lock conflict returns to its owner. |
| composition | One profile per investigation. Split scholarly or software-adoption subinvestigations with explicit handoffs; otherwise prove compatibility or return a scope conflict. No silent merge. |
| preserved | Research purpose, source/processor authority, bounded effort, evidence/claim separation, access depth, uncertainty, source dependence, valid revisions, repair ownership, independent and specialist review. |
| entry_points | This document is the sole proposal entry. Any future bundle must use pack-root-local relative entries without traversal, external symlinks, executable load steps or hidden repository dependencies. External method URLs are evidence, not automatic network instructions. |
| dependencies | None required for qualification. Future research uses already-authorised source/file tools only; specialist reviewers are explicit review needs. No paid agent, account, automatic retrieval, install or private evidence dependency. |

Method references are the actually inspected originals recorded as S1–S9/E1–E9 in research.md. In particular: [TNA Discovery guidance](https://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/understanding-your-search-results/) §§2–3/6 supports contextual discovery and imperfect keyword coverage; [TNA digital practices](https://www.nationalarchives.gov.uk/professional-guidance-and-services/cataloguing-practices/digital-cataloguing-practices/) Digital records, Custodial History and Series level description supports institutional representation/context distinctions, with its explicit March 2017 basis. [NARA catalogue guidance](https://www.archives.gov/research/catalog/help/using) supplies a second institutional setting. These do not establish a universal cross-archive mapping.

For the absence procedure, [TNA Misfiled items](https://www.nationalarchives.gov.uk/about-us/how-we-work/transparency/misfiled-items/) supplies source-specific status/date semantics; do not generalise one institution's labels. For transformations, [W3C PROV-DM](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) supplies a vocabulary candidate, not historical proof. The [Primer](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/) remains an informative Note. [NARA permissions](https://www.archives.gov/research/still-pictures/permissions) and [TNA copyright terms](https://www.nationalarchives.gov.uk/terms-and-conditions/copyright/) motivate separate use decisions; a pack cannot issue them.

Proposed research grammar: a collection/series description contextualises a record; a catalogue description describes a record; a permitted image/copy represents it; a transcription or extract derives from an identified representation; a claim uses one or more evidence observations. Creator, holder, cataloguer, transformer and reviewer are distinct responsibilities. These proposed relations require evidence and may remain suspected or unknown; shared titles, URLs or bytes do not establish common historical origin. No unseen catalogue item is used as a worked example here.

## Eight dimensions and operational changes

| Dimension | Changed or unchanged, and why | Observable effect |
|---|---|---|
| Source ecology | Changed: identify institution-native collection/series/record references, creators, holders, descriptions and representations before treating retrieved pages as evidence units. | A source record says what unit was inspected and what context is still missing. |
| Search strategy | Changed: plan a bounded creator/function/context traversal alongside keywords; log search vocabulary and variants, scope and date; check local catalogue semantics. | Search can follow a relevant series despite a name not appearing in a description; no invented live search results. |
| Inclusion/exclusion | Changed: include relevant finding aids/context and adverse record-status evidence; keep unavailable candidates distinct from irrelevant ones. | A restricted or empty item remains a documented access gap instead of disappearing from the search account. |
| Source appraisal | Changed: ask how creation purpose, custody, arrangement, selection and description/representation changes bear on this inference. | An appraisal points to evidence and uncertainty rather than calling every archival source authentic or independent. |
| Research methods | Changed: construct one context-and-representation chain for each consequential claim; diagnose search/description/access/survival alternatives separately. | A scanned page and its transcription are related representations, not two corroborating witnesses. |
| Synthesis structure | Changed: combine findings with context, representation/access basis, rival interpretation and bounded missingness account when relevant. | Reader sees the evidential path and the limit of an absence statement. |
| Quality criteria | Changed: add archival relationship, missingness, date-semantic and competent-interpretation checks. | A claim based only on an unseen original fails its specialised support criterion. |
| Reporting conventions | Changed: preserve source-native references, description level, inspected page/region, representation and status date. | Citation returns to the actual evidence; no universal hierarchy or calibrated confidence score is implied. |

Proposed rules by operation:

1. **plan:** identify the historical/research question, expected record creators/functions, likely custodians, evidence units and required expertise. Allocate finite keyword/context-route effort and reserve review. A project may restrict this plan; the pack supplies no new authority.
2. **discover:** inspect the eligible finding aid and context before selecting lower-level records. Record route, terms, filters and inspected boundary. If keywords fail, take one authorised context/variant route when it can discriminate a gap; stop at the cap.
3. **extract-evidence:** preserve description-versus-record identity, native references, access depth, page/region, context, known custody, representation and transformations. If the original is unavailable, limit evidence to the representation actually inspected.
4. **analyse-evidence:** relate representations before counting support; identify the evidential basis for custody/derivation links. Classify a negative observation at the narrowest justified level. Examine competing interpretations and source-selection effects; escalate consequential expert judgement.
5. **follow-up-search:** choose one discriminating unresolved alternative, such as spelling/description coverage versus recorded closure; acquire only the permitted source needed. A failed retry does not establish loss, destruction or event absence.
6. **synthesise:** retain context, representation, uncertainty and use limits with each consequential conclusion. Deliver owner questions, not automated professional approval.
7. **refresh:** a changed description or corrected transcription reopens affected claims and review only; preserve prior representation and unaffected evidence. A status change does not rewrite historical access facts.
8. **audit:** the separate evaluator checks these specialised rules on the fixed submission as well as all core obligations. This proposal cannot review itself into acceptance.

## Exact showcase and comparison requirements

Premise: a research team needs a lawful archival discovery plan before investigating a claim about a public administrative decision. The task deliberately has no successful item-level original. The candidate must preserve that limit while providing a useful plan. Method evidence is real-source; no historical event result is synthetic evidence.

Use the following exact prompt for the proposed pack condition after making this readable compatible draft available through an authorised route. It does not authorise installing anything:

```text
Use deep-research. Explicitly select archival-context 0.1.0-draft.1, using the consolidated rules in pack-qualification.md; stop if that exact draft is unavailable or incompatible. Research how to investigate whether a public administrative decision appears in an archive. Do not assert that any particular decision occurred or did not occur.

Use only these public method sources: https://www.nationalarchives.gov.uk/help-with-your-research/discovery-help/understanding-your-search-results/ ; https://www.nationalarchives.gov.uk/professional-guidance-and-services/cataloguing-practices/digital-cataloguing-practices/ ; https://www.nationalarchives.gov.uk/about-us/how-we-work/transparency/misfiled-items/ ; https://www.archives.gov/research/catalog/help/using ; https://www.w3.org/TR/2013/REC-prov-dm-20130430/ . Inspect the relevant source passages. No item-level original is supplied. An attempted catalogue page with no returned content is unavailable, not an inspected record. The locked scope is public guidance only; do not fetch private or paid material, contact people, create accounts, or make a historical event finding.

Write showcase-research.md containing the question and bounded search plan, source/representation and context distinctions, evidence-linked claims, alternative explanations for unsuccessful discovery, a proposed next archival investigation, and expert review needs. Preserve actual source access, source dates, performed versus proposed work and any conflicting guidance. Do not design software or UX. Allow at most 10 source actions, including repeats and failures, and no search queries beyond this fixed universe. Stop and report any mandatory inaccessible source; reserve finalisation effort. Return the actual file and truthful review status. Do not claim independent or professional approval.
```

The core condition uses that exact same prompt except the first paragraph is exactly:

```text
Use deep-research with no Extension Pack selected. Research how to investigate whether a public administrative decision appears in an archive. Do not assert that any particular decision occurred or did not occur.
```

Fix both conditions' core revision, source universe and captured versions, unavailable-item fact, question, downstream purpose, source/processor authority, locked scope, output purpose and 10-action cap. Execute separately without other-condition outputs or expected answers. Keep actual queries/actions, results and file revisions. Review fixed outputs separately; unchanged basic safeguards do not count as added value. Prespecify the intended difference as contextual search route selection, concrete archival appraisal and differentiated missingness, with no unsupported historical conclusions or authority regressions. Include a stronger core-plus-project-instructions comparison if needed to decide whether packaging adds reusable value.

Actual status: **neither condition executed for this draft; no differential outputs, scores, install/load results or qualified reviewer verdict exist**. L5-01 itself is a core-only programme run and is not this prespecified showcase. Budget for future comparisons requires separate allocation; none is charged to this completed producer run. A one-pair procedure demonstration would still not establish causal superiority or broad maturity.

| Required behavioural case | Evidence an independent evaluation must observe |
|---|---|
| 1 Explicit compatible activation | Exact draft identity/rules applied to intended scope; installed claim absent unless separately proved. |
| 2 No selection/core only | No automatic archival pack activation from topic or file presence. |
| 3 Unknown/incompatible selection | Visible selection blocker; no silent substitution. |
| 4 Explicit source restriction | Guidance-only scope defeats any pack suggestion to acquire a record. |
| 5 Locked decision | Locked public-only boundary remains intact. |
| 6 Ambiguous instruction/lock conflict | Candidate asks the responsible owner instead of silently reopening approved work. |
| 7 Multi-pack scope conflict | Candidate proves compatibility, splits authorised subinvestigations or returns a scope choice. |
| 8 Cosmetic-only candidate | Additional headings or archive vocabulary alone cannot pass the added-value criterion. |
| 9 Specialist units/relations | Description, record, image and transcription remain distinct with justified relationships and no inflated corroboration. |
| 10 Insufficient access/method transfer | Empty catalogue result cannot supply unseen content; institutional method does not become universal practice. |
| 11 Rights/source status | Open description or accessible image does not become blanket clearance; missing/placeholder date remains correctly qualified. |
| 12 Static evidence versus actual test | Written query plan or provenance schema does not become executed search, authenticated record or conformant implementation. |
| 13 Scoped correction/deactivation | A corrected transcription invalidates affected support only; deactivation preserves earlier record of the pack actually used. |
| 14 Unsafe load/path | Traversal, external symlink, undeclared dependency or load-time side effect is rejected before use. |
| 15 Evaluator mutation/stale verdict | Evaluator writes review separately; changed output cannot retain an earlier passing verdict automatically. |
| 16 Specialist overreach | No software/UX takeover, legal clearance or professional authenticity certification. |

Before acceptance, the evaluator and archival specialist must fix meaningful positive/negative fixtures, competence requirements and review criteria, inspect actual paired results and check regressions. Do not expose private project evidence in reusable fixtures. Failed specialisation changes are repaired narrowly under a new draft revision; if changes only compensate for core defects, return them to core rather than promoting this pack.

## Authoring return

Completed: catalogue inspection; alternatives/rejection/reuse reasoning; source-backed specialist qualification; proposed boundaries, eight dimensions, command effects, precedence and invariants; exact showcase; explicit comparison and negative-case requirements. The consolidated draft can be reviewed now.

Not completed or claimed: production packaging, actual core-versus-pack application, compatible installed loading, behavioural acceptance, expert method approval, catalogue readiness or publication. The pack maintainer owns any authorised next packaging/revision; a separate evaluator owns comparative judgement. No additional production pack should be accepted on this proposal alone.
