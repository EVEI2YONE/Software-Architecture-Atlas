---
id: api-contracts
title: "API contracts and compatibility"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# API contracts and compatibility

> **Reviewed — scoped source-backed guidance, not a target-application audit.**

## Applicability
OpenAPI describes HTTP API surfaces in a language-neutral form; RFC 9110 defines HTTP method semantics. Neither guarantees compatibility with an actual consumer or protects a business operation from duplicate processing.

## Contract decision checklist
- Record methods/paths, payload schemas, required fields, errors, auth schemes, pagination, idempotency and support windows.
- Inventory real consumers, including UI versions, workers and third parties; document old/new deployments.
- Consider required request-field additions, renamed paths, changed field meaning or removed enum options as potential breaking changes. Even additive responses may break strict consumers.
- HTTP GET is safe by protocol semantics; PUT and DELETE have idempotent intended effects under RFC 9110, but transport retries do not guarantee application-level exactly-once side effects.
- Distinguish event contracts from synchronous HTTP contracts; event ordering and delivery require separate reasoning.

## Example and alternatives
Illustrative POST /orders: document validation, authorization, 201/4xx errors and duplicate-key policy. If there is one controlled consumer, coordinated change may be simpler than parallel versions. A public API with legacy consumers may require overlapping compatibility windows.

## Verification and rollback
Validate OpenAPI syntax, compare contract diffs, test negative and authorization paths and run consumer-driven tests against deployed versions. Use gradual deprecation and parallel support where justified; retain rollback of both producer and consumer without assuming storage schema compatibility.

## Search aliases
api contracts; architecture contracts; data and security boundaries

## Related concepts
- [idempotency](../distributed-systems/idempotency.md)
- [event-driven](../distributed-systems/event-driven.md)
- [testing-strategy](../quality/testing-strategy.md)

## Evidence and sources
1. OpenAPI Specification 3.2.1: https://spec.openapis.org/oas/v3.2.1.html (accessed 2026-11-07).
2. RFC 9110 HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110.html (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit after standards/framework changes, incidents, new consumers or changed trust boundaries.
