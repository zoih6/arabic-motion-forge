#!/bin/sh
# Arabic Motion Forge — skill-native bootstrap.
# Kit lands in $HOME/.motion-forge (never the workspace), a personal skill is registered at
# ~/.claude/skills/arabic-motion-forge, render engines warm up silently in background.
# Usage: curl -fsSL https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/install.sh | sh
#   or:  sh install.sh [kit-destination] [tag]
set -eu
DEST="${1:-$HOME/.motion-forge}"
TAG="${2:-latest}"
REPO="zoih6/arabic-motion-forge"
mkdir -p "$(dirname "$DEST")"
if [ -d "$DEST" ] && [ -n "$(ls -A "$DEST" 2>/dev/null || true)" ]; then
  echo "Refusing to install into non-empty $DEST" >&2
  exit 1
fi
BOOT=/tmp/iamf-bootstrap.py
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/tools/install_from_release.py" -o "$BOOT" || { echo "could not fetch installer" >&2; exit 1; }
python3 "$BOOT" --destination "$DEST" --tag "$TAG" --repo "$REPO" >/dev/null || { echo "install failed — rerun with the installer visible" >&2; exit 1; }
# register the personal skill (global; workspace stays untouched)
SKILL_DIR="$HOME/.claude/skills/arabic-motion-forge"
{ mkdir -p "$SKILL_DIR" && sed "s#@KIT@#$DEST#g" "$DEST/skill_launcher.md" > "$SKILL_DIR/SKILL.md"; } 2>/dev/null || true
# silent render warmup, non-fatal
LOG="$HOME/.cache/motion-forge-session/bootstrap.log"
mkdir -p "$(dirname "$LOG")"
if ! python3 -c "import playwright, imageio_ffmpeg, av" >/dev/null 2>&1; then
  (nohup python3 "$DEST/tools/bootstrap.py" --install >>"$LOG" 2>&1 &) >/dev/null 2>&1 || true
fi
echo "MOTION FORGE READY — kit: $DEST · skill: $SKILL_DIR · say hi in chat and the studio will ask you 5 questions"
