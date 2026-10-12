"""Experiment H: does OKF add value beyond an API contract? Writes three AgentTrialRig configs.

Five ways of giving the agent knowledge of a dependency it works against:
  none      nothing but a note that the dependency exists elsewhere
  contract  its OpenAPI document
  notes     a short hand-written reference (<= 30 KB; ours are 3 KB and 1 KB)
  okf       the generated OKF guide (the `recommended` preset)
  source    the dependency's source, readable (the upper bound)

H1  the four cross-repo change tasks of test G (field names the backend defines)
H2  six cross-repo questions about the backend's call structure (what a contract does not hold)
H3  four change tasks against a small runnable FastAPI service (behaviour the contract does not hold)
Network access is ON for every run and logged (scripts/net_check.py).

    python make_h.py SCRATCH_DIR          (SCRATCH_DIR is the `cx` folder of test G, with the `h` folder beside it)
"""
import pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
CX = pathlib.Path(sys.argv[1]).resolve()
H = CX.parent / "h"
EXP = pathlib.Path(__file__).resolve().parent.parent
NOTE = {
    "none": "The {what} is a separate repository and is not available here.\n",
    "contract": "The {what} is a separate repository and is not available here. Its OpenAPI document is at `{p}openapi.json`.\n",
    "notes": "The {what} is a separate repository and is not available here. A short reference written by its team is at `{p}notes.md`.\n",
    "okf": "The {what} is a separate repository and is not available here. `okf/` is an Open Knowledge Format guide generated from its source{x}. Start at `okf/index.md`.\n",
    "source": "The {what} is a separate repository, checked out read-only at `{src}`.\n",
}
SYSTEM = "# Repository notes\n\n"
HIDDEN = EXP / "hidden" / "h"


def overlays(name, what, p, guide, source, openapi, notes_file, extra_okf="", source_copy=None):
    ov = H / name
    shutil.rmtree(ov, ignore_errors=True)
    for arm, text in NOTE.items():
        d = ov / arm
        d.mkdir(parents=True)
        (d / "AGENTS.md").write_text(SYSTEM + text.format(what=what, p=p, src=source, x=extra_okf), encoding="utf-8")
        if arm == "contract":
            (d / p).mkdir(parents=True, exist_ok=True)
            shutil.copy(openapi, d / p / "openapi.json")
        if arm == "notes":
            (d / p).mkdir(parents=True, exist_ok=True)
            shutil.copy(notes_file, d / p / "notes.md")
        if arm == "source" and source_copy:
            shutil.copytree(source_copy, d / "service")
        if arm == "okf":
            shutil.copytree(guide, d / "okf")
    return ov


def arms(ov, source_name):
    out = []
    for a in NOTE:
        use = {"okf": 'uses = "okf/"\n', "source": f'uses = "{source_name}"\n', "contract": 'uses = "api/"\n', "notes": 'uses = "api/"\n'}.get(a, "")
        out.append(f'[[arms]]\nname = "{a}"\noverlay = "{ov / a}"\n{use}')
    return "\n".join(out)


AGENT = ('[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nedits = true\n'
         'args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\"", "-c", "sandbox_workspace_write.network_access=true"]\n')


def trial(name, title, reps, timeout, repos, ov, source_name, qs, suffix):
    return (f'name = "{name}"\n[defaults]\nreps = {reps}\nparallel = 3\ntimeout = {timeout}\nbaseline = "none"\nprompt_suffix = "{suffix}"\n'
            f'{repos}\n{arms(ov, source_name)}\n{AGENT}\n{qs}')


# H1 and H2: storefront working repository, Shopizer backend (identifiers renamed, as in tests D to G)
ov12 = overlays("overlays_h12", "backend this storefront calls", "api/", CX / "bundles_fe2/ref", CX / "pr2", H / "openapi.json", HIDDEN / "backend-notes.md",
                " (the backend's guide is in `okf/references/backend/`; the storefront's own guide is the rest of `okf/`)")
