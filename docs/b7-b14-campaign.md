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
| B7 | Yes | 9/9 reviewed pages (4 stub upgrades, 5 new) | 9 pages passed metadata/source/link checks; GitHub Actions succeeded on commit 9a61420 | Complete (scoped catalog curation) |
| B8 | Yes | 6/6 reviewed pages (1 stub upgraded, 5 new) | GitHub Actions succeeded on commit 2e48665; catalog and retrieval tests | Complete (scoped catalog curation) |
| B9 | Yes | 12/12 reviewed pages (5 stub upgrades, 7 new) | 12 connector page checks passed; CI pending | Curated, awaiting workflow validation |
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

## B7 verification (follow-up)
- Connector-based checks of all nine B7 pages: frontmatter/index consistency, `source_count` vs numbered source URLs, and local concept links: 9 checked, 0 errors.
- GitHub Actions pull-request workflow on commit `9a61420781e80390bec4defe47d61946c936c8f9`: completed with **success**. The local Python commands were not run due to container DNS. Verify the associated workflow logs for exact test coverage before asserting the specific commands passed.

## B8 implementation record (2026-11-07)
- Context/research documented in [B8 report](batch-8-structure-navigation.md), after comparison with existing archetypes and feature-first, modularity, and evolution entries.
- Upgraded `project-structure-selection` from stub; added `vertical-slice-architecture`, `package-by-feature-vs-layer`, `module-public-contracts`, `architecture-dependency-rules`, `monorepo-vs-multirepo` as scoped reviewed guidance.
- Index: 57 total, 41 reviewed, 16 stubs; category README and branch coverage report updated.
- Six B8 page checks performed via GitHub connector: frontmatter/index consistency, numbered citation metadata and local concept links; **0 errors**. Not a substitute for executing all repo Python validation/tests; remote CI result recorded separately when available.
- Sources: official Microsoft Learn architectural and ASP.NET Core feature-organization guidance; Nx module-boundary and monorepo/polyrepo tool documentation (Nx product-vendor view, not independent empirical outcome).
- No target application was inspected or refactored; navigation or code reduction benefits remain hypotheses to test on actual projects.

## B8 regression repair
- Initial GitHub Actions run `42357378764` reported `CATALOG VALID: 57 indexed concepts`, but failed six retrieval tests because previously fixed expectations still labelled `project-structure-selection` as a stub.
- Updated `tests/test_search_catalog.py`, `tests/test_retrieval_gold.py`, and `tests/fixtures/retrieval_gold.json` to reflect its documented promotion to `reviewed`, add canonical retrieval coverage for five new B8 IDs, and retain a negative regression using the actual `caching` stub (evidence remains `unknown`).
- CI status for subsequent commits must be checked independently. Do not label the entire validation suite successful based only on connector-side checks.

## B8 completed verification
- GitHub Actions workflow run `42357485179` on commit `2e486651fb00b220c762cf3d24396f88abac0081` completed **success** after updating the final stale test assertion.
- Prior CI logs independently confirmed catalog validation against 57 concepts and revealed the original test expectation mismatch. All B8 metadata/source-count/local-concept-link checks reported zero errors.
- This is catalog schema and regression-test verification; it does not independently certify references or prove target-application benefit.

## B9 curation record (2026-11-07)
- Source context and decision boundaries in [B9 report](batch-9-dependencies-quality.md). Five existing stubs upgraded: `dependency-conflicts`, `supply-chain`, `cognitive-complexity`, `quality-gates`, `testing-strategy`.
- Seven scoped reviewed pages added: `transitive-dependency-resolution`, `package-locking-and-version-policy`, `cyclic-dependency-prevention`, `dead-code-and-dependency-removal`, `sonar-rules-and-quality-profiles`, `mutation-and-contract-testing`, `architecture-fitness-functions`.
- Canonical index: 64 total, 53 reviewed, 11 stubs on campaign branch; category READMEs, coverage, 37-case golden query fixture and search regression tests updated.
- Connector-side checks on all 12 pages verified index/frontmatter consistency, numbered source counts and related/local concept links; 0 errors. CI status recorded separately. No target app package graph or Sonar scan supplied.
