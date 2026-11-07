# Catalog retrieval and agent navigation

This is the consolidated active guide. Previous search-document paths remain compatibility entrypoints.

## Principles

- Use `catalog/index.json` for canonical IDs, category, title, status, source_count, reviewed_at, and paths.
- Use `catalog/taxonomy.json` for canonical topic categories.
- Search is deterministic, offline, lexical and candidate-oriented: it does not establish factual correctness, source accuracy or semantic completeness.
- Read the 2–5 relevant concept pages and sources, then inspect the actual target application before making recommendations.
- Separate observed facts, source-supported statements, inferred risks and unknowns.

## Detailed search interface

The Atlas includes a **deterministic, offline, zero-dependency** lexical search CLI. It uses the canonical `catalog/index.json`, not unverified LLM-generated answers. It is designed for agent tools, CI jobs and humans who need small, inspectable retrieval results. It does **not** provide embeddings, a hosted API or semantic guarantees.

## Quick start

```sh
python scripts/search_catalog.py "sync over async" --json
python scripts/search_catalog.py "dependency hell" --limit 3
python scripts/search_catalog.py "throughput" --category performance --json
python scripts/search_catalog.py "idempotency" --expand 2 --json
python -m unittest discover -s tests -v
```

## Retrieval protocol for agents

1. Inspect `catalog/taxonomy.json` and the canonical index. Search the question with `python scripts/search_catalog.py "<query>" --json`.
2. Inspect result `status`, `source_count`, `reviewed_at`, and `path`. Use canonical IDs to avoid confusing neighboring concepts. Optional `--category` and `--status` narrow search; `--expand N` adds up to N related IDs per leading hit (not recursively).
3. Read only the first 2–5 relevant pages, check source details and applicability, and cross-check the actual system under review. A `stub` is **unknown** evidence; a `reviewed` label still requires inspection of evidence and freshness.
4. Respond with observed facts, supported claims, inferences and unknowns separated. Cite the precise catalog page and primary sources as appropriate. Give trade-offs, simpler alternatives and verification plan rather than pattern prescriptions.
5. If no relevant entry exists, or sources are weak, report a gap using `templates/gap-request.md`. Do not invent a canonical concept or silently turn a stub into advice.

## JSON response contract

`query` is the submitted string, `total_matches` counts lexical candidates **before** `--limit`, and `results` is the ranked subset plus optional graph neighbors. Each result includes `id`, `title`, `category`, `path`, `status`, `summary`, `source_count`, `reviewed_at`, `score`, `matched_by`, `related`, and `evidence`. `matched_by=lexical` means scored; `matched_by=related:<id>` means a graph neighbor with score zero. `evidence=unknown` for draft/stub; other statuses say `requires-source-inspection` (not a guarantee). A notice explicitly warns against treating stubs as guidance.

## Ranking and limitations

Terms are lowercase alphanumeric tokens; exact ID, ID tokens, title, tags, summary, and related IDs have descending weights. A small explicit synonym table handles common phrases. Sorting uses score descending and ID ascending for reproducible results. The search does not read concept bodies or rank by technical correctness; additions to aliases must be tested and reviewed. Lexical matches can miss a synonym; zero results are a retrieval gap, **not** proof the concept is absent.

No network or proprietary model is required. Generated embeddings, if introduced later, should be optional, versioned, and stored outside the canonical source; lexical fallback must remain functional. No external repository is modified by this search tool.

## B0 retrieval evaluation

The [B0 integrity report](../research/archive/batches/batch-0-catalog-integrity.md) explains a version-controlled [golden query fixture](../tests/fixtures/retrieval_gold.json) with exact expected IDs, statuses, and deliberate misses. Run `python -m unittest discover -s tests -v` after changing aliases or ranking. A passing Top-1 suite means these queries are reproducible, **not** that retrieval is semantically complete or that cited guidance is verified against a target application.

The catalog validator checks frontmatter review dates and numbered URL source counts in reviewed concept pages; it does not independently verify the truth, accessibility, or claim relevance of external links.

## B14 query-intent regression cases

The optional, version-controlled `QUERY_INTENTS` table in `scripts/search_catalog.py` handles **seven exact normalized paraphrases**: ADR supersession, .NET/C# boundaries, TS/Node exports, Java/Scala builds, Python wheels/src layout, catalog claim audits and agent search evaluation. Intents apply only when the complete lowercase token sequence matches; they do **not** override longer ambiguous questions. Existing lexical scoring, canonical-ID precedence, status/category filters, graph expansion and offline operation remain available.

The expanded [golden fixture](../tests/fixtures/retrieval_gold.json) records expected Top-1 results and evidence labels for canonical IDs and these human-authored paraphrases. Do not infer that a passing suite measures real-world user relevance or fully grounds any answer. On a zero-hit query, report that the indexed search found no candidate—not that the architecture concept is absent.

## Related navigation strategy


## Index-first lookup
`catalog/index.json` exposes stable `id`, `title`, `domain`, `category`, `path`, `status`, `summary`, `tags`, `related`, `source_count`, and `reviewed_at`. Use these fields for lexical retrieval, graph expansion and small-context retrieval.

## Query strategy
1. Normalize terms (e.g. "sync over async" → async-await; "dependency hell" → dependency-conflicts).
2. Filter by `tags`/title/summary; include related concepts only when the design decision spans domains.
3. Read top candidates' pages and evidence; rank reviewed, current, applicable guidance over stubs.
4. Report what is missing, including index coverage gaps and unverified entries. Distinguish "indexed" from "curated".
5. If adding embeddings, store generated vectors outside the canonical Markdown/JSON source and record model/version and refresh policy. Lexical search must continue to function without embeddings.

## Context budget
Use one index lookup, 2–5 relevant concept files, and follow neighboring concepts only when justified. Avoid loading all topic files into an LLM context.

## Example mappings
- "Sonar says cognitive complexity" → `cognitive-complexity`, `quality-gates`, `code-simplification`
- "circular DI with conflicting packages" → `dependency-conflicts`, `dependency-inversion`, `modularity`
- "we need more throughput" → `scalability`, `backpressure`, `caching` (do not automatically prescribe caching)
- "DDD microservices?" → `bounded-contexts`, `modularity`, `consistency`

## Executable retrieval interface

For deterministic offline querying, use `python scripts/search_catalog.py "sync over async" --json` (optional `--limit`, `--category`, `--status`, `--expand`). See [agentic search guide](retrieval.md) for result structure, scoring, evidence handling, tests and limitations. Lexical search is a candidate-finding mechanism, not a verification engine.
