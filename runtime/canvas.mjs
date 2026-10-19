/* Original low-level raster/vector primitives. No project-specific scene compositions. MIT. */
import {clamp,lerp,smooth,trimPath,pathPoint,shutterTimes} from './core.mjs';
export function surface(w,h){const c=document.createElement('canvas');c.width=Math.ceil(w);c.height=Math.ceil(h);return c;}
export function textSprite(text,{size=120,family='IBM Plex Sans Arabic',weight=600,color='#111827',padding=24,direction='rtl'}={}){
 const probe=surface(1,1),p=probe.getContext('2d');p.direction=direction;p.font=`${weight} ${size}px "${family}"`;p.textAlign='left';p.textBaseline='alphabetic';const m=p.measureText(text);
 const left=Math.ceil(Math.max(0,m.actualBoundingBoxLeft)),right=Math.ceil(Math.max(m.width,m.actualBoundingBoxRight));
 const ascent=Math.ceil(Math.max(size*.8,m.actualBoundingBoxAscent)),descent=Math.ceil(Math.max(size*.25,m.actualBoundingBoxDescent));
 const c=surface(left+right+padding*2,ascent+descent+padding*2),g=c.getContext('2d');g.direction=direction;g.font=p.font;g.textAlign='left';g.textBaseline='alphabetic';g.fillStyle=color;g.fillText(text,padding+left,padding+ascent);
 return{canvas:c,width:c.width,height:c.height,advance:m.width,baseline:padding+ascent,padding,text,font:p.font,direction};
}
export function fitText(text,width,options={}){let size=options.size||160,probe=surface(1,1).getContext('2d');do{probe.font=`${options.weight||600} ${size}px "${options.family||'IBM Plex Sans Arabic'}"`;if(probe.measureText(text).width<=width)break;size-=2;}while(size>24);return textSprite(text,{...options,size});}
export function paintSprite(g,s,x,y,{anchor='center',scale=1,rotation=0,alpha=1}={}){g.save();g.translate(x,y);g.rotate(rotation);g.scale(scale,scale);g.globalAlpha*=alpha;const ox=anchor==='right'?-s.width:anchor==='left'?0:-s.width/2;g.drawImage(s.canvas,ox,-s.height/2);g.restore();}
const matteBuffers=new WeakMap();
export function maskedSprite(sprite,paintMask,target){
 const c=target||surface(sprite.width,sprite.height),g=c.getContext('2d');let mask=matteBuffers.get(c);if(!mask){mask=surface(c.width,c.height);matteBuffers.set(c,mask);}const mg=mask.getContext('2d');mg.setTransform(1,0,0,1,0,0);mg.clearRect(0,0,mask.width,mask.height);paintMask(mg,c.width,c.height);
 g.setTransform(1,0,0,1,0,0);g.clearRect(0,0,c.width,c.height);g.globalCompositeOperation='source-over';g.drawImage(sprite.canvas||sprite,0,0);g.globalCompositeOperation='destination-in';g.drawImage(mask,0,0);g.globalCompositeOperation='source-over';return c;
}
export function rtlMatte(sprite,progress,{slant=0,bands=1,target}={}){
 return maskedSprite(sprite,(g,w,h)=>{g.fillStyle='#fff';const p=clamp(progress);if(p<=0)return;if(p>=1){g.fillRect(0,0,w,h);return;}for(let i=0;i<bands;i++){const u=clamp(p*1.25-i/(Math.max(1,bands-1))*.25),y=i*h/bands,hh=h/bands+1,left=w*(1-u);g.beginPath();g.moveTo(w+3,y);g.lineTo(left+slant,y);g.lineTo(left-slant,y+hh);g.lineTo(w+3,y+hh);g.closePath();g.fill();}},target);
}
export function irisMatte(sprite,progress,target){return maskedSprite(sprite,(g,w,h)=>{g.fillStyle='#fff';g.beginPath();g.ellipse(w/2,h/2,Math.hypot(w,h)*clamp(progress),Math.hypot(w,h)*clamp(progress),0,0,Math.PI*2);g.fill();},target);}
export function lumaAlpha(r,g,b,a=255){return(.2126*r+.7152*g+.0722*b)/255*(a/255);}
export function lumaMatte(fill,matte){const c=surface(fill.width,fill.height),g=c.getContext('2d');g.drawImage(fill,0,0);const pixels=g.getImageData(0,0,c.width,c.height),m=matte.getContext('2d').getImageData(0,0,c.width,c.height);for(let i=0;i<pixels.data.length;i+=4)pixels.data[i+3]*=lumaAlpha(m.data[i],m.data[i+1],m.data[i+2],m.data[i+3]);g.putImageData(pixels,0,0);return c;}
export function strokePath(g,path,progress,{start=0,color='#2365ff',width=8,head=false}={}){
 const p=trimPath(path,start,progress);if(p.length<2)return;g.save();g.strokeStyle=color;g.fillStyle=color;g.lineWidth=width;g.lineCap='round';g.lineJoin='round';g.beginPath();p.forEach((v,i)=>i?g.lineTo(...v):g.moveTo(...v));g.stroke();
 if(head){const end=pathPoint(path,progress);g.translate(end.x,end.y);g.rotate(end.angle);g.beginPath();g.moveTo(12,0);g.lineTo(-18,-13);g.lineTo(-18,13);g.closePath();g.fill();}g.restore();
}
export function poly(g,points,{fill,stroke,width=2,close=true}={}){g.beginPath();points.forEach((p,i)=>i?g.lineTo(...p):g.moveTo(...p));if(close)g.closePath();if(fill){g.fillStyle=fill;g.fill();}if(stroke){g.strokeStyle=stroke;g.lineWidth=width;g.stroke();}}
export function independentShadow(g,{x,y,width,height,elevation=0,opacity=.18}){g.save();g.translate(x+elevation*.17,y+height/2+12+elevation*.3);g.scale(1,.23);const grad=g.createRadialGradient(0,0,1,0,0,width*.6+elevation*.5);grad.addColorStop(0,`rgba(0,0,0,${opacity/(1+elevation*.012)})`);grad.addColorStop(1,'rgba(0,0,0,0)');g.fillStyle=grad;g.fillRect(-width,-width,width*2,width*2);g.restore();}
export function temporalAverage(target,t,fps,samples,drawAt,{angle=180,scratch}={}){
 const temp=scratch||surface(target.width,target.height),out=target.getContext('2d');out.setTransform(1,0,0,1,0,0);out.clearRect(0,0,target.width,target.height);
 shutterTimes(t,fps,samples,angle).forEach((time,i)=>{const g=temp.getContext('2d');g.setTransform(1,0,0,1,0,0);g.clearRect(0,0,temp.width,temp.height);drawAt(g,time);out.globalCompositeOperation='lighter';out.globalAlpha=1/samples;out.drawImage(temp,0,0);});out.globalAlpha=1;out.globalCompositeOperation='source-over';
}
export function samplePerspective({x,y,z=0},{x:cx=0,y:cy=0,dolly=0,focal=1600,centerX=0,centerY=0}){const d=focal-z-dolly;if(d<=0)throw new Error('Layer crosses camera plane');const k=focal/d;return{x:centerX+(x-cx)*k,y:centerY+(y-cy)*k,scale:k};}
export function wordLayout(g,text,maxWidth,{size=140,family='IBM Plex Sans Arabic',weight=600,gap=28}={}){
 const words=text.trim().split(/\s+/u);let widths,total;do{g.font=`${weight} ${size}px "${family}"`;g.direction='rtl';widths=words.map(w=>g.measureText(w).width);total=widths.reduce((a,b)=>a+b,0)+gap*(words.length-1);if(total>maxWidth)size-=2;}while(total>maxWidth&&size>24);
 let x=total/2;return{size,total,words:words.map((text,i)=>{const item={text,index:i,x:x-widths[i]/2,width:widths[i]};x-=widths[i]+gap;return item;})};
}
