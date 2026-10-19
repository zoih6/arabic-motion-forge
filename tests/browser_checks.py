from pathlib import Path
import json,re,hashlib
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];T=Path.home()/'.cache/motion-forge-session/browser-tests';T.mkdir(parents=True,exist_ok=True)
source='\n'.join(re.sub(r'^import\s+.*?;\s*$','',p.read_text(),flags=re.M).replace('export ','') for p in [R/'runtime/core.mjs',R/'runtime/canvas.mjs'])
tests=r'''
window.runChecks=async()=>{
 await document.fonts.load('600 110px "IBM Plex Sans Arabic"','لا للتكرار');
 const results=[];const check=(name,value,detail=null)=>{results.push({name,pass:!!value,detail});if(!value)throw new Error(name);};
 const bytes=c=>c.getContext('2d').getImageData(0,0,c.width,c.height).data;
 const alpha=c=>{let n=0;const d=bytes(c);for(let i=3;i<d.length;i+=4)n+=d[i];return n;};
 for(const text of ['لا تكرار','المعنى أولاً','الطريق إلى ٢٠٢٦']){
  const s=textSprite(text,{size:110,family:'IBM Plex Sans Arabic',weight:600});
  const empty=rtlMatte(s,0,{slant:65,bands:4});check('matte zero is transparent: '+text,alpha(empty)===0);
  const full=rtlMatte(s,1,{slant:65,bands:4});const a=bytes(s.canvas),b=bytes(full);check('full matte preserves every shaped pixel: '+text,a.length===b.length&&a.every((x,i)=>x===b[i]));
  const half=rtlMatte(s,.5,{slant:65,bands:4});check('partial matte is neither empty nor full: '+text,alpha(half)>0&&alpha(half)<alpha(full));
  check('glyph bounds reserve diacritics/descent: '+text,s.height>110&&s.width>0);
 }
 const fill=surface(2,1),f=fill.getContext('2d');f.fillStyle='blue';f.fillRect(0,0,2,1);const matte=surface(2,1),m=matte.getContext('2d');m.fillStyle='black';m.fillRect(0,0,1,1);m.fillStyle='white';m.fillRect(1,0,1,1);const l=lumaMatte(fill,matte),v=bytes(l);check('defined luma matte black/white endpoints',v[3]===0&&v[7]===255);
 const p=pathMetrics([[20,20],[120,20],[120,120]]),c=surface(160,160),g=c.getContext('2d');strokePath(g,p,.75,{color:'#fff',width:5,head:true});const img=bytes(c);check('trim path leaves untraversed endpoint transparent',img[(119*160+120)*4+3]===0);check('trim path paints its moving endpoint',img[(70*160+120)*4+3]>0);
 const sharp=surface(240,90),sg=sharp.getContext('2d');sg.fillRect(100,30,20,20);const blur=surface(240,90);
 temporalAverage(blur,.5,32,4,(cg,t)=>{cg.fillStyle='black';cg.fillRect(100+(t-.5)*1200,30,20,20);},{angle:180});
 const box=c=>{const d=bytes(c);let left=c.width,right=-1,partials=0;for(let y=0;y<c.height;y++)for(let x=0;x<c.width;x++){const a=d[(y*c.width+x)*4+3];if(a){left=Math.min(left,x);right=Math.max(right,x);if(a<255)partials++;}}return{width:right-left+1,partials};};
 check('real temporal blur expands moving coverage',box(blur).width>box(sharp).width+8,box(blur));check('temporal blur has partial exposure alpha',box(blur).partials>0);check('temporal blur approximately conserves coverage',Math.abs(alpha(blur)-alpha(sharp))/alpha(sharp)<.04);
 return results;
};
'''
html=f'''<!doctype html><style>@font-face{{font-family:'IBM Plex Sans Arabic';src:url('{(R/'assets/fonts/IBMPlexSansArabic-SemiBold.ttf').as_uri()}');font-weight:600}}</style><script>{source}\n{tests}</script>'''
(T/'fixture.html').write_text(html)
with sync_playwright() as p:
 b=p.chromium.launch(args=['--no-sandbox','--disable-dev-shm-usage','--allow-file-access-from-files']);page=b.new_page();page.add_init_script("window.requestAnimationFrame=()=>{throw new Error('real-time animation loop forbidden in this export test')}");page.goto((T/'fixture.html').as_uri());result=page.evaluate('()=>runChecks()');b.close()
report={'runtime':'Playwright Chromium','checks':result,'passed':sum(x['pass'] for x in result),'native_after_effects_executed':False};(R/'research/browser-tests.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('BROWSER_CHECKS_PASSED',report['passed'])
