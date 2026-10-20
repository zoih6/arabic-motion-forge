#!/bin/sh
# Arabic Motion Forge one-line bootstrap: verified release archive, no history, no media, no token.
# Self-preparing: after install it SILENTLY backgrounds render-dependency setup (no output noise).
# Usage: curl -fsSL https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/install.sh | sh
#   or:  sh install.sh [destination] [tag]
set -eu
DEST="${1:-./motion-forge}"
TAG="${2:-latest}"
REPO="zoih6/arabic-motion-forge"
if [ -d "$DEST" ] && [ -n "$(ls -A "$DEST" 2>/dev/null || true)" ]; then
  echo "Refusing to install into non-empty $DEST" >&2
  exit 1
fi
BOOT=/tmp/iamf-bootstrap.py
curl -fsSL "https://raw.githubusercontent.com/$REPO/main/tools/install_from_release.py" -o "$BOOT" || { echo "could not fetch installer" >&2; exit 1; }
set -- "$BOOT" "$DEST" "$TAG" "$REPO"
python3 "$1" --destination "$2" --tag "$3" --repo "$4" >/dev/null || { echo "install failed — rerun with the installer visible" >&2; exit 1; }
# silent autopilot: pre-provision the render stack unless already present
LOG="$HOME/.cache/motion-forge-session/bootstrap.log"
mkdir -p "$(dirname "$LOG")"
if ! python3 -c "import playwright, imageio_ffmpeg, av" >/dev/null 2>&1; then
  (nohup python3 "$DEST/tools/bootstrap.py" --install >>"$LOG" 2>&1 &) >/dev/null 2>&1 || true
fi
echo "MOTION FORGE READY — $DEST (v:$TAG) — deps: background warmup started if needed; details in $LOG"
