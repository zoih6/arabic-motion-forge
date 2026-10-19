# Audio Decision Tree — شجرة قرار الصوت

## الهدف

دليل مرجعي شامل لـ **شجرة قرار الصوت** التي يستخدمها `references/specs/audio-decision-tree.md`. يغطي: متى نستخدم كل نوع، كيف ندمج الطبقات، Lip-Sync، Mixing، Mastering.

---

## الطبقات الخمس للصوت

### 1. Dialogue (الحوار)

**شخصية تتحدث على الشاشة** — يتطلب Lip-Sync.

```yaml
dialogue:
  when_use:
    - "شخصية تتحدث على الشاشة (mouth visible)"
    - "حوار بين شخصيتين"
    - "مونولوج على الشاشة"
    - "خطاب مباشر (interview)"
  
  when_NOT:
    - "إذا الشخصية تظهر من الخلف"
    - "إذا لا تريد lip-sync"
    - "إذا استخدمت voiceover بدلاً"
  
  models:
    primary: "ElevenLabs"
    fallback: "Cartesia Sonic, Resemble AI"
  
  lipsync_models:
    native_video_audio: "Veo 3, Sora (with audio)"
    regenerate_with_audio: "Hedra, Omniverse Audio2Face"
    dubbing_post: "ElevenLabs + Adobe Podcast + manual sync"
  
  challenges:
    - "lip-sync accuracy (varies 60-90%)"
    - "accent authenticity"
    - "emotion nuance"
    - "language switching"
  
  fallbacks:
    - "voiceover_only (إن فشل lip-sync)"
    - "subtitle_overlay (لا صوت)"
    - "no_dialogue (إزالة الحوار)"
```

### 2. Voiceover (السرد)

**راوي يروي فوق المشهد** — لا lip-sync.

```yaml
voiceover:
  when_use:
    - "راوي خارج الشاشة"
    - "internal monologue"
    - "documentary narration"
    - "brand film (الأكثر شيوعًا)"
    - "explanation"
  
  when_NOT:
    - "إذا الشخصية تتحدث على الشاشة (استخدم dialogue)"
    - "إذا لا تريد سرد"
  
  models:
    primary: "ElevenLabs"
    fallback: "Cartesia Sonic, Resemble AI"
    for_narration: "ElevenLabs Narrator voice"
  
  parameters:
    stability: "0.60-0.80 (more stable for narration)"
    similarity_boost: "0.70-0.85"
    style: "0.30-0.50 (calm, clear)"
    speaker_boost: "true"
  
  processing:
    enhance: "Adobe Podcast enhance"
    eq: "boost 3kHz presence, 8kHz air, cut 200Hz"
  
  writing_tips:
    - "جمل قصيرة (5-12 كلمة)"
    - "لغة واضحة"
    - "إيقاع هادئ (150-170 wpm)"
    - "pause_after_key_words"
```

### 3. Music (الموسيقى)

**موسيقى تصويرية أو خلفية.**

