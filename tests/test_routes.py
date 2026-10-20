import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RouteTests(unittest.TestCase):
 def test_all_expected_pages_exist(self):
  for path in ['index.php','solutions.php','work/index.php','work/category.php','capabilities.php','technology.php','approach.php','about.php','contact.php','privacy.php','terms.php','404.php']:
   with self.subTest(path=path):self.assertTrue((ROOT/path).is_file())
 def test_shared_header_and_footer_are_included(self):
  for path in ['index.php','solutions.php','capabilities.php','technology.php','approach.php','about.php','contact.php','privacy.php','terms.php','work/index.php']:
   source=(ROOT/path).read_text(encoding='utf-8');self.assertIn('includes/header.php',source,path);self.assertIn('includes/footer.php',source,path)
if __name__=='__main__':unittest.main()
