"""Experiment I: re-score the saved per-run diffs with sites inside commented-out code made optional.
The original site list counted two commented-out calls in i1 (ProductFacadeImpl 235, ProductFacadeV2Impl 245) as required; they are dead code.
Usage: python regrade_i.py RESULTS_FOLDER_OF_GRADES SITES_JSON"""
import glob, json, re, sys, os, collections
gdir, sj = sys.argv[1], sys.argv[2]
sites = json.load(open(sj))
DEAD = {"i1_rename_findOne": {("ProductFacadeImpl.java", 235), ("ProductFacadeV2Impl.java", 245)}}
rows = []
for f in sorted(glob.glob(f"{gdir}/*.txt")):
    txt = open(f).read().split("\n")
    m = re.match(r"(\w+): renamed (\d+) of (\d+) sites; (\d+) other", txt[0])
    tid, ren, tot, wrong = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
    changed = collections.defaultdict(set)
    cur = None
    for line in txt[1:]:
        if line.startswith("+++ b/"):
            cur = line[6:]
        h = re.match(r"@@ -(\d+)(?:,(\d+))? ", line)
        if h and cur:
            a, c = int(h.group(1)), int(h.group(2) if h.group(2) is not None else 1)
            changed[cur].update(range(a, a + c))
    real = [(fi, ln) for fi, ln in sites[tid]["sites"] if (os.path.basename(fi), ln) not in DEAD.get(tid, ())]
    missed_real = [s for s in real if s[1] not in changed.get(s[0], ())]
    arm = "guide" if "_guide_" in f else "plain"
    rows.append((arm, tid, ren == tot and wrong == 0, len(missed_real) == 0 and wrong == 0))
print("| Task | plain (original rule) | plain (dead code optional) | guide (original) | guide (dead code optional) |\n| --- | --- | --- | --- | --- |")
for t in sorted({r[1] for r in rows}):
    c = []
    for a in ("plain", "guide"):
        rs = [r for r in rows if r[0] == a and r[1] == t]
        c += [f"{sum(r[2] for r in rs)}/8", f"{sum(r[3] for r in rs)}/8"]
    print(f"| {t} | " + " | ".join(c) + " |")
for a in ("plain", "guide"):
    rs = [r for r in rows if r[0] == a]
    print(a, "original", sum(r[2] for r in rs), "of", len(rs), "; dead code optional", sum(r[3] for r in rs))
