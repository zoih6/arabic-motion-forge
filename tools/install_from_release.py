"""Stdlib-only verified installer. No token, no old-film clone and no automatic media download.
v2: resolves the LATEST release by default and any core archive version; --tag v1.0.0 still works."""
from pathlib import Path,PurePosixPath
import argparse,urllib.request,json,hashlib,zipfile,shutil,subprocess,sys,stat
p=argparse.ArgumentParser();p.add_argument('--destination',required=True);p.add_argument('--archive');p.add_argument('--sha256');p.add_argument('--tag',default='latest',help="'latest' or an exact tag like v1.0.0");p.add_argument('--repo',default='zoih6/arabic-motion-forge');p.add_argument('--setup',action='store_true');a=p.parse_args()
dest=Path(a.destination).expanduser().resolve()
if dest.exists() and any(dest.iterdir()):raise SystemExit('Choose an empty destination; existing files will not be overwritten.')
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'ArabicMotionForge lightweight installer','Accept':'application/vnd.github+json'})
 with urllib.request.urlopen(req,timeout=60) as f:return f.read()
if a.archive:
 data=Path(a.archive).read_bytes();expected=a.sha256
 if not expected:raise SystemExit('--archive requires --sha256')
else:
 url=f'https://api.github.com/repos/{a.repo}/releases/latest' if a.tag=='latest' else f'https://api.github.com/repos/{a.repo}/releases/tags/{a.tag}'
 meta=json.loads(get(url));assets={x['name']:x for x in meta['assets']}
 core=sorted(n for n in assets if n.startswith('arabic-motion-forge-core-') and n.endswith('.zip'))
 if not core:raise SystemExit('No core archive asset found on this release.')
 name=core[-1]  # highest-sorted version asset
 if 'SHA256SUMS.txt' in assets:
  import time as _t;_cb='?cb=%d'%_t.time()
 sums=get(assets['SHA256SUMS.txt']['browser_download_url']+_cb).decode();expected=next(l.split()[0] for l in sums.splitlines() if len(l.split())>=2 and l.split()[1]==name)
 else:
  expected=assets[name].get('digest') or ''
  if not expected:raise SystemExit('Release carries no verifiable checksum; refuse blind install. Pass --sha256 if you have one.')
 data=get(assets[name]['browser_download_url']+_cb)
if len(data)>16*1024**2:raise SystemExit('Core archive exceeds the declared lightweight safety budget.')
assert hashlib.sha256(data).hexdigest()==expected,'Archive checksum mismatch'
import io
with zipfile.ZipFile(io.BytesIO(data)) as z:
 for n in z.infolist():
  path=PurePosixPath(n.filename)
  if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0]!='arabic-motion-forge':raise SystemExit('Unsafe archive path')
  if stat.S_ISLNK(n.external_attr>>16):raise SystemExit('Symlinks are not accepted in the core archive')
  if n.file_size>8*1024**2:raise SystemExit('Unexpected large archive member')
 dest.mkdir(parents=True,exist_ok=True)
 for n in z.infolist():
  rel=PurePosixPath(n.filename).relative_to('arabic-motion-forge')
  if not rel.parts:continue
  target=dest/str(rel)
  if n.is_dir():target.mkdir(parents=True,exist_ok=True)
  else:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(n))
assert (dest/'AGENTS.md').is_file() and (dest/'skills/start/SKILL.md').is_file()
if a.setup:subprocess.run([sys.executable,str(dest/'tools/bootstrap.py'),'--install'],check=True)
(dest/'install-report.json').write_text(json.dumps({'installed':str(dest),'release':meta.get('tag_name',a.tag),'archive':name,'archive_sha256':expected,'demo_media_downloaded':False,'demo_scene_code_installed':(dest/'examples/vertical-showcase/scene.mjs').exists(),'native_plugin_registration_performed':False},indent=2)+"\n")
print(f"MOTION FORGE INSTALLED {dest} release {meta.get('tag_name',a.tag)} (full report: install-report.json)")
