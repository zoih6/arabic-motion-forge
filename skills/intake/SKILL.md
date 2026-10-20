---
name: intake
description: Extract and complete a film brief from vague user requests. Use when the ask is fuzzy ("make it creative about X"), when constraints (duration, format, voice, approval style) are missing, or before style lock. Produces brief.json and an approval plan.
---

# Intake

Goal: enough constraints to design, without interrogating the user like a form.

- **First-touch protocol (fresh skill, no project):** `python3 tools/intake.py --emit` → render greeting + its 5 option-questions via the host's question tool (AskUserQuestion in Claude Code) or numbered inline — this IS the whole first reply. On answers: `intake.py --record '<json>' --name <p> --dest <dir>` → project+brief scaffolded, reply with its `one_line`. User sent a task instead: `intake.py --defaults --text '<msg>'` auto-derives duration/platform/type; ask at most one blocking follow-up. Never re-ask a derived fact.
- Mid-project or after intake: ask at most one round of 3–4 questions, only for facts you cannot responsibly infer: purpose, audience, aspect/duration hard limits, whether real voices/music/photos are supplied, approval mode (board first / trust-and-review / silent-final), deadline pressure.
- Everything inferable goes into `brief.json` as explicit assumptions the user can veto in one word. Mark them `"assumed": true`.
- Copy: collect all on-screen text verbatim into `copy.txt` lines + `brief.approval` stays `pending` until the user confirms wording. Wording changes later = re-hash copy and re-run check_project (render.py refuses mismatched hashes).
- Reference media the user links: record in `brief.references` with what is being studied (structure? palette attitude? pacing?) and what must NOT be copied. Study concepts via AGENTS rules; do not download their films to inspect frames.
- Constraints honestly logged: aspect/format (1920×1080@32 vs 1080×1920@32 default vertical), sound design expectation, delivery destination, privacy limits on tokens.
- Missing voice/music? Note that `audio-sync` can only sync to real audio; silent films get rhythm from motion only. Never fake "we'll fix audio in post" energy.
- Close: journal `{"kind":"brief","assumptions":N,"open":M}`, then route to `creative-direction`.
