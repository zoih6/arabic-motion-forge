# 04 — Audio Package (الحزمة الصوتية)

## الهدف

**الملف الرابع من حزمة الإنتاج الخماسية.** يحوي **كل الطبقات الصوتية** (Ambience، Foley، SFX، Music، Dialogue/VO)، استراتيجية التوليد، خطة Lip-Sync، وخطط Mixing/Mastering.

> **يُنتَج من قبل:** `30-executive-producer` (مع `29-audio-decision-engine`).

---

## كيف تستخدمه

1. املأ كل قسم عند M7
2. لكل طبقة: source + timestamps + model
3. حدّد Lip-Sync Plan لكل مشهد فيه حوار
4. وثّق Mixing Levels
5. مرّر عبر `31-quality-gate` (G7)

---

## القالب الكامل

```markdown
# Audio Package — [اسم المشروع]

**التاريخ:** [ISO]
**الحالة:** [DRAFT / APPROVED_FOR_GENERATION / GENERATED / APPROVED]
**عدد الطبقات:** [N]
**المدة الإجمالية:** [Xs]
**منصة الاستهداف:** [YouTube / Instagram / TikTok / TV / Cinema]
**Master LUFS:** [-14 / -16 / -23]

---

## 0. Audio Strategy Overview

```yaml
strategy:
  dialogue_present: true / false
  voiceover_present: true / false
  music_present: true / false
  sfx_present: true / false
  foley_present: true / false
  ambience_present: true / false
  lipsync_required: [...]
  
  total_layers: N
  
  voice_strategy:
    primary: "ElevenLabs / Cartesia / Resemble AI"
    voice_cloning_required: true / false
    voice_clone_id: "..."  # إن وُجد
    languages: [...]
    dialects: [...]
  
  music_strategy:
    source: "Suno generated / Udio / licensed / composer"
    genre: "..."
    mood: "..."
    bpm: ...
    structure: "intro → build → climax → resolve"
  
  sfx_strategy:
    source: "ElevenLabs SFX / library / manual"
    primary_model: "..."
  
  foley_strategy:
    source: "library (BBC, Sonniss) / recorded / AI-generated"
    quality_priority: "high / medium / low"
  
  ambience_strategy:
    source: "library / AI-generated"
    layering: "single / multiple layers"
  
  target_platforms:
    primary: "YouTube"
    secondary: ["Instagram", "TikTok"]
    target_lufs_per_platform:
      youtube: -14
      instagram: -16
      tiktok: -14
      broadcast: -23
```

---

## 1. Voice Layers (طبقات الصوت البشري)

### VO-01 — Voiceover (المشهد 1)

```yaml
layer_id: "VO-01"
type: "voiceover"
purpose: "السرد الافتتاحي للفيلم"

text: "كل يوم، نفس الاستيقاظ. نفس الجسد. نفس السؤال."
text_translation: "Every day, the same waking. The same body. The same question."

language: "ar"
dialect: "يمني صنعاني (yemeni_sanaani)"

delivery:
  tone: "هادئ، بطيء، فيه نبرة يأس مكتومة"
  pace: "بطيء (2 كلمة/ثانية)"
  emotion: "تأمل متعب"
  pacing_notes: "وقفة قصيرة بعد 'نفس الجسد'"

timestamps:
  start: "0.0s"
  end: "4.0s"
  overlaps_with:
    - "AMBIENCE-01 (low, -18dB)"
    - "MUSIC-01 (low, -18dB, ducked to -24dB during VO)"

model:
  primary: "ElevenLabs"
  voice_id: "arabic_male_calm_v2 / custom-clone-sami"
  parameters:
    stability: 0.65
    similarity_boost: 0.80
    style: 0.30
    speaker_boost: true

processing:
  enhance: "Adobe Podcast enhance (clarity + presence)"
  noise_reduction: "iZotope RX Voice De-noise"
  eq: "cut 200Hz rumble, boost 3kHz presence, boost 8kHz air"
  compression: "3:1 ratio, attack 5ms, release 50ms"
  normalization: "true peak -3dBFS"

expected_attempts: 3
fallback:
  if_attempts_fail:
    - "Cartesia Sonic"
    - "Resemble AI"
    - "record human voice (last resort)"

output:
  format: "WAV 48kHz 24bit"
  path: "assets/audio/vo-01_v3.wav"
  duration: "4.0s"
  status: "approved"
