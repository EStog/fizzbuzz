#!/usr/bin/env bash

# Script for running tests. Just execute `./run_tests.sh` to run all tests.

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

echo running unittests...
pytest --doctest-modules --disable-warnings || exit 1

echo running tests to docs...
rm -r ./docs/source/API
cd ./${SCRIPT_DIR}/docs
make doctest
