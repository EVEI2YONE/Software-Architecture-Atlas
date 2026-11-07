---
id: project-structure-selection
title: "Application file and project structure selection"
category: code-organization
status: stub
reviewed_at: null
---

# Application file and project structure selection

> **Status: research stub.** This is a knowledge gap and research plan, **not a validated recommendation**. No target application or production metrics have been inspected.

## Question and impact
How should application code, project and file boundaries evolve to reduce accidental code and navigation friction while improving maintainability, proven reuse, modularity and extensibility without overengineering?

## Dimensions to investigate
- **Project kind:** UI/web/mobile/desktop; API; serverless Functions; scheduled/background WebJobs/workers; shared libraries/packages; multi-project solutions.
- **Growth stage:** prototype; MVP; growing business with several collaborating projects; enterprise with multiple teams, compliance and independent lifecycles.
- **Architecture evidence:** framework/runtime conventions; capability ownership; deployment cadence; coupling and dependency graph; build time; tested contracts; representative developer change tasks.
- **Layout alternatives:** flat structure; framework-native conventions; feature-first/vertical slices; layered folders; modular monolith; separately deployable services; selective shared packages.
- **Reuse:** distinguish shared business behavior from superficially identical code; guard against general-purpose `Common`/ `Shared` dumping grounds.
- **Code reduction:** safe deletion, unnecessary indirection, duplicate mapping/boilerplate, and accidental abstraction versus readability/correctness.

## Research matrix (questions, not rules)

| Application type | Prototype / MVP to examine | Growing / enterprise to examine |
| --- | --- | --- |
| UI | Route- or feature-local views, state and tests versus framework folders | Shared design system, domain features, contract boundaries and team ownership |
| API | Endpoint-centric slices versus controller/service/repository layers | Modular business capabilities, contract versioning and deployment boundaries |
| Functions | Trigger-local entrypoints with focused business logic | Independent triggers, packaging, retries/idempotency and common code ownership |
| WebJobs / background workers | Job-centric handler, schedule, tests | Worker-specific deployment, queues, checkpoints and operational ownership |
| Libraries | Local module versus publishing a separate library | Stable public API, versioning, dependency direction and consumer count |
| Multi-project systems | One deployable with clear internal modules | Multiple UI/API/functions/workers and selectively shared contracts versus over-fragmentation |

Do not equate enterprise with microservices or prototype with zero tests. Split along observed business/deployment boundaries, not a fixed number of files.

## Proposed evidence gathering and validation
1. Inspect a representative real repository tree, language/framework versions, dependency graph, deployables and tests; inventory developers' navigation tasks.
2. Record a no-change baseline: time/file hops to find a feature, files changed per ticket, accidental duplication, module/package count, circular references, build/test duration, release coordination.
3. Compare minimal folder relocation, feature grouping, module extraction and cross-project sharing; document their trade-offs and counterexamples.
4. Prototype one isolated change, preserve public behavior, test and measure before/after navigation, coupling, net maintained code (excluding generated output), clarity, compilation and regression risks.
5. Report recommendation confidence: observed, inferred, provisional or unknown. Include affected paths, tests, incremental migration and rollback.
6. Research authoritative platform documentation and architecture case studies for each selected runtime. Do not promote until applicability, competing approaches and primary-source links are documented.

## Agent search aliases
- UI API Functions WebJobs libraries application file structure
- prototype MVP growing business enterprise project organization
- feature first folders vertical slice modular monolith code navigation
- reduce code duplication improve reuse modularity extensibility
- multi project solution library sharing and developer discoverability

## Related concepts
- [feature-first-folders](feature-first-folders.md)
- [modularity](modularity.md)
- [code-simplification](code-simplification.md)
- [dependency-inversion](dependency-inversion.md)

## Evidence and sources
_None curated yet; do not cite this stub as verified guidance._

## Maintenance
- Research status: backlog / P0 candidate for developer-experience focused reviews
- Owner: unassigned curator
- Revisit: new platform conventions, real application review or measured developer friction
