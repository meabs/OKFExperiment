"""Count runs whose commands used the network (experiment H allows it). Usage: python net_check.py RESULTS_FOLDER"""
import json, glob, collections, re, sys
d = sys.argv[1]
PAT = re.compile(r"\b(curl|wget|git\s+(clone|fetch|pull)|pip3?\s+install|npm\s+(i|install)|npx|gh\s+|nc\s)\b|https?://(?!localhost|127\.0\.0\.1|example\.invalid)", re.I)
tot, hit, ex = collections.Counter(), collections.Counter(), {}
for f in glob.glob(f"{d}/runs/*/*/codex/*/run.json"):
    r = json.load(open(f)); a = r["arm"]; tot[a] += 1
    for t in r["tool_calls"]:
        m = PAT.search(t["text"])
        if m:
            hit[a] += 1; ex.setdefault(a, t["text"][:140].replace("\n", " ")); break
for a in sorted(tot):
    print(f"{a:10} runs using the network: {hit[a]:>2}/{tot[a]}   e.g. {ex.get(a, '')}")
