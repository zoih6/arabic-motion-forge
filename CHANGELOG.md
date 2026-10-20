# Changelog

## 2.4.0 — 2026-10-21 — skill-native install + studio intake
- Install is now skill-native per Claude/Codex skill conventions: kit lands in `~/.motion-forge` (never the workspace), a personal skill is auto-registered at `~/.claude/skills/arabic-motion-forge` (thin launcher → kit; progressive disclosure), render engines still warm silently in background. One READY line, no JSON dumps (full report stays in `install-report.json`).
- First touch is a real studio onboarding, not a status report: greeting + EXACTLY 5 kickoff questions with options (`tools/intake.py --emit`, via the host question tool when available; numbered inline otherwise). Answers scaffold the project (`intake.py --record` → new_project --quick + `intake.json` + brief patch).
- Direct-task autopilot: `intake.py --defaults --text '…'` derives duration/platform/type from the user's own message; nothing derived is ever re-asked; max one blocking question.
- AGENTS §0 / root SKILL.md / start / intake skills rewritten around this flow; validate_kit now enforces the install layout + intake wiring (159 checks).


## 2.3.1 — 2026-10-20 — setup chatter patch
- install.sh is now self-preparing: verifies+installs the release, silently backgrounds render-dependency warmup (log at ~/.cache/motion-forge-session/bootstrap.log), prints ONE `MOTION FORGE READY` line. No user decisions about toolchains.
- AGENTS §0 rewritten as SILENT AUTOPILOT with a verbatim ≤5-line first-reply template (rendered in the user's language) and explicit NEVER-DUMP list (raw JSON, doctor tables, feature menus, code blocks) — the field-observed setup wall is now a named contract breach; validate_kit enforces the wiring.


## 2.3.0 — 2026-10-20 — "quality is measurable, ceremony is optional"
Fixes from real-world v2.2 field test (user report: verbose first replies, superficial output, reframe deleting content, random research, bad ASR, weak type, slow pipeline, gate ceremony, doc drift):
- **First-reply budget (AGENTS §0.5, SKILL):** ≤6 lines contract — verdict + phase + ≤3 questions; no essays.
- **Preservation law (reframe):** user requests may be converted or extended, NEVER shortened — numbered `## User requirements` (preserved/converted/corrected) enforced by check_project; the old "rewrite and delete 90%" behavior now fails the gate.
- **Creative engine:** `skills/ideate` (art-director/director/social strategist persona panel, escalation test, "poster frame" requirement) + `catalog/dictionaries/creative-bank.json` (12 non-generic hooks, 8 wild-card cross-domain seeds, 12-entry cliché blacklist, 2026 trend questions) wired into `tools/direct.py` output — concepts now carry hook + wild card + forbidden tropes; style.json full mode requires `signature_move`, `forbidden_tropes`, `escalation`, `type_system`.
- **Motion-focused research:** `skills/web-research` rewritten as a specialist registry (Video Copilot/Ben Marriott/Mt. Mograph/School of Motion, GitHub expression repos, studio breakdowns, 2026 trends, Arabic case studies) with mandatory `research/design-language.md` mapping table (technique → kit primitive → steal/never) — browsing without mechanics rows no longer counts.
- **ASR engine:** `tools/transcribe.py` (faster-whisper/openai-whisper auto, 56 s windows — the OOM lesson encoded, word timestamps, confidence floor, sha-locked cache) + `--text` ALIGNMENT to approved copy with drift_ratio — raw ASR text never reaches the screen; `tools/sync_check.py` verifies every declared word entrance against the map at ±1.2 frames before final render; `bootstrap.py --transcribe` installs the backend.
- **Objective anti-slideshow audit:** `tools/motion_audit.py` measures flat_ratio, layered_ratio (16-cell motion grid), simultaneity and motion-burst density on any render; thresholds contract-enforced (flat>28% / layered<45% / simult>55% / <1.5 events/10s = FAIL). A photos+transitions video cannot pass — superficiality is now a number, not a vibe; quality skill runs it in both modes.
- **Typography upgrade:** `catalog/dictionaries/typography.json` (expressive Arabic display/body pairings with character notes, ≥1.5× size ladder, one deliberate break, weight-contrast law, no fake-bold) + `tools/fetch_font.py` (OFL faces from google/fonts, sha+license recorded into project manifest); single-family defaults now documented as defects.
- **Quick mode + gate aggregation:** `new_project.py --quick` for ≤30 s/simple asks (spec-lite, no preview gate, relaxed richness minimums — safety laws intact) and `tools/gate.py` runs the whole applicable gate set in ONE command with an aggregated verdict; removes the procedural burden users hit. Timebox table in performance skill (30 s ad ≤ ~20 min wall).
- **AE professional path:** `tools/export_ae.py` + `adapters/after-effects/export_ae.jsx` bridge — real comps/keyframes/eased interpolation generated from the layer plan for Adobe users (bridge export, honestly labeled; no parity claims).
- **Richness minimums in check_project:** ≥4 independent layers/scene (full), staggered unique start times, plus scene-count math — template-flat plans fail before rendering.
- **Docs sync:** README corrected (12→16 count) and validate_kit now FAILS on README skill-count drift permanently. 36 new checks total in validate_kit; all live smokes documented in research/v23-field-report.json.

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
