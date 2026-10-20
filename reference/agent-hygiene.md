# Agent session hygiene (why this exists)

Real failures in v1 sessions: chats growing heavy and stalling; duplicated renders; giant logs pasted into context; a whisper pass OOM-killing the box; "is it done?" ping-pong while a foreground loop ran. The rules are cheap insurance:

1. **Background + wait, never foreground grind.** Servers/renders start detached; block on a pattern/port/exit; timed-out commands get diagnosed, not blindly rerun.
2. **One renderer at a time.** A slow log line is not a hang; read it before assuming.
3. **Sample, don't dump.** `head`/`tail`/counts into context; full outputs to files with path+sha reported. No base64 images in chat.
4. **Journal every milestone** (`tools/journal.py`) — the tail is the resume point; new sessions pay ~2 reads, not a re-do.
5. **Bounded loops.** 3 QA passes max per version, top-3 issues each; draft tier for motion review; only rebuild parts whose sources changed.
6. **Memory: stream.** 60 s audio windows, per-frame pipes, no full-video arrays; check `tools/storage.py` before >5 MB writes.
7. **Progress reporting:** phase + number ("scene 5/8"), not step-by-step narration.