```

### DLG-01 — Dialogue (شخصية على الشاشة)

```yaml
layer_id: "DLG-01"
type: "dialogue"
purpose: "حوار الشخصية في المشهد 3"

text: "نعم. هذا ما كنت أحتاجه."
text_translation: "Yes. This is what I needed."

speaker: "SAMI-01"
scene: "SC03"
shot: "SC03_SH02"

language: "ar"
dialect: "يمني صنعاني"

delivery:
  tone: "واثق، دافئ، ابتسامة في الصوت"
  pace: "متوسط-بطيء (3 كلمات/ثانية)"
  emotion: "يقظة، رضا"

lipsync_required: true
lipsync_strategy: "regenerate_with_audio"
lipsync_model: "hedra / veo-3 (with audio)"

timestamps:
  start: "6.0s"  # ضمن shot SC03_SH02
  end: "8.0s"
  pre_roll: "0.5s (silence before)"
  post_roll: "0.5s (silence after)"

model:
  primary: "ElevenLabs"
  voice_id: "custom-clone-sami (from user voice sample)"
  parameters:
    stability: 0.50
    similarity_boost: 0.85
    style: 0.45

processing:
  enhance: "Adobe Podcast enhance"
  alignment: "synced with lip movement in video"

output:
  format: "WAV 48kHz 24bit"
  path: "assets/audio/dlg-01_v2.wav"
  duration: "2.0s"
  status: "approved"
  synced_video: "assets/motion/sc03_sh02_v3.mp4"
```

### VO-02, DLG-02, ...

[نفس النمط لكل طبقة صوت بشري]

---

## 2. Music Layer (الموسيقى)

### MUSIC-01 — Background Score

```yaml
layer_id: "MUSIC-01"
type: "music"
purpose: "الموسيقى التصويرية الرئيسية للفيلم"

source:
  strategy: "AI generated (Suno)"
  model: "Suno v3.5 / Udio"
  prompt: |
    Cinematic emotional music for a 45-second brand
    film about a Yemeni craftsman finding clarity
    through a quiet morning ritual. Piano-led with
    subtle strings, building gradually. Influences
    of Arabic maqam (Hijaz scale). Modern cinematic
    feel. Emotional arc: contemplative → awakening
    → confident. Instrumental only, no vocals.
  
  tags: "cinematic, emotional, piano, strings, arabic_maqam, brand_film, contemplative"
  
  duration: "45s (full film)"
  
  structure:
    intro:
      duration: "0-8s"
      mood: "contemplative, quiet"
      instruments: "solo piano, soft"
    build:
      duration: "8-25s"
      mood: "growing, hopeful"
      instruments: "piano + strings + light percussion"
    climax:
      duration: "25-35s"
      mood: "triumphant, awakened"
      instruments: "full ensemble"
    resolve:
      duration: "35-45s"
      mood: "warm, settled"
      instruments: "piano + strings fade out"

ducking:
  enabled: true
  trigger: "VO-01, DLG-01, DLG-02"
  duck_amount: "-6dB"
  attack: "200ms"
  release: "500ms"

processing:
  mastering: "LANDR AI / iZotope Ozone"
  normalization: "true peak -3dBFS"
  eq: "subtle high-shelf boost for air, low-cut at 30Hz"
  stereo_width: "wide (1.2x)"

expected_attempts: 5
fallback:
  if_attempts_fail:
    - "Try different prompt keywords"
    - "Use Udio instead of Suno"
    - "License a track (Artlist, Epidemic Sound)"
    - "Last resort: hire composer"

output:
  format: "WAV 48kHz 24bit (master) + MP3 320kbps (preview)"
  paths:
    master: "assets/audio/music-01_v4-master.wav"
    preview: "assets/audio/music-01_v4-preview.mp3"
  duration: "45.0s"
  status: "approved"
  notes: "Suno v3.5, version 4, with Hijaz scale influence"
```

---

## 3. SFX Layers (المؤثرات)

### SFX-01 — Door Open

```yaml
layer_id: "SFX-01"
type: "sfx"
purpose: "صوت فتح الباب عند دخول SAMI-01"

description: "صوت فتح باب خشبي ثقيل في صمت الفجر، صرير خفيف"

