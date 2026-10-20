from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];P=['index.php','solutions.php','work/index.php','capabilities.php','technology.php','approach.php','about.php','contact.php','privacy.php','terms.php']
def main():
 c=json.loads((R/'data/site.json').read_text());u=(c.get('production_url') or '').rstrip('/')
 if not u.startswith('https://'):print('Set verified HTTPS production_url first.');return 2
 ns='http://www.sitemaps.org/schemas/sitemap/0.9';ET.register_namespace('',ns);root=ET.Element(f'{{{ns}}}urlset')
 for p in P:ET.SubElement(ET.SubElement(root,f'{{{ns}}}url'),f'{{{ns}}}loc').text=u+'/'+p
 ET.indent(root,space='  ');(R/'sitemap.xml').write_bytes(ET.tostring(root,encoding='utf-8',xml_declaration=True)+b'\n');return 0
if __name__=='__main__':raise SystemExit(main())