#!/usr/bin/env python3
"""Direction gate: fails until directions.json is genuinely authored.
Checks: TODOs resolved with substance, rationale references topic vocabulary,
directions structurally distinct, and no fingerprint collision with protected
house styles (kit example + prior delivered projects when provided)."""
import argparse, hashlib, json, re, sys
from pathlib import Path

STOP = set('the a an and or of to in for on with is are be as at by it this that from into we you your our they'.split())

def tokens(s):
    return {w for w in re.findall(r'[^\W\d_]{3,}', s.lower(), re.UNICODE) if w not in STOP}

def topic_hit(topic_toks, prose):
    """Morphology-tolerant: a topic token counts if any prose word shares its stem (first 4+ chars)."""
    prose_toks = tokens(prose)
    hits = 0
    for t in topic_toks:
        stem = t[:max(4, len(t) - 2)]
        if any(pt.startswith(stem) or t.startswith(pt[:max(4, len(pt) - 2)]) for pt in prose_toks):
            hits += 1
    return hits

def style_fingerprint(style: dict) -> str:
    axes = style.get('direction_axes') or {}
    return hashlib.sha256(json.dumps({k: axes[k] for k in sorted(axes)}, sort_keys=True).encode()).hexdigest()[:12] if axes else ''

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('project', help='project.json path')
    ap.add_argument('--against', nargs='*', default=[],
                    help='extra style.json files treated as protected house styles (e.g. prior projects)')
    args = ap.parse_args()
    proj = Path(args.project)
    proj_dir = proj if proj.is_dir() else proj.parent
    data = json.loads((proj_dir / 'directions.json').read_text())
    brief = json.loads((proj_dir / 'brief.json').read_text()) if (proj_dir / 'brief.json').exists() else {}
    errors = []

    topic_tokens = tokens(data.get('topic', '') + ' ' + str(brief.get('subject', '')))
    min_required = data.get('min_required', 3)
    ds = data.get('directions', [])
    if len(ds) < 3:
        errors.append('need at least 3 directions')

    protected = set()
    kit = Path(__file__).resolve().parents[1]
    for p in [str(kit / 'examples/vertical-showcase/style.json')] + list(args.against):
        fp = Path(p)
        if fp.exists():
            f = style_fingerprint(json.loads(fp.read_text()))
            if f:
                protected.add(f)

    for d in ds:
        for k, v in (d.get('TODO') or {}).items():
            errors.append(f"{d['id']} TODO.{k} unresolved")
        why = (d.get('why_this_fits') or '')
        if len(why.split()) < 18:
            errors.append(f"{d['id']} why_this_fits too short to be a decision")
        elif topic_tokens and topic_hit(topic_tokens, why) < 2:
            errors.append(f"{d['id']} rationale never mentions the topic's own vocabulary (need 2 topic stems)")
        if d.get('style_fingerprint') in protected or style_fingerprint(d) in protected:
            errors.append(f"{d['id']} collides with a protected house style")
    names = list(data.get('directions', [{}])[0].get('axes', {})) if ds else []
    for i, a in enumerate(ds):
        for b in ds[i+1:]:
            h = sum(1 for k in names if a['axes'].get(k) != b['axes'].get(k))
            if h < min_required:
                errors.append(f"{a['id']}/{b['id']} differ on only {h} axes (need {min_required})")

    if errors:
        print('direction gate FAILS:\n- ' + '\n- '.join(errors), file=sys.stderr)
        return 1
    # lock the approved direction into style.json
    chosen = next((d for d in ds if d.get('approved')), ds[0])
    style_path = proj_dir / 'style.json'
    style = json.loads(style_path.read_text()) if style_path.exists() else {}
    style.update({'direction_axes': chosen['axes'], 'palette': chosen['palette'],
                  'approved_direction': chosen['id'], 'gate': 'check_directions.py passed'})
    style_path.write_text(json.dumps(style, ensure_ascii=False, indent=2) + '\n')
    (proj_dir / 'research/direction-gate.json').parent.mkdir(exist_ok=True)
    (proj_dir / 'research/direction-gate.json').write_text(json.dumps({'passed': True, 'approved': chosen['id'], 'distinctness': data.get('distinctness')}, indent=2) + '\n')
    print(f"direction gate PASS (approved {chosen['id']}); style.json updated")
    return 0

if __name__ == '__main__':
    sys.exit(main())
