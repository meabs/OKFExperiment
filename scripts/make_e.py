"""Experiment E: do per-entry confidence labels help an agent that cannot check the source?
The storefront is the working repository; the backend's guide is copied in. A few of the backend guide's `calls` entries
(the heuristic, `[medium]` kind) are made wrong on purpose. Arms differ in how the guide labels them."""
import pathlib, re, shutil
W = pathlib.Path(__file__).parent.resolve()
BASE = ("# Repository knowledge\n\nThis is a storefront for a separate backend repository that is not available here. "
        "`okf/` is an Open Knowledge Format guide generated from this repository's source, and `okf/references/backend/` is the guide of the backend, copied in as it was when generated. "
        "Start at `okf/index.md`. Use it to find your way around, then read the source to confirm before you rely on it.\n")
RULE = "\nEntries marked `[medium]` are heuristic guesses, not facts read from the code. When your answer relies on one, say so.\n"
FACADE = "/references/backend/modules/com.salesmanager.shop.store.controller.%s.md"
PLANT = {  # caller -> (wrong class link, wrong callee)
    "SessionEndpoint.openSession": ("com.salesmanager.shop.store.controller.customer.facade.CustomerFacade", FACADE % "customer.facade", "CustomerFacade.registerCustomer"),
    "BasketEndpoint.removeLine": ("com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade", FACADE % "shoppingCart.facade", "ShoppingCartFacade.modifyCartMulti"),
    "BasketEndpoint.appendItem": ("com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade", FACADE % "shoppingCart.facade", "ShoppingCartFacade.replaceBasket"),
    "ShippingQuoteEndpoint.quote": ("com.salesmanager.shop.store.controller.order.facade.OrderFacade", FACADE % "order.facade", "OrderFacade.processOrder"),
}
def plant(root: pathlib.Path, mislabel: bool) -> int:
    n = 0
    for f in (root / "references/backend/modules").glob("*.md"):
        lines = f.read_text(encoding="utf-8").split("\n")
        for i, l in enumerate(lines):
            for caller, (cls, path, callee) in PLANT.items():
                if l.startswith(f"- `{caller}` calls ["):
                    cite = re.search(r" (`[^`]*:\d+`)( `\[medium\]`)?$", l)
                    tag = " `[high]`" if (mislabel and cite.group(2)) else (cite.group(2) or "")
                    lines[i] = f"- `{caller}` calls [{cls}]({path}) `{callee}` {cite.group(1)}{tag}"
                    n += 1
        f.write_text("\n".join(lines), encoding="utf-8")
    return n
ARMS = {"plain": ("ref", BASE, False), "labels": ("ref_tags", BASE, False), "labels_rule": ("ref_tags", BASE + RULE, False), "mislabelled_rule": ("ref_tags", BASE + RULE, True)}
ov = W / "overlays_e"
shutil.rmtree(ov, ignore_errors=True)
for arm, (src, text, mis) in ARMS.items():
    d = ov / arm
    d.mkdir(parents=True)
    shutil.copytree(W / "bundles_fe" / src, d / "okf")
    (d / "AGENTS.md").write_text(text, encoding="utf-8")
    assert plant(d / "okf", mis) == len(PLANT), arm
Q = [
 ("e1_login", "LoginRegister.js sends the login request to the backend. Which backend method handles it, and which class and method does that handler call to create the session token?", ["openSession", "JWTTokenUtil", "generateToken"], "registerCustomer"),
 ("e2_search", "SearchProduct.js sends the product search to the backend. Which backend method handles it, and which facade class and method does that handler call to run the search?", ["CatalogLookup", "lookup", "SearchFacade", "search"], None),
 ("e3_cart_delete", "deleteFromCart in cartActions.js sends a DELETE for one cart item. Which backend method handles it, and which facade method does that handler call to remove the item?", ["removeLine", "removeShoppingCartItem"], "modifyCartMulti"),
 ("e4_cart_add", "In cartActions.js, adding an item when there is no cart id yet sends a POST to the backend. Which backend method handles it, and which facade class and method does that handler call?", ["appendItem", r"ShoppingCartFacade\W+appendItem"], "replaceBasket"),
 ("e5_shipping", "Checkout.js POSTs a postal code and country to the backend to get shipping options for the cart. Which backend method handles it, and which class and method does that handler call to build the summary it returns?", ["quote", "ReadableShippingSummaryPopulator", "populate"], "processOrder"),
 ("e6_cart_update", "In cartActions.js, when a cart id already exists the storefront sends a PUT to the backend. Which backend method handles it, and which facade methods does that handler call?", ["replaceBasket", "modifyCartMulti"], None),
 ("e7_register", "LoginRegister.js posts the registration form to the backend. Which backend method handles it, and which facade method does that handler call to create the customer?", ["SessionEndpoint", "register", "registerCustomer"], None),
]
def qs():
    out = []
    for qid, prompt, expect, _ in Q:
        ex = ", ".join('"' + e.replace("\\", "\\\\") + '"' for e in expect)
        out.append(f'[[questions]]\nid = "{qid}"\nrepo = "fe"\nprompt = """{prompt}"""\nexpect = [{ex}]\nmin_recall = 1.0\n')
    return "\n".join(out)
arms = "\n".join(f'[[arms]]\nname = "{a}"\noverlay = "{ov / a}"\nuses = "okf/"\n' for a in ARMS)
toml = (f'name = "confidence-labels-crossrepo"\n[defaults]\nreps = 4\nparallel = 3\ntimeout = 900\nbaseline = "plain"\nprompt_suffix = "Answer briefly and say which tools or files you used."\n'
        f'[[repos]]\nname = "fe"\nsource = "{W / "fe"}"\n\n{arms}\n[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nargs = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]\n\n{qs()}')
(W / "trial_e.toml").write_text(toml, encoding="utf-8")
print("planted", len(PLANT), "questions", len(Q))
