"""Experiment G: harder cross-repo CHANGE tasks. Two edit the storefront's real code (a fix that depends on how the backend identifies a cart line, a new optional
parameter whose field name the backend defines); two write new modules whose field names are reached through the backend's inheritance chains.
Tests run the storefront's own modules in plain Node with the network and browser stubbed (harness/)."""
import pathlib, shutil
W = pathlib.Path(__file__).parent.resolve()
BASE = ("# Repository knowledge\n\nThis is a storefront for a separate backend repository that is not available here. "
        "`okf/` is an Open Knowledge Format guide generated from this repository's source, and `okf/references/backend/` is the guide of the backend, copied in as it was when generated. "
        "Start at `okf/index.md`. Use it to find your way around, then read the source to confirm before you rely on it.\n")
RULE = "\nEntries marked `[medium]` are heuristic guesses, not facts read from the code. When your answer relies on one, say so.\n"
ARMS = {
    "no_okf": ("# Storefront\n\nThe backend this storefront calls is a separate repository and is not available here.\n", None),
    "source": (f"# Storefront\n\nThe backend this storefront calls is a separate repository, checked out read-only at `{W / 'pr2'}`.\n", None),
    "okf": (BASE, "ref"),
    "okf_confidence": (BASE + RULE, "ref_tags"),
}
ov = W / "overlays_g"
shutil.rmtree(ov, ignore_errors=True)
for arm, (text, guide) in ARMS.items():
    d = ov / arm
    d.mkdir(parents=True)
    (d / "AGENTS.md").write_text(text, encoding="utf-8")
    if guide:
        shutil.copytree(W / "bundles_fe2" / guide, d / "okf")
T = {
 "g1_delete_item": "Users report that removing an item from the cart does nothing. `deleteFromCart` in src/redux/actions/cartActions.js sends a DELETE request to the backend. Find out why it fails against the backend and fix it. Change only that file.",
 "g2_add_voucher": "Add an optional last parameter `promoCode` to `addToCart` in src/redux/actions/cartActions.js. When it is given, send the discount code to the backend with the add-to-cart (or update-cart) request, in the field the backend's cart-item request defines for it. Do not send that field when no code is given. Keep everything else as it is. Change only that file.",
 "g3_checkout_request": "Create `src/util/checkoutRequest.mjs` (an ES module with no imports) exporting `buildCheckoutRequest({cartCode, shippingOptionId, currency, paymentToken, paymentModule, amount, agreedToTerms, comments})`. It returns `{method, path, body}` for the checkout request the storefront POSTs to `cart/<cartCode>/checkout` (see how src/pages/other/Checkout.js builds it). The body must use the field names the backend's order request class defines for: the chosen shipping option, the currency, whether the terms were accepted, the order comment, and a payment object holding paymentType `CREDITCARD`, transactionType `CAPTURE`, the payment module, the payment token and the amount, again under the backend's field names. Change only that file.",
 "g4_orders_list": "Create `src/util/ordersApi.mjs` (an ES module with no imports) exporting `normalizeOrderList(response)`. It turns the backend's order-list response (the one src/pages/other/RecentOrder.js loads) into `{orders, pages, total, onThisPage}`: the list of orders, the number of pages, the total number of records and the number of records on this page, read from the fields the backend's list response defines. Missing values become an empty list or 0. Change only that file.",
}
arms = "\n".join(f'[[arms]]\nname = "{a}"\noverlay = "{ov / a}"\n' + ('uses = "okf/"\n' if ARMS[a][1] else ('uses = "pr2"\n' if a == "source" else "")) for a in ARMS)
qs = "\n".join(f'[[questions]]\nid = "{k}"\nrepo = "fe"\nverify = "bash $OKF_EXP/verify_g.sh {k}"\nprompt = """{v}"""\n' for k, v in T.items())
toml = (f'name = "crossrepo-change-hard"\n[defaults]\nreps = 5\nparallel = 3\ntimeout = 1200\nbaseline = "no_okf"\nprompt_suffix = "Say briefly which files you used."\n'
        f'[[repos]]\nname = "fe"\nsource = "{W / "fe"}"\n\n{arms}\n[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nedits = true\n'
        f'args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]\nenv = {{ OKF_EXP = "{W}" }}\n\n{qs}')
(W / "trial_g.toml").write_text(toml, encoding="utf-8")
