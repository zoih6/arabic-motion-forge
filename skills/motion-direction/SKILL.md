---
name: motion-direction
description: Design and implement AE-grade layered choreography — decomposition into independent elements, three-stage keyframe timing, mattes, trim reveals, multi-plane camera, motivated transitions. Use for every shot's actual motion design, after style lock and before rendering.
---

# Motion direction

One flat motion across a whole scene is a defect. Work per shot through the loop: **decompose → assign behavior → time → ease → blur policy → verify.**

## Decompose (layer plan first)
- `layer-plan.json`: every shot lists layers with `role, channels[], in, out, parent(depth), matte?, blur_samples?`. Words, underlines, figures, mounts, shadows, counters, texture = separate entries whenever their narrative behavior differs. Bake nothing that later needs independent motion.
- Parenting = depth (`layerState` + camera projection from `runtime/core.mjs`), not convenience grouping.

## Behavior vocabulary (implemented — cite the primitive)
- Entrances: `spring/springPresets`, `ballistic`, `inertia`, `cubicBezier` ports of AE curves; `stagger` over word/line units (never Arabic characters).
- Reveals: arc-length `trimPath` (`pathTrim` + `pathPointAt` for head markers), RTL/iris/luma mattes (`runtime/canvas.mjs`), shape `morph` only with real correspondence (`flubber`-class rules; guard throws otherwise).
- Texture: `quantize` 8–12fps on element transforms for tactile feel while camera stays smooth; `squashStretch`, `followThrough`, `recoil`; shutter `shutterTimes` for motion blur sampling.
- Dictionaries: `catalog/dictionaries/easings.json` (what exists + when each reads cheap), `camera.json` (projection + anti-default), `continuity.json` (rules QA will run).
- Recipes with working code contracts: `reference/recipes/<mechanism>.md` — grep `catalog/README.md` first; never invent an API — `node -e "import('./runtime/core.mjs').then(m=>console.log(Object.keys(m)))"` lists truth.

## Timing law
- Every animated property: explicit keyframe array or analytic fn + named easing; multi-key where real (anticipation→move→settle). Overlap in/out across layers by design; simultaneous everything = dead board.
- Holds carry meaning; ≥6 frames settle before cuts unless cutting on motion.
- Text entrance pattern for Arabic: shaped whole-word blocks revealed by moving mattes/clip bands, or per-word `stagger` on position+opacity — mask moves, glyph stays intact.

## Verification (per shot, before moving on)
- `seek(t)` sanity at in/out/mid + determinism ping-pong (same t twice → identical digest).
- Draft tier: `python3 tools/render.py --project <dir>/project.json --tier draft` for the shot window (`--chunk-seconds` small); inspect ≤8 contact panels at file level — check per-layer separation (elements out-of-phase), no popping, matte edges, camera depth ratios.
- Fix top-3 issues, journal `scene` events with what changed. Two passes max per shot, then trust numbers, move on — polish loops kill chats.
