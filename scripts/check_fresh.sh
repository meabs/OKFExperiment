#!/usr/bin/env bash
# Fail when the committed guide no longer matches what the generator makes from the current source.
#
#   KGEN="python /path/to/kgen.py" scripts/check_fresh.sh REPO [extra kgen okf options]
#
# Run it in CI on every change to REPO. Generation is deterministic (the same source gives the same files), so any difference in content
# or in a source file's SHA-256 means the guide is out of date. The two date fields (`generated.at`, `sources[].last_modified`) come from git
# history and are ignored here, so a shallow CI clone gives the same answer as a full one. Fix by regenerating and committing:  kgen sync --repo REPO && kgen okf --repo REPO --out REPO/okf --pointer REPO/AGENTS.md
set -euo pipefail
repo="${1:?path to the repository}"; shift || true
: "${KGEN:?set KGEN to the kgen command, for example KGEN='python kgen.py'}"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
cp -R "$repo" "$tmp/r"
$KGEN sync --repo "$tmp/r" >/dev/null
$KGEN okf --repo "$tmp/r" --out "$tmp/okf" "$@" >/dev/null
IGN=(-I '^  at: ' -I '^    last_modified: ')
if diff -r -q "${IGN[@]}" "$repo/okf" "$tmp/okf" >/dev/null; then echo "guide is up to date"; else echo "guide is out of date:"; diff -r -q "${IGN[@]}" "$repo/okf" "$tmp/okf" | sed "s#$tmp/#generated/#; s#$repo/#committed/#" | head -20; exit 1; fi
