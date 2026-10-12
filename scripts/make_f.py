"""Experiment F: cross-repo CHANGE tasks. The working repository is the storefront; the backend it talks to is not available.
Each task writes a small pure function whose correctness depends on a fact only the backend knows (a field name, a declared path).
A hidden test checks the file the agent wrote."""
import pathlib, shutil
W = pathlib.Path(__file__).parent.resolve()
BASE = ("# Repository knowledge\n\nThis is a storefront for a separate backend repository that is not available here. "
        "`okf/` is an Open Knowledge Format guide generated from this repository's source, and `okf/references/backend/` is the guide of the backend, copied in as it was when generated. "
        "Start at `okf/index.md`. Use it to find your way around, then read the source to confirm before you rely on it.\n")
RULE = "\nEntries marked `[medium]` are heuristic guesses, not facts read from the code. When your answer relies on one, say so.\n"
ARMS = {
    "no_okf": ("# Storefront\n\nThe backend this storefront calls is a separate repository and is not available here.\n", None),
    "okf": (BASE, "ref"),
    "okf_confidence": (BASE + RULE, "ref_tags"),
}
ov = W / "overlays_f"
shutil.rmtree(ov, ignore_errors=True)
for arm, (text, guide) in ARMS.items():
    d = ov / arm
    d.mkdir(parents=True)
    (d / "AGENTS.md").write_text(text, encoding="utf-8")
    if guide:
        shutil.copytree(W / "bundles_fe" / guide, d / "okf")
T = {
 "f1_cart_request": "Create `src/util/cartRequest.mjs` (an ES module with no imports) that exports `buildAddToCartRequest({cartId, sku, quantity, voucher})`, returning `{method, path, body}` for the request the storefront sends to the backend to add an item to a cart. With no `cartId` it is a POST to `cart/`; with a `cartId` it is a PUT to `cart/<cartId>`. The body carries the product and quantity as in src/redux/actions/cartActions.js and, when `voucher` (a discount code) is given, the discount code in the field the backend's request class defines for it. Leave that field out when no discount code is given. Do not change other files.",
 "f2_search_request": "Create `src/util/searchRequest.mjs` (an ES module with no imports) that exports `buildSearchRequest({query, page, pageSize})`, returning `{method, path, body}` for the product search request the storefront sends to the backend (see src/pages/search-product/SearchProduct.js). Pages start at 1. The body carries the query plus the backend's two paging fields, the page size and the zero-based index of the first result, under the field names the backend's search request class defines. Do not change other files.",
 "f3_reviews_request": "Create `src/util/reviewsRequest.mjs` (an ES module with no imports) that exports `buildReviewsRequest({productId, store})`, returning `{method, path}` for the request that loads a product's reviews from the backend (see src/pages/product-details/ProductDetail.js). The path must be the one the backend declares for that route, followed by `?store=<store>`. Do not change other files.",
 "f4_store_config": "Create `src/util/storeConfig.mjs` (an ES module with no imports) that exports `canPurchaseOnline(config)`: given the object returned by the backend endpoint that `getConfig` in src/pages/other/Checkout.js calls (the backend's public configuration response, not any internal setting), return true only when that response's flag that controls online purchasing is true, and false when it is false or missing. Do not change other files.",
}
arms = "\n".join(f'[[arms]]\nname = "{a}"\noverlay = "{ov / a}"\n' + ('uses = "okf/"\n' if ARMS[a][1] else "") for a in ARMS)
qs = "\n".join(f'[[questions]]\nid = "{k}"\nrepo = "fe"\nverify = "bash $OKF_EXP/verify_f.sh {k}"\nprompt = """{v}"""\n' for k, v in T.items())
toml = (f'name = "crossrepo-change"\n[defaults]\nreps = 5\nparallel = 3\ntimeout = 900\nbaseline = "no_okf"\nprompt_suffix = "Say briefly which files you used."\n'
        f'[[repos]]\nname = "fe"\nsource = "{W / "fe"}"\n\n{arms}\n[[agents]]\nname = "codex"\nmodel = "gpt-5.6-luna"\nedits = true\n'
        f'args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]\nenv = {{ OKF_EXP = "{W}" }}\n\n{qs}')
(W / "trial_f.toml").write_text(toml, encoding="utf-8")