source:
  strategy: "AI generated"
  model: "ElevenLabs Sound Effects"
  prompt: |
    A heavy wooden door opening slowly in a quiet
    interior, with a soft creaking sound. Old hinges.
    No other ambient sounds. Close perspective.

timestamps:
  start: "0.0s"  # أول صوت عند بداية MOT-SC01-SH02
  end: "1.5s"
  fade_in: "0.0s (sharp)"
  fade_out: "0.2s"

volume_db: -12  # أعلى من ambience، يلفت الانتباه

processing:
  eq: "cut low rumble, boost mid frequencies"
  reverb: "light, interior (room size small)"

output:
  format: "WAV 48kHz 24bit"
  path: "assets/audio/sfx-01_v2.wav"
  duration: "1.5s"
  status: "approved"
```

### SFX-02 — Coffee Pour

```yaml
layer_id: "SFX-02"
type: "sfx"
purpose: "صوت صب القهوة"

description: "صوت صب سائل من إبريق نحاسي في فنجان صغير، صوت ناعم ودافئ"

source:
  strategy: "AI generated"
  model: "ElevenLabs Sound Effects"
  prompt: |
    The sound of dark coffee being poured from a brass
    pot (dallah) into a small ceramic cup. Smooth,
    continuous pour, gentle flow. No other sounds.
    Close perspective.

timestamps:
  start: "MOT-SC01-SH03 mid-pour start (3.5s into shot)"
  end: "MOT-SC01-SH03 pour end (6.5s into shot)"
  duration: "3.0s"

volume_db: -8  # high, this is a key moment

processing:
  eq: "boost 2-4kHz for liquid clarity"
  reverb: "minimal, close perspective"

output:
  format: "WAV 48kHz 24bit"
  path: "assets/audio/sfx-02_v1.wav"
  duration: "3.0s"
  status: "approved"
```

### SFX-03 — Cup Place

```yaml
layer_id: "SFX-03"
type: "sfx"
purpose: "صوت وضع الفنجان على الطاولة"

description: "صوت خفيف لوضع فنجان سيراميك على سطح خشبي"

source:
  strategy: "AI generated"
  model: "ElevenLabs Sound Effects"
  prompt: |
    A small ceramic cup being placed gently on a
    wooden table surface. Soft contact sound, no
    scraping.

timestamps:
  start: "MOT-SC01-SH04 end (last 0.5s)"
  duration: "0.5s"

volume_db: -10
```

### SFX-04..N

[نفس النمط لكل مؤثر]

---

## 4. Foley Layers (الأصوات اليومية)

### FOLEY-01 — Footsteps

```yaml
layer_id: "FOLEY-01"
type: "foley"
purpose: "خطوات SAMI-01 على البلاط"

description: "ثلاث خطوات بطيئة على بلاط تقليدي، حذاء جلدي"

source:
  strategy: "library"
  library: "BBC Sound Effects / Sonniss GDC Audio Bundle"
  path_in_library: "footsteps/wood_tile/slow_male_3steps.wav"
  notes: "If not in library, generate with ElevenLabs SFX"

timestamps:
  step_1: "1.0s"
  step_2: "2.5s"
  step_3: "4.0s"

volume_db: -10
processing:
  eq: "boost low-mid for weight"
  reverb: "small room"
  variation: "add slight pitch variation per step (realism)"
```

### FOLEY-02 — Cloth Movement

```yaml
layer_id: "FOLEY-02"
type: "foley"
purpose: "صوت حركة الملابس (المئزر)"

description: "صوت حفيف خفيف لقماش الكتّان عند الحركة"

source:
  strategy: "library"
  library: "BBC Sound Effects"

timestamps:
  start: "5.5s"  # عند بداية MOT-SC01-SH02
  end: "8.0s"

volume_db: -16
```

---

## 5. Ambience Layers (البيئة الصوتية)

### AMBIENCE-01 — Pre-dawn Coffee House

```yaml
layer_id: "AMBIENCE-01"
type: "ambience"
purpose: "البيئة الأساسية للمقهى قبل الفجر"

description: "صمت الفجر في المقهى، صوت هادئ جدًا، همس بعيد، صرير أرضية عرضي"

