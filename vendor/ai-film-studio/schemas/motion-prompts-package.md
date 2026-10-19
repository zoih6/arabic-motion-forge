# 03 — Motion Prompts Package (حزمة برومبتات الفيديو)

## الهدف

**الملف الثالث من حزمة الإنتاج الخماسية.** يحوي **كل prompt فيديو** جاهز للتوليد، مع ربط كل prompt بـ Image Source، Start/End Frame، Motion Strategy، ومحاولات التوليد.

> **يُنتَج من قبل:** `30-executive-producer` (مع `22-prompt-architecture` و `28-text-preservation-motion`).

---

## كيف تستخدمه

1. املأ كل prompt عند M9
2. كل prompt يجب أن يكون مرتبط بـ Image Source (من `schemas/image-prompts-package.md`)
3. مرّر كل prompt عبر `19-preflight-check` ثم `31-quality-gate` (G4)
4. سجّل محاولات التوليد في `generated_assets`

---

## القالب الكامل

```markdown
# Motion Prompts Package — [اسم المشروع]

**التاريخ:** [ISO]
**الحالة:** [DRAFT / APPROVED_FOR_GENERATION / GENERATED / APPROVED]
**عدد الـ Prompts:** [N]
**النماذج المستهدفة:** [bytedance/seedance-2.0, runwayml/gen4, ...]

---

## 0. Generation Strategy

```yaml
strategy:
  primary_model: "bytedance/seedance-2.0"
  fallback_models:
    - "runwayml/gen4"
    - "veo-3 (with audio)"
    - "kling-2.1"
  input_mode: "image_to_video / text_to_video"
  aspect_ratio: "16:9 / 9:16 / 1:1"
  resolution: "1920x1080 / 4K"
  duration_per_shot: "5-10s (avg)"
  expected_attempts_per_prompt: 3
  selection_criteria: "حركة سلسة + تطابق start/end + continuity match"
  
  workflow:
    1: "اختر الصورة المعتمدة من 02-image-prompts-package.md"
    2: "ولّد فيديو i2v مع prompt مفصل"
    3: "راجع: هل التطابق مع end_frame جيد؟"
    4: "إذا لا: أعد بـ prompt أقوى أو model آخر"
    5: "اختر الأفضل"
```

---

## 1. Anchors (مرجعيات الحركة)

### MOT-CHAR-01 — SAMI-01 Walk Cycle

```yaml
prompt_id: "MOT-CHAR-01"
type: "motion_anchor"
purpose: "تثبيت حركة المشي للشخصية"

input_image: "assets/main/sc01_sh02_v2.png"

motion_layers: |
  SAMI-01 walks slowly from left to right across the
  coffee house floor. Three deliberate steps, each step
  deliberate, slow, slightly heavy (showing fatigue).
  His right hand trails gently near his side. His gaze
  is downcast, looking at the floor. The brass dallah
  on the coals in the background continues to steam
  (steam rises slowly). Dust motes drift in the window
  light (very slow movement). His apron sways gently
  with each step. His shoulders are slightly slumped.
  
  Camera: static, locked, no motion.
  Duration: 8 seconds.

model: "bytedance/seedance-2.0"
duration: "8s"
```

### MOT-PROP-01 — Dallah Steam

```yaml
prompt_id: "MOT-PROP-01"
type: "motion_anchor"
purpose: "تثبيت حركة بخار الركوة"

input_image: "assets/anchors/prop-01_v1.png"

motion_layers: |
  Subtle steam rises slowly from the brass dallah on hot
  coals. The steam is wispy, organic, follows natural
  convection (rises, then drifts slightly to the right).
  The coals glow slightly brighter then dimmer (subtle
  pulse). The brass surface of the dallah reflects the
  warm glow from the coals.
  
  Camera: static, slight slow push in over 6 seconds.

model: "bytedance/seedance-2.0"
duration: "6s"
```

---

## 2. Main Scene Prompts (لقطات المشاهد)

### MOT-SC01-SH01

```yaml
prompt_id: "MOT-SC01-SH01"
shot_id: "SC01_SH01"
type: "main_scene"
input_image: "assets/main/sc01_sh01_v2.png"
duration: "8s"
purpose: "اللقطة الافتتاحية: تأسيس العالم (لا شخصية، مع حركة بسيطة)"

