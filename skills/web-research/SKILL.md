---
name: web-research
description: Motion-design-specialized research agent — targeted digs into AE technique education, motion studios, 2026 trends, GitHub expression repos and Arabic type case studies, producing a mapped design-language brief, not generic browsing. Use for craft input, current trends, unfamiliar topics, or when output risks being template-flat.
---

# Web research (motion-craft focused — random browsing is a failure mode)

Mission: pull CREATIVE INTELLIGENCE into the project before design. Mandatory targets in priority order; skip none that match the project:

## Target registry (queries are patterns, adapt them)
1. **AE/motion technique education** — Video Copilot breakdowns, Ben Marriott / Portugal the Man / Mt. Mograph / ECAbrams / School of Motion writes: `after effects [technique] site:videocopilot.co.uk`, `kinetic typography [need] tutorial 2025 2026`, `ae expression [bounce|whip|wave|trim] explanation`. Extract the MECHANIC (math/behavior), map to kit primitive (`catalog/README.md`).
2. **GitHub open craft** — search `topic:after-effects-expressions`, `topic:motion-design` repos, expression collections, easing/physics gists; read CODE for formulas worth porting into `runtime/` usage (record as `maps_to: spring/trimPath/...` rows).
3. **Studios + current trends (production year)** — Buck/ManvsMachine/Ordinary Folk/Gimbal/Hello Monday behind-the-scenes & interviews; `motion design trends 2026 typography`, `editorial animation paper collage 2026`, Behance/Dribbble motion-branding boards — structure and behavior only, files are off-limits (originality gate).
4. **Arabic-specific** — Arabic rebrand idents, museum/cultural-festival motion case studies, foundry specimen pages for pairing inspiration; W3C alreq as the technical backstop. Any font that survives goes through `tools/fetch_font.py` (OFL only).
5. **Platform conventions** for the delivery surface (Reels/TikTok/YouTube/DOOH): native pacing, safe margins, muted-viewing conventions → feeds style.json camera/rhythm choices honestly.

## Deliverable (full mode ≥6 rows, quick ≥3)
`research/design-language.md` table:
`| source(url) | technique observed | maps to kit primitive/recipe | steal-rule | never-line |`
plus `research/facts.json` for anything appearing ON SCREEN: `{value, source_url, retrieved, confidence}` — unverified numbers are cut or labeled illustrative, never "approximated".

## Limits (they protect the session)
- ≤8 sources total; ≤2 follow-ups per thread; STOP when sources repeat each other — repeat findings = diminishing creativity, move to ideation.
- No bulk media downloads; one still only when a frame decides a choice; interviews/articles over raw scraping.
- Offline/blocked → write `design-language.md` header `mode: no-network` and proceed from kit dictionaries; research NEVER blocks the pipeline beyond one retry.
- Every borrowed idea must end as a MECHANIC row; "we liked their vibe" rows are rejected by the quality pass.

Feeds: `skills/ideate` (concepts + cliché blacklist check) and `tools/direct.py` (trend_questions field in output is your checklist).
