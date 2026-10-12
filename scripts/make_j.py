"""Experiment J: a repository set up the recommended way against the same repository left as it is.
`plain`     the 1,173-file Shopizer backend, nothing added (no AGENTS.md, no guide, no graph, no skills).
`optimised` the same plus: the recommended `kgen okf` guide in okf/, the code graph and its `kg` tool in .agent-knowledge/,
            operating skills in .agents/skills/ (how to navigate and change, not about the technology), and an AGENTS.md that points to all of them.
Three change tasks (graded exactly, hidden/j/verify_j.py) and three structure questions (graded by expected class names).
Agents are isolated from the rest of the disk (AgentTrialRig `isolate`).

    python make_j.py SCRATCH_DIR     (SCRATCH_DIR is the `cx` folder; the `h` folder beside it holds `be` (graph in .agent-knowledge) and overlays_h12/okf (the guide))
"""
import pathlib, shutil, sys
CX = pathlib.Path(sys.argv[1]).resolve()
H = CX.parent / "h"
EXP = pathlib.Path(__file__).resolve().parent.parent
ov = H / "overlays_j"
shutil.rmtree(ov, ignore_errors=True)
(ov / "plain").mkdir(parents=True)
opt = ov / "optimised"
opt.mkdir()
shutil.copytree(H / "overlays_h12" / "okf" / "okf", opt / "okf")
shutil.copytree(H / "be" / ".agent-knowledge", opt / ".agent-knowledge", ignore=shutil.ignore_patterns("okf", "skills", "AGENTS.snippet.md", "__pycache__"))
shutil.copytree(EXP / "fixtures" / "operating-skills", opt / ".agents" / "skills", ignore=shutil.ignore_patterns("AGENTS.md"))
shutil.copy(EXP / "fixtures" / "operating-skills" / "AGENTS.md", opt / "AGENTS.md")
(ov / "plain" / ".keep").write_text("", encoding="utf-8")
T = {
 "j1_rename_payment_method": "Rename the method `authorizeAndCapture` declared in the interface `PaymentModule` to `chargeInOneStep`. Change the interface, every class that implements it, and every call to it. Do not change anything else.",
 "j2_add_param_to_overload": "The interface `PricingService` has several overloads of `calculateProductPrice`. Add a final parameter `boolean refresh` to the one overload that takes `(Product product, List<ProductAttribute> attributes)`, in the interface and in its implementation, and pass `false` at every call to that overload. Do not change the other overloads or the calls to them.",
 "j3_remove_unused_param": "The parameter `ShippingOrigin origin` of `ShippingQuoteModule.getShippingQuotes` is not used by any implementation. Remove it from the interface and from every implementation, and remove the matching argument from the call. Do not change anything else.",
}
Q = {
 "j4_overload_callers": ("Which classes call the overload `PricingService.calculateProductPrice(Product, List<ProductAttribute>)`, that is the one with two parameters where the second is a list of attributes? Only count calls that are real code, not commented out. Give only a list of simple class names, one per line, nothing else.",
                        ["ShoppingCartServiceImpl", "ShoppingCartFacadeImpl", "ProductVariationApi"],
                        ["ProductInventoryServiceImpl", "ReadableProductMapper", "ReadableMinimalProductMapper", "ReadableInventoryMapper", "ReadableProductPopulator", "ReadableProductPricePopulator", "PromoCodeCalculatorModule", "ManufacturerShippingCodeOrderTotalModuleImpl", "ProductFacade(V2)?Impl"]),
 "j5_shipping_chain" if False else "j5_shipping_chain": ("Which class contains the only direct call to `ShippingQuoteModule.getShippingQuotes`, which facade class calls that class, and which REST endpoint class calls that facade? Answer with the three class names.",
                        ["ShippingServiceImpl", "OrderFacadeImpl", "ShippingQuoteEndpoint"], []),
 "j6_checkout_path": ("Starting at the handler for `POST /api/v1/cart/{code}/checkout`, which classes are on the call path down to the payment module's `authorizeAndCapture` call? List the class names in call order.",
                      ["OrderApi", "OrderFacadeImpl", "OrderServiceImpl", "PaymentServiceImpl"], []),
}
SUFFIX = "Say briefly which files and commands you used. There is no Java compiler here; read the code."
arms = "\n".join(f'[[arms]]\nname = "{a}"\noverlay = "{ov / a}"\n' + ('uses = "okf/"\n' if a == "optimised" else "") for a in ("plain", "optimised"))
PY = "/tmp/gt/home/venv/bin/python"
qs = "\n".join(f'[[questions]]\nid = "{k}"\nrepo = "be"\nverify = "{PY} {EXP}/hidden/j/verify_j.py {k} {EXP}/hidden/j/spec.json"\nprompt = """{v}"""\n' for k, v in T.items())
q2 = "\n".join('[[questions]]\nid = "%s"\nrepo = "be"\nprompt = """%s"""\nexpect = [%s]\nmin_recall = 1.0\n%s' % (k, p, ", ".join(f'"{x}"' for x in ex), ("forbid = [%s]\n" % ", ".join(f'"{x}"' for x in fb)) if fb else "") for k, (p, ex, fb) in Q.items())
DENY = ["/Users/garry/code", "/private/tmp", "/tmp", "/Users/garry/Desktop", "/Users/garry/Documents", "/Users/garry/Downloads"]
toml = (f'name = "optimised-repo"\n[defaults]\nreps = 8\nparallel = 3\ntimeout = 1500\nbaseline = "plain"\nprompt_suffix = "{SUFFIX}"\n'
        f'[[repos]]\nname = "be"\nsource = "{H / "be"}"\n\n{arms}\n[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nedits = true\nsandbox = "danger-full-access"\n'
        f'isolate = {DENY!r}\n'.replace("'", '"') + f'args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]\n\n{qs}\n{q2}')
(CX / "trial_j.toml").write_text(toml, encoding="utf-8")
print("wrote", CX / "trial_j.toml")
