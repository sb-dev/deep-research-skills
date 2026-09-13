# L4-02 change record — r1 → D1 → r2

## Preserved baseline and observed findings

`provisional/` freezes the unmodified original comparison, calculation, manifest, original results and observed outputs before repair. `before-repair-identities.json` records exact SHA-256 identities. The real findings—shared snapshot keys, changed row contents/statuses/categories, and the new unpowered summary resource—remain unchanged. None is labelled an invented defect.

No natural arithmetic defect was found in the original calculation. The authorised demonstration used a **clearly labelled copy**, `demonstration-error.csv`: one denominator at 202507/powered/ALL/Fixed excluded Unknown (296,902), with its fraction recalculated from that wrong denominator. This was not a dataset mutation or an observed dataset defect. `demonstration-error.md` retained the intentionally false dependent all-status-share sentence.

## Actual independent diagnosis precedes repair

The parent evaluator wrote `evaluation/diagnosis.md` (D1), independently hashing and streaming both complete powered inputs. D1 returned material denominator-scope FAIL for the demonstration, identified analyse-evidence as owner and authorised changing only that denominator, its derived share and the one dependent sentence. No data reacquisition, category correction or whole calculation rerun was required.

## Executed repair and review scope

`python benchmarks/progressive/research/l4-02/repair.py` actually ran after D1. It calculated the all-status denominator from existing status counts and emitted `demonstration-repaired.csv`. Before: 165,144 / 296,902 = 0.556223939212 (55.6224%). After: 165,144 / 305,649 = 0.540306037317 (54.0306%). `demonstration-repaired.md` corrects the dependent claim. A report addendum records that correction and the pending revision review; valid original findings are untouched.

| Identity | SHA-256 |
|---|---|
| Wrong demonstration CSV, preserved | a499008c1c36b06073238902124b242856402e3bbb70103e732b24ad346a996b |
| Repaired demonstration CSV | 082987fcb19339207aa0e7548bfd428bbee90ccfeb236737c5731917ba0be7a2 |
| Original provisional results.csv | 082987fcb19339207aa0e7548bfd428bbee90ccfeb236737c5731917ba0be7a2 |
| Original provisional research.md | 739e67c9edb9fef90f424f59eba1f4e632b160bb2259a5266699a5f36e5008f1 |
| Report with r2 addendum | dcd6208314e2e96d76c7efc6a94785e62f47fb7a57531ae005f9f05ec2b51211 |

Observed delta: 1 row, 2 dependent fields (denominator and fraction); 103 unaffected CSV rows. Repaired CSV is byte-identical to original `provisional/results.csv` and production `results.csv`. The code asserted preservation of every frozen baseline hash. Production `calculation.py`, `results.csv`, `observed.json`, `input-manifest.json`, `coverage.csv`, `category-counts.csv`, `category-transitions.csv`, `provider-overlap.csv` and `execution-resources.json` are byte-identical to their provisional copies. Source CSVs were read-only and their original identities remain in the manifest; no originals were replaced.

Affected review dependencies: D1's failing demonstration row/claim must receive revision review against the fixed r2 copies; the report addendum and this change record require consistency checks. Unrelated valid calculations, mappings and baseline evidence retain their existing basis. Parent owns `evaluation/audit.md`; producer has performed only the described self-checks and does not issue a PASS.

Repair effort: one bounded local CSV repair and byte-preservation check, no new external source read/search, no additional acquired data, no installation/payment/contact. Acquisition remains 98,743,984 bytes. After D1: 21/64 conservatively charged acquisition-plus-review actions (22 including the one search call), two query strings; final review expenditure is additional and recorded by evaluator. Resumption should inspect current results and reuse these inputs, revising only changed dependencies.
