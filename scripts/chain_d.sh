#!/bin/bash
cd "$(dirname "$0")"
for t in d1 d2; do ../trvenv/bin/trialrig run trial_$t.toml --out out_$t --parallel 3 > run_$t.log 2>&1; echo "$t done" >> chain_d.log; done
