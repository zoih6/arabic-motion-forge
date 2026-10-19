---
name: intent-router
description: |
  يحوّل طلب المستخدم إلى **أصغر مسار إنتاجي كافٍ**. النقطة الأولى بعد قراءة SKILL.md.
  لا تشغّل M0–M11 إلا إذا كان المشروع كاملاً.
tier: 2
when_to_load: "دائمًا عند بداية أي مشروع جديد"
---

# Intent Router — AI Film Studio v2.0

> **قاعدة ورقة الإنتاج:** في كل طلب فيديو، أنشئ `workflows/adaptive-production-sheet.md` و`schemas/production-sheet.md` بعد الـBrief وقبل الـStoryboard/Prompts. الشيت ليس مرحلة M جديدة؛ هو عقد تخطيط متكيف مع نوع الطلب ومدته وقابل للتصدير CSV.

## الغرض

حوّل طلب المستخدم إلى **أصغر مسار إنتاجي كافٍ** بدل تشغيل M0–M11 دائمًا.

## عقد التوجيه (Routing Contract)

قبل أي تنفيذ، استخرج داخليًا:

| الحقل | الوصف |
|---|---|
| `intent` | ما الذي يريد المستخدم الحصول عليه الآن؟ |
| `scope` | مفرد / لقطة / مشهد / مشروع كامل |
| `inputs` | صور، فيديو، صوت، نص، مراجع، ملفات |
| `state` | مشروع جديد أم استمرار لمشروع قائم |
| `output` | prompt / plan / assets / production package / repair |
| `constraints` | مدة، نسبة، منصة، نموذج، هوية، لغة، نص حرفي |

## شجرة القرار (Priority)

طبّق القواعد بالترتيب:

```
1. طلب إصلاح واضح (لقطة مكسورة، نص مشوّه)
   → REPAIR: شخّص → أصلح الوكيل المتضرر → أعد الفحص
   
2. طلب تحريك صورة/فريم موجود
   → IMAGE_TO_VIDEO: workflows/shortcuts/image-to-video.md
   
3. طلب صورة/فريم ثابت
   → IMAGE_GENERATION: workflows/shortcuts/image-generation.md
   
4. طلب موشن جرافيك/kinetic typography
   → MOTION_GRAPHICS: workflows/shortcuts/motion-graphics.md
   
5. طلب حوار/لِبسِنك
   → DIALOGUE_LIPSYNC: workflows/shortcuts/dialogue-lipsync.md
   
6. طلب لقطة واحدة من مشروع قائم
   → SHOT_BUILD: workflows/M3a-shot-design.md → M8a-motion-prompts.md (يشمل M4c QC)
    
7. طلب مشهد متعدد اللقطات
   → SCENE_BUILD: workflows/M0-intake.md → **M4e-reference-orchestration.md (مراجع إلزامية)** → M3a → M4a → **M4c (QC إلزامي)** → M9c
   → الرجوع لـ `references/protocols/orchestration-runtime.md` للترتيب الكامل
    
8. طلب فيلم/إعلان متعدد المشاهد
   → FULL_PRODUCTION: workflows/M0-intake.md → **M4e-reference-orchestration.md (مراجع إلزامية)** → M11
   → كل المراحل M0–M11 + **M4c إلزامي** + G-APPROVAL × 3

9. طلب "اكتب برومبت" دون نطاق واضح
   → PROMPT_ONLY: workflows/shortcuts/single-prompt.md

10. طلب فكرة فقط / concept
    → CONCEPT: workflows/shortcuts/concept-only.md
```

## المحركات (Engines) — v3.0.0

المحركات **طبقة تنظيم وتسليم** فوق M0–M11، لكل منها عقد تشغيل خاص.
اختر المحرك أولًا إن كان الطلب يطابقه، ثم نفّذ مساره داخليًا.

