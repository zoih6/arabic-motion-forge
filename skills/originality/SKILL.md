---
name: originality
description: Keep every output a new design: learn from references without copying scenes, compositions, or another project's files. Use whenever prior work, example projects, or third-party films are involved, and before approving any "reuse this layout" instinct.
---

# Originality

- The kit's `examples/vertical-showcase` is a CONTRACT demonstration, not a style. Its scene code, palette, motif and beats are protected: `check_directions.py` collides any direction whose axis fingerprint matches it. Same rule applies to the user's previous delivered projects — pass them via `--against`.
- Learning a reference = extracting a transferable rule ("occluder wipe ties two eras") written into `originality.json.reference_lessons` as prose. Copying = importing/re-typing their layer timings, asset layouts, or bespoke shapes — that path ends here.
- New projects start empty by design (new_project.py refuses to seed). If a mechanism from another project genuinely applies, re-implement it from `runtime/` primitives and cite the runtime file, not the project file.
- Generated art/photos are "illustrative" never "authentic"; `asset-craft` records provenance. Historical footage/images need license evidence or explicit fair-use reasoning stored with the asset.
- `originality.json` final state required by check_project: `declared_new_composition:true`, non-empty lessons AND differences, zero copied scene imports (grep-verified against `examples/` and known project paths).
- If the user requests "same style as X", clarify: same FEELING (allowed — re-derive via directions engine) vs same FILES (refuse, explain, offer the derivation).
