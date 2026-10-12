"""Experiment J: find the true sites of each change task in the (readable) backend, by tree-sitter and explicit type checks, independently of kgen's claims.
Usage: python make_j_sites.py BACKEND_REPO OUT.json"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jlib
repo, out = sys.argv[1], os.path.abspath(sys.argv[2])
os.chdir(repo)
files = [f for f in glob.glob("**/*.java", recursive=True)]
src = {f: open(f, "rb").read() for f in files}
roots = {f: jlib.P.parse(src[f]).root_node for f in files}


def nodes(kind, name):
    for f in files:
        for n in jlib._walk(roots[f]):
            if n.type == kind and n.child_by_field_name("name").text.decode() == name:
                yield f, n


TASKS = {}
# J1: rename a polymorphic interface method (interface in sm-core-modules, seven implementations in sm-core)
sites = [{"file": f, "kind": "decl", "line": n.child_by_field_name("name").start_point[0] + 1} for f, n in nodes("method_declaration", "authorizeAndCapture")]
sites += [{"file": f, "kind": "call", "line": n.child_by_field_name("name").start_point[0] + 1} for f, n in nodes("method_invocation", "authorizeAndCapture")]
TASKS["j1_rename_payment_method"] = {"op": "rename", "name": "authorizeAndCapture", "new": "chargeInOneStep", "sites": sites}
# J2: add a parameter to one overload of calculateProductPrice: (Product, List<ProductAttribute>)
sites = []
for f, n in nodes("method_declaration", "calculateProductPrice"):
    ps = jlib.params(n)
    if len(ps) == 2 and ps[1].child_by_field_name("type").text.decode().startswith("List<ProductAttribute"):
        sites.append({"file": f, "kind": "decl", "line": n.child_by_field_name("name").start_point[0] + 1})
for f, n in nodes("method_invocation", "calculateProductPrice"):
    a = jlib.args(n)
    if len(a) == 2 and a[1].text.decode() in ("attributes", "attributesList", "productAttributes"):
        sites.append({"file": f, "kind": "call", "line": n.child_by_field_name("name").start_point[0] + 1})
TASKS["j2_add_param_to_overload"] = {"op": "add", "name": "calculateProductPrice", "decl_param": "boolean refresh", "call_arg": "false", "sites": sites}
# J3: remove the unused `origin` parameter of ShippingQuoteModule.getShippingQuotes
sites = []
for f, n in nodes("method_declaration", "getShippingQuotes"):
    sites.append({"file": f, "kind": "decl", "line": n.child_by_field_name("name").start_point[0] + 1})
for f, n in nodes("method_invocation", "getShippingQuotes"):
    a = jlib.args(n)
    idx = [i for i, x in enumerate(a) if x.text.decode() in ("origin", "shippingOrigin")]
    assert len(idx) == 1 and idx[0] == 4, (f, [x.text.decode() for x in a])
    sites.append({"file": f, "kind": "call", "line": n.child_by_field_name("name").start_point[0] + 1, "index": idx[0]})
TASKS["j3_remove_unused_param"] = {"op": "remove", "name": "getShippingQuotes", "param_name": "origin", "sites": sites}
for t, v in TASKS.items():
    print(t, len(v["sites"]), "sites in", len({s["file"] for s in v["sites"]}), "files")
    for s in v["sites"]:
        print("   ", s["kind"], os.path.basename(s["file"]), s["line"])
json.dump(TASKS, open(out, "w"), indent=1)
