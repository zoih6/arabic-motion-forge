# Install & bootstrap troubleshooting

**`curl … | sh install.sh` fails "Refusing to install into non-empty"** — pass a fresh destination: `sh install.sh ./mf2`. The installer never overwrites.

**No python3** — the one-liner needs python ≥3.11 for tools; read-only docs/catalog still work without it. On Windows: run tools via `py -3`; rendering needs WSL/Linux (Chromium+FFmpeg flow).

**Rate-limited by GitHub API (60 req/h anon)** — fetch `install.sh` raw once and rerun; or pass the pinned release: `sh install.sh ./mf2 v2.0.0` (single asset request + one API call). Offline: download `arabic-motion-forge-core-2.0.0.zip` + `SHA256SUMS.txt`, verify, then `python3 tools/install_from_release.py --archive <zip> --sha256 <sum> --destination ./mf2`.

**doctor says Playwright/Chromium missing** — expected on a cold box; only renders need it: `python3 tools/bootstrap.py --install` (background it; ~2 min). Docs, catalog, lab (`lab/index.html`), direction tools work without.

**Checksum mismatch** — someone re-released mid-fetch or a proxy altered bytes: refetch `SHA256SUMS.txt` from the release page and compare; never install on `--sha256` you typed from memory of an old chat.

**Old v1 project + v2 kit** — safe: runtime bytes are frozen (compat_check enforces); run `tools/compat_check.py` once; no migration needed. New fields in `project.json` are optional for v1-created projects; `journal.jsonl` can be created later (`tools/journal.py append --event boot ...`).

**Clone size surprise** — don't clone history for consumption; the release archive (≈1.3 MB) is the supported path.
