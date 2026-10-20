"""Regenerate sitemap.xml only when a production origin is configured."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
PAGES=['','solutions.php','work/','capabilities.php','technology.php','approach.php','about.php','contact.php','privacy.php','terms.php']
def main():
    config=json.loads((ROOT/'data/site.json').read_text(encoding='utf-8'))
    base=(config.get('production_url') or '').strip().rstrip('/')
    if not base.startswith('https://'):
        print('Production URL is not configured; writing a sitemap with no invented host.')
        content='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'
    else:
        urls=''.join(f'  <url><loc>{escape(base+("/" if not p else "/"+p))}</loc></url>\n' for p in PAGES)
        content='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(content,encoding='utf-8')
if __name__=='__main__':main()
