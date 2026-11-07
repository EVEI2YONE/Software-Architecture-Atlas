---
id: package-locking-and-version-policy
title: "Package locking and version policy"
category: dependencies
status: reviewed
reviewed_at: 2026-11-07
---

# Package locking and version policy

> **Reviewed: scoped source-backed decision guidance.** The citations support ecosystem behavior or testing/quality methods, not verified improvements in an uninspected target application.

## Problem and context
CI and local machines install different package graphs.

## Applicability and constraints
Select advice using actual package manager, runtime, framework versions, deployment topology, test ownership and active analyzer/quality profile. Prototype, MVP and enterprise contexts may warrant different levels of formal enforcement; no universal tooling or numeric threshold is implied.

## Decision and trade-offs
For applications, use consistent lockfiles and toolchain versions; for libraries, assess supported dependency ranges and consumer compatibility.

### Simpler/no-change option
Keep existing package management when it already produces reproducible results.

### Risks, failure modes and counterexamples
A lock cannot freeze build scripts or services; changed npm flags can invalidate lock replay.

## Illustrative application example
In a UI/API/worker solution, inspect the package declarations, lockfiles, import graph and CI execution before changing module boundaries, removing dependencies or claiming static-analysis compliance. A single coherent change with clear tests is preferable to extracting layers or reducing raw LOC without evidence.

## Verification, migration and rollback
Run supported locked restore or npm ci, then builds and tests; commit manifest and lock changes together. Record observed evidence versus inference, tested consumers, a reversible change plan and the stop criteria. **Sonar status remains not run/unknown** for any target project unless actual scanner output is provided.

## Search aliases
package locking and version policy; package locking and version policy; maintainability; software quality; dependency hygiene

## Related concepts
- [transitive-dependency-resolution](../dependencies/transitive-dependency-resolution.md)
- [supply-chain](../dependencies/supply-chain.md)

## B18: reproducible React/Vite install and build gate

For an application, commit the npm lockfile and compatible project npm configuration, pin the supported Node/npm versions in CI, and run `npm ci` on a **clean** runner. npm ci rejects lock/manifest disagreement rather than silently modifying the lock [npm CLI v11](https://docs.npmjs.com/cli/v11/commands/npm-ci/). Run a separate applicable TypeScript project typecheck (`tsc --noEmit` or `tsc -b`) because a Vite production build alone is not a type-safety check, then run tests and Vite's production build. A locally unavailable npm registry is a **blocked local gate**, not proof of a passing build.

See the [B18 clean-build and browser verification runbook](../../docs/batch-18-production-verification.md), plus [Vite production builds](https://vite.dev/guide/build) (checked 2026-11-07). Actual scripts must be read from the target project's package.json before using example commands.

## Evidence and sources
1. npm ci v11, https://docs.npmjs.com/cli/v11/commands/npm-ci/ (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.
2. NuGet PackageReference and lock files, https://learn.microsoft.com/en-us/nuget/consume-packages/package-references-in-project-files (accessed 2026-11-07). Applicability: the named ecosystem/tool and the specific behavior described above; not a benchmark of architectural success.

## Maintenance
Reviewed 2026-11-07. Revisit on new tool/runtime versions, conflicting vendor behavior, target-specific incidents or independent claim-source audit. No real application code was changed or tested.
