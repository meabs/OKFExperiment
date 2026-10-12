"""Experiment I: does structural knowledge improve a software-engineering outcome, not only answers to questions about structure?
Four method renames in the readable 1,173-file Java backend. Each method has a common name (findOne, saveOrUpdate, toLocale), so a text search finds
3 to 10 times more hits than there are true call sites. Two arms: `plain` (repository only) and `guide` (the generated OKF guide of the backend in the repository).
Graded by hidden/i/verify_i.py: every true site renamed and nothing else changed. Agents are isolated from the rest of the disk (AgentTrialRig `isolate`).

    python make_i.py SCRATCH_DIR     (SCRATCH_DIR is the `cx` folder; the `h` folder beside it holds `be` and `overlays_h12/okf`)
"""
import pathlib, shutil, sys
CX = pathlib.Path(sys.argv[1]).resolve()
H = CX.parent / "h"
EXP = pathlib.Path(__file__).resolve().parent.parent
GUIDE = H / "overlays_h12" / "okf" / "okf"
ov = H / "overlays_i"
shutil.rmtree(ov, ignore_errors=True)
TEXT = {
    "plain": "# Backend\n\nThe source of the backend is in this repository.\n",
    "guide": ("# Backend\n\nThe source of the backend is in this repository. `okf/` is an Open Knowledge Format guide generated from it: classes, methods, routes and who calls what, "
              "with the file and line each fact came from. Start at `okf/index.md`. Use it to find your way around, then read the source to confirm before you rely on it.\n"),
}
for arm, text in TEXT.items():
    (ov / arm).mkdir(parents=True)
    (ov / arm / "AGENTS.md").write_text(text, encoding="utf-8")
    if arm == "guide":
        shutil.copytree(GUIDE, ov / arm / "okf")
T = {
 "i1_rename_findOne": "Rename the method `findOne(Long id, MerchantStore merchant)` of the interface `ProductService` (and its implementation) to `findProductById`, and update every call to it. Other methods that are also called `findOne` (on other classes or interfaces) must keep their name.",
 "i2_rename_cart_save": "Rename the method `saveOrUpdate(ShoppingCart)` of the interface `ShoppingCartService` (and its implementation) to `persistShoppingCart`, and update every call to it. Other methods that are also called `saveOrUpdate` (on other classes or interfaces) must keep their name.",
 "i3_rename_config_save": "Rename the method `saveOrUpdate(MerchantConfiguration)` of the interface `MerchantConfigurationService` (and its implementation) to `saveMerchantConfiguration`, and update every call to it. Other methods that are also called `saveOrUpdate` (on other classes or interfaces) must keep their name.",
 "i4_rename_toLocale": "Rename the method `toLocale(Language, MerchantStore)` of the interface `LanguageService` (and its implementation) to `resolveLocale`, and update every call to it. Other methods that are also called `toLocale` (on other classes or interfaces) must keep their name.",
}
SUFFIX = "Change only Java source files under src/main. There is no Java compiler here, so find every call by reading the code. Say briefly which files you used."
arms = "\n".join(f'[[arms]]\nname = "{a}"\noverlay = "{ov / a}"\n' + ('uses = "okf/"\n' if a == "guide" else "") for a in TEXT)
qs = "\n".join(f'[[questions]]\nid = "{k}"\nrepo = "be"\nverify = "python3 {EXP}/hidden/i/verify_i.py {k} {EXP}/hidden/i/sites.json"\nprompt = """{v}"""\n' for k, v in T.items())
DENY = ["/Users/garry/code", "/private/tmp", "/tmp", "/Users/garry/Desktop", "/Users/garry/Documents", "/Users/garry/Downloads"]
toml = (f'name = "rename-in-big-repo"\n[defaults]\nreps = 8\nparallel = 3\ntimeout = 1500\nbaseline = "plain"\nprompt_suffix = "{SUFFIX}"\n'
        f'[[repos]]\nname = "be"\nsource = "{H / "be"}"\n\n{arms}\n[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nedits = true\nsandbox = "danger-full-access"\n'
        f'isolate = {DENY!r}\n'.replace("'", '"') + f'args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]\n\n{qs}')
(CX / "trial_i.toml").write_text(toml, encoding="utf-8")
print("wrote", CX / "trial_i.toml")
