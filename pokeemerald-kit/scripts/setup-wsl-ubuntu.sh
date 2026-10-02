#!/usr/bin/env bash
# Toolchain + clone for WSL2 / Ubuntu / Debian. Check docs/install/ in the repo if this drifts.
set -euo pipefail
sudo apt update
sudo apt install -y build-essential binutils-arm-none-eabi gcc-arm-none-eabi \
  libnewlib-arm-none-eabi libpng-dev git python3
DEST="${1:-$HOME/pokeemerald-expansion}"
[ -d "$DEST" ] || git clone https://github.com/rh-hideout/pokeemerald-expansion "$DEST"
cd "$DEST" && make -j"$(nproc)"
echo "Built: $DEST/pokeemerald.gba"
