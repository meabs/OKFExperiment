"""Experiment J: apply the expected edit for a task to the original Java source, so an agent's result can be compared with it.
Three kinds of edit, each at declarations and calls found by tree-sitter: rename, add a trailing parameter (and pass an argument at calls), remove a parameter (and the argument at calls)."""
import tree_sitter_java as tsj
from tree_sitter import Language, Parser

P = Parser(Language(tsj.language()))


def _walk(n):
    yield n
    for c in n.children:
        yield from _walk(c)


def find(root, kind, name, line):
    """the method_declaration / method_invocation called `name` whose name identifier starts on 1-based `line`"""
    for n in _walk(root):
        if n.type == kind:
            nm = n.child_by_field_name("name")
            if nm.text.decode() == name and nm.start_point[0] + 1 == line:
                return n
    return None


def params(decl):
    return [p for p in decl.child_by_field_name("parameters").named_children if p.type in ("formal_parameter", "spread_parameter")]


def args(call):
    return list(call.child_by_field_name("arguments").named_children)


def removal(items, k):
    """byte range that removes item k together with one comma"""
    if k > 0:
        return items[k - 1].end_byte, items[k].end_byte
    return items[0].start_byte, items[1].start_byte if len(items) > 1 else items[0].end_byte


def apply(src: bytes, task: dict, sites: list) -> bytes:
    """sites: [{kind: 'decl'|'call', line: int}]; task: {op: 'rename'|'add'|'remove', name, new?, decl_param?, call_arg?, param_name?}"""
    root = P.parse(src).root_node
    edits = []  # (start, end, replacement)
    for s in sites:
        if s["kind"] == "string":  # a string literal that names the method, such as an AspectJ pointcut
            hit = [n for n in _walk(root) if n.type == "string_literal" and n.start_point[0] + 1 == s["line"] and ("." + task["name"] + "(") in n.text.decode()]
            if not hit:
                raise ValueError(f"string site not found: {s}")
            for n in hit:
                edits.append((n.start_byte, n.end_byte, n.text.replace(("." + task["name"] + "(").encode(), ("." + task["new"] + "(").encode())))
            continue
        n = find(root, "method_declaration" if s["kind"] == "decl" else "method_invocation", task["name"], s["line"])
        if n is None:
            raise ValueError(f"site not found: {s} for {task['name']}")
        if task["op"] == "rename":
            nm = n.child_by_field_name("name")
            edits.append((nm.start_byte, nm.end_byte, task["new"].encode()))
        elif task["op"] == "add":
            items = params(n) if s["kind"] == "decl" else args(n)
            text = task["decl_param"] if s["kind"] == "decl" else task["call_arg"]
            edits.append((items[-1].end_byte, items[-1].end_byte, ("," + text).encode()))
        elif task["op"] == "remove":
            if s["kind"] == "decl":
                items = params(n)
                k = [i for i, p in enumerate(items) if p.child_by_field_name("name").text.decode() == task["param_name"]][0]
            else:
                items = args(n)
                k = s["index"]
            a, b = removal(items, k)
            edits.append((a, b, b""))
    out = bytearray(src)
    for a, b, r in sorted(edits, reverse=True):
        out[a:b] = r
    return bytes(out)
