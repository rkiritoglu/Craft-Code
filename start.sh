#!/usr/bin/env bash
# Craft&Code Local Studio Launcher
set -e
cd "$(dirname "$(readlink -f "$0")")"

if [ -x ".venv/bin/python3" ]; then
    exec .venv/bin/python3 serve.py --open "$@"
else
    exec python3 serve.py --open "$@"
fi
