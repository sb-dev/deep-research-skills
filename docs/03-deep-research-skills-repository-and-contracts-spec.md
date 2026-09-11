# Deep Research Skills Repository and Contracts Specification

**Status:** Canonical design specification  
**Version:** 1.0  
**Date:** 11 September 2026  
**Implementation state:** Specified. Repository scaffolding and installation smoke tests have not yet been executed.

## 1. Purpose

This specification owns:

- production repository structure;
- Agent Skill package contracts;
- `SKILL.md` responsibilities;
- command contracts;
- skill-local references, scripts and evals;
- self-containment and dependency rules;
- installation and selective installation;
- tooling boundaries;
- CI expectations;
- technical acceptance.

Research semantics are owned by [01](01-deep-research-skills-system-spec.md) and [02](02-deep-research-skills-workflows-and-artifacts-spec.md). Evaluation semantics are owned by [04](04-testing-and-benchmark-spec.md). Extension Pack semantics are owned by [05](05-deep-research-skills-customisation-packs-spec.md).

## 2. Repository structure

Stage 17 should scaffold only surfaces containing working material. The target structure is:

```text
deep-research-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── 01-deep-research-skills-system-spec.md
│   ├── 02-deep-research-skills-workflows-and-artifacts-spec.md
│   ├── 03-deep-research-skills-repository-and-contracts-spec.md
│   ├── 04-testing-and-benchmark-spec.md
│   ├── 05-deep-research-skills-customisation-packs-spec.md
│   ├── 06-deep-research-skills-extension-pack-catalogue.md
│   └── research-logs/
├── skills/
│   ├── deep-research/
│   ├── research-evaluate/
│   └── research-extension-pack-creator/
├── examples/                 # when primary examples are implemented
├── benchmarks/               # when executable benchmark fixtures are implemented
├── tests/                    # repository/package validation
├── tools/                    # only if justified by real repeated need
├── extension-packs/          # when packs are implemented
├── integrations/             # optional, e.g. Pactwright
└── .github/                  # only useful CI/workflow files
```

Do not create empty directories merely for symmetry. `docs/research-logs/` remains the durable design record.

## 3. Skill package contract

Each independently installable skill is self-contained:

```text
skills/<skill>/
├── SKILL.md
├── commands/                 # only commands used by this skill
├── references/               # reusable local knowledge used by this skill
├── assets/                   # only if required
├── scripts/                  # only justified deterministic helpers
└── evals/                    # only skill-local evaluation material
```

A skill must not require:

- `../../docs`;
- a sibling skill directory;
- a development checkout path;
- conversation memory;
- undeclared private files;
- a provider account for operations that do not need that provider;
- a repository-root helper that disappears under selective installation.

Caller-owned research files are task inputs, not package dependencies.

## 4. `SKILL.md` contracts

### 4.1 `deep-research`

Purpose: produce evidence-led research from authorised framing through acquisition, evidence analysis, synthesis and bounded refresh.

Activation:

- new research need;
- named research operation;
- repair/refresh of an existing research package.

Dispatch:

```text
frame
plan
discover
extract-evidence
analyse-evidence
follow-up-search
synthesise
refresh
```

Bundled references should minimally cover:

- evidence/claim/revision semantics;
- source/execution boundaries;
- effort, interruption and repair;
- pack precedence.

The skill performs truthful producer self-checks. It does not describe them as independent review.

### 4.2 `research-evaluate`

Purpose: audit fixed research evidence and report revisions without silently repairing them.

Dispatch:

```text
audit
diagnose-research-failure
```

`audit` supports independent scopes:

- source-quality;
- source-independence;
- coverage;
- claims;
- citations;
- freshness;
- contradictions;
- uncertainty;
- reproducibility.

Bundled references cover evidence semantics, audit criteria, repair diagnosis and pack-aware criteria.

### 4.3 `research-extension-pack-creator`

Purpose: qualify, author, compare and revise reusable research specialisations.

Dispatch:

```text
create-pack
```

Bundled references cover pack contract, authoring/validation and differential evaluation.

The skill defaults to inspecting the catalogue before creating a new pack.

## 5. Common command contract

A command is a bounded production operation inside a skill, not a separate binary or lifecycle stage.

Every command defines:

