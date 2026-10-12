"""Experiment I: pass counts, tokens, pairwise test, isolation and network use. Usage: python analyse_i.py RESULTS_FOLDER"""
import json, glob, re, sys, collections, statistics as st
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyse_h import fisher, NET
d = sys.argv[1]
rows = []
for f in glob.glob(f"{d}/runs/*/*/codex/*/run.json"):
    r = json.load(open(f))
    raw = open(f.replace("run.json", "raw.out"), errors="replace").read()
    r["pass"] = bool(r.get("verified"))
    r["net"] = any(NET.search(t["text"]) for t in r["tool_calls"])
    r["blocked"] = raw.count("Operation not permitted")
    r["outside"] = any(re.search(r"/Users/garry/code|/private/tmp|/tmp/", t["text"]) for t in r["tool_calls"])
    rows.append(r)
arms = ["plain", "guide"]
by = {a: [r for r in rows if r["arm"] == a] for a in arms}
for a in arms:
    rs = by[a]
    print(f"{a}: passed {sum(r['pass'] for r in rs)} of {len(rs)}; tokens {st.mean(r['tokens']['total'] for r in rs)/1000:.0f}k; network runs {sum(r['net'] for r in rs)}; "
          f"runs naming a path outside the workspace {sum(r['outside'] for r in rs)}; runs with a blocked access {sum(r['blocked'] > 0 for r in rs)}")
pa, pb = (sum(r["pass"] for r in by[a]) for a in arms)
print(f"overall plain {pa}/32 against guide {pb}/32: p = {fisher(pa, 32, pb, 32):.3f}")
print("\n| Task | plain | guide |\n| --- | --- | --- |")
for t in sorted({r["question"] for r in rows}):
    c = [f"{sum(r['pass'] for r in by[a] if r['question'] == t)}/8" for a in arms]
    print(f"| {t} | {c[0]} | {c[1]} |")