| المسار | المحرك | متى | M4c QC |
|---|---|---|---|
| **VOX_DOCUMENTARY** | `workflows/engines/E1-documentary-engine.md` | وثائقي · essay · قناة بدون وجه · كولاج ورقي (نمط VOX) | ❌ |
| **COMMERCIAL** | `workflows/engines/E2-commercial-engine.md` | إعلان منتج · حملة · brand film · promo | ✅ |
| **HYBRID** | `workflows/engines/E3-hybrid-commercial.md` | إعلان بسرد وثائقي/كولاج | ✅ |
| **SERIES** | `workflows/engines/E4-series-engine.md` | سلسلة · قناة · موسم · تقويم محتوى | ✅ |
| **BULK** | `workflows/engines/E5-bulk-production-pipeline.md` | تنفيذ بالجملة · كيف أنفّذ؟ | حسب الأصل |

### شجرة قرار المحركات

```
هل هناك منتج مادي يجب أن يبقى قابلاً للتعرّف؟
│
├─ لا ──── هل المحتوى سردي وثائقي/تاريخي؟
│           ├─ نعم ──► E1 (Documentary)
│           └─ لا  ──► M0 → M11 (فيلم/موشن/سرد حر)
│
└─ نعم ─── هل تريد سردًا وثائقيًا أو كولاجًا أرشيفيًا؟
            ├─ نعم ──► E3 (Hybrid)
            └─ لا  ───► E2 (Commercial)

هل تريد أكثر من عمل واحد؟      ──► E4 (Series) فوق أي محرك
هل وصلت لمرحلة التنفيذ؟        ──► E5 (Bulk Pipeline)
```

**القاعدة:** المحرك يستدعي المراحل (M) ولا يستبدلها.
→ الجدول الكامل: `references/protocols/engine-interop.md`

---

## المسارات السريعة (Shortcuts)

| الاختصار | المسار | متى | M4c QC |
|---|---|---|---|
| CONCEPT_ONLY | `workflows/shortcuts/concept-only.md` | "عندي فكرة، حوّلها concept" | ❌ |
| SINGLE_PROMPT | `workflows/shortcuts/single-prompt.md` | "اكتب برومبت واحد" | ❌ |
| IMAGE_GEN | `workflows/shortcuts/image-generation.md` | "صورة/فريم" | ❌ |
| I2V | `workflows/shortcuts/image-to-video.md` | "حرّك هذه الصورة" | ❌ |
| MOTION_GFX | `workflows/shortcuts/motion-graphics.md` | "موشن تايبوجرافي" | ❌ |
| LIPSYNC | `workflows/shortcuts/dialogue-lipsync.md` | "حوار/شفاه متحركة" | ❌ |
| SHOT_BUILD | M3a → M4a → M7b → M8a | لقطة واحدة في مشروع قائم | ✅ |
| SCENE | M0 → M4c (QC) → M9c | مشهد (3-8 لقطات) | ✅ إلزامي |
| FULL | M0 → M11 (بما فيه M4c) | فيلم/إعلان (30s-3min) | ✅ إلزامي |
| **THUMBNAIL** | `workflows/shortcuts/thumbnail.md` | ثامبنيل/غلاف لفيديو | ❌ |
| **SERIES** | `workflows/shortcuts/series.md` | تخطيط سلسلة أو قناة | ✅ |
| **DOCUMENTARY** | `workflows/shortcuts/documentary.md` | حلقة وثائقية بموضوع جاهز | ❌ |
| **PRODUCT_SHOT** | `workflows/shortcuts/product-shot.md` | مرجع منتج مقفول (IMG-00) | ❌ |

**القاعدة:** M4c إلزامي في أي مسار متعدد اللقطات (SHOT_BUILD، SCENE، FULL).
M4c اختياري في المسارات المستقلة (SINGLE، IMAGE_GEN، I2V، MOTION_GFX، LIPSYNC، CONCEPT).

## الأسئلة التشخيصية (إذا غامض)

بعد التصنيف الداخلي، ارجع إلى `references/protocols/user-facing-production-flow.md`. اسأل فقط ما يمنع البدء، في رسالة واحدة، وبحد أقصى **3 أسئلة** مع خيارات وافتراضات مهنية. لا تعرض اسم المسار للمستخدم.

