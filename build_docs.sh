#!/usr/bin/env bash

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

echo building docs...
rm -r ./docs/source/API
cd ./${SCRIPT_DIR}/docs
make $@
