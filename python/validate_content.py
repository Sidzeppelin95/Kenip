import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def main():
 for p in (R/'data').glob('*.json'):json.loads(p.read_text(encoding='utf-8'))
 c=json.loads((R/'data/solutions.json').read_text());assert len(c)==7 and len({x['slug'] for x in c})==7
 print('Content validation passed.')
if __name__=='__main__':main()