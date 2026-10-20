"""Kit validation v2: structure + Agent-Skills spec + compatibility + version discipline.
Runs the full contract; prints a single JSON verdict. Exit nonzero on any failure."""
from pathlib import Path
import json,re,sys,subprocess,hashlib
R=Path(__file__).resolve().parents[1];checks=[];errors=[]
def check(name,value):checks.append({'name':name,'passed':bool(value)});errors.extend([] if value else [name])
def read(p):return p.read_text(encoding='utf-8') if p.exists() else ''
def frontmatter(text):
 m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
 d={}
 if m:
  for line in m.group(1).splitlines():
   if ':' in line and not line.startswith((' ','-')):k,_,v=line.partition(':');d[k.strip()]=v.strip()
 return d
kit=json.loads(read(R/'kit.json') or '{}')
check('kit.json version semver',bool(re.fullmatch(r'\d+\.\d+\.\d+',kit.get('version',''))))
pkg=json.loads(read(R/'package.json') or '{}')
check('package.json version matches kit',pkg.get('version')==kit.get('version'))
plugin=json.loads(read(R/'.claude-plugin/plugin.json') or '{}')
check('plugin manifest version matches kit',plugin.get('version')==kit.get('version'))
check('plugin name',plugin.get('name')=='arabic-motion-forge')
mp=json.loads(read(R/'.claude-plugin/marketplace.json') or '{}')
check('marketplace points at plugin',mp.get('plugins',[{}])[0].get('name')=='arabic-motion-forge')
check('plugin skill directory',(R/plugin.get('skills','skills')).is_dir() if plugin.get('skills') else (R/'skills').is_dir())
# core docs
for doc in ['AGENTS.md','SKILL.md','README.md','CHANGELOG.md','kit.json','install.sh','LICENSE','THIRD_PARTY.md']:
 check(f'root {doc}',(R/doc).is_file())
