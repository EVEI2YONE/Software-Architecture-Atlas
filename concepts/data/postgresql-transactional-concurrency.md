---
id: postgresql-transactional-concurrency
title: "PostgreSQL transactional concurrency and SQLAlchemy"
category: data
status: reviewed
reviewed_at: 2026-11-07
---

# PostgreSQL transactional concurrency and SQLAlchemy

> **Scoped source-backed reference, not a verified Final Expanse implementation.** Examples below are illustrative, using PostgreSQL 18 and SQLAlchemy 2.0 documentation. No target database, tests or application schema have been executed for this Atlas page.

## Problem and scope

Concurrent API requests and background workers can read identical available capital and each attempt a debit. SQLite tests cannot prove PostgreSQL multi-connection or multi-process guarantees. This page specializes existing [transactions](transactions.md), [isolation levels](isolation-levels.md), and [transactional invariants](../domain-design/transactional-invariants.md). Cross-process leases, fencing and heartbeat belong to B16, not B15.

## Concurrency decision matrix

| Need | First candidate | Limitation / proof |
| --- | --- | --- |
| Protect existing balance row | SELECT FOR UPDATE with bounded transaction and storage constraints | Lock the exact tenant/account row; race-test concurrent debits |
| Claim due work | SELECT FOR UPDATE SKIP LOCKED in a short claim transaction | Skipped locks create an inconsistent view; suitable for queue-like work, not portfolio reads |
| Duplicate event / request | Unique tenant-scoped idempotency key and atomic effect/receipt | Distinguish same-key different-payload conflict and crash replay |
| Cross-row predicate | Explicit invariant owner/lock, constraints, or SERIALIZABLE isolation | Test write skew; SERIALIZABLE can abort and require full transaction retry |
| Avoid immediate lock waiting | NOWAIT, bounded lock timeout or application retry when justified | NOWAIT/SKIP LOCKED concern row locks and do not remove table-lock requirements |
| Financial effect plus external API | Keep local transaction short; explicitly design delivery boundary | Local commit cannot atomically commit an exchange or remote service side effect |

Prefer READ COMMITTED plus the narrowest tested constraints and row locks when sufficient. Do not apply SERIALIZABLE universally: conflicts and retry overhead are workload-specific [1, 2].

## SQLAlchemy 2.x illustration

The following example assumes the application has defined mapped CashBalance and InsufficientFunds objects. The caller supplies a short-lived Session; authorization, tenant identity, database constraints, currencies, decimal precision and receipt design are separate mandatory concerns.

~~~python
from decimal import Decimal
from sqlalchemy import select
from sqlalchemy.orm import Session

def reserve_cash(session: Session, account_id: str, amount: Decimal):
    if not amount.is_finite() or amount <= 0:
        raise ValueError("positive finite amount required")
    with session.begin():
        balance = session.execute(
            select(CashBalance)
            .where(CashBalance.account_id == account_id)
            .with_for_update()
        ).scalar_one()
        if balance.available < amount:
            raise InsufficientFunds()
        balance.available -= amount
        balance.reserved += amount
        # A real system must atomically persist a capital-reservation receipt.
~~~

SQLAlchemy's session.begin context provides transaction commit/rollback boundaries [3]. Do not share one Session across concurrent threads or asyncio tasks [4]. A nonexistent balance row must fail closed or be initialized under a separately verified uniqueness policy. The account ID must be derived from authenticated authorization, not blindly accepted from the caller.

### Queue-like row claim illustration

~~~sql
BEGIN;
SELECT id FROM paper_jobs
 WHERE status = 'due'
 ORDER BY due_at, id
 FOR UPDATE SKIP LOCKED
 LIMIT 1;
-- Update selected row ownership/status within this same transaction.
COMMIT;
~~~

This claims a database row temporarily. It is **not** a durable lease while doing long-running network work. Do not hold a row lock around exchange calls. B16 defines leases, fencing and stale-worker protection.

## Monetary and tenant invariants

