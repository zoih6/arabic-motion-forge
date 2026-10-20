#!/bin/sh
# Arabic Motion Forge one-line bootstrap: verified release archive, no history, no media, no token.
# Usage: curl -fsSL https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/install.sh | sh
#   or:  sh install.sh [destination] [tag]
set -eu
DEST="${1:-./motion-forge}"
TAG="${2:-latest}"
REPO="zoih6/arabic-motion-forge"
if [ ! -d "$DEST" ] || [ -z "$(ls -A "$DEST" 2>/dev/null || true)" ]; then
  python3 - "$DEST" "$TAG" "$REPO" <<'PY'
import subprocess,sys,urllib.request,os
dest,tag,repo=sys.argv[1:4]
boot='/tmp/iamf-bootstrap.py'
if not os.path.exists(boot) or os.path.getsize(boot)<500:
    with urllib.request.urlopen(f'https://raw.githubusercontent.com/{repo}/main/tools/install_from_release.py',timeout=30) as r:
        open(boot,'wb').write(r.read())
sys.exit(subprocess.call([sys.executable,boot,'--destination',dest,'--tag',tag,'--repo',repo]))
PY
  echo "Arabic Motion Forge ready at $DEST — next: python3 $DEST/tools/doctor.py"
else
  echo "Refusing to install into non-empty $DEST" >&2
  exit 1
fi
