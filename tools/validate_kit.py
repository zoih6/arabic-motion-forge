from pathlib import Path
import json,re,hashlib,argparse
R=Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument('--write-report',action='store_true');a=p.parse_args();errors=[];checks=[]
def check(name,value):checks.append({'name':name,'passed':bool(value)});errors.extend([] if value else [name])
for name in ['AGENTS.md','SKILL.md','README.md','INSTALL.md','THIRD_PARTY.md','LICENSE','catalog/motions.json','catalog/capabilities.json','.claude-plugin/plugin.json','.claude-plugin/marketplace.json','tools/doctor.py','tools/new_project.py','tools/check_project.py','tools/install_from_release.py']:
 check('required path '+name,(R/name).is_file())
plugin=json.loads((R/'.claude-plugin/plugin.json').read_text());market=json.loads((R/'.claude-plugin/marketplace.json').read_text())
check('plugin identity',plugin['name']=='arabic-motion-forge' and plugin['version']=='1.0.0')
check('plugin skill directory',(R/plugin['skills']).is_dir())
check('marketplace source resolves to root',market['plugins'][0]['name']==plugin['name'] and (R/market['plugins'][0]['source']).resolve()==R)
skills=list((R/'skills').glob('*/SKILL.md'));check('nine discoverable skills',len(skills)==9)
for s in skills:
 text=s.read_text();name=re.search(r'^name:\s*(.+)$',text,re.M);desc=re.search(r'^description:\s*(.+)$',text,re.M)
 check('skill metadata '+s.parent.name,bool(name and name.group(1).strip()==s.parent.name and desc and len(desc.group(1))>30))
check('Codex adapter exists',(R/'.agents/skills/arabic-motion-forge/SKILL.md').exists())
for folder in [R,R/'skills',R/'reference',R/'workflows']:
 files=folder.glob('*.md') if folder==R else folder.rglob('*.md')
 for f in files:
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()):
   target=target.split('#')[0]
   if not target or '://' in target or target.startswith('mailto:'):continue
   check('link '+str(f.relative_to(R))+' -> '+target,(f.parent/target).exists())
cat=json.loads((R/'catalog/motions.json').read_text());check('104 catalog entries',len(cat['entries'])==104);check('33 canonical mechanisms',len(cat['mechanisms'])==33)
for row in cat['entries']:check('recipe '+row['id'],(R/row['recipe']).is_file())
for lib in json.loads((R/'catalog/bundled-libraries.json').read_text()):
 check('license notice '+lib['package'],(R/lib['license_notice_path']).exists())
 for f in lib['bundled_files']:check('bundle hash '+f['path'],hashlib.sha256((R/f['path']).read_bytes()).hexdigest()==f['sha256'])
secret=re.compile(rb'(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)')
for f in R.rglob('*'):
 if f.is_file() and f.suffix.lower() in {'.py','.js','.mjs','.json','.md','.txt','.html','.csv','.yaml'}:check('secret scan '+str(f.relative_to(R)),not secret.search(f.read_bytes()))
report={'passed':not errors,'checks':len(checks),'failures':errors,'skills':len(skills),'catalog_entries':len(cat['entries']),'native_host_execution_claimed':False}
if a.write_report:(R/'research').mkdir(exist_ok=True);(R/'research/kit-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(1 if errors else 0)
