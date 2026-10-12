import shutil, pathlib
W = pathlib.Path(__file__).parent.resolve()
SENT = ", then read the source to confirm before you rely on it"
def pointer(sent=True, stale=False):
    t = ("# Repository knowledge\n\nThis is a storefront for a separate backend repository that is not available here. "
         "`okf/` is an Open Knowledge Format bundle generated from this repository's source, and `okf/references/backend/` is the bundle of the backend, copied in as it was when generated. "
         f"Start at `okf/index.md`. Use it to find your way around{SENT if sent else ''}.\n")
    if stale:
        t += "\nA concept whose `stale_after` time has passed describes source that has changed since it was generated; re-check it against the source.\n"
    return t
ARMS = {
    "none": ("# Storefront\n\nThe backend this storefront calls is a separate repository and is not available here.\n", None),
    "source": (f"# Storefront\n\nThe backend this storefront calls is a separate repository, checked out read-only at `{W / 'pr0'}`.\n", None),
    "source_drift": (f"# Storefront\n\nThe backend this storefront calls is a separate repository, checked out read-only at `{W / 'pr1'}`.\n", None),
    "bundle_sent": (pointer(True), "ref"),
    "bundle_nosent": (pointer(False), "ref"),
    "bundle_t_sent": (pointer(True, True), "ref_t"),
}
ov = W / "overlays_d"
shutil.rmtree(ov, ignore_errors=True)
for arm, (text, bundle) in ARMS.items():
    d = ov / arm
    d.mkdir(parents=True)
    (d / "AGENTS.md").write_text(text, encoding="utf-8")
    if bundle:
        shutil.copytree(W / "bundles_fe" / bundle, d / "okf")
def arm_block(arm):
    uses = 'uses = "okf/"\n' if ARMS[arm][1] else ('uses = "pr[01]"\n' if arm.startswith("source") else "")
    return f'[[arms]]\nname = "{arm}"\noverlay = "{ov / arm}"\n{uses}'
def q(id, prompt, expect):
    ex = ", ".join('"' + e.replace("\\", "\\\\") + '"' for e in expect)
    return f'[[questions]]\nid = "{id}"\nrepo = "fe"\nprompt = """{prompt}"""\nexpect = [{ex}]\nmin_recall = 1.0\n'
SUFFIX_STD = "Answer briefly and say which tools or files you used."
SUFFIX_EFF = "Be efficient: use the repository knowledge where it answers the question and avoid unnecessary file reads. Answer briefly and say which tools or files you used."
Q = {
 "x1_cart_add": ("In src/redux/actions/cartActions.js, when the storefront adds an item and there is no cart id yet, it POSTs to the backend. Which backend controller method handles that request, which class is the request body bound to, and which field does that class have that the storefront does not send?",
                 ["appendItem", "BasketLineInput", "voucher"], ["appendItem", "BasketLineInput", "discountCode"]),
 "x2_cart_update": ("In src/redux/actions/cartActions.js, when a cart id already exists the storefront sends a PUT to the backend. Which backend controller method handles it, and which class is the request body bound to?",
                    ["replaceBasket", "BasketLineInput"], ["replaceBasket", "BasketLineInput"]),
 "x3_cart_delete": ("deleteFromCart in src/redux/actions/cartActions.js sends a DELETE for one cart item. Which backend controller method handles it, and what does the backend call the path variable that identifies the item?",
                    ["removeLine", r"\bsku\b"], ["removeLine", "itemCode"]),
 "x4_login": ("Which backend controller method handles the login request that src/pages/other/LoginRegister.js sends, and which class holds the credentials it receives?",
              ["SessionEndpoint", "openSession", "SignInForm"], ["SessionEndpoint", "openSession", "LoginPayload"]),
 "x5_search": ("Which backend controller method handles the product search request that src/pages/search-product/SearchProduct.js sends, which class holds the request, and which two fields does that class have for paging that the storefront does not send?",
               ["CatalogLookup", "lookup", "LookupQuery", r"\bsize\b", r"\boffset\b"], ["CatalogLookup", "lookup", "LookupQuery", r"\bsize\b", r"\boffset\b"]),
 "x6_config": ("Checkout.js loads the store configuration from the backend. Which backend controller method serves it, what class does it return, and name one boolean flag in that class that controls purchasing.",
               ["StoreSettingsEndpoint", r"\breadSettings\b", "StoreSettings", "purchasingEnabled"], ["StoreSettingsEndpoint", "readPublicSettings", "StoreSettings", "purchasingEnabled"]),
 "x7_reviews": ("src/pages/product-details/ProductDetail.js loads a product's reviews from the backend. Which backend controller method serves the review list, and what is the exact path it declares?",
                ["FeedbackEndpoint", "listFeedback", r"product/\{id\}/reviews"], ["FeedbackEndpoint", "listFeedback", r"product/\{id\}/reviews"]),
 "x8_shipping": ("Checkout.js POSTs a postal code and country to the backend to get shipping options for the cart. Which backend controller method handles that POST, which class is the body bound to, and what does it return?",
                 ["ShippingQuoteEndpoint", "quote", "GeoPoint", "QuoteSummary"], ["ShippingQuoteEndpoint", "quote", "GeoPoint", "QuoteSummary"]),
}
def trial(name, arms, qids, idx, suffix, reps):
    return (f'name = "{name}"\n[defaults]\nreps = {reps}\nparallel = 3\ntimeout = 900\nbaseline = "{arms[0]}"\nprompt_suffix = "{suffix}"\n'
            f'[[repos]]\nname = "fe"\nsource = "{W / "fe"}"\n\n' + "\n".join(arm_block(a) for a in arms) +
            '\n[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nargs = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]\n\n' +
            "\n".join(q(i, Q[i][0], Q[i][idx]) for i in qids))
(W / "trial_d1.toml").write_text(trial("shopizer-crossrepo-fresh", ["none", "source", "bundle_sent", "bundle_nosent"], list(Q), 1, SUFFIX_STD, 3), encoding="utf-8")
(W / "trial_d2.toml").write_text(trial("shopizer-crossrepo-stale", ["source_drift", "bundle_nosent", "bundle_sent", "bundle_t_sent"], list(Q), 2, SUFFIX_EFF, 4), encoding="utf-8")
