"""Experiment H: pass counts, tokens and pairwise tests per arm. Usage: python analyse_h.py RESULTS_FOLDER [--markdown]

A run passes when its hidden test passed (`verified`) or, for questions, when every expected term is in the answer (`correct`).
Pairs are compared with a two-sided Fisher exact test; only p < 0.05 is called a difference (see docs/EXPERIMENT_H.md).
Runs that used the network are counted, and the table is repeated without them."""
import json, glob, re, sys, collections, statistics as st
from math import comb

ARMS = ["none", "contract", "notes", "okf", "source"]
PAIRS = [("contract", "okf"), ("notes", "okf"), ("okf", "source"), ("contract", "notes"), ("none", "contract"), ("none", "okf")]
NET = re.compile(r"\b(curl|wget|git\s+(clone|fetch|pull)|pip3?\s+install|npm\s+(i|install)|npx|gh\s+)\b|https?://(?!localhost|127\.0\.0\.1|example\.invalid)", re.I)


def fisher(a, n1, b, n2):
    """two-sided Fisher exact p for a/n1 against b/n2 successes"""
    k, n = a + b, n1 + n2
    lo, hi = max(0, k - n2), min(k, n1)
    p = lambda x: comb(n1, x) * comb(n2, k - x) / comb(n, k)
    obs = p(a)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs * (1 + 1e-9)))


def load(d):
    rows = []
    for f in glob.glob(f"{d}/runs/*/*/codex/*/run.json"):
        r = json.load(open(f))
        r["pass"] = bool(r.get("verified") or r.get("correct"))
        r["net"] = any(NET.search(t["text"]) for t in r["tool_calls"])
        rows.append(r)
    return rows


def table(rows, title):
    by = collections.defaultdict(list)
    for r in rows:
        by[r["arm"]].append(r)
    base = st.mean(r["tokens"]["total"] for r in by["none"]) if by["none"] else None
    out = [f"**{title}**", "", "| Arm | Passed | Tokens per run | Against `none` |", "| --- | --- | --- | --- |"]
    for a in ARMS:
        rs = by.get(a, [])
        if not rs:
            continue
        m = st.mean(r["tokens"]["total"] for r in rs)
        out.append(f"| `{a}` | {sum(r['pass'] for r in rs)} of {len(rs)} | {m / 1000:.0f}k | {m / base:.2f} |" if base else f"| `{a}` | {sum(r['pass'] for r in rs)} of {len(rs)} | {m / 1000:.0f}k | |")
    out += ["", "Pairs (two-sided Fisher exact):", ""]
    for a, b in PAIRS:
        ra, rb = by.get(a, []), by.get(b, [])
        if ra and rb:
            pa, pb = sum(r["pass"] for r in ra), sum(r["pass"] for r in rb)
            p = fisher(pa, len(ra), pb, len(rb))
            out.append(f"- `{a}` {pa}/{len(ra)} against `{b}` {pb}/{len(rb)}: p = {p:.3f}{' (reliable)' if p < 0.05 else ''}")
    return "\n".join(out)


def touched(r, pat):
    """a run outside the `source` arm that opened the dependency's files, the hidden tests or another arm's material"""
    return r["arm"] != "source" and any(re.search(pat, t["text"]) for t in r["tool_calls"])


if __name__ == "__main__":
    d = sys.argv[1]
    rows = load(d)
    if "--exclude" in sys.argv:
        pat = sys.argv[sys.argv.index("--exclude") + 1]
        bad = [r for r in rows if touched(r, pat)]
        print(f"{len(bad)} of {len(rows)} runs touched paths matching /{pat}/ " + str(dict(collections.Counter(r["arm"] for r in bad))) + "; kept the rest\n")
        rows = [r for r in rows if not touched(r, pat)]
    print(table(rows, f"All {len(rows)} runs"))
    print()
    tasks = sorted({r["question"] for r in rows})
    print("Per task (passed of runs):\n")
    print("| Task | " + " | ".join(f"`{a}`" for a in ARMS) + " |\n| --- |" + " --- |" * len(ARMS))
    for t in tasks:
        cells = []
        for a in ARMS:
            rs = [r for r in rows if r["question"] == t and r["arm"] == a]
            cells.append(f"{sum(r['pass'] for r in rs)}/{len(rs)}" if rs else "-")
        print(f"| {t} | " + " | ".join(cells) + " |")
    net = [r for r in rows if r["net"]]
    print(f"\nRuns that used the network: {len(net)} of {len(rows)} " + str(dict(collections.Counter(r["arm"] for r in net))))
    if net:
        print()
        print(table([r for r in rows if not r["net"]], f"Without the {len(net)} network runs"))
