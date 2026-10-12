"""Experiment I: the true set of sites for four renames in the (readable) backend, found independently of kgen's claims.
A site is a declaration (interface and implementation), a call through a variable declared with the interface type, or an unqualified/this call inside the implementation class.
Usage: python make_i_sites.py BACKEND_REPO OUT.json"""
import re, glob, json, sys, os
os.chdir(sys.argv[1])
TASKS = {
 "i1_rename_findOne": ("findOne", "ProductService", "ProductServiceImpl", "findProductById"),
 "i2_rename_cart_save": ("saveOrUpdate", "ShoppingCartService", "ShoppingCartServiceImpl", "persistShoppingCart"),
 "i3_rename_config_save": ("saveOrUpdate", "MerchantConfigurationService", "MerchantConfigurationServiceImpl", "saveMerchantConfiguration"),
 "i4_rename_toLocale": ("toLocale", "LanguageService", "LanguageServiceImpl", "resolveLocale"),
}
out = {}
files = [f for f in glob.glob("**/*.java", recursive=True)]
for tid, (old, iface, impl, new) in TASKS.items():
    sites = set()
    for f in files:
        L = open(f, encoding="utf-8", errors="replace").read().splitlines()
        text = "\n".join(L)
        vs = set(re.findall(r"\b" + iface + r"\s+(\w+)\s*[;=,)]", text))
        base = os.path.basename(f)
        for i, x in enumerate(L, 1):
            if x.lstrip().startswith(("*", "//", "/*")):
                continue
            hit = any(re.search(r"\b" + v + r"\s*\.\s*" + old + r"\s*\(", x) for v in vs)
            if base in (iface + ".java", impl + ".java") and re.search(r"(?<![\w.])" + old + r"\s*\(", x) and not re.search(r"private\s", x):
                hit = True  # declaration, or an unqualified call inside the implementation
            if base == impl + ".java" and re.search(r"\bthis\s*\.\s*" + old + r"\s*\(", x):
                hit = True
            if hit:
                assert len(re.findall(r"\b" + old + r"\s*\(", x)) == 1, (f, i, x)
                sites.add((f, i))
    out[tid] = {"old": old, "new": new, "sites": sorted(sites)}
    print(tid, len(sites), "sites in", len({s[0] for s in sites}), "files")
json.dump(out, open(sys.argv[2], "w"), indent=1)
