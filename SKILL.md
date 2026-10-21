---
name: arabic-motion-forge
description: Use when creating Arabic or multilingual motion-graphics videos, kinetic typography, reels, ads, explainers, or short films that need Arabic-safe text, layered choreography, deterministic rendering, or verified delivery.
license: MIT (original components only; see THIRD_PARTY.md)
compatibility: Linux/macOS; Python 3.11+ and Node 18+ for tools; Chromium+FFmpeg needed only for rendering (tools/bootstrap.py); no Adobe products required; network used only for explicitly authorized fetch/publish.
---

# Arabic Motion Forge — router

## Activation contract — highest priority

Use `tools/intake.py` as the only first-touch router:

- **First touch with no brief** (`install`, `ثبت`, `فعّل`, `شغّل`, or a bare start): run `python3 tools/intake.py --emit`, show its greeting and exactly five option questions through the host question tool when available, then record answers with `--record`. Do not show JSON, diagnostics, architecture, or feature tours.
- **Direct brief**: run `python3 tools/intake.py --defaults --text '<user message>'`, use the derived answers silently, ask at most one blocking question, and start the normal route.
- **Resume**: read the journal tail and project state first, state the resume phase in one line, and never re-ask saved answers.

The intake answers are saved in `intake.json`, `brief.json`, and `journal.jsonl`. The intake form is the onboarding UI; all production gates and quality contracts remain active after it.

You have been pointed here by a link; that means: become operational fast, read only what the task needs, and produce original motion design under the kit contract.

## FIRST REPLY = AGENTS.md §0 template: at first touch that means the greeting line + exactly 5 option-questions from `tools/intake.py --emit` (host question tool when available); after intake, one status line and work. Never paste JSON/tables/file-menus; the workspace never receives kit files.

## Quick vs full
`new_project.py --quick` (≤30 s / simple): spec-lite, no preview gate, one aggregated `tools/gate.py` before final. `full` for everything else: complete chain. Safety laws run in BOTH modes; quick cuts ceremony, never quality.

## First response on a fresh session (target < 60 s)

1. Bootstrap the kit (see `AGENTS.md` §0). Skip if already present.
2. On first touch, use `tools/intake.py --emit`; run `doctor.py` only when the environment is missing or broken.
3. If a project exists at the stated path: read `journal.jsonl` tail + `project.json`, resume from the recorded next step. Do not re-ask answered questions; do not re-run completed renders.
3b. Gates in ONE call: `python3 tools/gate.py <dir>/project.json [--stage final]`.
4. New project: use `tools/intake.py --record` after the five answers; it creates the project and preserves the answers before production begins.

## Unified video route — vendor first, local execution second

For **every** video/animation/motion request, read `workflows/vendor-bridge.md` and route through `vendor/ai-film-studio/workflows/intent-router.md` before `direct.py`, scene code, prompts, or rendering. The vendor route owns intent, story, production sheet, references, storyboard, and audio plan; Arabic Motion Forge owns Arabic-safe implementation, deterministic rendering, QA, and delivery. A new project cannot pass `check_project.py` until `vendor-bridge.json` and its mapped handoff artifacts are approved.

## Route table — load exactly what matches

| Any video/animation/motion request — ALWAYS | `workflows/vendor-bridge.md` → vendor `intent-router.md` → smallest matching vendor route, then local execution |
| Raw/messy/one-line request — ALWAYS before implementation | `skills/request-reframe/SKILL.md` + fill `spec.md` (hard gate) |
| Unknown topic, on-screen facts, style references | `skills/web-research/SKILL.md` (≤8 sources, recorded) |
| Project >30 s, before final render | `skills/preview/SKILL.md` + `tools/preview.py` (approval unlocks render gate) |
| Disk/snapshot pressure, slow chats | `skills/performance/SKILL.md` + `tools/quota.py` |
|---|---|
| vague brief, missing constraints | `skills/intake/SKILL.md` |
| generic/weak concept, make it bold | `skills/ideate/SKILL.md` (creative bank + persona panel BEFORE directions) |
| voiceover/song supplied | `tools/transcribe.py` then `tools/sync_check.py` (mandatory both modes) |
| user works in After Effects | `tools/export_ae.py` bridge after final render |
| style identity, "make it creative", anti-template gate | `skills/creative-direction/SKILL.md` + run `tools/direct.py` |
| layer/timing/camera design | `skills/motion-direction/SKILL.md`, `catalog/choreography-recipes.md` |
| any Arabic on-screen text | `skills/arabic-type/SKILL.md` (mandatory before text animation) |
| photos, cutouts, charts, generated art | `skills/asset-craft/SKILL.md` |
| voiceover, music, singing interlude, sync | `skills/audio-sync/SKILL.md` |
| render slow, big job, flaky session | `skills/performance/SKILL.md` |
| crash, resume, "continue where we stopped" | `skills/recovery/SKILL.md` |
| QA, review loops, approval honesty | `skills/quality/SKILL.md` |
| publish, backup, storage budget | `skills/delivery/SKILL.md` |
| full documentary/film pipeline beyond this kit | vendor `ai-film-studio` engine selected by the bridge |

Mechanism lookup: `catalog/README.md` → `catalog/motions.json` → `reference/recipes/<mechanism>.md`. Style families and their honest boundaries: `catalog/dictionaries/styles.json`. Motion vocabulary for directions: `catalog/dictionaries/direction-axes.json`.

## Non-negotiable gates (details in AGENTS.md)

1. Original design per topic: reference learning is allowed, scene/template copying is not. `tools/check_directions.py` and `tools/check_project.py` enforce the paperwork; the aesthetic judgment is yours and must be written down.
2. Arabic shaping integrity: words/lines as shaped units; transforms on masks and layout, never fractured letters.
3. Capability honesty: implemented vs equivalent vs documented-only vs unsupported. No fake "After Effects" claims; the AE tool is not in this environment.
4. Deterministic rendering: `seek(t)` purity, checkpointed encode, per-part verification, PTS checks, reuse-unchanged-on-fix.
5. Evidence before "done": media checks, upload verification, journal entry, and explicit statement of what remains unverified.
6. Never store secrets in repo files; publishing is per-project and user-authorized.
7. Reframe gate first (no literal execution of chaotic briefs), research when the topic demands it, preview before long renders, deliver capped copies into the workspace via `tools/deliver.py`, and watch `tools/quota.py` — data loss and filled disks are contract violations.

## Deliverable shapes

- Draft/motion review: short MP4 at draft tier + ≤8-panel contact sheet (files, not chat blobs).
- Final: verified MP4 + manifest (frames/fps/duration/sha), `journal.jsonl`, updated `project.json`.
- Always report: what ran, what passed, what could not be verified here (e.g., no human ear on the mix), and the exact next command for the user or the next session.