```yaml
music:
  when_use:
    - "أي فيديو (شائع جدًا)"
    - "Brand film (ضروري تقريبًا)"
    - "Storytelling (يعزز العاطفة)"
    - "Reel (لتعزيز الـ engagement)"
    - "Transition (بين المشاهد)"
  
  when_NOT:
    - "إذا كان الفيديو documentary صامت (نادر)"
    - "إذا كان الـ voiceover كافٍ (نادر جدًا)"
  
  sources:
    generated_ai:
      models: "Suno v3.5, Udio, Stable Audio"
      pros: "مخصص، سريع، مرن"
      cons: "جودة متفاوتة (70-85%)"
    
    licensed:
      sources: "Artlist, Epidemic Sound, Musicbed"
      pros: "100% جودة، license واضح"
      cons: "تكلفة، ليس مخصص"
    
    composer:
      pros: "100% مخصص، 100% جودة"
      cons: "تكلفة عالية، وقت"
  
  music_types_by_mood:
    energetic: "electronic uptempo (advertising, sports)"
    emotional: "cinematic orchestral, piano (drama)"
    contemplative: "ambient, soft piano (intimate)"
    suspenseful: "low brass, dark strings (thriller)"
    epic: "full orchestra + electronic (cinematic, trailer)"
    peaceful: "ambient, nature, acoustic (wellness)"
    cultural:
      arabic: "oud, qanun, maqam (عربي)"
      asian: "koto, gamelan (آسيوي)"
      african: "djembe, kora (أفريقي)"
      latin: "guitar, percussion (لاتيني)"
  
  music_structure:
    intro:
      duration: "3-5s"
      purpose: "تجهيز المزاج"
    build:
      duration: "5-15s"
      purpose: "بناء التوتر"
    climax:
      duration: "5-10s"
      purpose: "ذروة المشهد"
    resolve:
      duration: "5-15s"
      purpose: "إنزال"
    outro:
      duration: "3-5s"
      purpose: "نهاية"
  
  ducking:
    required: true
    amount: "-6dB under voice"
    attack: "200ms"
    release: "500ms"
```

### 4. SFX (Sound Effects)

**مؤثرات صوتية.**

```yaml
sfx:
  when_use:
    - "أصوات حادة (طرقعات، انفجارات)"
    - "أصوات مميزة (door slam, phone ring)"
    - "sound design (futuristic, magical)"
    - "key moments (product sound, brand sting)"
  
  when_NOT:
    - "إذا كان ambience كافٍ"
    - "إذا كان المشهد صامت عمدًا"
  
  sources:
    generated_ai:
      models: "ElevenLabs SFX, Stability Audio"
      pros: "مخصص، سريع"
      cons: "جودة متفاوتة (60-80%)"
    
    library:
      sources: "BBC, Freesound, Sonniss GDC"
      pros: "100% جودة، تنوع"
      cons: "قد لا تجد بالضبط ما تريد"
    
    recorded:
      pros: "100% دقيق"
      cons: "وقت، معدات"
  
  types:
    hard_sfx:
      - "انفجارات، طرقعات"
      - "أبواب، نوافذ"
      - "إطلاق نار (إن لزم)"
    
    soft_sfx:
      - "رياح، مطر، بحر"
      - "همهمات، أصوات بيئية"
    
    designed_sfx:
      - "sci-fi sounds"
      - "magical sounds"
      - "futuristic UI"
    
    brand_sfx:
      - "brand sting (صوت مميز للشعار)"
      - "logo reveal sound"
```

### 5. Foley (الأصوات اليومية)

**خطوات، ملابس، أدوات.**

```yaml
foley:
  when_use:
    - "واقعية عالية (drama, documentary)"
    - "حركة الشخصية (footsteps, cloth)"
    - "تفاعل مع الأشياء (cup, door)"
  
  when_NOT:
    - "إعلان سريع (غالبًا غير ضروري)"
    - "موشن جرافيك (لا شخصية)"
    - "موسيقى فيديو (الفوكاز على الموسيقى)"
  
  types:
    footsteps:
      materials: ["leather shoes on tile", "bare feet on wood", "boots on gravel"]
      libraries: "BBC, Sonniss GDC"
      importance: "high (لواقعية)"
    
    cloth_movement:
      materials: ["linen apron", "cotton shirt", "wool coat"]
      when: "character moves"
      importance: "medium"
    
    object_sounds:
      types: ["cup on table", "pot on stove", "paper rustling"]
      when: "interaction"
      importance: "high"
  
  best_practices:
    - "اجمع foley في post-production"
    - "أو: استخدم مكتبات احترافية"
    - "أو: AI generation كبداية، ثم تحسين"
```

### 6. Ambience (البيئة الصوتية)

**الصوت المستمر للمكان.**

