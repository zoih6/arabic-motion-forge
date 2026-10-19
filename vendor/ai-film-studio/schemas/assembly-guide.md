# 05 — Assembly Guide (دليل التجميع)

## الهدف

**الملف الخامس والأخير من حزمة الإنتاج الخماسية.** يقدّم **دليلًا خطوة بخطوة** لتجميع كل المخرجات (الصور، الفيديو، الصوت) في **الفيلم النهائي**.

> **يُنتَج من قبل:** `30-executive-producer` (بعد M10، قبل M11).

---

## كيف تستخدمه

1. اتبع الخطوات بالترتيب
2. لا تتخطى خطوة قبل إكمال سابقتها
3. سجّل أي مشاكل في Troubleshooting Log
4. لا تُسلّم الفيلم النهائي قبل التحقق من QA Checklist

---

## القالب الكامل

```markdown
# Assembly Guide — [اسم المشروع]

**التاريخ:** [ISO]
**الحالة:** [DRAFT / IN_ASSEMBLY / COMPLETE]
**المدة النهائية:** [Xs]
**الأداة الأساسية:** [DaVinci Resolve / Adobe Premiere / CapCut Pro]
**الـ Output Formats:** [Master + Platform-specific]

---

## 0. Pre-Assembly Checklist

```yaml
pre_assembly:
  
  inputs_ready:
    - production_blueprint_approved: true
    - image_prompts_generated: true
    - motion_prompts_generated: true
    - audio_package_generated: true
    - continuity_verified: true
    - all_assets_in_dedicated_folders: true
  
  tools_ready:
    - primary_editor_installed: true
    - audio_daw_installed: true
    - after_effects_installed (if needed): true
    - compositing_tool_installed (if needed): true
  
  file_organization:
    project_root/
    ├── 01_assets/
    │   ├── anchors/
    │   ├── main_scenes/
    │   │   ├── images/
    │   │   └── motion/
    │   ├── audio/
    │   │   ├── voice/
    │   │   ├── music/
    │   │   ├── sfx/
    │   │   ├── foley/
    │   │   └── ambience/
    │   └── overlays/
    │       ├── logos/
    │       ├── text/
    │       └── graphics/
    ├── 02_sequences/
    │   ├── rough_cut/
    │   ├── fine_cut/
    │   ├── online/
    │   └── final/
    ├── 03_exports/
    │   ├── master/
    │   ├── youtube/
    │   ├── instagram/
    │   └── tiktok/
    ├── 04_docs/
    │   ├── 01-production-blueprint.md
    │   ├── 02-image-prompts-package.md
    │   ├── 03-motion-prompts-package.md
    │   ├── 04-audio-package.md
    │   └── 05-assembly-guide.md (this file)
    └── 05_logs/
        ├── troubleshooting.log
        └── qa_checklist.log
```

---

## 1. Step 1 — Project Setup (إعداد المشروع)

**المدة:** 5-10 دقائق

```yaml
step_1_project_setup:
  
  actions:
    - action: "أنشئ مشروع جديد بالأبعاد الصحيحة"
      detail: "1920x1080 (16:9) / 1080x1920 (9:16) / 1080x1080 (1:1)"
      tool: "Premiere Pro → New Project → Settings"
    
    - action: "اضبط الـ Sequence Settings"
      detail: |
        - Frame size: 1920x1080 (or as needed)
        - Frame rate: 24fps (cinematic) / 30fps (web) / 25fps (PAL)
        - Audio: 48kHz, 24-bit, Stereo
        - Color space: Rec. 709 (web) / Rec. 2020 (HDR)
        - Renderer: Mercury Playback Engine (GPU)
    
    - action: "أنشئ الفولدر التنظيمي (انظر أعلاه)"
      detail: "..."
    
    - action: "استورد كل الفيديوهات"
      detail: "من assets/main_scenes/motion/"
    
    - action: "استورد كل الطبقات الصوتية"
      detail: "من assets/audio/"
    
    - action: "استورد كل الـ Overlays (نصوص، شعارات)"
      detail: "من assets/overlays/"
  
  verification:
    - "كل الملفات في مكانها"
    - "الفيديوهات تلعب بدون تقطيع"
    - "الصوت يعمل"
