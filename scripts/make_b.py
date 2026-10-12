import shutil, pathlib
W = pathlib.Path(__file__).parent
BASE = "# Repository knowledge\n\n`okf/` is an Open Knowledge Format bundle about this repository: one markdown file per module with its types, functions and call edges. Start at `okf/index.md`. Use it to find your way around, then read the source to confirm before you rely on it.\n"
TRUST = "\nEach concept's `generated` field says how it was produced. A concept with no `verified` entry is unverified: machine-written and not reviewed by a person.\n"
STALE = "\nA concept whose `stale_after` time has passed is stale: re-check it against the source before relying on it.\n"
ARMS = {"noflag": BASE, "native": BASE + TRUST, "tags": BASE, "banner": BASE, "all": BASE + TRUST, "targeted": BASE + TRUST + STALE, "blanket": BASE + TRUST + STALE}
ov = W / "overlays_b"
shutil.rmtree(ov, ignore_errors=True)
arms = ['[[arms]]\nname = "none"\n']
for arm, text in ARMS.items():
    d = ov / arm
    shutil.copytree(W / "bundles" / f"b_{arm}", d / "okf")
    (d / "AGENTS.md").write_text(text, encoding="utf-8")
    arms.append(f'[[arms]]\nname = "{arm}"\noverlay = "{d}"\nuses = "okf/"\n')
def q(id, prompt, expect):
    return f'[[questions]]\nid = "{id}"\nrepo = "click"\nprompt = """{prompt}"""\nexpect = [' + ", ".join('"' + e.replace("\\", "\\\\") + '"' for e in expect) + "]\nmin_recall = 1.0\n"
qs = [
 q("inherit", "Which classes in src/click directly inherit from Parameter?", [r"\bOption\b", r"PositionalParameter"]),
 q("callers", "Which functions or methods in src/click call iter_params_for_processing directly? Ignore tests. Give each as Class.method.", [r"_ordered_params"]),
 q("complete", "Which function in src/click builds the Context used for shell completion, and which function calls it?", ["_resolve_completion_context", "get_completions"]),
 q("where", "Where is get_parameter_source defined (file and class), and what does it return when the name is unknown?", [r"\bContext\b", r"\bNone\b"]),
 q("getdefault", "Which functions or methods in src/click call get_default directly? Ignore tests.", [r"\binvoke\b", "consume_value", "get_help_extra", "prompt_for_value"]),
]
toml = f'''name = "okf-flags"
[defaults]
reps = 4
parallel = 3
timeout = 900
baseline = "none"
prompt_suffix = "Answer briefly and say which tools or files you used."
[[repos]]
name = "click"
source = "{W / 'click1'}"
''' + "\n".join(arms) + '''
[[agents]]
name = "codex"
model = "gpt-5.6-luna"
args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]

''' + "\n".join(qs)
(W / "trial_b.toml").write_text(toml, encoding="utf-8")
