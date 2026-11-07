---
id: durable-worker-leases-and-fencing
title: "Durable worker leases, fencing and restart recovery"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Durable worker leases, fencing and restart recovery

> **Reviewed, scope-limited architectural pattern, not a tested distributed system.** The PostgreSQL 18 statements and cited source behavior are reference evidence; the proposed state machine, SQL sketches, timeout choices and failure matrix are design proposals requiring independent validation on an actual application. This page does not claim exactly-once delivery or prevent all external side effects.

## Problem, ownership and boundaries

Several processes can poll the same due job. Worker A acquires a lease, pauses longer than its lease duration, worker B reclaims the job and processes it, and A resumes. **Lease expiry makes recovery possible; it does not revoke A's process or network requests.** A successful claim, an active lease, an accepted database effect, and an external exchange request are different safety boundaries.

This concept specializes [idempotency](idempotency.md), [queues](queues.md), [delivery guarantees](delivery-guarantees.md), and [PostgreSQL concurrency](../data/postgresql-transactional-concurrency.md), without replacing their contracts. B16 owns coordination and crash recovery; B15 owns local transaction invariants; B18 will cover deployed observability and alert delivery.

## Smallest justified coordination design

| Situation | First candidate | Trade-off / missing guarantee |
| --- | --- | --- |
| One disposable process, no durable job state | In-process scheduling, cancellation and local lock | Loses in-flight work on crash; insufficient for unattended financial automation |
| Several processes sharing one PostgreSQL database | Durable job row, short atomic conditional claim, lease expiry, generation token, bounded retry | Requires DB health, schema invariants, real concurrency tests and fencing at every persistent effect |
| High-throughput asynchronous consumers | Evaluate a durable broker with ack/visibility/locking rules | Broker message lock does not fence the consumer's database or remote side effects |
| External provider operation | Provider-native request idempotency and reconciliation, or fail closed until outcome is known | Neither lease nor local DB transaction atomically commits provider effects |

Do not hold a PostgreSQL row lock while awaiting a market-data provider, model API or exchange call. Use a short claim transaction followed by a bounded, separately owned attempt.

## Proposed durable state machine

~~~text
DUE -> CLAIMED(token=N, owner=W, expires_at)
CLAIMED -> SUCCEEDED       (guarded commit, receipt)
CLAIMED -> RETRY_DUE       (bounded retry with next_due_at)
CLAIMED -> HALTED          (terminal or operator-halted)
CLAIMED -> DUE             (lease expired, next claimer increments token)
CLAIMED -> CLAIMED        (renew only matching owner AND token, before expiry)
~~~

A paused/stopped bot must fail eligibility checks **again at execution/commit**, not only when picked up. Separate a job's business idempotency identity (e.g. bot/configuration/candle version) from the lease generation: each retry may have a *different* generation but must not create an extra fill.

### Schema sketch (illustrative)

~~~sql
CREATE TABLE worker_jobs (
    job_id bigint PRIMARY KEY,
    tenant_id bigint NOT NULL,
    bot_id bigint NOT NULL,
    state text NOT NULL CHECK (state IN ('due','claimed','retry_due','succeeded','halted')),
    next_due_at timestamptz NOT NULL,
    lease_owner text,
    lease_expires_at timestamptz,
    lease_generation bigint NOT NULL DEFAULT 0 CHECK (lease_generation >= 0),
    attempts integer NOT NULL DEFAULT 0 CHECK (attempts >= 0),
    last_failure_code text
);
-- Real implementation requires indexes, tenancy FK/unique constraints,
-- configuration/version binding, allowed transition enforcement and receipts.
~~~

### Atomic claim and increment — illustrative PostgreSQL pattern

~~~sql
-- One short transaction; bind :worker_id and use a bounded candidate set.
WITH candidate AS (
    SELECT job_id FROM worker_jobs
    WHERE (state IN ('due','retry_due') AND next_due_at <= clock_timestamp())
       OR (state = 'claimed' AND lease_expires_at < clock_timestamp())
    ORDER BY next_due_at, job_id
    FOR UPDATE SKIP LOCKED
    LIMIT 1
)
UPDATE worker_jobs AS j
SET state = 'claimed',
    lease_owner = :worker_id,
    lease_expires_at = clock_timestamp() + interval '30 seconds',
    lease_generation = j.lease_generation + 1
