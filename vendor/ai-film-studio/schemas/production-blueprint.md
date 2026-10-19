# 01 — Production Blueprint (المخطط الإنتاجي)

## الهدف

**الملف الأول من حزمة الإنتاج الخماسية.** يقدّم النظرة الشاملة للمشروع: المفهوم، القصة، المشاهد، السكريبت، البصمة البصرية، والصوت. هو **المرجع الأعلى** الذي يُقرأ قبل أي prompt أو تنفيذ.

> **يُنتَج من قبل:** `30-executive-producer` (بعد M0–M9).

---

## كيف تستخدمه

1. املأ كل قسم عند إنجاز المرحلة المقابلة
2. اربط الأقسام ببعضها (cross-references)
3. لا تترك حقول فارغة (إذا غير قابل للتطبيق، اكتب "N/A" مع السبب)
4. احفظ في `schemas/state/production-blueprint.md` (نسخة محدثة) + `schemas/production-blueprint.md` (نسخة نهائية)

---

## القالب الكامل

```markdown
# Production Blueprint — [اسم المشروع]

**التاريخ:** [ISO]
**الحالة:** [DRAFT / IN_REVIEW / APPROVED / IN_PRODUCTION / DELIVERED]
**الإصدار:** v[X.Y]
**المعد:** AI Film Studio v2.0 (Executive Producer)

---

## 1. Project Metadata

```yaml
project:
  title: "[العنوان]"
  type: "[إعلان / Brand Film / قصة / وثائقي / شرح / موشن جرافيك / فيديو موسيقي / ريل]"
  duration: "[Xs or X:XX]"
  format:
    primary: "16:9 / 9:16 / 1:1 / 21:9 / 4:3"
    secondary: []
  resolution: "1080p / 4K / 8K"
  fps: "24 / 25 / 30 / 60"
  language: "ar / en / bilingual"
  dialect: "[لهجة]"
  platform:
    primary: "YouTube / Instagram / TikTok / TV / Cinema / Website"
    secondary: []
  target_audience:
    age_range: "..."
    interests: "..."
    region: "..."
  budget_tier: "low / mid / high / unlimited"
  deadline: "[تاريخ]"
```

---

## 2. Concept (المفهوم)

```yaml
concept:
  logline: "[شخصية + رغبة + عائق + ثمن]"
  one_liner: "[جملة واحدة تبيع الفكرة]"
  core_message: "[الرسالة المركزية]"
  visual_metaphor: "[الاستعارة البصرية]"
  genre: "[النوع]"
  tone: "[النبرة]"
  pace: "[الإيقاع]"
  
  inspiration:
    films: ["فيلم 1", "فيلم 2"]
    ads: ["إعلان 1"]
    art: ["فنان 1"]
  
  why_this_works:
    - "[سبب 1]"
    - "[سبب 2]"
```

---

## 3. Story Structure (البنية السردية)

```yaml
story_structure:
  type: "3-Act / 25-50-25 / Hook-Body-Payoff / Hero's Journey / Problem-Solution"
  chosen_reason: "[لماذا هذا النوع]"
  total_beats: ...
  
  story_spine:
    - beat: 1
      description: "..."
    - beat: 2
      ...
  
  emotional_map:
    - time: "0%"
      emotion: "..."
      intensity: 0-10
    - time: "20%"
      ...
```

---

## 4. Character Arc (قوس الشخصية)

```yaml
character_arc:
  character_id: "..."
  start_state: "..."
  end_state: "..."
  transformation: "..."
  lie_they_believe: "..."
  truth_they_learn: "..."
  want_vs_need:
    want: "..."
    need: "..."
```

---

## 5. Scenes (المشاهد)

```yaml
scenes:
  - id: "SC01"
    title: "..."
    duration: "8s"
    purpose: "..."
    location_id: "LOC-01"
    characters: ["SAMI-01"]
    time_of_day: "..."
    emotional_state: "..."
    key_beats:
      - "0-3s: ..."
      - "3-5s: ..."
      - "5-8s: ..."
    transition_out: "match_cut"
    transition_reason: "..."
    cumulative_time: "0-8s"
  
  - id: "SC02"
    title: "..."
    duration: "..."
    cumulative_time: "8-15s"
    ...
  
  # ... باقي المشاهد
