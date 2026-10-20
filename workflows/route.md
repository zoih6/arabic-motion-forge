# Production route (one page)

```
intake ──► direct.py (3 directions) ──► user picks ──► check_directions ──► style lock
   │                                                              │
   └ brief.json, copy.txt approved                          layer plan per shot
                                                                  │
     asset-craft ◄────────────────────────────────── motion-direction authors scene
        (provenance, matte QA)                     (seek(t) purity, dictionaries)
                          \                       /
                           ▼                     ▼
                     draft-tier render ──► quality passes 1–2 ──► fixes (reuse verified parts)
                                                        │
                                        check_project ──► final render (checkpoints) ──► audio mux
                                                                    │
                                             verification (frames/PTS/decode/LUFS) ──► delivery/publish
                                                                    │
                                              journal `final` line closes the loop
```

Rules that bind every arrow: AGENTS.md §2 (state contract), §5 (determinism), §8 (bounded QA), §9 (hygiene), §12 (closing checklist). Recovery at any arrow: `skills/recovery` — the journal tail tells you where you are.
