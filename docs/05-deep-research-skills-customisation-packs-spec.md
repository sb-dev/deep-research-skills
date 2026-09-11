# Deep Research Skills Customisation and Extension Packs Specification

**Status:** Canonical design specification  
**Version:** 1.0  
**Date:** 11 September 2026  
**Implementation state:** Pack semantics specified. Two design profiles have source-backed procedural demonstrations; production pack bundles and clean installation are later stages.

## 1. Purpose

An Extension Pack is reusable specialist research knowledge that materially changes how Deep Research performs its discipline for a coherent context.

This specification owns:

- pack qualification;
- pack dimensions;
- activation and precedence;
- source/method specialisation;
- core-skill effects;
- packaging;
- compatibility and composition;
- pack-aware evaluation;
- pack authoring;
- showcase requirements;
- repair and versioning;
- boundaries and non-goals.

The initial curated entries are in [06 — Extension Pack Catalogue](06-deep-research-skills-extension-pack-catalogue.md).

## 2. Definition

A valid research Extension Pack must satisfy all of the following:

1. the specialist knowledge is reusable across projects;
2. it materially changes research behaviour;
3. putting it in core would add irrelevant specialisation to ordinary research;
4. a realistic example can demonstrate the difference;
5. evaluation can distinguish the intended specialised behaviour from core;
6. the specialised behaviour does not weaken core evidence, authority, uncertainty or repair invariants.

A project-specific brief, customer facts, source list, style note, provider preset or model configuration is not a pack.

If a proposed pack merely fixes a general core defect, repair core instead.

## 3. Pack dimensions

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

## 4. Activation

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

## 5. Precedence

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

## 6. Composition

The initial composition model selects one profile per investigation.

Distinct subinvestigations can use different packs with explicit handoffs. If two packs are requested for one investigation:

- prove their rules are compatible for the same scope; or
- split the investigation into explicit subscopes; or
- return a conflict requiring a scoped choice.

There is no silent last-loaded-wins merge and no universal cross-domain pack interpreter.

Historical reports retain the pack identity actually used. Later pack changes do not retroactively reclassify earlier work.

## 7. Core-skill effects

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

## 8. Pack package

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

## 9. Manifest contract

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

## 10. Path and load safety

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

## 11. Authoring workflow

Use `research-extension-pack-creator`, operation `create-pack`.

The canonical authoring workflow is twelve steps:

| Step | Responsibility | Completion evidence |
|---|---|---|
| A01 | Inspect catalogue | Actual IDs/versions/use cases/limits read. |
| A02 | Decide whether a new pack is justified | Reuse, core repair and new-pack alternatives compared. |
| A03 | Research specialist method/source ecology | Primary method evidence and limitations inspected. |
| A04 | Define boundaries and research grammar | Evidence units, permissible relationships, method and specialist limits specified. |
| A05 | Define changed core behaviour | Every change mapped to command/focus and observable effect. |
| A06 | Define pack-aware evaluation | Comparable tasks, invariants, intended differences and negative cases fixed before output. |
| A07 | Implement requested draft | Self-contained bundle written in authorised working area. |
| A08 | Create realistic showcase | Lawful evidence and specialist behaviour used. |
| A09 | Include exact generation prompt | Complete prompt has scope, pack selection, authority, output and evaluation. |
| A10 | Compare core versus core+pack | Both conditions actually executed under comparable inputs. |
| A11 | Validate | Structure, activation, precedence, fidelity, preservation, negative cases and requested acceptance state checked. |
| A12 | Catalogue | Catalogue status reflects actual evidence only. |

A valid request can finish at “reuse existing pack” or “new pack not justified”.

## 12. Showcase contract

Every implemented catalogue pack must include at least one showcase with:

- premise;
- pack-specific research constraints;
- exact copyable prompt;
- source boundary;
- selected pack identity/version;
- allowed tools/processors;
- stopping boundary;
- expected specialised behaviour;
- actual output/evaluation status;
- relevant evaluation priorities;
- explicit limitations.

A source-backed generated output stays distinct from the underlying evidence.

If the pack is not installed-tested, the showcase status must say so.

## 13. Differential evaluation

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

## 14. Pack-aware evaluation ownership

`research-evaluate` can load applicable pack criteria from an explicitly identified selected pack.

It must still:

- review fixed submission bytes;
- record exact pack version;
- separate core and pack criteria;
- keep stronger explicit instructions/locked decisions visible;
- avoid silently repairing pack or research content;
- report inaccessible pack criteria as a limitation/blocker.

A pack cannot grade itself into acceptance.

## 15. Repair and versioning

A material pack change to:

- method;
- source basis;
- precedence;
- compatibility;
- core command effect;
- evaluation interpretation;

requires a new identifiable pack revision and affected tests.

Smallest repair targets:

- defective rule;
- method reference;
- compatibility declaration;
- prompt;
- fixture;
- local path.

Preserve compatible accepted work. Repeat only affected activation/comparison/install checks.

A corrected pack does not retroactively validate research produced with an older revision.

## 16. Deferred families

The initial catalogue selects only two packs.

Deferred candidate families are:

- market-intelligence;
- technology-landscape;
- trend-and-signal;
- creative-reference-research;
- investigative-osint.

They are not available packs merely because they have names.

A deferred family may be reconsidered only when a real repeated use case demonstrates specialist behaviour not adequately expressed by core plus project instructions, and the pack can meet the qualification and differential-evaluation contract.

`investigative-osint` additionally requires a bounded legitimate source method, privacy/harm controls and an actual specialist/editorial review route before catalogue promotion.

## 17. Maturity states

Use separate evidence states:

- **designed**: complete reusable pack contract;
- **procedure-demonstrated**: source-backed core-versus-pack application exists;
- **installed-tested**: production pack bundle successfully loads/activates from intended installation;
- **behaviourally evaluated**: fresh representative differential cases pass;
- **catalogue-ready**: required showcase, evaluation and packaging evidence is complete.

These do not imply repository-wide `working`, `benchmarked` or `mature` status.

## 18. Current state

The accepted initial profiles are:

- `scholarly-evidence`;
- `open-source-ecosystem`.

Both are designed and procedure-demonstrated on bounded public-source comparisons. They are not yet production pack bundles, clean-install tested or supported by a general improvement estimate.

Their full catalogue entries are in [06](06-deep-research-skills-extension-pack-catalogue.md).
