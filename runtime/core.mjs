/* Original, project-agnostic motion math. No scene layout, palette, asset, or real-time clock. MIT. */
export const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
export const lerp=(a,b,t)=>a+(b-a)*t;
export const smooth=t=>{t=clamp(t);return t*t*(3-2*t);};
export const smoother=t=>{t=clamp(t);return t*t*t*(t*(t*6-15)+10);};
export const eases={linear:t=>t,in:t=>t*t*t,out:t=>1-(1-t)**3,inOut:t=>t<.5?4*t*t*t:1-(-2*t+2)**3/2,smooth,smoother};
export function cubicBezier(x1,y1,x2,y2){
 if(x1<0||x1>1||x2<0||x2>1)throw new RangeError('Bezier time handles must be in [0,1].');
 const B=(u,a,b)=>3*(1-u)**2*u*a+3*(1-u)*u*u*b+u*u*u;
 return t=>{if(t<=0)return 0;if(t>=1)return 1;let lo=0,hi=1,u=t;for(let i=0;i<34;i++){u=(lo+hi)/2;if(B(u,x1,x2)<t)lo=u;else hi=u;}return B(u,y1,y2);};
}
export function mix(a,b,u){if(Array.isArray(a))return a.map((x,i)=>mix(x,b[i],u));return lerp(a,b,u);}
export function track(t,keys){
 if(!keys.length)throw new Error('A track needs keyframes.');
 if(t<=keys[0].t)return keys[0].value;
 for(let i=1;i<keys.length;i++){
  const a=keys[i-1],b=keys[i];if(b.t<=a.t)throw new Error('Keyframe times must be strictly increasing.');
  if(t<b.t){if(a.hold)return a.value;const f=typeof b.ease==='function'?b.ease:(eases[b.ease||'inOut']);if(!f)throw new Error('Unknown easing');return mix(a.value,b.value,f((t-a.t)/(b.t-a.t)));}
 }
 return keys.at(-1).value;
}
export const springPresets={snappy:{stiffness:280,damping:30,mass:1},soft:{stiffness:160,damping:24,mass:1},heavy:{stiffness:100,damping:26,mass:1.4},playful:{stiffness:220,damping:20,mass:1}};
export function spring(t,{stiffness:k=180,damping:d=24,mass:m=1,velocity:v=0}={}){
 if(k<=0||m<=0||d<0)throw new RangeError('Invalid spring parameters');if(t<=0)return 0;
 const a=d/(2*m),w2=k/m,q=a*a-w2;
 if(Math.abs(q)<1e-8)return 1+(-1+(v-a)*t)*Math.exp(-a*t);
 if(q<0){const w=Math.sqrt(-q);return 1+Math.exp(-a*t)*(-Math.cos(w*t)+(v-a)/w*Math.sin(w*t));}
 const s=Math.sqrt(q),r1=-a+s,r2=-a-s,A=(v+r2)/(r1-r2),B=-1-A;return 1+A*Math.exp(r1*t)+B*Math.exp(r2*t);
}
export function ballistic(t,{height=400,gravity=1700,restitution=.48}={}){
 if(height<0||gravity<=0||restitution<0||restitution>=1)throw new RangeError('Invalid ballistic parameters');
 t=Math.max(0,t);const fall=Math.sqrt(2*height/gravity);if(t<=fall)return height-.5*gravity*t*t;
 t-=fall;let velocity=Math.sqrt(2*gravity*height)*restitution;
 for(let i=0;i<24;i++){const duration=2*velocity/gravity;if(t<=duration)return Math.max(0,velocity*t-.5*gravity*t*t);t-=duration;velocity*=restitution;}
 return 0;
}
export const inertia=(t,x0,v0,tau=.3)=>x0+v0*tau*(1-Math.exp(-Math.max(0,t)/tau));
export const recoil=(t,amount=1,decay=8,frequency=5)=>t<0?0:amount*Math.exp(-decay*t)*Math.sin(2*Math.PI*frequency*t);
export const quantize=(t,fps)=>Math.floor(t*fps)/fps;
export const stagger=(i,count,step=.08,from='start')=>step*(from==='end'?count-1-i:from==='center'?Math.abs(i-(count-1)/2):i);
export function hash01(seed,index=0){let n=(seed^Math.imul(index+1,0x9e3779b1))>>>0;n=Math.imul(n^(n>>>16),0x85ebca6b);n=Math.imul(n^(n>>>13),0xc2b2ae35);return((n^(n>>>16))>>>0)/4294967296;}
export function noise(t,seed=1,frequency=2){const u=t*frequency,i=Math.floor(u);return lerp(hash01(seed,i)*2-1,hash01(seed,i+1)*2-1,smooth(u-i));}
export const followThrough=(driver,t,lag=.12,amount=1)=>driver(Math.max(0,t-lag))*amount;
export const squashStretch=(stretch=1)=>[1/Math.sqrt(Math.max(.001,stretch)),stretch];
export function cubicPath(a,b,c,d,samples=256){const p=[];for(let i=0;i<=samples;i++){const t=i/samples,u=1-t;p.push([u*u*u*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t*t*t*d[0],u*u*u*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t*t*t*d[1]]);}return p;}
export function pathMetrics(points){
 if(points.length<2)throw new Error('At least two path vertices required');let lengths=[0];
 for(let i=1;i<points.length;i++)lengths.push(lengths.at(-1)+Math.hypot(points[i][0]-points[i-1][0],points[i][1]-points[i-1][1]));
 return{points,lengths,length:lengths.at(-1)};
}
export function pathPoint(path,u){
 const distance=clamp(u)*path.length;let lo=1,hi=path.lengths.length-1;
 while(lo<hi){const m=(lo+hi)>>1;if(path.lengths[m]<distance)lo=m+1;else hi=m;}
 const i=lo,a=path.points[i-1],b=path.points[i],n=path.lengths[i]-path.lengths[i-1],f=n?(distance-path.lengths[i-1])/n:0;
 return{x:lerp(a[0],b[0],f),y:lerp(a[1],b[1],f),angle:Math.atan2(b[1]-a[1],b[0]-a[0]),segment:i};
}
export function trimPath(path,start=0,end=1){
 start=clamp(start);end=clamp(end);if(end<=start)return[];const a=pathPoint(path,start),b=pathPoint(path,end),p=[[a.x,a.y]];
 for(let i=a.segment;i<b.segment;i++)p.push(path.points[i]);p.push([b.x,b.y]);return p;
}
export function morphContours(a,b,u){if(a.length!==b.length||a.length<3)throw new Error('Morph needs explicit matching vertex correspondence.');return a.map((p,i)=>[lerp(p[0],b[i][0],u),lerp(p[1],b[i][1],u)]);}
export function radialShape(count,radius,kind='circle'){const p=[];for(let i=0;i<count;i++){const a=-Math.PI/2+i/count*Math.PI*2;let r=radius;if(kind==='square')r/=Math.max(Math.abs(Math.cos(a)),Math.abs(Math.sin(a)));if(kind==='diamond')r/=Math.abs(Math.cos(a))+Math.abs(Math.sin(a));p.push([Math.cos(a)*r,Math.sin(a)*r]);}return p;}
export function matrix({x=0,y=0,rotation=0,sx=1,sy=sx}={}){const c=Math.cos(rotation),s=Math.sin(rotation);return[c*sx,s*sx,-s*sy,c*sy,x,y];}
export const multiply=(a,b)=>[a[0]*b[0]+a[2]*b[1],a[1]*b[0]+a[3]*b[1],a[0]*b[2]+a[2]*b[3],a[1]*b[2]+a[3]*b[3],a[0]*b[4]+a[2]*b[5]+a[4],a[1]*b[4]+a[3]*b[5]+a[5]];
export const transformPoint=(m,p)=>[m[0]*p[0]+m[2]*p[1]+m[4],m[1]*p[0]+m[3]*p[1]+m[5]];
export function layerState(layers,id,t,seen=new Set()){
 if(seen.has(id))throw new Error('Parent cycle');const n=layers.find(x=>x.id===id);if(!n)throw new Error('Missing layer '+id);seen.add(id);
 const v={...n.base};for(const [key,keys] of Object.entries(n.tracks||{}))v[key]=track(t,keys);
 const local=matrix(v),world=n.parent?multiply(layerState(layers,n.parent,t,seen).matrix,local):local;return{...v,matrix:world};
}
export function shutterTimes(t,fps,samples=4,angle=180){if(samples<1||fps<=0)throw new Error('Invalid shutter');const exposure=angle/360/fps;return Array.from({length:samples},(_,i)=>t+((i+.5)/samples-.5)*exposure);}
export const derivative=(fn,t,h=1e-4)=>(fn(t+h)-fn(t-h))/(2*h);
export const scrollOffset=(t,speed,span)=>((t*speed)%span+span)%span;
export function safeTextUnits(text,mode='word'){
 if(mode==='word')return text.trim().split(/\s+/u);
 if(mode==='line')return text.split('\n');
 if(/\p{Script=Arabic}/u.test(text)&&!/^\p{N}+$/u.test(text))throw new Error('Connected Arabic character transforms are blocked. Shape the word/line and animate its matte instead.');
 return [...new Intl.Segmenter(undefined,{granularity:'grapheme'}).segment(text)].map(x=>x.segment);
}
export function selectorWeight(index,start,end,softness=0){if(!softness)return index>=start&&index<=end?1:0;return smooth((index-start)/softness)*smooth((end-index)/softness);}
export function scrambleASCII(text,t,{duration=1,seed=5,allowCopyMutation=false}={}){
 if(!allowCopyMutation)throw new Error('Text scramble requires explicit permission to mutate copy.');
 if(/[^\x20-\x7e]/u.test(text))throw new Error('This scramble implementation is ASCII-only; Arabic is blocked.');
 const chars='ABCDEFGHJKLMNPQRSTUVWXYZ0123456789',p=clamp(t/duration);return [...text].map((c,i)=>c===' '||p>=1||i<Math.floor(text.length*p)?c:chars[Math.floor(hash01(seed+i,Math.floor(t*16))*chars.length)]).join('');
}
export const waveOffset=(index,t,amplitude=8,frequency=1,phase=.5)=>Math.sin(t*Math.PI*2*frequency+index*phase)*amplitude;
