# Stage 15: Public README Design

Date: 11 September 2026. Repository: `sb-dev/deep-research-skills`. Branch: `feat/bootstrap`.

Status: COMPLETE. Content acceptance: PASS. Remote publication verification: PASS. Remaining blockers: none.

## Authority and prerequisites

The acceptance contract is section 21 of the original bootstrap specification on `main`, blob `8ff62c92bada2861ece3684a9e73a83da75d9d94`, plus the global research principles and section 29 maturity/acceptance gates. The accepted parent is the Stage 14 remote-verification receipt `066d545994e8925010098d2d35b39d3389cb65af`.

Stage 14 is complete and remotely verified. The six canonical specifications are the authoritative product-design inputs. The Stage 12 progressive example design supplies exactly fifteen selected examples and the complete prompts; the Stage 13 design supplies evaluation status and limitations.

Section 21 specifically requires following the proven public structure of `video-production-skills`. Only its public README structure was inspected for this stage. Broader cross-project pattern extraction is deliberately not performed here because that is Stage 16.

## Completion checklist

| ID | Requirement | Specification reference |
|---|---|---|
| R01 | Re-read the original Stage 15 contract and verify Stage 14 completion. | Execution instructions §3; bootstrap §21. |
| R02 | Inspect the proven `video-production-skills` public README structure and adapt, rather than copy, it for research. | §21 first sentence. |
| R03 | Make the positioning explicitly about research production rather than isolated browsing/search. | §21 positioning requirement. |
| R04 | Include research capabilities and effort/evidence control. | §21 target structure. |
| R05 | Include an installation surface without claiming unperformed installation. | §21 target structure; Stage 14 Spec 03. |
| R06 | Choose a strong Level 1 quick start demonstrating find → verify → cite → uncertainty without specialist credentials or expensive APIs. | §21 quick-start requirement. |
| R07 | Include five progressive levels with exactly three selected examples per level. | §21 target structure; accepted Stage 12. |
| R08 | Include project-structure guidance, all three skills, Extension Packs, execution, evaluation/benchmarks and documentation. | §21 target structure. |
| R09 | Include project boundary, contributing and licence sections while remaining truthful about not-yet-scaffolded files. | §21 target structure; section 29. |
| R10 | Preserve the exact accepted fifteen-example selection and the two selected pack profiles. | Accepted Stages 11–12. |
| R11 | Verify links, counts, quick-start completeness, installation disclaimers and maturity claims against actual repository state. | Execution instructions §5. |
| R12 | Commit only Stage 15, verify remote publication and record the receipt before progression. | Execution instructions §7–8. |

No README hero image, example previews, production `CONTRIBUTING.md`, `LICENSE`, skill directories or example directories are required by Stage 15. Creating those now would begin Stage 17 scaffolding. The public README must instead make their current absence explicit.

## Inputs inspected

### Governing Deep Research material

- original bootstrap §21 on `main`;
- current bootstrap progress at the verified Stage 14 receipt;
- all six Stage 14 canonical specifications;
- Stage 12 progressive example design, including the fifteen selected example IDs and exact `L1-01` prompt;
- Stage 13 evaluation design status.

### Public-structure reference

`sb-dev/video-production-skills/README.md` on `main`, blob `878ee7df6ad8f5f7ad1e8aa62f7014844ac78724`, was inspected as the required structural reference.

Useful public-surface patterns retained:

- one-sentence production positioning;
- capability overview before implementation detail;
- cost/decision-control section;
- installation near the top;
- one complete quick-start prompt;
- progressive learning levels;
- project structure that grows with responsibility;
- skill descriptions;
- execution-tool boundary;
- documentation index;
- contribution and licence closure.

Research-specific differences are intentional:

- evidence/claim/provenance replaces creative asset/approval semantics;
- the README has exactly three examples per level because the accepted Deep Research design requires 5 × 3;
- evaluation/benchmarking is first-class because §21 requires it;
- no visual previews are fabricated because examples have not been executed;
- installation commands are clearly marked as intended contracts, not present functionality;
- no `CONTRIBUTING.md` or `LICENSE` link is emitted because those files do not exist yet.

This is the limited structural adaptation expressly required by Stage 15, not the multi-project Stage 16 review.

## Positioning decision

The bootstrap's proposed direction is retained almost exactly:

> Conduct evidence-backed research, not isolated searches.

The supporting sentence then explains the actual research-production loop: framing, source strategy, source inspection, provenance, contradiction analysis, synthesis, audit and bounded refresh.

Alternatives rejected:

| Alternative | Reason |
|---|---|
| “AI-powered deep research” | Describes a category rather than the production responsibility; says nothing about evidence discipline. |
| “Browse the web and write cited reports” | Narrows research to browsing and hides source quality, provenance, contradictions, repair and private/connected evidence. |
| “Autonomous research platform” | Overstates authority and implies the universal runtime explicitly rejected by the accepted architecture. |
| “Conduct evidence-backed research, not isolated searches.” | Selected: concise, matches the bootstrap direction and accurately distinguishes research production from one-shot retrieval. |

