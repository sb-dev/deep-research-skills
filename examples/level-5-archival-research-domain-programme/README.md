# L5-01 — Archival-research domain programme

[All research examples](../../README.md#learn-by-researching)

## Problem

Research a new Production Skills domain before architecture design and qualify whether a new Extension Pack is justified.

## Exact prompt

Run this prompt in a consumer project with the skill selection it names.

```text
Use installed deep-research, research-evaluate and research-extension-pack-creator. Begin with no Extension Pack activated. Research a proposed archival-research Production Skills domain before architecture design. Start from professional archival guidance and public research/finding-aid resources of The National Archives (UK), the US National Archives and W3C provenance documents; follow relevant originals within a declared source strategy. Define questions about provenance, discovery, missing records, representations, interpretation, privacy/rights and review. Topic-specific factual claims require actual source inspection.

Use https://github.com/sb-dev/deep-research-skills/blob/30c14c5b0dd22d5a63ce875f12ad7b0528183b35/docs/research-logs/2026-09-10-stage-11-profiles.json as the explicit initial catalogue snapshot. Run create-pack to decide whether an existing pack plus project instructions is enough or a reusable archival specialisation is justified. A justified new proposal may remain a labelled draft with an exact showcase and comparison requirements; do not falsely mark it accepted or installed. Do not scaffold a repository or treat a missing catalogue entry as proof that an event did not happen.

Allow 30 searches and 96 source reads/actions total, reserving review and handoff effort. Use authorised tools only; no purchases, new paid agents, private-source disclosures or contact with people. Write research/l5-01/research.md, programme-map.md, pack-qualification.md, handoff-software.md, handoff-ux.md, review-needs.md and evaluation/audit.md beneath research/l5-01/. Preserve source/evidence/claim links, unknowns and expert decisions for the receiving owners. Read and preserve existing revisions. Return actual files and truthful research/authoring status without taking over software, UX or professional approval.
```

## Expected artefacts

- `research/l5-01/research.md`
- `research/l5-01/programme-map.md`
- `research/l5-01/pack-qualification.md`
- `research/l5-01/handoff-software.md`
- `research/l5-01/handoff-ux.md`
- `research/l5-01/review-needs.md`
- `research/l5-01/evaluation/audit.md`

## Evaluation contract

Evaluate research-before-architecture, catalogue-first qualification and explicit handoff ownership. The creator qualification can also be tested as a selective-install subtask using the explicitly supplied catalogue and programme request.

Catalogue-first create-pack qualification and research-before-architecture; FX11/AU01, pack precedence suite. All three skills; creator-only qualification also tested selectively.

Review the actual source access, evidence and claim support, temporal scope, uncertainty, resource bounds and preservation required by the prompt. Distinguish producer self-checks from fixed-input independent evaluation. A passing structural check does not establish research quality.

Benchmark mapping: `EX-L5-01`; L05/L08/L09; K01/K15/K16. See the [evaluation layers and quality dimensions](../../docs/04-testing-and-benchmark-spec.md).

## Recorded execution

[Progressive run](../../benchmarks/progressive/research/l5-01/research.md) contains the actual source-checkout output and its stated support and access limits. See the [separate review](../../benchmarks/progressive/research/l5-01/evaluation/audit.md) for assessed claims and remaining gaps.
