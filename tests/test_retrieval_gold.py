"""Deterministic retrieval benchmark: indexed candidates, not answer correctness."""
import json
import unittest
from pathlib import Path
from scripts.search_catalog import search

FIXTURE = Path(__file__).parent / "fixtures" / "retrieval_gold.json"


class RetrievalGoldTests(unittest.TestCase):
    def test_gold_top_one_and_evidence_status(self):
        cases = json.loads(FIXTURE.read_text(encoding="utf-8"))["cases"]
        for case in cases:
            with self.subTest(query=case["query"]):
                result = search(case["query"])
                if case["expected_id"] is None:
                    self.assertEqual(result["results"], [])
                    continue
                self.assertTrue(result["results"])
                top = result["results"][0]
                self.assertEqual(top["id"], case["expected_id"])
                self.assertEqual(top["status"], case["expected_status"])
                if top["status"] == "stub":
                    self.assertEqual(top["evidence"], "unknown")
                else:
                    self.assertEqual(top["evidence"], "requires-source-inspection")

    def test_no_reviewed_guarantee_from_retrieval(self):
        hit = search("idempotency")["results"][0]
        self.assertNotEqual(hit["evidence"], "verified")
        self.assertIn("stub", search("project-structure-selection")["results"][0]["status"])


if __name__ == "__main__":
    unittest.main()
