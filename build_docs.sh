#!/usr/bin/env bash

# Script to build the documentation. It takes as argument the format.
# Use `build_docs.sh` to see all available options.
# Use `build_docs.sh html` to build the documentation in HTML format.

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

echo building docs...
rm -r ./docs/source/API
cd ./${SCRIPT_DIR}/docs
make $@
