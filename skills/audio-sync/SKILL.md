---
name: audio-sync
description: Sync motion to real audio — narration word/phoneme timing, music beat maps, sung inserts replacing narration spans, LUFS/true-peak targets, frame-quantized cuts. Use whenever voice or music drives timing or when the edit must preserve/replace spoken content.
---

# Audio sync

Source of truth = the audio FILE, measured, never guessed.

1. **Analysis via the tool, not ad-hoc whisper.** `python3 tools/transcribe.py <audio> --project <dir> [--text copy.txt]`: windowed 56 s (full-file OOM lesson encoded), word timestamps, confidence floor 0.55 to `trusted`, cache keyed by (audio sha, model, lang); `--text` ALIGNS to approved strings and reports drift_ratio. Raw ASR NEVER appears on screen; approved copy owns the glyphs, the map owns the timing. Music: onsets/beat grid (librosa or ffmpeg silencedetect+energy comb; record method in research JSON). Store `audio-map.json`: `{words:[{t0,t1,text}], beats:[...], energy:[...]}` with source sha256.
2. **Lock.** Entrances land on word onsets or beat multiples (±1 frame tolerance asserted in QA `audio-visual-phase`). Narration-driven films: motion timeline derived from word times; music only ducks under voice (measure, don't vibe).
3. **Replacements/inserts** (e.g., a sung passage over a spoken span): exact source in/out points in `audio-map.json`; narration silenced for the span; original files untouched (build new mix via ffmpeg filter graph, keep splice map).
4. **Frame-quantize.** All cut points = k/fps seconds; mix sample rate locked (48k); master loudness on the ENCODED file: target −14 LUFS I, TP ≤ −1.5 dBTP, report measured values honestly; loudness via ffmpeg `loudnorm=print_format=json` two-pass or ebur128.
5. **Mux.** render.py streams per-part AAC from the same master — never mux a separate full-length mix against concat (drift); if replacing mux after, re-run PTS audit.
6. Agent honesty: you cannot listen. "Sounds good" is not a report — deliver the numbers (LUFS, TP, duration deltas, onset deltas), spot-check spectrograms around splices for clicks (energy spike >12dB at boundary = 2ms fade-in/out), and say what only a human can confirm.
