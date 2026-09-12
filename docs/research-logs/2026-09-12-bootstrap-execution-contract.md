Execute the Deep Research Skills bootstrap process below. Treat EACH STAGE AS A SEPARATE, COMPLETE TASK, exactly as though it were the only task I had asked you to perform.

Repository: `sb-dev/deep-research-skills`

Working branch: `feat/bootstrap`

Original bootstrap specification supplied by the user:
https://github.com/sb-dev/deep-research-skills/blob/main/docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md

Active branch bootstrap specification:
`docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md`

Active future-stage amendment:
`docs/research-logs/2026-09-11-deep-research-bootstrap-stage-amendment.md`

Accepted progress record:
`docs/research-logs/bootstrap-progress.md`

Starting point: commit `7b01cf7b07f51169b5624454e5c5b3448f55bfbb` on `feat/bootstrap` — the verified Stage 17 completion commit (`docs: complete stage 17 cross-project review`).

Accepted boundary:

- Stages 1–15 are immutable historical completed stages.
- Stage 16 — Public README Conformance Repair — is complete.
- Stage 17 — Cross-Project Review — is complete.
- Stage 18 — Scaffold Repository and Preserve Public README — is the next stage.
- Stages 18–25 are authorised, executed strictly sequentially.

Historical authority:

- Stages 1–15 were executed against the original bootstrap specification at approved baseline `80b209968b366662c01a8ded5ecb6c30bb6beb0b`, original specification blob `8ff62c92bada2861ece3684a9e73a83da75d9d94`.
- Do not reinterpret, rewrite, renumber or retroactively re-evaluate accepted Stages 1–15 under later family rules.

Future-stage authority:

- From Stage 16 onward, use `2026-09-11-deep-research-bootstrap-stage-amendment.md` together with the original research-specific quality gates that the amendment explicitly preserves.
- The amended active sequence is 16–25, not the superseded original future-stage sequence.
- Stages 16–17 are already accepted and must not be redone.

Do not modify accepted Stage 1–17 evidence merely to simplify a later stage. If Stage 18–25 uncovers a genuine contradiction or defect requiring an accepted earlier stage to change, STOP THE PROCESS AND ASK ME before modifying that accepted work.

## 1. Non-negotiable execution rule

Authorisation to complete multiple remaining stages means repeating the full execution and verification process for each stage. It does NOT mean batching stages, summarising their intent, reducing their depth or replacing required outputs with representative samples.

Your unit of work is ONE STAGE.

Treat the current stage exactly as if it were the ONLY task I had asked you to perform.

Do not consider the existence of later stages when deciding how much research, implementation, execution or verification the current stage deserves.

Do not start the next stage until the current stage:

- has every mandatory requirement satisfied;
- has every required activity actually performed;
- has every required deliverable present and complete;
- satisfies every exact count, distribution, structure and content requirement;
- has passed every specified exit criterion;
- has its verification evidence recorded;
- has been committed to `feat/bootstrap`;
- has the remote commit, parent and intended changed paths verified.

A stage is not complete merely because:

- a research log exists;
- a file has the expected name;
- a design or implementation is described;
- a representative subset was produced;
- a validator exists but was not executed;
- a command exists but was not run;
- an example prompt exists but the stage requires executed research;
- CI might execute later;
- a future stage could theoretically finish it;
- a commit was created.

Never substitute:

```text
representative
partial
illustrative
planned
future target
execution pending
structurally ready
expected behaviour
```

for a requirement that the current stage says must actually exist, execute or pass.

Exact requirements are exact.

If a stage requires 15 executed primary examples, execute and verify 15 primary examples.

If a stage requires two implemented Extension Packs, implement and evaluate both.

If a stage requires a clean external installation, perform the clean external installation.

If a stage requires a real core-vs-pack comparison, execute comparable substantive inputs and record the actual observed difference.

If a stage requires fixed-input independent evaluation, run `research-evaluate` against the fixed producer output rather than substituting the producer's self-review.

## 2. Authority and questions

The governing bootstrap specification plus the accepted amendment are the acceptance contract.

Do not rewrite, weaken, reinterpret, waive or silently defer a requirement because satisfying it makes the stage larger.

Do not use rejected or unrelated bootstrap branches as implementation sources, shortcuts, templates or authorities.

Use accepted work already on `feat/bootstrap` as prior-stage input, but do not treat accepted design as proof of later implementation or execution.

If ANY question requires my input, STOP THE ENTIRE PROCESS AND ASK ME.

This includes:

