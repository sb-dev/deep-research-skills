# Research Extension Pack contract

Contents: Definition; Pack dimensions; Activation; Precedence; Composition; Core-skill effects; Pack package; Manifest contract; Path and load safety.

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

## Core-skill effects

A pack may specialise these `deep-research` operations:

- `plan`;
- `discover`;
- `extract-evidence`;
- `analyse-evidence`;
- `follow-up-search`;
- `synthesise`;
- `refresh`.

It may specialise `research-evaluate` criteria through `audit`.

A pack should not:

- invent new core authority;
- silently add paid providers;
- auto-contact sources;
- replace the fixed-input evaluator boundary;
- modify another skill package;
- create a new workflow runtime.

If a new operation is genuinely required, it must be justified against the core command contract rather than smuggled into pack data.

## Pack package

Target production form:

```text
extension-packs/<pack-id>/
├── pack.json
├── PACK.md
├── references/method.md
├── examples/showcase.md
└── evals/cases.json
```

Responsibilities:

- `pack.json`: identity, compatibility, activation and local entry points;
- `PACK.md`: procedural rules and changed command behaviour;
- `references/method.md`: source-backed specialist method knowledge and limits;
- `examples/showcase.md`: premise, exact prompt, expected behaviour and actual evaluation status;
- `evals/cases.json`: behavioural positive/negative cases and expected results.

Files can be consolidated only if these responsibilities stay unambiguous.

## Manifest contract

Required fields:

| Field | Contract |
|---|---|
| `format_version` | Pack format version. Unknown versions fail selection. |
| `id` | Stable lowercase-hyphen identifier. |
| `version` | Semantic content version. |
| `core_contract` | Compatible Deep Research core contract/version. |
| `status` | Separate designed, procedure-demonstrated, installed-tested and behaviourally evaluated states. |
| `purpose` | Coherent reusable use case. |
| `not_for` | Explicit exclusions. |
| `dimensions` | All eight dimensions with changed/unchanged rationale. |
| `effects` | Target command/focus, behavioural change and observable consequence. |
| `preserved` | Core evidence, authority, uncertainty, effort and repair invariants. |
| `method_sources` | Locatable source-backed specialist basis and limits. |
| `activation` | Explicit selection rule. |
| `precedence` | Stronger instructions/locked decisions. |
| `composition` | Compatibility/splitting rule. |
| `showcase` | Exact prompt, expected change and actual evaluation status. |
| `evaluation` | Required positive/negative behavioural cases. |
| `entry_points` | Pack-root-local files only. |
| `dependencies` | Explicit optional tools/services/processors when needed. |

Duplicate pack ID/version with different bytes is an integrity conflict requiring reconciliation.

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
