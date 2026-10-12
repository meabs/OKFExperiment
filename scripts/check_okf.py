#!/usr/bin/env python3
"""Check a bundle against the rules of OKF v0.2 (SPEC.md sections 3.1, 4.1, 5, 6, 7, 8, 9 and 11).

    python check_okf.py BUNDLE_DIR [--strict]

Exit 1 when a MUST is broken. Without --strict, SHOULD-level findings are printed as warnings; with it they fail too.
Needs PyYAML. Timestamps are kept as text, as the reference agent's parser does, so the check sees what the author wrote.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

RESERVED = {"index.md", "log.md"}
STATUSES = {"draft", "stable", "deprecated"}
ACTOR = re.compile(r"^(human:[^\s]+|process:[^\s]+|[^\s:/]+/[^\s]+)$")  # human:<id> | process:<id> | <producer>/<version>
ISO_WITH_OFFSET = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$")
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {ch: [(t, r) for t, r in rs if t != "tag:yaml.org,2002:timestamp"] for ch, rs in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def split(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    raise ValueError("unterminated frontmatter")


def path_valued(v) -> str | None:
    """Section 6.2: an absolute URL, a bundle-relative path starting with '/', or a relative path."""
    if not isinstance(v, str) or not v:
        return "empty"
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", v) and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", v):
        return f"'{v}' uses a scheme that is not an absolute URL (no '//')"
    return None


def check(root: Path):
    must, should = [], []
    files = sorted(p for p in root.rglob("*.md"))
    rels = {p.relative_to(root).as_posix() for p in files}
    for p in files:
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding="utf-8")
        try:
            fm_text, body = split(text)
            fm = yaml.load(fm_text, Loader=Loader) if fm_text is not None else None
        except Exception as e:  # noqa: BLE001
            must.append(f"{rel}: frontmatter does not parse ({e})")
            continue
        if p.name in RESERVED:
            if p.name == "index.md":
                if fm is not None and not (rel == "index.md" and set(fm) <= {"okf_version"}):
                    must.append(f"{rel}: an index.md has frontmatter other than a root okf_version (section 8)")
                if rel == "index.md" and fm and not isinstance(fm.get("okf_version"), str):
                    should.append(f"{rel}: okf_version should be a quoted string")
                if not re.search(r"^#{1,6} .+", body, re.M):
                    should.append(f"{rel}: an index body should group entries under headings (section 8)")
                if not re.search(r"^[*-] \[[^\]]+\]\([^)]+\)", body, re.M):
                    should.append(f"{rel}: an index has no '* [Title](url) - description' entries")
            else:
                for h in re.findall(r"^## (.+)$", body, re.M):
                    if not re.match(r"^\d{4}-\d{2}-\d{2}$", h.strip()):
                        must.append(f"{rel}: log date heading '{h}' is not YYYY-MM-DD (section 9)")
            continue
        if fm is None or not isinstance(fm, dict):
            must.append(f"{rel}: no frontmatter block (section 11.1)")
            continue
        if not fm.get("type"):
            must.append(f"{rel}: missing or empty `type` (section 11.2)")
        for k in ("title", "description"):
            if k not in fm:
                should.append(f"{rel}: no `{k}` (recommended)")
        if "resource" in fm:
            why = path_valued(fm["resource"])
            if why:
                should.append(f"{rel}: resource {why} (section 6.2)")
        if "timestamp" in fm:
            should.append(f"{rel}: `timestamp` is the v0.1 field, superseded by generated.at (section 13.1)")
        if "tags" in fm and not (isinstance(fm["tags"], list) and all(isinstance(t, str) for t in fm["tags"])):
            should.append(f"{rel}: tags should be a list of strings")
        g = fm.get("generated")
        if g is not None:
            if not isinstance(g, dict) or not g.get("by"):
                should.append(f"{rel}: generated needs `by` (section 5.2)")
            else:
                if not ACTOR.match(str(g["by"])):
                    should.append(f"{rel}: generated.by '{g['by']}' does not follow the actor convention (section 7)")
                if g.get("at") is not None and not ISO_WITH_OFFSET.match(str(g["at"])):
                    should.append(f"{rel}: generated.at '{g['at']}' is not an ISO 8601 datetime with an explicit offset (section 5)")
        v = fm.get("verified")
        if v is not None:
            for ev in [v] if isinstance(v, dict) else v if isinstance(v, list) else []:
                if not isinstance(ev, dict) or not ev.get("by") or not ACTOR.match(str(ev.get("by"))):
                    should.append(f"{rel}: a verified event needs a `by` actor (section 5.2)")
                elif not ISO_WITH_OFFSET.match(str(ev.get("at", ""))):
                    should.append(f"{rel}: verified.at is not an ISO 8601 datetime with an explicit offset")
        if fm.get("status") is not None and fm["status"] not in STATUSES:
            should.append(f"{rel}: status '{fm['status']}' is not draft, stable or deprecated (section 5.4)")
        if fm.get("stale_after") is not None and not ISO_WITH_OFFSET.match(str(fm["stale_after"])):
            should.append(f"{rel}: stale_after is not an ISO 8601 datetime with an explicit offset (section 5.5)")
        for s in fm.get("sources") or []:
            if not isinstance(s, dict) or not s.get("resource"):
                should.append(f"{rel}: a sources entry needs `resource` (section 5.1)")
                continue
            why = path_valued(s["resource"])
            if why:
                should.append(f"{rel}: sources[].resource {why}")
            if s.get("last_modified") and not ISO_WITH_OFFSET.match(str(s["last_modified"])):
                should.append(f"{rel}: sources[].last_modified is not an ISO 8601 datetime with an explicit offset")
            if s.get("id") and not re.search(rf"\[\^{re.escape(str(s['id']))}\]", body):
                should.append(f"{rel}: sources[].id '{s['id']}' is never used as a footnote label in the body (section 5.1: id SHOULD be present when the body cites the source)")
    # links
    for p in files:
        rel = p.relative_to(root).as_posix()
        for target in LINK.findall(p.read_text(encoding="utf-8")):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            t = target.split("#")[0]
            base = root if t.startswith("/") else p.parent
            dest = (base / t.lstrip("/")).resolve() if t.startswith("/") else (base / t).resolve()
            if t and not dest.exists():
                should.append(f"{rel}: link {target} does not resolve (tolerated by section 6.1, but it is a defect in a generated bundle)")
    return must, should


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    root = Path(a.bundle)
    must, should = check(root)
    n = len(list(root.rglob("*.md")))
    for m in must:
        print("MUST   ", m)
    seen = {}
    for s in should:
        key = re.sub(r"'[^']*'", "'…'", re.sub(r"^[^:]+: ", "", s))
        key = re.sub(r"link \S+ does", "link … does", key)
        seen.setdefault(key, []).append(s.split(":")[0])
    for key, who in seen.items():
        print(f"SHOULD  {key}  [{len(who)} file(s), e.g. {who[0]}]")
    print(f"{n} markdown files: {len(must)} MUST finding(s), {len(should)} SHOULD finding(s)")
    return 1 if must or (a.strict and should) else 0


if __name__ == "__main__":
    sys.exit(main())
