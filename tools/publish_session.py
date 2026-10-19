"""Scoped GitHub source/checkpoint publisher. Token is process-memory only.
Usage: GITHUB_TOKEN=<temporary environment value> python tools/publish_session.py --name arabic-motion-forge
Do not put a real token into a saved command, file, git URL, or repository.
Heavy assets go to Releases, never the default source clone. This session service
accepts explicit jobs from its own queue; it is not an unsolicited file watcher.
"""
from pathlib import Path
import argparse,os,json,time,shutil,subprocess,hashlib,base64,re,mimetypes
from urllib.parse import urlsplit,quote
import requests
ROOT=Path(__file__).resolve().parents[1]
P=argparse.ArgumentParser();P.add_argument('--name',default='arabic-motion-forge');P.add_argument('--visibility',choices=['public','private'],default='private');P.add_argument('--root',default=str(ROOT));P.add_argument('--session-dir');a=P.parse_args();ROOT=Path(a.root).expanduser().resolve();(ROOT/'research').mkdir(exist_ok=True)
if (ROOT/'project.json').exists() and not json.loads((ROOT/'project.json').read_text()).get('publish_allowed',False):raise SystemExit('Project publication needs explicit recorded user authorization.')
CACHE=Path(a.session_dir).expanduser().resolve() if a.session_dir else Path.home()/'.cache'/('motion-forge-session' if ROOT.name=='arabic-motion-forge' else 'motion-forge-'+ROOT.name);WORK=CACHE/'publish-worktree';QUEUE=CACHE/'publish-queue';QUEUE.mkdir(parents=True,exist_ok=True)
STATE=ROOT/'research/repository.json';token=os.environ.pop('GITHUB_TOKEN','');assert token,'Temporary GITHUB_TOKEN environment value required.'
basic=base64.b64encode(('x-access-token:'+token).encode()).decode();session=requests.Session();session.headers.update(Authorization='Bearer '+token,Accept='application/vnd.github+json',**{'X-GitHub-Api-Version':'2022-11-28'})
state={'status':'initializing','credential_persisted':False,'assets':[],'releases':{}}
def safe(s):return str(s).replace(token,'[REDACTED]').replace(basic,'[REDACTED]')
def log(s):print(safe(s),flush=True)
def save():STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2))
def api(method,path,**kw):
 r=session.request(method,'https://api.github.com'+path,timeout=45,allow_redirects=False,**kw)
 if r.status_code>=300:
  try:msg=r.json().get('message','API failure')
  except Exception:msg='API failure'
  raise RuntimeError(f'GitHub {r.status_code}: {msg}')
 return r.json() if r.content else {}
def git(*args,auth=False):
 env=os.environ.copy();env['GIT_TERMINAL_PROMPT']='0'
 if auth:env.update(GIT_CONFIG_COUNT='1',GIT_CONFIG_KEY_0='http.https://github.com/.extraHeader',GIT_CONFIG_VALUE_0='AUTHORIZATION: basic '+basic)
 r=subprocess.run(['git',*args],cwd=WORK,env=env,capture_output=True,text=True,timeout=300)
 if r.returncode:raise RuntimeError(safe((r.stderr or r.stdout)[-1600:]))
 return r.stdout.strip()
excluded={'.git','.runtime','.cache','__pycache__','node_modules','deliverables','build','dist','coverage','out'}
secret=re.compile(rb'(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)')
def snapshot():
 for folder,dirs,files in os.walk(ROOT):
  dirs[:]=[d for d in dirs if d not in excluded]
  for n in files:
   p=Path(folder)/n;rel=p.relative_to(ROOT)
   if p.is_symlink() or n.startswith('.env') or n in {'.netrc','.git-credentials'}:continue
   if p.suffix.lower() in {'.mp4','.mov','.wav','.mp3','.m4a','.zip','.webm'}:continue
   data=p.read_bytes()
   if token.encode() in data or secret.search(data):raise RuntimeError('Secret scan blocked '+str(rel))
   if len(data)>4_000_000:raise RuntimeError('Source file too large for lightweight clone: '+str(rel))
   target=WORK/rel;target.parent.mkdir(parents=True,exist_ok=True)
   if not target.exists() or target.read_bytes()!=data:target.write_bytes(data)
 # Deliberately do not remove older remote source files or release assets.
def commit(message):
 snapshot();git('add','--all')
 if git('status','--porcelain'):git('commit','-m',message);git('push','-u','origin','main',auth=True)
 state.update(source_commit=git('rev-parse','HEAD'),status='awaiting_explicit_jobs');save();log('SOURCE_BACKED_UP '+state['source_commit'][:12]+' '+message)
