#!/usr/bin/env python3
"""Workspace quota guardian. Blocks the failure mode: 'disk/snapshot filled -> lost data/stuck chat'.
Run before renders and before writing any file >2MB; render.py and deliver.py consult it automatically.
verdict: ok | warn | block (exit 0/1/2)."""
import argparse, json, os, shutil, subprocess, sys
from pathlib import Path

EXCLUDE_DIRS = {'.git', 'node_modules', '__pycache__', '.cache', '.venv', 'dist', 'build', '.next', '.npm', '.local', '.pytest_cache', '.ruff_cache'}
SNAPSHOT_EXCLUDES = EXCLUDE_DIRS | {'deliverables'}  # deliverables counts too, but warn-only weights differ

def dir_bytes(root: Path, skip=EXCLUDE_DIRS) -> tuple[int, int]:
    total, largest, lp = 0, 0, None
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in skip]
        for f in fn:
            try: sz = os.path.getsize(os.path.join(dp, f))
            except OSError: continue
            total += sz
            if sz > largest: largest, lp = sz, os.path.join(dp, f)
    return total, (largest, lp)

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument('--root', default=str(Path.home()))
    ap.add_argument('--staging', default=str(Path.home() / '.cache/motion-forge-session'))
    ap.add_argument('--snapshot-limit-mib', type=float, default=118)
    ap.add_argument('--json', action='store_true'); a = ap.parse_args()
    root = Path(a.root)
    snap, (big_f, big_p) = dir_bytes(root, SNAPSHOT_EXCLUDES)
    total, _ = dir_bytes(root)
    disk = shutil.disk_usage(root)
    staging = Path(a.staging); stage_bytes = dir_bytes(staging)[0] if staging.exists() else 0
    mib = 1024 ** 2
    snap_mib, disk_pct, stage_mib = snap / mib, 100 * (disk.total - disk.free) / disk.total, stage_bytes / mib
    advisories = []
    if snap_mib > a.snapshot_limit_mib * 0.80:
        advisories.append('snapshot nearing limit: move heavy media to release assets/staging, keep only sources+small reports in workspace')
    if big_f and big_f > 40 * mib and big_p and '.cache' not in big_p:
        advisories.append(f'largest workspace file {big_mib if False else round(big_f/mib,1)} MiB at {big_p}; deliverables must stay capped (light<=25, hi<=50) and masters live in staging')
    verdict = 'ok'
    if snap_mib > a.snapshot_limit_mib: verdict = 'block'
    elif snap_mib > a.snapshot_limit_mib * 0.90 or disk_pct > 92: verdict = 'warn'
    if disk_pct > 96: verdict = 'block'
    if verdict == 'block':
        advisories.append('action: prune nothing of value — relocate render masters to staging (not snapshotted), deliver only capped copies, or ask user to clear deliverables already verified public')
    out = {'verdict': verdict, 'workspace_snapshot_mib': round(snap_mib, 1), 'workspace_total_mib': round(total / mib, 1),
           'snapshot_limit_mib': a.snapshot_limit_mib, 'disk_used_pct': round(disk_pct, 1), 'staging_mib': round(stage_mib, 1),
           'largest_file_mib': round(big_f / mib, 1) if big_f else 0, 'advisories': advisories}
    print(json.dumps(out, indent=2 if not a.json else None))
    return {'ok': 0, 'warn': 1, 'block': 2}[verdict]

if __name__ == '__main__':
    sys.exit(main())
