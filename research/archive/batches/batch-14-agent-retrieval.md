# B14 — Agent-friendly retrieval, governance and language overlays

**Date:** 2026-11-07. **Branch:** `curation/b7-b14-knowledge-gaps-20261107`. **Shared draft PR:** #3.

## Context and deduplication before implementation
The B13 branch index contained **86 canonical concepts, all reviewed, zero stubs**. We inspected `scripts/search_catalog.py`, `scripts/validate_catalog.py`, the golden retrieval fixture, `docs/agentic-search.md`, `docs/evidence-policy.md` and the existing `decision-records` concept. We also inspected taxonomy and category navigation. Existing lexical search supported exact IDs, tokenized aliases, category/status filtering and one-hop related expansion; validation already checked schema, frontmatter, related IDs, source counts and local concept links.

**Deduplication decisions:** retain `decision-records` as the ADR format, adding `adr-lifecycle` for change management. Retain `project-structure-selection` and project-type archetypes as general selectors; add language overlays only for platform-specific conventions. `knowledge-index-validation` documents metadata versus content-evidence integrity, while `retrieval-evaluation` documents candidate-ranking tests rather than pretending search proves technical correctness.

## Source and framework context (accessed 2026-11-07)
- [.NET web architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures), [.NET dependency injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection): project boundaries and scope pitfalls.
- [Node.js package exports](https://nodejs.org/api/packages.html) and [TypeScript module resolution](https://www.typescriptlang.org/docs/handbook/modules/reference): public entrypoints, ESM/module-resolution compatibility.
- [Java Language Specification, packages and modules](https://docs.oracle.com/javase/specs/jls/se25/html/jls-7.html) and [sbt multi-project builds](https://www.scala-sbt.org/1.x/docs/Multi-Project.html): JVM package visibility and build coordination.
- [Python Packaging, src vs flat](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) and [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/): source layout, installable packages and clean-install tests.
- [AWS ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) and [Martin Fowler ADR](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html): decision record ownership, history and supersession.
- [Python unittest documentation](https://docs.python.org/3/library/unittest.html), [GitHub code ownership](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework): tests, review responsibilities and evaluation governance.

These are platform source facts and workflow precedents. Query targets, recommendation heuristics and examples are curator choices, not externally verified empirical improvements.

## B14 delivered concepts
1. `adr-lifecycle`
2. `dotnet-and-csharp-overlay`
3. `typescript-and-node-overlay`
4. `java-and-scala-overlay`
5. `python-overlay`
6. `knowledge-index-validation`
7. `retrieval-evaluation`

Seven new pages are indexed as **reviewed, scoped**. Expected post-B14 branch inventory: **93 total, 93 reviewed, 0 stubs**. Existing 86 pages are retained; no new category was necessary.

## Executable agent retrieval change
- The existing deterministic offline search remains the primary interface and retains canonical-ID scoring, title/tags/summary/related terms, filters, stable ranking and graph expansion.
- `QUERY_INTENTS` covers **seven exact normalized human paraphrases**. These are explicit reviewed query-to-ID mappings; they only apply to whole normalized queries, reducing broad synonym collisions. This is not semantic embedding, a hosted search service or source-content ranking.
- Golden retrieval fixture expands from **69** to **83** queries: 7 canonical B14 IDs and 7 intended paraphrases, including existing earlier regression cases and a deliberate miss. `tests/test_search_catalog.py` checks canonical and paraphrase retrieval, `reviewed` status and `requires-source-inspection`.
- Retrieval failure is a **candidate-lookup gap**, not proof the concept does not exist. Review page and exact sources before suggesting changes to a target application.

## Agent verification protocol
1. **Discover:** inspect category/taxonomy, run offline search, keep 2–5 likely candidates.
2. **Disambiguate:** compare actual platform/runtime and decision questions; use explicit ID or query intent when supported.
3. **Verify:** read the canonical page and primary sources; classify application evidence as observed, source-backed, inferred or unknown; never upgrade confidence merely from the search score or review status.
4. **Recommend:** compare no change and a minimal, reversible alternative; cite evidence and name gaps.
5. **Evaluate:** run metadata validation, retrieval fixture, and application-specific tests before making a claim of improvement. Expand the query corpus with negative cases and held-out user paraphrases.

## Validation, limits and remaining follow-ups
Verify seven new pages' frontmatter, source count, local links and related IDs, run `python scripts/validate_catalog.py` and `python -m unittest discover -s tests -v` through the shared PR's GitHub Actions. Check all 83 retrieval gold queries after code updates. Record actual workflow results in the campaign tracker.

**Not done by the catalog tests:** no independent primary-URL/claim entailment audit of all 93 pages; no source version-freshness monitor, real user query relevance evaluation, semantic embedding benchmark, or application-specific refactoring, security, Sonar, navigation or runtime test. The matching code is deterministic lexical candidate retrieval, not answer verification.
