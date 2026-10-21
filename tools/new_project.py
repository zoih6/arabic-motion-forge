"""Create an EMPTY, non-template project. No inherited scene, palette, score or assets.
v2.2: seeds the spec (reframe gate), journal (resume backbone) and the direction pipeline."""
from pathlib import Path
import argparse,json,hashlib,time
p=argparse.ArgumentParser();p.add_argument('--destination',required=True);p.add_argument('--name',required=True);p.add_argument('--topic',default='');p.add_argument('--width',type=int,default=1080);p.add_argument('--height',type=int,default=1920);p.add_argument('--fps',type=int,default=32);p.add_argument('--seconds',type=float,default=60);p.add_argument('--quick',action='store_true',help='fast lane for <=30s/simple asks: spec-lite, no preview gate, same safety rules');a=p.parse_args()
r=Path(a.destination).expanduser().resolve()
if r.exists() and any(r.iterdir()):raise SystemExit('Refusing to overwrite a nonempty project.')
r.mkdir(parents=True,exist_ok=True)
def save(name,x):(r/name).write_text(json.dumps(x,ensure_ascii=False,indent=2))
(r/'copy.txt').write_text('')
save('project.json',{'id':a.name,'topic':a.topic,'kit_contract':2,'width':a.width,'height':a.height,'fps':a.fps,'frames':round(a.seconds*a.fps),'duration':round(a.seconds*a.fps)/a.fps,'requested_duration':a.seconds,'entry':'index.html','layer_plan':'layer-plan.json','copy_file':'copy.txt','copy_sha256':hashlib.sha256(b'').hexdigest(),'render_allowed':False,'approval_mode':'pending','publish_allowed':False,'publish_repository':None,'style_file':'style.json','originality_file':'originality.json','spec_file':'spec.md','preview_approved':False,'mode':'quick' if a.quick else 'full'})
save('style.json',{'palette':[],'fonts':[],'material_language':'','composition_grammar':'','camera_grammar':'','motif':'','reason_for_subject':'','type_system':{'display':'','body':'','numerals':'','size_ladder':'','broken_rule':''},'signature_move':'','forbidden_tropes':[],'escalation':''})
save('originality.json',{'declared_new_composition':False,'reference_lessons':[],'differences_from_references':[],'copied_scene_imports':[]})
save('layer-plan.json',{'scenes':[]})
save('brief.json',{'message':'','audience':'','assets':[],'narration':None,'approval':'pending','onboarding':{'status':'pending','answers':{},'source':None}})
(r/'spec.md').write_text("""# Production spec

## Objective
TODO(agent): what the film argues or feels — rewritten professionally from the user's raw words (skills/request-reframe). Never execute a vague brief literally.

## User requirements (ALL of them, numbered, verbatim essence)
TODO: every demand the user made becomes a numbered item — NOTHING is deleted; corrections ADD or CONVERT, never remove. Format: `1. [preserved|converted|corrected] <user ask> -> <how honored> (rule if changed)`

## Confirmed understanding
TODO: user intent in their own words + EVERY correction made to the literal ask with the violated rule (e.g. "animate letters" -> word-level shaped reveals per Arabic contract).

## Constraints & format
TODO: resolution/fps/duration/orientation/size budget; mark assumed vs user-fixed.

## Content & copy
TODO: verbatim on-screen strings (then copy.txt + re-hash project.json); topic facts with source URLs in research/facts.json; label anything illustrative.

## Motion & style
TODO: after the directions engine: chosen axis spine; 2.5D vs runtime/spatial.mjs 3D decision + reason (spatial-3d.json); blur/stagger policy.

## Deliverables
TODO: light<=25MiB + hi<=50MiB via tools/deliver.py into <project>/deliverables/ (never out/); preview artifact; publish yes/no.

## Assumptions (veto in one word)
TODO: bullets.

## Refusals & corrections
TODO: contradictions resolved and how; what the raw request asked that the kit contract forbids, and the professional substitute chosen.
""")
(r/'scene.mjs').write_text('// Author a new composition from the approved layer plan.\n// Do not import examples/ or previous project scene code.\nexport function drawScene(){throw new Error("Original composition has not been authored yet.");}\n')
(r/'README.md').write_text('# '+a.name+'\n\nIntentionally blank pipeline:\n1. skills/request-reframe -> fill spec.md (agent-authored, no literal obedience to messy asks)\n2. tools/direct.py --topic "..." --project . -> three directions, fill TODOs, user picks, tools/check_directions.py locks style\n3. brief.json + copy.txt approval -> layer-plan.json -> scene.mjs + index.html (canvas#film, filmReady, seek(t))\n4. tools/check_project.py -> tools/preview.py (30s approval preview; render.py gate for >30s)\n5. final render -> tools/deliver.py (workspace deliverables: light<=25MiB, hi<=50MiB; never out/)\njournal.jsonl records every step; resume = tools/journal.py tail.\nNo example scene, soundtrack or palette has been copied.\n')
(r/'journal.jsonl').write_text(json.dumps({'ts':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'kind':'boot','event':'project created by new_project.py','next':'reframe brief into spec.md, then directions'})+'\n')
print(r)
print('next: python3 tools/direct.py --topic "<subject>" --project '+str(r))
