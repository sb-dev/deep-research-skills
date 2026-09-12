# Pack authoring and validation

## Authoring workflow

Use `research-extension-pack-creator`, operation `create-pack`.

The authoring workflow is twelve steps (A01–A12 here are authoring steps, not research record IDs):

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

## Showcase contract

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

## Repair and versioning

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

## Maturity states

Use separate evidence states:

- **designed**: complete reusable pack contract;
- **procedure-demonstrated**: source-backed core-versus-pack application exists;
- **installed-tested**: production pack bundle successfully loads/activates from intended installation;
- **behaviourally evaluated**: fresh representative differential cases pass;
- **catalogue-ready**: required showcase, evaluation and packaging evidence is complete.

These do not imply repository-wide `working`, `benchmarked` or `mature` status.
