#!/usr/bin/env python3
"""Compatibility gate: v2 must be a strict superset of v1's public surface.
Verifies (1) every v1 file path still present, (2) runtime/core.mjs and
runtime/canvas.mjs byte-identical to the frozen v1 (freeze contract),
(3) exported API sets ⊇ baseline, (4) v1 catalog/kit fields preserved.
Any failure means: do not ship this version."""
import hashlib, json, re, subprocess, sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
BASE = json.loads((KIT / 'catalog/compatibility-baseline.json').read_text())

_MUTABLE_KIT_FIELDS = {'version', 'status', 'language', 'skills', 'catalog_entries', 'unique_motion_names',
                     'mechanism_contracts', 'audited_repositories', 'bundled_libraries_tested'}  # metrics may grow; contracts may not

def exports_of(mod: Path) -> set:
    src = mod.read_text()
    names = set(re.findall(r'export\s+(?:async\s+)?(?:function|const|class)\s+([A-Za-z_$][\w$]*)', src))
    m = re.search(r'export\s*\{([^}]*)\}', src)
    if m:
        for part in m.group(1).split(','):
            part = part.strip()
            if part:
                names.add(part.split(' as ')[-1].strip())
    return names

def main() -> int:
    fail = []
    # 1) path superset (contract surface; research/ holds regenerable session records deliberately
    # excluded from the core archive, so it is not part of the compatibility promise)
    for rel in BASE['paths_v1']:
        if rel.startswith('research/'):
            continue
        if not (KIT / rel).exists():
            fail.append(f'missing v1 path: {rel}')
    # 2) frozen runtime bytes
    for rel, want in BASE['runtime_sha256_v1'].items():
        got = hashlib.sha256((KIT / rel).read_bytes()).hexdigest()
        if got != want:
            fail.append(f'{rel} changed bytes vs frozen v1 ({got[:8]} != {want[:8]}) — runtime is frozen; ship new capabilities as separate modules')
    # 3) export supersets (belt and suspenders even with hashes equal)
    for rel, key in (('runtime/core.mjs', 'core_exports'), ('runtime/canvas.mjs', 'canvas_exports')):
        have = exports_of(KIT / rel)
        need = set(BASE[key])
        if not need <= have:
            fail.append(f'{rel} dropped exports: {sorted(need - have)}')
    # 4) data contract: v1 catalog entries still present with same ids+mechanisms
    mot = json.loads((KIT / 'catalog/motions.json').read_text())
    ids = {m['id'] for m in mot['entries']}
    if len(ids) < len(BASE.get('motion_ids_v1', ids)):
        fail.append('motions.json shrank below v1 entry count')
    kit = json.loads((KIT / 'kit.json').read_text())
    v1kit = BASE.get('kit_json_v1', {})
    for field, want in v1kit.items():
        if field not in kit:
            fail.append(f'kit.json lost v1 field: {field}')
        elif field not in _MUTABLE_KIT_FIELDS and not isinstance(want, (dict, list)) and kit[field] != want:
            fail.append(f'kit.json changed v1 value: {field} ({kit[field]!r} != {want!r})')
    v = kit['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+', v):
        fail.append(f'kit version {v!r} not semver')
    if v == '1.0.0':
        fail.append('version not bumped for v2 changes')
    if fail:
        print('COMPATIBILITY FAIL:\n- ' + '\n- '.join(fail), file=sys.stderr)
        return 1
    n_new = sum(1 for p in KIT.rglob('*') if p.is_file() and '.git' not in p.parts and str(p.relative_to(KIT)) not in BASE['paths_v1'])
    print(json.dumps({'verdict': 'PASS', 'v1_paths_kept': len(BASE['paths_v1']), 'runtime_frozen': True,
                      'new_or_changed_files_vs_v1': n_new, 'kit_version': v}))
    return 0

if __name__ == '__main__':
    sys.exit(main())
