"""Experiment J: re-score the j7 runs from their saved diffs with the four AspectJ pointcut strings in PublishProductAspect.java counted as required sites.
The first j7 grader missed them; every one of the 16 runs had updated them. A run passes when its other 57 files were exactly right (from the saved grade)
and its edit to PublishProductAspect.java changed exactly lines 70, 93, 114 and 136, each by renaming `.delete(` to `.removeEntity(` and nothing else.
Usage: python regrade_j.py GRADES_FOLDER"""
import glob, re, sys, collections
def j7_pass(path):
    txt = open(path).read().split("\n")
    m = re.match(r"j7_rename_entity_delete: (\d+) of (\d+) files correct; (\d+) other", txt[0])
    ok_files, others = int(m.group(1)), int(m.group(3))
    cur, old, new, pend = None, {}, {}, 0
    for line in txt[1:]:
        if line.startswith("+++ b/"):
            cur = line[6:]
        h = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)", line)
        if h and "PublishProductAspect" in (cur or ""):
            ln = int(h.group(1)); pend = ln
        elif cur and "PublishProductAspect" in cur and line.startswith("-") and not line.startswith("---"):
            old[pend] = line[1:]
        elif cur and "PublishProductAspect" in cur and line.startswith("+") and not line.startswith("+++"):
            new[pend] = line[1:]
            pend += 1
    aspect_ok = set(old) == {70, 93, 114, 136} and all(new.get(k) == old[k].replace(".delete(", ".removeEntity(") for k in old)
    others_ok = others == 1 and "PublishProductAspect" in txt[1]
    return ok_files == 57 and others_ok and aspect_ok


if __name__ == "__main__":
    res = collections.defaultdict(list)
    for f in sorted(glob.glob(f"{sys.argv[1]}/j7_*.txt")):
        res["optimised" if "_optimised_" in f else "plain"].append(j7_pass(f))
    for a in ("plain", "optimised"):
        print(a, "j7 passed", sum(res[a]), "of", len(res[a]))
