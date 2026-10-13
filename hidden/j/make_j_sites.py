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

# J7: rename the generic base-service method delete(E) of SalesManagerEntityService, with every override and every call through a service type
import collections
sup = collections.defaultdict(set)
for f in files:
    for n in jlib._walk(roots[f]):
        if n.type in ("class_declaration", "interface_declaration"):
            nm = n.child_by_field_name("name").text.decode()
            for c in n.children:
                if c.type in ("superclass", "super_interfaces", "extends_interfaces"):
                    for t in jlib._walk(c):
                        if t.type == "type_identifier":
                            sup[nm].add(t.text.decode())


def is_sub(t, base, seen=None):
    seen = seen or set()
    if t == base:
        return True
    if t in seen:
        return False
    seen.add(t)
    return any(is_sub(x, base, seen) for x in sup.get(t, ()))


svc = {t for t in sup if is_sub(t, "SalesManagerEntityService")} | {"SalesManagerEntityService"}
impl = {t for t in sup if is_sub(t, "SalesManagerEntityServiceImpl")} | {"SalesManagerEntityServiceImpl"}
types_of = {}  # name -> declared type, across the whole repo (tests declare services in a base class)
for f in files:
    for n in jlib._walk(roots[f]):
        if n.type in ("field_declaration", "local_variable_declaration", "formal_parameter"):
            ty = n.child_by_field_name("type")
            if ty is None:
                continue
            T = re.sub(r"<.*", "", ty.text.decode()).split(".")[-1]
            names = [n.child_by_field_name("name").text.decode()] if n.type == "formal_parameter" else [v.child_by_field_name("name").text.decode() for v in n.children if v.type == "variable_declarator"]
            for nm in names:
                types_of.setdefault((f, nm), T)
                types_of.setdefault(("*", nm), T)
sites, cls_of = [], {}
for f in files:
    for n in jlib._walk(roots[f]):
        if n.type in ("class_declaration", "interface_declaration"):
            cname = n.child_by_field_name("name").text.decode()
            for m in jlib._walk(n):
                if m.type == "method_declaration" and m.child_by_field_name("name").text == b"delete" and len(jlib.params(m)) == 1 and cname in (svc | impl):
                    sites.append({"file": f, "kind": "decl", "line": m.child_by_field_name("name").start_point[0] + 1, "why": "declaration in " + cname})
for f in files:
    cls = [n.child_by_field_name("name").text.decode() for n in jlib._walk(roots[f]) if n.type in ("class_declaration", "interface_declaration")]
    for n in jlib._walk(roots[f]):
        if n.type == "method_invocation" and n.child_by_field_name("name").text == b"delete" and len(jlib.args(n)) == 1:
            o = n.child_by_field_name("object")
            why = None
            if o is None or o.text.decode() in ("super", "this"):
                if any(c in impl for c in cls):
                    why = "inherited call in implementation"
            else:
                nm = o.text.decode().replace("this.", "")
                T = types_of.get((f, nm)) or types_of.get(("*", nm))
                if T in svc:
                    why = "through " + T
            if why:
                sites.append({"file": f, "kind": "call", "line": n.child_by_field_name("name").start_point[0] + 1, "why": why})
for f in files:  # pointcut strings and other string literals that name a service's delete method (found after the first run, see EXPERIMENT_J.md)
    for n in jlib._walk(roots[f]):
        if n.type == "string_literal" and re.search(r"(Service|ServiceImpl)\.delete\(", n.text.decode()):
            sites.append({"file": f, "kind": "string", "line": n.start_point[0] + 1, "why": "string literal naming the method"})
TASKS["j7_rename_entity_delete"] = {"op": "rename", "name": "delete", "new": "removeEntity", "sites": sites}
for t, v in TASKS.items():
    print(t, len(v["sites"]), "sites in", len({s["file"] for s in v["sites"]}), "files")
    for s in v["sites"]:
        if t != "j7_rename_entity_delete":
            print("   ", s["kind"], os.path.basename(s["file"]), s["line"])
json.dump(TASKS, open(out, "w"), indent=1)
