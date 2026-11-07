# Agent instructions — Software Architecture Atlas

## Purpose
Use this catalog as a retrieval-first, evidence-aware guide for architecture reviews and knowledge-gap identification. It is not a substitute for verified repository inspection or real measurements.

## Retrieval contract
1. Read `README.md`, `catalog/index.json`, and `catalog/taxonomy.json` before browsing concept files.
2. Retrieve by canonical `id`, tag, title, summary and related-concept links. Load only relevant files into context. Never dump the entire repository to answer a narrow question.
3. Follow `path` from the index, validate target exists and read the article's `status` and sources.
4. Explicitly label recommendations as **verified**, **inferred**, **provisional**, or **unknown**, and cite target repo paths/lines when available.
5. A `stub` is coverage intent, not evidence of a recommendation. Do not cite stubs as proof.
6. Report missing concepts and stale/weakly sourced guidance using `templates/gap-request.md`.

## Architecture-review priorities
- Establish the product goals, constraints, workloads, runtime/language versions and existing architecture before recommending patterns.
- Assess correctness/security; coupling and dependency conflicts; module cohesion; readable file organization; duplicated/unused code; quality gates; concurrency, caching and scalability only when relevant.
- Prioritize smallest justified changes. Compare no-change and simpler alternatives. Do not pursue fewer lines at the cost of clarity, safety or testability.
- Sonar compliance requires the target's actual quality profile, issue rules and gate settings; never claim a green gate without a verified scan.
- Separate observed evidence, hypotheses and proposed experiments. Include trade-offs, risk, migration, tests and rollback.
- Do not edit application code or modify other repositories without specific authorization.

## Curation workflow
- Use exact canonical IDs, one page per concept, all indexed in `catalog/index.json`.
- Add reviewable source links and reviewed date before changing `stub` to `reviewed`.
- Keep summaries concise and navigable with section headings, related-concept links and search aliases.
- Run `python scripts/validate_catalog.py` before proposing changes.

## Self-heal
When a user or validation flags omissions, wrong links, weak evidence or broken retrieval, explain the failure mode, fix the relevant source/schema/index/test, and record a generalizable prevention rule in `docs/curation-workflow.md` rather than patching only the symptom.