source:
  strategy: "AI generated"
  model: "ElevenLabs Sound Effects"
  prompt: |
    The ambient sound of a traditional Middle Eastern
    coffee house at pre-dawn, just before the morning
    prayer. Very quiet interior atmosphere. A faint
    distant hum of the city outside. Occasional
    creaking of old wood. The very low sound of hot
    coals hissing. No voices, no music. Contemplative,
    still.

timestamps:
  start: "0.0s (film start)"
  end: "45.0s (film end, with fade out in last 5s)"
  fade_in: "0-2s (gradual)"
  fade_out: "40-45s (gradual)"

volume_db: -22  # خلفية، لا تطغى
processing:
  loop: "seamless (crossfade at 22.5s)"
  eq: "cut extreme low (below 50Hz), cut extreme high (above 12kHz)"
  stereo_width: "moderate"
```

### AMBIENCE-02 — Outdoor City (Morning)

```yaml
layer_id: "AMBIENCE-02"
type: "ambience"
purpose: "بيئة المدينة الخارجية في الصباح"

description: "صوت مدينة في الصباح الباكر، بعيد، حركة خفيفة، أصوات بعيدة"

source:
  strategy: "library"
  library: "Freesound / BBC"

timestamps:
  start: "MOT-SC05 start (transition to outdoor)"
  end: "MOT-SC05 end"
  fade_in: "1s"
  fade_out: "1s"

volume_db: -18
```

---

## 6. Lip-Sync Plan (خطة تزامن الحوار)

```yaml
lipsync_plan:
  
  total_scenes_with_lipsync: 2
  
  scenes:
    - scene_id: "SC03_SH02"
      dialogue: "DLG-01"
      strategy: "regenerate_with_audio"
      model: "hedra"
      steps:
        - "Generate DLG-01 audio (ElevenLabs)"
        - "Pass audio + image to Hedra"
        - "Generate video with synced lips"
        - "Verify lip-sync quality"
        - "If poor: fallback to voiceover_only"
      expected_attempts: 5
      fallback:
        - "vo_only: regenerate video without dialogue, add DLG-01 as voiceover in post"
        - "subtitle_overlay: write text on screen"
        - "no_dialogue: remove dialogue, use VO instead"
    
    - scene_id: "SC05_SH03"
      dialogue: "DLG-02"
      strategy: "regenerate_with_audio"
      model: "hedra"
      steps: [...]
      expected_attempts: 5
```

---

## 7. Mixing Plan (خطة المزج)

```yaml
mixing_plan:
  
  master_target: "YouTube (-14 LUFS integrated)"
  
  levels:
    dialogue_db: -3
    voiceover_db: -3
    music_db: -12
    sfx_db: -10 (variable, depends on importance)
    foley_db: -15
    ambience_db: -22
  
  ducking:
    music_under_voiceover:
      amount: "-6dB"
      attack: "200ms"
      release: "500ms"
      trigger: "VO-01, DLG-01, DLG-02"
  
  panning:
    dialogue: "center"
    voiceover: "center (or 80% L if more intimate)"
    music: "stereo wide"
    ambience: "stereo wide"
    sfx: "match screen position"
  
  eq_zones:
    dialogue: "boost 3kHz presence, 8kHz air, cut 200Hz"
    music: "subtle high-shelf +3dB at 10kHz"
    ambience: "cut 50Hz, cut 12kHz (remove rumble + hiss)"
    sfx: "context-dependent"
  
  compression:
    dialogue: "3:1, attack 5ms, release 50ms"
    music: "1.5:1, soft (master bus)"
    sfx: "varies"
  
  reverb_sends:
    dialogue: "minimal (5-10% wet)"
    voiceover: "minimal"
    ambience: "100% (its own space)"
    sfx: "match context"
  
  automation:
    music_ducking: "side-chain from VO tracks"
    sfx_volume: "keyframed for impact moments"
    ambience_fade: "smooth in/out"
```

---

## 8. Mastering Plan (خطة الماسترينغ)

```yaml
mastering_plan:
  
  target_platforms:
    primary:
      name: "YouTube"
      target_lufs: -14
      peak_dbfs: -1
    secondary:
      - name: "Instagram Feed"
        target_lufs: -16
        peak_dbfs: -1
      - name: "TikTok"
        target_lufs: -14
        peak_dbfs: -1
  
  processing:
    final_eq: "subtle smile curve, +2dB at 100Hz, +1dB at 10kHz"
    final_compression: "1.5:1, master bus"
    limiter: "true peak -1dBFS"
    loudness_meter: "YouTube loudness penalty check"
  
  output_formats:
    master: "WAV 48kHz 24bit"
    web_h264: "MP4 with AAC 320kbps audio"
    social: "MP4 1080p with normalized audio per platform"
  
  tools:
    primary: "iZotope Ozone (AI Master)"
    alternative: "LANDR (AI)"
    manual: "Pro Tools, Logic Pro, Ableton"
