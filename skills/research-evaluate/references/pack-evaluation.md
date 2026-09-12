# Pack-aware evaluation

Contents: Pack dimensions; Activation; Precedence; Composition; Path and load safety; Differential evaluation; Pack-aware evaluation ownership.

## Pack dimensions

Each pack must address all eight dimensions, marking unchanged dimensions explicitly with a reason.

| Dimension | What a pack may change | What remains invariant |
|---|---|---|
| Source ecology | Specialist corpora, identifiers, evidence units and source classes. | Source/processor authority, direct-evidence preference, actual access and provenance. |
| Search strategy | Vocabulary, citation chaining, corpus strategy and temporal search. | Question-relative scope, actual search records, finite effort. |
| Inclusion/exclusion | Specialist eligibility criteria. | Adverse/null evidence cannot be excluded merely for polarity; unavailable differs from ineligible. |
| Source appraisal | Method-specific quality and status checks. | No universal source truth score, prestige shortcut or invented expert review. |
| Research methods | Specialist relationships, analysis and comparison. | Source statement, transformation and interpretation remain distinct. |
| Synthesis structure | Context-appropriate grouping and reporting. | Answer the actual question, retain contradictions and uncertainty. |
| Quality criteria | Additional specialist pass/fail requirements. | Core mandatory failures cannot be averaged away. |
| Reporting conventions | Specialist identifiers, terminology and declared method. | No certification of unperformed research, review, execution or rights clearance. |

A pack can qualify through one material dimension when that change is sufficiently reusable and observable. Cosmetic formatting alone never qualifies.

## Activation

Pack activation is explicit.

A pack is **not** activated by:

- topic similarity;
- filename;
- pack presence on disk;
- catalogue inspection;
- a model deciding that the pack looks useful.

A research run records:

- selected pack ID;
- version/content identity;
- compatible core contract;
- scope of activation;
- any explicit override;
- source/processor restrictions that continue to apply.

Requested but unavailable/incompatible packs produce a visible blocker for that selection. They are not silently ignored or replaced.

## Precedence

The common precedence is:

```text
explicit research instructions
→ approved / locked research decisions
→ selected Extension Pack
→ core Deep Research defaults
```

Permissions, truthful evidence, security, privacy and required review are not weakenable defaults.

For one decision field:

1. use an authorised explicit value if present;
2. otherwise preserve the applicable locked decision;
3. otherwise apply selected pack behaviour;
4. otherwise use core defaults.

An ambiguous conflict with a locked decision returns to its owner. A pack never reopens approved work by itself.

## Composition

The initial composition model selects one profile per investigation.

Distinct subinvestigations can use different packs with explicit handoffs. If two packs are requested for one investigation:

- prove their rules are compatible for the same scope; or
- split the investigation into explicit subscopes; or
- return a conflict requiring a scoped choice.

There is no silent last-loaded-wins merge and no universal cross-domain pack interpreter.

Historical reports retain the pack identity actually used. Later pack changes do not retroactively reclassify earlier work.

## Path and load safety

Relative paths resolve against the known pack root.

Reject:

- absolute paths;
- path traversal;
- symlinks escaping the pack root;
- undeclared repository-root dependencies;
- load-time executable scripts;
- automatic network calls;
- automatic credential acquisition;
- private project evidence in reusable pack references.

Installing or reading a pack must not mutate research state.

External URLs in method references are evidence links, not implicit execution.

## Differential evaluation

Every catalogue pack compares:

```text
core
vs
core + pack
```

Fix within a pair:

- question;
- source universe;
- downstream use;
- authority;
- output purpose;
- core invariants.

A pack survives only if it changes an intended research operation or criterion without unacceptable regressions.

Required cases include:

1. explicit compatible activation;
2. no selection/core only;
3. unknown/incompatible pack;
4. explicit source restriction overrides pack default;
5. locked decision overrides pack default;
6. ambiguous instruction/lock conflict;
7. multi-pack scope conflict;
8. cosmetic-only pack;
9. specialist unit/relationship case;
10. insufficient-access/method-transfer case;
11. specialist licence/readiness or source-status case;
12. static evidence requiring a real test rather than fabricated execution;
13. scoped correction/deactivation;
14. unsafe package path/load side effect;
15. evaluator mutation/stale verdict;
16. cross-domain or specialist overreach.

A model writing both conditions in one context can demonstrate procedural differences but not causal superiority.

## Pack-aware evaluation ownership

`research-evaluate` can load applicable pack criteria from an explicitly identified selected pack.

It must still:

- review fixed submission bytes;
- record exact pack version;
- separate core and pack criteria;
- keep stronger explicit instructions/locked decisions visible;
- avoid silently repairing pack or research content;
- report inaccessible pack criteria as a limitation/blocker.

A pack cannot grade itself into acceptance.
