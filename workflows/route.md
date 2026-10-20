# Production route (one page)

```
RAW REQUEST ──► request-reframe (spec.md, corrections logged) ──► web-research (bounded facts) ──► intake ──► direct.py (3 directions) ──► user picks ──► check_directions ──► style lock
   │                                                              │
   └ brief.json, copy.txt approved                          layer plan per shot
                                                                  │
     asset-craft ◄── (2.5D camera.json | true 3D via runtime/spatial.mjs + spatial-3d.json)──────────────────────────────── motion-direction authors scene
        (provenance, matte QA)                     (seek(t) purity, dictionaries)
                          \                       /
                           ▼                     ▼
                     draft-tier render ──► quality passes 1–2 ──► fixes (reuse verified parts)
                                                        │
                                        check_project ──► tools/preview.py ≤30s ──► USER APPROVES ──► final render (checkpoints) ──► quota-aware encode ──► audio mux
                                                                    │
                                             verification (frames/PTS/decode/LUFS) ──► tools/deliver.py (≤25/≤50MiB into workspace deliverables/) ──► publish (optional)
                                                                    │
                                              journal `final` line closes the loop
```

Rules that bind every arrow: AGENTS.md §2 (state contract), §5 (determinism), §8 (bounded QA), §9 (hygiene), §12 (closing checklist). Recovery at any arrow: `skills/recovery` — the journal tail tells you where you are.
