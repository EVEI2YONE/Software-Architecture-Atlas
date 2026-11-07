---
id: threat-modeling
title: "Threat modeling and trust boundaries"
category: governance
status: reviewed
reviewed_at: 2026-11-07
---

# Threat modeling and trust boundaries

> **Reviewed — scoped source-backed guidance, not a target-application audit.**

## Applicability
OWASP recommends mapping actors, data flows, stores, trust boundaries and threats. NIST SSDF offers secure-development practices. A diagram or threat-model document does not establish that an application is secure.

## Decision framework
1. Inventory assets, actors, entry points, sensitive data, trust boundaries, runtime/deployment versions and external systems.
2. Sketch an actual flow, including APIs, background workers, queues, callbacks and administrative access.
3. Investigate spoofing, tampering, repudiation, disclosure, denial of service and elevation of privilege (STRIDE) where relevant; add business abuse cases.
4. For each material threat, record affected path, assumed mitigation, owner, negative test, residual risk and revisit trigger.

## Example and alternatives
Illustrative flow: browser -> API -> database. Threats include unauthorized reads and cross-tenant access. Candidate checks include subject/resource authorization, policy-denied tests, and revocation. For small systems a compact reviewed flow diagram may be more useful than a ceremonial risk register. Additional complexity is justified by observed risk.

## Verification and rollback
Trace each mitigation to real code/config, test negative paths and policy failures, and verify deployment. Do not promote untested claims as observed. Release control changes incrementally, monitor denials and provide controlled recovery from accidental lockout without reverting to permit-all.

## Search aliases
threat modeling; architecture contracts; data and security boundaries

## Related concepts
- [decision-records](../governance/decision-records.md)
- [supply-chain](../dependencies/supply-chain.md)

## Evidence and sources
1. OWASP Threat Modeling Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html (accessed 2026-11-07).
2. NIST SSDF SP 800-218 v1.1 final: https://csrc.nist.gov/pubs/sp/800/218/final (accessed 2026-11-07).

## Maintenance
Reviewed 2026-11-07. Revisit after standards/framework changes, incidents, new consumers or changed trust boundaries.
