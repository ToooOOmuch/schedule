"""Build the publishable page from the template and the plan data.

    python3 build.py            -> writes dist/weekly-plan.html
"""
import json
import pathlib

root = pathlib.Path(__file__).parent
tpl = (root / "src/page.tpl.html").read_text(encoding="utf-8")
data = json.loads((root / "src/plan-data.json").read_text(encoding="utf-8"))
raw = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
out = root / "dist/weekly-plan.html"
out.parent.mkdir(exist_ok=True)
out.write_text(tpl.replace("__DATA__", raw), encoding="utf-8")
print(f"wrote {out}")
