import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILES = (
    "site.json",
    "navigation.json",
    "solutions.json",
    "approach.json",
    "workcategories.json",
    "technology,json",
)

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path.relative_to(ROOT)} at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc

def main():
    loaded = {}
    for name in DATA_FILES:
        path = ROOT / "data" / name
        if not path.is_file():
            raise SystemExit(f"Required content file is missing: {path.relative_to(ROOT)}")
        value = load_json(path)
        if not isinstance(value, (dict, list)):
            raise SystemExit(f"Expected an object or array in {path.relative_to(ROOT)}")
        loaded[name] = value

    site = loaded["site.json"]
    for required in ("owner_name", "brand_name", "default_description"):
        if not isinstance(site.get(required), str) or not site[required].strip():
            raise SystemExit(f"data/site.json must contain a non-empty {required!r}")
    solutions = loaded["solutions.json"]
    if len(solutions) != 7 or len({item.get("slug") for item in solutions}) != 7:
        raise SystemExit("data/solutions.json must contain seven uniquely-slugged solution areas")
    for name in ("navigation.json", "solutions.json", "approach.json", "workcategories.json", "technology,json"):
        if not loaded[name]:
            raise SystemExit(f"Content array is empty: data/{name}")
    print("Content validation passed: six JSON datasets parsed, required content checked.")

if __name__ == "__main__":
    main()
