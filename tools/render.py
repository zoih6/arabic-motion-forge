"""Generic deterministic frame-to-video exporter. It contains no scene composition.
Examples: python tools/render.py --project examples/vertical-showcase/project.json --audio /path/mix.m4a --publish-session ~/.cache/motion-forge-session
Without --publish-session no publication is performed. Media is never committed to the source tree.
"""
from pathlib import Path
import argparse,json,subprocess,time,base64,hashlib,shutil,math,os
import av,imageio_ffmpeg
from playwright.sync_api import sync_playwright
KIT=Path(__file__).resolve().parents[1]
P=argparse.ArgumentParser();P.add_argument('--project',required=True);P.add_argument('--audio');P.add_argument('--publish-session');P.add_argument('--output');P.add_argument('--chunk-seconds',type=float,default=10);P.add_argument('--crf',type=int,default=18);P.add_argument('--workspace-root',default=str(Path.home()));P.add_argument('--snapshot-limit-mib',type=float,default=118);a=P.parse_args()
PROJECT=Path(a.project).resolve();ROOT=PROJECT.parent;cfg=json.loads(PROJECT.read_text());fps=int(cfg['fps']);total=int(cfg['frames']);entry=(ROOT/cfg['entry']).resolve()
assert cfg.get('render_allowed') is True,'Explicit render approval is required.'
assert abs(total/fps-cfg['duration'])<1e-8,'Duration must explicitly match the frame grid.'
assert (ROOT/cfg['layer_plan']).exists(),'Layer plan required before production rendering.'
copy=(ROOT/cfg['copy_file']).read_bytes();assert hashlib.sha256(copy).hexdigest()==cfg['copy_sha256'],'Approved copy hash changed.'
allowed=set(copy.decode().splitlines());BUILD=hashlib.sha256(entry.read_bytes()+PROJECT.read_bytes()).hexdigest()[:10]
SESSION=Path(a.publish_session).expanduser().resolve() if a.publish_session else Path.home()/'.cache/motion-forge-session'
WORK=SESSION/'renders'/cfg['id']/BUILD;WORK.mkdir(parents=True,exist_ok=True);FF=imageio_ffmpeg.get_ffmpeg_exe();AUDIO=Path(a.audio).resolve() if a.audio else None
report={'project_id':cfg['id'],'build':BUILD,'status':'rendering','fps':fps,'width':cfg['width'],'height':cfg['height'],'frames':total,'duration':total/fps,'segments':[],'publish_requested':bool(a.publish_session),'copy_checked_against':cfg['copy_file'],'source_entry_sha256':hashlib.sha256(entry.read_bytes()).hexdigest()}
REPORT=ROOT/'render-report.json'
def save():
 temp=REPORT.with_suffix('.pending');temp.write_text(json.dumps(report,ensure_ascii=False,indent=2));temp.replace(REPORT)
