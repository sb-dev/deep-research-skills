# L1-01 — actual core research vertical

This consumer workspace records a real execution of the [accepted public prompt](../../../examples/level-1-prov-primer-publication-status/README.md) using the `deep-research` and `research-evaluate` source-checkout packages at `0d708a7fee2ec95effb345d10677b2c53f292155`. The host was ChatGPT Work Mode / Codex; its exact model build was not exposed. No Extension Pack was selected.

Current assessment: **accepted after metadata repair**. The original full audit supplies eight unchanged scope findings; the focused re-audit closes reproducibility and verifies their unchanged dependencies. The [combined execution result](result.json) identifies both assessments without relabelling either review.

## Actual inputs and outputs

| Record | Original submission | Corrected metadata submission |
|---|---|---|
| Submission identity | `run-2026-09-12-01` | `run-2026-09-12-02` |
| Exact task | [prompt.txt](prompt.txt) | [preserved prompt](revisions/run-2026-09-12-02/prompt.txt) |
| Pre-collection frame/plan | [brief-and-plan.md](brief-and-plan.md) | [preserved brief/plan](revisions/run-2026-09-12-02/brief-and-plan.md) |
| Runtime, operations, source use and identities | [execution.json](execution.json) | [corrected execution.json](revisions/run-2026-09-12-02/execution.json) |
| Producer report | [research/l1-01/research.md](research/l1-01/research.md) | [byte-identical report](revisions/run-2026-09-12-02/research/l1-01/research.md) |
| Fixed review input | [fixed-input.json](fixed-input.json) | [new fixed-input.json](revisions/run-2026-09-12-02/fixed-input.json) |
| Separate reviewer request | [original audit request](review-request.txt) | [focused re-audit request](revisions/run-2026-09-12-02/review-request.txt) |
| Actual evaluation | [full audit](research/l1-01/evaluation/audit.md), [metadata](research/l1-01/evaluation/review.json) | [focused re-audit](revisions/run-2026-09-12-02/research/l1-01/evaluation/audit.md), [metadata](revisions/run-2026-09-12-02/research/l1-01/evaluation/review.json) |

The report identifies the question, answer, source inspection, extracted evidence, supported claims, temporal scope, uncertainty and producer self-check. The source operations and actual reviewer inspections establish the semantic evidence. File hashes separately establish input and preservation identities.

## Observed execution and repair

The producer framed the exact-source question, reserved review effort, opened the supplied official page, followed a relevant original-document link, extracted evidence, analysed claim support and synthesised the report. It stopped after two source actions and zero queries.

The first reviewer ran the packaged `audit` operation in a fresh agent task, inspected original source passages, and separately assessed all nine dimensions. Eight passed. Reproducibility failed: `execution.json.prompt_sha256` matched prompt text without its terminal whitespace, while the field did not name that normalization. The fixed-input manifest itself correctly identified the raw bytes.

The [executed repair receipt](repair.json) identifies the owning provenance-metadata layer and preserved files. The [repair script](../../../docs/research-logs/2026-09-12-stage-19-repair.py) created a new submission, assigned the raw-file digest to `prompt_sha256`, and separately labelled the accepted prompt text digest with an exact single-terminal-LF transformation. It retained the original report revision and source acquisition identity. The original submission and its failed audit remain historical evidence.

The focused second audit checks the actual changed revision and dependency preservation. Its recorded scope determines whether previous semantic findings can be retained; it is not presented as a fresh full source audit.

## Bounds and limitations

The task ceiling is three search queries and eight external source reads/actions across producer, review and repair. Actual use was **five source actions and zero queries**: two producer actions, three original-review actions, zero metadata-repair actions and zero focused-review actions. The original review charged a body-less source result and its necessary successful reread. Local contract reads, hashing, revision writes and Git publication are separate from source acquisition.

Source inspection used original HTML represented by native web text. Exact historical response bodies were not retained. The report's edition and retrieval scope, and both reviews' access limitations, remain part of the evidence. This one execution supports the recorded source-checkout path and bounded metadata repair. Installation, multiple hosts, pack effects and broader research repair remain separate proof obligations.

Run the recorded integrity check from the repository root:

```sh
python docs/research-logs/2026-09-12-stage-19-verification.py
```

It reproduces the historical metadata defect and an [observed draft review-table error](fixtures/audit-table-before-qa.md) as negative controls, checks the corrected identities, preserves both submissions and validates local links. It does not score factual research support; read the actual audits for that assessment.