```yaml
ambience:
  when_use:
    - "دائمًا (نعم، حتى في 'الصمت')"
    - "تأسيس المكان"
    - "ربط المشاهد"
    - "إضافة عمق"
  
  when_NOT:
    - "نادرًا (يمكن تجاهله في 5% من الحالات)"
  
  types:
    nature: "غابة، بحر، صحراء، مطر، ريح"
    urban: "مدينة، مقهى، شارع، مكتب"
    interior: "غرفة، مصنع، بيت"
    silence: "صمت درامي (طبقة صامتة، لا غياب)"
  
  sources:
    generated_ai:
      models: "ElevenLabs SFX"
      pros: "مخصص، سريع"
      cons: "متوسط الجودة"
    
    library:
      sources: "BBC, Freesound, Soundsnap"
      pros: "100% جودة، تنوع"
    
    recorded:
      pros: "100% دقيق"
      cons: "وقت"
  
  best_practices:
    - "ambience موجود دائمًا (لا صمت مطلق)"
    - "loop seamless (تقاطع بدون نقطة)"
    - "volume منخفضة (-18 to -22 dB)"
    - "stereo wide (للعمق)"
```

---

## شجرة القرار الكاملة

```yaml
audio_decision:
  
  # Q1: ما نوع المحتوى؟
  q1_content_type:
    product_ad: "see matrix product_ad"
    brand_film: "see matrix brand_film"
    short_film: "see matrix short_film"
    music_video: "see matrix music_video"
    documentary: "see matrix documentary"
    explainer: "see matrix explainer"
    social_reel: "see matrix social_reel"
    silent_film: "see matrix silent_film"
  
  # Q2: هل يوجد حوار على الشاشة؟
  q2_screen_dialogue:
    if_yes:
      lipsync_required: true
      go_to: "lip_sync_strategy"
    if_no:
      lipsync_required: false
  
  # Q3: هل يوجد voiceover/سرد؟
  q3_voiceover:
    if_yes:
      add_layer: "voiceover"
    if_no:
      skip_layer: "voiceover"
  
  # Q4: نوع الموسيقى؟
  q4_music:
    needed: "almost always (95%)"
    if_yes:
      genre: "based on mood"
      source: "AI generated or licensed"
    if_no:
      skip_layer: "music (rare)"
  
  # Q5: المؤثرات؟
  q5_sfx:
    if_yes:
      add_layer: "sfx"
    if_no:
      skip_layer: "sfx"
  
  # Q6: Foley؟
  q6_foley:
    if_realistic:
      add_layer: "foley"
    if_stylized:
      skip_layer: "foley"
  
  # Q7: Ambience؟
  q7_ambience:
    always: "yes (99%)"
```

---

## Matrix حسب نوع المشروع

### 1. إعلان منتج (15-30s)

```yaml
product_ad:
  dialogue: "optional (CTA in 1-2 sentences)"
  voiceover: "common (3-4 sentences)"
  music: "yes (energetic, 70-80%)"
  sfx: "yes (product sound, brand sting)"
  foley: "minimal"
  ambience: "minimal or none"
  
  ratios:
    music: 70%
    voiceover: 30%
    ambience: 0%
    foley: 0%
    sfx: variable (key moments)
  
  lipsync_required: false (voiceover is outside)
  
  music_mood: "energetic, modern, hopeful"
  voiceover_tone: "clear, confident, inviting"
  
  master_lufs: -14 (YouTube) / -16 (Instagram)
```

### 2. Brand Film (60-90s)

```yaml
brand_film:
  dialogue: "rare"
  voiceover: "yes (main narration)"
  music: "yes (emotional, 60-80%)"
  sfx: "minimal (moments only)"
  foley: "light to medium"
  ambience: "light (during silence)"
  
  ratios:
    music: 60%
    voiceover: 25%
    ambience: 10%
    foley: 5%
  
  lipsync_required: false
  
  music_mood: "emotional, cinematic, hopeful"
  voiceover_tone: "intimate, warm, like a memory"
  
  master_lufs: -14
```

### 3. فيلم قصير (3-10 min)

