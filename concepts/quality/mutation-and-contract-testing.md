---
id: mutation-and-contract-testing
title: "Mutation and contract testing"
category: quality
status: reviewed
reviewed_at: 2026-11-07
---

# Mutation and contract testing

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
High line coverage overlooks incorrect predicates and consumers break after API evolution.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
Use mutation tests to assess assertions and contract tests to validate consumer/provider compatibility; they serve different purposes.

### Simpler/no-change option
Start with carefully chosen negative examples and integration tests; scale tooling only if justified.

### Risks, failure modes and counterexamples
Equivalent mutants waste effort; contracts cannot guarantee all runtime integration semantics.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Deliberately change one behavior in controlled tests and confirm failures; verify provider contract and roll back noisy tools. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
mutation and contract testing; mutation and contract testing; maintainability; software quality; dependency hygiene

## Related concepts
- [testing-strategy](../quality/testing-strategy.md)
- [api-contracts](../distributed-systems/api-contracts.md)

## Evidence and sources
1. Microsoft unit testing best practices, https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. Microsoft ASP.NET Core integration testing, https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
