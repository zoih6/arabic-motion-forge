"""Create an EMPTY, non-template project. No inherited scene, palette, score or assets.
v2: seeds the journal (resume backbone) and the direction-gate pipeline."""
from pathlib import Path
import argparse,json,hashlib,time
p=argparse.ArgumentParser();p.add_argument('--destination',required=True);p.add_argument('--name',required=True);p.add_argument('--topic',default='');p.add_argument('--width',type=int,default=1080);p.add_argument('--height',type=int,default=1920);p.add_argument('--fps',type=int,default=32);p.add_argument('--seconds',type=float,default=60);p.add_argument('--kit',default=None,help='kit root for tools/direct.py hints');a=p.parse_args()
r=Path(a.destination).expanduser().resolve()
if r.exists() and any(r.iterdir()):raise SystemExit('Refusing to overwrite a nonempty project.')
r.mkdir(parents=True,exist_ok=True)
def save(name,x):(r/name).write_text(json.dumps(x,ensure_ascii=False,indent=2))
(r/'copy.txt').write_text('')
save('project.json',{'id':a.name,'topic':a.topic,'kit_contract':2,'width':a.width,'height':a.height,'fps':a.fps,'frames':round(a.seconds*a.fps),'duration':round(a.seconds*a.fps)/a.fps,'requested_duration':a.seconds,'entry':'index.html','layer_plan':'layer-plan.json','copy_file':'copy.txt','copy_sha256':hashlib.sha256(b'').hexdigest(),'render_allowed':False,'approval_mode':'pending','publish_allowed':False,'publish_repository':None,'style_file':'style.json','originality_file':'originality.json'})
save('style.json',{'palette':[],'fonts':[],'material_language':'','composition_grammar':'','camera_grammar':'','motif':'','reason_for_subject':''})
save('originality.json',{'declared_new_composition':False,'reference_lessons':[],'differences_from_references':[],'copied_scene_imports':[]})
save('layer-plan.json',{'scenes':[]})
save('brief.json',{'message':'','audience':'','assets':[],'narration':None,'approval':'pending'})
(r/'scene.mjs').write_text('// Author a new composition from the approved layer plan.\n// Do not import examples/ or previous project scene code.\nexport function drawScene(){throw new Error("Original composition has not been authored yet.");}\n')
(r/'README.md').write_text('# '+a.name+'\n\nThis is intentionally blank. Workflow: brief.json -> `tools/direct.py --topic "..." --project .` -> fill TODOs -> `tools/check_directions.py project.json` -> layer-plan.json + scene -> `tools/check_project.py project.json` -> draft tier render -> QA -> final. copy.txt holds approved on-screen text verbatim (one line per string); project.json locks its hash at approval. journal.jsonl records every milestone; resume by reading its tail.\n')
(r/'journal.jsonl').write_text(json.dumps({'ts':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'kind':'boot','event':'project created by new_project.py','next':'brief + directions'})+'\n')
print(r)
print('next: python3 tools/direct.py --topic "<subject>" --project '+str(r))
