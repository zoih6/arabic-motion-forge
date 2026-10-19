"""Build only the explicit, non-template demonstration. Not called by project bootstrap."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'examples/vertical-showcase'
parts=[]
for file in [R/'runtime/core.mjs',R/'runtime/canvas.mjs',D/'scene.mjs']:
 s=file.read_text();s=re.sub(r'^import\s+.*?;\s*$', '',s,flags=re.M);s=re.sub(r'\bexport\s+(?=(?:const|function|class|let)\b)','',s);parts.append(s)
head='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>المعنى أولاً — دراسة حركة عربية</title><style>@font-face{font-family:'IBM Plex Sans Arabic';src:url('../../assets/fonts/IBMPlexSansArabic-SemiBold.ttf');font-weight:600;font-display:block}@font-face{font-family:'IBM Plex Sans Arabic';src:url('../../assets/fonts/IBMPlexSansArabic-Regular.ttf');font-weight:400;font-display:block}html,body{margin:0;background:#101d35;overflow:hidden}canvas{display:block;width:1080px;height:1920px}</style></head><body><canvas id="film" width="1080" height="1920"></canvas>'''
(D/'index.html').write_text(head+'<script>\n(()=>{\n'+'\n'.join(parts)+'\n})();</script></body></html>')
print('SHOWCASE_BUILT',hashlib.sha256((D/'scene.mjs').read_bytes()).hexdigest()[:12],1080,1920,32,2560)
