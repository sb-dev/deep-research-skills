# Fixed-input research audit — EX-L1-01

**Overall verdict: FAIL (low severity, input-provenance metadata).** The source-status answer is supported. Eight of nine requested scopes pass; reproducibility fails because `execution.json:11` presents an undocumented normalized prompt digest as `prompt_sha256`. No score or producer self-check overrides this defect.

## Review identity and authority

- Reviewer: ChatGPT Work Mode / Codex agent, task `/root/l1_01_fixed_audit`; separate agent review, not an independent human review. Model, host and tool build revisions were not exposed.
- Reviewed submission: `run-2026-09-12-01`, fixed at `2026-09-12T23:05:29.743117+00:00`. Review completed at `2026-09-12T23:15:53.275114+00:00`.
- Skill: `research-evaluate`, operation `audit`, contract `0.1`; source-checkout git commit `0d708a7fee2ec95effb345d10677b2c53f292155`, skill tree `8faf64960ff2b6d547d6c7460ff6265c31924c9f`. Git reported no changes in the skill directory. Read `SKILL.md`, `commands/audit.md`, and the command-contract, evidence-contract, audit-criteria and repair-diagnosis references.
- Inputs were limited to `prompt.txt`, `brief-and-plan.md`, `execution.json`, `fixed-input.json` and `research/l1-01/research.md`. No other research logs, example design files, expected answers or prior conversation conclusions informed the verdict.
- No Extension Pack, installation test, purchase, paid provider run, external communication or submission repair was performed. The producer self-check was inspected for labelling only, never used as the support oracle.

## Fixed revision and byte integrity

The four identities passed both before review (`2026-09-12T23:10:19.889074+00:00`) and after substantive review (completion time above). The expected, before and after SHA-256 values are identical:

| Fixed file | SHA-256 | Before / after |
|---|---|---|
| `prompt.txt` | `767ae9980659356a0b64c7d5528b62d221df74ad00abe20ea81973789dc89dd9` | PASS / PASS |
| `brief-and-plan.md` | `d400271c97b644fe1394de82e5554880e6e1d45ceee630131a4700a00fbb3125` | PASS / PASS |
| `execution.json` | `331ace2bf79d13e308d9648e943011be797081e9c0ba514c3f5687d5b876a97c` | PASS / PASS |
| `research/l1-01/research.md` | `958d0f4496603d5872f4c03b5e42e9ab9fa68c1bf142ac9306c6ac7c6dbceb2f` | PASS / PASS |

`fixed-input.json` itself hashes to `edfb9423a41acbb5b2643265beaebe141f6af9d3e62f294fc1dca296d28c84eb`. Its exact revision and report identity agree with the files; `execution.json` also records the correct report digest. Hash equality establishes preserved bytes, not the truth of source claims.

## Original-source assessment

