#!/usr/bin/env python3
"""OFL font fetcher (google/fonts master, per-file). Records sha256 + license path in the project
font manifest so renders can prove what was loaded. Network only when the agent asks for a font."""
import argparse, hashlib, io, json, re, ssl, sys, urllib.request, zipfile
from pathlib import Path
from urllib.parse import quote

BASE = 'https://api.github.com/repos/google/fonts/contents'

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'arabic-motion-forge fetch_font', 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(req, timeout=60) as f:
        return f.read()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--family', required=True, help='e.g. "Reem Kufi", "Rakkas", "Amiri"')
    ap.add_argument('--project', required=True); ap.add_argument('--weight', default=None); a = ap.parse_args()
    proj = Path(a.project).resolve(); proj_dir = proj if proj.is_dir() else proj.parent
    fam = a.family.strip(); slug = fam.lower().replace(' ', '-')
    def listing_of(dirpath):
        try:
            data = json.loads(get(f'{BASE}/{dirpath}'))
            return data if isinstance(data, list) else None
        except Exception:
            return None
    listing = listing_of(f'ofl/{quote(slug)}') or listing_of(f'ofl/{quote(slug.replace("-",""))}')
    if listing is None:
        # fuzzy: scan ofl/ dir names (paginated listing is ~1 request)
        all_ofl = listing_of('ofl?per_page=1000') or []
        names = [x['name'] for x in all_ofl if x['type'] == 'dir']
        import difflib
        flat = slug.replace('-', '')
        cands = [n for n in names if flat in n.replace('-', '')]
        if not cands:
            near = difflib.get_close_matches(flat, [n.replace('-', '') for n in names], k=6)
            raise SystemExit(f'family {fam!r} not under google/fonts ofl/. Close matches: {near}')
        listing = listing_of(f'ofl/{quote(cands[0])}')
        slug = cands[0]
    ttf = [x for x in listing if x['name'].endswith('.ttf') and 'static' not in x['path']]
    prefer = a.weight or ('Regular' if 'Regular' in ' '.join(x['name'] for x in ttf) else None)
    picked = [x for x in ttf if prefer and prefer.lower() in x['name'].lower()] or ttf
    bold = [x for x in ttf if 'bold' in x['name'].lower() and 'variable' not in x['name'].lower()]
    chosen = picked[:1] + ([b for b in bold if b not in picked][:1] if bold and prefer is None else [])
    # variable fonts acceptable too when only those exist
    files = {}
    for item in chosen:
        raw = get(f"https://raw.githubusercontent.com/google/fonts/main/{item['path']}")
        if raw[:4] not in (b'\x00\x01\x00\x00', b'true', b'ttcf', b'OTTO'): raise SystemExit('not a ttf/otf payload: ' + item['name'])
        (proj_dir / 'assets/fonts').mkdir(parents=True, exist_ok=True)
        dest = proj_dir / 'assets/fonts' / item['name']
        dest.write_bytes(raw); files[item['name']] = hashlib.sha256(raw).hexdigest()
    lic = next((x for x in listing if x['name'] == 'OFL.txt'), None)
    lic_sha = None
    if lic:
        data = get(f"https://raw.githubusercontent.com/google/fonts/main/{lic['path']}")
        (proj_dir / 'assets/fonts' / f'OFL-{slug}.txt').write_bytes(data); lic_sha = hashlib.sha256(data).hexdigest()
    man = proj_dir / 'assets/fonts/manifest.json'
    m = json.loads(man.read_text()) if man.exists() else {'fonts': []}
    m['fonts'].append({'family': fam, 'source': f'https://github.com/google/fonts/tree/main/ofl/{slug}',
                       'license': 'OFL-1.1', 'license_sha256': lic_sha, 'files': files, 'fetched_by': 'fetch_font.py'})
    man.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'family': fam, 'files': list(files), 'manifest': str(man)}, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    sys.exit(main())
