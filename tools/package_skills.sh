#!/usr/bin/env bash
# Zip every skill folder into dist/<name>-<version>.zip for upload to Claude, Cowork or Microsoft 365 Copilot.
# Usage: tools/package_skills.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for dir in skills/*/; do
  name="$(basename "$dir")"
  version="$(sed -n 's/^  version: *"\{0,1\}\([0-9.]*\)"\{0,1\}/\1/p' "$dir/SKILL.md" | head -1)"
  (cd skills && zip -qr "../dist/${name}-${version:-0.0.0}.zip" "$name" -x '*.DS_Store')
  echo "dist/${name}-${version:-0.0.0}.zip"
done