full_prompt_motion: |
  Cinematic film still with subtle motion. The frame is
  identical to the input image (empty Sanaani coffee
  house, pre-dawn). Subtle, slow movements only:
  
  - Faint steam rises slowly from the brass dallah on
    the hot coals in the background (wispy, organic,
    rises 30cm then drifts right slightly)
  - Dust motes drift slowly through the window light
    beam (very slow, almost imperceptible)
  - The coals under the dallah pulse subtly (slight
    brightening/dimming, 1 cycle over 4 seconds)
  - The brass lamp hanging from the ceiling sways
    imperceptibly (1cm total over 8s)
  
  Camera: static, locked, no motion whatsoever.
  No character appears. No action. The frame is
  contemplative, waiting.
  
  The composition, lighting, and color remain exactly
  as in the input image. The window light remains cool
  blue 8000K. The atmosphere remains still and
  pre-dawn.

model:
  primary: "bytedance/seedance-2.0"
  fallback: "runwayml/gen4"
  aspect_ratio: "16:9"
  duration: "8s"

start_frame: |
  [Description matching input image, more details]
  Empty coffee house, low light, dallah on coals in
  background, window light from upper left, dust motes
  visible in light beam.

end_frame: |
  [Description matching start_frame + slight steam
  movement + slightly more visible dust drift]
  Same composition, same lighting, but the steam from
  the dallah has risen further, and the dust motes have
  shifted position slightly. The image is otherwise
  almost identical to the start frame (intentional —
  this is a contemplative establishing shot).

lipsync:
  required: false
  text: "N/A"

text_preservation:
  required: false
  text: "N/A"
  strategy: "N/A"

acceptance_criteria:
  - "اللقطة تبدأ = input image (نفس التكوين)"
  - "حركة البخار طبيعية (organic, not mechanical)"
  - "الإضاءة ثابتة (لا تتغير)"
  - "الركوة في نفس الموقع"
  - "لا شخصية تظهر"
  - "الـ Camera ثابتة"
  - "Frame يبقى contemplative"

rejection_criteria:
  - "حركة كاميرا"
  - "شخصية تظهر فجأة"
  - "إضاءة تتغير"
  - "البخار ينفجر بشكل غير طبيعي"
  - "تغير تكوين الكادر"

expected_attempts: 3
fallback_strategy:
  if_3_attempts_fail:
    - "ولّد prompt أبسط: 'subtle steam, no other motion'"
    - "جرّب model مختلف"
    - "إذا فشل: استخدم static image (no motion)"

generated_assets:
  - path: "assets/motion/sc01_sh01_v1.mp4"
    attempt: 1
    status: "rejected"
    reason: "حركة كاميرا زائدة"
  - path: "assets/motion/sc01_sh01_v2.mp4"
    attempt: 2
    status: "approved"
    notes: "تطابق ممتاز، البخار طبيعي"
```

### MOT-SC01-SH02

```yaml
prompt_id: "MOT-SC01-SH02"
shot_id: "SC01_SH02"
type: "main_scene"
input_image: "assets/main/sc01_sh02_v2.png"
duration: "6s"
purpose: "دخول الشخصية: SAMI-01 يدخل من اليسار ويمشي نحو الطاولة"

full_prompt_motion: |
  Cinematic film motion. The frame begins as the input
  image (SAMI-01 just entering from the left, hands at
  sides, expression tired).
  
  Motion:
  - SAMI-01 walks slowly from left to right across the
    coffee house floor toward the counter
  - Three deliberate steps, each step slow, slightly
    heavy (showing fatigue)
  - His gaze is downcast, looking at the floor then
    gradually lifts toward the brass dallah on the coals
  - His right hand trails near his side, then lifts
    slightly as he approaches the counter
  - His apron sways gently with each step (fabric
    physics)
  - His shoulders are slightly slumped (fatigue
    posture)
  - Brass dallah continues to steam (consistent with
    previous shot)
  - Dust motes drift slowly in window light
  
  Camera: static, locked, no motion.
  
  Continuity: This shot continues from MOT-SC01-SH01
  (same location, same lighting, time progresses 1-2
  seconds). SAMI-01's appearance must EXACTLY match
  IMG-CHAR-01 (face, beard with gray patch on left
  cheek, burn scar on right hand, charcoal apron,
  off-white shirt, weathered brown leather watch on
  left wrist).
  
  End state: SAMI-01 standing at the counter, looking
  down at the brass dallah, hands near the counter
  edge (this is the start of the next shot).