```yaml
short_film:
  dialogue: "yes (multi-character)"
  voiceover: "optional"
  music: "yes (emotional, 50-70%)"
  sfx: "yes (per scene)"
  foley: "very important"
  ambience: "continuous (no absolute silence)"
  
  ratios:
    dialogue: 30%
    music: 40%
    ambience: 15%
    foley: 10%
    sfx: 5%
  
  lipsync_required: "yes if dialogue present"
  
  music_mood: "varies per scene"
  
  master_lufs: -14
```

### 4. فيديو موسيقي (Music Video)

```yaml
music_video:
  dialogue: "no usually"
  voiceover: "no"
  music: "yes (100% of audio)"
  sfx: "minimal (beat sync)"
  foley: "no usually"
  ambience: "no"
  
  ratios:
    music: 100%
  
  lipsync_required: "yes (lip-sync to lyrics)"
  
  music_mood: "the song itself"
  
  master_lufs: -14
```

### 5. وثائقي

```yaml
documentary:
  dialogue: "yes (interviews)"
  voiceover: "yes (narration)"
  music: "light (transitions only)"
  sfx: "light"
  foley: "light"
  ambience: "important (realism)"
  
  ratios:
    dialogue: 40%
    voiceover: 25%
    ambience: 20%
    music: 10%
    foley: 5%
  
  lipsync_required: "yes (interviews)"
  
  music_mood: "subtle, ambient, traditional"
  
  master_lufs: -14
```

### 6. تعليمي/شرح

```yaml
explainer:
  dialogue: "no (unless character)"
  voiceover: "yes (explanation)"
  music: "light (background)"
  sfx: "yes (UI sounds, transitions)"
  foley: "no"
  ambience: "light"
  
  ratios:
    voiceover: 70%
    music: 15%
    sfx: 10%
    ambience: 5%
  
  lipsync_required: "no (voiceover only)"
  
  music_mood: "upbeat, modern, light"
  
  master_lufs: -14
```

### 7. Social Media Reel (15-60s)

```yaml
social_reel:
  dialogue: "yes (or captions)"
  voiceover: "sometimes"
  music: "yes (trending audio)"
  sfx: "yes (whoosh, pop, swish)"
  foley: "light"
  ambience: "light"
  
  ratios:
    music: 50%
    voiceover: 30%
    sfx: 15%
    ambience: 5%
  
  lipsync_required: "if dialogue visible"
  
  music_mood: "trending, energetic, recognizable"
  note: "trending audio may be required for reach"
  
  master_lufs: -14 (TikTok) / -16 (Instagram)
```

### 8. Silent / Visual-only

```yaml
silent_film:
  dialogue: "no"
  voiceover: "no"
  music: "yes (essential)"
  sfx: "yes (key moments)"
  foley: "light"
  ambience: "yes (essential)"
  
  ratios:
    music: 70%
    ambience: 20%
    sfx: 5%
    foley: 5%
  
  lipsync_required: "no"
  
  music_mood: "emotional, supportive"
  
  master_lufs: -14
```

---

## Lip-Sync Strategy

### متى تحتاج Lip-Sync؟

```yaml
lipsync_required:
  - "شخصية تتحدث على الشاشة (mouth visible)"
  - "حوار بين شخصيتين"
  - "مونولوج على الشاشة"
  - "interview"

lipsync_NOT_required:
  - "voiceover (راوي خارج الشاشة)"
  - "internal monologue (فم مغلق)"
  - "لا حوار"
  - "الشخصية تظهر من الخلف"
```

### الاستراتيجيات الأربع

