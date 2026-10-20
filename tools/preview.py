#!/usr/bin/env python3
"""30-second approval preview: representative draft windows per scene -> one small MP4 + contact sheet.
render.py's final gate (kit_contract>=2, duration>30s) unlocks only after --approve."""
import argparse, hashlib, json, subprocess, sys, time
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]

def pick_windows(cfg, plan, hook=3.5, per_scene=1.6, cap=30.0):
    fps = cfg['fps']; wins = []
    total = cfg['duration']
    scenes = plan.get('scenes', [])
    if scenes:
        wins.append(('hook', 0, min(hook, total)))
        step = 0
        for s in scenes:
            t0, t1 = float(s.get('start', 0)), float(s.get('end', 0))
            if t1 <= t0: continue
            mid = t0 + (t1 - t0) * 0.45  # entrance-forward: where choreography reads
            wins.append((s.get('id', f'S{len(wins)}'), round(mid, 3), round(mid + per_scene, 3)))
    # fall back: slice evenly
    if not wins: wins = [(f'W{i}', i * 5, min((i + 1) * 5, total)) for i in range(int(min(total, cap) // 5) + 1)]
    trimmed, acc = [], 0
    for w in wins:
        dur = min(w[2], total) - w[1]
        if acc + dur > cap: dur = max(0.5, cap - acc)
        if dur <= 0: break
        trimmed.append((w[0], w[1], round(w[1] + dur, 4))); acc += dur
        if acc >= cap: break
    return [(n, round(t0 * fps), round((t1 - t0) * fps)) for n, t0, t1 in trimmed]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('action_pos', nargs='?', choices=['approve'], help="approve marker (see --project)")
    ap.add_argument('--project', required=True); ap.add_argument('--approve', action='store_true')
    ap.add_argument('--out', default=None); a = ap.parse_args()
    pj = Path(a.project).resolve(); proj_dir = pj.parent
    cfg = json.loads(pj.read_text())
    if a.approve or a.action_pos == 'approve':
        cfg['preview_approved'] = True; cfg['preview_approved_at'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        pj.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + '\n')
        subprocess.run([sys.executable, str(KIT / 'tools/journal.py'), 'append', '--project', str(pj), '--event', 'review',
                        '--data', json.dumps({'gate': 'preview-approved', 'next': 'final render'})], check=False)
        print('preview_approved=true written'); return 0
    plan_path = proj_dir / cfg.get('layer_plan', 'layer-plan.json')
    plan = json.loads(plan_path.read_text()) if plan_path.exists() else {'scenes': []}
    wins = pick_windows(cfg, plan)
    stamp = hashlib.sha256((pj.read_text() + str([w[2] for w in wins])).encode()).hexdigest()[:8]
    out_dir = proj_dir / 'deliverables'; out_dir.mkdir(exist_ok=True)
    def av_ok(f):
        try: return f.stat().st_size > 1000 and f.read_bytes()[:12].find(b'ftyp') != -1
        except OSError: return False
    entry_sha = hashlib.sha256(Path(cfg['entry'] if Path(cfg['entry']).is_absolute() else proj_dir / cfg['entry']).read_bytes()).hexdigest()[:8]
    parts, used = [], 0.0
    for name, start_f, count in wins:
        wid = f'{name}-{start_f}'
        # persistent cache key: window spec + source entry build — unchanged scenes never re-render
        out_mp4 = proj_dir / 'preview' / f'cache-{wid}-{entry_sha}-{hashlib.sha256(str((start_f, count, cfg["fps"])).encode()).hexdigest()[:6]}.mp4'
        out_mp4.parent.mkdir(parents=True, exist_ok=True)
        if out_mp4.exists() and av_ok(out_mp4):
            parts.append(out_mp4); used += count / cfg['fps']; continue
        win_cfg = dict(cfg); win_cfg.update({'frames': int(count), 'duration': int(count) / cfg['fps'],
            'requested_duration': int(count) / cfg['fps'], 'id': cfg['id'] + '-preview', 'render_allowed': True})
        # the window project lives in a subdir: re-anchor all relative project paths to the real project root
        for key in ('entry', 'layer_plan', 'copy_file', 'style_file', 'originality_file', 'spec_file'):
            if win_cfg.get(key) and not Path(win_cfg[key]).is_absolute():
                win_cfg[key] = str((proj_dir / win_cfg[key]).resolve())
        wproj = proj_dir / 'preview' / f'project-{wid}.json'; wproj.parent.mkdir(exist_ok=True)
        wproj.write_text(json.dumps(win_cfg))
        cmd = [sys.executable, str(KIT / 'tools/render.py'), '--project', str(wproj), '--tier', 'draft',
               '--start-frame', str(start_f), '--workspace-root', str(Path.home()), '--work-suffix', f'prev-{wid}']
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        rep = wproj.parent / 'render-report.draft.json'
        if r.returncode != 0 or not rep.exists():
            print(f'window {name} failed:\n{r.stdout[-400:]}\n{r.stderr[-400:]}', file=sys.stderr); return 1
        parts.append(Path(json.loads(rep.read_text())['output'])); used += count / cfg['fps']
        out_mp4.write_bytes(parts[-1].read_bytes())
    listfile = out_dir / f'.preview-{stamp}-list.txt'
    listfile.write_text('\n'.join(f"file '{p.as_posix()}'" for p in parts) + '\n')
    final = Path(a.out) if a.out else out_dir / f'preview-{stamp}.mp4'
    import os
    ff = None
    try:
        import imageio_ffmpeg; ff = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception: pass
    if ff is None: ff = subprocess.run(['which', 'ffmpeg'], capture_output=True, text=True).stdout.strip()
    if not ff: raise SystemExit('no ffmpeg available; run tools/bootstrap.py --install')
    subprocess.run([ff, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', str(listfile),
                    '-c', 'copy', '-movflags', '+faststart', str(final)], check=True)
    for p in out_dir.glob(f'.preview-{stamp}-*.mp4'): p.unlink(missing_ok=True)
    listfile.unlink(missing_ok=True)
    # prune stale window caches older than the newest 24
    caches = sorted(out_mp4.parent.glob('cache-*.mp4'), key=lambda x: x.stat().st_mtime, reverse=True)
    for x in caches[24:]: x.unlink(missing_ok=True)
    meta = {'file': str(final), 'bytes': final.stat().st_size, 'windows': len(wins),
            'duration_shown': round(used, 2), 'sha256': hashlib.sha256(final.read_bytes()).hexdigest()}
    (out_dir / 'preview-report.json').write_text(json.dumps(meta, indent=2))
    subprocess.run([sys.executable, str(KIT / 'tools/journal.py'), 'append', '--project', str(pj), '--event', 'review',
                    '--data', json.dumps({'gate': 'preview-rendered', **{k: meta[k] for k in ('file', 'bytes', 'windows')}})], check=False)
    print(json.dumps(meta))
    print('NEXT: present the preview file to the user; on approval run: python3 tools/preview.py --approve ' + str(pj))
    return 0

if __name__ == '__main__':
    sys.exit(main())