```

---

## 9. Generation Workflow (سير التوليد)

```yaml
workflow:
  
  step_1_setup:
    duration_minutes: 15
    actions:
      - "تثبيت نماذج الصوت (ElevenLabs, Suno)"
      - "إنشاء voice clone (إن لزم)"
      - "تجهيز مكتبات SFX/Foley"
  
  step_2_generate_voice_layers:
    duration_minutes: 30
    actions:
      - "ولّد VO-01, VO-02, ... (voiceovers)"
      - "ولّد DLG-01, DLG-02, ... (dialogue)"
      - "كل واحد 3 محاولات، اختر الأفضل"
  
  step_3_generate_music:
    duration_minutes: 30
    actions:
      - "ولّد MUSIC-01 (5 محاولات)"
      - "اختر الأفضل، أو ادمج"
      - "أضف ducking automation"
  
  step_4_generate_sfx_foley:
    duration_minutes: 30
    actions:
      - "ولّد أو استورد كل SFX"
      - "ولّد أو استورد كل Foley"
      - "طبّق EQ + volume"
  
  step_5_generate_ambience:
    duration_minutes: 15
    actions:
      - "ولّد أو استورد كل ambience layers"
      - "تأكد من seamless loop"
  
  step_6_mix:
    duration_minutes: 30
    actions:
      - "استورد كل الطبقات في DAW"
      - "طبق mixing plan"
      - "تأكد من ducking VO"
      - "تأكد من levels"
  
  step_7_master:
    duration_minutes: 15
    actions:
      - "طبق mastering chain"
      - "تحقق من LUFS"
      - "صدّر بصيغ متعددة"
  
  step_8_qc:
    duration_minutes: 15
    actions:
      - "استمع لكل منصة مستهدفة"
      - "تحقق من no clipping"
      - "تحقق من loudness target"
```

---

## 10. Inventory (جرد الطبقات)

```yaml
inventory:
  voice_layers:
    - VO-01
    - VO-02
    - DLG-01
    - DLG-02
    total: 4
  
  music_layers:
    - MUSIC-01
    total: 1
  
  sfx_layers:
    - SFX-01 (door)
    - SFX-02 (pour)
    - SFX-03 (cup place)
    - ...
    total: 5
  
  foley_layers:
    - FOLEY-01 (footsteps)
    - FOLEY-02 (cloth)
    total: 2
  
  ambience_layers:
    - AMBIENCE-01 (interior)
    - AMBIENCE-02 (outdoor)
    total: 2
  
  total_layers: 14
  total_duration_seconds: 45
  total_lipsync_scenes: 2
```

---

## Cross-References

- **Production Blueprint:** `schemas/production-blueprint.md`
- **Image Prompts Package:** `schemas/image-prompts-package.md`
- **Motion Prompts Package:** `schemas/motion-prompts-package.md` (للـ lipsync)
- **Assembly Guide:** `schemas/assembly-guide.md` (للـ mix النهائي)
- **Script:** في `schemas/production-blueprint.md` section 6
```

---

## معايير الجودة

- ✅ كل طبقة لها source + timestamps + model
- ✅ Voice Cloning مخطط له (إن لزم)
- ✅ Music Structure محدد (intro → build → climax → resolve)
- ✅ Lip-Sync Strategy واضحة لكل مشهد
- ✅ Mixing Plan محدد بـ levels + ducking
- ✅ Mastering Plan محدد بـ LUFS لكل منصة
- ✅ Fallback Strategy لكل طبقة

---

## ما لا تفعله

- ❌ لا طبقة بدون source strategy
- ❌ لا تنسَ ducking (music under VO)
- ❌ لا تنسَ lipsync plan
- ❌ لا تتجاوز master LUFS
- ❌ لا تنسَ معالجة AI audio (enhance, denoise)
- ❌ لا تنسَ Foley (مهم للواقعية)
