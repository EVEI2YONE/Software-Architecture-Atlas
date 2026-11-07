# B12 — Distributed systems and integration reliability

**Date:** 2026-11-07. **Branch:** `curation/b7-b14-knowledge-gaps-20261107`; shared **draft PR #3**. Scope is evidence-backed catalog curation, not a production integration audit.

## Context gathered before implementation
After B11, the branch had 76 concepts: 72 reviewed, 4 stubs. The three B12 stubs were `consistency`, `event-driven`, `queues`; the last remaining non-B12 stub was `caching`, reserved for B13. Before adding new concepts, we inspected the existing pages and reviewed `idempotency`, `api-contracts`, `transactions`, `domain-events`, `backpressure` and the campaign context matrix.

Primary research reviewed on 2026-11-07:
- Microsoft Azure [event-driven architecture style](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven) and [microservices guidance](https://learn.microsoft.com/en-us/azure/architecture/microservices/) — asynchronous integration trade-offs, contract and observability needs.
- Azure Service Bus [message sessions](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) and [duplicate detection](https://learn.microsoft.com/en-us/azure/service-bus-messaging/duplicate-detection) — ordering, tier, duplicate-detection-window limits and effects of redelivery.
- AWS Prescriptive Guidance [transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) and [saga patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html).
- Azure [compensating transactions](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction) — business compensations can fail or require manual handling.
- Confluent [schema evolution and compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) — directionality, transitivity, schema-format caveats.

These sources establish capabilities and design alternatives. They are not evidence of exactly-once business effects, outage recovery or throughput in a target application.

## Deduplication and acceptance decisions
- `consistency` covers distributed stale reads and convergence, not database isolation already in `transactions`/`isolation-levels`.
- `event-driven` covers integration topology, not local business facts already in `domain-events`.
- `queues` covers durable messaging, session ordering, retries and dead-letter operations; `backpressure` remains the admission/overload topic.
- `delivery-guarantees` specifies exact scope of guarantees (producer to broker, broker to consumer, consumer to business effect). Broker deduplication is not universal end-to-end exactly once.
- `outbox-pattern` covers state-commit/notification dual writes. Outbox relay retries still require idempotent consumers.
- `sagas-and-compensation` governs cross-service workflows; compensation is not ACID rollback and can fail or be irreversible.
- `schema-and-event-versioning` covers async payload compatibility, complementary to HTTP contracts and database schema evolution.
- `service-boundaries` evaluates independent deployables, data authority and release autonomy; do not equate a bounded context or code module with a microservice.

## Decision matrix (illustrative, not an implemented workflow)
| Situation | Simpler/no-change option | Evidence that may justify distribution | Verification |
| --- | --- | --- | --- |
| One API and one database | Local transaction plus direct call | Asynchronous failure recovery or genuine independent consumer | Commit/rollback and consumer contract tests |
| Notification after order commit | In-process call if no durable delivery requirement | State/event dual-write failure must be closed | Outbox crash before/after commit/publish; deduplication |
| Multiple consumers of order events | Targeted synchronous integration | Independent consumers and replay/recovery requirements | Lag, duplicate, schema and permission tests |
| Stock/payment/shipping workflow | Single owner/transaction when possible | Cross-service long-lived business process | Compensation failures, irreversible actions, orchestration restart |
| Ordered per-account jobs | One serialized worker | Broker sessions/partition handling for independent workers | Out-of-order completion, session expiry, replay |
| Consumer version rollout | Coordinated deployment | Long-lived mixed versions and retained event replay | Old/new producer-consumer compatibility and rollback |

## Delivered
Upgraded `consistency`, `event-driven`, `queues` from stubs to scoped reviewed guidance. Added five new canonical concepts: `delivery-guarantees`, `outbox-pattern`, `sagas-and-compensation`, `schema-and-event-versioning`, `service-boundaries`. Updated canonical index and distributed-systems navigation.

**Expected branch index: 81 concepts, 80 reviewed, 1 stub (`caching`).**

## Completion and open constraints
Validate frontmatter, source counts, local links, related-ID graph and retrieval golden queries. Update the status-filter regression from distributed stubs to `performance`'s real `caching` stub; preserve its `evidence=unknown` expectation. Run `python scripts/validate_catalog.py` and `python -m unittest discover -s tests -v` through GitHub Actions and record the actual status in campaign notes.

No real broker, API, queue, production data or external application was inspected or tested. Capability statements are scoped to named products, versions and tiers. A green CI run checks catalog integrity, not distributed correctness, security or exactly-once effects.
