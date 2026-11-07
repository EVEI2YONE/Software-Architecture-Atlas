"""B19 campaign contract checks: documentation consistency, not production tests."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "catalog/index.json"
REPORT = ROOT / "docs/batch-19-final-integration-validation.md"
CAMPAIGN = ROOT / "docs/final-expanse-blocker-campaign.md"

FOCUSED = {
    "postgresql-transactional-concurrency": "data",
    "durable-worker-leases-and-fencing": "distributed-systems",
    "trading-market-data-integrity": "data",
}
B18_EXISTING = (
    "concepts/operations/observability.md",
    "concepts/operations/reliability-objectives.md",
    "concepts/governance/identity-and-access.md",
    "concepts/dependencies/package-locking-and-version-policy.md",
    "concepts/quality/testing-strategy.md",
)


class CampaignIntegrityTests(unittest.TestCase):
    def test_focused_concepts_present_once_and_source_scoped(self):
        entries = json.loads(INDEX.read_text(encoding="utf-8"))["concepts"]
        for name, category in FOCUSED.items():
            with self.subTest(name=name):
                hits = [e for e in entries if e["id"] == name]
                self.assertEqual(len(hits), 1)
                self.assertEqual(hits[0]["category"], category)
                self.assertEqual(hits[0]["status"], "reviewed")
                self.assertGreater(hits[0]["source_count"], 0)
                self.assertTrue((ROOT / hits[0]["path"]).is_file())
                self.assertIn("not", (ROOT / hits[0]["path"]).read_text(encoding="utf-8").lower())

    def test_batch_reports_and_six_blockers_mapped(self):
        doc = REPORT.read_text(encoding="utf-8")
        for batch in range(15, 20):
            with self.subTest(batch=batch):
                self.assertIn(f"B{batch}", doc)
        for phrase in (
            "PostgreSQL multi-worker",
            "stale-worker fencing",
            "Background monitoring",
            "Hosted login",
            "Trusted Kraken",
            "React/Vite build",
            "NOT DONE",
            "source-supported",
            "inferred/proposed",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, doc)

    def test_lease_is_not_same_as_lock_or_business_key(self):
        report = REPORT.read_text(encoding="utf-8")
        for term in ("Short claim lock", "Lease", "Fencing generation", "Business idempotency key"):
            self.assertIn(term, report)
        self.assertIn("Does not cancel or stop the expired worker", report)

    def test_validation_is_not_product_certification(self):
        doc = REPORT.read_text(encoding="utf-8")
        self.assertIn("do **not** execute PostgreSQL", doc)
        self.assertIn("Application exit", doc)
        self.assertIn("still", doc.lower())

    def test_b18_reuses_existing_canonical_concepts(self):
        for path in B18_EXISTING:
            with self.subTest(path=path):
                self.assertIn(
                    "batch-18-production-verification.md",
                    (ROOT / path).read_text(encoding="utf-8"),
                )
        ids = {e["id"] for e in json.loads(INDEX.read_text(encoding="utf-8"))["concepts"]}
        self.assertTrue(set(FOCUSED).issubset(ids))

    def test_campaign_retains_all_five_batches(self):
        text = CAMPAIGN.read_text(encoding="utf-8")
        for number in range(15, 20):
            self.assertIn(f"| B{number} |", text)

    def test_kraken_errors_canonical_link(self):
        text = (ROOT / "concepts/data/trading-market-data-integrity.md").read_text(encoding="utf-8")
        self.assertIn("https://docs.kraken.com/exchange/guides/general/errors", text)
        self.assertNotIn("api/docs/guides/spot-errors/", text)


if __name__ == "__main__":
    unittest.main()
