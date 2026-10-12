#!/usr/bin/env bash
# Independent check after the agent finishes: the task's hidden test passes and Click's own tests still do.
set -uo pipefail
task="${1:?t1, t2 or t3}"
cd "$TRIAL_DIR" || exit 2
PY="$OKF_PY"
cp "$OKF_EXP/hidden_${task}.py" tests/test_hidden_${task}.py
export PYTHONPATH=src
"$PY" -m pytest "tests/test_hidden_${task}.py" -q -p no:cacheprovider 2>&1 | tail -3
[ "${PIPESTATUS[0]}" -eq 0 ] || { echo "verify: hidden test failed" >&2; exit 1; }
"$PY" -m pytest tests -q -x -p no:cacheprovider --ignore="tests/test_hidden_${task}.py" 2>&1 | tail -2
[ "${PIPESTATUS[0]}" -eq 0 ] || { echo "verify: existing tests failed" >&2; exit 1; }
