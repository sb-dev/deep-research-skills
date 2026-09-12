#!/usr/bin/env python3
"""Deterministic public/package contracts. No research-quality or install verdict."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]\n]+\]\(([^\s)]+)\)')
FORBIDDEN = [
    r'\bstage\s+(?:\d+|N)\b', r'feat/bootstrap', r'bootstrap\s+(?:progress|sequence|stage)',
    r'production scaffold', r'\bmaturity\b', r'completion\s+SHA', r'\b[0-9a-f]{40}\b',
    r'verification\s+counts?', r'\bnot[- ]run\b', r'not yet scaffolded', r'implemented later',
    r'docs/research-logs/',
]
FIELDS = ['Purpose', 'Inputs and preconditions', 'Operation', 'Outputs and write scope',
          'Completion and review', 'Failure and smallest repair',
          'Independent use and evaluation reason', 'Example invocation']


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def contract(root: Path) -> dict:
    return json.loads(read(root / 'tests/fixtures/public-contract.json'))


def prose(text: str) -> str:
    """Ignore fenced examples when extracting document navigation."""
    return re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text, flags=re.M | re.S)


def heading_slug(heading: str) -> str:
    heading = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading)
    heading = re.sub(r'[^\w\- ]', '', heading.lower(), flags=re.UNICODE)
    return heading.replace(' ', '-')


def anchors(text: str) -> set[str]:
    counts: dict[str, int] = {}
    result = set()
    for value in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(text), re.M):
        slug = heading_slug(value)
        index = counts.get(slug, 0)
        result.add(slug + (f'-{index}' if index else ''))
        counts[slug] = index + 1
    return result


def links(root: Path, path: Path, text: str | None = None, boundary: Path | None = None) -> list[str]:
    errors = []
    text = read(path) if text is None else text
    for target in LINK.findall(prose(text)):
        parsed = urlsplit(target)
        if parsed.scheme in ('https', 'http', 'mailto'):
            continue
        if parsed.scheme or parsed.netloc:
            errors.append(f'link scheme is unsupported: {path.relative_to(root)} -> {target}')
            continue
        part = unquote(parsed.path)
        resolved = (path.parent / part).resolve() if part else path.resolve()
        limit = (boundary or root).resolve()
        if not resolved.is_relative_to(limit):
            errors.append(f'link escapes boundary: {path.relative_to(root)} -> {target}')
        elif not resolved.exists():
            errors.append(f'broken local link: {path.relative_to(root)} -> {target}')
        elif parsed.fragment and resolved.is_file() and resolved.suffix == '.md':
            if unquote(parsed.fragment) not in anchors(read(resolved)):
                errors.append(f'broken anchor: {path.relative_to(root)} -> {target}')
    return errors


def validate_readme(root: Path, text: str | None = None) -> list[str]:
    cfg = contract(root)
    text = read(root / 'README.md') if text is None else text
    errors = []
    if re.findall(r'^#{1,3} .+$', prose(text), re.M) != cfg['headings']:
        errors.append('README sections/order differ from the accepted public contract')
    for pattern in FORBIDDEN:
        if re.search(pattern, text, re.I):
            errors.append(f'public-process leakage: {pattern}')
    quick = re.findall(r'```text\n(Use the installed deep-research skill.*?)(?:\n```)', text, re.S)
    if len(quick) != 1 or sha(quick[0]) != cfg['examples'][0]['prompt_sha256']:
        errors.append('complete inline Level 1 prompt changed or missing')
    levels = list(re.finditer(r'^### Level ([1-5]) — .+$', text, re.M))
    if [int(m[1]) for m in levels] != list(range(1,6)):
        errors.append('expected exactly five ordered levels')
    for i, match in enumerate(levels):
        end = levels[i+1].start() if i+1<len(levels) else text.find('\n## Project structure', match.end())
        ids = re.findall(r'^- \*\*(L\d-\d\d) —', text[match.end():end], re.M)
        if ids != [f'L{match[1]}-{n:02d}' for n in range(1,4)]:
            errors.append(f'exact three-example progression differs at level {match[1]}')
    navigation = []
    restored = text
    for example in cfg['examples']:
        token = '**' + example['id'] + ' — [' + example['title'] + '](' + example['path'] + ')**'
        if text.count(token) != 1:
            errors.append('public example identity/link mismatch: ' + example['id'])
        navigation.append(example['path'])
        restored = restored.replace('['+example['title']+']('+example['path']+')', example['title'])
    actual = [p for p in LINK.findall(prose(text)) if p.startswith('examples/')]
    if actual != navigation:
        errors.append('public example navigation is not exactly the accepted 15 paths')
    for filename in ('CONTRIBUTING.md','LICENSE'):
        token = f'[{filename}]({filename})'
        if text.count(token) != 1:
            errors.append('required publication link missing: ' + filename)
        restored = restored.replace(token, '`'+filename+'`')
    if sha(restored) != cfg['accepted_readme_sha256']:
        errors.append('README contains a non-mechanical change')
    for name in cfg['skills']:
        match = re.search(r'^### `'+re.escape(name)+r'`\n(.*?)(?=^## |^### |\Z)', text, re.M | re.S)
        if match is None or len(match[1].strip()) < 180:
            errors.append('substantive skill section missing: ' + name)
    errors += links(root, root/'README.md', text)
    return errors


def validate_examples(root: Path) -> list[str]:
    errors = []
    cfg = contract(root)
    actual = sorted(str(p.relative_to(root)) for p in (root/'examples').glob('level-*/README.md'))
    if actual != sorted(e['path'] for e in cfg['examples']):
        errors.append('primary example surface count/path mismatch')
    for example in cfg['examples']:
        path = root / example['path']
        if not path.is_file():
            errors.append('missing example: '+example['id'])
            continue
        text = read(path)
        prompts = re.findall(r'```text\n(.*?)\n```', text, re.S)
        if len(prompts) != 1 or sha(prompts[0]) != example['prompt_sha256']:
            errors.append('exact accepted prompt changed: '+example['id'])
        for heading in ('## Problem','## Exact prompt','## Expected artefacts','## Evaluation contract'):
            if heading not in text:
                errors.append(f'{example["id"]}: missing {heading}')
        for output in example['expected_artefacts']:
            if '- `'+output+'`' not in text:
                errors.append(f'{example["id"]}: missing required output {output}')
        for key in ('evaluation','benchmark','negative_contract'):
            if example[key] not in text:
                errors.append(f'{example["id"]}: missing {key} contract')
        errors += links(root,path)
    return errors


def validate_packages(root: Path) -> list[str]:
    errors = []
    cfg = contract(root)
    installed = sorted(p.parent.name for p in (root/'skills').glob('*/SKILL.md'))
    if installed != sorted(cfg['skills']):
        errors.append('expected exactly the three accepted skill packages')
    for name, commands in cfg['skills'].items():
        base = root/'skills'/name
        entry = base/'SKILL.md'
        if not entry.is_file():
            errors.append('missing skill: '+name)
            continue
        content = read(entry)
        front = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
        if not front or not re.search(r'^name: '+re.escape(name)+r'$', front[1], re.M) or not re.search(r'^description: .{20,}$', front[1], re.M):
            errors.append('invalid skill identity/frontmatter: '+name)
        if not front or not re.search(r'^license: MIT$', front[1], re.M):
            errors.append('missing chosen skill licence: '+name)
        if not (base/'LICENSE').is_file() or (base/'LICENSE').read_bytes() != (root/'LICENSE').read_bytes():
            errors.append('independent package is missing the MIT notice: '+name)
        found = sorted(p.stem for p in (base/'commands').glob('*.md'))
        if found != sorted(commands):
            errors.append('command ownership/count mismatch: '+name)
        for operation in commands:
            path = base/'commands'/f'{operation}.md'
            if not path.is_file():
                continue
            command = read(path)
            for field in FIELDS:
                if '**'+field+'.**' not in command:
                    errors.append(f'incomplete {name}/{operation}: {field}')
            if f'](commands/{operation}.md)' not in content:
                errors.append(f'undiscoverable command: {name}/{operation}')
        for reference in cfg['required_references'][name]+['command-contract']:
            target = base/'references'/f'{reference}.md'
            if not target.is_file() or len(read(target).strip()) < 200:
                errors.append(f'missing or empty reference: {name}/{reference}')
            if f'](references/{reference}.md)' not in content:
                errors.append(f'undiscoverable reference: {name}/{reference}')
        for path in base.rglob('*'):
            if path.is_symlink() and not path.resolve().is_relative_to(base.resolve()):
                errors.append('package symlink escapes skill: '+str(path.relative_to(root)))
            if path.suffix != '.md' or not path.is_file():
                continue
            body = read(path)
            errors += links(root,path,boundary=base)
            if re.search(r'\bStage\s+\d|docs/research-logs/|\.\./\.\./docs/|\bTODO\b|\bTBD\b',body):
                errors.append('unresolved design/checkout dependency: '+str(path.relative_to(root)))
    a = root/'skills/deep-research/references/evidence-contract.md'
    b = root/'skills/research-evaluate/references/evidence-contract.md'
    if a.is_file() and b.is_file() and a.read_bytes() != b.read_bytes():
        errors.append('producer/evaluator evidence invariant drift')
    return errors


def validate_history(root: Path) -> list[str]:
    expected = json.loads(read(root/'tests/fixtures/accepted-history.json'))['files']
    return ['accepted evidence changed: '+p for p,h in expected.items()
            if not (root/p).is_file() or sha(read(root/p)) != h]


def validate_surfaces(root: Path) -> list[str]:
    errors = []
    for filename in ('LICENSE','CONTRIBUTING.md','CHANGELOG.md','.github/workflows/validate.yml'):
        path=root/filename
        if not path.is_file() or not read(path).strip():
            errors.append('missing useful scaffold surface: '+filename)
        elif path.suffix=='.md':
            errors += links(root,path)
    licence=root/'LICENSE'
    if licence.is_file():
        text=read(licence)
        if not text.startswith('MIT License\n') or 'Permission is hereby granted, free of charge' not in text or 'THE SOFTWARE IS PROVIDED "AS IS"' not in text:
            errors.append('selected MIT licence text missing')
    for path in sorted((root/'docs').glob('0[1-6]-*.md')):
        errors += links(root,path)
    return errors


def check(root: Path) -> dict:
    groups = {'readme':validate_readme(root),'examples':validate_examples(root),
              'packages':validate_packages(root),'history':validate_history(root),
              'surfaces':validate_surfaces(root)}
    cfg=contract(root)
    return {'result':'FAIL' if any(groups.values()) else 'PASS','checks':groups,
            'counts':{'primary_examples':len(cfg['examples']),'skills':len(cfg['skills']),
                      'commands':sum(len(v) for v in cfg['skills'].values()),
                      'preserved_files':len(json.loads(read(root/'tests/fixtures/accepted-history.json'))['files'])},
            'scope':'Deterministic repository conformance; excludes research quality, execution and installation.'}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    args=parser.parse_args()
    result=check(args.root.resolve())
    print(json.dumps(result,indent=2))
    return int(result['result']!='PASS')


if __name__=='__main__':
    raise SystemExit(main())
