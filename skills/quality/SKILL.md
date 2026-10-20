---
name: quality
description: Bounded QA loops that actually catch defects — still-frame legibility, draft-tier motion review, encoded-media verification, continuity rule checks, honest reporting. Use after scenes exist and before declaring any render done; also use to triage user complaints about the film.
---

# Quality

Three passes MAX per version; each pass: measure → top-3 fixes → journal. Endless polish loops hang chats — bounded loops ship films.

## Pass 1 — stills (cheap, catches 40%)
Sample `seek()` frames: first frame, t=1.0s hook, each shot's in/mid/out, one frame at every transition midpoint. Inspect as ≤8-panel contact sheets (files under `research/qa/`, ≤480px panels). Checklist: Arabic shaping intact (final forms, lam-alef), diacritic clipping, text safe margins, contrast at 25% scale, unapproved text absent (render enforces copy.txt), element overlap accidents.

## Pass 2b — objective superficiality audit (both modes)
`python3 tools/motion_audit.py <draft.mp4>`: FAILS when longest_flat_run>3s (dead air), flat_ratio>55%, layered_ratio<45% (one global motion), simultaneity>55% (zoom-pulse film), <1.5 motion events/10s (no choreographed entrances). A slideshow of photos+transitions cannot pass — the user's complaint made mechanical. Fix = per-element keyframed behavior (motion-direction), re-audit, then proceed.

## Pass 2 — motion (draft tier)
`tools/render.py --tier draft` over windows around entrances/exits (2 s each, not the whole film at first). Review: per-layer independence visible? stagger readable, not mushy? camera depth ratio consistent (`camera.json`)? matte edges crisp (no AA crawl)? hold before cut ≥6f unless cutting on motion; continuity dictionary ids one by one (`continuity.json`).

## Pass 3 — the real file
On the final MP4: exact frame count, constant fps, decode-clean, audio streams + LUFS/TP numbers from `audio-sync`, determinism ping-pong on 3 timestamps, seek-time monotonicity. `render.py` asserts 1–3 of these already; PASS means the manifest says so — quote values, don't summarize vibes.

## Reporting style
"QA pass 2 found 3 issues (headline matte clipped at t=3.1, chart axis drift, camera ratio mismatch on scene 5); fixed via X/Y/Z; re-rendered scenes 2 and 5 only (hash-reuse kept the other 21 parts)." — that is a report. "Looks great!" is not.

Scorecards optional; every score needs the defect it caught listed.
