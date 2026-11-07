"""B18 research wiring checks: documentation coverage, not target app verification."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

CONCEPTS = (
    "concepts/operations/observability.md",
    "concepts/operations/reliability-objectives.md",
    "concepts/governance/identity-and-access.md",
    "concepts/dependencies/package-locking-and-version-policy.md",
    "concepts/quality/testing-strategy.md",
)

class B18ReferenceTests(unittest.TestCase):
    def test_runbook_covers_each_blocker(self):
        guide = (ROOT / "docs/batch-18-production-verification.md").read_text(encoding="utf-8")
        for expected in (
            "## 1. Durable worker monitoring",
            "## 2. Hosted OIDC authentication",
            "## 3. React/Vite reproducible build",
            "B16",
            "B17",
            "RFC 10017",
            "npm ci",
            "Playwright",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, guide)

    def test_existing_canonical_concepts_link_to_guide(self):
        for path in CONCEPTS:
            with self.subTest(path=path):
                content = (ROOT / path).read_text(encoding="utf-8")
                self.assertIn("batch-18-production-verification.md", content)
                self.assertIn("## B18:", content)

    def test_no_claims_of_executed_target_verification(self):
        guide = (ROOT / "docs/batch-18-production-verification.md").read_text(encoding="utf-8")
        self.assertIn("no target-system deployment", guide)
        self.assertIn("NOT RUN", guide)
        self.assertIn("does not", guide.lower())

if __name__ == "__main__":
    unittest.main()
