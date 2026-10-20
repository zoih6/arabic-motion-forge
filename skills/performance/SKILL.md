---
name: performance
description: Keep heavy sessions fast and alive — render throughput tuning, memory ceilings, context bloat control, output sampling, avoiding duplicate work. Use when renders are slow, chats get heavy/stuck, outputs balloon, or a machine feels on the edge of OOM.
---

# Performance

This kit has been hung and bloated chats before; these rules are the fix, not suggestions.

## Renders
- Tier discipline: never full-quality for review — `render.py --tier draft` (half-res, silent, crf28) first; final only after motion approved.
- Checkpoints: `--chunk-seconds 10` default; smaller chunks (4–6) on flaky hosts or when iterating a fix (only affected parts rebuild — entry hash in BUILD id detects staleness; reuse verified parts).
- Parallelism: one Chromium render process at a time; ffmpeg `-threads 2` set deliberately (host has ~2 GB RAM). Never launch a second renderer because the first "seems stuck" — check its log tail (`get_process_output` / logfile) instead.
- Background + wait pattern: start server/renderer with a process tool, then block on a log pattern/exit; never tight-poll, never re-issue timed-out commands unchanged.

## Memory (2 GB ceiling)
- Images: batch loops, `del` + not holding numpy stacks; frames stream to ffmpeg stdin (render.py already never writes PNGs).
- Audio/whisper: ≤60 s windows with refine passes (full-file whisper OOM-killed in this project — recorded dead end).
- Video probes: PyAV stream info only; `-f null` decode checks on final file only, timeout 600s.

## Context economy
- Tool outputs: `head -c`/`tail`, jq-style python for JSON, `wc` before reading; write big results to files, report path+hash+3-line summary.
- Present ONE file per reply; previews cost double — don't re-open the same render board repeatedly.
- No repeated identical tool calls; if a command fails twice, change approach, not the retry counter.
- Progress pings to the user: phase name + one number ("scene 5/8 drafted"), not narration of every step.

## Diagnose before optimizing
Suspected stall: (1) process alive? logs last lines? (2) disk free, snapshot size; (3) `storage.py`; (4) swap/OOM `dmesg | tail`. Fix the named cause; log it as journal `issue`.
