---
id: dependency-inversion
title: "Dependency direction and injection"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Dependency direction and injection

> **Reviewed: scoped .NET-oriented guidance.** Do not assume every class requires an interface or dependency injection (DI) container.

## Core distinction
**Dependency inversion** means high-level policy need not depend on replaceable low-level implementation details. **Dependency injection** supplies dependencies from outside a class. A DI container is an optional composition mechanism; it is not equivalent to dependency inversion.

Microsoft's Clean Architecture discussion places interfaces in the application core with infrastructure implementations depending on that core [1]. Microsoft's DI guidelines recommend avoiding service locator and unnecessary runtime resolution, and describe object-lifetime and testing considerations [2].

## Decision and trade-offs
- For stable, trivial local code, a direct call may be simplest. Introducing an interface for a single stable implementation can increase indirection without reducing coupling.
- At a meaningful infrastructure boundary (persistent storage, outbound provider, clock, external service), consider a narrow consumer-owned interface **if** doing so protects policy or enables necessary test substitution.
- Place wiring in the entrypoint/composition root. Avoid resolving dependencies from ambient globals or service locator access hidden inside business logic.
- Respect lifetime rules (such as scoped service dependencies captured by singleton services in .NET) and disposal ownership.

## Illustrative dependency direction

```text
API entrypoint --> Orders policy interface --> Orders policy
                          ^                       |
                          | uses port              v
                     Storage port <-- Storage adapter
```

This diagram is conceptual; dependency graph and runtime invocation are not identical. A smaller codebase may keep modules in one project.

## Failure modes and counterexamples
- A container registration error breaks composition even when source dependencies compile.
- Interface-per-class can multiply files, obscure navigation and make simple changes harder.
- A shared interface package used by every feature can produce coupling in the opposite direction.
- Direct construction is reasonable for pure value objects and short-lived private implementation details.

## Verification and migration
Review imports/project references and a representative test requiring infrastructure substitution. Compare direct calls, a local interface and a separated port. Change one boundary at a time; verify DI registration, lifetimes, integration behavior and build graph. Revert if indirection cost outweighs the observed need.

## Search aliases
dependency inversion; dependency injection; DI lifetime; service locator; ports and adapters; interface overengineering

## Related concepts
- [modularity](modularity.md)
- [dependency conflicts](../dependencies/dependency-conflicts.md)
- [code simplification](code-simplification.md)

## Evidence and sources
1. Microsoft Learn, *Common web application architectures*, https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures (accessed 2026-11-07), particularly Clean Architecture sections.
2. Microsoft Learn, *Dependency injection guidelines*, https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-guidelines (accessed 2026-11-07), applicable to .NET DI and its lifecycle/anti-patterns.

## Maintenance
Reviewed: 2026-11-07. Revisit for framework/container changes, lifetime failures or new boundary requirements.
