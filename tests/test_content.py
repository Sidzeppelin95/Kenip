import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ContentTests(unittest.TestCase):
    def test_every_declared_dataset_parses(self):
        names = ("site.json", "navigation.json", "solutions.json", "approach.json", "workcategories.json", "technology,json")
        for name in names:
            with self.subTest(name=name):
                with (ROOT / "data" / name).open(encoding="utf-8") as handle:
                    self.assertIsInstance(json.load(handle), (dict, list))

    def test_solution_slugs_are_unique(self):
        items = json.loads((ROOT / "data" / "solutions.json").read_text(encoding="utf-8"))
        self.assertEqual(len(items), 7)
        self.assertEqual(len({item["slug"] for item in items}), 7)

if __name__ == "__main__":
    unittest.main()
