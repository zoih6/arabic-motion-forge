---
name: recovery
description: Resume interrupted, crashed, or context-truncated sessions without duplicating work or losing state. Use when continuing after an error, a new chat about an ongoing project, a killed render, or an unclear "did it finish?" situation.
---

# Recovery

The invariant: state lives in files, not in the chat. If you can't see it in a file, it didn't happen.

## Resume protocol
1. `python3 tools/journal.py tail --project <dir>/project.json --n 15` — the tail IS the state machine.
2. Read the last `render-part`/`final` lines; open the matching `render-report.json` (or `render-report.draft.json`) and compare `build` hash against current `sha256(entry+project.json)` recomputed — mismatch means sources changed: only then re-render affected parts.
3. `RENDER_PAUSED` in logs → read the report's `error`, fix that specific thing, restart the SAME command; render.py resumes per checkpoint only by skipping existing verified parts if invoked with the same BUILD — otherwise it restarts the current BUILD id (new hash) which is safe by design.
4. Upload jobs: `research/repository.json`/publisher queue states decide whether an asset is public; never re-push blindly — publisher refuses existing names, then version yours.
5. New chat mid-project: start from `skills/start`, do the two file reads above, and TELL the user which step you resume at in one line before working.

## Never do on recovery
- Re-ask the user questions already answered (brief.json/directions approval is the record).
- Re-render a segment whose part file exists with matching sha in the report.
- Re-run a timed-out identical command without changing inputs.
- Assume the previous session failed because output is missing from YOUR context — it's on disk; go look.

## If the host/chat UI itself hangs
Write `journal.jsonl` append `{"kind":"handoff","next":"<exact command>"}` is impossible from a frozen session, so PRE-LOG: after every milestone the agent appends `next:<command>` (journal.py makes it cheap). A hung chat then costs nothing: next session reads tail and continues.
