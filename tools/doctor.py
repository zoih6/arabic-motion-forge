from pathlib import Path
import importlib.util,importlib.metadata,platform,shutil,sys,json,argparse
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');a=p.parse_args()
modules={'playwright':'playwright','PIL':'Pillow','numpy':'numpy','scipy':'scipy','soundfile':'soundfile','av':'av','imageio_ffmpeg':'imageio-ffmpeg'}
found={}
for module,package in modules.items():
 ok=importlib.util.find_spec(module) is not None
 try:version=importlib.metadata.version(package) if ok else None
 except importlib.metadata.PackageNotFoundError:version='unknown'
 found[module]={'available':ok,'version':version}
result={'python':sys.version.split()[0],'os':platform.system(),'node_path':shutil.which('node'),'git_path':shutil.which('git'),'modules':found,'fonts_present':all((R/'assets/fonts'/n).exists() for n in ['IBMPlexSansArabic-Regular.ttf','IBMPlexSansArabic-SemiBold.ttf']),'native_AE_on_PATH':shutil.which('aerender'),'native_AE_executed':False,'claude_on_PATH':shutil.which('claude'),'codex_on_PATH':shutil.which('codex'),'note':'Discovery is scoped to this environment/PATH. A manifest or installed library is not proof that all engines or providers work.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
