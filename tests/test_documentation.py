"""Documentation consistency regression checks."""
import json
import tempfile
import unittest
from pathlib import Path
from scripts.validate_documentation import validate

class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "catalog").mkdir()
        (self.root / "docs").mkdir()
        (self.root / "concepts/principles").mkdir(parents=True)
        (self.root / "catalog/index.json").write_text(json.dumps({"concepts":[{"id":"one","category":"principles"}]}))
        (self.root / "docs/coverage.md").write_text("1 indexed concepts\n| [principles](../concepts/principles/README.md) | 1 |\n")
        (self.root / "concepts/principles/README.md").write_text("# Principles\n[One](one.md)\n")
        (self.root / "concepts/principles/one.md").write_text("# One\n")
    def test_valid(self):
        self.assertEqual(validate(self.root), [])
    def test_bad_count(self):
        p = self.root / "docs/coverage.md"
        p.write_text(p.read_text().replace("| 1 |", "| 2 |"))
        self.assertTrue(any("coverage count" in e for e in validate(self.root)))
    def test_missing_category_item(self):
        (self.root / "concepts/principles/README.md").write_text("# Principles\n")
        self.assertTrue(any("README index mismatch" in e for e in validate(self.root)))
    def test_broken_active_link(self):
        (self.root / "docs/coverage.md").write_text((self.root / "docs/coverage.md").read_text()+"\n[missing](missing.md)")
        self.assertTrue(any("broken local link" in e for e in validate(self.root)))
