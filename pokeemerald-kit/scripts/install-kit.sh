#!/usr/bin/env bash
# Copy CLAUDE.md and design/ into a pokeemerald-expansion clone and commit them.
set -euo pipefail
KIT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?usage: install-kit.sh <path-to-pokeemerald-expansion>}"
cp -n "$KIT/CLAUDE.md" "$DEST/CLAUDE.md"
mkdir -p "$DEST/design" && cp -n "$KIT"/design/*.md "$DEST/design/"
cd "$DEST" && git add CLAUDE.md design && git commit -m "Add CLAUDE.md and design docs"
