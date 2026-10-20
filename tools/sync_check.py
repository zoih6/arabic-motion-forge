#!/usr/bin/env python3
"""Sync verification: proves word entrances in the layer plan actually match measured onsets.
Every scene layer may declare: "word_sync": [{"text": "...", "t": 12.34}].
Fails if: no audio-map.json; map stale (sha mismatch vs project audio); any declared word time
deviates > tol frames from the nearest matching word in the map; or a claimed word doesn't exist
in the map at all. Exit nonzero = do not render."""
import argparse, hashlib, json, re, sys
from pathlib import Path

def norm(s): return re.sub(r'\W+', '', s or '', flags=re.UNICODE).lower()

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument('project_json')
    ap.add_argument('--tol-frames', type=float, default=1.2); a = ap.parse_args()
    pj = Path(a.project_json).resolve(); root = pj.parent; cfg = json.loads(pj.read_text())
    fps = cfg['fps']
    map_path = next((p for p in [root / 'audio-map.json', root / 'research/audio-map.json'] if p.exists()), None)
    if not map_path: raise SystemExit('SYNC FAIL: audio-map.json missing — run tools/transcribe.py on the audio first')
    am = json.loads(map_path.read_text())
    audio = cfg.get('audio_file')
    if audio:
        p = (root / audio) if not Path(audio).is_absolute() else Path(audio)
        if p.exists():
            h = hashlib.sha256(); h.update(p.read_bytes())
            if am.get('source_sha256') and am['source_sha256'] != h.hexdigest():
                raise SystemExit('SYNC FAIL: audio-map is stale (audio file changed since transcription)')
    plan = json.loads((root / cfg['layer_plan']).read_text())
    words = am.get('trusted') or am.get('words') or []
    errors, checked, worst = [], 0, (0.0, None)
    for sc in plan.get('scenes', []):
        for lay in sc.get('layers', []):
            for w in lay.get('word_sync', []):
                checked += 1
                tgt = norm(w.get('text'))
                cands = [x for x in words if norm(x['text']) == tgt]
                if not cands:
                    errors.append(f"{sc.get('id')}/{lay.get('id')}: word '{w.get('text')}' not found in audio map"); continue
                t = float(w['t']); best = min(cands, key=lambda x: min(abs(x['t0'] - t), abs(x['t1'] - t)))
                err = min(abs(best['t0'] - t), abs(best['t1'] - t))
                if err > worst[0]: worst = (err, f"{sc.get('id')}/{lay.get('id')}:{w.get('text')}")
                if err > a.tol_frames / fps:
                    errors.append(f"{sc.get('id')}/{lay.get('id')}: '{w.get('text')}' planned {t:.3f}s vs measured {best['t0']:.3f}/{best['t1']:.3f}s (Δ{err*fps:.1f}f)")
    if checked == 0:
        raise SystemExit('SYNC FAIL: audio project but zero word_sync declarations — every word entrance must cite the map')
    if errors:
        print('SYNC FAIL:\n- ' + '\n- '.join(errors[:25]), file=sys.stderr); return 1
    print(json.dumps({'passed': True, 'words_checked': checked, 'worst_delta_frames': round(worst[0] * fps, 2),
                      'worst_at': worst[1], 'map': str(map_path), 'trusted_words': len(words)}))
    return 0

if __name__ == '__main__':
    sys.exit(main())
