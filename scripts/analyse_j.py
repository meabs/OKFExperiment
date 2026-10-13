"""Experiment J: pass counts per part and task, tokens, adoption of the optimised setup, isolation. Usage: python analyse_j.py RESULTS_FOLDER"""
import json, glob, re, sys, collections, statistics as st
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyse_h import fisher, NET
from regrade_j import j7_pass
d = sys.argv[1]
rows = []
for f in glob.glob(f"{d}/runs/*/*/codex/*/run.json"):
    r = json.load(open(f))
    raw = open(f.replace("run.json", "raw.out"), errors="replace").read()
    t = [x["text"] for x in r["tool_calls"]]
    r["pass"] = bool(r.get("verified") or r.get("correct"))
    if r["question"].startswith("j7"):  # the first j7 grader missed four pointcut strings; re-scored from the saved diff (see EXPERIMENT_J.md)
        r["pass"] = j7_pass(f"{d}/grades/{r['question']}_{r['arm']}_codex_{r['rep']}.txt")
    r["part"] = "changes" if r["question"][:2] in ("j1", "j2", "j3", "j7") else "questions"
    r["net"] = any(NET.search(x) for x in t)
    r["blocked"] = raw.count("Operation not permitted") > 0
    r["kg"] = any("bin/kg" in x for x in t)
    r["okf"] = any("okf/" in x for x in t)
    r["skill"] = sorted({m for x in t for m in re.findall(r"\.agents/skills/([\w-]+)/SKILL", x)})
    rows.append(r)
arms = ["plain", "optimised"]
def mean_tok(rs): return st.mean(r["tokens"]["total"] for r in rs)
for part in ("changes", "questions"):
    print(f"## {part}")
    by = {a: [r for r in rows if r["arm"] == a and r["part"] == part] for a in arms}
    pa, pb = (sum(r["pass"] for r in by[a]) for a in arms)
    na, nb = len(by["plain"]), len(by["optimised"])
    ta, tb = mean_tok(by["plain"]), mean_tok(by["optimised"])
    print(f"plain {pa}/{na} ({ta/1000:.0f}k tokens); optimised {pb}/{nb} ({tb/1000:.0f}k, {tb/ta:.2f} times); p = {fisher(pa, na, pb, nb):.3f}")
    print("| Task | plain | optimised | tokens plain | tokens optimised |\n| --- | --- | --- | --- | --- |")
    for t in sorted({r["question"] for r in rows if r["part"] == part}):
        c, k = [], []
        for a in arms:
            rs = [r for r in rows if r["question"] == t and r["arm"] == a]
            c.append(f"{sum(r['pass'] for r in rs)}/{len(rs)}"); k.append(f"{mean_tok(rs)/1000:.0f}k")
        print(f"| {t} | {c[0]} | {c[1]} | {k[0]} | {k[1]} |")
    print()
o = [r for r in rows if r["arm"] == "optimised"]
print(f"Adoption in the optimised arm ({len(o)} runs): ran kg {sum(r['kg'] for r in o)}; opened okf/ {sum(r['okf'] for r in o)}; read navigate {sum('navigate-the-repo' in r['skill'] for r in o)}, change {sum('change-the-code' in r['skill'] for r in o)}, check {sum('check-your-work' in r['skill'] for r in o)}; read no skill {sum(not r['skill'] for r in o)}")
for a in arms:
    rs = [r for r in rows if r["arm"] == a]
    print(f"{a}: network runs {sum(r['net'] for r in rs)}; runs with a refused access {sum(r['blocked'] for r in rs)}")
ok = [r for r in o if r["kg"]]; no = [r for r in o if not r["kg"]]
print(f"optimised runs that used kg: passed {sum(r['pass'] for r in ok)} of {len(ok)}; did not: {sum(r['pass'] for r in no)} of {len(no)}")
