#!/usr/bin/env bash

echo running unittests...
pytest --doctest-modules

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

echo running tests to docs...
rm -r ./docs/source/API
sphinx-apidoc -T -e -M -o ./docs/source/API ./
cd ./${SCRIPT_DIR}/docs
make doctest
