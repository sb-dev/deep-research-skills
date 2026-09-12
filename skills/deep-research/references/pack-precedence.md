# Optional pack selection and precedence

## Definition

A valid research Extension Pack must satisfy all of the following:

1. the specialist knowledge is reusable across projects;
2. it materially changes research behaviour;
3. putting it in core would add irrelevant specialisation to ordinary research;
4. a realistic example can demonstrate the difference;
5. evaluation can distinguish the intended specialised behaviour from core;
6. the specialised behaviour does not weaken core evidence, authority, uncertainty or repair invariants.

A project-specific brief, customer facts, source list, style note, provider preset or model configuration is not a pack.

If a proposed pack merely fixes a general core defect, repair core instead.

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
