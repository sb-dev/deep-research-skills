#!/usr/bin/env python3
"""Validate the Stage 15 public README contract.

This checks public-surface structure, exact accepted inventories, relative links
and maturity-claim discipline. It is not an installed-agent or semantic benchmark.
"""
from __future__ import annotations
from pathlib import Path
import argparse, json, re, shutil, tempfile

REQUIRED_SECTIONS = [
    "## Research capabilities",
    "## Research effort and evidence control",
    "## Installation",
    "## Quick start — PROV Primer publication status",
    "## Learn by researching",
    "### Level 1 — Find and verify one bounded answer",
    "### Level 2 — Compare a small evidence set",
    "### Level 3 — Produce a focused decision-ready report",
    "### Level 4 — Handle contested, scaled and changing evidence",
    "### Level 5 — Run a research programme that feeds production",
    "## Project structure grows with the research",
    "## Skills",
    "## Extension Packs",
    "## Execution",
    "## Evaluation / benchmarks",
    "## Documentation",
    "## Project boundary",
    "## Contributing",
    "## Licence",
]
EXPECTED_BY_LEVEL = {
    1: ["L1-01", "L1-02", "L1-03"],
    2: ["L2-01", "L2-02", "L2-03"],
    3: ["L3-01", "L3-02", "L3-03"],
    4: ["L4-01", "L4-02", "L4-03"],
    5: ["L5-01", "L5-02", "L5-03"],
}
SPEC_LINKS = [
    "docs/01-deep-research-skills-system-spec.md",
    "docs/02-deep-research-skills-workflows-and-artifacts-spec.md",
    "docs/03-deep-research-skills-repository-and-contracts-spec.md",
    "docs/04-testing-and-benchmark-spec.md",
    "docs/05-deep-research-skills-customisation-packs-spec.md",
    "docs/06-deep-research-skills-extension-pack-catalogue.md",
]
SKILLS = ["deep-research", "research-evaluate", "research-extension-pack-creator"]
COMMANDS = [
    "frame", "plan", "discover", "extract-evidence", "analyse-evidence",
    "follow-up-search", "synthesise", "refresh", "audit",
    "diagnose-research-failure", "create-pack",
]
PACKS = ["scholarly-evidence", "open-source-ecosystem"]

def section(text: str, heading: str, next_level: str = "## ") -> str:
    start = text.index(heading)
    rest = text[start + len(heading):]
    m = re.search(rf"(?m)^{re.escape(next_level)}", rest)
    return rest[:m.start()] if m else rest

def relative_links(text: str):
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#") or target.startswith("mailto:"):
            continue
        yield target.split("#", 1)[0]

def validate(root: Path):
    text = (root / "README.md").read_text()
    checks = {}

    checks["title"] = text.startswith("# Deep Research Skills\n")
    checks["research production positioning"] = (
        "research production" in text.lower()
        and "not isolated searches" in text.lower()
    )
    checks["all required sections"] = all(h in text for h in REQUIRED_SECTIONS)

    seen = re.findall(r"\*\*(L[1-5]-0[1-3])\s+—", text)
    checks["exact fifteen examples"] = len(seen) == 15 and len(set(seen)) == 15
    for level, ids in EXPECTED_BY_LEVEL.items():
        heading = REQUIRED_SECTIONS[4 + level]
        body = section(text, heading, "### ")
        found = re.findall(rf"\*\*(L{level}-0[1-3])\s+—", body)
        checks[f"level {level} exact trio"] = found == ids

    q = section(text, "## Quick start — PROV Primer publication status")
    quick_sentinels = [
        "https://www.w3.org/TR/prov-primer/",
        "precise locator",
        "3 search queries",
        "8 source reads/actions",
        "no purchase, new paid provider run or external communication",
        "research/l1-01/research.md",
        "Preserve uncertainty and unavailable-source limits",
    ]
    checks["quick start complete"] = all(s in q for s in quick_sentinels)

    install = section(text, "## Installation")
    checks["installation contract present"] = (
        "npx skills add sb-dev/deep-research-skills" in install
        and all(s in install for s in SKILLS)
    )
    checks["installation status honest"] = (
        "do **not** exist yet" in install
        and "have **not** passed local or clean external installation testing" in install
        and "not current installation instructions" in install
    )

    skills_body = section(text, "## Skills")
    checks["three skills"] = all(f"`{s}`" in skills_body for s in SKILLS)
    checks["eleven commands"] = all(c in skills_body for c in COMMANDS)

    packs = section(text, "## Extension Packs")
    checks["selected packs"] = all(f"`{p}`" in packs for p in PACKS)
    checks["pack maturity honest"] = (
        "design catalogue" in packs
        and "Neither is yet a production pack bundle or clean-install-validated product." in packs
    )

    docs = section(text, "## Documentation")
    checks["six canonical docs"] = all(link in docs for link in SPEC_LINKS)
    checks["relative link closure"] = all((root / path).exists() for path in relative_links(text))

    boundary = section(text, "## Project boundary")
    checks["project boundary"] = (
        "research production intelligence" in boundary.lower()
        and "does **not** own" in boundary
    )
    checks["future scaffold files not falsely linked"] = (
        "(CONTRIBUTING.md)" not in text and "(LICENSE)" not in text
    )
    checks["maturity honest"] = (
        "production skill packages have not yet been scaffolded or installation-tested" in text
        and "Live installed-agent scores, clean installation and benchmarked-product status have **not** yet been established." in text
        and "Status: working" not in text
        and "Status: mature" not in text
    )
    return checks

def mutate_and_check(root: Path, mutator):
    tmp = Path(tempfile.mkdtemp(prefix="stage15-negative-"))
    shutil.copytree(root, tmp / "repo", dirs_exist_ok=True)
    target = tmp / "repo" / "README.md"
    target.write_text(mutator(target.read_text()))
    checks = validate(tmp / "repo")
    shutil.rmtree(tmp)
    return checks

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--negative-controls", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    checks = validate(root)
    negatives = []
    if args.negative_controls:
        cases = [
            ("remove one example", lambda s: s.replace("**L5-03 —", "**LX-03 —", 1), "exact fifteen examples"),
            ("remove quick-start source", lambda s: s.replace("https://www.w3.org/TR/prov-primer/", "SOURCE-REMOVED", 1), "quick start complete"),
            ("false install readiness", lambda s: s.replace("do **not** exist yet", "are ready to install", 1), "installation status honest"),
            ("break canonical link", lambda s: s.replace("docs/06-deep-research-skills-extension-pack-catalogue.md", "docs/missing-catalogue.md", 1), "relative link closure"),
        ]
        for name, mutator, expected in cases:
            result = mutate_and_check(root, mutator)
            negatives.append({
                "mutation": name,
                "expected_failed_check": expected,
                "detected": result.get(expected) is False,
            })

    output = {
        "stage": 15,
        "kind": "public README structure, inventory, links and maturity validation; no installed-agent test",
        "checks": {k: "PASS" if v else "FAIL" for k, v in checks.items()},
        "negative_controls": negatives,
        "result": "PASS" if all(checks.values()) and all(n["detected"] for n in negatives) else "FAIL",
    }
    print(json.dumps(output, indent=2))
    raise SystemExit(0 if output["result"] == "PASS" else 1)

if __name__ == "__main__":
    main()
