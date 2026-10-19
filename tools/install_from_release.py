"""Stdlib-only verified installer. No token, no old-film clone and no automatic media download."""
from pathlib import Path,PurePosixPath
import argparse,urllib.request,json,hashlib,zipfile,tempfile,shutil,subprocess,sys,stat
p=argparse.ArgumentParser();p.add_argument('--destination',required=True);p.add_argument('--archive');p.add_argument('--sha256');p.add_argument('--tag',default='v1.0.0');p.add_argument('--repo',default='zoih6/arabic-motion-forge');p.add_argument('--setup',action='store_true');a=p.parse_args()
dest=Path(a.destination).expanduser().resolve()
if dest.exists() and any(dest.iterdir()):raise SystemExit('Choose an empty destination; existing files will not be overwritten.')
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'ArabicMotionForge lightweight installer','Accept':'application/vnd.github+json'})
 with urllib.request.urlopen(req,timeout=90) as f:return f.read()
if a.archive:
 data=Path(a.archive).read_bytes();expected=a.sha256
 if not expected:raise SystemExit('--archive requires --sha256')
else:
 meta=json.loads(get(f'https://api.github.com/repos/{a.repo}/releases/tags/{a.tag}'));assets={x['name']:x for x in meta['assets']};name='arabic-motion-forge-core-1.0.0.zip'
 sums=get(assets['SHA256SUMS.txt']['browser_download_url']).decode();expected=next(line.split()[0] for line in sums.splitlines() if line.split()[-1]==name);data=get(assets[name]['browser_download_url'])
if len(data)>12*1024**2:raise SystemExit('Core archive exceeds the declared lightweight safety budget.')
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
print(json.dumps({'installed':str(dest),'archive_sha256':expected,'demo_media_downloaded':False,'demo_scene_code_installed':(dest/'examples/vertical-showcase/scene.mjs').exists(),'native_plugin_registration_performed':False},indent=2))