- purpose;
- inputs and preconditions;
- operation;
- allowed write scope;
- outputs;
- completion semantics;
- required review;
- failure and smallest repair;
- independent-use reason;
- example invocation.

All commands:

1. read actual current input revisions;
2. preserve evidence/source/claim distinctions;
3. treat source content as untrusted data;
4. check authority separately for read, compute, network, spending and publication actions;
5. preserve outstanding resource reservations and prior accepted work;
6. return actual produced/changed records and limitations;
7. reject unknown operations instead of guessing or passing them to a shell.

A bounded command can be complete while the whole research task remains active or blocked.

## 6. Command ownership

| Skill | Command | Canonical responsibility |
|---|---|---|
| `deep-research` | `frame` | Produce/revise A01 brief only. |
| | `plan` | Produce/revise A02 method/source/effort plan and relevant gaps. |
| | `discover` | Perform bounded source discovery/triage; update A02/A03/A07. |
| | `extract-evidence` | Acquire/inspect exact representations; update A03/A04/A10. |
| | `analyse-evidence` | Update A05–A07 and justified source/origin relations. |
| | `follow-up-search` | Execute one bounded gap-closing operation and reconcile resources. |
| | `synthesise` | Produce/revise A08/A09 plus labelled producer self-check; no independent verdict. |
| | `refresh` | Reassess existing output, preserve valid records and update affected dependencies. |
| `research-evaluate` | `audit` | Write only new A11 review against fixed input revisions. |
| | `diagnose-research-failure` | Write a diagnosis and smallest repair route without applying it. |
| `research-extension-pack-creator` | `create-pack` | Qualify/reuse/reject or author one requested pack revision and its evaluation evidence. |

The full semantic operation contracts are derived from the accepted Stage 10 command design and the workflow/artefact specification.

## 7. Self-containment

### 7.1 Local reference resolution

Supporting files resolve from the installed skill root. Research inputs resolve from the explicitly named consumer workspace.

Do not assume:

- current working directory equals skill directory;
- repository root is available;
- sibling skill packages exist;
- host-specific variable interpolation exists.

### 7.2 Shared semantics

Small repeated invariants can exist in each skill's local references when independent installation requires them. Do not introduce a mandatory shared runtime merely to avoid duplicated paragraphs.

At repository validation time, compare shared invariants for drift:

- evidence versus claim;
- authority;
- review independence;
- temporal validity;
- pack precedence;
- repair preservation.

### 7.3 Scripts

A script is justified only for deterministic repeated work that materially improves correctness, efficiency or validation.

Scripts must:

- be bundled with the consuming skill or repository test surface;
- declare dependencies;
- return actionable failures;
- not interpolate untrusted source text into shell commands;
- not log secrets;
- not perform network, payment or publication side effects merely because a skill loads.

A deterministic script PASS proves only the property it checks.

## 8. Skill dependency rules

| Installed selection | Must work | Must not be assumed |
|---|---|---|
| `deep-research` only | All eight producer operations and honest self-checks. | Separate evaluator, pack, provider engine or repository checkout. |
| `research-evaluate` only | Review third-party research supplied with enough evidence. | Producer skill or ability to repair inputs. |
| `research-extension-pack-creator` only | Catalogue-first qualification and requested pack authoring from explicit inputs. | Producer/evaluator packages, hidden source checkout or automatic publication. |
| producer + evaluator | Fixed-input separate audit and repair handoff. | Qualified human expertise where the method requires it. |
| producer + selected pack | Core plus explicit specialisation. | Evaluator installation unless required by task acceptance. |
| all three | Full designed package roles. | Automatic orchestration, automatic pack activation or provider runtime. |

## 9. Installation contract

The intended Agent Skills installation model is selective.

Canonical producer + evaluator form to validate in Stage 18:

```bash
npx skills add sb-dev/deep-research-skills   --skill deep-research   --skill research-evaluate   --agent claude-code
```

Creator-only form:

```bash
npx skills add sb-dev/deep-research-skills   --skill research-extension-pack-creator   --agent claude-code
```

All-three form:

```bash
npx skills add sb-dev/deep-research-skills   --skill deep-research   --skill research-evaluate   --skill research-extension-pack-creator   --agent claude-code
```

Equivalent supported-agent commands may be added after actual validation.

