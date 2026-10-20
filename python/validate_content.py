"""Validate JSON structure and required content completeness."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED={'site.json','navigation.json','solutions.json','work-categories.json','capabilities.json','technology.json','approach.json'}
def main():
    data=ROOT/'data';missing=REQUIRED-{p.name for p in data.glob('*.json')}
    if missing:raise SystemExit(f'Missing required JSON files: {sorted(missing)}')
    decoded={}
    for name in sorted(REQUIRED):
        path=data/name;raw=path.read_text(encoding='utf-8')
        if not raw.strip():raise SystemExit(f'{path.relative_to(ROOT)} is empty; provide valid JSON. Empty optional values must be JSON null, not blank text.')
        try:decoded[name]=json.loads(raw)
        except json.JSONDecodeError as exc:raise SystemExit(f'{path.relative_to(ROOT)}:{exc.lineno}:{exc.colno}: {exc.msg}') from exc
    if not isinstance(decoded['site.json'],dict):raise SystemExit('site.json must be an object')
    categories=decoded['work-categories.json']
    if not isinstance(categories,list) or len(categories)!=7:raise SystemExit('work-categories.json must contain exactly seven categories')
    slugs=[c.get('slug') for c in categories]
    if len(set(slugs))!=7 or not all(isinstance(s,str) and s for s in slugs):raise SystemExit('Category slugs must be unique non-empty strings')
    for c in categories:
        for key in ('title','summary','overview','problems','capabilities','technology_domains','engagements'):
            if not c.get(key):raise SystemExit(f'Category {c.get("slug")} has missing or empty {key}')
    if len(decoded['approach.json'])!=5:raise SystemExit('approach.json must contain five stages')
    if decoded['site.json'].get('contact_form_enabled') is not False:raise SystemExit('Contact form must remain disabled')
    print(f'Validated {len(REQUIRED)} JSON files, {len(categories)} categories, and {len(decoded["approach.json"])} approach stages.')
if __name__=='__main__':main()
