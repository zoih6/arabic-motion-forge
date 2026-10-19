"""An original procedural score/SFX for this demonstration only, not a reusable brand soundtrack."""
from pathlib import Path
import json,subprocess,re
import numpy as np,soundfile as sf,imageio_ffmpeg
R=Path(__file__).resolve().parents[1];CACHE=Path.home()/'.cache/motion-forge-session';CACHE.mkdir(parents=True,exist_ok=True)
SR=48000;DUR=80;N=SR*DUR;mix=np.zeros((N,2),dtype='float32');rng=np.random.default_rng(20261019);cues=[]
def add(y,start,level=1,pan=0):
 i=round(start*SR);n=min(len(y),N-i)
 if n<=0:return
 gains=np.array([np.sqrt((1-pan)/2),np.sqrt((1+pan)/2)],dtype='float32');mix[i:i+n]+=y[:n,None]*level*gains
for b in range(160):
 when=b*.5
 t=np.arange(int(.26*SR))/SR
 kick=np.sin(2*np.pi*(47*t+4*(1-np.exp(-t*28))))*np.exp(-t*18)
 add(kick,when,.14 if b%4==0 else .075)
 h=rng.standard_normal(int(.045*SR));h=np.diff(h,prepend=0);tt=np.arange(len(h))/SR;add(h*np.exp(-tt*95),when+.25,.010,(-1 if b%2 else 1)*.38)
 if b%2==1:
  n=int(.10*SR);t=np.arange(n)/SR;noise=rng.standard_normal(n);add(noise*np.exp(-t*40),when,.017)
# Sparse harmonic progression, not a copy of a reference song.
roots=[146.832,164.814,130.813,146.832]
for k in range(40):
 root=roots[(k//5)%4];t=np.arange(int(2.8*SR))/SR;env=np.minimum(1,t/.12)*np.exp(-t*.9)
 tone=(np.sin(2*np.pi*root*t)+.32*np.sin(2*np.pi*root*1.5*t)+.18*np.sin(2*np.pi*root*2*t))*env
 add(tone,k*2,.032, .12*np.sin(k))
for s in range(8):
 for j,offset in enumerate([.20,1.45,2.05,3.4,5.2,6.8]):
  at=s*10+offset;t=np.arange(int(.10*SR))/SR;freq=600+100*j;y=np.sin(2*np.pi*freq*t)*np.exp(-t*52);add(y,at,.025,(-1 if j%2 else 1)*.2);cues.append({'time':at,'type':'text/path accent','not_voice':True})
for at in [9,19.2,29.3,49.35,57.05,65.8,75.5]:
 t=np.arange(int(.6*SR))/SR;n=rng.standard_normal(len(t));n=np.convolve(n,np.ones(19)/19,mode='same');env=np.sin(np.pi*t/.6)**2;add(n*env,at,.033);cues.append({'time':at,'type':'designed handoff'})
fade=np.minimum(1,np.arange(N)/(SR*.8))*np.minimum(1,(N-1-np.arange(N))/(SR*1.1));mix*=np.maximum(0,fade[:,None]);assert np.max(np.abs(mix))<1
raw=CACHE/'showcase-premix.wav';sf.write(raw,mix,SR,subtype='PCM_24');ff=imageio_ffmpeg.get_ffmpeg_exe()
def stats(path):
 q=subprocess.run([ff,'-hide_banner','-i',str(path),'-af','loudnorm=I=-14:TP=-2.3:LRA=8:print_format=json','-f','null','-'],capture_output=True,text=True,check=True);return json.loads(re.findall(r'\{\s*"input_i"[\s\S]*?\}',q.stderr)[-1])
a=stats(raw);flt=f'loudnorm=I=-14:TP=-2.3:LRA=8:measured_I={a["input_i"]}:measured_TP={a["input_tp"]}:measured_LRA={a["input_lra"]}:measured_thresh={a["input_thresh"]}:offset={a["target_offset"]}:linear=true'
final=CACHE/'showcase-audio.m4a';subprocess.run([ff,'-y','-v','error','-i',str(raw),'-af',flt,'-ar',str(SR),'-c:a','aac','-b:a','160k',str(final)],check=True);b=stats(final)
(R/'examples/vertical-showcase/audio-cues.json').write_text(json.dumps({'bpm':120,'beats_seconds':[i*.5 for i in range(160)],'sfx':cues,'composition':'original procedural demonstration score; do not inherit into a new project','narration':None},indent=2))
(R/'research/showcase-audio.json').write_text(json.dumps({'measured_lufs':float(b['input_i']),'measured_true_peak_dbtp':float(b['input_tp']),'duration':80,'sample_rate':SR,'source':'original procedural synthesis','path':str(final)},indent=2));print('SCORE_READY',b['input_i'],'LUFS',b['input_tp'],'dBTP',flush=True)
