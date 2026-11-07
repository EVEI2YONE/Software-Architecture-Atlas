---
id: testing-strategy
title: "Architecture-focused testing strategy"
category: quality
status: reviewed
reviewed_at: 2026-11-07
---

# Architecture-focused testing strategy

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
Unit tests miss integration, contract or deployment failures.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Choose unit, integration, contract and end-to-end tests by architecture risk and owned boundaries.

### Simpler/no-change option
Start with deterministic tests for critical business rules and user journeys.

### Risks, failure modes and counterexamples
Mocks can miss serialization and DI; E2E-only suites can be slow and flaky.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Map risks to tests, run negative paths, verify contract compatibility and record coverage limitations. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
architecture-focused testing strategy; testing strategy; maintainability; software quality; dependency hygiene

## Related concepts
- [mutation-and-contract-testing](../quality/mutation-and-contract-testing.md)
- [architecture-fitness-functions](../quality/architecture-fitness-functions.md)
- [quality-gates](../quality/quality-gates.md)

## B18: hosted identity, paper worker and browser acceptance layers

Do not substitute successful source-text tests for TypeScript compilation or a production browser render. A risk-weighted test plan should separately verify: clean dependency install, generated API-contract drift, typecheck, bundler build, authenticated API negative paths, browser navigation, accessible interaction, and production-only controls. For worker reliability, test multiple processes and real database connections plus lease loss, stale-data SKIP, retry and restore/alert drills. For OIDC, test hostile token/nonce/state and cross-tenant cases on deployed domains.

Use [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing) with an axe integration for common errors, followed by **manual keyboard, focus and assistive-technology review**; automated checks cannot certify all accessibility barriers. The [B18 test/acceptance matrix](../../docs/batch-18-production-verification.md) lists specific required negative cases. None is claimed to have run on Final Expanse here.

## Evidence and sources
1. Microsoft ASP.NET Core integration testing, https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Microsoft unit testing best practices, https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
