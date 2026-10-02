# pokeemerald-expansion starter kit for Claude

Everything to drop into a fresh pokeemerald-expansion clone so Claude (Desktop or Code) works well in it.

## What's here

| File | Goes where | Purpose |
|---|---|---|
| `CLAUDE.md` | repo root of your clone | Project rules Claude Code loads automatically |
| `design/*.md` | `design/` in your clone | Your hack's plan, so Claude doesn't invent lore or balance |
| `scripts/setup-wsl-ubuntu.sh` | run once | Installs the build toolchain and clones the repo (WSL2 / Ubuntu) |
| `scripts/setup-macos.sh` | run once | Same, for macOS (Homebrew) |
| `scripts/install-kit.sh` | run once | Copies `CLAUDE.md` + `design/` into your clone and commits |

## Quick start

```bash
# Windows: install WSL2 first (PowerShell as admin): wsl --install -d Ubuntu
# then inside Ubuntu (keep the repo in ~/, NOT /mnt/c — it builds far faster):
bash scripts/setup-wsl-ubuntu.sh        # or scripts/setup-macos.sh on a Mac
bash scripts/install-kit.sh ~/pokeemerald-expansion
cd ~/pokeemerald-expansion && make -j$(nproc)   # produces pokeemerald.gba
```

Get an unmodified build working before asking Claude to change anything.
If a step fails, `docs/install/` in the expansion repo is the source of truth.

## Resources

### The project
- Repo: https://github.com/rh-hideout/pokeemerald-expansion — clone this one (fork it on GitHub first if you want to push your own work).
- In-repo docs: `docs/` (tutorials), `docs/install/` (per-OS setup), `docs/changelogs/` (read before upgrading — breaking changes are listed there).
- Wiki: https://github.com/rh-hideout/pokeemerald-expansion/wiki
- Underlying decomp: https://github.com/pret/pokeemerald (and its wiki, which has many tutorials that still apply).

### Tools
- Porymap — map/event/encounter editor: https://github.com/huderlem/porymap/releases (use a version the expansion changelog supports).
- Poryscript — readable scripting language: https://github.com/huderlem/poryscript (much easier for Claude than raw `.inc` scripts).
- Porytiles — tileset compiler: https://github.com/grunt-lucas/porytiles
- mGBA — emulator with a good debugger for testing: https://mgba.io
- Floating IPS / Lunar IPS — make `.bps`/`.ips` patches to share instead of ROMs.

### Optional, third-party (vet before using)
- TORCH: https://github.com/eagredev/TORCH
- Expansion Editor: https://github.com/Bjornis12/pokeemerald-expansion-editor

### Community
- ROM Hacking Hideout (RHH) Discord — home of the expansion (invite in the repo README).
- pret Discord — the decomp projects.

## Using Claude Desktop vs Claude Code
- **Claude Code** (CLI, desktop Code tab, or VS Code) can run `make`, read errors and fix them in a loop. That's the setup this kit is built for.
- **Claude Desktop chat** can't run your build unless you add a filesystem/shell MCP server. If you use it, attach `CLAUDE.md` and the relevant `design/` file to a Project so it has the same context, and paste build errors back in.

## Workflow habits
1. `git commit` before every AI task; `git restore .` / `git reset --hard` if it goes wrong.
2. One small, specific task per request ("give Roxanne a Nosepass at Lv 15", not "rebalance gym leaders").
3. Claude edits code/data; you do maps in Porymap.
4. Share patches, never ROMs.
