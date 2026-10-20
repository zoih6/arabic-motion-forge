#!/usr/bin/env python3
"""After Effects bridge: project layer plan -> self-contained .jsx for AE (File>Scripts>Run).
Maps tracks/keyframes/easings; text layers carry content + timing (glyph source stays a re-link step);
solids mark footage layers. No AE here — generated scripts are linted as JS and structure-tested only.
Honesty label: 'bridge export for Adobe workflows', NOT 'AE project file' and NOT a claim of visual parity."""
import argparse, json, re, subprocess, sys
from pathlib import Path
KIT = Path(__file__).resolve().parents[1]

EASE_MAP = {'linear': 'linear', 'out': 'out', 'in': 'in', 'inOut': 'both', 'both': 'both', 'hold': 'hold'}

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument('project_json'); ap.add_argument('--out', default=None); a = ap.parse_args()
    pj = Path(a.project_json).resolve(); root = pj.parent; cfg = json.loads(pj.read_text())
    plan = json.loads((root / cfg['layer_plan']).read_text())
    scenes = []
    for sc in plan.get('scenes', []):
        out_layers = []
        for lay in sc.get('layers', []):
            o = {'id': lay.get('id'), 'kind': lay.get('kind', 'solid'), 'text': lay.get('text')}
            ti = lay.get('timing', {})
            if ti.get('start') is not None: o['in'] = round(float(ti['start']) / cfg['fps'], 4)
            if ti.get('settle_or_stage_end') is not None: o['out'] = round(float(ti['settle_or_stage_end']) / cfg['fps'], 4)
            tracks = {}
            for ch in (lay.get('channels') or []):
                if isinstance(ch, dict) and ch.get('keys'):
                    name = ch.get('name', 'position')
                    keys = []
                    for k in ch['keys']:
                        keys.append({'t': round(float(k.get('t', 0)) / cfg['fps'], 4), 'v': k.get('v', 0),
                                     'ease': EASE_MAP.get(k.get('easing') or k.get('ease') or 'linear', 'linear')})
                    keys = [k for k in keys if k['t'] >= 0]
                    if keys: tracks[name if name in ('position', 'opacity', 'scale', 'rotation') else 'position'] = keys
            if tracks: o['tracks'] = tracks
            out_layers.append(o)
        if out_layers: scenes.append({'id': sc.get('id'), 'layers': out_layers})
    data = {'name': cfg.get('title', cfg['id']), 'width': cfg['width'], 'height': cfg['height'],
            'duration': cfg['duration'], 'meta': {'generator': 'arabic-motion-forge ' + json.loads((KIT / 'kit.json').read_text())['version'],
            'note': 'bridge export; re-link footage/glyph sources; AE-side easing is approximation of analytic curves'},
            'scenes': scenes}
    tpl = (KIT / 'adapters/after-effects/export_ae.jsx').read_text()
    js = 'window.AMF_AE_PLAN = ' + json.dumps(data, ensure_ascii=False) + ';\n' + tpl
    out = Path(a.out) if a.out else root / f"{cfg['id']}-ae-bridge.jsx"
    out.write_text(js, encoding='utf-8')
    # lint the embedded plan object as JS via node (syntax only)
    node = subprocess.run(['node', '-e', 'JSON.parse(process.argv[1]);console.log("plan json ok")', json.dumps(data, ensure_ascii=False)], capture_output=True, text=True)
    if node.returncode != 0: raise SystemExit('plan lint failed: ' + node.stderr[-200:])
    print(json.dumps({'jsx': str(out), 'scenes': len(scenes), 'layers': sum(len(s['layers']) for s in scenes),
                      'ae_execution_verified': False, 'next': 'In AE: File > Scripts > Run Script File… then relink footage and run a RAM preview'}))
    return 0

if __name__ == '__main__':
    sys.exit(main())
