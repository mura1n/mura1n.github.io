#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
source scripts/ruby-env.sh
export JEKYLL_ENV=production
"${site_bundle[@]}" exec jekyll build --trace
