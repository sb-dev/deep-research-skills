# Stage 13 Publication Receipt

Date: 10 September 2026. Branch: `feat/bootstrap`.

Status: COMPLETE. Content acceptance: PASS. Remote publication verification: PASS. Remaining blockers: none.

Completed-stage commit: `9d223ee2655f1c9642bc5b0e21caddfbfae3c66a`.
Sole parent: `24bc5755cd769587e367792ba17f892116542551`.
Root tree: `dace18e3d1e4d0ab2f0f1ead297a788d05c389da`.

After the non-force update, the branch reference and Git commit were read back. The reference pointed to the completed-stage commit; the commit had the intended sole parent and root tree. The parent comparison contains exactly seven added Stage 13 files and the updated progress index. No accepted earlier-stage file was changed.

Each new file was then read at the immutable completed-stage commit. The returned blob identities match the locally checked full bytes and the earlier blob-creation results:

| File | Verified Git blob |
|---|---|
| `2026-09-10-stage-13-evaluation-design.md` | `2a21274a2d899442b735cc694ae6fb4afd0d1340` |
| `2026-09-10-stage-13-benchmark-research.md` | `7d2e8b3c977eb52dd2b2dd4252d7d681bd9dd86b` |
| `2026-09-10-stage-13-case-contracts.json` | `fd6869b8b10bb1fee4e39f892f7bf82071af61eb` |
| `2026-09-10-stage-13-fixture-check.py` | `496cc56bcce457fa14fa58b5230164ce62b1212d` |
| `2026-09-10-stage-13-verification.json` | `ee0a13b00c12c941c48df58b7234e8dc92fa718a` |
| `2026-09-10-stage-13-document-check.py` | `0ea17e6c190a089737c289f18ca9da28c5eea0a8` |
| `2026-09-10-stage-13-document-verification.json` | `6d1c74447a9397f8ba671b9fd0408e7422ce4596` |
| `bootstrap-progress.md` at the completed-stage commit | `0a415bd24cfb088cbcf35f183f696a82f184042a` |

The published result records twelve priority and six additional synthetic cases, four isolated failure-layer controls, nine packaging controls, sixteen pack-selection controls, six acceptance controls and four scorer-mutation controls. All met their expected positive/negative outcomes; input preservation passed. The separate document result records seventeen passing checks and eight detected negative controls. These are bounded typed reference and document checks, not live-agent scores, arbitrary-language entailment, independent human review or installed-product results.

The design and primary research complete all eight current-stage output responsibilities, all ten evaluation layers, the five required external benchmark families, all fifteen progressive-example mappings and both selected pack pair contracts. The original section 19 was re-read during final conformance review. The accepted Stage 11 source-backed comparisons retain their actual shared-session limitations; no new independent trial was fabricated.

Verification routes: GitHub GET `git/ref/heads/feat/bootstrap`, `git/commits/9d223ee2655f1c9642bc5b0e21caddfbfae3c66a`, parent comparison, and exact file reads at that immutable commit. Short readback ranges verify published identity; they are not relabelled as the earlier full semantic review.

The complete progress record at the content commit is preserved byte-for-byte as [historical progress through Stage 13](bootstrap-progress-through-stage-13.md). Its pending-publication text is historical. This receipt and the current index record the observed completed state. Stage 14 is next; no release, merge or maturity promotion is made.
