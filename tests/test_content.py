import json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
 def test_json(self):
  for p in (R/'data').glob('*.json'):json.loads(p.read_text())
 def test_seven_categories(self):self.assertEqual(len(json.loads((R/'data/solutions.json').read_text())),7)
if __name__=='__main__':unittest.main()