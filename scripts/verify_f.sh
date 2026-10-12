#!/usr/bin/env bash
# Hidden test for a cross-repo change task: runs the task's test against the file the agent wrote in the storefront.
set -uo pipefail
task="${1:?f1_cart_request, f2_search_request, f3_reviews_request or f4_store_config}"
cd "$TRIAL_DIR" || exit 2
cp "$OKF_EXP/hidden/f/${task}.test.mjs" "/tmp/${TRIAL_ID}_${task}.test.mjs" 2>/dev/null || cp "$OKF_EXP/hidden/f/${task}.test.mjs" ./.hidden_${task}.test.mjs
f="./.hidden_${task}.test.mjs"; [ -f "$f" ] || f="/tmp/${TRIAL_ID}_${task}.test.mjs"
node "$f" 2>&1 | tail -3
[ "${PIPESTATUS[0]}" -eq 0 ] || { echo "verify: hidden test failed" >&2; exit 1; }