```

---

## 2. Step 2 — Rough Cut (القص الأولي)

**المدة:** 15-20 دقيقة

```yaml
step_2_rough_cut:
  
  actions:
    - action: "رتّب كل اللقطات في Timeline حسب Scene Order"
      detail: "SC01 → SC02 → SC03 → SC04 → SC05 → SC06"
      reference: "01-production-blueprint.md → section 5"
    
    - action: "قص كل لقطة لإزالة البداية/النهاية غير الضرورية"
      detail: "استخدم Shot Card 'edit_handles' كمرجع"
      tool: "Blade tool (B) / Razor tool"
    
    - action: "طبّق الانتقالات الأساسية"
      detail: "من transition_map في 01-production-blueprint.md"
      common_transitions:
        - "hard_cut: 60% من الحالات"
        - "dissolve: 20% (للتأملية)"
        - "match_cut: 15% (للذكية)"
        - "fade: 5% (للنهايات)"
      tool: "Effects panel → Video Transitions"
    
    - action: "تأكد من الإيقاع"
      detail: "كل shot = المدة المحددة في Shot Card"
      warning: "إذا شعرت بالملل → قصر، إذا شعرت بالاستعجال → أطل"
  
  rough_cut_output:
    duration: "Xs (target)"
    file_path: "02_sequences/rough_cut/v1.prproj"
    notes: "..."
```

---

## 3. Step 3 — Audio Mix (مزج الصوت)

**المدة:** 20-30 دقيقة

```yaml
step_3_audio_mix:
  
  actions:
    
    - action: "أنشئ Audio Tracks (طبقات صوتية)"
      detail: |
        Track 1: VO (voiceover)
        Track 2: Dialogue
        Track 3: Music
        Track 4: SFX
        Track 5: Foley
        Track 6: Ambience
        Track 7: Master
      tool: "Audio Track Mixer"
    
    - action: "ضع كل الطبقات في الـ track المناسب"
      detail: "..."
    
    - action: "زامن VO/Dialogue مع الفيديو"
      detail: "..."
      warning: "أي تأخير > 0.5s = أعد التسجيل أو قص الفيديو"
    
    - action: "اضبط مستويات الصوت (Volumes)"
      detail: "حسب mixing_plan في 04-audio-package.md"
      levels:
        dialogue: -3 dB
        voiceover: -3 dB
        music: -12 dB
        sfx: -10 dB (variable)
        foley: -15 dB
        ambience: -22 dB
    
    - action: "أضف Ducking (الموسيقى تنخفض تحت الصوت البشري)"
      detail: |
        - Music track: side-chain from VO track
        - Duck amount: -6dB
        - Attack: 200ms, Release: 500ms
      tool: "Side-chain compression (in DAW) / Volume keyframes"
    
    - action: "أضف EQ لكل track"
      detail: "حسب eq_zones في 04-audio-package.md"
    
    - action: "أضف Reverb حيث يلزم"
      detail: "..."
    
    - action: "اختبر المزيج: استمع كاملاً"
      detail: "..."
  
  audio_mix_output:
    file_path: "02_sequences/audio_mix/v1.wav"
    duration: "Xs"
    notes: "..."
```

---

## 4. Step 4 — Text & Graphics (النصوص والجرافيكس)

**المدة:** 15-20 دقيقة

```yaml
step_4_text_graphics:
  
  actions:
    
    - action: "أضف On-Screen Text (النصوص على الشاشة)"
      detail: "حسب on_screen_text في script section"
      for_each_text:
        - "أضف Text Layer"
        - "Font: من typography_plan"
        - "Color: من typography_plan"
        - "Size: من typography_plan"
        - "Position: title-safe area"
        - "Animation: fade in/out (simple)"
        - "Duration: حسب script"
      tool: "Essential Graphics panel (Premiere) / Text+ (DaVinci)"
    
    - action: "أضف Brand Logo (الشعار)"
      detail: "post_overlay strategy"
      steps:
        - "استورد logo PNG (transparent background)"
        - "أضفه في الـ overlay track"
        - "Position: top-right or center (حسب design)"
        - "Animation: fade in"
        - "Duration: 3-5s in the end (CTA)"
    
    - action: "أضف Lower Thirds (إن وُجدت)"
      detail: "..."
    
    - action: "أضف Credits (إن وُجدت)"
      detail: "..."
  
  text_graphics_output:
    file_path: "02_sequences/with_graphics/v1.prproj"
    notes: "..."
