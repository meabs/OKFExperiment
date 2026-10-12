#!/usr/bin/env bash
# usage: PRICING_SERVICE_TGZ=<fixtures/pricing-service.tgz> run_h3.sh h3_1_fetch_all   (run from the trial directory, which holds shop/)
set -e
export PRICING_SERVICE_TGZ="${PRICING_SERVICE_TGZ:?}"
python3 "$(dirname "$0")/$1.py"
