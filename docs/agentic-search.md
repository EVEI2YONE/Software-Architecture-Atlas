# Agent-friendly catalog search

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

The [B0 integrity report](batch-0-catalog-integrity.md) explains a version-controlled [golden query fixture](../tests/fixtures/retrieval_gold.json) with exact expected IDs, statuses, and deliberate misses. Run `python -m unittest discover -s tests -v` after changing aliases or ranking. A passing Top-1 suite means these queries are reproducible, **not** that retrieval is semantically complete or that cited guidance is verified against a target application.

The catalog validator checks frontmatter review dates and numbered URL source counts in reviewed concept pages; it does not independently verify the truth, accessibility, or claim relevance of external links.

## B14 query-intent regression cases

The optional, version-controlled `QUERY_INTENTS` table in `scripts/search_catalog.py` handles **seven exact normalized paraphrases**: ADR supersession, .NET/C# boundaries, TS/Node exports, Java/Scala builds, Python wheels/src layout, catalog claim audits and agent search evaluation. Intents apply only when the complete lowercase token sequence matches; they do **not** override longer ambiguous questions. Existing lexical scoring, canonical-ID precedence, status/category filters, graph expansion and offline operation remain available.

The expanded [golden fixture](../tests/fixtures/retrieval_gold.json) records expected Top-1 results and evidence labels for canonical IDs and these human-authored paraphrases. Do not infer that a passing suite measures real-world user relevance or fully grounds any answer. On a zero-hit query, report that the indexed search found no candidate—not that the architecture concept is absent.
