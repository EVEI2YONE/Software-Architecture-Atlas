---
id: python-overlay
title: "Python architecture and packaging overlay"
category: code-organization
status: reviewed
reviewed_at: 2026-11-07
---

# Python architecture and packaging overlay

> **Scoped research guidance, not target-repository verification.** Source-backed platform behavior, inferred trade-offs and missing project-specific evidence are distinct. A reviewed catalog page always requires source inspection.

## Problem and context
A Python API, worker and library share imports that work from the repo root but fail in installed/test environments.

## Applicability and decision
Distinguish installable import packages from source directories, document pyproject.toml packaging metadata and prefer a src layout when it helps catch accidental direct-source imports. Keep FastAPI/task framework entrypoints discoverable and separate true library contracts from application wiring.

### Simpler/no-change option
A script or prototype can use a flat layout and one environment; adopt src layout and packaging only when distribution, test isolation or reusable libraries make it worthwhile.

### Failure modes and counterexamples
Relative imports, namespace packages, editable installs and test invocation can behave differently from published artifacts. Deep framework package trees add navigation cost for simple scripts.

## Illustrative example (not an inspected application)
Illustrative `pyproject.toml`, `src/orders/`, `tests/` for a published library; a tiny internal job may stay at `jobs/invoice.py` with a dedicated environment and tests.

## Validation, migration and rollback
Build and install wheel in a clean virtual environment, run tests without relying on the repo working directory, validate import paths and dependency groups. Roll back reorganization if deploy entrypoints break. Preserve original application behavior and compare against no-change. Verify framework/runtime/build-tool version and platform conventions; use a small reversible change before broad reorganization. Never assert measured code reduction, security, developer navigation or quality-gate success without a target application's results.

## Search aliases
python overlay; python architecture and packaging overlay; python; pyproject; src-layout; packaging; source applicability

## Related concepts
- [libraries-project-structure](../code-organization/libraries-project-structure.md)
- [functions-project-structure](../code-organization/functions-project-structure.md)
- [project-structure-selection](../code-organization/project-structure-selection.md)

## Evidence and sources
1. Python Packaging User Guide, src layout vs flat: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/ (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.
2. Python Packaging User Guide, Packaging Python Projects: https://packaging.python.org/en/latest/tutorials/packaging-projects/ (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.

## Maintenance
Reviewed 2026-11-07. Revisit on policy/tool/version changes, contradictory sources or observed application behavior. Independent detailed claim-to-source and project-specific audits remain open.
