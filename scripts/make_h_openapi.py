"""Experiment H, arm B: an OpenAPI 3 contract for a Spring backend, derived from its source.

Run with the Python that has tree-sitter (see kgen). It reads the routes from kgen's claims, then reads each handler's real
signature with tree-sitter so the contract has what springdoc would give: parameter names and where they travel
(path, query, header, body), the request-body schema, the response schema and the field types of every schema, with
inherited fields flattened in. It deliberately holds nothing a contract does not hold: no call graph, no behaviour.

    python make_h_openapi.py BACKEND_REPO OUT.json      (BACKEND_REPO has been through `kgen sync`)
"""
import json, re, sys, pathlib
from collections import defaultdict
import tree_sitter_java as tsj
from tree_sitter import Language, Parser

P = Parser(Language(tsj.language()))
repo = pathlib.Path(sys.argv[1])
claims = [json.loads(l) for l in (repo / ".agent-knowledge/claims.jsonl").read_text().splitlines() if l]
by = defaultdict(list)
for c in claims:
    by[c["predicate"]].append(c)

fields = defaultdict(list)       # type id -> [(name, type)]
supers = defaultdict(list)       # type id -> [type id]
simple = defaultdict(list)       # simple name -> [type id]
for c in by["is_a"]:
    simple[c["subject"].rsplit(".", 1)[-1]].append(c["subject"])
for c in by["has_field"]:
    n, t = c["attrs"]["name"], c["attrs"]["type"]
    if n != "serialVersionUID" and not c["attrs"].get("static"):
        fields[c["subject"]].append((n, t))
for c in by["extends"]:
    if not c["object"].startswith("external:"):
        supers[c["subject"]].append(c["object"])

PRIM = {"String": ("string", None), "Long": ("integer", "int64"), "long": ("integer", "int64"), "Integer": ("integer", "int32"), "int": ("integer", "int32"),
        "Boolean": ("boolean", None), "boolean": ("boolean", None), "BigDecimal": ("number", None), "Double": ("number", "double"), "double": ("number", "double"),
        "Date": ("string", "date-time"), "Float": ("number", "float"), "BigInteger": ("integer", None)}
schemas: dict[str, dict] = {}


file_of = {c["subject"]: c["source"]["file"] for c in by["is_a"]}
_imports: dict[str, tuple] = {}


def imports(file: str):
    """(explicit imports by simple name, wildcard packages, own package) of one Java file: how javac would find a name."""
    if file not in _imports:
        src = (repo / file).read_text(encoding="utf-8", errors="replace")
        pkg = (re.search(r"^package\s+([\w.]+);", src, re.M) or [None, ""])[1]
        exp, wild = {}, []
        for m in re.finditer(r"^import\s+(static\s+)?([\w.]+?)(\.\*)?;", src, re.M):
            if m.group(3):
                wild.append(m.group(2))
            else:
                exp[m.group(2).rsplit(".", 1)[-1]] = m.group(2)
        _imports[file] = (exp, wild, pkg)
    return _imports[file]


def resolve(name, ctx=None):
    ids = simple.get(name, [])
    if len(ids) <= 1 or ctx is None:
        return ids[0] if ids else None
    exp, wild, pkg = imports(ctx)
    for want in ([exp[name]] if name in exp else []) + [pkg + "." + name] + [w + "." + name for w in wild]:
        if "type:" + want in ids:
            return "type:" + want
    return sorted(ids)[0]


def ref_for(tname: str, ctx=None) -> dict:
    tname = tname.strip()
    m = re.match(r"^(\w+)<(.+)>$", tname)
    if tname.endswith("[]"):
        return {"type": "array", "items": ref_for(tname[:-2], ctx)}
    if m:
        outer, inner = m.groups()
        if outer in ("List", "Set", "Collection", "Iterable"):
            return {"type": "array", "items": ref_for(inner, ctx)}
        if outer in ("Map",):
            return {"type": "object", "additionalProperties": ref_for(inner.split(",")[-1], ctx)}
        if outer in ("ResponseEntity", "Optional", "Page"):
            return ref_for(inner, ctx)
        return ref_for(inner.split(",")[0], ctx) if resolve(outer, ctx) is None else ref_for(outer, ctx)
    if tname in PRIM:
        t, f = PRIM[tname]
        return {"type": t, **({"format": f} if f else {})}
    tid = resolve(tname, ctx)
    if tid is None:
        return {"type": "object"} if tname not in ("void", "Void") else {}
    return {"$ref": f"#/components/schemas/{schema_of(tid)}"}


names: dict[str, str] = {}


def schema_of(tid: str) -> str:
    if tid in names:
        return names[tid]
    base = tid.rsplit(".", 1)[-1]
    name = base if base not in names.values() else ".".join(tid.split(".")[-2:])  # two classes of one name: qualify the second by its package
    names[tid] = name
    schemas[name] = {}
    props, parents = {}, []
    for s in supers.get(tid, []):
        parents.append({"$ref": f"#/components/schemas/{schema_of(s)}"})
    for n, t in fields.get(tid, []):
        props[n] = ref_for(t, file_of.get(tid))
    body = {"type": "object", "properties": props}
    schemas[name] = {"allOf": parents + [body]} if parents else body
    return name