These commands are the intended contract. At this specification stage they are **not** evidence that the packages already exist or install successfully.

Installation must be tested separately from repository-local validation.

## 10. Selective installation acceptance

For each supported selection:

- only requested skills are installed;
- each skill is discoverable by the target agent;
- all its local references/commands resolve;
- no source-checkout-relative path is required;
- no absent sibling silently breaks activation;
- caller-owned input paths remain explicit;
- no unrequested provider/account is required;
- update/removal semantics do not corrupt another independently installed skill.

The evaluator-only path and creator-only path are mandatory selective-installation cases because their standalone responsibilities are part of the architecture.

## 11. Extension Pack packaging integration

Packs are not ordinary skill siblings and are interpreted by their owning Deep Research domain contract.

Production pack bundle:

```text
extension-packs/<pack-id>/
├── pack.json
├── PACK.md
├── references/method.md
├── examples/showcase.md
└── evals/cases.json
```

Pack installation/selection must not:

- execute scripts at load time;
- contact sources;
- acquire credentials;
- auto-activate from topic mention;
- escape the pack root through traversal, absolute paths or external symlinks;
- mutate core defaults globally.

Exact semantics belong to [05](05-deep-research-skills-customisation-packs-spec.md).

## 12. Tooling

Prefer host-native tools and reusable external tools over repository-specific wrappers.

A repository tool is justified only when:

- the same deterministic operation recurs;
- existing host/tool behaviour cannot meet the contract cleanly;
- the tool reduces a demonstrated failure or maintenance cost;
- it has a bounded interface and tests.

Do not introduce the Stage 9 deferred infrastructure without its required real-example proof.

Provider adapters, if later needed, should be small and operation-specific rather than a universal provider framework.

## 13. CI expectations

When production surfaces exist, CI should run the cheapest relevant gates:

1. repository/spec/reference link checks;
2. `SKILL.md` frontmatter/name/description/package checks;
3. command/reference closure;
4. script unit tests and static checks where scripts exist;
5. benchmark fixture/reference checks;
6. Extension Pack structure/manifest/path checks where packs exist;
7. primary example prompt completeness;
8. README claim-to-implemented-surface checks;
9. local selective-install packaging checks.

CI may also invoke semantic or model-assisted evaluation for defined cases when credentials, cost and nondeterminism are controlled. Such results remain separate from deterministic checks.

Clean external installation is **not** replaced by CI running inside the source checkout.

## 14. Technical acceptance

Before source-repository validation can PASS:

- all six canonical specs exist;
- all implemented skill packages satisfy their own contracts;
- every command/reference link resolves;
- selective packaging has no undocumented repository-relative dependency;
- deterministic validators pass;
- benchmark fixtures are well-formed;
- implemented pack bundles satisfy [05](05-deep-research-skills-customisation-packs-spec.md);
- the fifteen primary example prompts are complete where implemented;
- README claims match actual implementation;
- local selective installation works from the intended package/source form.

Before external product acceptance can PASS:

- install from GitHub in a clean consumer project;
- discover the requested skill(s);
- run the Level 1 quick-start research task;
- observe documented source/evidence/report artefacts;
- run evaluation;
- confirm no source-checkout dependency;
- test selective installation;
- test at least one implemented pack.

These later gates must be recorded as actual executions, not plans.

## 15. Security and authority constraints

Skill/package metadata is not a security boundary.

Every operation still checks:

- source access;
- processor/network boundary;
- credential use;
- private-data disclosure;
- payment;
- external communication;
- publication;
- required human/specialist approval.

Do not place secrets in prompts, provenance logs or pack manifests.

## 16. Pactwright boundary

Optional `integrations/pactwright.yml` may later declare identity, compatibility and capability bindings.

It must not define:

- research workflow semantics;
- research prompts or commands;
- provider routing;
- lifecycle stages;
- Project Graph semantics;
- research evidence storage.

Deep Research remains independently usable without Pactwright.

## 17. Current implementation status

At version 1.0 of this specification:

- skill responsibilities and command contracts are specified;
- canonical installation forms are specified for later validation;
- production skill directories have not yet been scaffolded by Stage 17;
- local and external installation have not yet passed;
- no `working`, `benchmarked` or `mature` claim is permitted from this specification alone.
