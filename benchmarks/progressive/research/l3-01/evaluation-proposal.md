# Proposed software-team evaluation

Revision **L3-01-r2**, 2026-09-13. **Proposal only: no dataset built, annotations commissioned, model calls made, benchmark run, or result observed.** This is the downstream application experiment, separate from the parent's fixed-input audit of this report.

## Question and decision

Can full-context reading replace retrieval **within a defined evidence packet**, at acceptable evidence fidelity, completeness, cost and latency? Separately, can an end-to-end workflow preserve source acquisition, version resolution and refresh? Keep those two questions separate so better source access is not mistaken for better reading.

The motivating mechanisms are C1–C4 in `research.md`. The design below is the producer's proposed transfer test, not a protocol performed in those studies. Numerical sample sizes and decision margins below are planning choices, not derived benchmark thresholds.

## Fixed inputs and comparison arms

Start with a 24-task pilot for rubric/debugging, then a separate 120-task held-out set, with 20 tasks in each of six strata: exact fact with locator; support distributed across two or more documents; comparative synthesis including adverse evidence; competing versions/corrections; answer absent or genuinely indeterminate; and bounded evidence refresh. Use authorized software-team research material representative of the intended corpus. Include difficult cases independent of which architecture is expected to win.

Before any future run, a team member establishes answerable claims, required supporting spans, report/version relationships and allowable unresolved outcomes. A second reviewer checks disputed gold labels. This review is proposed, not completed. Keep test answers separate from candidate prompts and tuning inputs. Preserve source snapshots with ordinary exact document/version locators; do not invent a private oracle or claim unseen reference answers were used in this research report.

Compare three primary arms with the **same model version**, evidence corpus, question, citation instructions, decoding settings, output limit and permitted tools:

1. Full-context: all evidence documents supplied, with source IDs and version/date labels.
2. Retrieval: fixed corpus indexed; tuned chunking, top-k and reranking selected on pilot/dev material and then locked.
3. Hybrid: retrieval followed by an explicit, locked expansion/full-context policy. Record the cost and outcome of every fallback.

Include a gold-evidence-only diagnostic input to distinguish failures in selection from failures in using supplied evidence. It is a controlled diagnostic, not a deployable competitor. For multi-hop questions, include a tuned iterative retrieval variant if that is the team's intended alternative; comparing only weak single-shot retrieval would not test the actual decision.

Pin executable/data/model/prompt/retriever versions before execution. If using auxiliary diagnostics, start from the retained original LongBench implementation pinned in `study-report-map.md` and select original RULER/Lost protocols explicitly; current repository defaults may describe later benchmark generations. The recovered LongBench code is not proof of historical paper-execution bytes. Do not execute installation commands or spend money under this proposal's authority.

## Conditions and contamination controls

For 30 representative held-out tasks, produce five orderings that place required support near beginning, quarter, middle, three-quarter and end positions. Cross with two distractor loads on that subset; use the same base task across arms. Report clustered uncertainty because order variants are not independent tasks. Add deliberately separated multi-hop support and contradictory distractors. Keep genuine evidence content constant when testing position.

Measure actual tokens with each selected model tokenizer; reserve room for instructions, output and any reasoning allowance. Report feasible-window and beyond-window strata separately. Do not silently middle-truncate full-context inputs: mark overflow and evaluate the team's declared overflow policy separately. A words/characters label is not a token-budget measurement.

Use evidence unavailable in general pretraining where authorized, plus controlled altered-fact packets and unanswerable cases, to expose reliance on prior knowledge. Keep source changes documented. Evaluate English and other required languages separately; do not assume bilingual benchmark coverage transfers to the team's distribution. Freeze corpus snapshots for reading comparisons, then introduce a recorded source revision for refresh tests.

## Outcomes and analysis

| Outcome | Operational measure | Why it changes the decision |
|---|---|---|
| Claim support | Supported factual claims / all factual claims, adjudicated against cited spans | Answer similarity alone can reward an unsupported statement |
| Evidence completeness | Required evidence units found and used / gold required units; also all-required-units success | One retrieved fact does not establish complete multi-hop support |
| Citation correctness | Correct source/version and locator, plus citation entailment; report separately | Valid URL syntax is insufficient |
| Contradiction/version handling | Tasks correctly preserving conflict or choosing applicable version / eligible tasks | Essential to evidence-led research |
| Appropriate uncertainty | False answers on unanswerable tasks; unnecessary abstentions on answerable tasks | A cautious-looking output can still mislead or fail usefulness |
| Position and distractor robustness | Best-minus-worst and middle-minus-edge differences on paired tasks | Measures the transfer risk exposed by the originals |
| Acquisition/refresh coverage | Required authoritative sources discovered; affected claims updated; unaffected valid evidence retained | Needed for a whole-workflow claim |
| Operating performance | Measured per-task input/output tokens, complete cost including index/routing/refresh, wall-clock p50/p95, failures | Historical token savings are not current total operating cost |

Mask architecture identity during human scoring where possible. Log disagreements and adjudications. Preserve raw outputs and exact prompts for error inspection. Use task-level paired differences with 95% confidence intervals; resample whole tasks, keeping their order variants together. Report per-stratum results and absolute counts alongside any overall mean; never hide critical citation/version failures inside a broad average. The pilot should estimate variability and whether 120 tasks can resolve the chosen margin. Expand only under new authorized effort if precision is inadequate; a wide interval means inconclusive.

## Proposed acceptance logic

Before looking at held-out outputs, the team should choose and record minimum support/completeness levels, maximum false-answer rate, noninferiority margins, and cost/latency ceilings according to its actual use. As a **draft discussion starting point**, consider a two-percentage-point noninferiority margin for both claim support and evidence completeness, with no observed critical wrong-version or fabricated-source failures in the held-out set. These are not calibrated safety guarantees, universal standards or RULER's 85.6% threshold. Zero observed critical errors still leaves uncertainty, especially within small strata.

Replace packet-level retrieval only if full-context reading meets the preregistered quality constraints with adequate confidence and its operating costs are acceptable. Prefer the hybrid arm if it meets the same quality constraints more efficiently. Retain retrieval if full-context overflow, selection, position or freshness failures remain material. If tradeoffs vary by stratum, route by a tested policy rather than issuing a universal winner. If confidence intervals cross decision margins, record no decision and the specific additional evidence needed.

For the separate whole-workflow test, hold source/tool access and acquisition budget constant across candidate pipelines; include finding originals, resolving versions, following adverse evidence, writing claim-linked synthesis and refreshing a changed source. Manually assess the preserved evidence trail. Packet-reading success alone cannot pass this test. No whole-workflow replacement is justified before that outcome is measured.

The software team owns execution authority, model/service access, corpus disclosure and acceptance values. This proposal grants none of those. The present authorized deliverable ends with a reviewable design and open support needs.
