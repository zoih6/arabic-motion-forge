---
name: arabic-motion-forge
description: Produce original Arabic or multilingual motion-graphics videos and films with layered After-Effects-style choreography, Arabic-safe typography, deterministic Canvas/FFmpeg rendering, audio-accurate synchronization, provenance-recorded assets, and verified GitHub checkpointing. Use for any motion/video/kinetic-typography request. Do not use for unrelated coding, and never reuse this kit's example compositions or any prior project's scenes as templates.
license: MIT (original components only; see THIRD_PARTY.md)
compatibility: Linux/macOS; Python 3.11+ and Node 18+ for tools; Chromium+FFmpeg needed only for rendering (tools/bootstrap.py); no Adobe products required; network used only for explicitly authorized fetch/publish.
---

# Arabic Motion Forge — router

You have been pointed here by a link; that means: become operational fast, read only what the task needs, and produce original motion design under the kit contract.

## First response on a fresh session (target < 60 s)

1. Bootstrap the kit (see `AGENTS.md` §0). Skip if already present.
2. `python3 <kit>/tools/doctor.py` — one JSON summary; do not re-read other files to double-check it.
3. If a project exists at the stated path: read `journal.jsonl` tail + `project.json`, resume from the recorded next step. Do not re-ask answered questions; do not re-run completed renders.
4. New project: `python3 tools/new_project.py ...`, then collect only genuinely missing brief facts in one short message (max 3–4 questions).

## Route table — load exactly what matches

| Task signal | Load |
|---|---|
| vague brief, missing constraints | `skills/intake/SKILL.md` |
| style identity, "make it creative", anti-template gate | `skills/creative-direction/SKILL.md` + run `tools/direct.py` |
| layer/timing/camera design | `skills/motion-direction/SKILL.md`, `catalog/choreography-recipes.md` |
| any Arabic on-screen text | `skills/arabic-type/SKILL.md` (mandatory before text animation) |
| photos, cutouts, charts, generated art | `skills/asset-craft/SKILL.md` |
| voiceover, music, singing interlude, sync | `skills/audio-sync/SKILL.md` |
| render slow, big job, flaky session | `skills/performance/SKILL.md` |
| crash, resume, "continue where we stopped" | `skills/recovery/SKILL.md` |
| QA, review loops, approval honesty | `skills/quality/SKILL.md` |
| publish, backup, storage budget | `skills/delivery/SKILL.md` |
| full documentary/film pipeline beyond this kit | `vendor/ai-film-studio/SKILL.md` (routing starts at its `workflows/intent-router.md`) |

Mechanism lookup: `catalog/README.md` → `catalog/motions.json` → `reference/recipes/<mechanism>.md`. Style families and their honest boundaries: `catalog/dictionaries/styles.json`. Motion vocabulary for directions: `catalog/dictionaries/direction-axes.json`.

## Non-negotiable gates (details in AGENTS.md)

1. Original design per topic: reference learning is allowed, scene/template copying is not. `tools/check_directions.py` and `tools/check_project.py` enforce the paperwork; the aesthetic judgment is yours and must be written down.
2. Arabic shaping integrity: words/lines as shaped units; transforms on masks and layout, never fractured letters.
3. Capability honesty: implemented vs equivalent vs documented-only vs unsupported. No fake "After Effects" claims; the AE tool is not in this environment.
4. Deterministic rendering: `seek(t)` purity, checkpointed encode, per-part verification, PTS checks, reuse-unchanged-on-fix.
5. Evidence before "done": media checks, upload verification, journal entry, and explicit statement of what remains unverified.
6. Never store secrets in repo files; publishing is per-project and user-authorized.

## Deliverable shapes

- Draft/motion review: short MP4 at draft tier + ≤8-panel contact sheet (files, not chat blobs).
- Final: verified MP4 + manifest (frames/fps/duration/sha), `journal.jsonl`, updated `project.json`.
- Always report: what ran, what passed, what could not be verified here (e.g., no human ear on the mix), and the exact next command for the user or the next session.