```

---

## 6. Script (السكريبت)

```yaml
script:
  total_words: ...
  total_duration: "..."
  words_per_second: ...
  
  voiceover:
    - id: "VO-01"
      scene: "SC01"
      timestamp: "0-3s"
      text: "[النص]"
      language: "..."
      delivery: "[هادئ، سريع، يائس، ...]"
  
  dialogue:
    - id: "DLG-01"
      scene: "SC02"
      timestamp: "5-7s"
      speaker: "..."
      text: "[النص]"
      direction: "..."
  
  on_screen_text:
    - id: "OST-01"
      scene: "SC06"
      timestamp: "0-3s"
      text: "[النص]"
      execution_strategy: "post_overlay"
```

---

## 7. Visual Grammar (القواعد البصرية)

### 7.1 Camera

```yaml
camera_grammar:
  default:
    lens: "35mm"
    aperture: "f/2.0"
    dof: "shallow"
    height: "eye_level"
    motion: "static_or_slow_dolly"
  sensor: "ARRI Alexa 35"
  film_stock: "Kodak Vision3 500T"
  forbidden_movements:
    - "handheld_without_reason"
    - "whip_pan"
    - "360_orbit"
    - "macro_establishing"
```

### 7.2 Lighting

```yaml
lighting_grammar:
  overall: "low_key_dramatic / high_key_clean / mixed"
  key_light: "..."
  fill: "..."
  rim: "..."
  practical_lights: [...]
  atmosphere: [...]
  color_temperature_mix: "..."
  forbidden:
    - "أحمر مشبع"
    - "نيون"
```

### 7.3 Color Palette

```yaml
color_palette:
  primary:
    - name: "primary_brown"
      hex: "#3B2F2F"
      usage: "..."
  secondary:
    - name: "warm_amber"
      hex: "#C9A66B"
      usage: "..."
  forbidden:
    - "أحمر مشبع"
    - "أصفر فلوري"
  color_script:
    "SC01": "warm_amber + deep_teal"
    "SC02": "..."
```

---

## 8. Continuity Bible (ملخص)

```yaml
continuity_bible:
  characters:
    - id: "SAMI-01"
      visual_signature: "..."
      anatomy: "..."
      forbidden_changes: [...]
  
  wardrobe:
    - character: "SAMI-01"
      scene_range: "SC01-SC06"
      items: [...]
  
  props:
    - id: "brass_dallah_01"
      ...
  
  locations:
    - id: "sanaani_coffee_house"
      ...
```

> **ملاحظة:** النسخة الكاملة في `schemas/state/continuity-bible.md`.

---

## 9. Frame Chain (ملخص)

```yaml
frame_chain:
  total_shots: ...
  chain_breaks: ...
  status: "complete"
  shots_summary:
    - shot_id: "SC01_SH01"
      duration: "10s"
      start_frame: "FRAME-001"
      end_frame: "FRAME-002"
      links_to: "SC01_SH02"
    - ...
```

> **ملاحظة:** النسخة الكاملة في `schemas/state/frame-chain.md`.

---

## 10. Audio Strategy (ملخص)

```yaml
audio_strategy:
  total_layers: ...
  dialogue: "..."
  voiceover: "..."
  music: "..."
  sfx: "..."
  foley: "..."
  ambience: "..."
  lipsync_required: [...]
  master_lufs: -14
  target_platform: "..."
```

> **ملاحظة:** التفاصيل الكاملة في `schemas/audio-package.md`.

---

## 11. Risks (المخاطر)

```yaml
risks:
  - id: "RISK-01"
    risk: "..."
    probability: "high"
    impact: "critical"
    mitigation: "..."
    owner: "..."
    status: "mitigated"
  - ...
```

> **ملاحظة:** التفاصيل الكاملة في `schemas/state/risk-register.md`.

---

## 12. Decisions Log (ملخص)

```yaml
decisions:
  - id: "DEC-01"
    decision: "..."
    reason: "..."
  - ...
```

> **ملاحظة:** التفاصيل الكاملة في `schemas/state/decision-log.md`.

---

## 13. Production Notes

```yaml
production_notes:
  total_shots: ...
  total_image_prompts: ...
  total_motion_prompts: ...
  total_audio_layers: ...
  
  estimated_generation_time:
    images: "X hours"
    videos: "X hours"
    audio: "X hours"
    total: "X hours"
  
  recommended_workflow:
    - "ولّد كل الصور أولاً"
    - "راجع، اختر الأفضل"
    - "ثم ولّد الفيديو من الصور المختارة"
    - "..."
  
  critical_warnings:
    - "..."
    - "..."