```yaml
strategy_1_native_video_audio:
  description: "النموذج يولّد الفيديو والصوت معًا"
  models:
    - "Veo 3 (Google)"
    - "Sora (OpenAI) — مع audio"
    - "Runway Gen-4 — مع audio"
  pros:
    - "أسهل، مزامنة تلقائية"
    - "أقل تعقيدًا"
  cons:
    - "جودة الصوت متوسطة (70-80%)"
    - "تحكم محدود في الصوت"
  success_rate: "70-85%"
  best_for: "محتوى سريع، ريل، تجريبي"

strategy_2_regenerate_with_audio:
  description: "ولّد video، ثم regenerate مع audio reference"
  models:
    - "Hedra"
    - "Omniverse Audio2Face"
    - "Synthesia (لـ avatars)"
  pros:
    - "تحكم في الصوت منفصل"
    - "جودة صوت أعلى"
  cons:
    - "خطوتين"
    - "مزامنة يدوية أحيانًا"
  success_rate: "75-90%"
  best_for: "إعلانات، brand films"

strategy_3_dubbing_post:
  description: "ولّد video بدون صوت، أضف dialogue في post"
  workflow:
    - "video_model: يولّد بدون حوار (فم مغلق أو حركة بدون صوت)"
    - "elevenlabs: يولّد dialogue audio"
    - "adobe_podcast: enhance الصوت"
    - "premiere/davinci: مزامنة يدوية"
  pros:
    - "أعلى جودة صوت (90-95%)"
    - "تحكم كامل"
  cons:
    - "manual sync (صعب على 10+ مشاهد)"
    - "وقت أطول"
  success_rate: "90-95%"
  best_for: "محتوى احترافي، brand films"

strategy_4_avoid_lipsync:
  description: "تجنب الحاجة أصلًا"
  methods:
    - "voiceover_only"
    - "شخصية لا ترى وجهها (من الخلف)"
    - "لقطة CU على يد أو شيء آخر"
    - "نص مكتوب (subtitles)"
    - "لقطة على المرآة (الوجه ينعكس، يمكن التحكم)"
  pros:
    - "بدون تعقيد lip-sync"
  cons:
    - "ليس مناسبًا لكل قصة"
  success_rate: "100% (لا lip-sync = لا مشكلة)"
  best_for: "محتوى سريع، voiceover-focused"
```

### نصائح Lip-Sync

```yaml
lipsync_tips:
  general:
    - "كلام بطيء (2-3 كلمات/ثانية) أسهل في المزامنة"
    - "وجه مستقيم (not profile) أفضل"
    - "إضاءة جيدة على الوجه"
    - "لا تحريك قوي للرأس أثناء الكلام"
  
  prompt_optimization:
    - "speaking slowly"
    - "mouth moving in sync with speech"
    - "clear lip movement"
    - "natural speech rhythm"
  
  fallback_hierarchy:
    1: "native_video_audio (أبسط)"
    2: "regenerate_with_audio (Hedra)"
    3: "dubbing_post (الأعلى جودة)"
    4: "avoid_lipsync (لا حوار)"
    5: "subtitle_overlay (آخر حل)"
  
  testing_protocol:
    - "ولّد 3-5 محاولات"
    - "اختر الأفضل"
    - "إذا < 70% نجاح: fallback"
```

---

## Music Design المتقدم

### Music Prompt Engineering