```

---

## 5. Step 5 — Color Grading (تصحيح الألوان)

**المدة:** 15-20 دقيقة

```yaml
step_5_color_grading:
  
  actions:
    
    - action: "طبق Color Grade أساسي (Look up Table / LUT)"
      detail: |
        - إذا كنت تستخدم LUT: اختر LUT سينمائي دافئ
        - إذا كنت تعدّل يدويًا: اتبع color_palette في Production Blueprint
      tool: "Lumetri Color (Premiere) / Color page (DaVinci)"
    
    - action: "تأكد من اتساق الألوان بين اللقطات"
      detail: |
        - قارن اللقطة 1 مع اللقطة 5 (نفس الشخصية)
        - قارن اللقطة 3 مع اللقطة 7 (نفس المكان)
        - إذا اختلاف: عدّل الثانية لتطابق الأولى
      tool: "Comparison View"
    
    - action: "حقق Color Script Map"
      detail: "حسب color_script في Production Blueprint"
      example:
        "SC01": "warm_amber + deep_teal"
        "SC04": "warm_amber burst (الذروة)"
    
    - action: "حقق Skin Tones"
      detail: "Brow Tone Checker / Skin Tone Indicator"
      tool: "Lumetri Color → Vectorscope"
    
    - action: "اضبط لكل منصة"
      detail: |
        - YouTube: أكثر سطوعًا قليلًا
        - Instagram: saturation أعلى
        - Cinema: contrast أعلى
    
    - action: "Final Color Pass"
      detail: "..."
  
  color_grade_output:
    file_path: "02_sequences/color/v1.prproj"
    notes: "..."
```

---

## 6. Step 6 — Effects & Polish (المؤثرات واللمسات)

**المدة:** 10-15 دقيقة

```yaml
step_6_effects_polish:
  
  actions:
    
    - action: "أضف أي Post-Effects موثقة في Production Blueprint"
      detail: "..."
      common_effects:
        - "Light leak: 2-3% opacity, very subtle"
        - "Film grain: 35mm grain overlay, subtle"
        - "Vignette: subtle, 10-15% opacity"
        - "Halation: around highlights (cinematic look)"
      tool: "Adjustment layers + blending modes"
    
    - action: "أضف Title Cards (بطاقات العنوان) إن وُجدت"
      detail: "..."
    
    - action: "أضف Final Brand Sting (النغمة الأخيرة للشعار)"
      detail: "..."
    
    - action: "أضف أي Animated Graphics"
      detail: "lower thirds animated, countdowns, etc."
    
    - action: "Final Polish: مراجعة شاملة"
      detail: |
        - هل كل شيء متماسك؟
        - هل النصائح من Continuity Bible محققة؟
        - هل هناك أي "flicker" أو "stutter"؟
```

---

## 7. Step 7 — Export (التصدير)

**المدة:** 10-15 دقيقة

```yaml
step_7_export:
  
  exports:
    
    - name: "Master (للأرشيف)"
      format: "ProRes 422 HQ / DNxHR HQX"
      codec: "ProRes 422 HQ"
      resolution: "1920x1080"
      fps: "24"
      audio: "48kHz 24bit, master mix"
      file_path: "03_exports/master/v1_master.mov"
      use: "أرشيف، تعديل مستقبلي"
    
    - name: "YouTube"
      format: "H.264 (MP4)"
      codec: "H.264 High Profile"
      resolution: "1920x1080 (or 4K if available)"
      fps: "24 (or 30)"
      bitrate: "20-50 Mbps (VBR 2-pass)"
      audio: "AAC 320kbps, -14 LUFS"
      file_path: "03_exports/youtube/v1_youtube.mp4"
      use: "YouTube"
    
    - name: "Instagram Feed"
      format: "H.264 (MP4)"
      codec: "H.264"
      resolution: "1080x1350 (4:5) or 1080x1080 (1:1)"
      bitrate: "8-12 Mbps"
      audio: "AAC 256kbps, -16 LUFS"
      file_path: "03_exports/instagram/v1_instagram.mp4"
      notes: "إذا الفيديو الأصلي 16:9، أعد تصديره بـ 4:5 (crop) أو 1:1"
    
    - name: "TikTok"
      format: "H.264 (MP4)"
      codec: "H.264"
      resolution: "1080x1920 (9:16)"
      bitrate: "10-15 Mbps"
      audio: "AAC 256kbps, -14 LUFS"
      file_path: "03_exports/tiktok/v1_tiktok.mp4"
      notes: "إذا الفيديو الأصلي 16:9، أعد تصديره بـ 9:16"
    
    - name: "Twitter/X"
      format: "H.264 (MP4)"
      resolution: "1920x1080 (16:9)"
      bitrate: "10 Mbps"
      audio: "AAC 256kbps"
      file_path: "03_exports/twitter/v1_twitter.mp4"
  
  export_settings_summary:
    - "Render at maximum quality"
    - "Use VBR 2-pass if available"
    - "Maximum bitrate for platform"
    - "Audio: per platform LUFS"