model:
  primary: "bytedance/seedance-2.0"
  fallback: "runwayml/gen4"
  aspect_ratio: "16:9"
  duration: "6s"

start_frame:
  matches: "input image (sc01_sh02_v2.png)"
  description: "SAMI-01 mid-stride, just entered frame, head slightly turned, looking down"

end_frame:
  matches: "start of MOT-SC01-SH03"
  description: "SAMI-01 at counter, both hands on counter edge, looking down at dallah, calm"

lipsync:
  required: false
  text: "N/A"

text_preservation:
  required: false
  text: "N/A"

acceptance_criteria:
  - "الشخصية تطابق IMG-CHAR-01 (الوجه، البقعة الرمادية، الندبة)"
  - "الملابس تطابق IMG-WARD-01 (المئزر، القميص، الساعة)"
  - "3 خطوات واضحة"
  - "الإيقاع بطيء (تعب)"
  - "اليد اليمنى تظهر الندبة عند المرور"
  - "نفس الإضاءة (pre-dawn)"
  - "البخار يستمر"
  - "Frame يبدأ = input image"
  - "Frame ينتهي = hands on counter, looking down"

rejection_criteria:
  - "تغير ملامح الوجه"
  - "اختفاء البقعة الرمادية"
  - "اختفاء الندبة"
  - "ملابس مختلفة"
  - "خطوات سريعة (إيقاع خاطئ)"
  - "حركة كاميرا"
  - "إضاءة تتغير"

expected_attempts: 4
fallback_strategy:
  if_3_attempts_fail:
    - "قسّم لقطتين: دخول + مشي"
    - "ولّد بدون حركة شخصية، أضف الشخصية في post (compositing)"
    - "آخر حل: static image (no motion)"

generated_assets:
  - path: "assets/motion/sc01_sh02_v1.mp4"
    attempt: 1
    status: "rejected"
    reason: "الوجه تغيّر بين البداية والنهاية"
  - path: "assets/motion/sc01_sh02_v2.mp4"
    attempt: 2
    status: "rejected"
    reason: "الإيقاع سريع جدًا"
  - path: "assets/motion/sc01_sh02_v3.mp4"
    attempt: 3
    status: "approved"
    notes: "ممتاز، الشخصية ثابتة، الإيقاع صحيح"
```

### MOT-SC01-SH03

```yaml
prompt_id: "MOT-SC01-SH03"
shot_id: "SC01_SH03"
type: "main_scene"
input_image: "assets/main/sc01_sh03_v2.png"
duration: "5s"
purpose: "الشخصية تمسك الركوة"

full_prompt_motion: |
  [Prompt مفصل بـ 10 طبقات، مع Motion مفصّل]
  
  Motion:
  - SAMI-01 reaches with his right hand toward the
    brass dallah
  - His hand grasps the curved handle of the dallah
  - He lifts the dallah slowly (1.5 seconds)
  - He tilts the dallah toward the brass cup
  - He begins to pour coffee (start of pour, end of
    shot is mid-pour)
  - Coffee stream is dark brown, smooth
  - Steam rises from the pouring coffee
  
  Camera: slight slow dolly in (1cm/second)
  
  Continuity: Must match SC01_SH02 end state
  (SAMI-01 at counter, hands on counter, looking at
  dallah). This shot begins with him reaching and
  ends with him mid-pour.

[باقي الحقول بنفس النمط]
```

### MOT-SC01-SH04..N

[نفس النمط لكل لقطة]

---

## 3. Lip-Sync Scenes (إن وُجدت)

```yaml
lipsync_scenes:
  - scene_id: "SC03"
    shot_id: "SC03_SH02"
    type: "dialogue_with_lipsync"
    input_image: "assets/main/sc03_sh02_v2.png"
    duration: "4s"
    text: "نعم. هذا ما كنت أحتاجه."
    text_translation: "Yes. This is what I needed."
    speaker: "SAMI-01"
    direction: "نحو الكاميرا، ابتسامة خفيفة، صوت واثق"
    
    strategy: "regenerate_with_audio (Hedra)"
    
    motion_layers: |
      SAMI-01 looks at the camera, smiles subtly,
      speaks: "Yes. This is what I needed." The
      speech is slow, deliberate, confident. His
      lips move in sync with the audio.
    
    audio:
      model: "ElevenLabs"
      voice_id: "SAMI-01-voice-clone"
      text: "نعم. هذا ما كنت أحتاجه."
      language: "ar"
      delivery: "confident, soft, warm"
      processing: "Adobe Podcast enhance"
    
    model: "hedra / veo-3 (with audio)"
    
    acceptance_criteria:
      - "شفاه متحركة (ليست ثابتة)"
      - "التزامن صحيح"
      - "الصوت واضح"
      - "نفس الشخصية من IMG-CHAR-01"
    
    expected_attempts: 5
    fallback:
      - "vo_only: video بدون حوار، أضف VO في post"
      - "subtitle_overlay: اكتب النص على الشاشة"
