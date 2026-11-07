---
id: resilience
title: "Resilience patterns"
category: operations
status: stub
reviewed_at: null
---

# Resilience patterns

> **Status: research stub.** This page is a structured topic placeholder, **not** a verified best-practice claim. Curators must research and cite evidence before marking it reviewed.

## Why this matters
Use timeout, retry budgets, bulkheads and circuit breakers purposefully.

## Decision questions
- What actual workload, ownership boundaries and constraints justify this approach?
- Which simpler alternative would meet the same requirements?
- What failure modes, operational costs and maintainability risks does it introduce?
- How would the benefit be measured and tested?

## Guidance to research
- Appropriate contexts and counterexamples
- Language/runtime-specific caveats and version applicability
- Trade-offs against at least one viable alternative
- Measurable acceptance or review criteria
- Migration and rollback considerations

## Search aliases
- Resilience patterns
- resilience

## Related concepts
- [idempotency](../distributed-systems/idempotency.md)
- [observability](../operations/observability.md)

## Evidence and sources
_None curated yet. Do not represent this stub as validated guidance._

## Maintenance
- Research status: backlog
- Suggested revisit trigger: new framework version, production incident, or contradictory evidence