```

---

## 8. Final QA Checklist (قائمة التحقق النهائية)

**المدة:** 10-15 دقيقة

```yaml
qa_checklist:
  
  visual:
    - "كل اللقطات بالترتيب الصحيح"
    - "لا توجد لقطات مفقودة"
    - "الانتقالات مطبقة بشكل صحيح"
    - "النصائح من Continuity Bible محققة (نفس الشخصية، الملابس، المكان)"
    - "الإضاءة متسقة عبر المشاهد"
    - "Color grade متسق"
    - "النصائح من Frame Chain محققة (لا كسور غير مبررة)"
    - "الشعارات والنصوص مقروءة 100%"
    - "لا flickering أو stuttering"
    - "نسبة العرض إلى الارتفاع صحيحة للمنصة"
  
  audio:
    - "كل الطبقات الصوتية موجودة"
    - "الـ VO/Dialogue متزامن مع الفيديو"
    - "الموسيقى ducked تحت الصوت البشري"
    - "المستويات ضمن mixing_plan"
    - "Master LUFS ضمن target"
    - "لا clipping"
    - "لا أصوات غير مرغوبة (background noise)"
  
  technical:
    - "Export settings صحيحة للمنصة"
    - "Resolution صحيحة"
    - "FPS صحيح"
    - "Audio codec صحيح"
    - "Bitrate كافٍ"
    - "File size معقول (ليس صغيرًا جدًا أو ضخمًا)"
  
  narrative:
    - "القصة مفهومة"
    - "الشخصية تتطور"
    - "الرسالة واضحة"
    - "الإيقاع مناسب"
    - "البداية تجذب (first 3s)"
    - "النهاية مُرضية"
    - "لا يوجد لحظات ميتة (dead air)"
  
  brand:
    - "الشعار يظهر كما هو"
    - "الألوان متطابقة مع Brand Guidelines"
    - "النبرة مناسبة"
    - "CTA واضحة (إن وُجدت)"
  
  final_questions:
    - "هل أنجز المشروع الهدف المحدد؟"
    - "هل يخدم الجمهور المستهدف؟"
    - "هل يستحق النشر؟"
```

---

## 9. Troubleshooting (حل المشاكل)

```yaml
troubleshooting:
  
  - issue: "اللون بين اللقطات مختلف"
    cause: "Color grade غير متسق"
    fix: "استخدم Color Match tool، أو طبّق نفس الـ LUT على كل اللقطات"
  
  - issue: "الصوت متأخر عن الصورة (lip-sync off)"
    cause: "Rendering latency أو audio sample rate خاطئ"
    fix: "تأكد من 48kHz audio، أعد sync يدويًا، أو أعد التسجيل"
  
  - issue: "النص مشوه في الفيديو المُولَّد"
    cause: "video model شوّه النص"
    fix: "احذف النص من الفيديو، أضفه كـ overlay في post"
  
  - issue: "الموسيقى تطغى على الصوت البشري"
    cause: "Ducking ضعيف أو غير مطبق"
    fix: "زِد ducking إلى -8dB أو -10dB، تحقق من side-chain"
  
  - issue: "حركة الشخصية متقطعة (stuttering)"
    cause: "fps غير متطابق بين shots"
    fix: "تأكد من نفس الـ fps في كل اللقطات، أعد export من المصدر"
  
  - issue: "الشخصية تبدو مختلفة بين shots"
    cause: "Character anchor لم يُستخدم بشكل صحيح"
    fix: "أعد توليد الـ shots بدون anchor، أضف anchor image في الـ reference"
  
  - issue: "الفيديو طويل جدًا (over duration target)"
    cause: "Transitions أطول من اللازم"
    fix: "قصّر الـ transitions إلى 0.5s (أو hard cut)"
  
  - issue: "الفيديو قصير جدًا (under duration target)"
    cause: "shots أقصر من المخطط"
    fix: "أطل بعض اللقطات بإضافة hold frames في البداية/النهاية"
  
  - issue: "الـ Master LUFS خارج target"
    cause: "Mixing levels غير صحيحة"
    fix: "أعد master مع limiter، تحقق بـ LUFS meter"
  
  - issue: "Black bars (letterbox) غير مرغوبة للمنصة"
    cause: "Aspect ratio خاطئ"
    fix: "غيّر export إلى ratio المنصة (9:16, 1:1, 4:5)"
