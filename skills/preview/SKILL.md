---
name: preview
description: Mandatory 30-second approval preview before any long production render — representative windows of every scene at draft tier, delivered as a small MP4 plus contact sheet for user sign-off. Use before final rendering on any project longer than 30 seconds; prevents 40-minute renders nobody approved.
---

# Preview gate (show-then-commit)

No project >30 s jumps to full-quality render. Sequence:

1. `python3 tools/preview.py --project <dir>/project.json` — auto-picks: hook window (first ~3.5 s) + one 1.2–2 s window per scene from `layer-plan.json` (mid-entrance moments where choreography is judgeable), capped at ~30 s total; renders them at draft tier; concatenates into `<dir>/deliverables/preview-<hash>.mp4` (typically 1–6 MB) + `preview-report.json` + contact-sheet PNG grid under `research/qa/`.
2. Present exactly ONE file to the user (the preview mp4) with a 3-line note: what's shown, what's NOT yet done (audio mix, untouched scenes), and the question: proceed / change what.
3. On approval: `python3 tools/preview.py --approve <dir>/project.json` writes `preview_approved:true` + journal line. Only then does final-tier rendering unlock (render.py enforces the gate for kit_contract≥2 long projects).
4. On rejection: fix the flagged scenes, re-run preview (only changed windows rebuild — window project hashes make unchanged ones cache-hits). Two revision rounds max before escalating the tradeoff to the user honestly.

The preview is the contract for "what will the film feel like" — motion, layering, typography behavior. Pixel-grade asset QA is NOT promised here (draft is half-res); say so in the same message.
