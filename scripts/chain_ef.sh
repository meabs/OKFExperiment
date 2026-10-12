#!/bin/bash
cd "$(dirname "$0")"
while pgrep -f "[t]rialrig run trial_e" >/dev/null; do sleep 20; done
../trvenv/bin/trialrig run trial_f.toml --out out_f --parallel 3 > run_f.log 2>&1; echo "f done" >> chain_ef.log