- ambiguous requirements;
- conflicting requirements;
- uncertainty about the active amendment or stage mapping;
- uncertainty about the approved baseline or branch;
- a genuine contradiction in accepted Stage 1–17 work;
- missing source material required by a mandatory stage requirement;
- an unavailable tool/provider/host required by the stage;
- an unresolved prerequisite;
- an unresolved requirement from an earlier stage;
- a proposed deferral;
- a proposed substitution;
- a proposed scope reduction;
- a proposed exception;
- a user-owned research or product decision;
- an external write, publication, release, registry promotion or other action requiring authority I have not provided.

Do not answer such questions on my behalf.

Do not make a “reasonable assumption” and continue when my decision is required.

Do not continue with another stage while waiting for my answer.

The rule is:

```text
QUESTION REQUIRES USER INPUT
→ STOP
→ ASK
→ DO NOT CONTINUE UNTIL ANSWERED
```

Use only `feat/bootstrap` throughout this continuation unless I explicitly change the branch strategy.

## 3. Before starting EACH stage

At the beginning of every remaining stage:

1. Read the active bootstrap specification on `feat/bootstrap`.
2. Read `2026-09-11-deep-research-bootstrap-stage-amendment.md` completely for the current stage.
3. Read the original research-specific acceptance requirements that the amendment leaves in force.
4. Read `bootstrap-progress.md`.
5. Read the accepted outputs of every earlier stage materially required by the current stage.
6. Verify the current branch head and the last accepted completion boundary.
7. Verify all prerequisites actually exist and passed their earlier exit criteria.

Then extract a stage-specific acceptance checklist.

The checklist must explicitly capture:

```text
stage purpose
active governing section
historical/original requirements still applicable
required inputs
prerequisites
questions to resolve
required research
required implementation
required execution
required comparisons
required candidate discovery
required analysis
required decisions
required deliverables
required contents of each deliverable
exact counts
exact distribution requirements
exact naming requirements
exact repository paths
required prompts
required examples
required source/tool/runtime evidence
required Extension Packs
required tests
required installation checks
required evaluation
required measurements
required public README preservation/conformance checks
required claims-ledger changes
research-log output
exit criteria
things explicitly deferred to later stages
```

For every checklist item, cite or identify the corresponding requirement in the amendment/original specification.

Before substantive work, state:

```text
Stage: <number and title>

Completion requires:
- ...
- ...
- ...
```

Do not begin work belonging to a later stage.

## 4. Deep Research evidence discipline

Deep Research Skills is a research-production system, not a prompt collection.

Preserve the domain distinctions established by accepted work:

```text
research need
≠ question
≠ source
≠ evidence
≠ claim
≠ synthesis
≠ recommendation
```

Where applicable preserve:

```text
source identity
source provenance
source version / publication date
valid-as-of / temporal scope
retrieval method
retrieved passage / structured fact
claim supported or challenged
contradictions
uncertainty
limitations
citation relationship
```

Do not invent:

- sources;
- citations;
- retrieved passages;
- publication dates;
- search results;
- document contents;
- benchmark executions;
- agent outputs;
- tool/runtime identities;
- installation results;
- provider behaviour;
- verification passes;
- empirical findings.

Synthetic fixtures must always remain explicitly synthetic.

Generated synthesis must never be relabelled as retrieved evidence.

A citation that merely mentions a topic does not automatically support a specific claim.

Contradictory evidence must remain visible rather than being silently averaged into a confident answer.

Temporal claims must retain their valid-as-of boundary where material.

If evidence required for a mandatory requirement is unavailable and cannot legitimately be obtained, STOP and ask me rather than weakening the requirement.

## 5. Stage 18 — Scaffold Repository and Preserve Public README

Treat Stage 18 as the ONLY task until complete.

Follow the accepted Stage 16 README contract and Stage 17 scaffold/preservation findings exactly.

Create only useful production surfaces justified by accepted specifications. Do not create empty directories for symmetry.

Where needed establish:

```text
README.md
LICENSE
CONTRIBUTING.md
CHANGELOG.md
docs/
skills/
examples/
benchmarks/
tests/
tools/
extension-packs/
integrations/
.github/
```

README changes are limited to permitted mechanical publication changes:

```text
link selected repository licence
link CONTRIBUTING.md
create and link stable public example paths
correct factual repository paths created by scaffolding
```

Do NOT independently:

```text
change positioning
shorten/replace Level 1 quick-start prompt
change 5 × 3 progression
collapse skill sections into a table
add bootstrap/maturity narration
route public onboarding through research logs
```

