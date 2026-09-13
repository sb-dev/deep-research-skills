# L4-03 — Scoped follow-up and repair record

## Fixed initial state

Producer r1 is frozen in provisional/claim-audit.md and provisional/sources.json. At 36 source actions and zero searches, GROBID README.md returned NOT_FOUND/404 at befaa302d2336aae83971d4700b25de02144109a; same-commit metadata/build.gradle succeeded. The producer notified the parent of the exact failed locator and frozen files before changing the support record. No single-broken-locator mutation was needed.

The parent independently diagnosed D1 in evaluation/diagnosis.md from the frozen input: discover the actual README filename at the same ref, restore only affected documentary support and preserve other eleven repositories. The parent also identified C2's local-data claim as unsupported and endorsed targeted provider inspection. The producer had already dispatched the announced bounded follow-up when that diagnosis arrived; it then read the diagnosis and checked that the actual changes matched its scope. No source acquisition was presented as performed by the evaluator.

## Actual delta

| Action | Evidence result | Affected dependency |
|---|---|---|
| GitHub root-directory GET at GROBID's pinned SHA | Actual filename is Readme.md | D1 identity/locator; no branch change |
| GitHub file GET Promptfoo src/providers/openai/chat.ts at its pinned SHA | Provider request path POSTs JSON body to selected chat/completions endpoint | C2 privacy interpretation; unresolved provider-specific boundaries retained |
| GitHub file GET GROBID Readme.md at original SHA | Full text retrieved, role documented; build.gradle remains prior code/config support | GROBID map row and D1 documentary coverage |

All 36 prior source records remain, including the failed README.md record; three follow-up records are appended. Failed-access detail is made explicit on the defective current record, with the frozen pre-repair copy retained. Other eleven repositories' pre-existing records are unchanged. No original repository source was edited. Source acquisition total advances 36 → 39; no reset, paid work or runtime assurance.

## Affected rechecks and status

- D1: same repository and SHA, exact case-sensitive filename, actual full-text access, documented role and related build requirements checked. Status: locator repaired; parser correctness untested.
- C2: request method, endpoint construction, body, authorization and timeout/retry fields inspected. Status: universal local-only claim rejected; chosen deployment's privacy boundary still requires tests.
- C1: dependency equality and wrapper-versus-engine interpretation retained; no change to accepted support or wording.
- Source preservation: compare each pre-existing non-GROBID record to frozen sources.json; additions are only the declared scoped follow-ups. No unrelated evidence refresh or date advancement.
- Review: parent final fixed-input audit must examine corrected source access, narrowed claim and preservation. Producer checks are not independent approval.

Reopen affected scope if the source ref changes, the selected provider/retriever or data boundary changes, a parser output fails an original-source check, or evidence contradicts the shared-engine interpretation. No downstream installation, publication or security certification is authorised by this repair.


## Independent-review locator correction — review R2

Preserved the exact pre-correction map as provisional/ecosystem-map-review-R1.md (its producer r2 heading belongs to the earlier D1 lifecycle). Independent review identified three compound claims whose original links covered only one clause. Using already acquired originals at unchanged refs, the map now adds Docling error-option lines 519–536 and error-handling lines 639–663; GROBID service-entry-point lines 414–421; and Trafilatura rescue-implementation lines 191–277. Existing format/toolchain/interface links remain. Only those three rows’ locators changed; claim wording, the other nine rows, source records and independent-review files are unchanged. Local comparison confirmed exactly three changed map lines. No new source acquisition: total remains 39/64 actions and 0/20 searches. Review R2 is fixed for the evaluator’s affected-locator recheck.
