import {engine,createTimeline} from '../vendor/primitives/anime.esm.mjs';
engine.useDefaultMainLoop=false;engine.pause();
export function frameLockedTimeline(state,build){const timeline=createTimeline({autoplay:false});build(timeline,state);return {sample(seconds){timeline.seek(seconds*1000,true);return structuredClone(state);},dispose(){timeline.cancel();}};}