```yaml
music_prompts_by_type:
  
  advertising_energetic:
    prompt: |
      Upbeat electronic music, energetic, modern, suitable
      for a 30-second product advertisement. BPM 120, building
      energy throughout, hopeful and confident, with a clear
      brand sting at the end (2 seconds, distinctive sound).
      Instrumental only, no vocals.
    suno_tags: "electronic, upbeat, advertising, instrumental, energetic, modern"
  
  brand_film_emotional:
    prompt: |
      Cinematic emotional music for a 60-second brand film
      about craftsmanship and tradition. Piano-led with light
      strings, building to a hopeful climax. Modern cinematic
      feel with subtle Arabic maqam influences (Hijaz scale).
      Emotional arc: contemplative → awakening → confident.
      Instrumental only, no vocals.
    suno_tags: "cinematic, emotional, piano, strings, hopeful, arabic_maqam"
  
  suspense_thriller:
    prompt: |
      Dark suspenseful music, low brass, deep strings, minimal
      percussion, building tension. Modern thriller style, 90 BPM.
      Subtle dissonant harmonies. No vocals.
    suno_tags: "suspense, dark, thriller, cinematic, brass, strings"
  
  documentary_ambient:
    prompt: |
      Subtle ambient underscore, contemplative, light piano with
      atmospheric pads. Suitable for documentary narration.
      Unobtrusive, supports voiceover without competing.
      Gentle, hopeful undertone.
    suno_tags: "ambient, documentary, piano, subtle, atmospheric"
  
  music_video_edm:
    prompt: |
      High-energy EDM track, 128 BPM, driving beat, synth
      leads, modern drop at the chorus. Suitable for a 3-minute
      music video. Electronic with hints of trap percussion.
    suno_tags: "edm, electronic, energetic, drop, modern, dance"
  
  acoustic_intimate:
    prompt: |
      Acoustic guitar and soft vocals, intimate, singer-songwriter
      style. Suitable for a personal story or vlog. Warm, organic,
      slightly melancholic. 90 BPM.
    suno_tags: "acoustic, intimate, guitar, vocals, singer-songwriter"
```

### هيكل الأغنية

```yaml
song_structure_for_film:
  
  intro:
    duration: "3-5s"
    purpose: "تجهيز المزاج"
    elements: "instrumentation only, light"
  
  verse_1:
    duration: "15-25s"
    purpose: "بناء القصة"
    elements: "vocals enter, simple accompaniment"
  
  chorus_1:
    duration: "10-15s"
    purpose: "ذروة عاطفية"
    elements: "full instrumentation, hook"
  
  verse_2:
    duration: "15-25s"
    purpose: "تطوير"
    elements: "similar to verse 1, slight variation"
  
  chorus_2:
    duration: "10-15s"
    purpose: "ذروة (أكبر)"
    elements: "bigger than chorus 1"
  
  bridge:
    duration: "8-12s"
    purpose: "تحول"
    elements: "different feel, builds to final chorus"
  
  chorus_3:
    duration: "10-15s"
    purpose: "ذروة نهائية"
    elements: "biggest, most emotional"
  
  outro:
    duration: "5-10s"
    purpose: "حل"
    elements: "fade out, similar to intro"
```

---

## Sound Design مفصّل

### مثال: مشهد في مقهى

```yaml
sound_design_sanaani_coffee:
  
  scene: "SC01 — الاستيقاظ المتعب"
  duration: "8s"
  
  layers:
    
    - layer: "ambience"
      source: "AI generated (ElevenLabs SFX)"
      prompt: "early morning interior room tone, very quiet, slight hum, hint of distant city"
      duration: "8s (full scene)"
      fade_in: "0.5s"
      fade_out: "1s"
      volume_db: -22
      stereo_width: "wide"
    
    - layer: "foley_footsteps"
      source: "library (BBC)"
      prompt: "soft footsteps on tile floor, three steps, man, slow, leather shoes"
      timestamps:
        - "1.0s: step 1"
        - "2.5s: step 2"
        - "4.0s: step 3"
      volume_db: -10
    
    - layer: "foley_cloth"
      source: "library"
      prompt: "linen cloth movement, apron rustle"
      timestamp: "5.5s"
      volume_db: -16
    
    - layer: "sfx_dallah"
      source: "AI generated"
      prompt: "traditional brass coffee pot being set on hot coals, soft metallic sound"
      timestamp: "5.0s"
      volume_db: -8
    
    - layer: "ambience_steam"
      source: "library"
      prompt: "subtle steam hissing from hot pot, very quiet"
      duration: "5-8s"
      volume_db: -22
    
    - layer: "voiceover"
      source: "ElevenLabs TTS"
      text: "كل يوم، نفس الاستيقاظ. نفس الجسد. نفس السؤال."
      language: "ar"
      dialect: "yemeni_sanaani"
      timestamps: "0-4s"
      volume_db: -3
      processing: "Adobe Podcast enhance"
    
    - layer: "music"
      source: "Suno generated"
      prompt: "see brand_film_emotional"
      structure: "intro (first 8s, fades in 0.5s)"
      volume_db: -12
      duck_under_voiceover: "-6dB during VO"
  
  mixing:
    dialogue_db: -3
    music_db: -12 (with -6dB ducking under VO)
    sfx_db: -8 (key moments)
    foley_db: -10 to -16
    ambience_db: -22
    
  total_layers: 7
  total_audio_complexity: "high"
```

