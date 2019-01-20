#!/bin/sh

set -e
cd -- "$(dirname "$(readlink "$0" || echo "$0")")"

#./main.py &
#pid=$!

#sleep 2
#
#if ! kill -0 $pid; then
#    echo >&2 "E: server process is not present."
#    exit 1
#fi

env PleaseDeterministicIds=1 PleaseNoDelays=1 ./runner.py example/contract.py example/tests.py
./check1.py

#kill $pid

echo PASSED
