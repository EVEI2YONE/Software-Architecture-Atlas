---
id: async-await
title: "Async/await and cancellation"
category: runtime
status: stub
reviewed_at: null
---

# Async/await and cancellation

> **Status: research stub.** This page is a structured topic placeholder, **not** a verified best-practice claim. Curators must research and cite evidence before marking it reviewed.

## Why this matters
Avoid sync-over-async, propagate cancellation and bound concurrent work.

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
- Async/await and cancellation
- async await

## Related concepts
- [thread-safety](../../runtime/thread-safety.md)
- [backpressure](../../runtime/backpressure.md)

## Evidence and sources
_None curated yet. Do not represent this stub as validated guidance._

## Maintenance
- Research status: backlog
- Suggested revisit trigger: new framework version, production incident, or contradictory evidence