Create exactly one stable public README for each accepted primary example:

```text
examples/level-1-<example>/README.md
...
examples/level-5-<example>/README.md
```

There must be exactly 15 primary public example surfaces matching the accepted 5 × 3 identity.

Each initial public example may contain accepted problem, exact prompt, expected artefacts and evaluation contract without claiming execution that has not happened.

Add deterministic README protection for the required public sections/order, complete inline Level 1 prompt, exact 5 × 3 progression, public example-link closure, substantive three-skill sections, local link closure and absence of bootstrap/maturity leakage.

Do not advance until the scaffold exists, all 15 example paths are navigable and the accepted README contract passes actual deterministic checks.

## 6. Stage 19 — Implement and Prove Core Vertical

Treat Stage 19 as the ONLY task until complete.

Use L1-01 as the actual proving vertical:

```text
research need
→ frame
→ source strategy / bounded plan
→ exact source inspection
→ evidence extraction
→ claim analysis
→ synthesis
→ fixed-input evaluation
→ bounded repair when needed
```

The proof must use the actual `deep-research` implementation and actual `research-evaluate` implementation.

It must record:

- exact L1-01 prompt/input;
- actual retrieved sources;
- actual producer artefact;
- actual producer tool/runtime identity;
- evidence/claim/citation/temporal distinctions;
- evaluator fixed input;
- evaluator output;
- failures;
- owning-layer diagnosis;
- any bounded repair;
- rerun evidence where repair occurs.

The producer's own self-check is not independent evaluation.

Do not replace executed proof with command contracts, mock output, hand-authored expected output or structural validation.

Clean external installation is NOT Stage 19 and must not be falsely claimed here.

## 7. Stage 20 — Expand Progressive Coverage and Extension Packs

Treat Stage 20 as the ONLY task until complete.

Execute all fifteen accepted primary examples at the fidelity required by their accepted design.

For all 15 preserve:

- exact accepted prompt;
- actual source/tool inputs;
- actual produced artefacts;
- evidence/citation review;
- limitations;
- actual evaluator behaviour where required;
- bounded repair where needed;
- execution/runtime identity.

Do not substitute:

```text
15 prompt files
15 README files
15 expected-output descriptions
15 structural checks
```

for 15 executed research behaviours.

Implement and evaluate both accepted initial Extension Packs:

```text
scholarly-evidence
open-source-ecosystem
```

For EACH pack prove with actual comparable substantive inputs:

```text
core works without pack
core + pack materially changes intended research behaviour
explicit task instructions outrank pack defaults
accepted research decisions outrank pack defaults
pack-aware evaluation recognises intentional specialisation
```

Exercise `research-extension-pack-creator` on:

1. at least one valid catalogue/revision case;
2. at least one rejection/reuse case.

Pack files alone are not proof of pack behaviour.

## 8. Stage 21 — Configure Skill Installation

Treat Stage 21 as the ONLY task until complete.

Validate the documented project-local installation contract for:

```text
deep-research
research-evaluate
research-extension-pack-creator
producer + evaluator
producer + selected pack where applicable
all three skills
```

Record exact installer version, repository revision and supported host for every installation claim.

Verify:

- selective installation;
- skill-local references and commands;
- self-containment;
- no undocumented source-checkout dependency;
- correct pack discovery where applicable.

Do not substitute source-tree presence for installation behaviour.

Clean external consumer installation remains Stage 23.

## 9. Stage 22 — Local Validation and Public README Conformance

Treat Stage 22 as the ONLY task until complete.

Actually run and record validation for:

```text
repository structure
SKILL.md contracts
command/reference closure
deterministic validators
benchmark fixtures
implemented Extension Packs
all 15 public example prompts
local selective installation
README structure
README local links
claims-ledger consistency
```

The README checker must reject public process leakage, including:

```text
Stage <number>
feat/bootstrap
bootstrap progress
production scaffold
maturity promotion
completion SHAs
not-run bookkeeping
research-log links as primary example route
```

A structural checker does not prove research quality. Keep deterministic structural evidence separate from actual semantic/execution evidence.

Update the internal public claims ledger with actual evidence gathered so far.

Do not mark the stage complete with unexecuted validators.

## 10. Stage 23 — Publish, Clean External Install and Reconcile Public Claims

Treat Stage 23 as the ONLY task until complete.

From a genuinely clean consumer project:

