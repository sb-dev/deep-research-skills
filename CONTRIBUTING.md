# Contributing

Read the [system](docs/01-deep-research-skills-system-spec.md), [workflow](docs/02-deep-research-skills-workflows-and-artifacts-spec.md) and [repository contracts](docs/03-deep-research-skills-repository-and-contracts-spec.md) before changing research behaviour. Keep the question, source, evidence, claim, synthesis and recommendation distinct.

## Where work belongs

| Surface | Responsibility |
|---|---|
| `skills/<skill>/SKILL.md` | Activation, boundaries and routing to local material |
| `skills/<skill>/commands/` | Bounded semantic operations, inputs, writes, review and repair |
| `skills/<skill>/references/` | Portable research knowledge used by that skill |
| `examples/level-<n>-<example>/README.md` | Complete public task prompt, expected artefacts and evaluation contract |
| `tests/` | Deterministic repository checks and their negative controls |
| `docs/` | Canonical design responsibilities |
| `docs/research-logs/` | Internal decisions, verification, claims evidence and execution records |

Add benchmark fixtures under `benchmarks/` when executable cases are implemented. Add real pack bundles under `extension-packs/<id>/` following the [pack contract](docs/05-deep-research-skills-customisation-packs-spec.md). Optional integration bindings belong under `integrations/`. Create these directories only when they contain useful material. Add `tools/` only for a demonstrated repeated need that existing tools cannot adequately satisfy.

## Make a bounded change

Read existing work and identify the owning command, reference or criterion. Preserve unaffected evidence and issued revisions. An evaluator writes a separate review against fixed inputs; it does not repair its own submission. Resolve required owner decisions before changing approved research or expanding authority.

Keep each skill self-contained. Supporting links resolve within the installed skill directory. Consumer research files and a supplied catalogue are explicit task inputs. A skill must not depend on sibling skills, repository-root documentation, private files or a mandatory provider account.

Keep public onboarding in the root README and public example pages. Preserve the complete quick-start prompt, five levels with three primary examples each, substantive skill sections and public link closure. Record bootstrap and maturity evidence internally.

## Run the repository checks

From the repository root, with Python 3.10 or newer and no third-party Python dependencies:

```bash
python3 tests/check_repository.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
git diff --check
```

The checks verify structure, prompt identity, link closure, package boundaries and preservation. They do not establish research quality, host discovery, successful installation or benchmark performance. Behaviour changes need actual source/input/output evidence and an appropriate fixed-input review. A new fixture must expose the owning defect and keep synthetic mutations labelled.

In a change description, explain the problem, affected responsibility, resulting behaviour and actual verification. Report omitted or blocked checks accurately. Never alter an expected result merely to fit a candidate output; a corrected oracle needs its own evidence and revision.

## Sources and licence

The repository uses the [MIT licence](LICENSE). Retain relevant notices. Source documents, data, models and services keep their own terms. Keep source access depth, dates, locators, material transformations and limitations with research evidence. Do not commit credentials or redistribute private or restricted evidence.
