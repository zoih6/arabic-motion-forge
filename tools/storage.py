from pathlib import Path
import os,json,shutil,argparse
EXCLUDED={'.arena','.cache','.local','.mypy_cache','.next','.nox','.npm','.nuxt','.output','.parcel-cache','.pytest_cache','.ruff_cache','.svelte-kit','.tox','.turbo','.venv','.vite','__pycache__','build','coverage','dist','node_modules','out','target'}
def eligible_bytes(root):
 total=0
 for folder,dirs,files in os.walk(root):
  dirs[:]=[x for x in dirs if x not in EXCLUDED]
  for name in files:
   p=Path(folder)/name
   if not p.is_symlink():
    try:total+=p.stat().st_size
    except OSError:pass
 return total
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',default=str(Path.home()));p.add_argument('--limit-mib',type=float,default=118);a=p.parse_args();n=eligible_bytes(Path(a.root));print(json.dumps({'snapshot_bytes':n,'snapshot_mib':round(n/1024**2,2),'limit_mib':a.limit_mib,'within_limit':n<=a.limit_mib*1024**2,'system_free_gib':round(shutil.disk_usage(a.root).free/1024**3,2),'cache_is_not_a_durable_backup':True},indent=2));raise SystemExit(0 if n<=a.limit_mib*1024**2 else 1)
