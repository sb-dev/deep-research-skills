---
name: research-evaluate
description: Audit research evidence, claims, citations, coverage, independence, uncertainty and temporal validity against fixed input revisions. Use for a separate research review or failure diagnosis, not for silently writing or repairing the submitted report.
license: MIT
metadata:
  contract-version: "0.1"
---

# research-evaluate

**Compatibility.** Requires access to the submitted report and permitted supporting records. Local evidence can be reviewed offline; unavailable originals or required human expertise remain explicit limitations.

**Purpose and activation.** Own independent research assessment and diagnosis. Activate for an audit of any producer’s report/evidence package or investigation of an observed research defect. Independence is an authoring/review boundary, not a claim to be a qualified human reviewer.

**Intake.** Identify the actual brief, exact report/support revisions, requested scope, selected pack/criteria and permitted source access. Establish a separate output location. The author’s verdict and generated rubric are not ground truth. Do not modify the submitted records or expected test outcomes.

**Dispatch.** Default: audit all applicable dimensions. [audit](commands/audit.md) accepts source-quality, source-independence, coverage, claims, citations, freshness, contradictions, uncertainty and reproducibility scopes. [diagnose-research-failure](commands/diagnose-research-failure.md) maps observed defects to repair ownership and verification. A focused audit explicitly leaves other scopes unassessed.

**Bundled references.** [evidence-contract](references/evidence-contract.md) contains the minimal source/claim/revision semantics needed to review caller-owned formats. [audit-criteria](references/audit-criteria.md) separates structural integrity, semantic support, method fit and required expertise. [repair-diagnosis](references/repair-diagnosis.md) defines defects, dependency scope and permitted re-entry. [pack-evaluation](references/pack-evaluation.md) explains selected-pack criteria without requiring creator installation.

**Output and completion.** Write only a new review or diagnosis. Record exact inputs, criterion, evidence, PASS/FAIL/BLOCKED/NOT APPLICABLE with reasons, reviewer process, omitted scopes, limitations and smallest repair route. No numeric average overrides a mandatory failure. Unavailable support is not a passing source check. Required human approval remains an external obligation.

**Repair boundary.** Return findings to the authorised producer or pack author. Re-audit the actual changed revision after repair; retain prior reviews as historical. A diagnostic recommendation is not executed work or publication authority.

## Operation contracts

Read the [common command contract](references/command-contract.md) on activation. Resolve bundled links from this skill directory; resolve research files from the named consumer project. Do not rely on sibling packages, a source checkout or previous conversation state.

- [audit](commands/audit.md)
- [diagnose-research-failure](commands/diagnose-research-failure.md)
