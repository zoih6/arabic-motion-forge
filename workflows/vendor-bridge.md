# Vendor Bridge — the single production spine

## Purpose

`vendor/ai-film-studio` is the upstream creative-production system. Arabic Motion Forge is the downstream Arabic-safe motion implementation and deterministic render system. They are not competing routers and must not be run as two separate projects.

For every request whose output includes a video, animation, motion graphic, reel, ad, explainer, short film, or kinetic typography, use this bridge before authoring scenes or prompts.

## Authority split

| Decision | Authority |
|---|---|
| User intent, scope, narrative promise, audience, platform, duration | `vendor/ai-film-studio/workflows/intent-router.md` + `M0-intake.md` |
| Creative direction, visual world, reference pack, continuity, storyboard, audio plan | `vendor/ai-film-studio` relevant route and engine |
| Arabic shaping, RTL, copy lock, type metrics, layer choreography, 2.5D/3D runtime | Arabic Motion Forge `skills/arabic-type`, `motion-direction`, `runtime/` |
| Deterministic rendering, checkpoints, quota, encoded-media QA, delivery | Arabic Motion Forge `tools/`, `skills/quality`, `performance`, `delivery` |
| Conflict | Preserve the user's requirement; use the stricter safety rule and record the conversion in `spec.md` and `vendor-bridge.json`. |

## Mandatory sequence

1. **Intake once.** Use `tools/intake.py` answers or direct-brief defaults. Never ask the same question again in vendor or local intake.
2. **Vendor route.** Read `vendor/ai-film-studio/SKILL.md`, then `workflows/intent-router.md`, then only the selected shortcut/engine and its `user-facing-production-flow.md` requirements.
3. **Create the upstream handoff in the project root.** Required files:
   - `vendor-bridge.json`
   - `production-brief.md` (or a project-local equivalent explicitly mapped to it)
   - `production-sheet.md` using `vendor/ai-film-studio/schemas/production-sheet.md`
   - `storyboard.md` for any multi-shot project; for a single shot, record the shot card in the production sheet
   - `reference-manifest.json` for recurring products, characters, locations, or style references; use `{}` with a reason when none are needed
   - `audio-plan.md` or an explicit `N/A` reason
4. **User checkpoint.** Present only the compact vision/plan required by the vendor user-facing protocol. Do not show internal agent names, raw research, or raw prompts. If the user asks to execute directly, record that approval and continue; do not invent an extra approval ceremony.
5. **Translate, do not restart.** Map the approved vendor artifacts into `brief.json`, `copy.txt`, `style.json`, `originality.json`, and `layer-plan.json`. Preserve IDs: `scene_id`, `shot_id`, `reference_ids`, timing, copy, and audio-map links.
6. **Arabic Motion Forge execution.** Load only the local skills required by the approved plan. Arabic text always goes through `arabic-type`; motion goes through `motion-direction`; assets/audio/quality/delivery are conditional but governed by their local contracts.
7. **Dual QA.** Run the applicable vendor gate for the route, then local `tools/gate.py`/`check_project.py`, motion audit, encoded-media checks, and delivery checks. A PASS in one system never substitutes for the other.
8. **Close the loop.** Append both vendor stage and local stage to `journal.jsonl`. `vendor-bridge.json` records the source commit/version, route, artifact hashes, local mapping, approvals, and any unresolved limitations.

## Routing map

- **Motion graphics / kinetic typography / ≤30s simple:** vendor `workflows/shortcuts/motion-graphics.md` + adaptive production sheet → local quick mode. Do not skip the vendor brief or production sheet.
- **Product ad / promo / brand film:** vendor E2 Commercial Engine; hybrid documentary ad uses E3 → local full mode.
- **Documentary / essay / faceless:** vendor E1 Documentary Engine → local execution for any Arabic motion, overlays, or deterministic assembly.
- **Scene with multiple shots:** vendor M0 → reference orchestration → storyboard/continuity/QC → local layer plan and render.
- **Series / bulk:** vendor E4/E5 → one local project per approved deliverable or a documented batch manifest.
- **Image-only or prompt-only requests:** use the vendor shortcut and do not create a local render project unless the user asks for video execution.

## Forbidden shortcuts

- Do not route a generic "make me a video" request directly to `direct.py`, `motion-direction`, or rendering.
- Do not read the whole vendor tree. Load the router, then the smallest matching route and references.
- Do not copy vendor examples or style locks into a new scene. Extract rules and author a new composition.
- Do not let vendor prompt conventions override Arabic shaping or local deterministic-render rules.
- Do not declare completion from a storyboard or prompt package; completion requires the local encoded-media and delivery gates when a rendered video was requested.

## Resume

On resume, read `vendor-bridge.json` and the journal tail first. Continue from the recorded handoff stage. Never re-run upstream ideation or re-ask approved answers unless a source artifact hash changed.
