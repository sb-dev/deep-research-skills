# Handoff to Software Engineering

Revision r2, 2026-09-13. Receiving input: [research.md](research.md) r2 and its source/evidence/claim record, plus [programme-map.md](programme-map.md). Status: pre-architecture recommendations awaiting independent audit and archival decisions. This handoff gives evidence needs; the software owner selects architecture, scope and implementation.

| Evidence-backed need | Proposed behaviour to investigate | Verification and unresolved choice |
|---|---|---|
| C1/C5/C8 context is material | Keep source-native reference, holder, creator and context distinct; allow uncertain relationships. | Trace a reviewed fixture to its collection/series context. Decide storage and mappings after a real fixture; do not assume a reference encodes ancestry. |
| C4/C6 representation and transformation | Retain original locator/access depth, derivative identity, page/region, transcription/OCR method, changed text and responsible role. | A correction should expose the prior version and affected claims. Choose formats and tooling; a provenance relation is not an authenticity verdict. |
| C2/C3/C5 missingness | Preserve a search observation separately from an institution's record-status assertion and from a historical conclusion. | On a no-result fixture, output bounded search scope with unknown cause; prohibit automatic event-absence conclusions. Exact absence vocabulary is for archival review. |
| C7/C8 use conditions | Store an item's access evidence separately from a permission decision for a proposed use. | A public catalogue description must not silently authorise external processing or publication of the record. Rights owner decides the policy. |
| C10 review and revision | Keep claim support and review scope attached to the actual reviewed revision. | Correct one transcription; invalidate affected claims/review without discarding unrelated verified evidence. |

Open engineering questions: actual catalogue interfaces and licences, stable identifiers, pagination, exports, API limits, document sizes, authentication, redaction handling, accessibility of source formats and preservation requirements. None was tested. S5's conflicting AND/OR description (research X1) must be resolved before a query translator or automated completeness inference is designed. S2 is a 2017-based account, so present field semantics need confirmation.

A useful first engineering investigation is a small, local, synthetic or explicitly cleared fixture with two representations and one corrected transcription. This is a proposal for the receiving owner, not authorisation for new tools, accounts, remote processors or live system changes. No schema, API, framework, database, hosting, build or deployment choice is made here.

Support access: original URLs and exact sections are in research.md; the TNA detail attempt U1 has no content and cannot populate a fixture. For item-level work obtain a permitted original under G1. Review needed: archival mapping, privacy/rights decision, independent research audit, and actual integration checks. Reopen affected requirements when sources relocate, catalogue semantics change, a new representation changes support, or intended use/audience changes. Return engineering constraints to the research owner; do not silently narrow the research claim.