O1: The [Primer header](https://www.w3.org/TR/prov-primer/) gives a working-group Note category and the date 30 April 2013; its declared edition is the dated 2013-04-30 URL. These directly support E1/C1. Locator: title-adjacent heading and “This version”, native text lines 0–3.

O2: The same [status section](https://www.w3.org/TR/prov-primer/) separates the Primer from the linked Recommendations and repeats its own category in the publication paragraph. These support E2/C2. Locator: Status of This Document → PROV Family of Documents, and Please Send Comments, first paragraph; lines 26–49.

O3: The linked [PROV-DM edition](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) independently supplies its own Recommendation label and date. Its status publication paragraph agrees. These support E3/C2. Locator: title-adjacent header, then Status of This Document → Endorsed By W3C / Please Send Comments; lines 0–3 and 41–64.

O4: The [Primer caveat](https://www.w3.org/TR/prov-primer/) treats status as publication-time information and permits later replacement; the report retains that boundary. No conflicting category appeared in the checked passages. This is a bounded absence observation, not a supersession search.

The material source claims and source locators were checked against these originals, separately from the internal S/E/C reference check. The dated Primer target was observed as its declared version, not separately fetched. Both sources share publisher/family origin; separate-origin empirical corroboration is unnecessary for their own labels.

## All nine requested scopes

Record shorthand: P1=`prompt.txt`; B1=`brief-and-plan.md`; X1=`execution.json`; R1=`research/l1-01/research.md`; F1=`fixed-input.json`. Numbers identify lines in those fixed files. O1–O4 are the original-source checks above; H1/H2 are the before/after hash checks. Full criterion records and exact source-tool arguments are in `review.json`.

| Scope | Verdict / severity | Evidence and reason | Smallest owning-layer repair |
|---|---|---|---|
| source-quality | PASS / none | O1, O2, O3, R1:17-20. The inspected publisher originals directly establish their own document labels. Text extraction and section locators are proportionate to this narrowly specified question; no empirical quality appraisal is required. | None. |
| source-independence | PASS / none | O2, O3, R1:20. The submission identifies shared publisher/family origin and does not count two labels as independent confirmation of performance. Separate documents answer separate identity propositions; independent empirical corroboration is not required. | None. |
| coverage | PASS / none | P1:1-5, B1:7-17, R1:7-11,17-38, O1, O2, O3. The exact requested document, its required sections and a linked comparison were covered. The output avoids a standards survey and any implementation conclusion. Recorded collection boundaries support the narrow stopping rule; no global recall claim is made. | None. |
| claims | PASS / none | R1:11,26-30, O1, O2, O3. C1 and C2 follow from the independently inspected source passages, including the date normalization in E1/E3. The distinction is local to document identity and imports no implementation premise. | None. |
| citations | PASS / none | R1:11,17-18,26-28, O1, O2, O3. S1/S2 and E1-E3 resolve internally; the external targets and section descriptions locate the propositions. Structural resolution was assessed separately from original-source entailment. The dated Primer URL was observed as the declared edition, not separately fetched. | None. |
| freshness | PASS / none | R1:34, O1, O3, O4. The report separates publication and retrieval dates and confines its answer to the inspected edition. The requested historical self-label needs no broad currentness or supersession investigation. | None. |
| contradictions | PASS / none | R1:27,30,34, O1, O2, O3, O4. The relevant header and status sections agree. The apparent difference between linked categories is correctly assigned to different documents. The absence statement is limited to inspected passages. The records contain a separate digest inconsistency, handled under reproducibility. | None for source contradictions; apply D1 for the input-record inconsistency. |
| uncertainty | PASS / none | R1:20,30,34,40-51, O4. Historical scope, actual representation, omitted broad searches and lack of retained originals remain explicit. No unsupported confidence number, conformance assurance or independent-human-review claim appears. The producer PASS table was not used as evidence of support. | None. |
| reproducibility | FAIL / low | D1, X1:11, F1:files.prompt.txt, H1, H2. execution.json labels a digest prompt_sha256 without identifying that it matches bytes.rstrip(), while the fixed prompt file has a different exact-byte digest. This undocumented normalization makes the input identity record inconsistent. Source paths and the report digest are otherwise reconstructable. | D1: producer A10/W04 metadata revision; record the exact raw-file digest and explicitly label any retained normalized-text digest. Preserve the fixed submission and this review, freeze the corrected revision, then re-audit identity/provenance only unless substantive inputs change. |

## Separate domain criteria

| Criterion | Verdict / severity | Case-grounded evidence and reason | Smallest repair |
|---|---|---|---|
| K01 | PASS / none | P1:1, R1:7-11. Question and intended-use boundary match. | None. |
| K02 | PASS / none | X1:36-74, R1:34-38. Actual recorded source boundary is stated without a web-completeness claim. | None. |
| K03 | PASS / none | R1:17-20,34, O1, O2, O3. Source representations and locators are recoverable; exact historic response bytes were not retained. | None for this exact-label task. |
| K04 | PASS / none | R1:17-20, O2, O3. Distinct document identities and shared family are preserved. | None. |
| K05 | PASS / none | P1:1, O1, O2, O3. Direct original-document inspection fits a self-status observation. | None. |
| K06 | PASS / none | R1:20. No false independent support count; separate-origin corroboration is unnecessary for this proposition. | None. |
| K07 | PASS / none | R1:26-28, O1, O2, O3. E1-E3 preserve the source labels, date and document scope. | None. |
| K08 | PASS / none | R1:30,34, O4. Inspected status caveats are compatible with the bounded answer; no eligible contrary passage was discarded. | None within the inspected boundary. |
| K09 | PASS / none | R1:11,27-30, O1, O2, O3. The modest category distinction follows without an unsupported conformance inference. | None. |
| K10 | PASS / none | R1:20,30,34. Access and temporal limitations survive into the report. | None. |
| K11 | PASS / none | R1:34, O1, O3, O4. Publication, retrieval and edition applicability are not substituted. | None. |
| K12 | PASS / none | R1:40-51, H1, H2, reviewer/process. The producer check is labelled; this is a separate agent review of exact fixed bytes. No human or install certification is claimed. | None; no qualified-human gate applies to the requested observation. |
| K13 | FAIL / low | D1, X1:11, F1:files.prompt.txt, H1, H2. An exact input digest and an undocumented normalized-text digest disagree. | D1: A10/W04 metadata correction in a new revision, followed by L01/K13 recheck. |
| K14 | PASS / none | B1:15-17, X1:36-74, source_actions. The producer records two actions; this reviewer used three, all necessary to expose the checked passages, with zero queries. No capacity was treated as proof of sufficiency. | None. |
| K15 | PASS / none | P1:3, B1:15, X1:36-41, reviewer/process. Observed review uses authorised local/native-web tools; no paid run, purchase or external communication was made. Historical producer non-acquisition conduct is not independently replayed. | None on available evidence. |
| K16 | PASS / none | H1, H2, D1. Inputs remain fixed and the recommendation isolates the provenance repair while preserving verified source findings. | Perform D1 only in a separately authorised changed revision; no repair was executed here. |

## D1 — input-digest normalization is not identified

- Location: `execution.json:11`, `prompt_sha256 = db135db41ddf70fc351eac8b218309b98ad422fef4dad1ab956f48bd6f0fc9ab`.
- The fixed `prompt.txt` raw-file digest is `767ae9980659356a0b64c7d5528b62d221df74ad00abe20ea81973789dc89dd9`.
- Local computation demonstrated that `sha256(Path("prompt.txt").read_bytes().rstrip()).hexdigest()` exactly equals the recorded execution value. This identifies a trailing-whitespace normalization mismatch; it does not establish a materially different prompt or tampering.
- Verdict: FAIL, low severity, L01/K13. The prompt identity is required to reconstruct the submitted run, and the normalization is not named. The correct fixed manifest prevents ambiguity about what this reviewer assessed.
- Owner and smallest repair: producer A10 material provenance, W04 identity/representation metadata. Preserve this fixed revision and review; create a new metadata revision that records the exact raw-file digest. If retaining the old value, label it as normalized text and record `bytes.rstrip()` explicitly. Re-freeze and re-audit the affected identity/provenance fields. No new source acquisition or answer change is needed unless the substantive inputs also change.
- Diagnostic class: F13 identity/preservation confusion, narrowly limited to digest semantics. No repair was executed by this reviewer.

## Source action accounting

| Action | Actual recoverable operation | Outcome |
|---|---|---|
| SA1 | `tools.web__run`, `open` of `https://www.w3.org/TR/prov-primer/`, in SC1; `response_length=long` | PASS: original HTML-derived text exposed O1/O2/O4. |
| SA2 | Same SC1, second `open` of `https://www.w3.org/TR/2013/REC-prov-dm-20130430/` | BLOCKED at that step: title/URL/content identity returned, body passages absent from displayed result. Charged once; not treated as substantive verification. |
| SA3 | SC2, `tools.web__run`, `open` of the same PROV-DM URL with `lineno=0`, `response_length=long` | PASS: header/status body returned; resolved SA2 and supported O3/O4. |

**Actual reviewer use: 3 external source actions in 2 native web calls, 0 search queries, 2 distinct source URLs.** Allocation: 3 actions, now exhausted. Each requested URL operation is charged, including the body-less result and reopen; local reads, hashes, git inspection and output writes are separate. The fixed producer record reports 2 actions and 0 queries, so recorded producer plus actual review use is 5 of the task ceiling of 8 actions and 0 of 3 queries. The brief reserves 2 actions for repair; D1 needs none. No source jobs remain outstanding. Source-call dates are known only to the day (2026-09-12); exact arguments and per-action outcomes are in `review.json`.

## Applicability, omissions and limits

- No requested audit scope was omitted. L08 Extension Pack testing is NOT APPLICABLE because none was selected. L10 clean-install/host-discovery testing is NOT APPLICABLE because this is explicitly source-checkout execution. Whole-suite L09 acceptance is NOT APPLICABLE to this one-case review. Each has no repair within this task.
- Qualified human/specialist approval is NOT APPLICABLE to the requested document-label observation; this review supplies none.
- Original-source inspection used native HTML-derived text. No browser rendering, historic source snapshot, exact response-body hash or source archive was available in the submission or created here. The reviewer confirms the live returned passages, not the exact producer response bytes.
- No broad standards-family, subsequent-status, errata, implementation-conformance or global web-recall audit was performed. These are outside the brief. The relevant originals were accessible after the charged reopen.
- The producer operation log provides recoverable source routes and outcomes; no historic host transcript was independently replayed. Producer source use is therefore distinguished from the reviewer’s directly observed calls.
- Only the two new evaluation files were written. Submission files and skill bytes remained unchanged; no commit or GitHub state change was made.

Next permitted operation: producer metadata-only repair of D1 in a preserved new revision, followed by a separate fixed-input check of the affected provenance. The supported source findings can be retained.
