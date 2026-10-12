"""Experiment J grader. Run inside the agent's work folder (a git repo at the original commit). Usage: python verify_j.py TASK_ID spec.json
Passes only if every Java file equals the original with the expected edit applied at exactly the true sites. Comments, imports and whitespace are ignored,
so editing (or not editing) commented-out code, tidying imports or re-wrapping a line makes no difference."""
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jlib
tid, sj = sys.argv[1], sys.argv[2]
task = json.load(open(sj))[tid]


def norm(src: bytes) -> str:
    root = jlib.P.parse(src).root_node
    cut = [(n.start_byte, n.end_byte) for n in jlib._walk(root) if n.type in ("line_comment", "block_comment", "import_declaration")]
    out = bytearray(src)
    for a, b in sorted(cut, reverse=True):
        out[a:b] = b""
    return re.sub(rb"\s+", b"", bytes(out)).decode("utf-8", "replace")


by_file = {}
for s in task["sites"]:
    by_file.setdefault(s["file"], []).append(s)
changed = {x[3:] for x in subprocess.run(["git", "status", "--porcelain", "--", "*.java"], capture_output=True, text=True).stdout.split("\n") if x.strip()}
ok = wrong_files = 0
detail = []
for f in sorted(set(by_file) | changed):
    orig = subprocess.run(["git", "show", f"HEAD:{f}"], capture_output=True).stdout
    try:
        cur = open(f, "rb").read()
    except FileNotFoundError:
        cur = b""
    exp = jlib.apply(orig, task, by_file[f]) if f in by_file else orig
    good = norm(cur) == norm(exp)
    if f in by_file:
        ok += good
    elif not good:
        wrong_files += 1
        detail.append(f)
total = len(by_file)
msg = f"{tid}: {ok} of {total} files correct; {wrong_files} other files wrongly changed"
print(msg)
if os.environ.get("TRIAL_OUT") and os.environ.get("TRIAL_ID"):
    g = os.path.join(os.environ["TRIAL_OUT"], "grades")
    os.makedirs(g, exist_ok=True)
    open(os.path.join(g, os.environ["TRIAL_ID"] + ".txt"), "w").write(msg + "\n" + "\n".join(detail) + "\n" + subprocess.run(["git", "diff", "-U0", "--", "*.java"], capture_output=True, text=True).stdout)
sys.exit(0 if ok == total and wrong_files == 0 else 1)