1. install the documented skill selection from GitHub;
2. verify discovery by every claimed host;
3. run the complete Level 1 quick-start;
4. verify documented research artefacts;
5. run fixed-input independent evaluation;
6. verify no source-checkout-relative dependencies;
7. test selective installation;
8. test at least one implemented Extension Pack;
9. record exact repository revision, installer version, host and observed result.

Then reconcile every material public README claim against the claims ledger:

```text
supported
→ keep

partially supported
→ narrow

unsupported but required for release
→ finish owning work or BLOCK publication

unsupported and non-essential
→ remove
```

Do not explain unsupported product claims to public users using bootstrap scheduling language.

Do not claim clean external installation if only a local copy/symlink/source checkout was tested.

## 11. Stage 24 — Optional Pactwright Integration and Registry Promotion

Treat Stage 24 as the ONLY task until complete.

Pactwright integration remains optional.

Do not move research semantics, evidence state, source graph or research workflow ownership into Pactwright.

Registry/maturity promotion must follow demonstrated evidence, not documentation volume.

Do not claim:

```text
working
benchmarked
mature
```

unless the corresponding accepted family evidence gates are actually satisfied.

A registry change, release, merge or external publication requiring user authority must not be inferred from stage authorisation. If such an action requires my explicit approval and has not already been granted, STOP AND ASK ME.

## 12. Stage 25 — Review Shared-Abstraction Candidates

Treat Stage 25 as the ONLY task until complete.

Review candidates only after implementation evidence exists.

Potential candidates include:

```text
research-to-production handoff metadata
source provenance conventions
valid-as-of semantics
citation evidence packages
```

Apply the governing family rule: do not centralise an abstraction unless multiple independent domains demonstrate substantially the same need.

Do NOT introduce without evidence:

```text
shared research runtime
central evidence database
universal claim graph
universal source-quality score
central provider router
universal Extension Pack interpreter
```

Record accepted, rejected and retained-domain-specific candidates with evidence.

## 13. Verification before completing ANY stage

After doing the current stage's work:

1. Re-read the active stage requirement from the amendment.
2. Re-read applicable original research-quality gates.
3. Inspect actual repository contents and execution evidence.
4. Verify against the governing requirement, not against your own summary of intent.

Produce a conformance table:

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| ... | ... | ... | ... | PASS / FAIL / BLOCKED |

Use only:

```text
PASS
FAIL
BLOCKED
NOT APPLICABLE
```

`NOT APPLICABLE` requires explicit specification-grounded justification.

Verification must include substance, not filenames.

Check where applicable:

- exact item counts;
- exact 5 × 3 example identity;
- exact prompt preservation;
- executed behaviour rather than prompt/file existence;
- actual source provenance;
- citations and claim support;
- contradiction handling;
- temporal scope;
- actual producer output;
- fixed-input evaluator independence;
- pack differential execution;
- extension-pack creator behaviour;
- local installation;
- clean external installation;
- host discovery;
- self-containment;
- local/public link closure;
- README leakage rules;
- claims-ledger reconciliation;
- preservation of accepted earlier decisions;
- maturity/publication claims.

Do not weaken a validator, rubric or criterion to make incomplete work pass.

If anything is FAIL:

```text
repair owning layer
→ rerun affected verification
```

If anything is BLOCKED and requires my input:

```text
STOP
→ ASK ME
```

Do not begin the next stage.

## 14. Durable stage-record requirements

Each stage must persist enough evidence for a future session to verify it without conversation memory.

Where relevant record:

```text
stage goal
governing requirements
accepted parent/baseline
inputs inspected
sources actually retrieved
source limitations
tools/runtimes actually used
exact commands where material
actual outputs
candidate/coverage analysis
pack comparisons
decisions
rejected alternatives
failures and repairs
verification
conformance table
executed results
unresolved questions
explicitly deferred work
exit assessment
next-stage handoff
```

Do not mark a stage COMPLETE while its own mandatory requirement says execution or verification is pending.

## 15. Commit the completed stage

Only after every mandatory current-stage requirement is PASS:

1. Persist complete stage outputs.
2. Persist execution and conformance evidence.
3. Update `bootstrap-progress.md` accurately.
4. Review changed files for accidental next-stage/unrelated work.
5. Commit only the current stage's work to `feat/bootstrap`.
6. Verify the remote branch points to the new commit.
7. Verify commit message, parent and changed paths.
8. Verify intended files resolve at the immutable commit.

Commit messages must remain stage-scoped.

Examples:

```text
feat: complete stage 18 production scaffold and public examples
feat: complete stage 19 core research vertical
feat: complete stage 20 progressive execution and extension packs
docs: complete stage 25 shared abstraction review
```