1. **ما المخرج النهائي؟**
   - برومبت / صورة / فيديو / صوت / كل شيء

2. **ما الحجم؟**
   - لقطة واحدة / مشهد / فيلم كامل

3. **هل لديك أصول موجودة؟**
   - لا (ابدأ من الصفر) / نعم (صور/فيديو/صوت)

4. **ما المدة؟**
   - < 10s / 10-30s / 30-90s / > 90s

5. **ما المنصة؟**
   - TikTok/Reels (9:16, < 30s) / YouTube (16:9, any) / TV (16:9/4K)

**قاعدة:** إذا كانت المعلومات كافية فلا تسأل. إذا كانت ناقصة فاجمع حتى 3 أسئلة ضرورية في رسالة واحدة، ثم اختر المسار الأقرب وابدأ. لا تطلب من المستخدم صياغة Prompt أو استعمال مصطلحات تقنية.

## طبقة الإخراج العليا

بعد تحديد المسار، طبّق دائمًا:

1. `references/protocols/user-facing-production-flow.md`
2. `references/protocols/output-protocol.md`
3. `references/protocols/interaction-flow.md`

في المشاريع متعددة المشاهد: **الرؤية المختصرة → ورقة إنتاج متكيفة مع المدة والنوع قابلة للتصدير CSV → حزمة المرجعيات واعتمادها → Storyboard → اعتماد → Prompt كامل واحد لكل فريم → اختيار التوليد الخارجي/داخل المنصة → Prompt كامل واحد لكل لقطة**. لا تعرض البحث الخام أو الأجزاء الداخلية أو Prompts تحتاج إلى تركيب.

## Mermaid — خريطة المسار

```mermaid
flowchart TD
  Start[طلب المستخدم] --> Q1{يوجد أصول؟}
  Q1 -->|لا| Q2{حجم؟}
  Q1 -->|نعم| Q3{نوع الإصلاح؟}
  Q3 -->|صورة| IMG[IMAGE_GEN]
  Q3 -->|فيديو| I2V[IMAGE_TO_VIDEO]
  Q3 -->|صوت| AUDIO_REPAIR[REPAIR audio]
  Q2 -->|برومبت واحد| SP[SINGLE_PROMPT]
  Q2 -->|لقطة/مشهد| M0[M0 → M3]
  Q2 -->|فيلم كامل| FULL[M0 → M11]
```

## معايير التوجيه الجيد

| ✅ افعل | ❌ لا تفعل |
|---|---|
| اختر المسار الأدنى | لا تشغّل M0–M11 لمشروع بسيط |
| اجمع حتى 3 أسئلة ضرورية في رسالة واحدة | لا تسأل أسئلة متتابعة منخفضة القيمة |
| استخدم shortcuts/ إن أمكن | لا تخترع workflow جديد |
| احترم state القائم | لا تهمل project-memory.md |
| وثّق في decision-log | لا تنسَ سجل القرارات |

## عند الغموض الكامل

إذا كان الطلب غامضًا تمامًا ولا تستطيع تحديد intent، طبّق:

```
1. اقرأ workflows/M0-intake.md → املأ intake_brief
2. اعرض على المستخدم → "هل هذا صحيح؟"
3. طبّق تدفق `user-facing-production-flow` → ثم حدّد المسار
```

## Next Step

بعد تحديد المسار:
- **Shortcuts** → ارجع لـ `SKILL.md` § Quick Start
- **M0+** → ابدأ بـ `workflows/M0-intake.md`
- **كل المسارات** → طبّق `references/protocols/user-facing-production-flow.md` و`references/protocols/output-protocol.md`
- **REPAIR** → اقرأ `references/knowledge/failure-modes.md`
- **SCENE / FULL / SHOT_BUILD** → اقرأ `references/protocols/orchestration-runtime.md` (الـ executable spec للترتيب الكامل، load_context، validate، commit)
