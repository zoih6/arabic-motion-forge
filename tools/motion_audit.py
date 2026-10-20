#!/usr/bin/env python3
"""Objective superficiality detector — kills the 'photos + transitions' failure.
Samples frames from a render at ~6fps, measures WHERE motion happens (16-cell grid):
  * flat_ratio: % of sampled intervals with negligible whole-frame change
  * simultaneity: % of moving intervals where ALL 16 cells move together (global opacity/zoom = one flat motion)
  * layered_ratio: % of moving intervals with 2..13 active cells (independent element choreography)
  * burst count: motion events (entrances/exits) per 10s — a slideshow shows bursts only at cuts
Verdict: FAIL when flat>28% or layered<45% or (bursts/10s < scenes*1.2 and duration>6s).
Draft tier is fine — this audits MOTION DESIGN, not pixels."""
import argparse, json, subprocess, sys
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('video'); ap.add_argument('--fps', type=float, default=6.0)
    ap.add_argument('--json', action='store_true'); a = ap.parse_args()
    try:
        import av, numpy as np
        from fractions import Fraction
    except ImportError:
        raise SystemExit('needs av+numpy: python3 tools/bootstrap.py --install-render')
    v = Path(a.video)
    with av.open(str(v)) as c:
        s = c.streams.video[0]
        rate = float(s.average_rate or 32); stride = max(1, round(rate / a.fps))
        cells = np.zeros((4, 4), dtype=np.float64); prev = None
        flat = moving = layered = simult = 0; bursts = 0; was_moving = False; frames = 0
        flat_flags = []
        for i, fr in enumerate(c.decode(s)):
            if i % stride: continue
            from PIL import Image
            im = Image.fromarray(fr.to_ndarray(format='gray')).resize((128, 128))
            x = np.asarray(im, dtype=np.float32)
            if prev is not None:
                d = np.abs(x - prev); frames += 1
                moved = d.mean() > 1.1
                grid = np.stack([d[q*32:(q+1)*32, r*32:(r+1)*32].mean() for q in range(4) for r in range(4)])
                active = int((grid > 1.1).sum())
                if moved:
                    moving += 1
                    if active >= 15: simult += 1
                    if 2 <= active <= 13: layered += 1
                    if not was_moving: bursts += 1
                else:
                    flat += 1
                flat_flags.append(not moved)
                was_moving = moved
            prev = x
        # rhythm tolerance: isolated/short still runs (<=2 samples ~0.33s) are holds between beats, not dead air
        short_runs = 0; run = 0
        for f in flat_flags + [False]:
            if f: run += 1
            else:
                if 0 < run <= 2: short_runs += run
                run = 0
        flat = max(0, flat - short_runs)
        dur = frames / a.fps
    longest_run = rrun = 0
    for f in flat_flags:
        rrun = rrun + 1 if f else 0
        longest_run = max(longest_run, rrun)
    longest_flat_s = longest_run / a.fps
    flat_ratio = flat / max(1, frames); layered_ratio = layered / max(1, moving); simult_ratio = simult / max(1, moving)
    bursts10 = bursts / max(0.1, dur) * 10
    verdicts = []
    if longest_flat_s > 3.0: verdicts.append(f'longest_flat_run {longest_flat_s:.1f}s > 3.0s — extended dead air; short holds are rhythm, sustained stillness is slideshow')
    if flat_ratio > 0.55: verdicts.append(f'flat_ratio {flat_ratio:.0%} > 55% — most of the sampled film is static')
    if moving and layered_ratio < 0.45: verdicts.append(f'layered_ratio {layered_ratio:.0%} < 45% — motion is global fades/zooms, not independent layers')
    if moving and simult_ratio > 0.55: verdicts.append(f'simultaneity {simult_ratio:.0%} — almost all cells move together (single flat motion per scene)')
    if dur > 6 and bursts10 < 1.5: verdicts.append(f'motion events {bursts10:.1f}/10s < 1.5 — entrances/exits not choreographed')
    out = {'verdict': 'FAIL' if verdicts else 'PASS', 'seconds_sampled': round(dur, 2), 'frames_compared': frames,
           'flat_ratio': round(flat_ratio, 3), 'longest_flat_run_s': round(longest_flat_s, 2), 'layered_ratio': round(layered_ratio, 3),
           'simultaneity': round(simult_ratio, 3), 'motion_bursts_per_10s': round(bursts10, 2), 'issues': verdicts,
           'note': 'numbers guide taste; a PASS is necessary not sufficient — human eye still judges beauty'}
    print(json.dumps(out, ensure_ascii=False, indent=None if a.json else 2))
    return 1 if verdicts else 0

if __name__ == '__main__':
    sys.exit(main())