FROM candidate
WHERE j.job_id = candidate.job_id
RETURNING j.job_id, j.lease_generation, j.lease_expires_at;
~~~

The 30-second value is **illustrative, not a recommendation**. Define lease duration, polling, heartbeat and worker deadline from measured workloads. PostgreSQL's clock_timestamp() is wall-clock evaluation time; transaction_timestamp()/CURRENT_TIMESTAMP is fixed at transaction start [3]. Database-side time can reduce differences between client clocks, but wall-clock shifts and DB availability still require investigation. The two clock_timestamp() calls are not one guaranteed atomic timestamp; capture a consistent value where boundary equality matters.

### Renewal and guarded effects

~~~sql
-- Renewal: require the same owner, generation and still-valid lease.
UPDATE worker_jobs
SET lease_expires_at = clock_timestamp() + interval '30 seconds'
WHERE job_id = :job_id
  AND state = 'claimed'
  AND lease_owner = :worker_id
  AND lease_generation = :generation
  AND lease_expires_at > clock_timestamp()
RETURNING job_id;

-- Guarded completion in one DB transaction, with same identity and lease check:
UPDATE worker_jobs
SET state = 'succeeded', lease_owner = NULL, lease_expires_at = NULL
WHERE job_id = :job_id
  AND state = 'claimed'
  AND lease_owner = :worker_id
  AND lease_generation = :generation
  AND lease_expires_at > clock_timestamp()
RETURNING job_id;
-- Only after verifying exactly one row was returned, append the unique
-- business receipt and associated local ledger effects in the SAME transaction.
-- On any failure, ROLLBACK the entire unit, including the state transition.
~~~

**Critical:** A guarded completion row alone is insufficient if the side effect was already written separately. Every durable local effect (capital reservation, fill, ledger, receipt) must share the guarded transaction, or be guarded at its own authoritative resource boundary. A stale generation must not reach an unguarded write path. The schema sketch intentionally omits application-specific receipt tables.

## Fencing token versus a lease check

A worker can be paused after its last lease check and later write after another worker takes ownership. This is the stale-worker problem described by Kleppmann [4]. A monotonically increasing lease generation is useful only if the **authoritative side-effect consumer** compares it with current ownership or the highest accepted generation. Simply storing a token or checking it once before a long-running call is not fencing.

- For the same PostgreSQL database: use conditional updates with the current generation and a single atomic commit of business effects; include unique business-effect receipts.
- For independent storage/resources: they must reject stale-generation operations, or the design must use another proven serialization mechanism.
- For a remote API lacking fencing: a local lease provides no proof that an expired worker's request will be rejected. Use documented provider idempotency, reconciliation and explicit unknown-outcome handling before enabling consequential external actions.

Generation values must not be reset/reused within the job's fencing domain. Renewal keeps the **same** generation; every new acquisition increments it. Keep a clear policy for job deletion/recreation and token range/overflow.

## Retry, expiry, pause and cancellation rules

1. Claim only work eligible for processing; commit the claim before performing network I/O.
2. Bound attempts, call duration, heartbeat/renewal intervals and total retry time; use backoff with jitter to avoid synchronized retries (a proposal, not a universal formula).
3. Distinguish transient, deterministic permanent, authorization, missing market data and ambiguous committed-result failures. Permanent or unknown-external outcomes must **not** be blindly retried.
4. On process stop: stop new claims, request cooperative cancellation, finish/rollback short transactions, and let expired leases be reclaimed if necessary. A process kill has no cleanup guarantee.
5. On pause/stop of a bot: fence the pending evaluation against its configuration revision and state before accepting any local fill; cancellation alone cannot undo committed effects.
6. Reclaimed jobs may be retried; always look up a durable business receipt before performing new effects. Never assert exactly-once delivery based only on job locking.

