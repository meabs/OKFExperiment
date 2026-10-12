#!/usr/bin/env python3
"""Check a copied-in guide against the dependency it describes.

    python check_references.py GUIDE_DIR DEPENDENCY_CHECKOUT [--list]

Every concept records, for each source file it was made from, a SHA-256 in `sources[].sha256` and the file's URL in `sources[].resource`.
This compares those hashes with the files in a current checkout of the dependency. A file that differs or is gone means the guide is
out of date for the concepts that cite it. Exit 1 when anything differs.

The file is found by matching the end of the URL against paths in the checkout, so it works for GitHub blob URLs and for relative paths.
"""
import argparse, hashlib, re, sys
from pathlib import Path

import yaml


def hash_of(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sources_of(md: Path):
    text = md.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return []
    fm = yaml.safe_load(m.group(1)) or {}
    return [(s.get("resource", ""), s.get("sha256", "")) for s in fm.get("sources") or []]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("guide")
    ap.add_argument("checkout")
    ap.add_argument("--list", action="store_true", help="also list the concepts affected")
    a = ap.parse_args()
    guide, repo = Path(a.guide), Path(a.checkout)
    files = {p.relative_to(repo).as_posix(): p for p in repo.rglob("*") if p.is_file() and ".git" not in p.parts}
    bad, checked, affected = {}, 0, {}
    for md in sorted(guide.rglob("*.md")):
        for resource, digest in sources_of(md):
            if not digest:
                continue
            path = max((rel for rel in files if resource.endswith(rel)), key=len, default=None)
            checked += 1
            state = "missing" if path is None else ("changed" if hash_of(files[path]) != digest else None)
            if state:
                bad[(path or resource)] = state
                affected.setdefault(path or resource, []).append(md.relative_to(guide).as_posix())
    for f, why in sorted(bad.items()):
        print(f"{why}: {f}" + (f"   (cited by {', '.join(affected[f])})" if a.list else ""))
    print(f"{checked} source citations checked, {len(bad)} file(s) differ" if bad else f"{checked} source citations checked, all match")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
