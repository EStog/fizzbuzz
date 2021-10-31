#!/usr/bin/env bash

# Script for running tests. Just execute `./run_tests.sh` to run all tests.

echo running unittests...
pytest --doctest-modules --cov=./ --cov-report=xml --disable-warnings || exit 1

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

echo running tests to docs...
rm -r ./docs/source/API
cd ./${SCRIPT_DIR}/docs
make doctest
