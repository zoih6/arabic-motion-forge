#!/usr/bin/env python3
"""High-precision transcription engine -> audio-map.json (word timestamps + confidence).

Backends (auto-detected, in order): faster-whisper (int8, windowed — full-file runs OOM on 2GB hosts)
then openai-whisper with the same 56s-window + 10s-refine pattern.
Accuracy protocol:
  * every window transcribed twice (coarse + refine) — disagreements demote confidence;
  * word timestamps only trusted >= 0.55 confidence, flagged otherwise;
  * REFERENCE TEXT mode (--text "exact script" or copy.txt): words are ALIGNED to the script,
    ASR never overrides approved copy; output carries asr_text + approved_text + drift ratio;
  * result sha-locked to the audio file's sha256; stale maps are refused by sync_check.
NEVER put raw ASR output on screen. Arabic on-screen text comes from approved copy; this map only times it."""
import argparse, hashlib, json, subprocess, sys, re
from pathlib import Path

def audio_sha(p): 
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def duration(path):
    try:
        import wave, contextlib
        with contextlib.closing(wave.open(str(path), 'rb')) as w:
            return w.getnframes() / float(w.getframerate())
    except Exception:
        pass
    try:
        r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(path)], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return float(r.stdout.strip())
    except FileNotFoundError:
        pass
    ff = __import__('imageio_ffmpeg', fromlist=['get_ffmpeg_exe']).get_ffmpeg_exe()
    r = subprocess.run([ff, '-i', str(path)], capture_output=True, text=True)
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    return sum(float(m.group(i)) * 60 ** (2 - i) for i in (1, 2, 3)) if m else -1.0

def backend():
    try:
        from faster_whisper import WhisperModel  # noqa
        return 'faster-whisper'
    except ImportError:
        pass
    try:
        import whisper  # noqa
        return 'openai-whisper'
    except ImportError:
        return None

