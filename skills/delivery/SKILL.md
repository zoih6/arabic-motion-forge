---
name: delivery
description: Finalize and publish — checkpoint backup to GitHub Releases via the session publisher, anonymous verification of published state, archive assembly, storage budget, handoff summary. Use when a render or project phase must become durable/external or when closing any session.
---

# Delivery

## Storage law first
`python3 tools/storage.py` before writing >5 MB. Snapshot ~128 MB cap: sources in git, heavy media ONLY in Releases/staging (`~/.cache/...`), nothing under repo `out/`, deliverables under `deliverables/`. Media files are publisher-fed; they never enter the kit's own repository (package_core enforces for the kit; for projects, `tools/publish_session.py` blocks git-pushed files >95 MB by design).

## Session publishing (only with project.json publish_allowed + repo)
1. Publisher loop: `python3 tools/publish_session.py --serve ...` as a BACKGROUND process; enqueue per-part jobs (render.py `--publish-session` does this automatically and blocks until `uploaded`).
2. Refusals are features: existing asset name → version the asset name; large file → Release asset, not git.
3. Verify anonymously before claiming: fetch the release JSON, compare asset sha256/size against local; `git ls-remote` the tag. Quote both hashes.
4. Close: stop publisher, final manifest with all piece→commit→asset mappings, journal `final` line.
5. Tokens: environment of one process only, never written to any file/git config/command history; after any chat exposure, tell the user to revoke and reissue.

## Kit releases (maintaining this repo)
`tools/package_core.py` → `deliverables/arabic-motion-forge-core-<ver>.zip` (+SHA256SUMS); demo media to release assets only; `validate_kit` + `compat_check` green BEFORE tagging; CHANGELOG + version bump in same commit; public smoke test via raw URLs after push.

## Handoff
End every session with: state file paths, what is verified public vs local-only, exact resume command (`journal.py tail` + next tool call), and the token/hygiene note if applicable.
