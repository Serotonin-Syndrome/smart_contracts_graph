#!/bin/sh

set -e
cd -- "$(dirname "$(readlink "$0" || echo "$0")")"

env PleaseDeterministicIds=1 PleaseNoDelays=1 ../runner.py ../example/contract.py ../example/tests.py
./check1.py

echo PASSED