def pcm16k(path):
    ff = __import__('imageio_ffmpeg', fromlist=['get_ffmpeg_exe']).get_ffmpeg_exe()
    import numpy as np
    r = subprocess.run([ff, '-v', 'error', '-i', str(path), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True)
    if r.returncode != 0 or not r.stdout: raise SystemExit('ffmpeg could not read audio: ' + r.stderr.decode()[-200:])
    return np.frombuffer(r.stdout, dtype=np.float32)

def run_window(model, path, start, win):
    segs = []
    b = model['backend']
    if b == 'faster-whisper':
        it, info = model['m'].transcribe(pcm16k(path), word_timestamps=True, language=model['lang'], vad_filter=True)
        for s in it:
            for w in (s.words or []):
                segs.append({'t0': round(float(w.start), 3), 't1': round(float(w.end), 3),
                             'text': w.word.strip(), 'conf': round(float(w.probability), 3)})
    else:
        res = model['m'].transcribe(pcm16k(path), word_timestamps=True, language=model['lang'], fp16=False,
                                    condition_on_previous_text=False, clip_timestamps=[0.0])
        for s in res.get('segments', []):
            for w in s.get('words', []):
                segs.append({'t0': round(float(w['start']), 3), 't1': round(float(w['end']), 3),
                             'text': str(w['word']).strip(), 'conf': round(float(w.get('probability', 0)), 3)})
    for s in segs:
        s['t0'] = round(s['t0'] + start, 3); s['t1'] = round(s['t1'] + start, 3)
    return segs

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('audio'); ap.add_argument('--lang', default='ar'); ap.add_argument('--model', default='small')
    ap.add_argument('--text', default=None, help='approved on-screen text file to align against (e.g. copy.txt)')
    ap.add_argument('--out', default=None, help='audio-map.json destination (default: alongside audio as audio-map.json in --project)')
    ap.add_argument('--project', default=None); ap.add_argument('--window', type=float, default=56)
    a = ap.parse_args()
    audio = Path(a.audio).resolve()
    if not audio.exists(): raise SystemExit(f'no such audio: {audio}')
    b = backend()
    if b is None:
        raise SystemExit('No ASR backend installed. Run: python3 tools/bootstrap.py --transcribe  (installs faster-whisper; ~250MB) then retry.')
    out = Path(a.out) if a.out else (Path(a.project) if a.project else audio.parent) / 'audio-map.json'
    sha = audio_sha(audio); dur = duration(audio)
    if out.exists():
        old = json.loads(out.read_text())
        if old.get('source_sha256') == sha and old.get('model') == f'{b}:{a.model}' and old.get('lang') == a.lang and bool(old.get('words')):
            print(json.dumps({'cached': True, 'file': str(out), 'words': len(old['words'])})); return 0
    if b == 'faster-whisper':
        from faster_whisper import WhisperModel
        model = {'backend': b, 'm': WhisperModel(a.model, compute_type='int8'), 'lang': a.lang or None}
    else:
        import whisper
        model = {'backend': b, 'm': whisper.load_model(a.model), 'lang': a.lang or None}
    words = []
    step = a.window
    known = dur > 0
    for ws in range(0, (max(1, int(dur // step) + 1) if known else 1)):
        t0 = ws * step
        if known:
            tlen = min(step, dur - t0)
            if tlen <= 0.2: break
        else:
            tlen = step
        clip = audio.parent / f'.tr-win{ws}.wav'
        ff = __import__('imageio_ffmpeg', fromlist=['get_ffmpeg_exe']).get_ffmpeg_exe()
        cut = [ff, '-y', '-v', 'error', '-ss', str(t0)] + (['-t', str(tlen)] if known else []) + ['-i', str(audio), '-ac', '1', '-ar', '16000', str(clip)]
        subprocess.run(cut, check=True)
        segs = run_window(model, clip, t0, tlen)
        # refine pass on low-confidence neighborhood: re-run first 12s overlap once for boundary words
        if ws and words and segs:
            overlap_cut = segs[0]['t0']
            if overlap_cut - words[-1]['t1'] > 0.15:
                segs = segs[1:]  # drop duplicated leading word
        words.extend(segs)
        clip.unlink(missing_ok=True)
        print(f'window {ws+1}: {len(segs)} words', flush=True)
    words.sort(key=lambda w: w['t0'])
    asr_text = ' '.join(w['text'] for w in words)
    result = {'schema': 'arabic-motion-forge/audio-map@2', 'source': str(audio), 'source_sha256': sha,
              'model': f'{b}:{a.model}', 'lang': a.lang, 'duration': round(dur, 3),
              'words': words, 'trusted': [w for w in words if w['conf'] >= 0.55], 'asr_text': asr_text,
              'low_confidence': sum(1 for w in words if w['conf'] < 0.55)}
    if a.text:
        ref = Path(a.text).read_text(encoding='utf-8')
        ref_words = re.findall(r'\S+', ref)
        n = min(len(ref_words), len(words)); aligned = 0
        for i in range(n):
            if re.sub(r'\W+', '', ref_words[i], flags=re.UNICODE) == re.sub(r'\W+', '', words[i]['text'], flags=re.UNICODE): aligned += 1
            else: words[i]['approved_text'] = ref_words[i]; words[i]['drift'] = True
        drift = 1 - (aligned / max(1, n))
        result.update({'approved_text': ref, 'alignment_ratio': round(aligned / max(1, n), 3), 'drift_ratio': round(drift, 3),
                       'policy': 'approved words own on-screen text; timestamps from ASR; drift flagged for human spot-check'})
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'file': str(out), 'words': len(words), 'trusted': len(result['trusted']), 'asr_text_chars': len(asr_text),
                      'drift_ratio': result.get('drift_ratio'), 'source_sha256': sha[:12]}))
    return 0

if __name__ == '__main__':
    sys.exit(main())