repos12 = f'[[repos]]\nname = "fe"\nsource = "{CX / "fe"}"\n'
import re
g = (CX / "make_g.py").read_text()
G = eval(re.search(r"^T = (\{.*?^\})", g, re.S | re.M).group(1))
e = (CX / "make_e.py").read_text()
Q = eval(re.search(r"^Q = (\[.*?^\])", e, re.S | re.M).group(1))
KEEP = {"e1_login", "e2_search", "e3_cart_delete", "e4_cart_add", "e5_shipping", "e7_register"}
q1 = "\n".join(f'[[questions]]\nid = "h1_{k}"\nrepo = "fe"\nverify = "OKF_EXP={CX} bash {CX}/verify_g.sh {k}"\nprompt = """{v}"""\n' for k, v in G.items())
q2 = "\n".join('[[questions]]\nid = "h2_%s"\nrepo = "fe"\nprompt = """%s"""\nexpect = [%s]\nmin_recall = 1.0\n' % (qid, p, ", ".join('"' + x.replace("\\", "\\\\") + '"' for x in ex))
               for qid, p, ex, _ in Q if qid in KEEP)
(CX / "trial_h1.toml").write_text(trial("h1-contract-vs-okf-changes", "", 4, 1200, repos12, ov12, "pr2", q1, "Say briefly which files you used."), encoding="utf-8")
(CX / "trial_h2.toml").write_text(trial("h2-contract-vs-okf-questions", "", 4, 900, repos12, ov12, "pr2", q2, "Answer briefly and say which tools or files you used."), encoding="utf-8")

# H3: small runnable service, a client repository to change
# the service source is kept out of reach: only the `source` arm gets it, inside its own workspace; the tests unpack it from a tarball
ov3 = overlays("overlays_h3", "pricing service this client talks to", "api/", H / "svc_okf", "service/", H / "svc_openapi.json", HIDDEN / "service-notes.md", source_copy=H / "svc")
T3 = {
    "h3_1_fetch_all": "Implement `fetch_all_orders(http)` in shop/client.py: it returns every order the service holds, in order, as a list of the dicts the service returns. Change only that file.",
    "h3_2_retry": "Implement `place_order(http, items, coupons, key, sleep=time.sleep)` in shop/client.py. It places an order with the service and returns the order dict. The service limits how fast orders can be created: when it refuses for that reason, wait as long as the service asks (call `sleep(seconds)`) and try again, so that the order is created exactly once and calling it again with the same `key` returns the same order. Change only that file.",
    "h3_3_errors": "Implement `place_order(http, items, coupons, key, sleep=time.sleep)` in shop/client.py: it places an order with the service and returns the order dict. When the service refuses, it raises the exceptions already defined in that file: `UnknownSku` when the order names a SKU the catalogue does not have, `KeyConflict` when the idempotency key was already used for a different order, and `OrderError` for any other refusal. Change only that file.",
    "h3_4_preview": "Implement `preview_total(items, coupons)` in shop/client.py. It returns, without calling the service, the total in cents that the service would quote for the same items and coupon codes (including its shipping), for any valid input. Change only that file.",
}
VER3 = {"h3_1_fetch_all": "h3_1_fetch_all", "h3_2_retry": "h3_2_retry", "h3_3_errors": "h3_3_errors", "h3_4_preview": "h3_4_preview"}
q3 = "\n".join(f'[[questions]]\nid = "{k}"\nrepo = "client"\nverify = "PRICING_SERVICE_TGZ={EXP / "fixtures" / "pricing-service.tgz"} bash {HIDDEN}/run_h3.sh {k}"\nprompt = """{v}"""\n' for k, v in T3.items())
repos3 = f'[[repos]]\nname = "client"\nsource = "{H / "client"}"\n'
(CX / "trial_h3.toml").write_text(trial("h3-contract-vs-okf-service", "", 4, 900, repos3, ov3, "service/", q3, "Say briefly which files you used."), encoding="utf-8")
print("wrote trial_h1/h2/h3.toml in", CX)
