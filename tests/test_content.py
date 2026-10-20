import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ContentTests(unittest.TestCase):
 def test_all_required_json_parses(self):
  for name in ['site.json','navigation.json','solutions.json','work-categories.json','capabilities.json','technology.json','approach.json']:
   with self.subTest(name=name):self.assertTrue(json.loads((ROOT/'data'/name).read_text(encoding='utf-8')))
 def test_seven_complete_categories(self):
  items=json.loads((ROOT/'data/work-categories.json').read_text(encoding='utf-8'));self.assertEqual(len(items),7);self.assertEqual(len({x['slug'] for x in items}),7)
  for item in items:
   for field in ['title','summary','overview','problems','capabilities','technology_domains','engagements']:self.assertTrue(item[field],(item['slug'],field))
 def test_no_form_enabled(self):self.assertIs(json.loads((ROOT/'data/site.json').read_text())['contact_form_enabled'],False)
if __name__=='__main__':unittest.main()