```

---

## 10. Delivery Checklist (التسليم النهائي)

```yaml
delivery:
  
  files_to_deliver:
    - "03_exports/youtube/v1_youtube.mp4"
    - "03_exports/instagram/v1_instagram.mp4"
    - "03_exports/tiktok/v1_tiktok.mp4"
    - "03_exports/twitter/v1_twitter.mp4"
    - "03_exports/master/v1_master.mov"
    - "04_docs/01-production-blueprint.md (final)"
    - "04_docs/02-image-prompts-package.md (final)"
    - "04_docs/03-motion-prompts-package.md (final)"
    - "04_docs/04-audio-package.md (final)"
    - "04_docs/05-assembly-guide.md (final, this file)"
  
  thumbnails:
    - "أنشئ 3 thumbnails (YouTube)"
    - "أنشئ 1 cover (Instagram)"
    - "أنشئ 1 cover (TikTok)"
  
  captions_subtitles:
    - "أنشئ SRT/VTT (auto-generated من VO، ثم راجع)"
    - "Export for each platform"
  
  metadata:
    - title: "..."
    - description: "..."
    - tags: "..."
    - hashtags: "..."
    - thumbnail: "..."
    - category: "..."
  
  delivery_to_user:
    - "شارك رابط المشروع (Google Drive / Dropbox)"
    - "وثّق في final delivery message"
    - "اطلب feedback"
```

---

## 11. Post-Delivery (بعد التسليم)

```yaml
post_delivery:
  
  monitoring:
    - "تابع المشاهدات والتفاعل"
    - "اجمع feedback"
    - "سجّل الملاحظات للتحسين المستقبلي"
  
  iteration:
    - "إذا كان هناك v2: استخدم هذا الـ Assembly Guide كأساس"
    - "وثّق ما تغيّر في CHANGELOG"
    - "حدّث Continuity Bible إن تغيّرت شخصيات/أماكن"
  
  archival:
    - "احفظ كل الملفات في archive"
    - "احتفظ بـ decision log و risk register"
    - "لا تحذف assets حتى لو انتهى المشروع"
```

---

## Cross-References

- **Production Blueprint:** `schemas/production-blueprint.md`
- **Image Prompts Package:** `schemas/image-prompts-package.md`
- **Motion Prompts Package:** `schemas/motion-prompts-package.md`
- **Audio Package:** `schemas/audio-package.md`
- **Continuity Bible:** `schemas/state/continuity-bible.md`
- **Frame Chain:** `schemas/state/frame-chain.md`
- **Decision Log:** `schemas/state/decision-log.md`
- **Risk Register:** `schemas/state/risk-register.md`
```

---

## معايير الجودة

- ✅ كل خطوة موثّقة بتفاصيل كافية للتنفيذ
- ✅ Troubleshooting Log يغطي المشاكل الشائعة
- ✅ QA Checklist شامل (visual + audio + technical + narrative + brand)
- ✅ Export Settings محددة لكل منصة
- ✅ Cross-references تعمل

---

## ما لا تفعله

- ❌ لا تتخطى خطوة قبل إكمال سابقتها
- ❌ لا تنسَ QA Checklist
- ❌ لا تنسَ troubleshooting
- ❌ لا تنسَ platform-specific exports
- ❌ لا تنسَ captions/subtitles
- ❌ لا تحذف الملفات بعد التسليم
