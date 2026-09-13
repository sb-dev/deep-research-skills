# scholarly-evidence showcase

Premise: A team needs evidence about advertised long-context capacity, not a model purchasing recommendation.

## Exact pack prompt

```text
Use deep-research with scholarly-evidence version 0.1.0, compatible core contract 0.1. Answer: what does RULER establish, and not establish, about relying on an advertised context window for a research assistant? Use only the authors' arXiv record 2404.06654 and its v2/v3 paper representations. Distinguish versions, direct findings, inference and unknowns. Give a supported answer, source locators, temporal limits and the next justified verification step. Do not run a model, claim an exhaustive literature review, infer current product rankings or approve a product. Preserve valid findings from every eligible representation. Use existing authorised read tools only. Allow at most eight source actions, with no search beyond the named source universe. Record actual access, evidence, claims, uncertainty and source-checkout execution. Review exact wording and write a separate report. Stop when this bounded question is answered.
```

## Exact core comparison prompt

```text
Use deep-research without an Extension Pack. Answer: what does RULER establish, and not establish, about relying on an advertised context window for a research assistant? Use only the authors' arXiv record 2404.06654 and its v2/v3 paper representations. Distinguish versions, direct findings, inference and unknowns. Give a supported answer, source locators, temporal limits and the next justified verification step. Do not run a model, claim an exhaustive literature review, infer current product rankings or approve a product. Preserve valid findings from every eligible representation. Use existing authorised read tools only. Allow at most eight source actions, with no search beyond the named source universe. Record actual access, evidence, claims, uncertainty and source-checkout execution. Review exact wording and write a separate report. Stop when this bounded question is answered.
```

## Comparison contract

One fresh isolated run per condition, same substantive source universe, tool authority, core revision and budget. Both receive the same known baseline facts: scholarly versions change model populations and use a context-dependent threshold; the engine has a broad exception-to-termination path. These facts must not be hidden to favour a pack. No other-condition answer is supplied. The only changed input is explicit pack selection and its method criteria. Parent review gets four additional source actions per pair.

Expected change: Version-linked unit counting and design-specific threshold applicability, with preserved core findings.

Require core question fit, source/claim support, temporal and access honesty, preserved evidence and authority. For scholarly specialisation check actual work/report linkage, eligible-version status and design-transfer appraisal. For open-source specialisation check cross-file setup reconciliation, consequential code inspection and static-risk-to-test mapping. Cosmetic differences fail. One pair establishes only the observed application, not a general quality gain.

Status: the actual 0.1.0 pair passed for a bounded source-appraisal difference. One pair does not establish a general quality gain. Installation has not been tested.
