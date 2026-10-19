"""Create a small installable archive; deliberately exclude demonstration compositions and media."""
from pathlib import Path
import zipfile,hashlib,json
R=Path(__file__).resolve().parents[1];D=R/'deliverables';D.mkdir(exist_ok=True)
include={'AGENTS.md','SKILL.md','README.md','CHANGELOG.md','INSTALL.md','CLAUDE.md','LICENSE','THIRD_PARTY.md','kit.json','package.json','.gitignore','.claude-plugin','.agents','skills','workflows','runtime','adapters','schemas','templates','reference','catalog','tools','tests','vendor','assets','research'}
exclude={'__pycache__','node_modules','.cache','.git','out','build','dist'}
file=D/'arabic-motion-forge-core-1.0.0.zip';members=[]
with zipfile.ZipFile(file,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(R.rglob('*')):
  if not p.is_file() or p.is_symlink():continue
  rel=p.relative_to(R)
  if rel.parts[0] not in include or any(x in exclude for x in rel.parts):continue
  if rel.parts[0]=='research' and (p.suffix not in {'.json','.tap','.md','.txt'} or p.name in {'repository.json','workspace-health.json','core-package.json','install-smoke.json','release-verification.json','distribution.json'}):continue
  if rel.parts[0]=='tools' and p.name in {'build_showcase.py','showcase_audio.py'}:continue
  if p.suffix.lower() in {'.mp4','.mp3','.m4a','.wav','.webm','.mov','.zip','.tgz'}:continue
  z.write(p,str(Path('arabic-motion-forge')/rel));members.append(str(rel))
assert not any(x.startswith('examples/') for x in members)
record={'file':file.name,'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'files':len(members),'excluded_demo_compositions':True,'included_media_files':0,'members':members}
(R/'research/core-package.json').write_text(json.dumps(record,indent=2));print(json.dumps({k:v for k,v in record.items() if k!='members'}))