```

---

## 4. Inventory (جرد الـ Motion Prompts)

```yaml
inventory:
  motion_anchors:
    - MOT-CHAR-01
    - MOT-PROP-01
  
  main_scenes:
    SC01:
      - MOT-SC01-SH01
      - MOT-SC01-SH02
      - MOT-SC01-SH03
      - MOT-SC01-SH04
    SC02:
      - MOT-SC02-SH01
      - ...
    ...
  
  lipsync_scenes:
    - SC03_SH02
    - ...
  
  total_prompts: N
  total_duration: "Xs"
  expected_total_assets: "3-5x (attempts per prompt)"
```

---

## 5. Continuity Verification (تأكيد الاستمرارية)

```yaml
continuity_verification:
  per_scene:
    SC01:
      shots:
        - MOT-SC01-SH01
          start_matches: "input image"
          end_matches: "MOT-SC01-SH02 start"
        - MOT-SC01-SH02
          start_matches: "MOT-SC01-SH01 end"
          end_matches: "MOT-SC01-SH03 start"
        - ...
      chain_breaks: 0
      status: "complete"
    ...
  
  final_check:
    all_continuity_matched: true
    issues: []
    action: "ready for assembly"
```

---

## 6. Generation Workflow

```yaml
workflow:
  step_1_select_images:
    duration_minutes: 10
    description: "من 02-image-prompts-package، اختر الصورة المعتمدة لكل shot"
  
  step_2_generate_anchors:
    duration_minutes: 30
    description: "ولّد motion anchors (character walk, prop steam)"
  
  step_3_generate_main_scenes:
    duration_minutes: 60-180
    description: "ولّد كل shot بالترتيب، ابدأ بـ SC01"
    notes: "تأكد من مطابقة end_frame مع start_frame التالي"
  
  step_4_continuity_check:
    duration_minutes: 30
    description: "افحص الاستمرارية: end → start بين كل shots"
    action: "إذا كسر → أعد التوليد"
  
  step_5_generate_lipsync:
    duration_minutes: 30
    description: "ولّد المشاهد التي تحتاج lip-sync (إن وُجدت)"
    notes: "استخدم Hedra أو Veo 3"
  
  step_6_final_review:
    duration_minutes: 20
    description: "راجع كل الفيديوهات، اختر النسخة النهائية"
  
  step_7_export:
    duration_minutes: 10
    description: "صدّر بصيغ متعددة (MP4 max + web versions)"
```

---

## Cross-References

- **Production Blueprint:** `schemas/production-blueprint.md`
- **Image Prompts Package:** `schemas/image-prompts-package.md` (مصدر الصور)
- **Continuity Bible:** `schemas/state/continuity-bible.md`
- **Frame Chain:** `schemas/state/frame-chain.md`
- **Asset Registry:** `schemas/state/asset-registry.md`
- **Audio Package:** `schemas/audio-package.md` (للـ VO + lip-sync)
- **Assembly Guide:** `schemas/assembly-guide.md`
```

---

## معايير الجودة

- ✅ كل prompt يحوي Motion layer مفصّلة
- ✅ Input Image مذكور دائمًا
- ✅ Start/End Frame متطابقان
- ✅ Reference Models محددة
- ✅ Lip-Sync Strategy واضحة (إن وُجد)
- ✅ Continuity verified
- ✅ Fallback Strategy لكل prompt

---

## ما لا تفعله

- ❌ لا prompt بدون Input Image
- ❌ لا تترك Start/End Frame فارغين
- ❌ لا تنسَ التحقق من Continuity
- ❌ لا تُهمل Fallback Strategy
- ❌ لا تسلّم بدون Final Selection لكل prompt
- ❌ لا تنسَ تسجيل المحاولات
