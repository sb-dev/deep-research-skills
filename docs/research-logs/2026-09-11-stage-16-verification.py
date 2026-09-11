#!/usr/bin/env python3
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "## Research capabilities",
    "## Research effort and evidence control",
    "## Install",
    "## Quick start — PROV Primer publication status",
    "## Learn by researching",
    "## Project structure grows with the research",
    "## Skills",
    "### `deep-research`",
    "### `research-evaluate`",
    "### `research-extension-pack-creator`",
    "## Extension Packs",
    "## Execution",
    "## Evaluation and benchmarks",
    "## Documentation",
    "## Project boundary",
    "## Contributing",
    "## Licence",
]

FORBIDDEN = [
    r"\bStage\s+\d+\b",
    r"feat/bootstrap",
    r"bootstrap progress",
    r"bootstrap sequence",
    r"production scaffold",
    r"maturity promotion",
    r"\bnot-run\b",
    r"docs/research-logs/",
]

QUICK_START = [
    "https://www.w3.org/TR/prov-primer/",
    "precise locator",
    "Bound discovery to 3 search queries",
    "acquisition to 8 source reads/actions",
    "research/l1-01/research.md",
    "Preserve uncertainty",
    "producer self-check",
]

SPEC_LINKS = [
    "docs/01-deep-research-skills-system-spec.md",
    "docs/02-deep-research-skills-workflows-and-artifacts-spec.md",
    "docs/03-deep-research-skills-repository-and-contracts-spec.md",
    "docs/04-testing-and-benchmark-spec.md",
    "docs/05-deep-research-skills-customisation-packs-spec.md",
    "docs/06-deep-research-skills-extension-pack-catalogue.md",
]

def validate(text: str) -> list[str]:
    errors: list[str] = []
    if not text.startswith("# Deep Research Skills\n"):
        errors.append("wrong README title")

    positions = []
    for heading in REQUIRED_HEADINGS:
        pos = text.find(heading)
        if pos < 0:
            errors.append(f"missing heading: {heading}")
        positions.append(pos)
    filtered = [p for p in positions if p >= 0]
    if filtered != sorted(filtered):
        errors.append("required headings are out of order")

    for pattern in FORBIDDEN:
        if re.search(pattern, text, re.I):
            errors.append(f"public-process leakage: {pattern}")

    for token in QUICK_START:
        if token not in text:
            errors.append(f"quick-start requirement missing: {token}")

    levels = list(re.finditer(r"^### Level ([1-5]) — .+$", text, re.M))
    if len(levels) != 5:
        errors.append(f"expected 5 levels, found {len(levels)}")
    else:
        for idx, match in enumerate(levels):
            level = int(match.group(1))
            start = match.end()
            end = levels[idx + 1].start() if idx + 1 < len(levels) else text.find("\n## Project structure", start)
            block = text[start:end]
            ids = re.findall(rf"^\- \*\*(L{level}-\d{{2}}) —", block, re.M)
            expected = [f"L{level}-{i:02d}" for i in range(1, 4)]
            if ids != expected:
                errors.append(f"level {level} examples mismatch: {ids}")

    for level in range(1, 6):
        for n in range(1, 4):
            eid = f"L{level}-{n:02d}"
            if text.count(f"**{eid} —") != 1:
                errors.append(f"example identity count mismatch: {eid}")

    for path in SPEC_LINKS:
        if path not in text:
            errors.append(f"missing canonical spec link: {path}")

    for skill in ["deep-research", "research-evaluate", "research-extension-pack-creator"]:
        heading = f"### `{skill}`"
        start = text.find(heading)
        if start >= 0:
            end = text.find("\n### `", start + len(heading))
            if end < 0:
                end = text.find("\n## Extension Packs", start)
            if end - start < 180:
                errors.append(f"skill section too thin: {skill}")

    return errors

def negative_controls(text: str) -> dict[str, bool]:
    controls = {
        "stage leakage": "## Stage 99\n" + text,
        "research-log route": text.replace("L1-01 — PROV Primer publication status", "[L1-01](docs/research-logs/example.md) — PROV Primer publication status", 1),
        "missing example": text.replace("- **L2-03 — Small numeric repair comparison** — produce a reproducible descriptive comparison while retaining denominators and sampling limits.\n", "", 1),
        "missing skill": text.replace("### `research-evaluate`", "### evaluator-removed", 1),
    }
    return {name: bool(validate(mutated)) for name, mutated in controls.items()}

def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
    text = path.read_text()
    errors = validate(text)
    negatives = negative_controls(text)
    result = {
        "result": "PASS" if not errors and all(negatives.values()) else "FAIL",
        "positive_errors": errors,
        "negative_controls": negatives,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["result"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
