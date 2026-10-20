#!/usr/bin/env python3
"""One command instead of gate-ceremony: runs everything the mode demands, aggregates verdicts.
usage: python3 tools/gate.py <project>/project.json [--stage preview|final]
Quick mode (project.json mode:"quick") skips research requirements and heavy checks, never the safety ones."""
import argparse, json, subprocess, sys
from pathlib import Path
KIT = Path(__file__).resolve().parents[1]

def run(*cmd):
    r = subprocess.run(['python3'] + [str(x) for x in cmd], capture_output=True, text=True, timeout=1800)
    return r.returncode, (r.stdout + r.stderr)[-700:]

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument('project'); ap.add_argument('--stage', default='final', choices=['style', 'preview', 'final'])
    a = ap.parse_args(); pj = Path(a.project).resolve()
    cfg = json.loads(pj.read_text()); mode = cfg.get('mode', 'full'); results = {}; fails = 0
    need = {'style': ['directions', 'check'], 'preview': ['directions', 'check', 'audit?'], 'final': ['directions', 'check', 'sync?', 'audit?', 'compat']}
    if (pj.parent / 'directions.json').exists():
        rc, o = run(KIT / 'tools/check_directions.py', pj); results['directions'] = {'rc': rc, 'tail': o[-200:]}; fails += rc != 0
    rc, o = run(KIT / 'tools/check_project.py', pj); results['project'] = {'rc': rc, 'tail': o[-400:]}; fails += rc != 0
    if cfg.get('audio_file') or (pj.parent / 'audio-map.json').exists():
        rc, o = run(KIT / 'tools/sync_check.py', pj); results['audio_sync'] = {'rc': rc, 'tail': o[-300:]}; fails += rc != 0
    if a.stage == 'final':
        rep = pj.parent / 'render-report.json'
        if rep.exists():
            master = json.loads(rep.read_text()).get('output')
            if master and Path(master).exists():
                rc, o = run(KIT / 'tools/motion_audit.py', master, '--json'); results['motion_audit'] = {'rc': rc, 'tail': o[-300:]}; fails += rc != 0
        rc, o = run(KIT / 'tools/compat_check.py'); results['compat'] = {'rc': rc, 'tail': o[-160:]}; fails += rc != 0
    rc, o = run(KIT / 'tools/quota.py', '--json'); results['quota'] = {'rc': rc, 'tail': o[-160:]}
    verdict = {'passed': fails == 0, 'mode': mode, 'stage': a.stage, 'results': results, 'note': 'engineering gates PASS = necessary, not sufficient — beauty is judged on the contact sheet + motion_audit PASS together'}
    print(json.dumps(verdict, ensure_ascii=False, indent=2))
    return 0 if fails == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
