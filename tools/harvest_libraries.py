"""Small, read-only upstream audit. No repository clones, templates or media downloads."""
from pathlib import Path
import json,subprocess,hashlib,time
import requests
ROOT=Path(__file__).resolve().parents[1]
repos=[('animejs','juliangarnier/anime','MIT'),('motion','motiondivision/motion','MIT'),('motion-canvas','motion-canvas/motion-canvas','MIT'),('pixijs','pixijs/pixijs','MIT'),('threejs','mrdoob/three.js','MIT'),('lottie-web','airbnb/lottie-web','MIT'),('gsap','greensock/GSAP','custom'),('remotion','remotion-dev/remotion','custom'),('bezier-easing','gre/bezier-easing','MIT'),('svg-path-properties','rveciana/svg-path-properties','ISC'),('flubber','veltman/flubber','MIT'),('harfbuzzjs','harfbuzz/harfbuzzjs','MIT'),('opentypejs','opentypejs/opentype.js','MIT'),('d3-ease','d3/d3-ease','ISC'),('d3-shape','d3/d3-shape','ISC'),('d3-interpolate','d3/d3-interpolate','ISC'),('popmotion','popmotion/popmotion','MIT'),('roughjs','rough-stuff/rough','MIT'),('revideo','redotvideo/revideo','MIT'),('theatrejs','theatre-js/theatre','review'),('motion-studio-reference','estebantobon/motion-studio','MIT'),('gsap-skills-reference','greensock/gsap-skills','review')]
records=[];session=requests.Session();session.headers['User-Agent']='ArabicMotionForge research (source-license audit; no bulk media download)'
for name,repo,expected in repos:
 rec={'id':name,'repository':'https://github.com/'+repo,'verified_on':'2026-10-19','runtime_tested':False,'default_install':False,'expected_license_not_authoritative':expected}
 try:
  p=subprocess.run(['git','ls-remote','https://github.com/'+repo+'.git','HEAD'],capture_output=True,text=True,timeout=35,check=True);sha=p.stdout.split()[0];rec['commit']=sha
  for file in ['LICENSE','LICENSE.md','LICENSE.txt','license','COPYING']:
   url=f'https://raw.githubusercontent.com/{repo}/{sha}/{file}';r=session.get(url,timeout=20)
   if r.status_code==200:
    text=r.text;rec.update(license_path=file,license_url=url,license_sha256=hashlib.sha256(r.content).hexdigest(),license_excerpt=text[:220])
    if 'GNU AFFERO GENERAL PUBLIC LICENSE' in text:rec['license_class']='AGPL-3.0'
    elif 'GNU GENERAL PUBLIC LICENSE' in text:rec['license_class']='GPL-family-review'
    elif 'Permission is hereby granted, free of charge' in text and 'Remotion License' not in text:rec['license_class']='MIT-like-verify-notice'
    elif 'Permission to use, copy, modify, and/or distribute' in text:rec['license_class']='ISC-like-verify-notice'
    elif name=='gsap':rec['license_class']='GSAP-custom-not-OSI'
    elif name=='remotion':rec['license_class']='Remotion-custom-source-available'
    else:rec['license_class']='custom-or-needs-review'
    # Only legal notices, not full articles or third-party creative templates, are preserved.
    dest=ROOT/'research/upstream-licenses'/f'{name}.txt';dest.parent.mkdir(exist_ok=True);dest.write_text(text);break
  if 'license_path' not in rec:rec['license_class']='not-found-do-not-assume'
  r=session.get(f'https://raw.githubusercontent.com/{repo}/{sha}/package.json',timeout=20)
  if r.status_code==200:
   pkg=r.json();rec.update(package_name=pkg.get('name'),package_version=pkg.get('version'),package_license=pkg.get('license'))
  rec['audit_status']='source-and-license-inspected'
 except Exception as e:rec.update(audit_status='incomplete',error=str(e)[:180])
 records.append(rec);(ROOT/'catalog/libraries.lock.json').write_text(json.dumps(records,ensure_ascii=False,indent=2));print(name,rec.get('commit','')[:12],rec.get('license_class'),rec['audit_status'],flush=True)
print('LIBRARY_AUDIT_COMPLETE',len(records),flush=True)
