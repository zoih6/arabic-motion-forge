"""Install a lightweight LOCAL skill adapter without copying the kit or any media.
This installs a skill entry, not a native plugin or authenticated model session.
"""
from pathlib import Path
import argparse
p=argparse.ArgumentParser();p.add_argument('--project',required=True);p.add_argument('--host',choices=['codex','claude-skill','generic'],required=True);p.add_argument('--kit',default=str(Path(__file__).resolve().parents[1]));a=p.parse_args()
kit=Path(a.kit).expanduser().resolve();project=Path(a.project).expanduser().resolve();assert (kit/'AGENTS.md').is_file() and (kit/'SKILL.md').is_file()
if a.host=='generic':dest=project/'MOTION-FORGE.md'
else:dest=project/('.agents' if a.host=='codex' else '.claude')/'skills/arabic-motion-forge/SKILL.md'
dest.parent.mkdir(parents=True,exist_ok=True)
text='---\nname: arabic-motion-forge\ndescription: Original Arabic motion production with independent layers, correct shaping, deterministic rendering and verified delivery.\n---\n\nRead '+str(kit/'AGENTS.md')+' then '+str(kit/'SKILL.md')+'.\nUse the kit at '+str(kit)+', but keep the new project in '+str(project)+'.\nNever import example scene compositions. No credentials or heavy demo media are installed by this adapter.\n'
if dest.exists() and dest.read_text()!=text:raise SystemExit('Existing adapter differs; refusing to overwrite it.')
dest.write_text(text);print(dest);print('Local skill adapter installed; native host execution is not implied.')
