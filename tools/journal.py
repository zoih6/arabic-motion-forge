#!/usr/bin/env python3
"""Append-only project journal: the anti-hang / crash-resume backbone.
Every milestone, render part, upload, review pass, and hand-off decision is one
JSONL line; resuming sessions read the tail instead of re-asking or re-running."""
import argparse, json, sys, time
from pathlib import Path

REQUIRED_KINDS = {'boot', 'brief', 'directions', 'style-lock', 'asset', 'scene', 'render-part', 'upload', 'review', 'issue', 'handoff', 'final', 'note'}

def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')

def journal_path(project_json: Path) -> Path:
    return (project_json if project_json.is_dir() else project_json.parent) / 'journal.jsonl'

def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('append'); a.add_argument('--project', required=True); a.add_argument('--event', required=True); a.add_argument('--data', default='{}')
    t = sub.add_parser('tail'); t.add_argument('--project', required=True); t.add_argument('--n', type=int, default=12)
    s = sub.add_parser('stats'); s.add_argument('--project', required=True)
    args = ap.parse_args()
    pj = Path(args.project)
    if pj.name != 'project.json':
        pj = pj / 'project.json'
    jp = journal_path(pj)

    if args.cmd == 'append':
        if args.event not in REQUIRED_KINDS:
            print(f'unknown event kind {args.event!r}; allowed: {sorted(REQUIRED_KINDS)}', file=sys.stderr); return 2
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError as e:
            print(f'--data must be JSON: {e}', file=sys.stderr); return 2
        line = {'ts': now(), 'kind': args.event, **data}
        with jp.open('a') as f:
            f.write(json.dumps(line, ensure_ascii=False) + '\n'); f.flush()
        print(json.dumps(line, ensure_ascii=False))
        return 0
    if not jp.exists():
        print(json.dumps({'lines': 0})); return 0
    lines = [json.loads(x) for x in jp.read_text().splitlines() if x.strip()]
    if args.cmd == 'tail':
        print(json.dumps(lines[-args.n:], ensure_ascii=False, indent=2))
    else:
        kinds, renders = {}, {}
        for l in lines:
            kinds[l['kind']] = kinds.get(l['kind'], 0) + 1
            if l['kind'] == 'render-part':
                renders[l.get('part', '?')] = {'status': l.get('status'), 'frames': l.get('frames'), 'sha': (l.get('sha256') or '')[:12]}
        print(json.dumps({'lines': len(lines), 'kinds': kinds, 'render_parts': renders, 'last': lines[-1] if lines else None}, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    sys.exit(main())
