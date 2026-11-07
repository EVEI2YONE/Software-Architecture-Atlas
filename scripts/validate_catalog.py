#!/usr/bin/env python3
"""Validate canonical catalog metadata, evidence and local links (stdlib only)."""
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SOURCE = re.compile(r"^\s*\d+\.\s+.*https?://\S+", re.M)
HEAD = re.compile(r"^##\s+(?:Evidence and sources|Sources)\s*$", re.I | re.M)
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---", 4)
    if closing < 0:
        return {}
    result = {}
    for line in text[4:closing].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def source_list(text):
    match = HEAD.search(text)
    if not match:
        return []
    section = text[match.end():]
    next_header = re.search(r"^##\s+", section, re.M)
    if next_header:
        section = section[:next_header.start()]
    return SOURCE.findall(section)


def validate(root=ROOT):
    errors = []
    try:
        index = json.loads((root / "catalog/index.json").read_text(encoding="utf-8"))
        taxonomy = json.loads((root / "catalog/taxonomy.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"catalog metadata could not be read: {exc}"]
    categories = {item["id"] for item in taxonomy["categories"]}
    entries = index["concepts"]
    ids, paths = set(), set()
    for entry in entries:
        cid, path = entry["id"], entry["path"]
        if not SLUG.fullmatch(cid):
            errors.append(f"invalid ID: {cid}")
        if cid in ids:
            errors.append(f"duplicate ID: {cid}")
        ids.add(cid)
        if path in paths:
            errors.append(f"duplicate path: {path}")
        paths.add(path)
        if entry["category"] not in categories:
            errors.append(f"{cid}: unknown category")
        if path != f"concepts/{entry['category']}/{cid}.md":
            errors.append(f"{cid}: noncanonical path")
        for name in ("tags", "related"):
            values = entry.get(name, [])
            if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
                errors.append(f"{cid}: invalid {name} list")
            elif len(values) != len(set(values)):
                errors.append(f"{cid}: duplicate {name}")
        if cid in entry.get("related", []):
            errors.append(f"{cid}: self-related concept")
        status = entry.get("status")
        if status not in {"stub", "draft", "reviewed", "deprecated"}:
            errors.append(f"{cid}: invalid status")
        reviewed = entry.get("reviewed_at")
        count = entry.get("source_count")
        if type(count) is not int or count < 0:
            errors.append(f"{cid}: invalid source_count")
            count = -1
        if reviewed is not None:
            if not isinstance(reviewed, str) or not DATE.fullmatch(reviewed):
                errors.append(f"{cid}: invalid reviewed_at")
            else:
                try:
                    date.fromisoformat(reviewed)
                except ValueError:
                    errors.append(f"{cid}: invalid reviewed_at calendar date")
        if status == "reviewed" and (not reviewed or count < 1):
            errors.append(f"{cid}: reviewed requires review date and sources")
        if status == "stub" and (reviewed is not None or count != 0):
            errors.append(f"{cid}: stub must have null review date and zero sources")
        page = root / path
        if not page.is_file():
            errors.append(f"missing file: {path}")
            continue
        text = page.read_text(encoding="utf-8")
        front = parse_frontmatter(text)
        for key in ("id", "category", "status"):
            if front.get(key) != str(entry[key]):
                errors.append(f"{path}: frontmatter mismatch for {key}")
        expected_review = reviewed if reviewed is not None else "null"
        if front.get("reviewed_at") != expected_review:
            errors.append(f"{path}: frontmatter mismatch for reviewed_at")
        if status == "reviewed":
            found = source_list(text)
            if len(found) != count:
                errors.append(f"{cid}: source_count {count} != {len(found)} numbered URL references in sources section")
        for match in LINK.findall(text):
            url = match.strip().split()[0].strip("<>")
            if url.startswith(("https://", "http://", "#", "mailto:")):
                continue
            local = unquote(url.split("#", 1)[0].split("?", 1)[0])
            if local and not (page.parent / local).resolve().is_file():
                errors.append(f"{path}: broken link {url}")
    for entry in entries:
        for related in entry.get("related", []):
            if related not in ids:
                errors.append(f"{entry['id']}: unknown related ID {related}")
    actual = {p.relative_to(root).as_posix() for p in (root / "concepts").rglob("*.md") if p.name != "README.md"}
    for extra in sorted(actual - paths):
        errors.append(f"unindexed concept: {extra}")
    return errors


def main():
    errors = validate()
    if errors:
        print("CATALOG INVALID:")
        for error in errors:
            print(" -", error)
        return 1
    index = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))
    print(f"CATALOG VALID: {len(index['concepts'])} indexed concepts, evidence metadata and links checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
