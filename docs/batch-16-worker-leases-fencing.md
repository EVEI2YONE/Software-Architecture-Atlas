# B16 — Distributed worker coordination, fencing and restart recovery

**Research date:** 2026-11-07. **Targeted blocker:** Final Expanse Phase 5 durable paper-bot automation with multiple independent PostgreSQL workers. **Status:** Reference curation complete; application-specific multi-process proof remains open.

## Context gathered before edits

Existing Atlas concepts describe [idempotency](../concepts/distributed-systems/idempotency.md), [queues](../concepts/distributed-systems/queues.md), [delivery guarantees](../concepts/distributed-systems/delivery-guarantees.md), [locking](../concepts/runtime/lock-contention-and-deadlocks.md) and [reliability](../concepts/operations/reliability-objectives.md). [B15](batch-15-postgresql-concurrency.md) adds short PostgreSQL transactions and SQLAlchemy Session guidance. None of those pages individually explains stale workers resuming after lease takeover, enforcing fencing at every committed effect, or reconciling ambiguous external outcomes. B16 fills that **distinct** coordination gap.

## Research deliverables

1. New indexed canonical [Durable worker leases, fencing and restart recovery](../concepts/distributed-systems/durable-worker-leases-and-fencing.md), retaining the generic queue/idempotency references rather than duplicating them.
2. Candidate architecture comparison: single-process, database-backed claims/leases and durable broker delivery, with explicit non-guarantees for external side effects.
3. Proposed job state machine: due, claimed, succeeded, retry due and halted, with separate ownership, expiration, generation and business-effect identifiers.
4. PostgreSQL claim, renewal and completion **illustrations** using conditional updates, generations and short transactions. Time constants are arbitrary examples, not workload-driven recommendations.
5. Fencing analysis: an expired worker may resume even after re-claim; successful lease acquisition is not proof the previous worker cannot write. Guard all local financial effects in the accepted database transaction. Remote providers require their own idempotency/reconciliation arrangements.
6. Real-PostgreSQL multi-process **proposed failure tests**: competing workers, lease expiry/stale generation, heartbeat failure, crash before/after commit, retries, bot pause, tenant isolation, clock boundaries, and unknown external effects.
7. Catalog navigation, related concept links and natural/canonical retrieval regression cases.

## Source and evidence boundaries

Source scope: PostgreSQL 18 SELECT, UPDATE and datetime behavior; SQLAlchemy 2.0 session transactions; Kubernetes Lease reference; Martin Kleppmann's original distributed-locking analysis. Source-backed platform facts must be distinguished from the proposed schema and worker policy. No claim here establishes any broker, PostgreSQL deployment, cloud scheduler or trading API as independently safe.

The SQL is *illustrative*, not standalone runnable infrastructure. It requires application-specific authorization, row schema, receipt and ledger integration, proper indexing, reliable migration/rollback, explicit timeout policy and real concurrency verification.

## Acceptance and negative tests for Final Expanse

| Failure injected | What application must establish |
| --- | --- |
| Two real worker processes claim one due bot | No duplicate accepted business effect |
| Worker A stalls, B reclaims with larger generation, A resumes | A cannot change bot/account ledger or overwrite B's committed result |
| Worker dies after DB commit, before response | Unique receipt replay; no extra fill |
| Worker loses DB access during heartbeat | Ownership becomes unknown; no unguarded financial writes |
| Bot is paused/config changed during evaluation | State/config rechecked before commit, old execution rejected |
| Provider request timed out | Unknown external outcome reconciled; not blindly repeated |

This research batch itself **does not execute** those application tests.

## Validation of Atlas changes

Run catalog, active-documentation, and full unittest checks, including golden retrieval queries:

~~~sh
python scripts/validate_catalog.py
python scripts/validate_documentation.py
python -m unittest discover -s tests -v
python scripts/search_catalog.py "durable-worker-leases-and-fencing" --json
python scripts/search_catalog.py "durable worker leases fencing" --json
~~~

Review actual GitHub Actions results before treating CI as green. Passing Atlas validation proves metadata/retrieval consistency, not a safe production bot.

## Handoff and next research

- **B15 + B16**: candidate PostgreSQL transaction and multi-worker coordination knowledge is now documented.
- **B17**: trusted exchange market-data provenance, candle freshness and eligibility remains the next planned research batch.
- **B18**: worker-health metrics, hosted OIDC/tenancy and frontend verification remain separate.
- **B19**: independent source-claim audit, retrieval relevance and campaign-wide integration remain open.

**Exit classification:** scoped researched material and proposed validation protocol delivered; Final Expanse's PostgreSQL multi-worker blocker remains unresolved until its own tests pass.
