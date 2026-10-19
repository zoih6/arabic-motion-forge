/* ORIGINAL DEMONSTRATION COMPOSITION — NOT A PROJECT TEMPLATE.
   Do not import, recolor, retitle, or reuse this scene sequence for a different topic.
   Reusable primitives live in runtime/. This composition is intentionally excluded from core installation. */
import {clamp,lerp,smooth,smoother,eases,cubicBezier,track,spring,springPresets,ballistic,inertia,noise,recoil,stagger,cubicPath,pathMetrics,pathPoint,morphContours,radialShape,derivative} from '../../runtime/core.mjs';
import {surface,textSprite,fitText,maskedSprite,rtlMatte,irisMatte,strokePath,poly,independentShadow,temporalAverage,wordLayout} from '../../runtime/canvas.mjs';
const W=1080,H=1920,FPS=32,DURATION=80;
const C={ink:'#101d35',blue:'#245bff',lime:'#d7f85b',ice:'#f3f7ff',muted:'#7c91b8',cyan:'#70d8ef'};
const cache=new Map(),masks=new Map(),layers=[];
const ease=cubicBezier(.18,.05,.16,1),exit=cubicBezier(.55,0,.95,.6);
const cn=document.getElementById('film'),ctx=cn.getContext('2d',{alpha:false});
const blurLayer=surface(W,H),blurScratch=surface(W,H);
function p(t,a,d=1,f=ease){return f(clamp((t-a)/d));}
function note(id,type,state){const item={id,type,...state},at=layers.findIndex(x=>x.id===id);if(at<0)layers.push(item);else layers[at]=item;}
function sprite(id,text,size,color,width=900,weight=600){const key=[id,text,size,color,width,weight].join('|');if(!cache.has(key))cache.set(key,fitText(text,width,{size,family:'IBM Plex Sans Arabic',weight,color,padding:28}));return cache.get(key);}
function label(g,id,text,x,y,size,color,reveal=1,{mode='bands',slant=24,bands=3,rotation=0,scale=1,width=900,weight=600,alpha=1}={}){
 const s=sprite(id,text,size,color,width,weight);let target=masks.get(id);if(!target||target.width!==s.width||target.height!==s.height){target=surface(s.width,s.height);masks.set(id,target);}
 const image=mode==='iris'?irisMatte(s,reveal,target):rtlMatte(s,reveal,{slant,bands:mode==='plain'?1:bands,target});
 g.save();g.translate(x,y);g.rotate(rotation);g.scale(scale,scale);g.globalAlpha*=alpha;g.drawImage(image,-s.width/2,-s.height/2);g.restore();note(id,'shaped-text',{text,x,y,reveal,rotation,scale,granularity:'whole-shaped-run/matte'});
}
function rect(g,id,x,y,w,h,color,rotation=0){g.save();g.translate(x,y);g.rotate(rotation);g.fillStyle=color;g.fillRect(-w/2,-h/2,w,h);g.restore();note(id,'shape',{x,y,w,h,rotation});}
function disc(g,id,x,y,r,color){g.beginPath();g.arc(x,y,Math.max(.01,r),0,Math.PI*2);g.fillStyle=color;g.fill();note(id,'shape',{x,y,r});}
function line(g,id,pts,progress,color,width=8,head=false){const path=pathMetrics(pts);strokePath(g,path,progress,{color,width,head});const end=pathPoint(path,progress);note(id,'trimmed-path',{progress,end:{x:end.x,y:end.y},head});return end;}
function chapter(g,title,t,color){label(g,'chapter-'+title,title,540,235,52,color,p(t,.18,.65),{width:900,weight:400,bands:1,slant:0});}
function background(g,color){g.fillStyle=color;g.fillRect(0,0,W,H);}
function glyphPattern(g,t,color,alpha=.13){g.save();g.globalAlpha=alpha;for(let i=0;i<8;i++){const x=90+i*145;g.strokeStyle=color;g.lineWidth=2;g.beginPath();g.moveTo(x,-60);g.lineTo(x-120,1980);g.stroke();}g.restore();}
function opening(g,t){
 background(g,C.ink);
 // The field, title matte, secondary text, ray, and route have separate timing and geometry.
 const sweep=p(t,0,.9);rect(g,'entry-field',1080-540*sweep,960,1080*sweep,1920,C.blue);
 rect(g,'entry-rail',90,950,18,1300*p(t,.35,1.05),C.lime);
 label(g,'entry-title','الحركة',555,625,280,C.ice,p(t,.2,1.2),{width:870,bands:4,slant:85});
 label(g,'entry-thesis','ليست زينة',550,940,176,C.lime,p(t,1.45,1.0),{width:900,bands:2,slant:-65});
 const end=line(g,'entry-rule',cubicPath([940,1150],[880,1260],[260,1080],[180,1290]),p(t,2.05,1.2),C.ice,11,true);
 const arrival=spring(t-3.0,springPresets.soft);disc(g,'entry-anchor',end.x,1320-95*(1-arrival),38,C.ink);
 label(g,'entry-message','إنها قرار بصري',555,1450,71,C.ice,p(t,3.0,.9),{width:820,weight:400});
 if(t>5.2){label(g,'entry-detail','اتجاه  •  هدف  •  معنى',550,1640,49,C.ice,p(t,5.2,1.05),{weight:400,bands:1});}
 // An independently animated surface occludes the next composition, not a flattened poster pan.
 if(t>8.9){const u=p(t,8.9,1.1);poly(g,[[1080,0],[1080,1920],[1080-1240*u,1920],[1080-1200*u,0]],{fill:C.ice});note('entry-outgoing-occluder','shape',{u});}
}
function physics(g,t){
 background(g,C.ice);chapter(g,'النابض والوزن',t,C.ink);
 label(g,'physics-a','وزن',550,545,257,C.ink,p(t,.22,.9),{width:850,bands:2,slant:35});
 label(g,'physics-b','وإيقاع',545,805,218,C.blue,p(t,.9,1.1),{width:900,bands:3,slant:-35});
 const h=ballistic(Math.max(0,t-1.3),{height:320,gravity:1800,restitution:.47});const landing=Math.sqrt(640/1800);
 const impact=Math.max(0,1-Math.abs((t-1.3)-landing)/.10),sx=1+impact*.20,sy=1-impact*.21;
 independentShadow(g,{x:310,y:1414,width:180,height:0,elevation:h*.55,opacity:.23});note('ball-shadow','independent-shadow',{elevation:h});
 g.save();g.translate(310,1350-h);g.scale(sx,sy);disc(g,'gravity-ball',0,0,76,C.blue);g.restore();
 const y2=1120+226*spring(t-1.65,springPresets.heavy);
 independentShadow(g,{x:750,y:1414,width:180,height:0,elevation:Math.max(0,1346-y2),opacity:.17});rect(g,'weighted-block',750,y2,160,160,C.ink,.04*(1-p(t,2.5,.8)));
 line(g,'spring-link',Array.from({length:80},(_,i)=>{const u=i/79;return[386+284*u,1348+Math.sin(u*Math.PI*16)*18*Math.sin(Math.PI*u)*(1+.4*Math.exp(-Math.max(0,t-2.4)*3))];}),p(t,3.6,.8),C.muted,6);
 label(g,'weight-light','خفيف',310,1515,58,C.blue,p(t,2.5,.55),{width:350,bands:1});
 label(g,'weight-heavy','ثقيل',750,1515,58,C.ink,p(t,3.1,.65),{width:350,bands:1});
 label(g,'physics-limit','ارتداد محسوب',540,1725,63,C.ink,p(t,4.2,.9),{weight:400,width:900});
 if(t>6){const curve=Array.from({length:101},(_,i)=>{const q=i/100;return[145+790*q,1075-55*(spring(q*2,springPresets.playful)-1)];});line(g,'physics-response',curve,p(t,6,1.4),C.blue,4);}
 if(t>9.2)rect(g,'physics-exit',540,1920-960*p(t,9.2,.8),1080,1920*p(t,9.2,.8),C.ink);
}
function scrolling(g,t){
 background(g,C.ink);chapter(g,'التمرير والعمق',t,C.lime);
 const rows=['فكرة','مسار','اتجاه','معنى','أثر','فكرة','مسار'];
 // Three independently sampled depth planes, with a shared framing target and different parallax rates.
 const camera=track(t,[{t:0,value:125},{t:1.2,value:125},{t:4.1,value:430,ease:'inOut'},{t:5.2,value:430,hold:true},{t:7.6,value:735,ease:'inOut'},{t:10,value:735}]);
 g.save();g.beginPath();g.rect(70,360,940,1130);g.clip();
 for(let plane=0;plane<3;plane++){
  const x=plane===0?220:plane===1?540:850,rate=[.48,1,1.42][plane],alpha=[.18,1,.32][plane];
  for(let i=0;i<rows.length;i++){const y=520+i*305-camera*rate;label(g,`scroll-${plane}-${i}`,rows[i],x,y,plane===1?176:112,plane===1?C.ice:C.cyan,p(t,.2+i*.05,.6),{width:plane===1?520:350,alpha:alpha*(plane===1?(.22+.78*smooth(1-Math.abs(y-1005)/240)):1),rotation:plane===0?-.08:plane===2?.08:0,bands:2});}
  note('depth-plane-'+plane,'depth-plane',{camera,rate,z:[-360,0,260][plane]});
 }
 g.restore();
 rect(g,'scroll-focus-rule-top',540,830,850*p(t,.6,.8),7,C.lime);rect(g,'scroll-focus-rule-bottom',540,1190,850*p(t,.85,.8),7,C.lime);
 label(g,'scroll-point','وجّه العين',540,1610,95,C.lime,p(t,1.6,.85),{width:860});
 // Horizontal ticker is independently clipped and not confused with camera movement.
 g.save();g.beginPath();g.rect(90,1725,900,95);g.clip();for(let i=0;i<5;i++)label(g,'ticker-'+i,'إلى الفكرة التالية',120+i*520-(t*120)%520,1770,48,C.ice,1,{width:490,weight:400,bands:1});g.restore();
 if(t>9.3){const u=p(t,9.3,.7);rect(g,'scroll-mask',540,960,1200*u,2100,C.lime,.08*(1-u));}
}
function reveals(g,t){
 background(g,C.lime);chapter(g,'الكشف المقنّع',t,C.ink);
 // The content is shaped once; alpha is supplied by independently animated, nonuniform mask geometry.
 label(g,'reveal-command','اكشف',540,670,285,C.ink,p(t,.18,1.45),{width:900,bands:5,slant:110});
 label(g,'reveal-complement','المعنى',540,1000,244,C.blue,p(t,1.35,1.3),{width:940,mode:'iris'});
 const ribbon=track(t,[{t:0,value:1100},{t:2.4,value:1100},{t:3.8,value:-150,ease:'inOut'},{t:5,value:-150}]);
 rect(g,'reveal-scanner',ribbon,905,28,700,C.ice,-.12);note('scanner-is-separate','mask-control',{x:ribbon});
 line(g,'reveal-stroke',cubicPath([900,1240],[750,1180],[180,1320],[200,1440]),p(t,2.8,1.25),C.ink,11,true);
 label(g,'reveal-detail','مسار يُرسم',540,1530,78,C.ink,p(t,3.4,.85),{width:900});
 label(g,'reveal-detail2','وكلمة تُكشف',540,1695,78,C.blue,p(t,4.35,.85),{width:900});
 // A split matte can reveal the second content layer without moving or dissolving the entire title.
 if(t>6.3){const s=sprite('reveal-bottom','لا اختصار للفكرة',58,C.ink,900,400),target=surface(s.width,s.height),u=p(t,6.3,1.15);const masked=maskedSprite(s,(mg,w,h)=>{mg.fillStyle='white';mg.fillRect(w/2-w*u/2,0,w*u,h);},target);g.drawImage(masked,540-s.width/2,1845-s.height/2);}
}
function typography(g,t){
 background(g,C.blue);chapter(g,'الطباعة الحركية',t,C.ice);
 const titles=[{word:'كل',x:815,y:610,w:320,start:.12},{word:'كلمة',x:420,y:610,w:570,start:.55},{word:'لها',x:820,y:965,w:320,start:1.35},{word:'إيقاع',x:405,y:965,w:590,start:1.85}];
 for(let i=0;i<titles.length;i++){const q=titles[i],gate=p(t,q.start,.95),wave=t>3?Math.sin((t-3)*Math.PI*1.6+i*.7)*12:0,rot=t>3?Math.sin((t-3)*2+i)*.014:0;label(g,'type-'+i,q.word,q.x,q.y+wave,208,i===3?C.lime:C.ice,gate,{width:q.w,bands:i%2?3:2,slant:i%2?35:-35,rotation:rot});}
 const end=line(g,'type-staff',cubicPath([130,1235],[420,1110],[760,1370],[945,1215]),p(t,2.4,1.4),C.lime,9);
 for(let i=0;i<8;i++){const tt=t-3.5-i*.09;if(tt<0)continue;const y=1420+Math.sin(t*2.4+i*.72)*42,scale=spring(tt,springPresets.soft);rect(g,'beat-'+i,190+i*100,y,34,Math.max(4,90*scale),i%2?C.ice:C.lime,.08*Math.sin(t+i));}
 label(g,'type-rule','متصلة في شكلها',540,1650,67,C.ice,p(t,4,.95),{width:920,weight:400});
 label(g,'type-rule2','مستقلة في توقيتها',540,1795,67,C.lime,p(t,5,.95),{width:940,weight:400});
 if(t>9.35){const u=p(t,9.35,.65);disc(g,'type-transition-object',540,960,Math.hypot(W,H)*u,C.ink);}
}
function transitionWorld(g,t){
 const pan=track(t,[{t:0,value:0},{t:7.05,value:0},{t:8.05,value:1080,ease:'inOut'},{t:10,value:1080}]);
 g.save();g.translate(-pan,0);
 const col=C.lime;
 // At 5.2 seconds the scene changes while the circular anchor preserves size and position: a match cut.
 disc(g,'transition-shared-anchor',540,850,148,col);
 label(g,'transition-first',t<5.2?'فكرة':'رابط',540,545,220,C.ice,p(t,t<5.2?.15:5.2,.8),{width:900});
 label(g,'transition-second',t<5.2?'تصل':'لا قفزة',540,1300,188,C.ice,p(t,t<5.2?1:5.55,.6),{width:900});
 line(g,'transition-link',cubicPath([540,1000],[460,1100],[750,1110],[700,1130]),p(t,1.6,1),C.lime,9,true);
 label(g,'transition-after','بلا انقطاع',1620,900,180,C.lime,p(t,7.75,.9),{width:900,bands:4});
 line(g,'transition-after-rule',[[1250,1140],[1980,1140]],p(t,8.25,.9),C.ice,10);
 g.restore();note('transition-camera','camera',{x:pan});
}
function transitions(g,t){
 background(g,t<5.2?C.ink:'#142c52');chapter(g,'الانتقال علاقة',t,C.ice);
 if(t>=7&&t<=8.15){temporalAverage(blurLayer,t,FPS,6,(c,st)=>transitionWorld(c,st),{angle:180,scratch:blurScratch});g.drawImage(blurLayer,0,0);note('whip-motion-blur','temporal-sampling',{samples:6,angle:180});}else transitionWorld(g,t);
 // The occluder and the incoming color field have independent layers with shared geometric coverage.
 if(t>3&&t<4.8){const q=clamp((t-3)/1.8),x=lerp(1260,-200,ease(q));rect(g,'object-wipe-front',x,960,380,2200,C.blue,-.08);rect(g,'object-wipe-edge',x-204,960,22,2200,C.lime,-.08);}
 label(g,'transition-rule','شكل يربط المشهدين',540,1640,65,C.ice,p(t,2,.8),{width:920,weight:400,alpha:1-p(t,6.8,.4)});
 if(t>8.2)label(g,'transition-caption','اتجاه واضح',540,1590,88,C.ice,p(t,8.2,.8),{width:900});
}
function paths(g,t){
 background(g,C.ice);chapter(g,'الخطوط والمؤشرات',t,C.blue);
 label(g,'path-main','الخط',540,560,250,C.ink,p(t,.2,1),{width:880,bands:2});
 label(g,'path-second','يشرح',540,830,235,C.blue,p(t,1,1),{width:900,bands:4});
 const pts=cubicPath([155,1170],[230,1450],[760,990],[895,1320],360);const progress=p(t,1.8,2.7,cubicBezier(.4,0,.15,1));const tip=line(g,'path-route',pts,progress,C.blue,15,true);
 if(progress>.15)disc(g,'path-start',155,1170,24,C.ink);
 const ring=p(t,4.25,.75);g.beginPath();g.arc(tip.x,tip.y,56,-Math.PI/2,-Math.PI/2+Math.PI*2*ring);g.strokeStyle=C.blue;g.lineWidth=5;g.stroke();note('path-arrival-ring','circular-reveal',{progress:ring});
 label(g,'path-callout','هنا',800,1480,78,C.ink,p(t,4.6,.65),{width:400});
 const a=radialShape(64,118,'circle'),b=radialShape(64,86,'square'),u=p(t,6.0,1.3);g.save();g.translate(280,1590);g.rotate(.1*Math.sin(t));poly(g,morphContours(a,b,u),{fill:C.lime,stroke:C.ink,width:4});g.restore();note('path-corresponding-morph','vertex-morph',{u,vertices:64});
 label(g,'path-final','كل مؤشر له وجهة',540,1790,63,C.ink,p(t,6.8,.9),{width:950,weight:400});
}
const timingCurve=cubicBezier(.25,.05,.15,1);
function graph(g,id,fn,x,y,w,h,progress,color){
 line(g,id+'-axis',[[x,y-h],[x,y],[x+w,y]],1,C.muted,3);const points=Array.from({length:121},(_,i)=>[x+w*i/120,y-h*fn(i/120)]);line(g,id+'-curve',points,progress,color,7);const u=clamp(progress);disc(g,id+'-sample',x+w*u,y-h*fn(u),13,C.ink);
}
function timing(g,t){
 background(g,C.lime);chapter(g,'التوقيت والحركة',t,C.ink);
 label(g,'timing-a','التوقيت',540,520,228,C.ink,p(t,.1,1),{width:940,bands:4});
 label(g,'timing-b','يصنع المعنى',540,790,136,C.blue,p(t,.95,.95),{width:940,bands:2});
 const u=p(t,2,3.6,eases.linear),speed=q=>Math.max(0,derivative(timingCurve,q))/4.2;
 graph(g,'value-graph',timingCurve,190,1250,700,265,u,C.blue);label(g,'value-label','قيمة',890,940,51,C.ink,p(t,1.7,.55),{width:250,weight:400});
 graph(g,'speed-graph',speed,190,1650,700,245,u,C.ink);label(g,'speed-label','سرعة',890,1360,51,C.ink,p(t,2.2,.55),{width:250,weight:400});
 if(t>5.5){const u=p(t,5.5,1);rect(g,'timing-resolution',540,960,1080,2100*u,C.ink);label(g,'final-thesis','المعنى',540,760,260,C.ice,p(t,6.25,.95),{width:940,bands:3});label(g,'final-priority','أولاً',540,1050,250,C.lime,p(t,6.85,.9),{width:850,bands:2});label(g,'final-subline','حركة واعية. لا قالب.',540,1450,69,C.ice,p(t,7.2,.8),{weight:400,width:930});}
 if(t>9.5){g.fillStyle=`rgba(16,29,53,${smooth((t-9.5)/.5)})`;g.fillRect(0,0,W,H);}
}
const shots=[opening,physics,scrolling,reveals,typography,transitions,paths,timing];
window.seek=t=>{t=clamp(t,0,DURATION-1/FPS);layers.length=0;const i=Math.min(7,Math.floor(t/10));ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;ctx.globalCompositeOperation='source-over';ctx.filter='none';shots[i](ctx,t-i*10);window.MF_LAST_FRAME_LAYERS=layers.map(x=>({...x}));return{time:t,frame:Math.round(t*FPS),scene:i,layers:layers.length};};
window.filmReady=(async()=>{await document.fonts.ready;await document.fonts.load('600 160px "IBM Plex Sans Arabic"','الحركة المعنى');await document.fonts.load('400 60px "IBM Plex Sans Arabic"','توقيت');if(!document.fonts.check('600 160px "IBM Plex Sans Arabic"'))throw new Error('Arabic font failed');window.seek(0);document.documentElement.dataset.ready='true';return true;})();
window.MF_DEMO={width:W,height:H,fps:FPS,duration:DURATION,frames:2560,originalComposition:true,notReusableTemplate:true};
