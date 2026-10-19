"""Restore confirmed public Release checkpoints by checksum. No token and no automatic media install.
Usage: python tools/restore_artifacts.py --repo owner/repository --manifest project/render-report.json --destination ~/.cache/restored-pieces
Private repositories require an authenticated connector/manual download; this tool does not pretend otherwise.
"""
from pathlib import Path
import argparse,json,hashlib,urllib.request
p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--manifest',required=True);p.add_argument('--destination',required=True);a=p.parse_args()
r=Path(a.destination).expanduser().resolve();r.mkdir(parents=True,exist_ok=True);data=json.loads(Path(a.manifest).read_text());playlist=[]
for i,part in enumerate(data['segments']):
 backup=part.get('backup')
 if not backup:raise SystemExit('This checkpoint was not confirmed published; no invented recovery URL will be used.')
 name=backup['asset_name'];url=f'https://github.com/{a.repo}/releases/download/{backup["release_tag"]}/{name}';dest=r/name
 if not dest.exists() or hashlib.sha256(dest.read_bytes()).hexdigest()!=part['sha256']:
  request=urllib.request.Request(url,headers={'User-Agent':'ArabicMotionForge verified recovery'})
  with urllib.request.urlopen(request,timeout=120) as response:blob=response.read()
  if hashlib.sha256(blob).hexdigest()!=part['sha256']:raise SystemExit('Checksum mismatch: '+name)
  dest.write_bytes(blob)
 playlist.extend([f"file '{dest}'",f'duration {(part["frame_out"]-part["frame_in"])/data["fps"]:.8f}'])
 print('Verified',name)
(r/'restored-pieces.txt').write_text('\n'.join(playlist)+'\n');print('Restored without deleting existing media. Reassemble video-only pieces and mux the continuous approved audio mix, as tools/render.py does.')
