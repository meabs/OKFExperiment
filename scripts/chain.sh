#!/bin/bash
cd "$(dirname "$0")"
for t in b2 c2 a2; do ../trvenv/bin/trialrig run trial_$t.toml --out out_$t --parallel 3 > run_$t.log 2>&1; echo "$t done" >> chain.log; done