## Quick-start decision

`L1-01 — PROV Primer publication status` is selected.

It is the strongest public quick start because:

- it uses a public official W3C source;
- no private account or specialist credential is required;
- no new paid provider run is required;
- it is tightly bounded;
- the prompt explicitly requires an exact locator;
- it distinguishes a document's own status from neighbouring formal Recommendations;
- it preserves uncertainty/access limits;
- it writes one small inspectable output;
- Stage 12 already selected it as the strongest keyless quick start.

The README copies the complete accepted Stage 12 prompt rather than replacing it with a shortened example. It also states that the prompt becomes executable only after the skill is actually scaffolded and installed.

## Progressive example surface

The README includes exactly the accepted fifteen examples:

```text
Level 1: L1-01, L1-02, L1-03
Level 2: L2-01, L2-02, L2-03
Level 3: L3-01, L3-02, L3-03
Level 4: L4-01, L4-02, L4-03
Level 5: L5-01, L5-02, L5-03
```

Each links to the accepted Stage 12 heading containing its exact prompt. The README describes the responsibility exercised; it does not claim the example has been executed or benchmarked.

## Installation and maturity decision

The README includes the three intended installation forms from canonical Spec 03 because installation is a required public surface. It explicitly says:

- skill directories do not exist yet;
- the commands have not passed local installation;
- clean external installation has not passed;
- the commands are specified contracts, not current working instructions.

This keeps Stage 15 useful while preserving Stage 17–20 acceptance boundaries.

Similarly:

- the two selected packs are described as design catalogue entries, not installed packs;
- Stage 13 reference/design checks are distinguished from live installed-agent benchmarks;
- contribution and licence sections state that their production files are not yet scaffolded.

## Verification strategy

The Stage 15 verifier checks:

1. exact README title and positioning;
2. all required public sections;
3. exactly five levels;
4. exactly three accepted examples per level and fifteen unique accepted IDs overall;
5. quick-start W3C source, exact output path, bounded search/read limits, locator requirement and uncertainty language;
6. intended installation forms and the not-yet-installable warning;
7. all three skill names and eleven command names;
8. exactly the two selected initial pack profiles;
9. all six canonical specification links;
10. relative link closure against the actual parent repository plus the Stage 15 README;
11. explicit project-boundary language;
12. truthful current maturity;
13. no link to nonexistent `CONTRIBUTING.md` or `LICENSE`.

Negative controls deliberately remove one example, remove the quick-start source URL, replace the installation disclaimer with a false readiness claim, and break a canonical-spec link.

The verifier is structural/contract validation. It is not an installed-agent test, semantic benchmark or clean installation.

## Conformance

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| R01 | Execution §3; bootstrap §21 | Authority/prerequisite section | Original §21 and Stage 14 receipt inspected. | PASS |
| R02 | §21 first sentence | Public-structure analysis | `video-production-skills` README inspected; retained/rejected adaptations recorded. | PASS |
| R03 | §21 positioning | README opening | Positioning and research-production explanation inspected. | PASS |
| R04 | §21 target structure | README capability/control sections | Required content and accepted principles checked. | PASS |
| R05 | §21 installation | README installation section | Commands match Spec 03 and disclaimer prevents false installation claim. | PASS |
| R06 | §21 quick start | README L1-01 full prompt | Exact accepted prompt, public source, bounded actions, locator and uncertainty checked. | PASS |
| R07 | §21 5 × 3 structure | README learning levels | Count exactly three accepted examples in each of five levels. | PASS |
| R08 | §21 target structure | README remaining product sections | All required sections and accepted skill/pack/evaluation responsibilities checked. | PASS |
| R09 | §21 closure; §29 | Boundary/contributing/licence | Missing future scaffold files stated honestly; no broken links emitted. | PASS |
| R10 | Stages 11–12 | Pack/example inventories | Two selected packs and all fifteen accepted IDs preserved. | PASS |
| R11 | Execution §5 | Verifier + result | Positive checks and four negative controls executed; relative links checked. | PASS |
| R12 | Execution §7–8 | Stage-only commit/readback | Cumulative Stage 15 content head `065ecd4762660d02d2ff4a65987634eacb2ec24d` was compared with verified Stage 14 receipt `066d545994e8925010098d2d35b39d3389cb65af`: exactly five intended Stage 15 paths changed. README, research log, verifier, result and progress were read back at the immutable head and matched the validated Git blobs. | PASS |

Remote publication verification is complete. The five sequential contents-API commits are all Stage 15-scoped and their cumulative delta contains no earlier-stage modification.

## Exit assessment

The intended public product surface is now clear before repository scaffolding. It explains the product, research controls, intended installation, quick start, progressive learning path, skills, packs, execution, evaluation, documentation and boundary without claiming later bootstrap stages have passed.

Stage 15 exit criteria pass. The README identity, evidence files, progress update and cumulative changed-file scope were read back from `feat/bootstrap`. Stage 16 is the next authorised stage, but is not started by this completion record.
