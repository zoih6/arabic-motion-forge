"""Explicit lightweight setup; never downloads prior films or demo media.
Run with --install to install the verified Python renderer profile.
Run with --system-deps only when OS package installation is authorized.
"""
from pathlib import Path
import sys,subprocess,argparse,json,platform,importlib.util
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--install',action='store_true');p.add_argument('--system-deps',action='store_true');p.add_argument('--transcribe',action='store_true',help='also install faster-whisper ASR backend (model weights download on first transcription)');a=p.parse_args()
required={'playwright':'playwright==1.64.0','imageio_ffmpeg':'imageio-ffmpeg==0.6.0','av':'av==16.1.0','PIL':'Pillow>=11,<13','numpy':'numpy>=2,<3','scipy':'scipy>=1.14,<2','soundfile':'soundfile>=0.13,<1','jsonschema':'jsonschema>=4,<5'}
missing=[spec for module,spec in required.items() if importlib.util.find_spec(module) is None]
print('Environment:',platform.system(),platform.machine(),'Python',sys.version.split()[0],flush=True)
print('Missing:',missing,flush=True)
extra=['faster-whisper>=1,<2'] if a.transcribe and importlib.util.find_spec('faster_whisper') is None else []
if a.install:
 if missing or extra:subprocess.run([sys.executable,'-m','pip','install','--user','--disable-pip-version-check',*missing,*extra],check=True)
 if a.system_deps:
  if platform.system()!='Linux':raise SystemExit('--system-deps is Linux-only; use the platform-specific Playwright installer.')
  subprocess.run([sys.executable,'-m','playwright','install-deps','chromium'],check=True)
 subprocess.run([sys.executable,'-m','playwright','install','chromium'],check=True)
print('No example videos, old film repositories or credentials downloaded; model weights only if --transcribe was explicitly requested.',flush=True)
