---
name: asset-craft
description: Build and verify the film's visual assets — cut-outs/mattes with edge QA, procedural charts and diagrams, generated imagery with honest provenance, shadows and mounts as independent layers. Use when creating or processing any image, illustration, chart, or texture for a project.
---

# Asset craft

## Rules
- Every asset ships with a provenance record appended to `assets/manifest.json`: `{file,kind:genuine|generated|illustrative|archival,source,author,license,sha256,mods}`. Check `tools/storage.py` before adding anything >2 MB; media goes to staging/Releases, never into the sources tree.
- Cut-outs: alpha edge QA on TWO backgrounds (dark+light) at 400% zoom — halos/fringing = re-matte (edge-contract 1px + feather 0.5 max). Feathered 3px halos on flat art = cheap tell.
- Shadows/mounts are SEPARATE layers derived from the silhouette (offset/blur/opacity independent params) whenever the design needs them to move or fade differently.
- Charts: geometry from the data table in code (no hand-placed bars); axis units recorded; entrance = per-element stagger with continuity rule `color-claim-link`.
- Generated imagery: prompts recorded; label `illustrative`; never pass invented historical texture as documentation (see originality).
- Vector motifs: build as parametric functions of `t` where they must animate; static SVG for hold art; trim-path strokes need the path object at runtime (not raster).

## Pipeline
1. Draft on the board (still frame at t=0 of its shot) → user sign-off if approval_mode requires.
2. Process in batches (PIL per-file loop, free memory between), write `assets/<id>.png|svg` + manifest entries, sha per file.
3. Wire into layer plan; matte QA still-frame via `--tier draft` micro-render (one chunk).
4. Memory discipline: no full-frame numpy stacks of >200 1080p images; stream. Images ≤4096px.

The kit's runtime has no asset loaders with network access by design — assets are local files, hashes locked into project state so renders can prove what they used.