def release(tag,prerelease):
 if tag in state['releases']:return state['releases'][tag]
 value=api('POST',f'/repos/{state["full_name"]}/releases',json={'tag_name':tag,'target_commitish':state['source_commit'],'name':tag,'body':'Verified source and separately downloadable artifacts. Default installation does not download movies.','draft':False,'prerelease':prerelease})
 value={k:value[k] for k in ['id','upload_url','html_url','tag_name']};state['releases'][tag]=value;save();return value
try:
 me=api('GET','/user');previous=json.loads(STATE.read_text()) if STATE.exists() else {}
 if previous.get('full_name') and previous.get('owner')==me['login']:
  info=api('GET','/repos/'+previous['full_name']);assert info['id']==previous['repository_id'];state.update(previous)
 else:
  name=a.name
  for n in range(1,6):
   rr=session.post('https://api.github.com/user/repos',json={'name':name if n==1 else f'{name}-{n:02d}','private':a.visibility=='private','description':'Arabic-first, evidence-led motion production system. Layer-specific choreography, deterministic rendering, verified catalogs, lightweight agent installation.','auto_init':False},timeout=45,allow_redirects=False)
   if rr.status_code==201:info=rr.json();break
   if rr.status_code==422 and 'already exists' in rr.text.lower():continue
   raise RuntimeError('Repository creation failed: '+str(rr.status_code)+' '+rr.json().get('message',''))
  else:raise RuntimeError('No unused repository name found')
 state.update(owner=me['login'],repository_id=info['id'],full_name=info['full_name'],url=info['html_url'],clone_url=info['clone_url'],public=not info['private'],credential_persisted=False)
 assert urlsplit(info['clone_url']).hostname=='github.com';save();log('REPOSITORY '+info['html_url'])
 WORK.mkdir(parents=True,exist_ok=True)
 if not (WORK/'.git').exists():
  git('init','-b','main');git('remote','add','origin',info['clone_url'])
  if previous.get('source_commit'):git('fetch','origin','main',auth=True);git('reset','--hard','origin/main')
 assert git('remote','get-url','origin')==info['clone_url'],'Publisher scope mismatch: choose a separate session directory';git('config','user.name','Motion Forge Production');git('config','user.email',f'{me["id"]}+{me["login"]}@users.noreply.github.com');git('config','pack.windowMemory','64m');git('config','pack.threads','1')
 commit('Initialize the independent lightweight motion-production system')
 while True:
  for file in sorted(QUEUE.glob('*.json')):
   job=json.loads(file.read_text())
   if job.get('status')=='uploaded':continue
   kind=job['kind']
   if kind in ['source','finish']:commit(job.get('message','Preserve production source checkpoint'))
   elif kind=='asset':
    local=Path(job['path']).resolve();assert ROOT in local.parents or CACHE in local.parents,'Asset outside publisher scope'
    assert local.is_file();tag=job.get('tag','session-checkpoints-2026-10-19');rel=release(tag,job.get('prerelease',True));name=job.get('name',local.name)
    existing=api('GET',f'/repos/{state["full_name"]}/releases/{rel["id"]}/assets')
    if any(x['name']==name for x in existing):raise RuntimeError('Refusing to overwrite an existing release asset; choose a new version/name: '+name)
    url=rel['upload_url'].split('{')[0];assert urlsplit(url).hostname=='uploads.github.com'
    with local.open('rb') as stream:
     response=session.post(url+'?name='+quote(name),data=stream,headers={'Content-Type':mimetypes.guess_type(name)[0] or 'application/octet-stream'},timeout=240,allow_redirects=False)
    if response.status_code!=201:raise RuntimeError('Release upload failed '+str(response.status_code))
    item=response.json();assert item['size']==local.stat().st_size
    record={'name':name,'bytes':item['size'],'id':item['id'],'tag':tag,'url':item['browser_download_url'],'sha256':hashlib.sha256(local.read_bytes()).hexdigest()}
    if item.get('digest','').startswith('sha256:'):assert item['digest'].split(':',1)[1]==record['sha256']
    state['assets'].append(record);save();log('ASSET_BACKED_UP '+name+' '+record['url'])
   else:raise RuntimeError('Unknown explicit job type')
   job.update(status='uploaded',source_commit=state.get('source_commit'));file.write_text(json.dumps(job,ensure_ascii=False,indent=2))
   if kind=='finish':state['status']='complete';save();log('PUBLISHER_COMPLETE');raise SystemExit(0)
  time.sleep(2)
except Exception as e:
 state.update(status='failed',error=safe(e));save();log('PUBLISHER_FAILED '+safe(e));raise SystemExit(1)
