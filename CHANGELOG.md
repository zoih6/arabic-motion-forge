# Changelog

## 2.2.0 — 2026-10-20 — "professional intake pipeline"
- **Reframe gate (skills/request-reframe + spec.md + check_project enforcement):** messy/one-line/contradictory user requests are NEVER executed literally — a spec-engineer pass rewrites them into a full production spec with visible corrections (letter-splitting→word reveals, fake-3D claims→spatial module rules, size-without-duration→bitrate math, "exactly like X"→transferable rules).
- **Web-research agent (skills/web-research + research/facts.json + notes.md):** bounded (≤8 sources, ≤10 min) knowledge intake for unfamiliar topics, on-screen facts and reference-media study; offline-safe, never blocks the pipeline.
- **True 3D: `runtime/spatial.mjs`** — additive, zero-dependency perspective compositor: camera pose math, point/quad projection with behind-camera guard, stable painter sort, unit-normal faces + Lambert-lite shade, axis-aligned slabs, orbit/dolly deterministic keys, exact two-triangle affine planar texturing (drawPlanar), depth-parallax ratio helper. 7 node tests; rules and honesty boundaries in `catalog/dictionaries/spatial-3d.json` (no C4D/AE claims; three.js documented as opt-in).
- **Preview gate:** `tools/preview.py` builds a ≤30 s representative draft (hook + per-scene windows), assembles ONE small mp4 + contact sheets for approval; render.py refuses final >30 s projects (kit_contract≥2) until `preview_approved` — no more 40-minute renders nobody sanctioned; windows cache by hash.
- **Quota guardian:** `tools/quota.py` (snapshot/disk/staging audit, ok|warn|block) consulted before every render; block verdict aborts cleanly with relocation advice. Kills the filled-disk/lost-data failure mode in hosted sandboxes.
- **Capped workspace delivery:** `tools/deliver.py` extracts light ≤25 MiB + hi ≤50 MiB copies into `<project>/deliverables/` (refuses out/ paths; decode+duration parity checks; sha+journal). Results land in the persistent workspace even after session churn; masters stay in staging.
- `new_project.py` seeds spec.md skeleton + preview fields; route/router/AGENTS updated; validate_kit enforces the new surface.
- Measured live: preview run 24.9 s (9 windows, 16.25 s, deterministic sha across runs) → re-run 170 ms via per-window persistent cache keyed to entry hash; render.py refuses unapproved >30 s finals and quota-blocked starts; deliver parity+decode checks; spatial suite 7/7; totals: 27 node tests, 18 browser checks, 132 kit checks, compat PASS (371 v1 paths, frozen runtime).


## 2.0.1 — 2026-10-20
- compat_check: v1 path-superset scope corrected to the contract surface; `research/` records are session state intentionally excluded from the core archive (was falsely failing validate_kit inside installed copies). No runtime, skill, dictionary or installer behavior changed.

## 2.0.0 — 2026-10-20

**Contract, tooling and stability upgrade. `runtime/*.mjs` byte-frozen from 1.0.0 — v1 projects render identically; `tools/compat_check.py` gates every release on that promise.**

### Agent instructions in English (accuracy pass)
- `AGENTS.md`, `SKILL.md`, all 12 `skills/*/SKILL.md`, `.agents` adapter and `workflows/` rewritten in English per Agent-Skills spec (name==dir, ≤1024-char triggering descriptions, <500-line bodies, progressive disclosure). Arabic remains where it belongs: on-screen copy and the Arabic-language notes in `README.md`/`reference/user-requirements-ar.md`.

### Inspiration engine + dictionaries (no more template output)
- `tools/direct.py`: topic-seeded generator of three structurally distinct concept directions across 8 axes (story device, metaphor, material, type architecture, camera, rhythm, accent, transitions) with a self-reported distinctness matrix.
- `tools/check_directions.py`: hard gate before style lock — TODOs must be resolved with topic-grounded rationale, directions must differ on ≥4 axes, and approved style fingerprints are collision-checked against the kit example and any `--against` prior project.
- `catalog/dictionaries/`: `direction-axes.json` (engine fuel + anti-patterns), `easings.json` (AE-curve → implementation status map), `camera.json` (depth-projection rules, anti-default moves), `continuity.json` (10 machine-checkable continuity rules), `styles.json` (Vox/Kurzgesagt/Ordinary Folk/Carbon study notes with explicit never-copy lines).

### Stability & session health (the "heavy chat" fix)
- `tools/journal.py` + per-project `journal.jsonl`: append-only milestone ledger; resume = read tail, never re-ask/re-render. `new_project.py` seeds it.
- `skills/performance` + `skills/recovery` + AGENTS.md §9: output-size discipline, one-renderer rule, background+wait pattern, 2 GB memory rules, bounded 3-pass QA loops.
- `tools/render.py --tier draft`: half-resolution silent review renders (~4× faster), isolated work dir/report, never blocks or overwrites a final; `--heartbeat-seconds` for upload waits.

### Compatibility & verification
- `catalog/compatibility-baseline.json`: v1 public surface (371 paths from the published v1.0.0 archive), 36+15 runtime exports, runtime sha256 freeze. `tools/compat_check.py` enforces superset + frozen bytes + kit field preservation and ships PASS/FAIL json.
- `tools/validate_kit.py` v2: 500+ checks incl. spec compliance per skill, dictionary schema sanity, English-contract enforcement, install-script safety, secret scan across tracked text, doc-link resolution.

### Faster install
- Root `install.sh` one-liner (`curl … | sh`) → verified latest-release zip (~1.3 MB, sha256-checked, path-symlink-hardened) → doctor; `tools/install_from_release.py` now resolves `latest` and any core-asset version while `--tag v1.0.0` keeps working.
- Library audit extended to 22 repositories (d3-shape, d3-interpolate, popmotion, roughjs added; commits+licenses re-verified).

## 1.0.0 — 2026-10-19
- Initial verified release: 9 skills, 104-entry catalog/33 mechanisms, frozen core math+canvas runtime with Arabic guards, 80 s vertical demo film, cold-install smoke, GitHub release assets.
