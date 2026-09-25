#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/ruby-env.sh
exec "${site_bundle[@]}" exec jekyll serve --host 127.0.0.1 --port "${PORT:-8000}"
