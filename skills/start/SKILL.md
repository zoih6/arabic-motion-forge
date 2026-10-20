---
name: start
description: Entry point when a motion/video request arrives or a session resumes with this kit. Use to reach a running project state fast: bootstrap check, journal read, route selection. First action for any new conversation using Arabic Motion Forge.
---

# Start

1. Kit present? `python3 tools/doctor.py` → one JSON verdict. If absent, AGENTS.md §0 bootstrap (<60 s). Never clone history or fetch media "to look around".
2. Existing project? `python3 tools/journal.py stats --project <dir>/project.json` + read `project.json`/`brief.json`. Resume at the recorded `next`; do not re-ask settled questions, do not re-render verified parts (compare `render-report.json` build hash first).
2b. Setup/bootstrap turns: reply with the AGENTS §0 template ONLY (install.sh already prints the single `MOTION FORGE READY` line — quote that, nothing else). doctor/bootstrap logs live in `~/.cache/motion-forge-session/bootstrap.log`; tail it when a render is about to start, never in chat.
3. New brief? ≤30 s or simple → `new_project.py --quick`. Route: unclear → `intake`; weak/generic concept → `ideate` FIRST; then `creative-direction`; audio → `tools/transcribe.py`; scenes via `motion-direction` (+ `arabic-type` if Arabic), assets (`asset-craft`), audio (`audio-sync`).
4. Session budgeting (prevents heavy/hung chats): plan phases up to the next natural checkpoint; keep tool output samples small; heavy renders in background with `get_process_output`-style waits; one presentable file per reply.
5. Before ANY render: `python3 tools/gate.py <dir>/project.json` — one aggregated verdict; `render_allowed:true` only after user sees direction+first-frame approval (or explicitly waives).
6. Long or risky work: say the phase you are in once, do the phase, journal it. If interrupted, the journal is the handoff — close with the exact next command.