def anns(node):
    out = []
    for m in node.children:
        if m.type == "modifiers":
            for a in m.children:
                if a.type in ("annotation", "marker_annotation"):
                    nm = a.child_by_field_name("name").text.decode()
                    args = {}
                    al = a.child_by_field_name("arguments")
                    if al:
                        for e in al.named_children:
                            if e.type == "element_value_pair":
                                args[e.child_by_field_name("key").text.decode()] = e.child_by_field_name("value").text.decode().strip('"')
                            elif e.type == "string_literal":
                                args["value"] = e.text.decode().strip('"')
    # annotations also appear directly on parameters (modifiers child)
                    out.append((nm, args))
    return out


def find_method(path: pathlib.Path, name: str, line: int):
    tree = P.parse(path.read_bytes())
    best = None
    def walk(n):
        nonlocal best
        if n.type == "method_declaration" and n.child_by_field_name("name").text.decode() == name and n.start_point[0] + 1 <= line + 12 and n.end_point[0] + 1 >= line:
            if best is None or abs(n.start_point[0] + 1 - line) < abs(best.start_point[0] + 1 - line):
                best = n
        for c in n.children:
            walk(c)
    walk(tree.root_node)
    return best


paths: dict[str, dict] = {}
miss = 0
for c in sorted(by["handled_by"], key=lambda c: (c["attrs"]["path"], c["attrs"]["http"])):
    f = c["source"]["file"]
    if "/test/" in f:
        continue
    cls, mname = c["object"].split("#")
    m = find_method(repo / f, mname, c["source"]["line"])
    if m is None:
        miss += 1
        continue
    op = {"operationId": f"{cls.rsplit('.', 1)[-1]}.{mname}", "parameters": [], "responses": {"200": {"description": "OK"}}}
    for p in m.child_by_field_name("parameters").named_children:
        if p.type != "formal_parameter":
            continue
        pname = p.child_by_field_name("name").text.decode()
        ptype = p.child_by_field_name("type").text.decode()
        a = dict(anns(p))
        if ptype in ("MerchantStore", "Language", "HttpServletRequest", "HttpServletResponse", "Principal", "Locale", "Model", "BindingResult"):
            continue  # injected by the framework, not part of the contract
        if "RequestBody" in a:
            op["requestBody"] = {"required": True, "content": {"application/json": {"schema": ref_for(ptype, f)}}}
        elif "PathVariable" in a:
            op["parameters"].append({"name": a["PathVariable"].get("value") or a["PathVariable"].get("name") or pname, "in": "path", "required": True, "schema": ref_for(ptype, f)})
        elif "RequestHeader" in a:
            op["parameters"].append({"name": a["RequestHeader"].get("value") or pname, "in": "header", "schema": ref_for(ptype, f)})
        else:
            q = a.get("RequestParam", {})
            req = q.get("required", "true") != "false" and "defaultValue" not in q
            op["parameters"].append({"name": q.get("value") or q.get("name") or pname, "in": "query", "required": req, "schema": ref_for(ptype, f)})
    mods = next((x.text.decode() for x in m.children if x.type == "modifiers"), "")
    ao = re.search(r"@ApiOperation\((.*?)\)\s*(?=@|public)", mods, re.S)
    if ao:  # springfox puts the human text of @ApiOperation in the contract
        for key, out in (("value", "summary"), ("notes", "description")):
            t = re.search(key + r'\s*=\s*"((?:[^"\\]|\\.)*)"', ao.group(1))
            if t and t.group(1):
                op[out] = t.group(1).replace('\\"', '"')
    for ip in re.finditer(r"@ApiImplicitParam\(([^)]*)\)", mods):  # query/header parameters declared for the framework-injected arguments
        g = lambda k: (re.search(k + r'\s*=\s*"([^"]*)"', ip.group(1)) or [None, None])[1]
        if g("name") and not any(x["name"] == g("name") for x in op["parameters"]):
            op["parameters"].append({"name": g("name"), "in": "query", "required": False, "schema": {"type": (g("dataType") or "string").lower(), **({"default": g("defaultValue")} if g("defaultValue") else {})}})
        elif g("name"):
            for x in op["parameters"]:
                if x["name"] == g("name") and g("defaultValue"):
                    x["schema"]["default"] = g("defaultValue")
    ret = m.child_by_field_name("type").text.decode()
    r = ref_for(ret, f)
    if r:
        op["responses"]["200"]["content"] = {"application/json": {"schema": r}}
    http = c["attrs"]["http"].lower()
    for verb in (["get", "post", "put", "delete", "patch"] if http == "any" else [http]):
        paths.setdefault(c["attrs"]["path"], {})[verb] = op
doc = {"openapi": "3.0.3", "info": {"title": "Backend API", "version": "1"}, "paths": paths, "components": {"schemas": dict(sorted(schemas.items()))}}
pathlib.Path(sys.argv[2]).write_text(json.dumps(doc, indent=1), encoding="utf-8")
print(f"{len(paths)} paths, {len(schemas)} schemas, {miss} handlers not found, {pathlib.Path(sys.argv[2]).stat().st_size // 1024} KB")
