from pathlib import Path
import argparse,json,hashlib,re
p=argparse.ArgumentParser();p.add_argument('project');a=p.parse_args();f=Path(a.project).resolve();r=f.parent;d=json.loads(f.read_text());errors=[]
for k in ['id','width','height','fps','frames','duration','entry','layer_plan','copy_file','copy_sha256']:
 if k not in d:errors.append('Missing '+k)
if not errors:
 if abs(d['frames']/d['fps']-d['duration'])>1e-8:errors.append('Frame grid mismatch')
 c=r/d['copy_file']
 if not c.exists() or not c.read_text().strip():errors.append('Approved copy is empty/missing')
 elif hashlib.sha256(c.read_bytes()).hexdigest()!=d['copy_sha256']:errors.append('Copy hash mismatch')
 l=r/d['layer_plan']
 if not l.exists():errors.append('Missing layer plan')
 else:
  plan=json.loads(l.read_text());scenes=plan.get('scenes',[])
  if not scenes:errors.append('No authored scenes')
  for s in scenes:
   layers=s.get('layers',[])
   if len(layers)<3:errors.append('Insufficient layer decomposition in '+s.get('id','?'))
   ids=[x.get('id') for x in layers]
   if len(set(ids))!=len(ids):errors.append('Duplicate layer IDs')
   signatures=set()
   for x in layers:
    if not x.get('role') or not x.get('channels'):errors.append('Layer role/channels missing')
    ti=x.get('timing',{});signatures.add((ti.get('start'),ti.get('settle_or_stage_end'),str(x.get('channels'))))
   if len(signatures)<3:errors.append('Uniform group motion rather than independent choreography')
 for s in r.rglob('*.mjs'):
  text=s.read_text()
  if re.search(r'import[^;]*(?:alhambra|examples/vertical-showcase)',text,re.I):errors.append('Forbidden scene import: '+s.name)
 if d.get('style_file'):
  style=json.loads((r/d['style_file']).read_text())
  if not style.get('palette') or not style.get('fonts') or not style.get('reason_for_subject'):errors.append('Original style decision is incomplete')
 if d.get('originality_file'):
  o=json.loads((r/d['originality_file']).read_text())
  if not o.get('declared_new_composition') or not o.get('differences_from_references'):errors.append('Originality review incomplete')
 if not (r/d['entry']).exists():errors.append('Render entry missing')
 if d.get('kit_contract',0)>=2 and d.get('mode','full')=='full':
  if (r/'spec.md').exists():
   ur=(r/'spec.md').read_text().split('## User requirements',1)[-1].split('\n## ',1)[0]
   import re as _re
   if not _re.findall(r'^\s*\d+[.)]',ur,_re.M):errors.append('spec user-requirements section has no numbered items')
  st=r/d['style_file']
  if st.exists():
   sv=json.loads(st.read_text())
   ts=sv.get('type_system') or {}
   if not (ts.get('display') and ts.get('body') and sv.get('signature_move') and sv.get('forbidden_tropes') and sv.get('escalation')):
    errors.append('Full mode: style.json needs type_system(display+body), signature_move, forbidden_tropes[], escalation — the anti-superficiality fields')
 if d.get('layer_plan') and (r/d['layer_plan']).exists():
  plan2=json.loads((r/d['layer_plan']).read_text())
  quick=d.get('mode')=='quick'
  for sc in plan2.get('scenes',[]):
   ly=sc.get('layers',[])
   if len(ly)<(3 if quick else 4):errors.append('scene '+str(sc.get('id'))+': needs >=%d independent layers'%(3 if quick else 4))
   starts={x.get('timing',{}).get('start') for x in ly if x.get('timing')}
   if len(starts)<max(2,len(ly)-1):errors.append('scene '+str(sc.get('id'))+': entrances not staggered (unique start times %d of %d layers)'%(len(starts),len(ly)))
 if d.get('kit_contract',0)>=2:
  if d.get('mode','full')=='quick':
   spec=(r/d.get('spec_file','spec.md')).read_text() if (r/d.get('spec_file','spec.md')).exists() else ''
   if '## User requirements' not in spec:errors.append('quick mode still requires numbered user-requirements section')
  sf=r/d.get('spec_file','spec.md')
  if not sf.exists():errors.append('Reframe gate: spec.md missing (skills/request-reframe)')
  else:
   spec=sf.read_text()
   secs=['## User requirements','## Objective','## Constraints & format','## Deliverables'] if d.get('mode')=='quick' else ['## User requirements','## Objective','## Confirmed understanding','## Constraints & format','## Content & copy','## Motion & style','## Deliverables','## Refusals & corrections']
   for sec in secs:
    body=spec.split(sec,1)[-1].split('\n## ',1)[0] if sec in spec else ''
    if len(body.strip())<25 or 'TODO' in body:errors.append('spec.md section unresolved: '+sec)
kit=Path(__file__).resolve().parents[1]
baselines=json.loads((kit/'catalog/originality-baselines.json').read_text())
protected={x['sha256'] for x in baselines['protected_scene_hashes']}
for source in r.rglob('*.mjs'):
 if hashlib.sha256(source.read_bytes()).hexdigest() in protected:errors.append('Copied protected scene code: '+source.name)
if d.get('style_file') and (r/d['style_file']).exists():
 style=json.loads((r/d['style_file']).read_text())
 for reference in baselines['protected_styles']:
  keys=['palette','fonts','material_language','composition_grammar','camera_grammar','motif']
  if sum(bool(style.get(k)) and style.get(k)==reference.get(k) for k in keys)>=4:errors.append('Style fingerprint copies a reference; author a new direction')
print(json.dumps({'passed':not errors,'errors':errors,'limit':'Heuristics and source contracts do not prove semantic originality; visual review remains required.'},ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
