---
name: web-research
description: Bounded web research agent role — gather topic facts, style techniques, Arabic typography findings and reference rules BEFORE design, so the film is informed by real knowledge instead of assumptions. Use when the topic is unfamiliar, the user names reference styles/videos, or fact-checking on-screen claims is required.
---

# Web research (bounded, evidence-shaped)

Mission: build the knowledge the brief lacks — cheaply, with citations, in ≤8 sources, ~10 minutes, never as a procrastination loop.

## What to search (per project, in order)
1. Topic facts that will APPEAR on screen: numbers, dates, names — one search per claim class, prefer primary/official sources; any figure going on screen gets `{value, source_url, retrieved}` in `research/facts.json`. Unverified numbers are cut or labeled illustrative — never "approximated".
2. Craft techniques: "[subject] motion design technique", "[reference studio] process breakdown", "arabic kinetic typography [specific need]" — harvest 2–4 transferable RULES (sentences), not files. Log to `research/notes.md` with URL.
3. Style/reference media the user linked: fetch the interview/article ABOUT it (not the raw video); record "steal/never" lines in the SAME shape as `catalog/dictionaries/styles.json`. If the user attached a reference video file: analyze structurally (shot lengths via ffprobe, motion cadence from sampled frames ≤16) — describe, don't copy.
4. Fonts/assets if needed: license-checked sources only (OFL/SIL, clearly public-domain); record sha + license before use.

## Hard limits (they protect the session)
- ≤8 sources total, ≤2 searches per sub-question; stop when answers repeat.
- No bulk media download; thumbnails/screenshots only when a single still decides a design choice — save to research/, never into deliverables.
- Every fact used on screen must trace to `facts.json`; the quality pass spot-checks two numbers.
- Offline or blocked network: declare it in the spec's Constraints ("research unavailable; proceeding on kit knowledge") and continue — never stall the pipeline waiting on web.

Output: `research/notes.md` (3–8 bullets + URLs) + `facts.json` referenced by spec.md `## Content & copy`. These feed tools/direct.py's topic vocabulary and make rationales substantive (check_directions counts topic-token grounding — real facts help pass honestly, not by padding).