## Failure-injection matrix (proposed; NOT EXECUTED)

| Fault/interleaving | Expected behavior / assertion |
| --- | --- |
| Two claimers race for one job | One active claim generation returned; no duplicate accepted effect |
| Worker A stalls past expiry; B reclaims; A resumes | B generation increases; all A's local effects rejected |
| A pauses just before durable completion | Lease guarded commit or rollback; no orphaned partial financial writes |
| A commits effect but dies before acknowledgment | B reads business receipt and replays outcome without second effect |
| Heartbeat after expiry or with old generation | Renewal affects zero rows; A must stop acting |
| Database unavailable at renewal | Worker treats ownership as unknown, does not proceed with unguarded writes |
| Bot paused or config changed between claim and commit | Running/config revision revalidated; no obsolete fill accepted |
| Duplicate job business key with different parameters | Conflict rejected or versioned per documented dedupe policy |
| Clock advance/rollback around expiry boundary | Defined behavior using DB time; no stale generation accepted |
| Retry storm, poison job, invalid market data | Bounded retry/backoff, actionable terminal status, no infinite hot loop |
| Process killed during query/cancellation | Transaction rollback/connection cleanup; replay safe |
| Lease owner identity reused, job recreated | Generation/identity uniqueness preserved; stale actor cannot write |
| Multi-tenant known ID probe | Worker and status API enforce tenant authorization |
| External provider times out after request | Status UNKNOWN until reconciliation; no blind repeat of side effect |

Run scenarios against **real PostgreSQL with two or more independent processes and database connections**, deterministic barriers/fault injection, and real persistence. SQLite tests or single-process mocks do not prove cross-process lease/fencing safety. Capture worker IDs, generations, retry state, timing, committed receipt count and balances; redact tenant details in telemetry.

## Observability and recovery handoff

At minimum expose actionable job age, oldest-due age, active/expired lease counts, claim conflicts, renewal failures, retries, terminal failures, and last successful evaluation. Alert policies and operational readiness are B18 topics; do not infer deployed worker health from these fields alone.

## Search aliases

distributed lease; worker fencing token; stale worker; split brain job; lease generation; heartbeat renewal; worker crash recovery; zombie worker; exactly once job; postgres multi process schedule; retry safety

## Related concepts

- [Idempotency](idempotency.md)
- [Queues](queues.md)
- [Delivery guarantees](delivery-guarantees.md)
- [PostgreSQL transactional concurrency](../data/postgresql-transactional-concurrency.md)
- [Lock contention](../runtime/lock-contention-and-deadlocks.md)
- [Reliability objectives](../operations/reliability-objectives.md)

## Evidence and sources

1. PostgreSQL 18 Documentation, SELECT and SKIP LOCKED: https://www.postgresql.org/docs/18/sql-select.html (accessed 2026-11-07). Short claim and lock semantics.
2. PostgreSQL 18 Documentation, UPDATE with WHERE and RETURNING: https://www.postgresql.org/docs/18/sql-update.html (accessed 2026-11-07). Conditional updates and result identity.
3. PostgreSQL 18 Documentation, Date/Time Functions: https://www.postgresql.org/docs/18/functions-datetime.html (accessed 2026-11-07). Database timestamp and clock_timestamp behavior.
4. Martin Kleppmann, How to do distributed locking (original technical analysis): https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html (accessed 2026-11-07). Expired lease and stale-worker fencing argument.
5. Kubernetes Documentation, Leases: https://kubernetes.io/docs/concepts/architecture/leases/ (accessed 2026-11-07). Example of lease/heartbeat and leader-election coordination; Kubernetes Lease is **not** used in the proposed PostgreSQL pattern.
6. SQLAlchemy 2.0 Documentation, Session Transactions: https://docs.sqlalchemy.org/en/20/orm/session_transaction.html (accessed 2026-11-07). Application transaction ownership; not cross-process lease certification.

## Maintenance

Reviewed 2026-11-07. Reassess for deployed database versions, actual scheduling topology, partner idempotency contracts, recovery drills, measurements and new evidence. Do not interpret this as a working financial trading scheduler.