After remote verification report:

```text
Stage:
Status: COMPLETE

Deliverables:
- ...

Verification:
- ...

Commit:
<full SHA>

Remaining blockers:
none
```

Only then may the next authorised stage begin.

## 16. Stage progression

Stages 18–25 are authorised, but they are NOT one task.

The execution model is:

```text
STAGE 18 IS THE ONLY TASK
→ complete
→ verify
→ commit
→ remotely verify

THEN

STAGE 19 IS THE ONLY TASK
→ complete
→ verify
→ commit
→ remotely verify

...

THEN STAGE 25
```

Do not think:

```text
“I need to finish Stages 18–25.”
```

Think only:

```text
“I need to complete the current stage perfectly.”
```

The existence of a later stage never justifies incomplete current-stage work.

## 17. Context and interruption safety

The repository is authoritative state.

At the start of every stage reconstruct context from:

```text
active bootstrap specification
+
active amendment
+
bootstrap-progress.md
+
accepted earlier stage outputs on feat/bootstrap
```

Do not rely on long conversation memory.

If context becomes too large, STOP at the latest fully verified stage boundary rather than compressing, batching or skipping work.

If interrupted during a stage:

- do not claim completion;
- identify the last fully verified commit;
- preserve accurate partial work only if useful and clearly incomplete;
- resume the SAME stage later.

## 18. Final bootstrap audit

After Stage 25 has individually passed and been remotely verified, perform a separate end-to-end conformance audit.

Use:

- immutable original Stage 1–15 specification/history;
- active amendment for Stages 16–25;
- current Production Skills family requirements where applicable without retroactively rewriting accepted historical work.

Build a complete matrix across all stages and global acceptance gates.

Verify at minimum:

```text
accepted historical stage evidence remains intact
Stage 16 README contract remains satisfied
Stage 17 review findings remain preserved
Stage 18 scaffold and exactly 15 public example surfaces
Stage 19 real L1-01 producer/evaluator vertical
Stage 20 all 15 executed examples
Stage 20 both initial Extension Packs executed and differentiated
Stage 20 extension-pack creator valid + rejection/reuse cases
Stage 21 installation combinations verified
Stage 22 local validators actually pass
Stage 22 public README leakage/link rules pass
Stage 23 clean external GitHub installation actually passes
Stage 23 claimed-host discovery actually passes
Stage 23 Level 1 quick-start actually runs externally
Stage 23 claims ledger fully reconciles README claims
Stage 24 maturity/registry statements match actual evidence
Stage 25 abstraction decisions follow multi-domain evidence rule
canonical docs remain internally consistent
public README matches demonstrated product behaviour
```

If the final audit finds a mandatory failure, the bootstrap is NOT COMPLETE.

Repair the owning stage and rerun affected downstream checks.

Do not mark a PR ready, merge, release or promote maturity until the full audit has zero unresolved mandatory failures and any required user authorisation has been obtained.

## 19. Governing execution sequence

For EVERY remaining stage:

```text
READ THE ACTIVE STAGE CONTRACT
        ↓
READ APPLICABLE ORIGINAL QUALITY GATES
        ↓
EXTRACT EVERY REQUIREMENT
        ↓
VERIFY PREREQUISITES AND ACCEPTED PARENT
        ↓
STATE THE ACCEPTANCE CHECKLIST
        ↓
PERFORM ALL REQUIRED RESEARCH / IMPLEMENTATION / EXECUTION
        ↓
CREATE EVERY REQUIRED DELIVERABLE
        ↓
RE-READ THE GOVERNING REQUIREMENTS
        ↓
VERIFY ACTUAL OUTPUT AND EXECUTION AGAINST EVERY REQUIREMENT
        ↓
FAIL? → REPAIR OWNING LAYER AND RERUN
BLOCKED / USER DECISION? → STOP AND ASK
        ↓
ALL PASS
        ↓
PERSIST CONFORMANCE AND EXECUTION EVIDENCE
        ↓
COMMIT ONLY THIS STAGE
        ↓
VERIFY REMOTE COMMIT, PARENT AND FILES
        ↓
REPORT COMPLETION
        ↓
ONLY THEN START THE NEXT STAGE
```

The most important rule is:

# COMPLETE EACH STAGE AS IF IT WERE THE ONLY TASK I ASKED YOU TO DO.

Do not optimise for the whole bootstrap.

Do not preserve merely the “general intent”.

Follow the active Deep Research Skills bootstrap contract literally and verify that you did so.
