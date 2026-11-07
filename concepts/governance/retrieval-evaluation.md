---
id: retrieval-evaluation
title: "Agent retrieval evaluation and query disambiguation"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Agent retrieval evaluation and query disambiguation

> **Scoped research guidance, not target-repository verification.** Source-backed platform behavior, inferred trade-offs and missing project-specific evidence are distinct. A reviewed catalog page always requires source inspection.

## Problem and context
An agent's search finds a technically adjacent concept, but not the intended decision or framework overlay.

## Applicability and decision
Evaluate canonical-ID retrieval and representative natural-language queries with version-controlled expected IDs and evidence statuses; distinguish matching from answer grounding. Add specific aliases only for demonstrated misses, compare Top-1/Top-k and maintain deterministic lexical fallback.

### Simpler/no-change option
Keep the small offline lexical index and evaluate it first; embeddings, re-rankers and hosted APIs introduce complexity and do not inherently verify claims.

### Failure modes and counterexamples
A golden set of self-matching concept IDs inflates accuracy. Broad aliases may bias unrelated queries; exact ID matches must remain stable; category/status filters and related expansion must remain deterministic.

## Illustrative example (not an inspected application)
Disambiguate 'python wheel packaging' to python-overlay, 'ADR superseded' to adr-lifecycle and 'dependency hell' to dependency-conflicts; open the selected concept and cite primary sources before offering advice.

## Validation, migration and rollback
Run golden lexical regression after index/alias changes; add held-out paraphrases, negative/unmatched questions, filtering/related expansion and label evidence. Measure retrieval hit rate with a stated evaluation set; do not claim semantic relevance from this suite alone. Preserve original application behavior and compare against no-change. Verify framework/runtime/build-tool version and platform conventions; use a small reversible change before broad reorganization. Never assert measured code reduction, security, developer navigation or quality-gate success without a target application's results.

## Search aliases
retrieval evaluation; agent retrieval evaluation and query disambiguation; retrieval; agent-search; evaluation; aliases; disambiguation; source applicability

## Related concepts
- [knowledge-index-validation](../governance/knowledge-index-validation.md)
- [project-structure-selection](../code-organization/project-structure-selection.md)
- [decision-records](../governance/decision-records.md)

## Evidence and sources
1. NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.
2. Python Standard Library, unittest: https://docs.python.org/3/library/unittest.html (accessed 2026-11-07). Scope: the named platform, documentation workflow or evaluation approach, not a benchmark of this catalog.

## Maintenance
Reviewed 2026-11-07. Revisit on policy/tool/version changes, contradictory sources or observed application behavior. Independent detailed claim-to-source and project-specific audits remain open.
