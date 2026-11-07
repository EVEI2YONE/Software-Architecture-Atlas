---
id: idempotency
title: "Idempotency and retries"
category: distributed-systems
status: reviewed
reviewed_at: 2026-11-07
---

# Idempotency and retries

> **Reviewed — protocol and API-design scope only.** An HTTP method's semantics are not a guarantee that application effects are deduplicated.

## Problem
After a timeout or lost response, callers may not know whether an operation committed. RFC 9110 defines idempotent HTTP methods by the intended server effect of repeating the *same* request; clients should not automatically retry non-idempotent methods without additional assurances [1].

## Decision questions
- Is the operation safe, HTTP-idempotent or **business-effect** idempotent? Distinguish them.
- Is the request identified by a stable client key, and what does that key mean per user/tenant and payload?
- What is the concurrent duplicate policy, retention window, result replay and cleanup?
- Are message acknowledgments, database commit and external side effects coordinated?

## Example (illustrative)
For POST /orders, a unique request key scoped to an actor could identify a previously completed result. A storage uniqueness constraint and atomic write may help prevent duplicate order records; downstream payments or emitted events still need separate design. This is a design candidate, not a universal algorithm or exactly-once guarantee.

## Verification and alternatives
Try repeated identical requests, conflicting payload with same key, concurrent duplicates, crash between commit/response, timeout, retries after retention expiry, and duplicate message delivery. If operation is purely replace-state PUT and conforms to RFC semantics, a separate idempotency-key layer may be unnecessary. Do not introduce retries that amplify overload.

## Migration and rollback
Stage deduplication behind visibility metrics, ensure key collision behavior and backwards compatibility; rollback must avoid losing deduplication history during retry windows.

## Search aliases
duplicate request; retry safety; idempotent POST; exactly once; deduplication

## Related concepts
- [transactions](../data/transactions.md)
- [event-driven](event-driven.md)
- [API contracts](api-contracts.md)

## Evidence and sources
1. IETF RFC 9110, *HTTP Semantics*, Section 9.2.2: https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2 (accessed 2026-11-07).
2. PostgreSQL 18 Documentation, *Transaction Isolation*: https://www.postgresql.org/docs/18/transaction-iso.html (accessed 2026-11-07). Database concurrency constraints are separate from HTTP semantics.

## Maintenance
Reviewed 2026-11-07; revisit for service delivery contracts, storage lifetime and API behavior changes.
