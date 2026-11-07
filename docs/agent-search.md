# Agentic search and retrieval

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

For deterministic offline querying, use `python scripts/search_catalog.py "sync over async" --json` (optional `--limit`, `--category`, `--status`, `--expand`). See [agentic search guide](agentic-search.md) for result structure, scoring, evidence handling, tests and limitations. Lexical search is a candidate-finding mechanism, not a verification engine.