---

## Mixing Levels Reference

```yaml
mixing_levels:
  
  dialogue:
    target_db: -3
    notes: "الأعلى، يجب أن يكون مسموعًا دائمًا"
  
  voiceover:
    target_db: -3
    notes: "نفس الحوار"
  
  music:
    target_db: -12
    notes: "ducking تحت VO بمقدار -6dB"
    no_ducking: -8 (إذا لا VO)
  
  sfx:
    target_db: "-8 to -12 (variable)"
    notes: "حسب أهمية اللحظة"
  
  foley:
    target_db: "-10 to -16"
    notes: "خفيف، يضيف واقعية"
  
  ambience:
    target_db: -22
    notes: "الأخفض، خلفية فقط"
  
  mastering:
    master_lufs_youtube: -14
    master_lufs_instagram: -16
    master_lufs_tiktok: -14
    master_lufs_broadcast: -23
    master_lufs_cinema: -20
    true_peak_max: -1 dBFS
```

---

## Mastering Plan

```yaml
mastering:
  
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
      - name: "Facebook"
        target_lufs: -16
        peak_dbfs: -1
      - name: "Twitter/X"
        target_lufs: -14
        peak_dbfs: -1
      - name: "Cinema"
        target_lufs: -20
        peak_dbfs: -2
  
  processing_chain:
    - "Subtle EQ (smile curve, +2dB at 100Hz, +1dB at 10kHz)"
    - "Multiband compression (1.5:1, soft)"
    - "Stereo widening (subtle, +10%)"
    - "Limiter (true peak -1dBFS)"
    - "Loudness normalization (per platform)"
  
  tools:
    primary: "iZotope Ozone (AI Master)"
    alternative: "LANDR (AI)"
    manual: "Pro Tools, Logic Pro, Ableton, DaVinci Fairlight"
  
  quality_check:
    - "LUFS matches target"
    - "No clipping (true peak < -1 dBFS)"
    - "No audible pumping (compression)"
    - "Stereo image is clean (no phase issues)"
    - "Listen on multiple devices (headphones, speakers, phone)"
```

---

## Voice Cloning Strategy

```yaml
voice_cloning:
  
  when_use:
    - "الشخصية لها صوت مميز وثابت"
    - "الفيلم طويل (يستحق العناء)"
    - "الـ brand voice مهم"
    - "voice consistency مطلوب"
  
  when_NOT:
    - "فيلم قصير (1-2 voice lines)"
    - "صوت غير مميز"
    - "لا وقت للاستنساخ"
  
  tools:
    - "ElevenLabs (5-30 min audio sample)"
    - "Resemble AI (1-10 min sample)"
    - "PlayHT (varied options)"
    - "Cartesia (real-time, lower quality)"
  
  process:
    step_1_collect_samples:
      - "5-30 min من صوت الهدف (نظيف، بدون ضوضاء)"
      - "مجموعة متنوعة (حوار، عاطفة، هدوء)"
    
    step_2_train_model:
      - "ElevenLabs: Instant Voice Clone (5 min audio) or Professional Clone (30 min)"
      - "انتظر 5-10 دقائق للمعالجة"
    
    step_3_test:
      - "اختبر مع السكريبت"
      - "اضبط parameters (stability, similarity, style)"
    
    step_4_validate:
      - "هل يحاكي الصوت الأصلي؟"
      - "هل العاطفة مناسبة؟"
      - "هل اللهجة صحيحة؟"
  
  challenges:
    - "اللهجات المحلية (Yemeni, Saudi, etc.)"
    - "العواطف الدقيقة (حزن خفيف vs حزن عميق)"
    - "العمر الصوتي (لا يطابق العمر الحقيقي أحيانًا)"
    - "الموافقات القانونية (استخدم صوتك فقط أو بإذن)"
  
  parameters_tuning:
    stability:
      high: "0.80+ (متسق، أقل تعبيرًا)"
      medium: "0.50-0.70 (متوازن)"
      low: "0.30- (متغير، أكثر تعبيرًا)"
    
    similarity_boost:
      high: "0.85+ (يقلد الأصل)"
      low: "0.50- (حرية أكبر)"
    
    style:
      high: "0.50+ (يعبّر عن العاطفة)"
      low: "0.20- (محايد)"
```

