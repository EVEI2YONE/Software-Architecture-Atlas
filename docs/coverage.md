# Current architecture catalog coverage

**Canonical inventory (2026-11-07): 93 indexed concepts, 93 with status `reviewed`, 0 stubs.** These are metadata statuses, not independently certified architectural claims. This table is a current snapshot derived from [the canonical index](../catalog/index.json); update it when that index changes.

| Category | Indexed concepts |
| --- | ---: |
| [principles](../concepts/principles/README.md) | 7 |
| [domain-design](../concepts/domain-design/README.md) | 8 |
| [code-organization](../concepts/code-organization/README.md) | 22 |
| [dependencies](../concepts/dependencies/README.md) | 6 |
| [runtime](../concepts/runtime/README.md) | 9 |
| [distributed-systems](../concepts/distributed-systems/README.md) | 10 |
| [data](../concepts/data/README.md) | 5 |
| [performance](../concepts/performance/README.md) | 7 |
| [quality](../concepts/quality/README.md) | 6 |
| [operations](../concepts/operations/README.md) | 5 |
| [governance](../concepts/governance/README.md) | 8 |
| **Total** | **93** |

## Interpreting coverage

- `reviewed` means the page has scoped references and curation metadata; it does **not** mean its claims were independently validated against primary sources or any target application.
- Metadata validation, retrieval benchmarks and passing CI are different from technical accuracy audits, performance tests, vulnerability scans or Sonar quality-gate results.
- Remaining work is primarily independent claim/source review, version freshness, real-workload validation and retrieval relevance, not an indexed-stub backlog. See [active research gaps](../research/open-gaps.md).
- Historical inventories, batch counts and campaign reports are retained under [research/archive](../research/README.md). Do not use historical batch totals as current catalog counts.