def info(path):
 with av.open(str(path)) as c:
  v=c.streams.video[0]
  return {'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'frames':int(v.frames),'fps':float(v.average_rate),'width':v.width,'height':v.height,'start':float(v.start_time*v.time_base) if v.start_time else 0,'duration':float(v.duration*v.time_base),'audio_streams':len(c.streams.audio)}
def checkpoint(path,name):
 if not a.publish_session:return None
 q=SESSION/'publish-queue';q.mkdir(exist_ok=True);p=q/(name+'.json');temp=p.with_suffix('.pending')
 job={'kind':'asset','path':str(path),'name':name+'.mp4','tag':'session-checkpoints-2026-10-19','prerelease':True}
 temp.write_text(json.dumps(job));temp.replace(p);started=time.monotonic()
 while time.monotonic()-started<300:
  try:
   result=json.loads(p.read_text())
   if result.get('status')=='uploaded':return {'job':p.name,'source_commit':result.get('source_commit'),'release_tag':job['tag'],'asset_name':job['name']}
  except json.JSONDecodeError:pass
  time.sleep(1)
 raise RuntimeError('Checkpoint publication not confirmed; pause and preserve local files.')
try:
 save();step=round(a.chunk_seconds*fps);errors=[];start=time.monotonic()
 with sync_playwright() as p:
  browser=p.chromium.launch(args=['--no-sandbox','--disable-dev-shm-usage','--allow-file-access-from-files']);page=browser.new_page(viewport={'width':cfg['width'],'height':cfg['height']},device_scale_factor=1);page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(entry.as_uri());page.evaluate('()=>filmReady')
  for idx,first in enumerate(range(0,total,step)):
   count=min(step,total-first);target=WORK/f'part-{idx+1:03}.mp4';logfile=WORK/f'part-{idx+1:03}.log'
   cmd=[FF,'-y','-hide_banner','-loglevel','warning','-threads','1','-f','image2pipe','-vcodec','mjpeg','-framerate',str(fps),'-i','pipe:0']
   if AUDIO:cmd+=['-ss',str(first/fps),'-i',str(AUDIO),'-map','0:v:0','-map','1:a:0','-c:a','aac','-b:a','160k','-ar','48000']
   else:cmd+=['-an']
   cmd+=['-frames:v',str(count),'-t',str(count/fps),'-c:v','libx264','-preset','veryfast','-crf',str(a.crf),'-pix_fmt','yuv420p','-r',str(fps),'-g',str(fps*2),'-threads','2','-movflags','+faststart',str(target)]
   print('RENDER_CHECKPOINT',idx+1,first/fps,(first+count)/fps,flush=True);stamp=time.monotonic()
   with logfile.open('wb') as log:
    encoder=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=log,stdout=subprocess.DEVNULL)
    try:
     for frame in range(first,first+count):
      value=page.evaluate('(t)=>{seek(t);return {jpg:document.getElementById("film").toDataURL("image/jpeg",.96).split(",")[1],text:(window.MF_LAST_FRAME_LAYERS||[]).filter(x=>x.text).map(x=>x.text)}}',frame/fps)
      if any(text not in allowed for text in value['text']):raise RuntimeError('Rendered unapproved text: '+repr([x for x in value['text'] if x not in allowed]))
      encoder.stdin.write(base64.b64decode(value['jpg']))
    finally:encoder.stdin.close()
    code=encoder.wait(timeout=120)
   if code or errors:raise RuntimeError('Encoder/browser error: '+str(errors)+' '+logfile.read_text()[-1200:])
   data=info(target);assert data['frames']==count and data['fps']==fps and data['width']==cfg['width'] and data['height']==cfg['height'],data
   data.update(file=str(target),frame_in=first,frame_out=first+count,elapsed=round(time.monotonic()-stamp,2));asset=f'{cfg["id"]}-{BUILD}-p{idx+1:02}-{data["sha256"][:8]}'
   data['backup']=checkpoint(target,asset);report['segments'].append(data);save();print('CHECKPOINT_VERIFIED',idx+1,data['bytes'],flush=True)
  browser.close()
 # Stream-copy video-only pieces to avoid per-piece AAC priming and concat start shifts.
 concat=WORK/'concat.txt';records=[]
 for i,s in enumerate(report['segments']):
  silent=WORK/f'video-{i+1:03}.mp4';subprocess.run([FF,'-y','-v','error','-i',s['file'],'-map','0:v:0','-an','-c:v','copy','-avoid_negative_ts','disabled',str(silent)],check=True)
  assert abs(info(silent)['start'])<1/fps/8
  records.extend([f"file '{silent}'",f'duration {(s["frame_out"]-s["frame_in"])/fps:.8f}'])
 concat.write_text('\n'.join(records)+'\n');master=WORK/'final.mp4'
 cmd=[FF,'-y','-v','warning','-copyts','-f','concat','-safe','0','-i',str(concat)]
 if AUDIO:cmd+=['-i',str(AUDIO),'-map','0:v:0','-map','1:a:0','-c:a','copy']
 else:cmd+=['-map','0:v:0','-an']
 cmd+=['-c:v','copy','-t',str(total/fps),'-avoid_negative_ts','disabled','-movflags','+faststart','-metadata','title='+cfg.get('title',cfg['id']),str(master)]
 subprocess.run(cmd,check=True);meta=info(master);assert meta['frames']==total and meta['fps']==fps
 with av.open(str(master)) as c:
  stream=c.streams.video[0];pts=sorted(p.pts for p in c.demux(stream) if p.pts is not None);delta=1/(fps*float(stream.time_base));assert len(pts)==total and all(abs(y-x-delta)<1e-6 for x,y in zip(pts,pts[1:]))
 decode=subprocess.run([FF,'-v','error','-i',str(master),'-f','null','-'],capture_output=True,text=True,timeout=600);assert decode.returncode==0 and not decode.stderr.strip(),decode.stderr
 if a.output:
  from storage import eligible_bytes
  output=Path(a.output).resolve();output.parent.mkdir(parents=True,exist_ok=True)
  if output.exists() and hashlib.sha256(output.read_bytes()).hexdigest()!=meta['sha256']:raise RuntimeError('Refusing to overwrite an existing delivery; use a new path or archive the verified previous version first.')
  increase=0 if output.exists() else master.stat().st_size
  if eligible_bytes(Path(a.workspace_root))+increase>a.snapshot_limit_mib*1024**2:raise RuntimeError('Persistent snapshot budget exceeded; master remains safely staged. Publish it before choosing a smaller same-resolution delivery.')
  shutil.copy2(master,output)
 else:output=master
 report.update(status='rendered_media_checks_passed',master=meta,output=str(output),pts_constant=True,full_decode=True,elapsed_total=round(time.monotonic()-start,2));save();print('RENDER_COMPLETE',json.dumps({'output':str(output),**meta},ensure_ascii=False),flush=True)
except Exception as e:
 report.update(status='paused_on_error',error=str(e));save();print('RENDER_PAUSED',str(e),flush=True);raise
