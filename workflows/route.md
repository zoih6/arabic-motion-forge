# Production route (one page)

**Mandatory spine:** every video request first follows `workflows/vendor-bridge.md` → `vendor/ai-film-studio/workflows/intent-router.md` → the smallest vendor shortcut/engine. Only the approved handoff enters the Arabic Motion Forge route below. Vendor plans the production; this kit implements and verifies it.

```
RAW REQUEST ──► vendor bridge + intent-router ──► production-brief/sheet + refs + storyboard ──► request-reframe (spec.md) ──► web-research (bounded facts) ──► intake ──► direct.py (3 directions) ──► user picks ──► check_directions ──► style lock
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

The bridge handoff is a hard prerequisite for new projects: run `python3 tools/vendor_bridge.py init --project <dir>/project.json --route <vendor-route>`, author the required vendor artifacts, mark the vendor and local handoffs approved/ready, then run `python3 tools/vendor_bridge.py check --project <dir>/project.json` before local gates.
