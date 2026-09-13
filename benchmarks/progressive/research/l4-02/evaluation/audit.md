# L4-02 — Independent final audit A1

2026-09-13. Primary assistant, separate from producer, applied actual research-evaluate/audit all nine scopes at core0.1, no pack, to fixed r2 report, input manifest, calculation and actual result/repair files. D1 is preserved in diagnosis.md. No producer file changed.

Actual checks: independently streamed both powered originals and verified their byte counts/hashes; counted every status including Unknown; inspected calculation and equivalent powered schemas plus40-category codelist; ran read-only SQLite joins for shared keys, status/category changes and within-snapshot duplicates; compared actual error/repaired/provisional/result files. Repaired CSV equals valid original exactly, one row has two dependent fields changed,103rows unchanged. No external acquisition or query; conservatively nine review source/input inspections including D1, total27/64actions (producer18conservative),2/20queries. Existing98,743,984acquired data bytes remain below150MB.

| Scope | Verdict | Evidence |
|---|---|---|
| Source quality | PASS for descriptive reconciliation | Complete pinned original snapshots and actual release schemas; underlying collection not independently validated. |
| Independence | PASS | Cumulative snapshots linked by provider+ID; shared records not added as new events. |
| Coverage | PASS | Both powered snapshots and202507unpowered summary processed; unavailable202407unpowered remains unavailable. |
| Claims | PASS | Independent powered counts208491/305649; Fixed110731/165144; Unknown7268/8747. Read-only joins reproduce201201sharedkeys,5277statuschanges,15364categorychanges. |
| Citations | PASS | Exactcommit/path, hashes, schemas, original-inputmanifest and executed outputs present. |
| Freshness | PASS | Snapshot/end-of-observation/release/retrieval dates distinct; no current-year population inference. |
| Contradictions | PASS | Stable definitions do not hide actual recoding; changed rows and removed/newkeys retained. |
| Uncertainty | PASS | No household-rate, provider-quality, independence, causality or missing-as-zero claim. |
| Reproducibility | PASS within supplied-input scope | Standard-library bounded-memory code, hashes and real outputs; bulk inputs are fetched from manifest URLs and passed with documented overrides, using a fresh work DB path. |

Repair PASS: the prompt-permitted synthetic denominator error was clearly separated from observed dataset findings, frozen before D1, repaired after independent diagnosis, and independently compared. Correct all-status202507Fixed fraction165144/305649=0.540306037317315. No original result, input or unrelated row was silently altered. These checks establish this finite calculation and repair, not statistical representativeness or installed-skill performance.
