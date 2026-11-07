# B7–B14 research campaign: context and progress

Date: 2026-11-07. Base: `main`. Branch: `curation/b7-b14-knowledge-gaps-20261107`. Scope: catalog curation only, not application refactoring.

## Baseline and source-of-truth rules
- `catalog/index.json`: 47 indexed concepts; 26 reviewed, 21 stubs before this campaign. Review status means scoped citations were supplied, **not** independent source-claim or target-application verification.
- Existing reports: [B0 integrity](batch-0-catalog-integrity.md), [B1–B6 plan and reports](knowledge-gap-batches.md), [coverage](coverage.md), [foundational gaps](foundational-gap-assessment.md).
- [Evidence policy](evidence-policy.md), [curation workflow](curation-workflow.md), [concept template](../templates/concept.md), [agent guidance](../AGENTS.md). Keep source counts and dates consistent with index and page; test links; do not invent tests or benefits.
- This file is **context collected for every batch before knowledge-gap implementations**. Research questions and source targets are not evidence that a proposed concept is missing from *all prose*. Check exact IDs and neighboring pages again before creating each one.
- Existing reviewed work to reuse: modularity, dependency inversion, code simplification, six app structure archetypes, architecture evolution, ADRs, idempotency, transactions, API contracts, schema evolution, identity/access, threat modeling, scalability, reliability, deployment, operational costs, observability and workload admission.

## Initial context matrix for all batches

| Batch | Existing stubs to finish | Candidate additional IDs (deduplicate before adding) | Existing reviewed neighbors | Key questions / primary-source research targets | Status |
| --- | --- | --- | --- | --- | --- |
| **B7 Foundations and judgment** | solid; separation-of-concerns; dry-vs-abstraction; kiss-yagni | composition-vs-inheritance; cohesion-and-coupling; information-hiding; architecture-drivers; architecture-styles | modularity, dependency-inversion, decision-records, architecture-evolution | Which principle is relevant to actual change pressure? Which simpler option? Official design/architecture guidance, original software design literature; architecture-style constraints; measurable quality attributes | Context captured; first implementation |
| **B8 Structure and navigation** | project-structure-selection | vertical-slice-architecture; package-by-feature-vs-layer; module-public-contracts; architecture-dependency-rules; monorepo-vs-multirepo | feature-first-folders; UI/API/Functions/WebJobs/libraries/multi-project structure; incremental-boundary-migration | Compare prototype/MVP/growth/enterprise by project type and framework; trace a feature from entrypoint to tests; measure navigation, import cycles and code churn; official framework layout guidance | Context captured; not started |
| **B9 Dependencies and quality** | dependency-conflicts; supply-chain; cognitive-complexity; quality-gates; testing-strategy | transitive-dependency-resolution; package-locking-and-version-policy; cyclic-dependency-prevention; dead-code-and-dependency-removal; sonar-rules-and-quality-profiles; mutation-and-contract-testing; architecture-fitness-functions | code-simplification; dependency-inversion; API contracts | NuGet/npm/Python/JVM official resolver docs, language-aware Sonar rule documentation, tests and real quality profiles; distinguish predicted vs observed failures | Context captured; not started |
| **B10 Domain and data** | bounded-contexts; aggregates; domain-events; cqrs | ubiquitous-language; context-mapping; domain-services-vs-application-services; transactional-invariants; anti-corruption-layers; data-access-boundaries; isolation-levels | transactions; schema-evolution; API contracts | Business invariants, domain ownership, transaction/isolation semantics, migration and API stability; primary DDD and database vendor references | Context captured; not started |
| **B11 Async and concurrency** | async-await; thread-safety; backpressure | cancellation-propagation; structured-concurrency; lock-contention-and-deadlocks; workload-isolation; async-streams-and-channels | workload-admission; resilience | Framework/runtime docs for .NET, JS, JVM, Python; cancellation, structured tasks, bounded queue behavior, deadlocks, saturation and reproducible tests | Context captured; not started |
| **B12 Distributed integration** | consistency; event-driven; queues | delivery-guarantees; outbox-pattern; sagas-and-compensation; schema-and-event-versioning; service-boundaries | idempotency; API contracts; resilience; transactions | Broker/database vendor guarantees and ordering boundaries; duplicate effects; schema compatibility; partial failure and reconciliation | Context captured; not started |
| **B13 Caching/performance** | caching | cache-invalidation-and-stampedes; load-testing-and-baselines; rate-limiting; partitioning-and-sharding; resource-budgets | scalability; workload-admission; observability; operational-costs | Workload baselines and bottlenecks; cache TTL/invalidation; hot keys, backpressure, quotas, partitioning costs; official datastore/performance references | Context captured; not started |
| **B14 Agent retrieval/governance** | none | adr-lifecycle; dotnet-and-csharp-overlay; typescript-and-node-overlay; java-and-scala-overlay; python-overlay; knowledge-index-validation; retrieval-evaluation | decision-records; B0 validator and 20-query lexical benchmark | Query false negatives, aliases, versioned snippets, source-to-claim audit, retrieval tests across application archetypes; prevent overlapping ADR governance | Context captured; not started |

