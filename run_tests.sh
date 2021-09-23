#!/usr/bin/env bash

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

echo running unittests...
pytest --doctest-modules --disable-warnings

echo running tests to docs...
rm -r ./docs/source/API
sphinx-apidoc -T -e -M -o ./docs/source/API ./fizzbuzz_lib
cd ./${SCRIPT_DIR}/docs
make doctest
