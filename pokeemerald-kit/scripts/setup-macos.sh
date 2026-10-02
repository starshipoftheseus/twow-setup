#!/usr/bin/env bash
# Toolchain + clone for macOS (Homebrew). Check docs/install/ in the repo if this drifts.
set -euo pipefail
brew install libpng pkg-config git python arm-none-eabi-gcc
DEST="${1:-$HOME/pokeemerald-expansion}"
[ -d "$DEST" ] || git clone https://github.com/rh-hideout/pokeemerald-expansion "$DEST"
cd "$DEST" && make -j"$(sysctl -n hw.ncpu)"
echo "Built: $DEST/pokeemerald.gba"
