#!/usr/bin/env bash
# Build command for Cloudflare Workers Builds (set in the dashboard as
# `bash scripts/cloudflare-build.sh`). Produces site/_site, which
# wrangler.jsonc serves as static assets for preview links.
set -euo pipefail

# The Primer theme's SCSS fails under a non-UTF-8 locale.
export LANG=C.UTF-8 LC_ALL=C.UTF-8

cd "$(dirname "$0")/../site"

# Keep gems outside site/: Jekyll 3.10 would otherwise scan site/vendor/.
bundle config set --local path "${HOME}/.bff-bundle"
bundle install

# Previews are served from the root of their own *.workers.dev address,
# so the default empty baseurl in _config.yml is correct here.
bundle exec jekyll build --trace --config _config.yml
