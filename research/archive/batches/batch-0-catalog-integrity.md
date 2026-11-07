# B0 — Catalog integrity, evidence audit and agent retrieval benchmark

**Date:** 2026-11-07 · **Scope:** GAP-01 and cross-cutting catalog quality.  
**State:** Catalog tooling curated; no independent technical audit of every reference or production repository.

## Context gathered before changes
The live branch held 47 canonical concepts (26 reviewed with scoped references, 21 stubs), a deterministic lexical search tool, basic metadata/link validator and CI workflow. Existing tests covered a handful of exact and alias queries. The validator checked valid IDs, canonical paths, existing related IDs and the *presence* of a review date/source count, but did not compare source_count with actual cited references or detect duplicate tags/related IDs. The index contained **14 entries with duplicate metadata** (13 tag lists, one related-ID list). None of these duplicates established false architectural claims, but they created avoidable retrieval/index integrity risk.

## Work performed
- Removed duplicate `tags` and `related` values from the canonical index while preserving first-seen order; concept IDs and review statuses unchanged.
- Strengthened `scripts/validate_catalog.py` to check duplicate metadata, self-relations, valid review dates, stub evidence consistency, page/frontmatter review-date matching and numbered URL reference counts within each reviewed article's **Sources** or **Evidence and sources** section.
- Added isolated validator regression tests for duplicate metadata, source counts, invalid stub metadata, missing links and review-date mismatch.
- Added `tests/fixtures/retrieval_gold.json` with 20 fixed queries (IDs, aliases, project-type searches, a known stub and a no-result query) plus `tests/test_retrieval_gold.py` with Top-1, status and evidence-label assertions.
- Preserved the zero-dependency/offline lexical API and stable JSON response contract. No embeddings, hosted model, external index or API key required.

## Evidence and verification boundaries

| Signal | What it establishes | What it does **not** establish |
| --- | --- | --- |
| Validator passes | Canonical paths, page metadata, local links and source *counts* agree with listed artifacts | Source URL is live, correct, recent, primary or actually supports each claim |
| Gold query Top-1 | Current lexical ranking reproduces 20 curated expectations | Semantic search recall across all possible queries, reasoning quality or answer correctness |
| `reviewed` + sources | A curator supplied dated reference metadata for a scoped claim | Source-claim entailment, target-specific effectiveness, security or performance certification |
| `stub` | Intended research topic is discoverable | Validated implementation advice |
| CI passes | This repository's configured catalog checks and Python unit tests succeeded on a specific commit | Sonar passing, target application tests or operational compliance |

## Evidence rubric for agents
1. **Observed:** link to immutable repository commit/path and tests/measurements, not just a file name.
2. **Supported:** exact external primary/official source and claim, dated applicability/version and scope. Manual human source review is still required.
3. **Inferred:** hypothesis or candidate decision; include assumptions, a simpler option and a falsifiable verification step.
4. **Unknown:** missing source, absent target-runtime measurements, unsupported analogy, outdated context or an unreviewed stub.
5. **Conflicted/stale:** two sources differ or a standard/runtime has moved; preserve the disagreement and date, do not silently resolve it with model intuition.

## Agent retrieval protocol
Search using the deterministic CLI:
```sh
python scripts/search_catalog.py "mvp enterprise project architecture" --json
python scripts/search_catalog.py "canary deployment" --status reviewed --json
python scripts/search_catalog.py "project structure" --expand 2 --json
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
```

Read the highest-scoring relevant *page*, inspect its cited sources and applicability, then inspect related entries when needed. If a result is a stub, report a research gap; if it is reviewed, treat the label as **requires-source-inspection**, not as independently verified evidence. A lexical miss never proves an architectural concept absent. Require a real application tree before recommending file moves or claiming fewer lines/improved navigation.

## Benchmark interpretation and limitations
- The fixed query suite measures **Top-1 retrieval agreement on selected queries**, not precision/recall in a representative real-world question distribution.
- No independent adversarial evaluation of citations, source reliability or claim-to-source support was run.
- The current lexical search uses a curated alias table; phrases outside it can miss matching concepts. Keep aliases versioned and add regression cases for user-observed misses.
- The numbered-URL source counter detects discrepancies, not whether a reference is authentic, reachable or appropriate.
- Markdown links in nonconcept documentation and remote URLs are not exhaustively checked by this catalog validator.

## Open research and follow-up
- Run independent manual source-claim audits across reviewed concept pages and confirm current official standards and framework versions. Do not auto-promote stubs.
- Enlarge benchmark from observed agent queries, especially ambiguous questions across UI/API/Functions/WebJobs and multi-stage evolution. Record false-positive and missing cases without quietly changing evaluation data to force passing.
- Add metadata schema and optional snapshot-level checks for categorized navigation/other docs if needed.
- Measure real target-application navigation, refactoring benefits, security and runtime correctness with actual build/test/observability evidence.

**B0 conclusion:** Implemented repository-level integrity controls and a reproducible retrieval test suite. Remains *partially completed* pending independent source validation and representative live-query evaluation.
