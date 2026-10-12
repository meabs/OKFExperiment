import shutil, pathlib, sys
W = pathlib.Path(__file__).parent
ARMS = {"none": None, "minimal": "a_minimal", "nocalls": "a_nocalls", "default": "a_default", "allcalls": "a_allcalls", "package": "a_package", "noindex": "a_noindex"}
import os
POINTER = "# Repository knowledge\n\n`okf/` is an Open Knowledge Format bundle about this repository: one markdown file per module with its types, functions and (where listed) call edges. {where} Use it to find your way around.\n"
if os.environ.get("ARMS"):
    ARMS = {k: v for k, v in ARMS.items() if k in os.environ["ARMS"].split(",")}
ov = W / "overlays_a"
shutil.rmtree(ov, ignore_errors=True)
for arm, bundle in ARMS.items():
    if not bundle:
        continue
    d = ov / arm
    shutil.copytree(W / "bundles" / bundle, d / "okf")
    where = "Start at `okf/modules/`." if arm == "noindex" else "Start at `okf/index.md`."
    (d / "AGENTS.md").write_text(POINTER.format(where=where), encoding="utf-8")
KG = "" + os.environ.get('KGEN_SKILL', 'agent-graph-worktree/.apm/skills/agent-graph') + ""
arms = ['[[arms]]\nname = "none"\n']
for arm in ARMS:
    if arm != "none":
        arms.append(f'[[arms]]\nname = "{arm}"\noverlay = "{ov / arm}"\nuses = "okf/"\n')
arms.append(f'''[[arms]]
name = "graph"
prepare = ["rm -rf $TRIAL_OUT/warm && mkdir -p $TRIAL_OUT/warm && cd $TRIAL_OUT/warm && git init -q && printf 'x = 1\\\\n' > a.py && git add . && python3 {KG}/install.py --repo . --home $TRIAL_OUT/agent-graph-home >/dev/null 2>&1"]
setup = ["git config user.email t@e && git config user.name t && python3 {KG}/install.py --repo . --home $TRIAL_OUT/agent-graph-home >/dev/null 2>&1"]
uses = "agent-knowledge/bin/kg|kg (callers|subclasses|impact|find|show|deps)"
''')
def q(id, prompt, expect=None, verify=None, min_recall=None):
    t = f'[[questions]]\nid = "{id}"\nrepo = "click"\nprompt = """{prompt}"""\n'
    if expect: t += "expect = [" + ", ".join('"' + e.replace("\\", "\\\\") + '"' for e in expect) + "]\n"
    if min_recall: t += f"min_recall = {min_recall}\n"
    if verify: t += f'verify = "{verify}"\n'
    return t
qs = [
 q("inherit", "Which classes in src/click directly inherit from Parameter?", [r"\bOption\b", r"\bArgument\b"], min_recall=1.0),
 q("callers", "Which functions or methods in src/click call iter_params_for_processing directly? Ignore tests. Give each as Class.method.", [r"parse_args"], min_recall=1.0),
 q("where", "Where is get_parameter_source defined (file and class), and what does it return when the name is unknown?", [r"\bContext\b", r"\bNone\b"], min_recall=1.0),
 q("getdefault", "Which functions or methods in src/click call get_default directly? Ignore tests.", [r"\binvoke\b", "consume_value", "get_help_extra", "prompt_for_value"], min_recall=1.0),
 q("complete", "Which function in src/click builds the Context used for shell completion, and which function calls it?", ["_resolve_context", "get_completions"], min_recall=1.0),
 q("t1", "Add a method `Context.get_parameter_source_name(name)` that returns the source of the named parameter as a lowercase string such as 'commandline' or 'default', and None when the parameter is unknown. Keep existing tests passing. Do not add tests.", verify="bash $OKF_EXP/verify.sh t1"),
 q("t2", "Add a method `Command.params_by_priority(ctx)` that returns the parameter names in the order their callbacks would run when none of them were given on the command line: eager parameters first, then the rest in declaration order. Keep existing tests passing. Do not add tests.", verify="bash $OKF_EXP/verify.sh t2"),
 q("t3", "Add a read-only property `is_positional` to Parameter: True for Argument and False for Option. Keep existing tests passing. Do not add tests.", verify="bash $OKF_EXP/verify.sh t3"),
]
toml = f'''name = "okf-config-v2"
[defaults]
reps = 3
parallel = 3
timeout = 900
baseline = "none"
prompt_suffix = "Answer briefly and say which tools or files you used."
[[repos]]
name = "click"
source = "{W / 'click0'}"
''' + "\n".join(arms) + f'''
[[agents]]
name = "codex"
model = "gpt-5.6-luna"
edits = true
args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]
env = {{ OKF_EXP = "{W / 'exp'}", OKF_PY = "{W / 'pyv/bin/python'}" }}

''' + "\n".join(qs)
(W / os.environ.get("TRIAL_FILE", "trial_a.toml")).write_text(toml, encoding="utf-8")
print("arms", len(ARMS) + 1, "questions", len(qs))
