#!/usr/bin/env bash
set -uo pipefail
task="${1:?c1, c2 or c3}"
cd "$TRIAL_DIR" || exit 2
cp "$OKF_EXP/hidden_${task}.py" tests/test_hidden_${task}.py
export PYTHONPATH=.
"$OKF_PY" -m pytest "tests/test_hidden_${task}.py" -q -p no:cacheprovider 2>&1 | tail -3
[ "${PIPESTATUS[0]}" -eq 0 ] || { echo "verify: hidden test failed" >&2; exit 1; }
"$OKF_PY" -m pytest tests -q -p no:cacheprovider --ignore="tests/test_hidden_${task}.py" 2>&1 | tail -2
[ "${PIPESTATUS[0]}" -eq 0 ] || { echo "verify: existing tests failed" >&2; exit 1; }
