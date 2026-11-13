#!/usr/bin/env bash
# Zip every skill folder into dist/<name>.zip for upload to Claude Cowork or Microsoft 365 Copilot.
# The zip name has no version number, so this link always gets the newest release of a skill:
# https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest/download/<name>.zip
# The version is in each skill's SKILL.md.
# Usage: tools/package_skills.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for dir in skills/*/; do
  name="$(basename "$dir")"
  (cd skills && zip -qr "../dist/${name}.zip" "$name" -x '*.DS_Store')
  echo "dist/${name}.zip"
done