check('AGENTS.md English',len(re.findall(r'[\u0600-\u06FF]',read(R/'AGENTS.md')))==0)
check('root SKILL.md has frontmatter',read(R/'SKILL.md').startswith('---'))
check('SKILL.md body under 500 lines',len(read(R/'SKILL.md').splitlines())<530)
# skills: spec-compliant, English, routed
skill_dirs=sorted(d.name for d in (R/'skills').glob('*') if (d/'SKILL.md').is_file())
expect=['arabic-type','asset-craft','audio-sync','creative-direction','delivery','ideate','intake','motion-direction','originality','performance','preview','quality','recovery','request-reframe','start','web-research']
check('sixteen discoverable skills',skill_dirs==expect)
for s in skill_dirs:
 text=read(R/f'skills/{s}/SKILL.md');fm=frontmatter(text)
 check(f'{s}: name matches dir',fm.get('name')==s)
 check(f'{s}: lowercase-hyphen name',bool(re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',fm.get('name',''))))
 check(f'{s}: description present',10<len(fm.get('description',''))<=1024)
 check(f'{s}: English body',len(re.findall(r'[\u0600-\u06FF]',text))<20)
 check(f'{s}: under 500 lines',len(text.splitlines())<500)
check('Codex adapter exists',(R/'.agents/skills/arabic-motion-forge/SKILL.md').exists())
check('Codex adapter English',(R/'.agents/skills/arabic-motion-forge/SKILL.md').exists() and len(re.findall(r'[\u0600-\u06FF]',read(R/'.agents/skills/arabic-motion-forge/SKILL.md')))==0)
# catalog + dictionaries
cat=json.loads(read(R/'catalog/motions.json') or '{}')
check('catalog has 100+ motions',len(cat.get('entries',[]))>=100)
check('catalog mechanisms dir',len(list((R/'reference/recipes').glob('*.md')))>=30)
lock=json.loads(read(R/'catalog/libraries.lock.json') or '[]')
check('library lock >=20 pinned repos',len(lock)>=20 and all(x.get('commit') for x in lock))
for dfile in ['direction-axes','easings','camera','continuity','styles','typography','creative-bank','spatial-3d']:
 j=json.loads(read(R/f'catalog/dictionaries/{dfile}.json') or 'null')
 check(f'dictionary {dfile} valid json',isinstance(j,dict) and j)
da=json.loads(read(R/'catalog/dictionaries/direction-axes.json') or '{}')
check('direction axes >=6 with >=4 options each',len(da.get('axes',{}))>=6 and all(len(v.get('options',[]))>=4 for v in da.get('axes',{}).values()))
# spatial engine (additive)
sp = read(R/'runtime/spatial.mjs')
check('spatial engine exists with core exports', sp.count('export') > 8 and all(x in sp for x in ('projectPoint','sortPainterly','slab','orbitKey','drawPlanar')))
check('spatial dictionary present',(R/'catalog/dictionaries/spatial-3d.json').is_file())
check('preview gate wired in render','preview_approved' in read(R/'tools/render.py'))
check('quota guardian present',(R/'tools/quota.py').is_file() and 'QUOTA BLOCK' in read(R/'tools/render.py'))
check('deliver policy in place',(R/'tools/deliver.py').is_file() and 'deliverables must live under' in read(R/'tools/deliver.py'))
# runtime freeze + compat gate (authoritative check)
r=subprocess.run([sys.executable,str(R/'tools/compat_check.py')],capture_output=True,text=True,timeout=60)
check('compat_check passes (v1 superset, runtime frozen)',r.returncode==0)
for t in ['direct','check_directions','journal','compat_check','render','validate_kit','new_project','check_project','install_from_release','package_core','doctor','bootstrap','storage','harvest_libraries','preview','deliver','quota','gate','transcribe','sync_check','motion_audit','fetch_font','export_ae']:
 check(f'tool {t}.py exists',(R/f'tools/{t}.py').is_file())
r2=subprocess.run([sys.executable,str(R/'tools/direct.py'),'--topic','smoke test','--json'],capture_output=True,text=True,timeout=30)
smoke_ok=False
if r2.returncode==0:
 try:
  d=json.loads(r2.stdout);smoke_ok=len(d['directions'])==3 and min(d['distinctness'].values())>=d['min_required']
 except Exception:pass
check('inspiration engine smoke: 3 distinct directions',smoke_ok)
# install.sh hygiene
ish=read(R/'install.sh')
check('install.sh refuses non-empty dest','Refusing to install' in ish and 'set -eu' in ish)
check('install.sh routes through verified installer','install_from_release' in ish)
# no secrets anywhere in tracked text
secret_pat=re.compile(r'(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})')
leak=[str(p.relative_to(R)) for p in R.rglob('*') if p.is_file() and p.suffix in {'.md','.json','.py','.mjs','.sh','.html','.csv','.txt','.yaml','.yml'} and secret_pat.search(p.read_bytes()[:200000].decode('utf-8','ignore'))]
check('no GitHub tokens in any tracked text file',not leak)
# v2.3 surface
check('gate aggregator exists',(R/'tools/gate.py').is_file() and 'tools/gate.py' in read(R/'AGENTS.md'))
check('quick mode wired', '--quick' in read(R/'tools/new_project.py') and 'mode' in read(R/'tools/check_project.py'))
check('preservation law in AGENTS+reframe','Preservation law' in read(R/'AGENTS.md') and 'PRESERVE EVERYTHING' in read(R/'skills/request-reframe/SKILL.md'))
check('motion_audit thresholds present',all(x in read(R/'tools/motion_audit.py') for x in ('flat_ratio','layered_ratio','simultaneity','bursts')))
check('user requirements section in spec template','## User requirements' in read(R/'tools/new_project.py') and '## User requirements' in read(R/'tools/check_project.py'))
check('typography law in arabic-type skill','typography.json' in read(R/'skills/arabic-type/SKILL.md'))
check('research registry motion-focused','videocopilot' in read(R/'skills/web-research/SKILL.md').lower() and 'design-language.md' in read(R/'skills/web-research/SKILL.md'))
check('first-reply contract wired','FIRST-REPLY TEMPLATE' in read(R/'AGENTS.md') and 'FIRST REPLY' in read(R/'SKILL.md') and 'never' in read(R/'AGENTS.md').lower())
check('skill-native install','HOME/.motion-forge' in read(R/'install.sh') and '.claude/skills/arabic-motion-forge' in read(R/'install.sh') and (R/'skill_launcher.md').exists() and 'name: arabic-motion-forge' in read(R/'skill_launcher.md'))
check('intake flow executable',(R/'tools/intake.py').is_file() and 'intake.py --emit' in read(R/'AGENTS.md'))
check('install.sh self-warms render deps','bootstrap.py' in read(R/'install.sh') and 'MOTION FORGE READY' in read(R/'install.sh') and '>/dev/null' in read(R/'install.sh'))
check('AE bridge files present',(R/'adapters/after-effects/export_ae.jsx').is_file() and 'AMF_AE_PLAN' in read(R/'adapters/after-effects/export_ae.jsx'))
# README/actual skill-count sync (drift was user-flagged)
rm = read(R/'README.md')
m = re.search(r'(\d+) spec-compliant skills', rm)
check('README skill count matches reality', bool(m) and int(m.group(1)) == len(skill_dirs))
# links inside docs resolve (relative, file-level)
broken=[]
for doc in [R/'README.md',R/'AGENTS.md',R/'SKILL.md']+[R/f'skills/{s}/SKILL.md' for s in skill_dirs]:
 for link in re.findall(r'\]\(([^)#][^)]*)\)',read(doc)):
  if link.startswith(('http://','https://','mailto:')):continue
  target=(doc.parent/link).resolve()
  if not target.exists():broken.append(f'{doc.name}:{link}')
check('all relative doc links resolve',not broken)
report={'passed':not errors,'checks':len(checks),'failures':errors,'skills':len(skill_dirs),'catalog_entries':len(cat.get('entries',[])),'native_host_execution_claimed':False}
(R/'research/kit-validation.json').write_text(json.dumps({'tool':'validate_kit.py v2','ran_at':kit['version'],'result':report},indent=2))
print(json.dumps(report,indent=2));sys.exit(0 if not errors else 1)