## Batch acceptance and evidence policy
1. For each new ID, check `catalog/index.json`, title, tags, related IDs and neighbor articles for duplication; prefer extending an existing concept where its scope already covers the question.
2. Gather and inspect primary authoritative sources; record exact URLs, access date and applicability. Explicitly distinguish source-backed claims, inference and unknown project-specific outcomes.
3. Supply applicability, simpler/no-change option, decision trade-offs, failure modes, example and counterexample, verification, migration/rollback and revisit trigger.
4. Update canonical page, index metadata, category README and relevant cross-links. Promote a stub to reviewed only when its claims and citations were manually examined; otherwise leave as draft/stub.
5. Run `python scripts/validate_catalog.py` and `python -m unittest discover -s tests -v`; record actual outcomes. Do not represent a future CI run as a pass.
6. Use this same branch and PR for B7–B14; one independently reviewable batch at a time.

## Completion board (update only after verified deliverables)
| Batch | Context gathered | Concept curation | Validation | State |
| --- | --- | --- | --- | --- |
| B7 | Yes | 9/9 reviewed pages (4 stub upgrades, 5 new) | Local Python tests blocked by GitHub DNS; connector checks pending | Curation committed, validation pending |
| B8 | Yes | Not started | Not run | 0% |
| B9 | Yes | Not started | Not run | 0% |
| B10 | Yes | Not started | Not run | 0% |
| B11 | Yes | Not started | Not run | 0% |
| B12 | Yes | Not started | Not run | 0% |
| B13 | Yes | Not started | Not run | 0% |
| B14 | Yes | Not started | Not run | 0% |

## Open constraints
No target application's repository, performance traces, measured developer navigation or project-specific Sonar profile was supplied for this campaign. Accordingly no page may assert measured code reduction, compliance, capacity, security or deployment improvements. External primary-source verification remains topic-by-topic, not automatically satisfied by this context capture.

## B7 implementation record (2026-11-07)
- Source pages: `solid`, `separation-of-concerns`, `dry-vs-abstraction`, `kiss-yagni` upgraded from stub, plus new `composition-vs-inheritance`, `cohesion-and-coupling`, `information-hiding`, `architecture-drivers`, `architecture-styles`.
- Index: 52 total, 35 reviewed, 17 stubs; category READMEs updated.
- Source leads examined: Microsoft Learn architecture styles, common .NET web architectures and microservices; Martin Fowler Yagni, Beck Design Rules and Is Design Dead?; Refactoring.Guru Replace Inheritance with Delegation.
- B7 limitations: scoped conceptual research; no production code evaluation, independent expert review or claims of measured improvement. `git clone` failed in the local container because `github.com` DNS could not resolve; therefore `scripts/validate_catalog.py` and Python unit tests have NOT been executed locally. Remote CI status must be inspected separately.
