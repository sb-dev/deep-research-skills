# Pack differential evaluation contract

Contents: Differential evaluation; Pack-aware evaluation ownership; Case contract; Submission and review contract.

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

## Case contract

Every benchmark case records:

### Identity

- case ID and version;
- split: development, regression, teaching or hold-out;
- synthetic versus real-source character;
- owning layer/requirement;
- licensing/exposure limits.

### Task

- exact prompt;
- required output;
- intended use;
- mandatory subquestions;
- selected skills/commands/packs;
- prior approved decisions;
- allowed sources/processors;
- prohibited side effects.

### Evidence universe

- source identity/version;
- actual locators/access;
- snapshots where lawful;
- gold evidence where established;
- mutable-source mode;
- known unavailable material.

### Oracle

- atomic criterion ID;
- mandatory/optional state;
- expected behaviour/proposition;
- source/logic;
- tolerances if justified;
- disallowed behaviour;
- reviewer competence requirement.

The target model's self-verdict is never the oracle.

### Execution envelope

- bounded searches/reads/data/compute;
- parent aggregate;
- outstanding jobs;
- finalisation reserve;
- permitted retry/stopping behaviour.

### Repair contract

- defect;
- owning operation;
- expected affected dependencies;
- records that must remain unchanged;
- allowed new acquisition;
- recheck scope.

### Provenance

- case author/source inspection dates;
- source/corpus identities;
- case/oracle revisions;
- changes and rationale.

## Submission and review contract

A submission identifies:

- case/revision;
- candidate skill/repository commit;
- host/model/tool versions actually known;
- source/corpus identities;
- actual queries and relevant inspected sources;
- operation outcomes and limits;
- output paths/content identities;
- actual resource use and outstanding reservations where known;
- actual date precision.

A review identifies:

- exact submission revision;
- criterion;
- evidence;
- verdict;
- severity;
- assessed/unassessed scope;
- smallest repair;
- actual reviewer/process.

Evaluation does not silently repair its input.