```

---

## 14. Approvals (الموافقات)

```yaml
approvals:
  concept:
    approved_by: "user"
    date: "..."
    notes: "..."
  
  script:
    approved_by: "user"
    date: "..."
    notes: "..."
  
  final_delivery:
    approved_by: "user"
    date: "..."
    notes: "..."
```

---

## Cross-References

- **Continuity Bible الكامل:** `schemas/state/continuity-bible.md`
- **Frame Chain الكامل:** `schemas/state/frame-chain.md`
- **Asset Registry:** `schemas/state/asset-registry.md`
- **Decision Log:** `schemas/state/decision-log.md`
- **Risk Register:** `schemas/state/risk-register.md`
- **Quality Gates Log:** `schemas/state/quality-gates-log.md`
- **Image Prompts:** `schemas/image-prompts-package.md`
- **Motion Prompts:** `schemas/motion-prompts-package.md`
- **Audio Package:** `schemas/audio-package.md`
- **Assembly Guide:** `schemas/assembly-guide.md`
```

---

## معايير الجودة

- ✅ لا حقول فارغة (N/A مع السبب إذا لم ينطبق)
- ✅ Cross-references تعمل
- ✅ YAML صالح (تحقق منه)
- ✅ Story Spine بـ 7-10 beats
- ✅ Character Arc محدد
- ✅ Camera Grammar شامل
- ✅ Color Palette + Forbidden
- ✅ Risks مسجلة
- ✅ Decisions موثقة

---

## مثال جزئي

```yaml
# Production Blueprint — "صوت الصنعاني"

project:
  title: "صوت الصنعاني"
  type: "Brand Film"
  duration: "45s"
  format:
    primary: "16:9"
    secondary: ["9:16"]
  language: "ar"
  dialect: "يمني صنعاني"
  platform:
    primary: "YouTube"
    secondary: ["Instagram"]

concept:
  logline: "رجل صنعاني متعب يستعيد يقظته من خلال فنجان قهوة تقليدية، فيعيد اكتشاف شغفه."
  one_liner: "القهوة لا تصنع اليقظة. أنت تصنعها."
  visual_metaphor: "البخار = الشرارة الداخلية"
  genre: "درامي حميمي"
  tone: "تأملي، دافئ"
  pace: "بطيء مع تصاعد"

story_structure:
  type: "3-Act Classic"
  total_beats: 8
  
  story_spine:
    - beat: 1
      description: "استيقاظ متعب، صباح رمادي"
    - beat: 2
      description: "النظر في المرآة، رؤية الضبابية"
    - beat: 3
      description: "دخول المطبخ، رؤية الركوة على النار"
    - beat: 4
      description: "السكب في الفنجان، صب دقيق"
    - beat: 5
      description: "أول رشفة، تحول العيون"
    - beat: 6
      description: "الخروج إلى المدينة، العالم يتحرك"
    - beat: 7
      description: "العمل بشغف، عينان يقظتان"
    - beat: 8
      description: "العودة للبيت، ابتسامة"

scenes:
  - id: "SC01"
    title: "الاستيقاظ"
    duration: "6s"
    cumulative_time: "0-6s"
    purpose: "تأسيس الشخصية والحالة المتعبة"
    location_id: "sanaani_coffee_house"
    characters: ["SAMI-01"]
    time_of_day: "قبل الفجر"
    key_beats:
      - "0-2s: وجه نائم، عينان مغمضتان"
      - "2-4s: فتح العينين ببطء"
      - "4-6s: نظرة تعب، تذكر الروتين"
    transition_out: "match_cut"
    transition_reason: "الجفن يُكمل في عين الشخص"
  
  - id: "SC02"
    title: "المرآة"
    duration: "5s"
    cumulative_time: "6-11s"
    purpose: "تأكيد التعب، إدخال المرآة كرمز"
    location_id: "..."
    ...
```

> **مثال كامل:** `examples/energy-drink-ad.md` (سيُنشأ مع v2.0).

---

## ما لا تفعله

- ❌ لا تترك حقول `null` أو `""` — اكتب N/A مع السبب
- ❌ لا تنسَ Cross-references — يجب أن تعمل
- ❌ لا تنسَ YAML validation قبل التسليم
- ❌ لا تُهمل القرارات — كل قرار كبير موثّق
- ❌ لا تُهمل المخاطر — كل خطر مُدار
