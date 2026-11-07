#!/usr/bin/env python3
"""Check current catalog coverage and local Markdown navigation (stdlib only)."""
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

def validate(root=ROOT):
    errors = []
    index = json.loads((root / "catalog/index.json").read_text(encoding="utf-8"))
    entries = index["concepts"]
    counts = Counter(entry["category"] for entry in entries)
    coverage = (root / "docs/coverage.md").read_text(encoding="utf-8")
    expected = f"{len(entries)} indexed concepts"
    if expected not in coverage:
        errors.append(f"coverage summary missing canonical total: {expected}")
    for category, count in counts.items():
        if not re.search(rf"^\| \[{re.escape(category)}\]\([^)]*\) \| {count} \|$", coverage, re.M):
            errors.append(f"coverage count mismatch: {category}={count}")
        readme = root / "concepts" / category / "README.md"
        if not readme.is_file():
            errors.append(f"missing category README: {readme.relative_to(root)}")
            continue
        linked = set(re.findall(r"\]\(([a-z0-9-]+)\.md\)", readme.read_text(encoding="utf-8")))
        expected_ids = {entry["id"] for entry in entries if entry["category"] == category}
        if linked != expected_ids:
            errors.append(f"category README index mismatch: {category} missing={sorted(expected_ids-linked)} extra={sorted(linked-expected_ids)}")
    # Active docs only. Archived snapshots preserve historical, path-relative text.
    files = [root / "README.md", root / "AGENTS.md", root / "CONTRIBUTING.md"]
    files += list((root / "docs").glob("*.md"))
    files += list((root / "research").glob("*.md"))
    files += list((root / "concepts").glob("*/README.md"))
    for page in files:
        if not page.is_file():
            continue
        for raw in LINK.findall(page.read_text(encoding="utf-8")):
            url = raw.strip().split()[0].strip("<>")
            if url.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local = unquote(url.split("#", 1)[0].split("?", 1)[0])
            if local and not (page.parent / local).resolve().exists():
                errors.append(f"{page.relative_to(root)}: broken local link {url}")
    return errors

if __name__ == "__main__":
    errs = validate()
    if errs:
        print("DOCUMENTATION INVALID:")
        for error in errs:
            print(" -", error)
        sys.exit(1)
    print("DOCUMENTATION VALID: coverage, category navigation and active local links")
