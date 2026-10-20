#!/usr/bin/env python3
"""Capped delivery extraction into the WORKSPACE (never out/, never lost between sessions).
Takes the verified master from staging and writes: light copy ≤25 MiB (720p-class) + hi copy ≤50 MiB.
Probes frame/duration parity, records sha256, journals the result. If the session dies mid-pipeline,
masters in staging can still be assembled — this tool is the safe landing strip."""
import argparse, hashlib, json, subprocess, sys, shutil
from pathlib import Path

def ffexe():
    try:
        import imageio_ffmpeg; return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        w = subprocess.run(['which', 'ffmpeg'], capture_output=True, text=True).stdout.strip()
        if not w: raise SystemExit('ffmpeg missing: python3 tools/bootstrap.py --install')
        return w

def probe(ff, path):
    r = subprocess.run([ff, '-i', str(path)], capture_output=True, text=True)
    import re
    line = next((l for l in r.stderr.splitlines() if 'Duration' in l), '')
    dur = re.search(r'Duration: (\d+):(\d+):(\d+\.?\d*)', line)
    v = re.search(r'(\d{2,5})x(\d{2,5})', r.stderr)
    return {'duration_s': sum(float(dur.group(i)) * (60 ** (2 - i)) for i in (1, 2, 3)) if dur else 0,
            'w': int(v.group(1)) if v else 0, 'h': int(v.group(2)) if v else 0}

def encode(ff, src, dst, *, max_mib, height, crf_min=26, label):
    dur = max(probe(ff, src)['duration_s'], 0.5)
    kb = max_mib * 1024 * 1024 * 8 / dur * 0.94
    vbr = int(kb) - 128  # 128k audio
    if vbr < 200: raise SystemExit(f'{label}: duration too long for budget; raise budget or cut the film')
    cmd = [ff, '-y', '-v', 'error', '-i', str(src), '-vf', f'scale=-2:{height}', '-c:v', 'libx264',
           '-b:v', str(vbr), '-maxrate', str(int(vbr * 1.45)), '-bufsize', str(vbr * 2), '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', str(dst)]
    subprocess.run(cmd, check=True)
    if dst.stat().st_size > max_mib * 1024 * 1024:  # 2-pass tighten
        cmd = [ff, '-y', '-v', 'error', '-i', str(src), '-vf', f'scale=-2:{height}', '-c:v', 'libx264',
               '-b:v', str(int(vbr * 0.8)), '-maxrate', str(int(vbr * 1.1)), '-bufsize', str(int(vbr * 1.6)),
               '-crf', str(crf_min), '-pix_fmt', 'yuv420p', '-preset', 'medium',
               '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', str(dst)]
        subprocess.run(cmd, check=True)
    if dst.stat().st_size > max_mib * 1024 * 1024:
        dst.unlink(missing_ok=True); raise SystemExit(f'{label}: cannot fit {max_mib}MiB at {height}p; lower height request')
    # decode sanity
    dec = subprocess.run([ff, '-v', 'error', '-i', str(dst), '-f', 'null', '-'], capture_output=True, text=True, timeout=900)
    if dec.returncode != 0: raise SystemExit(f'{label}: decode check failed: {dec.stderr[-300:]}')
    return {'file': str(dst), 'bytes': dst.stat().st_size, 'sha256': hashlib.sha256(dst.read_bytes()).hexdigest(),
            'max_mib': max_mib, 'height': height}

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument('project_json'); ap.add_argument('--master', default=None)
    ap.add_argument('--light-mib', type=float, default=25); ap.add_argument('--high-mib', type=float, default=50)
    ap.add_argument('--light-height', type=int, default=720); a = ap.parse_args()
    pj = Path(a.project_json).resolve(); proj_dir = pj.parent
    cfg = json.loads(pj.read_text())
    out = proj_dir / 'deliverables'
    if out.name == 'out' or 'out' in out.parts:
        raise SystemExit('deliverables must live under <project>/deliverables — out/ directories are lost between sessions')
    master = Path(a.master) if a.master else None
    if master is None:
        rep = proj_dir / 'render-report.json'
        if not rep.exists(): raise SystemExit('no render-report.json; pass --master /path/to/master.mp4')
        master = Path(json.loads(rep.read_text())['output'])
    if not master.exists():
        raise SystemExit(f'master {master} missing; if the render died after checkpoints, run the merge first or pass a verified part set')
    out.mkdir(parents=True, exist_ok=True)
    ff = ffexe()
    hi_src = master
    hi_size = master.stat().st_size / 1024 ** 2
    hi = proj_dir / 'deliverables' / f"{cfg['id']}-hi.mp4"
    if hi_size <= a.high_mib:
        shutil.copy2(master, hi)
        hi_rec = {'file': str(hi), 'bytes': hi.stat().st_size, 'sha256': hashlib.sha256(hi.read_bytes()).hexdigest(),
                  'max_mib': a.high_mib, 'height': probe(ff, hi)['h'], 'source': 'master-direct'}
    else:
        hi_rec = encode(ff, master, hi, max_mib=a.high_mib, height=cfg['height'], label='hi') | {'source': 're-encoded'}
    lt = proj_dir / 'deliverables' / f"{cfg['id']}-light.mp4"
    lt_rec = encode(ff, master, lt, max_mib=a.light_mib, height=a.light_height, label='light')
    # parity
    pm, pl = probe(ff, master)['duration_s'], probe(ff, lt)['duration_s']
    if abs(pm - pl) > 0.3: raise SystemExit(f'duration drift light({pl}) vs master({pm})')
    result = {'master': str(master), 'light': lt_rec, 'high': hi_rec,
              'master_mib': round(hi_size, 2), 'policy': 'workspace deliverables; no out/; light<=25MiB hi<=50MiB'}
    (out / 'delivery.json').write_text(json.dumps(result, indent=2))
    subprocess.run([sys.executable, str(Path(__file__).parent / 'journal.py'), 'append', '--project', str(pj),
                    '--event', 'final', '--data', json.dumps({'delivery': 'capped-copies-written', **{k: lt_rec[k] for k in ('bytes', 'sha256')}})], check=False)
    print(json.dumps(result, indent=2))
    return 0

if __name__ == '__main__':
    sys.exit(main())
