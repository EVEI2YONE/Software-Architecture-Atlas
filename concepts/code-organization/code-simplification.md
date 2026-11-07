---
id: code-simplification
title: "Code reduction and readability"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Code reduction and readability

> **Status: reviewed (scoped guidance).** Sources support concrete refactoring options and evolutionary design. They do **not** establish that reducing lines or files by itself improves quality. No codebase-specific reductions have been measured.

## Goal

Reduce *accidental* maintained code while preserving behavior, accessibility, error handling, security, testability and developer comprehension. Total LOC is a secondary observation, not the success criterion.

## Evidence-backed options

- **Remove dead code** when demonstrated unused and safe to delete, after checking public reflection, dependency injection, dynamic imports, jobs and external consumers. "Remove Dead Code" is cataloged by Fowler [1].
- **Inline needless indirection** when a function/class adds no meaningful separation and the resulting code becomes clearer; Fowler catalogues Inline Function, Inline Class and Remove Middle Man [1].
- **Extract a cohesive function/module** when it makes intent visible or avoids fragile repeated behavior, not to satisfy arbitrary file-size thresholds. Fowler catalogues Extract Function and Move Function [1].
- **Defer speculative extensibility:** Fowler's YAGNI discussion distinguishes premature capabilities from deliberate refactoring that keeps software easy to change [2].

These are **candidate operations**, not automatic code transformations.

## Decision checklist

1. What task or defect triggered simplification? Inspect affected callers and tests.
2. What behavior must remain invariant (including errors, configuration, observability and concurrency)?
3. Is duplication truly the same business behavior or similar code with separate change reasons?
4. Can a smaller change solve the problem (rename, delete unused branch, inline wrapper) before extracting a shared package?
5. Would the new abstraction increase cognitive load, coupling, import depth or migration effort?
6. How will before/after findings be measured and rolled back?

## Alternatives and failure modes

| Option | Benefit sought | Warning |
| --- | --- | --- |
| Keep existing code | No migration risk | Acceptable when change friction is low |
| Delete unused code | Less maintained surface | Dynamic or external uses may be invisible to basic searches |
| Inline wrapper/adapter | Fewer hops and abstractions | May duplicate necessary boundary logic or leak dependencies |
| Extract shared function | Centralizes *stable* behavior | Incorrect abstraction can force unrelated features to change together |
| Extract package/project | Separates mature public API and lifecycle | Adds versioning, build and ownership overhead |

**Inference:** Prefer the least intrusive reversible change that a representative developer can explain and validate. Avoid claiming that more generic APIs automatically imply more reuse or extensibility.

## Worked hypothetical comparison

Before: multiple simple pass-through services each forward the same request to a handler, with no validation or policy. Candidate change: invoke the handler directly and delete the pass-through layer. Counterexample: preserve that layer if it enforces security, transactions, auditing or framework-required boundaries. Record exact touched files and tests before deleting anything.

## Evaluation and rollback

Baseline and after: net maintained LOC, number of classes/files, caller-to-behavior hops, dependency cycles, representative task completion time and files changed per ticket. Compare compiler, unit/integration/contract tests, public API and runtime checks. Never infer improved performance or Sonar compliance from file counts. Revert if behavior or navigability regresses.

## Search aliases

remove boilerplate; reduce code; simplify layers; unnecessary abstraction; unused code; code duplication; inline wrapper; code footprint

## Related concepts

- [feature-first-folders](feature-first-folders.md)
- [modularity](modularity.md)
- [project-structure-selection](project-structure-selection.md)
- [DRY versus premature abstraction](../principles/dry-vs-abstraction.md)

## Evidence and sources

1. Martin Fowler, *Catalog of Refactorings*: https://refactoring.com/catalog/ (accessed 2026-11-07). **Direct support:** named behavior-preserving refactoring options and their trade-offs; verify each refactoring's preconditions in the linked catalog entry.
2. Martin Fowler, *Yagni*, published 2015-05-26: https://martinfowler.com/bliki/Yagni.html (accessed 2026-11-07). **Direct support:** cost of speculative capabilities/abstractions and importance of keeping code malleable.

## Maintenance

- Reviewed: 2026-11-07; language-agnostic at principle level, but implementation and verification depend on runtime/framework.
- Revisit after contradictory refactoring evidence, changes to dynamic usage or public-consumer assumptions.
