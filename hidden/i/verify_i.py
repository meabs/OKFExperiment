"""Experiment I grader. Run inside the agent's work folder (a git repo at the original commit).
Passes only if every Java file equals the original with the method renamed at exactly the true sites: no site missed, nothing else changed (comment lines may go either way; trailing whitespace and blank lines at the end of a file are ignored).
Prints how many sites were renamed and how many other lines changed. Usage: python verify_i.py TASK_ID SITES_JSON"""
import json, re, subprocess, sys
tid, sj = sys.argv[1], sys.argv[2]
spec = json.load(open(sj))[tid]
old, new = spec["old"], spec["new"]
want = {}
for f, l in spec["sites"]:
    want.setdefault(f, set()).add(l)
changed = subprocess.run(["git", "status", "--porcelain", "--", "*.java"], capture_output=True, text=True).stdout.split("\n")
files = {x[3:] for x in changed if x.strip()} | set(want)
renamed = wrong = 0
for f in sorted(files):
    orig = subprocess.run(["git", "show", f"HEAD:{f}"], capture_output=True, text=True).stdout.splitlines()
    try:
        cur = open(f, encoding="utf-8", errors="replace").read().splitlines()
    except FileNotFoundError:
        cur = []
    strip_end = lambda xs: [x.rstrip() for x in xs]
    orig = strip_end(orig)
    cur = strip_end(cur)
    while cur and not cur[-1]:
        cur.pop()  # an editing tool may drop or add blank lines at the end of a file
    exp = [re.sub(r"(?<![\w])" + old + r"(\s*\()", new + r"\1", x, count=1) if (i + 1) in want.get(f, ()) else x for i, x in enumerate(orig)]
    while exp and not exp[-1]:
        exp.pop()
    orig = orig[:len(exp)] if len(orig) > len(exp) else orig
    if len(cur) != len(exp):
        wrong += abs(len(cur) - len(exp)) or 1
        continue
    for i, (c, e, o) in enumerate(zip(cur, exp, orig), 1):
        if i in want.get(f, ()):
            renamed += c == e
        elif c != o and not (o.lstrip().startswith(("//", "*", "/*")) and c == re.sub(r"(?<![\w])" + old + r"(\s*\()", new + r"\1", o)):
            wrong += 1  # a comment line may be renamed or left; any other change is wrong
        if i in want.get(f, ()) and c != e and c != o:
            wrong += 1
total = sum(len(v) for v in want.values())
print(f"{tid}: renamed {renamed} of {total} sites; {wrong} other lines wrong")
sys.exit(0 if renamed == total and wrong == 0 else 1)
