# Stage 16 — Deep Research Public Claims Ledger

**Status:** Internal bootstrap evidence contract  
**Date:** 11 September 2026  
**Public surface:** none — do not copy this ledger into `README.md`

This ledger separates target product copy from the evidence required before final publication.

| Public claim | Owning evidence gate | Current evidence state after Stage 16 | Publication rule |
|---|---|---|---|
| `deep-research` is an installable skill | Stage 21 local installation + Stage 23 clean external installation | Target contract only | Keep only after actual installation evidence |
| `research-evaluate` is independently installable | Stages 21 and 23 selective-install cases | Target contract only | Keep only after evaluator-only installation succeeds |
| `research-extension-pack-creator` is independently installable | Stages 21 and 23 selective-install cases | Target contract only | Keep only after creator-only installation succeeds |
| Claude Code installation command works | Stage 23 clean consumer smoke test | Target command only | Verify exact installer/revision/host before publication |
| any additional host is supported | Stage 23 host-specific clean test | No claim authorised | Add only after actual host evidence |
| L1-01 produces `research/l1-01/research.md` with the documented evidence semantics | Stage 19 core vertical + Stage 23 clean consumer rerun | Prompt/design evidence only | Require actual producer output and inspection |
| `research-evaluate` can audit fixed producer output independently | Stage 19 core vertical | Contract only | Require actual fixed-input evaluation evidence |
| bounded repair preserves unaffected verified work | Stage 19 core vertical and regression evidence | Design/eval contract only | Require observed repair evidence |
| all fifteen primary examples are usable production examples | Stage 20 progressive execution | Prompts/designs exist | Require all fifteen substantive executions |
| `scholarly-evidence` materially changes research behaviour | Stage 20 core-vs-pack differential | Design/profile evidence only | Require comparable core-vs-pack execution |
| `open-source-ecosystem` materially changes research behaviour | Stage 20 core-vs-pack differential | Design/profile evidence only | Require comparable core-vs-pack execution |
| pack authoring/revision works | Stage 20 pack-creator cases | Contract only | Require at least one valid author/revision case and one reuse/reject case |
| benchmark or quality result | Stage 20/22 executed suite | No public measured claim authorised | Publish only measured, scoped results |
| local selective installation works | Stage 21 | No execution evidence | Keep internal until executed |
| clean external installation works | Stage 23 | No execution evidence | Required for external product acceptance |
| public example links resolve | Stage 18 scaffold + Stage 22 conformance | Public example directories do not yet exist | Add links when surfaces exist, then validate |
| contribution workflow exists | Stage 18 scaffold | Target surface only | Link only after `CONTRIBUTING.md` exists |
| repository licence | Stage 18 owner decision/scaffold | No licence decision inferred here | Do not name a licence until explicitly selected |
| Pactwright compatibility | Stage 24 if implemented | Optional, no public claim required | Add only if actually implemented and tested |

## Reconciliation rule

At Stage 23:

```text
supported
→ keep

partially supported
→ narrow to demonstrated scope

unsupported but required for release
→ finish the owning work or block publication

unsupported and non-essential
→ remove
```

The absence of evidence is handled here, not by turning the public README into a list of unfinished bootstrap stages.