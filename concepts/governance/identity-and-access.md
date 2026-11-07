---
id: identity-and-access
title: "Identity, authorization and secrets lifecycle"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Identity, authorization and secrets lifecycle

> **Reviewed — scoped source-backed guidance, not a target-application audit.**

## Applicability
Authentication establishes identity; authorization evaluates allowed subject-resource-action operations. OWASP recommends least privilege and deny by default. Secret and service credentials require access controls, rotation and revocation; no one identity provider is prescribed.

## Questions
- Who is acting (user, service, queue-triggered Function, WebJob, administrator), on which resource, in which tenant?
- Is authorization enforced on the backend, including object-level and cross-tenant access?
- What happens with missing/revoked credentials, stale policy and policy-engine failures?
- Can deployment identities alter schema while normal service identities cannot? Who owns rotation and incident response?

## Alternatives and counterexamples
Small services may use a simple auditable access matrix rather than a general-purpose policy engine; that still requires backend enforcement. UI-only hiding and shared privileged credentials do not create strong boundaries.

## Verification and rollback
Test denied, permitted, cross-tenant, stale/revoked and error paths; inspect actual credential storage and rotation and audit records. Stage controls with monitoring and controlled access recovery, not a permit-all rollback. No security certification is implied.

## Search aliases
identity and access; architecture contracts; data and security boundaries

## Related concepts
- [threat-modeling](../governance/threat-modeling.md)
- [supply-chain](../dependencies/supply-chain.md)
- [decision-records](../governance/decision-records.md)

## Evidence and sources
1. OWASP Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html (accessed 2026-11-07).
2. OWASP Threat Modeling Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html (accessed 2026-11-07).
3. NIST SSDF SP 800-218 v1.1 final: https://csrc.nist.gov/pubs/sp/800/218/final (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit after standards/framework changes, incidents, new consumers or changed trust boundaries.
