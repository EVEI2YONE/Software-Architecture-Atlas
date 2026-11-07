#!/usr/bin/env python3
"""Deterministic, offline search over the canonical architecture catalog."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {
    "sync over async": "async-await",
    "dependency hell": "dependency-conflicts",
    "sonar": "quality-gates",
    "cognitive complexity": "cognitive-complexity",
    "microservices": "bounded-contexts modularity consistency",
    "throughput": "scalability backpressure",
    "race condition": "thread-safety",
    "retry duplicate": "idempotency",
    "file structure": "project-structure-selection",
    "folder structure": "project-structure-selection",
    "project organization": "project-structure-selection",
    "webjobs": "project-structure-selection",
    "vertical slice": "project-structure-selection feature-first-folders",
}

def terms(value):
    return re.findall(r"[a-z0-9]+", value.lower())

def search(query, *, category=None, status=None, limit=5, expand=0, index=None):
    if index is None:
        index = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))
    original = terms(query)
    expanded = list(original)
    lower_query = query.lower()
    for phrase, replacement in ALIASES.items():
        if phrase in lower_query:
            expanded.extend(terms(replacement))
    q = set(expanded)
    ranked = []
    concepts = index["concepts"]
    by_id = {item["id"]: item for item in concepts}
    for item in concepts:
        if category and item["category"] != category:
            continue
        if status and item["status"] != status:
            continue
        fields = {
            "id": set(terms(item["id"])),
            "title": set(terms(item["title"])),
            "tags": set(t for tag in item.get("tags", []) for t in terms(tag)),
            "summary": set(terms(item["summary"])),
            "related": set(t for rel in item.get("related", []) for t in terms(rel)),
        }
        score = sum(weight * len(q & tokens) for weight, tokens in
                    ((10, fields["id"]), (7, fields["title"]), (5, fields["tags"]),
                     (2, fields["summary"]), (1, fields["related"])))
        if item["id"].lower() == lower_query.strip():
            score += 30
        if score:
            ranked.append((score, item["id"], item))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    results = []
    seen = set()
    for score, _, item in ranked[:limit]:
        results.append(make_result(item, score, "lexical"))
        seen.add(item["id"])
    if expand:
        seeds = list(results)
        for seed in seeds:
            for rel in by_id[seed["id"]].get("related", [])[:expand]:
                if rel in by_id and rel not in seen and len(results) < limit + len(seeds) * expand:
                    neighbor = by_id[rel]
                    if (not category or neighbor["category"] == category) and (not status or neighbor["status"] == status):
                        results.append(make_result(neighbor, 0, "related:" + seed["id"]))
                        seen.add(rel)
    return {"query": query, "total_matches": len(ranked), "results": results,
            "notice": "Indexed stubs are coverage intent, not verified guidance."}

def make_result(item, score, match):
    return {k: item[k] for k in
            ("id", "title", "category", "path", "status", "summary", "source_count", "reviewed_at")} | {
                "score": score, "matched_by": match, "related": item.get("related", []),
                "evidence": "unknown" if item["status"] in ("stub", "draft") else
                "requires-source-inspection"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Natural-language question, phrase or canonical ID")
    parser.add_argument("--category", help="Limit results to a canonical category")
    parser.add_argument("--status", choices=("stub", "draft", "reviewed", "deprecated"))
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--expand", type=int, default=0, help="Include up to N related IDs per top hit")
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    args = parser.parse_args()
    if args.limit < 1 or args.expand < 0:
        parser.error("--limit must be >= 1 and --expand >= 0")
    result = search(args.query, category=args.category, status=args.status, limit=args.limit, expand=args.expand)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f'{result["total_matches"]} lexical match(es) for {args.query!r}')
        for hit in result["results"]:
            print(f'[{hit["score"]:>3}] {hit["id"]} ({hit["status"]}; {hit["matched_by"]}) -> {hit["path"]}')
        print(result["notice"])

if __name__ == "__main__":
    main()
