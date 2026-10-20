#!/usr/bin/env python3
"""Inspiration engine: deterministic, topic-seeded generation of three structurally
distinct concept directions. Output is a starting point an agent must refine —
TODO fields block check_directions.py until the agent fills real rationale."""
import argparse, hashlib, json, re, sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
AXES_PATH = KIT / 'catalog/dictionaries/direction-axes.json'

def rng(seed: str):
    n = int(hashlib.sha256(seed.encode()).hexdigest()[:8], 16)
    while True:
        n = (1103515245 * n + 12345) & 0x7FFFFFFF
        yield n

def pick_options(gen, axes, k, used_sets):
    """Pick one option per axis; retry whole-sets until Hamming distance >= 3 vs used."""
    names = list(axes)
    for attempt in range(64):
        choice = {}
        for a in names:
            opts = axes[a]['options']
            choice[a] = opts[next(gen) % len(opts)]['id']
        if all(sum(1 for a in names if choice[a] != u[a]) >= max(3, len(names)//2) for u in used_sets):
            return choice
    return choice  # exhausted: best-effort, validator still checks distinctness

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--topic', required=True)
    ap.add_argument('--audience', default='')
    ap.add_argument('--project', default=None, help='write directions.json next to project.json')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    spec = json.loads(AXES_PATH.read_text())
    bank = json.loads((KIT / 'catalog/dictionaries/creative-bank.json').read_text())
    axes = spec['axes']
    seed = hashlib.sha256(args.topic.encode()).hexdigest()[:12]
    gen = rng(seed)
    used, directions = [], []
    palettes = spec['palette_sets']
    for i in range(3):
        choice = pick_options(gen, axes, i, used)
        used.append(choice)
        pal = palettes[next(gen) % len(palettes)]
        hook = bank['hook_bank'][next(gen) % len(bank['hook_bank'])]
        wild = bank['wild_cards'][next(gen) % len(bank['wild_cards'])]
        label = f"{choice['story_device']} / {choice['visual_metaphor']}"
        directions.append({
            'id': f'D{i+1}',
            'axes': choice,
            'palette': pal,
            'hook': hook, 'wild_card': wild,
            'first_frame_prompt': (
                f"{choice['visual_metaphor']} stage, {choice['material_language']} surface, "
                f"{choice['typography_architecture']} headline treatment, camera: {choice['camera_grammar']}, "
                f"accent: {choice['accent_system']}, rhythm: {choice['rhythm_policy']}."),
            'do_not_copy': ['any scene from the kit examples', 'any previously delivered project of this user',
                            'the literal library style unless the brief demands it'],
            'TODO': {
                'why_this_fits': 'AGENT: 3+ sentences tying topic specifics to at least 3 chosen axes; name what you rejected in the other directions.',
                'audience_note': 'AGENT: one sentence about the stated audience.',
                'evidence_plan': 'AGENT: which dictionary rules (continuity.json ids) + measurements prove this direction on the draft tier.'
            }
        })
    # distinctness self-check report
    def ham(a, b):
        return sum(1 for k in axes if a['axes'][k] != b['axes'][k])
    pairs = {f"{x['id']}{y['id']}": ham(x, y) for i, x in enumerate(directions) for y in directions[i+1:]}
    out = {'topic': args.topic, 'audience': args.audience, 'seed': seed,
           'cliche_blacklist': bank['cliche_blacklist'], 'trend_questions': bank['trend_questions_2026'],
           'quality_bar': bank['quality_bar'],
           'distinctness': pairs, 'min_required': max(3, len(axes)//2),
           'directions': directions,
           'next': 'Fill every TODO field with real rationale, present the three to the user, then run tools/check_directions.py.'}
    if args.project:
        p = Path(args.project)
        target = (p if p.is_dir() else p.parent) / 'directions.json'
        target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
        print(f'wrote {target}')
    print(json.dumps(out, ensure_ascii=False, indent=2 if not args.json else None))
    bad = [k for k, v in pairs.items() if v < out['min_required']]
    if bad:
        print(f'WARNING: directions {bad} share too many axes — regenerate with a different topic string.', file=sys.stderr)
    return 0

if __name__ == '__main__':
    sys.exit(main())
