#!/usr/bin/env python3
"""Validate canonical catalog records, page frontmatter and Markdown links (stdlib only)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = json.loads((ROOT / 'catalog/index.json').read_text(encoding='utf-8'))
taxonomy = json.loads((ROOT / 'catalog/taxonomy.json').read_text(encoding='utf-8'))
errors = []
ids = set()
paths = set()
categories = {item['id'] for item in taxonomy['categories']}
entries = index['concepts']
for entry in entries:
    cid = entry['id']
    path = entry['path']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', cid): errors.append(f'invalid id: {cid}')
    if cid in ids: errors.append(f'duplicate id: {cid}')
    ids.add(cid)
    if path in paths: errors.append(f'duplicate path: {path}')
    paths.add(path)
    if entry['category'] not in categories: errors.append(f'unknown category: {cid}')
    if path != f"concepts/{entry['category']}/{cid}.md": errors.append(f'noncanonical path: {cid}')
    file = ROOT / path
    if not file.is_file():
        errors.append(f'missing file: {path}')
        continue
    text = file.read_text(encoding='utf-8')
    for key, value in [('id', cid), ('category', entry['category']), ('status', entry['status'])]:
        if not re.search(rf'(?m)^{key}:\s*{re.escape(value)}\s*$', text):
            errors.append(f'{path}: frontmatter mismatch for {key}')
    if entry['status'] not in {'stub','draft','reviewed','deprecated'}: errors.append(f'{cid}: invalid status')
    if entry['status'] == 'reviewed' and (not entry['reviewed_at'] or entry['source_count'] < 1):
        errors.append(f'{cid}: reviewed requires date and sources')
    for url in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)', text):
        if url.startswith(('https://','http://','#','mailto:')): continue
        target = (file.parent / url.split('#')[0]).resolve()
        if not target.is_file(): errors.append(f'{path}: broken link {url}')
for entry in entries:
    for related in entry.get('related', []):
        if related not in ids: errors.append(f"{entry['id']}: unknown related id {related}")
actual = {p.relative_to(ROOT).as_posix() for p in (ROOT/'concepts').rglob('*.md') if p.name != 'README.md'}
for extra in sorted(actual - paths): errors.append(f'unindexed concept: {extra}')
if errors:
    print('CATALOG INVALID:')
    for error in errors: print(' -', error)
    sys.exit(1)
print(f'CATALOG VALID: {len(entries)} indexed concepts, {len(categories)} categories, links and frontmatter checked')
