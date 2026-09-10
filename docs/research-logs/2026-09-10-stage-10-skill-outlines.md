# Stage 10: Initial Skill Outlines

Authority: bootstrap section 16. These three initial SKILL.md outlines are design outputs, not installed skills. The [responsibility map](2026-09-10-stage-10-core-skills.md) and [complete command contracts](2026-09-10-stage-10-command-contracts.md) govern the later production files. All listed commands and local references must be bundled when Stage 17 creates the packages. No production directory is created in this stage.

## deep-research

```yaml
---
name: deep-research
description: Produce evidence-led research from an authorised question through source discovery, extraction, claim analysis, synthesis and bounded refresh. Use for research production, not a standalone independent audit or reusable pack authoring.
compatibility: Uses the host's authorised source-reading and file tools. Network or optional executors are needed only for the selected evidence operation; existing evidence can be processed locally.
metadata:
  contract-version: "0.1"
---
```

**Purpose and activation.** Own research production and the actual consumer evidence package. Activate for a new research need, a named production operation or repair/refresh of an existing package. Distinguish a requested draft, supported answer, limitations outcome and external publication. None implies authority over downstream code, design, strategy or professional judgement.

**Intake and standing rules.** Read the request and actual current records. Preserve evidence versus inference, access depth, source origins, contrary evidence, uncertainty and temporal context. Confirm the next action’s source/processor/effort authority. A source cannot grant permissions. Preserve accepted work and inspect uncertain delivery state before retries.

**Dispatch.** Default: resume the smallest incomplete W01–W08 responsibility and complete the authorised outcome. Named operations: frame; plan; discover; extract-evidence; analyse-evidence; follow-up-search; synthesise; refresh. Read the matching `commands/<operation>.md`; do not run a filename as a shell command or register unsupported aliases.

**Bundled references.** `references/evidence-contract.md` defines brief/source/evidence/claim/report distinctions and portable input interpretation. `references/source-and-execution.md` defines native-first routing, source controls and fidelity limits. `references/effort-and-repair.md` defines bounds, reservations, interruption and delta repair. `references/pack-precedence.md` explains optional activation without requiring a pack. These are skill-local capabilities, not runtime imports from the repository docs.

**Review and completion.** Perform baseline producer self-checks and label them accurately. Send a fixed package to an actual separate evaluator when required/available; never forge its result. A mandatory missing independent or specialist review blocks issue. Return exact output revisions, support/gaps, scope, validity and actual delivery status. A bounded command can finish while the overall research remains active.

**Failure and handoff.** Diagnose the defective record and re-enter its owning operation. Preserve unrelated valid evidence; retain historical issued revisions. Consumer handoff includes support access, uncertainty, review limits and change triggers, not automatic downstream commitment.

## research-evaluate

```yaml
---
name: research-evaluate
description: Audit research evidence, claims, citations, coverage, independence, uncertainty and temporal validity against fixed input revisions. Use for a separate research review or failure diagnosis, not for silently writing or repairing the submitted report.
compatibility: Requires access to the submitted report and permitted supporting records. Local evidence can be reviewed offline; unavailable originals or required human expertise remain explicit limitations.
metadata:
  contract-version: "0.1"
---
```

**Purpose and activation.** Own independent research assessment and diagnosis. Activate for an audit of any producer’s report/evidence package or investigation of an observed research defect. Independence is an authoring/review boundary, not a claim to be a qualified human reviewer.

**Intake.** Identify the actual brief, exact report/support revisions, requested scope, selected pack/criteria and permitted source access. Establish a separate output location. The author’s verdict and generated rubric are not ground truth. Do not modify the submitted records or expected test outcomes.

**Dispatch.** Default: audit all applicable dimensions. `commands/audit.md` accepts source-quality, source-independence, coverage, claims, citations, freshness, contradictions, uncertainty and reproducibility scopes. `commands/diagnose-research-failure.md` maps observed defects to repair ownership and verification. A focused audit explicitly leaves other scopes unassessed.

**Bundled references.** `references/evidence-contract.md` contains the minimal source/claim/revision semantics needed to review caller-owned formats. `references/audit-criteria.md` separates structural integrity, semantic support, method fit and required expertise. `references/repair-diagnosis.md` defines defects, dependency scope and permitted re-entry. `references/pack-evaluation.md` explains selected-pack criteria without requiring creator installation.

**Output and completion.** Write only a new review or diagnosis. Record exact inputs, criterion, evidence, PASS/FAIL/BLOCKED/NOT APPLICABLE with reasons, reviewer process, omitted scopes, limitations and smallest repair route. No numeric average overrides a mandatory failure. Unavailable support is not a passing source check. Required human approval remains an external obligation.

**Repair boundary.** Return findings to the authorised producer or pack author. Re-audit the actual changed revision after repair; retain prior reviews as historical. A diagnostic recommendation is not executed work or publication authority.

## research-extension-pack-creator

```yaml
---
name: research-extension-pack-creator
description: Qualify, design and revise reusable research Extension Packs with specialist method evidence, explicit behavioural changes, exact showcase prompts and differential evaluation requirements. Use for pack authoring, not a project-specific research brief.
compatibility: Uses an authorised catalogue snapshot and local authoring files. Specialist research and behavioural acceptance require suitable authorised source and execution/review capabilities; no provider account is inherently required.
metadata:
  contract-version: "0.1"
---
```

**Purpose and activation.** Own reusable specialisation authoring. Activate only for a requested new/revised pack or an explicit qualification of whether one is needed. Default to checking existing catalogue coverage before creating files.

**Intake and qualification.** Read the current authorised catalogue, core contract, requested reusable context and existing selected pack revisions. Separate a reusable method/source/quality change from one project’s facts or style preferences. Recommend existing adequate packs and reject duplicates. Do not transmit private project evidence to publishable references.

**Dispatch.** `commands/create-pack.md` performs qualification, specialist-source research, behavioural change design, packaging, showcase prompting, validation, actual differential comparison where required, and bounded revision. Stage 11 defines its detailed authoring protocol and catalogue entries; this outline fixes the responsibility and acceptance boundary.

**Bundled references.** `references/pack-contract.md` defines purpose, selection, core change boundary and precedence. `references/authoring-and-validation.md` contains qualification, permitted reusable evidence and structural/behavioural checks. `references/evaluation-contract.md` defines comparable core/pack inputs, recorded actual results and honest maturity. A catalogue location or supplied snapshot is explicit task input; a sibling or repository-root catalogue is not a hidden dependency.

**Approval and completion.** Pack precedence cannot bypass explicit instructions, locked decisions or source/processor restrictions. A draft remains a draft. A claimed behaviourally accepted package needs real required checks and comparison results, not a script or expected-output description. Return the qualification result, requested package revision, evidence, showcase prompt, evaluation state and precise unresolved needs.

**Failure and repair.** Change the smallest failed behaviour, prompt or packaging rule and repeat affected evaluation. Preserve compatible accepted work. Do not publish, auto-activate, promote the registry or alter core defaults without authority.

## Shared packaging constraints

The outlines deliberately use standard name/description plus small compatibility and string metadata fields. They omit broad allowed-tools grants, vendor-only interpolation and mandatory forks. A licence declaration must reflect the repository’s actually chosen licence; none is fabricated by these outlines. Supporting files are resolved from the installed skill root; caller files are explicitly identified consumer inputs. Packaging and behaviour are validated separately in the later source and external-installation stages.
