#!/usr/bin/env python3
"""Stage 14 canonical-specification validation.

Checks exact inventories, ownership markers, links and obvious false maturity claims.
This is not a semantic agent benchmark or installation test.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import re
import shutil
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
LOGS = DOCS / "research-logs"

CANONICAL = [
    "01-deep-research-skills-system-spec.md",
    "02-deep-research-skills-workflows-and-artifacts-spec.md",
    "03-deep-research-skills-repository-and-contracts-spec.md",
    "04-testing-and-benchmark-spec.md",
    "05-deep-research-skills-customisation-packs-spec.md",
    "06-deep-research-skills-extension-pack-catalogue.md",
]

BASELINE_PATHS = {
    "README.md",
    "docs/research-logs/2026-09-07-deep-research-skills-new-project-bootstrap-process.md",
    "docs/research-logs/bootstrap-progress-through-stage-08.md",
    "docs/research-logs/bootstrap-progress-through-stage-13.md",
}

STAGE_SUPPORT = {
    "docs/research-logs/2026-09-11-stage-14-canonical-specifications.md",
    "docs/research-logs/2026-09-11-stage-14-verification.py",
    "docs/research-logs/2026-09-11-stage-14-verification.json",
    "docs/research-logs/bootstrap-progress.md",
}

PROMPT_SCH = (
    "Use the accepted deep-research procedure with the scholarly-evidence profile specified in the Stage 11 profiles file. "
    "Answer: what does RULER establish, and not establish, about relying on an advertised context window for a research assistant? "
    "Use only the authors' arXiv record 2404.06654 and its v2/v3 paper representations. Distinguish versions, direct findings, inference and unknowns. "
    "Give a supported answer, source locators, temporal limits and the next justified verification step. Do not run a model, claim an exhaustive literature review, "
    "infer current product rankings or approve a product. Preserve any valid finding even if it also appears in another representation. Use the supplied Stage 11 source register; "
    "new retrieval is limited to this same source universe. Record actual access. Stop when this bounded question is answered and review the exact wording. "
    "Write a separate pack output without editing the core output."
)
PROMPT_OSS = (
    "Use the accepted deep-research procedure with the open-source-ecosystem profile specified in the Stage 11 profiles file. "
    "Assess langchain-ai/open_deep_research at commit 1b7d2e80db9faa586165c60e09096dbbfd483a64 as a candidate optional execution engine for an evidence-led research skill. "
    "Use only that revision's README.md, LICENSE, pyproject.toml, langgraph.json, src/open_deep_research/configuration.py, src/open_deep_research/deep_researcher.py and its Git commit metadata. "
    "Explain capabilities, setup, licence scope, important limitations and the next verification step. Distinguish documentary claims, static inspection and unexecuted tests. "
    "Do not install or run the engine, change code, spend money, contact maintainers, infer security from popularity or approve deployment. Use the supplied Stage 11 source register and only this source universe "
    "for any follow-up. Preserve qualifications and review the exact answer. Write a separate pack output without editing the core output."
)

def canonical_texts(base: Path) -> dict[str, str]:
    return {name: (base / "docs" / name).read_text(encoding="utf-8") for name in CANONICAL if (base / "docs" / name).exists()}

def rel_links(text: str) -> list[str]:
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    return [x.split("#", 1)[0] for x in links if x and not re.match(r"^[a-z]+://", x) and not x.startswith("#")]

def all_stage_files(base: Path) -> set[str]:
    result = set(BASELINE_PATHS) | set(STAGE_SUPPORT)
    result |= {f"docs/{name}" for name in CANONICAL}
    return result

def check(base: Path) -> dict[str, str]:
    checks: dict[str, str] = {}
    texts = canonical_texts(base)
    actual_root = sorted(p.name for p in (base / "docs").glob("*.md"))
    checks["exact six canonical names"] = "PASS" if actual_root == CANONICAL else "FAIL"

    required = {
        CANONICAL[0]: [
            "## 2. Mission and owned outcomes", "## 3. Boundary", "## 4. Governing principles",
            "## 5. Core skill architecture", "## 6. Execution architecture", "## 7. Source and tool boundary",
            "## 8. Effort, cost and stopping policy", "## 10. Human review and commitment points",
            "## 11. Build order", "## 12. System acceptance",
            "`deep-research`", "`research-evaluate`", "`research-extension-pack-creator`",
        ],
        CANONICAL[1]: [
            "## 2. Workflow", "## 3. Research information model", "## 5. Provenance contract",
            "## 11. Contradictions and gaps", "## 12. Synthesis and handoff",
            "## 13. Failure taxonomy and repair", "## 14. Repair routes", "## 15. Refresh semantics",
            "## 16. Cross-domain handoffs",
        ] + [f"W{i:02d}" for i in range(1,9)] + [f"A{i:02d}" for i in range(1,12)] + [f"F{i:02d}" for i in range(1,21)],
        CANONICAL[2]: [
            "## 2. Repository structure", "## 3. Skill package contract", "## 4. `SKILL.md` contracts",
            "## 5. Common command contract", "## 7. Self-containment", "## 9. Installation contract",
            "## 10. Selective installation acceptance", "## 12. Tooling", "## 13. CI expectations",
            "## 14. Technical acceptance",
            "`deep-research`", "`research-evaluate`", "`research-extension-pack-creator`",
            "`frame`", "`plan`", "`discover`", "`extract-evidence`", "`analyse-evidence`",
            "`follow-up-search`", "`synthesise`", "`refresh`", "`audit`",
            "`diagnose-research-failure`", "`create-pack`",
        ],
        CANONICAL[3]: [
            "## 3. Benchmark suites", "## 4. Evaluation layers", "## 5. Domain quality dimensions",
            "## 8. Case contract", "## 10. Retrieval evaluation", "## 12. Citation and provenance evaluation",
            "## 13. Synthesis evaluation", "## 14. Progressive-example coverage",
            "## 15. Extension Pack differential suite", "## 17. Regression policy",
            "## 18. Release gates", "## 19. Measured evidence status",
            "BrowseComp", "DeepResearch Bench", "BrowseComp-Plus", "ResearchRubrics", "FINDER/DEFT",
        ] + [f"L{i:02d}" for i in range(1,11)] + [f"K{i:02d}" for i in range(1,17)]
          + [f"EX-L{level}-{idx:02d}" for level in range(1,6) for idx in range(1,4)],
        CANONICAL[4]: [
            "## 2. Definition", "## 3. Pack dimensions", "## 4. Activation", "## 5. Precedence",
            "## 8. Pack package", "## 9. Manifest contract", "## 11. Authoring workflow",
            "## 12. Showcase contract", "## 13. Differential evaluation", "## 16. Deferred families",
            "Source ecology", "Search strategy", "Inclusion/exclusion", "Source appraisal",
            "Research methods", "Synthesis structure", "Quality criteria", "Reporting conventions",
        ] + [f"A{i:02d}" for i in range(1,13)],
        CANONICAL[5]: [
            "## 3. Pack: `scholarly-evidence`", "## 4. Pack: `open-source-ecosystem`",
            "## 5. Deferred catalogue candidates", "## 7. Catalogue acceptance",
            "`market-intelligence`", "`technology-landscape`", "`trend-and-signal`",
            "`creative-reference-research`", "`investigative-osint`",
        ],
    }
    for name, markers in required.items():
        text = texts.get(name, "")
        checks[f"required content {name}"] = "PASS" if text and all(m in text for m in markers) else "FAIL"

    cat = texts.get(CANONICAL[5], "")
    checks["exact scholarly showcase prompt"] = "PASS" if PROMPT_SCH in " ".join(cat.split()) else "FAIL"
    checks["exact open-source showcase prompt"] = "PASS" if PROMPT_OSS in " ".join(cat.split()) else "FAIL"

    # Link closure over the accepted-parent paths that these documents actually use plus Stage 14.
    virtual = all_stage_files(base)
    broken = []
    stage_docs = list((base/"docs").glob("*.md")) + list((base/"docs/research-logs").glob("2026-09-11-stage-14-*.md")) + [base/"docs/research-logs/bootstrap-progress.md"]
    for path in stage_docs:
        text = path.read_text(encoding="utf-8")
        for link in rel_links(text):
            target = (Path(path.relative_to(base)).parent / link).as_posix()
            # normalise .. and .
            target = Path(os.path.normpath(target)).as_posix()
            if target not in virtual:
                broken.append(f"{path.relative_to(base)} -> {link} ({target})")
    checks["relative link closure"] = "PASS" if not broken else "FAIL"

    banned = [
        "clean external installation: PASS",
        "installed-tested: PASS",
        "repository maturity: mature",
        "**Implementation state:** Working",
        "**Implementation state:** Benchmarked",
        "**Implementation state:** Mature",
    ]
    false_claims = [(n, b) for n,t in texts.items() for b in banned if b in t]
    checks["no false product maturity claim"] = "PASS" if not false_claims else "FAIL"

    top_dirs = {p.name for p in base.iterdir() if p.is_dir()}
    checks["no premature production directories"] = "PASS" if top_dirs == {"docs"} else "FAIL"
    checks["stage support files"] = "PASS" if all((base/p).exists() or p.endswith("verification.json") for p in STAGE_SUPPORT if p.startswith("docs/research-logs/2026-09-11")) else "FAIL"
    return checks

def negative_controls(base: Path) -> list[dict]:
    results = []
    mutations = [
        ("remove canonical spec", lambda d: (d/"docs"/CANONICAL[-1]).unlink()),
        ("remove required inventory", lambda d: (d/"docs"/CANONICAL[1]).write_text((d/"docs"/CANONICAL[1]).read_text().replace("F20", "FX20"), encoding="utf-8")),
        ("break local link", lambda d: (d/"docs"/CANONICAL[0]).write_text((d/"docs"/CANONICAL[0]).read_text().replace("02-deep-research-skills-workflows-and-artifacts-spec.md", "missing-spec.md", 1), encoding="utf-8")),
        ("false clean install claim", lambda d: (d/"docs"/CANONICAL[2]).write_text((d/"docs"/CANONICAL[2]).read_text()+"\nclean external installation: PASS\n", encoding="utf-8")),
    ]
    for name, mutate in mutations:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            shutil.copytree(base/"docs", tmp/"docs")
            mutate(tmp)
            outcome = check(tmp)
            detected = [k for k,v in outcome.items() if v == "FAIL"]
            results.append({"mutation": name, "detected": detected, "result": "PASS" if detected else "FAIL"})
    return results

def main():
    # verification.json may not exist until this script writes it.
    result_path = LOGS / "2026-09-11-stage-14-verification.json"
    result_path.write_text("{}\n", encoding="utf-8")
    checks = check(ROOT)
    neg = negative_controls(ROOT)
    hashes = {}
    for rel in [f"docs/{x}" for x in CANONICAL] + [
        "docs/research-logs/2026-09-11-stage-14-canonical-specifications.md",
        "docs/research-logs/2026-09-11-stage-14-verification.py",
        "docs/research-logs/bootstrap-progress.md",
    ]:
        data = (ROOT/rel).read_bytes()
        hashes[rel] = {
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
            "bytes": len(data),
        }
    result = {
        "stage": 14,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "kind": "canonical specification inventory, ownership, link and maturity validation; no installed-agent test",
        "parent": "62b65ebd5f3174c0ec63c4bfd15ac0729b44ce35",
        "canonical_count_required": 6,
        "canonical_names": CANONICAL,
        "checks": checks,
        "negative_controls": neg,
        "hashes": hashes,
        "result": "PASS" if all(v=="PASS" for v in checks.values()) and all(x["result"]=="PASS" for x in neg) else "FAIL",
    }
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": result["result"], "checks": checks, "negative_controls": neg}, indent=2))
    raise SystemExit(0 if result["result"]=="PASS" else 1)

if __name__ == "__main__":
    import os
    main()
