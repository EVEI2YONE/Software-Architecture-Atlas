---
id: java-and-scala-overlay
title: "Java and Scala architecture overlay"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Java and Scala architecture overlay

> **Scoped research guidance, not target-repository verification.** Source-backed platform behavior, inferred trade-offs and missing project-specific evidence are distinct. A reviewed catalog page always requires source inspection.

## Problem and context
A JVM solution mixes business packages, shared build modules and public APIs without a clear dependency and versioning policy.

## Applicability and decision
Use cohesive packages first and compiled modules only for justified access constraints, shared contracts or independent deployment. Java Platform Module System exports and requires clauses can enforce visibility; Scala build/project structure must account for the actual sbt/Gradle/Maven toolchain and cross-built binaries.

### Simpler/no-change option
A small single JVM project organized by feature and tests may be simpler than a many-module build; language-specific style and framework conventions override generic folder prescriptions.

### Failure modes and counterexamples
Public classes in Java are not automatically exported outside a named JPMS module; over-modularization increases build orchestration. Scala binary cross-version and Java/Scala compilation order require tested artifact compatibility.

## Illustrative example (not an inspected application)
Illustrative `app.orders` domain package plus `app.adapters` infrastructure; if shared contract consumers exist, expose only `orders.api`, with Java `module-info.java` if the project actually adopts JPMS.

## Validation, migration and rollback
Compile and test actual Gradle/Maven/sbt configurations, inspect API exports, resolve dependency cycles and publish/consume an artifact when relevant. Measure navigation versus module count. Preserve original application behavior and compare against no-change. Verify framework/runtime/build-tool version and platform conventions; use a small reversible change before broad reorganization. Never assert measured code reduction, security, developer navigation or quality-gate success without a target application's results.

## Search aliases
java and scala overlay; java and scala architecture overlay; java; scala; jvm; jpms; sbt; gradle; source applicability

## Related concepts
- [package-by-feature-vs-layer](../code-organization/package-by-feature-vs-layer.md)
- [module-public-contracts](../code-organization/module-public-contracts.md)
- [cyclic-dependency-prevention](../dependencies/cyclic-dependency-prevention.md)

## Evidence and sources
1. Java Language Specification 25, Packages and Modules: https://docs.oracle.com/javase/specs/jls/se25/html/jls-7.html (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.
2. sbt documentation, Multi-project builds: https://www.scala-sbt.org/1.x/docs/Multi-Project.html (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.

## Maintenance
Reviewed 2026-11-07. Revisit on policy/tool/version changes, contradictory sources or observed application behavior. Independent detailed claim-to-source and project-specific audits remain open.