- Exact monetary values: appropriate NUMERIC precision/scale and documented unit/currency; never binary-float balances.
- Capital changes and matching reservation or accounting receipt commit or roll back together.
- Nonnegative amounts, unique business receipt IDs and account ownership enforced at the correct database and API boundaries.
- Dedupe keys must be scoped correctly by tenant, bot and operation; prevent same key with conflicting payload silently replaying.
- No summing balances in differing currencies without a separate conversion model.
- Full-transaction retries must be bounded after deadlock or SQLSTATE 40001 serialization failure, and must not repeat unprotected remote effects [1].

## Real PostgreSQL verification plan — proposed, NOT RUN

Use disposable real PostgreSQL with separate connections, concurrent process barriers, the deployed isolation policy, and representative constraints. SQLite cannot substitute.

| Scenario | Fault/interleaving | Passing invariant |
| --- | --- | --- |
| Concurrent overspend | Two simultaneous debit transactions | At most affordable debits; no negative balance |
| Duplicate replay | Two simultaneous same-key requests, plus conflict payload | One committed effect and documented replay/conflict |
| Predicate write skew | Concurrent writes to different rows based on shared predicate | Cross-row business invariant preserved |
| Deadlock | Reverse lock order on two rows | Correct rollback and bounded operation retry |
| Serializable conflict | Force conflicting read/write dependencies | SQLSTATE 40001 retried only as whole safe transaction |
| Lock timeout | Hold row lock beyond defined deadline | No partial funds/receipts persisted |
| Crash before commit | Terminate after write, before commit | Transaction has no partial persisted effects |
| Crash after commit | Terminate before response/ack | Receipt replay prevents second effect |
| Parallel claims | Two workers claim same due-row pool | Unique ownership at commit; fairness caveats tracked |
| Cross-tenant access | Try known foreign account or bot IDs | Denied in API and data access paths |
| Pool saturation | API and workers compete for DB connections | Measured waits/timeouts and cleanup |

Record versions, isolation level, real transaction traces, lock waits, deadlocks, retry counts and actual test output. A sequential test or a metadata-valid catalog does not prove concurrent safety.

## Migration and rollback

First identify which financial invariant fails under concurrent interleaving. Prefer minimal constraints or locking over speculative rearchitecture. Rehearse production-like migration, lock waits, rollback and preservation of idempotency history; never erase already-committed financial receipts simply to undo a code change.

## Search aliases

postgresql concurrency; SQLAlchemy transaction; select for update; skip locked; serializable retry; row lock; database overspend; transactional capital reservation; SQLSTATE 40001

## Related concepts

- [Transactions](transactions.md)
- [Isolation levels](isolation-levels.md)
- [Data access boundaries](data-access-boundaries.md)
- [Transactional invariants](../domain-design/transactional-invariants.md)
- [Idempotency](../distributed-systems/idempotency.md)

## Evidence and sources

1. PostgreSQL 18, Transaction Isolation: https://www.postgresql.org/docs/18/transaction-iso.html (accessed 2026-11-07). Isolation semantics and serialization failures.
2. PostgreSQL 18, SELECT and locking: https://www.postgresql.org/docs/18/sql-select.html (accessed 2026-11-07). FOR UPDATE, SKIP LOCKED and NOWAIT.
3. SQLAlchemy 2.0, Session Transactions: https://docs.sqlalchemy.org/en/20/orm/session_transaction.html (accessed 2026-11-07). Transaction context.
4. SQLAlchemy 2.0, Session Basics: https://docs.sqlalchemy.org/en/20/orm/session_basics.html (accessed 2026-11-07). Session concurrency scope.
5. PostgreSQL 18, Explicit Locking: https://www.postgresql.org/docs/18/explicit-locking.html (accessed 2026-11-07). Lock waits and deadlocks.
6. PostgreSQL 18, Constraints: https://www.postgresql.org/docs/18/ddl-constraints.html (accessed 2026-11-07). Uniqueness and check constraints.

## Multi-process lease handoff

For short atomic claims that continue beyond the database transaction, use the distinct [Durable worker leases and fencing](../distributed-systems/durable-worker-leases-and-fencing.md) design. Holding or skipping PostgreSQL row locks is not an expiring worker lease or a guarantee of safe external side effects.

## Maintenance

Reviewed 2026-11-07. Check exact server, driver and SQLAlchemy versions; source-claim entailment and real application concurrency remain unverified.