---

## AI Audio Processing

```yaml
ai_audio_processing:
  
  voice_enhancement:
    tool: "Adobe Podcast Enhance"
    what: "clarity, presence, noise reduction"
    when: "always (لكل voiceover/dialogue)"
  
  music_mastering:
    tools: "LANDR, iZotope Ozone, eMastered"
    when: "always (لكل موسيقى)"
  
  noise_reduction:
    tool: "iZotope RX"
    features: "Voice De-noise, De-click, De-reverb"
    when: "إذا كان الصوت فيه ضوضاء"
  
  de_essing:
    tool: "iZotope RX, manual EQ"
    what: "إزالة 'س' الزائد"
    when: "إذا كانت 'س' حادة"
  
  breath_control:
    tool: "manual edit or iZotope RX Breath Control"
    when: "إذا كانت الأنفاس مزعجة"
  
  dialogue_isolation:
    tool: "iZotope RX Dialogue Isolate"
    what: "فصل الحوار عن الضوضاء"
    when: "إذا كان الحوار في بيئة صاخبة"
```

---

## Common Mistakes

### ❌ 1. VO والموسيقى في نفس المستوى

```yaml
problem: "الموسيقى تطغى على VO"
fix: "Ducking بمقدار -6dB على الأقل"
```

### ❌ 2. لا ducking

```yaml
problem: "الموسيقى تستمر في نفس مستوى VO"
fix: "Side-chain compression من VO track"
```

### ❌ 3. Master LUFS خاطئ

```yaml
problem: "الفيديو صامت على YouTube"
fix: "تأكد من -14 LUFS لـ YouTube، -16 لـ Instagram"
```

### ❌ 4. لا معالجة AI audio

```yaml
problem: "الصوت فيه ضوضاء أو رنين"
fix: "Adobe Podcast enhance + iZotope RX"
```

### ❌ 5. Lip-sync ضعيف

```yaml
problem: "الشفتين لا تتطابق مع الصوت"
fix: "Hedra أو Veo 3 native، أو voiceover fallback"
```

### ❌ 6. لا ambience

```yaml
problem: "'الصمت' مطلق، يبدو ميتًا"
fix: "حتى في الصمت الدرامي، ضع طبقة ambience خفيفة جدًا"
```

---

## Quick Reference

| السؤال | الجواب |
|---|---|
| هل أحتاج موسيقى؟ | 95% نعم |
| هل أحتاج voiceover؟ | 50% نعم (يعتمد على النوع) |
| هل أحتاج lip-sync؟ | فقط إذا الحوار على الشاشة |
| ما LUFS لـ YouTube؟ | -14 |
| ما LUFS لـ Instagram؟ | -16 |
| ما LUFS لـ TikTok؟ | -14 |
| ما هو ducking؟ | الموسيقى تنخفض -6dB تحت VO |
| كيف أعالج الصوت؟ | Adobe Podcast + iZotope RX |
| كيف أُنتج موسيقى؟ | Suno, Udio, أو licensed |
| كيف أتعامل مع lip-sync؟ | Hedra, Veo 3, أو voiceover |
