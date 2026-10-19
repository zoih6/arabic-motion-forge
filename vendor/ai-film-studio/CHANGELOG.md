<!-- verify_links: allow-legacy -->

# AI Film Studio v1.1.0

## 3.1.0 — Reference & Prompt Orchestration

- Added `workflows/M4e-reference-orchestration.md` as a mandatory pre-Storyboard gate for multi-shot projects.
- Added a `reference_manifest` and `shot_reference_map` contract for characters, costumes, creatures, products, locations, props, and style anchors.
- Made every `@imageN` slot role-bound and traceable to an approved asset instead of leaving reference selection implicit.
- Added automated validation through `scripts/verify_reference_orchestration.py` and integrated it into `verify_all.sh`.
- Updated the user-facing sequence: vision → reference pack approval/lock → storyboard → image prompts → motion prompts.

## 3.2.0 — Executable Prompt Compiler

- Added `scripts/prompt_compiler.py` for deterministic JSON-to-prompt compilation.
- Added automatic `@ImageN` assignment from locked reference anchors and model-specific reference roles.
- Added camera-direction adapters for Seedance 2.0, Gemini Omni Flash, Veo 3, and natural-language fallbacks.
- Added provider validation for reference limits, video duration, and Seedance first/last-frame conflicts.
- Added `schemas/prompt-compiler-input.schema.json`, `examples/compiler-fixture.json`, and compiler tests.

## الهدف
تحويل AI Film Studio من منهج إنتاج متعدد الوكلاء إلى إطار تشغيل قابل للتتبع، مع الحفاظ على الوكلاء الحالية.

## التغييرات
- إصلاح بوابة الاعتماد: بعد M5 وقبل M6، بدل التعارض السابق بين M3/M4.
- إضافة Production State Machine.
- إضافة Agent Contract موحد.
- إضافة Shot Contract.
- إضافة Asset Registry.
- إضافة Continuity Ledger.
- إضافة Approval Log.
- إضافة Generation Log.
- إضافة Version Lineage.
- إضافة Text Execution Matrix.
- إضافة Repair/Revalidation Loop.
- ربط جميع الوكلاء بعقد تشغيل v1.1.
- تحويل `state/` من مفهوم ضمني إلى بنية فعلية.

## مبدأ التوافق
لا تزال ملفات الوكلاء الأصلية هي مصدر الاختصاص. طبقة v1.1 تضيف التحكم والتتبع ولا تستبدل الخبرة المتخصصة لكل وكيل.


## v1.1.1 — Output & Interaction Layer

- Added `references/protocols/output-protocol.md` for clean, progressive, copy-ready user-facing output.
- Added `references/protocols/interaction-flow.md` for a single-voice studio interaction model.
- First clarification round is now exactly 3 high-impact questions; second round is up to 3 only when required.
- Internal agent/state/validation details are hidden from normal user output.
- Added standardized response modes: DISCOVER, BUILD, DELIVER, REPAIR.
- Added `APPROVE / EDIT` single production approval interaction after M5.
- Updated Intake Agent to follow the new interaction protocol.
- Version bumped to 1.1.1.


## v1.2.0 — Adaptive Intelligence Layer

- Added `workflows/intent-router.md` for minimum-sufficient routing.
- Added `references/protocols/decision-policy.md` for user-vs-studio decision ownership.
- Added `references/specs/scene-shot-dna.md` for Scene DNA / Shot DNA inheritance.
- Added `references/knowledge/context-assembly.md` for tiered context loading and stale-context protection.
- Changed M0–M13 from mandatory universal flow to an adaptive full-production path selected by intent.
- Added a no-ask threshold so professional reversible decisions are made internally.
- Preserved v1.1.1 Output & Interaction Layer and single-voice user experience.
- Version bumped to 1.2.0.


## v1.3.0 — Prompt Runtime
- Added `references/specs/prompt-compiler.md`
- Added `references/specs/model-adapters.md`
- Added `references/specs/prompt-quality-gate.md`
- Added canonical prompt schema and compilation rules.
- Added capability-aware model adaptation.
- Added hard prompt quality gates and targeted repair loop.
- Established single-source Prompt Spec to prevent inconsistent prompt writing across agents.


## v1.4.0 — Project Memory System
- Added persistent project memory architecture.
- Added canonical memory schema, lifecycle, context policy, and session continuation protocol.
- Added `schemas/state/project-memory.md`, `schemas/state/decision-log.md`, and `schemas/state/session-checkpoint.md`.
- Added memory hierarchy, conflict resolution, versioning, compaction, and durable-fact rules.
- Added automatic continuation behavior for short follow-up commands without restarting Intake.
- Preserved v1.3 Prompt Compiler / Model Adapter / Quality Gate architecture.

## v1.4.1 — Arabic Typography + Validation Integration

- Preserved the Arabic copywriting and exact-text rendering rules from the prior production branch.
- Preserved the boundary between static Arabic text rendered in image models and time-based text rendered as editable motion/compositing layers.
- Adapted the structural and functional verification suite to the M0–M13 state-machine architecture.
- Added validation for agent contracts, prompt compiler, model adapters, memory state, continuity ledger, approval protocol, and text execution matrix.
- Corrected the package version metadata to `1.4.0` and expanded the skill description to include project memory and session continuation.
# AI Film Studio v1.5.0 — Changelog

## الهدف العام

إصدار v1.5 يحوّل المهارة من «نظام قوي» إلى **نظام حوكَوم**. الفكرة المركزية:

> **«القرار الذي يمكن اتخاذه على الورق، لا يجب أن يُتخذ في النموذج.»**

الإصدار يضيف طبقة فحص قبل التوليد (Pre-flight Check)، وكيل توطين عربي، خريطة قراءة سريعة، وقالب Concept Deck شفّاف. كل ذلك دون تغيير بنية المسار v1.4 — فقط إضافة طبقة.

---

## الإضافات الرئيسية

### 1. `workflows/M9c-preflight.md` — وكيل ما قبل التوليد

**المشكلة التي يحلها:**
حتى مع وجود 26 مرجعًا و 20 وكيلًا، قد يُرسَل prompt يخالف قاعدة موثقة (نسبة مدعومة، حركة كاميرا مفردة، نص ثابت في نموذج فيديو). إعادة التوليد تكلّف ميزانية ووقتًا.

**الحل:**
وكيل جديد يفحص كل prompt قبل إرساله للنموذج. يطبّق 8 Hard Gates (هوية، مراجع، حركة، استمرارية، توافق نموذج، نص، نظافة، سلامة) + 3 فحوصات خاصة بالموشن جرافيك.

**التأثير:**
- يمنع الهدر قبل حدوثه
- يكتشف الأخطاء في ثانية بدل 30 ثانية (زمن إعادة التوليد)
- موثّق في `schemas/state/asset-registry.md` بحقل `preflight_status`

**Gates الـ 8:**
- G1 — الهوية
- G2 — المراجع
- G3 — الحركة
- G4 — الاستمرارية
- G5 — توافق النموذج (نقلا عن `references/specs/model-matrix.md`)
- G6 — النص
- G7 — النظافة اللغوية
- G8 — السلامة والحقوق

**Gates خاصة بـ Motion Graphics:**
- G-M1 — الفصل المعماري (لا easing في prompt فيديو)
- G-M2 — القواعد العربية
- G-M3 — التراتبية (Hero > Punch > Supporting)

### 2. `workflows/M9d-localization.md` — وكيل التوطين

**المشكلة التي يحلها:**
المهارة تخدم السوق العربي، لكن النماذج تفهم الإنجليزية أفضل. لا يوجد وكيل متخصص في:
- ترجمة المعنى لا الحرف
- الحساسية الثقافية
- تمييز اللهجات (يمني/سعودي/خليجي/مصري/شامي/مغربي)
- قواعد النص العربي داخل الصور

**الحل:**
وكيل جديد يقدم:
- قاموس ترجمة سينمائية عربي ↔ إنجليزي
- قواعد ترجمة الصفة المجردة إلى فعل مرئي
- جدول تفاصيل ثقافية (ملابس، أماكن، دعائم) لكل منطقة
- معالجة الـ cultural_flags (كحول، دين، سياسة، لهجة، جندر)
- قواعد الطباعة العربية في prompts

**التأثير:**
- prompts أكثر دقة في تصوير السياقات العربية
- منع الإهانات الثقافية العرضية
- توفير قاموس جاهز لكل وكيل يحتاج الترجمة

### 3. `docs/` — خريطة القراءة السريعة

**المشكلة التي يحلها:**
SKILL.md ضخم (600+ سطر في v1.4)، وأي نموذج يقرأه يستهلك توكنز على أقسام قد لا يحتاجها.

**الحل:**
ملف فهرسي يقدم:
- خريطة المسارات حسب نية المستخدم
- جدول «أي وكيل أقرأه؟» لكل حالة
- خريطة المرجعيات الـ 26
- خريطة القوالب والـ state
- خريطة ملفات الفحص
- شجرة قرارات سريعة
- قائمة «لا تفعل»

**التأثير:**
- تقليل حجم السياق المُحمَّل
- تسريع التوجيه في بداية كل مشروع
- مرجع قابل للقراءة البشرية

### 4. `schemas/concept-deck.md` — قالب عرض المفاهيم

**المشكلة التي يحلها:**
عند توليد 3–5 اتجاهات إبداعية، يحتاج المستخدم طريقة واضحة للمقارنة والاختيار.

**الحل:**
قالب يقدم:
- بطاقة كاملة لكل اتجاه (زاوية، لوجلاين، لحظة حاسمة، افتتاحية)
- مقارنة بصرية بين الاتجاهات
- مخاطر وتكلفة وجدوى لكل اتجاه
- توصية مع سبب
- نموذج اعتماد صريح

**التأثير:**
- شفافية في قرارات M1
- قرارات أسرع وأدق
- توثيق اعتمادات في جدول مدمج

### 5. توسيع `references/knowledge/failure-modes.md`

**الإضافات:**
- **القسم 7:** أعطال الترجمات والتوطين
  - ملامح أوروبية رغم طلب «عربي»
  - ملابس غير مناسبة ثقافيًا
  - نص عربي مشوّه
  - lip-sync فاشل
- **القسم 8:** أعطال ما قبل التوليد
  - preflight لم يُدمج
  - prompt طويل جدًا
  - تكرار بدون seed

---

## مبدأ التوافق

v1.5 **لا يغير** أي قاعدة في v1.4 أو v1.3 أو v1.2 أو v1.1. كل الإضافات تكمّل ولا تستبدل.

| الإصدار | الإضافة | التوافق |
|---|---|---|
| v1.1 | State Machine + Agent Contracts | ✅ محفوظ |
| v1.1.1 | Output & Interaction Layer | ✅ محفوظ |
| v1.2 | Adaptive Routing | ✅ محفوظ |
| v1.3 | Prompt Compiler | ✅ محفوظ |
| v1.4 | Project Memory | ✅ محفوظ |
| v1.4.1 | Arabic Typography + Validation | ✅ محفوظ |
| **v1.5** | **Pre-flight + Localization + Index + Concept Deck** | ✅ جديد مكمّل |

---

## المسار المحدّث (v1.5)

```text
USER REQUEST
  ↓
[INDEX.md] — تحديد المسار الأدنى
  ↓
INTENT ROUTER (references/intent-router.md)
  ↓
[20-localization] — ترجمة وحساسية ثقافية
  ↓
CREATIVE / SHOT SPEC
  ↓
SCENE DNA + SHOT DNA
  ↓
CANONICAL PROMPT SPEC
  ↓
MODEL ADAPTER
  ↓
PROMPT COMPILER
  ↓
QUALITY GATE (references/prompt-quality-gate.md)
  ↓
[19-preflight-check] — 8 Hard Gates
  ├─ FAIL → TARGETED REPAIR → RECOMPILE → PRE-FLIGHT
  └─ PASS → CLEAN DELIVERY
```

---

## أرقام v1.5

| المورد | v1.4.1 | v1.5 |
|---|---|---|
| وكلاء | 18 | **20** |
| مرجعيات | 24 | **24** (failure-modes توسعت) |
| قوالب | 5 | **6** (concept-deck) |
| ملفات فهرسة | 0 | **1** (INDEX.md) |
| Gates فحص | 7 (quality) | **7 + 8 (preflight) + 3 (motion)** |
| تحقق آلي | 4 scripts | **4 scripts (محدّثة)** |

---

## تغييرات في الأمان

- Pre-flight Gate G8 يُضيف فحصًا منهجيًا للقيود الإقليمية (EEA/CH/UK)
- Localization يضيف `cultural_flags` للقضايا الحساسة
- Concept Deck يفرض شفافية في القرارات الإبداعية قبل التوليد

---

## ملفات تم تحديثها

| الملف | التغيير |
|---|---|
| `SKILL.md` | إضافة قسم v1.5، تحديث قائمة الوكلاء، تحديث رقم الإصدار |
| `workflows/M9c-preflight.md` | **جديد** |
| `workflows/M9d-localization.md` | **جديد** |
| `docs/` | **جديد** |
| `schemas/concept-deck.md` | **جديد** |
| `references/knowledge/failure-modes.md` | قسمان جديدان (7 و 8) |
| `_verify_structure.py` | فحوصات v1.5 في القسم 8 |
| CHANGELOG-v1.5 | **هذا الملف** |

---

## Breaking Changes

**لا شيء.** v1.5 backward-compatible بالكامل.

- الـ 18 وكيلًا الحاليين لم يتغير أي منهم
- الـ 24 مرجعًا الحاليين لم يتغير أي منهم
- جميع القواعد الـ 24 (في SKILL.md) لم تتغير
- Prompt Compiler و Model Adapter لم يتغيرا
- Project Memory لم يتغير

الإضافات كلها **اختيارية التكامل**:
- إذا لم تستدعِ 19-preflight-check، المهارة تعمل كالسابق
- إذا لم تستدعِ 20-localization، prompts تخرج بدون توطين
- إذا لم تستخدم INDEX.md، اقرأ SKILL.md كالسابق
- إذا لم تستخدم concept-deck، اعرض الاتجاهات في رسالة عادية

---

## قرار الترقية

| إذا كنت... | يجب أن ترقّي |
|---|---|
| تستخدم v1.4.x في الإنتاج | ✅ نعم — Pre-flight يوفّر ميزانية |
| تخدم محتوى عربي ثقافي | ✅ نعم — Localization ضروري |
| تدير أكثر من مشروع متوازٍ | ✅ نعم — INDEX يوفر وقت |
| تعرض الاتجاهات للمستخدم | ✅ نعم — Concept Deck |
| تكامل مع Claude/GPT | ⚠️ اختياري — الـ preflight script كافٍ |

---

## المساهمون

- الإصدار v1.5 صُمّم كتحليل وتطوير لمنظومة v1.4.1
- الفلسفة: «الحوكمة قبل التوليد»

---

## القادم

لا توجد خارطة طريق معلنة لـ v1.6. الترقيات المستقبلية ستعتمد على:
1. ملاحظات المستخدمين الفعليين
2. تحديثات في قدرات النماذج
3. أنماط الفشل الجديدة المكتشفة
# Changelog v2.0 — من "Prompt Writer" إلى "AI Film Production System"

**تاريخ الإصدار:** 2026-01-15
**النوع:** Major Release (Backward Compatible)
**المطور:** AI Film Studio Team
**المدة:** 90 يوم تطوير

---

## الملخص التنفيذي

v2.0 هي **إعادة هندسة كاملة** للمهارة من "نظام يكتب Prompts لمشاهد" إلى **"AI Film Production System" متكامل**. المنظومة الآن تحتوي على **31 وكيلًا** بدل 20، و**10 طبقات Prompt Architecture (A-J)**، و**Continuity Bible + Frame Chain** لإدارة Start→End Frame Chaining، و**AI-Native Graphic Composition**، و**Audio Decision Engine**، و**8 Quality Gates** صارمة، و**Executive Producer مركزي**، و**5 ملفات تسليم** منفصلة.

**كل التحسينات backward-compatible** — الكود والمخرجات القديمة (v1.5) تعمل كما هي.

---

## 🎯 ما الجديد في v2.0

### 1. 11 وكيلًا جديدًا (من 20 إلى 31)

| # | الاسم | الوظيفة | المرحلة |
|---|---|---|---|
| 21 | Creative Research Lab | البحث الإبداعي الموحد (5 محاور + Divergent→Convergent) | M1 |
| 22 | Prompt Architecture Director | هندسة البرومبتات بـ 10 طبقات A-J | M8, M9 |
| 23 | Narrative Architect | البنية السردية + Story Spine + Script | M3 |
| 24 | Shot Architect | تصميم اللقطات + Blocking + Edit Handles | M4 |
| 25 | Continuity Supervisor | Continuity Bible + Frame Chain | M5 |
| 26 | Transition Engineer | تصميم الانتقالات (12 نوع) | M6 |
| 27 | Graphic & Typography Director | AI-Native Graphic Composition | M6.5 |
| 28 | Text Preservation Motion | استراتيجية تحريك النصوص | M6.5 |
| 29 | Audio Decision Engine | شجرة قرار الصوت | M7 |
| 30 | Executive Producer | المنسق المركزي + 5 Output Files | M10, M11 |
| 31 | Quality Gate Controller | 8 Quality Gates (G0–G8) | مستمرة |

### 2. Prompt Architecture — 10 طبقات A-J

كل prompt الآن يمر عبر 10 طبقات معمارية:

- **A — Intent** (الهدف)
- **B — Subject** (الموضوع)
- **C — Environment** (البيئة)
- **D — Composition** (التكوين)
- **E — Camera** (الكاميرا)
- **F — Lighting** (الإضاءة)
- **G — Motion** (الحركة — فيديو فقط)
- **H — Cinematic Continuity** (الاستمرارية)
- **I — Style & Visual DNA** (الأسلوب)
- **J — Constraints** (القيود)

التوثيق الكامل في `references/specs/prompt-architecture.md`.

### 3. Continuity Bible + Frame Chain

نظام **Start→End Frame Chaining** يضمن أن:
- `SC(N+1)_START_FRAME = SC(N)_END_FRAME` بصريًا
- Identity String محفوظ حرفيًا عبر كل prompt
- Image Anchors للشخصيات، الملابس، الدعائم، الأماكن
- Color Palette Lock + Color Script Map
- Camera Grammar ثابتة
- Acoustic Signature محددة

التوثيق الكامل في `references/specs/continuity-bible-schema.md`.

### 4. AI-Native Graphic Composition

استراتيجيات 5 للنصوص:
- **Burn-In داخل Prompt الصورة**
- **Post-Production Overlay** (الأضمن، 100%)
- **Image-to-Video من صورة محتوية النص**
- **Video-to-Video مع Locked Region**
- **Typography as Architecture** (نادر)

**مبدأ Single Locked Visual Plane:** طبقة بصرية واحدة محكومة لكل نص.

### 5. Audio Decision Engine

شجرة قرار كاملة للصوت:
- 6 طبقات صوتية (Dialogue, VO, Music, SFX, Foley, Ambience)
- 4 استراتيجيات Lip-Sync (Native Audio, Regenerate, Dubbing, Avoid)
- Mixing Plan (levels + ducking)
- Mastering Plan (-14 LUFS YouTube, -16 Instagram, etc.)

التوثيق الكامل في `references/specs/audio-decision-tree.md`.

### 6. 12 نوع انتقال (من 3 إلى 12)

توثيق كامل لـ 12 نوع انتقال:
1. Cut, 2. Cross Dissolve, 3. Fade to Black, 4. Match Cut, 5. Whip Pan, 6. Morph, 7. Zoom Transition, 8. Wipe, 9. L-Cut/J-Cut, 10. Graphic Match, 11. Sound Bridge, 12. Hard Cut on Action

التوثيق الكامل في `references/specs/transition-types.md`.

### 7. 8 Quality Gates (G0–G8)

- **G0 — Intake Clarity**
- **G1 — Idea Quality**
- **G2 — Narrative Quality**
- **G3 — Continuity Quality**
- **G4 — Prompt Quality** (Hard Gate)
- **G5 — Transition Quality**
- **G6 — Text Quality**
- **G7 — Audio Quality**
- **G8 — Master Quality** (Hard Gate)

كل Gate لها معايير صارمة، scoring matrix، وإجراء الفشل.

### 8. 5 Output Files (حزم التسليم)

لا تخرج مخرجات خام. كل مشروع يُسلَّم في 5 ملفات منفصلة:

1. **`schemas/production-blueprint.md`** — النظرة الشاملة
2. **`schemas/image-prompts-package.md`** — كل prompt صورة
3. **`schemas/motion-prompts-package.md`** — كل prompt فيديو
4. **`schemas/audio-package.md`** — كل الطبقات الصوتية
5. **`schemas/assembly-guide.md`** — دليل التجميع خطوة بخطوة

### 9. Decision Log + Risk Register

كل قرار كبير موثّق في `schemas/state/decision-log.md`. كل خطر مُسجَّل مع mitigation في `schemas/state/risk-register.md`.

### 10. State Management

3 ملفات state جديدة:
- `schemas/state/continuity-bible.md`
- `schemas/state/frame-chain.md`
- `schemas/state/quality-gates-log.md`

(مكملّة للـ `references/knowledge/project-memory.md` و `schemas/state/asset-registry.md` و `schemas/state/decision-log.md` و `schemas/state/risk-register.md` من v1.5)

---

## 📊 إحصائيات الترقية

| المقياس | v1.5 | v2.0 | التغيير |
|---|---|---|---|
| عدد الوكلاء | 20 | 31 | +55% |
| عدد الـ Prompts لكل مشهد | 1-2 | 1-3 (مع Motion layer مفصّل) | +50% |
| عدد الـ Quality Gates | 5 (soft) | 8 (مع hard gates) | +60% |
| عدد ملفات التسليم | 1-2 (مدمجة) | 5 (منفصلة) | +250% |
| عدد الـ References | 24 | 28 | +17% |
| عدد الـ Templates | 1 (concept-deck) | 6 | +500% |
| عدد ملفات state | 5 | 8 | +60% |
| متوسط طول الـ Prompt | 30-50 كلمة | 100-300 كلمة | +400% |
| عدد أنواع الانتقالات الموثقة | 3 (cut/dissolve/fade) | 12 | +300% |
| أسلوب Pipeline | 6 مراحل | 12 مرحلة (M0–M11) | +100% |

---

## 🔄 Backward Compatibility

كل شيء في v1.5 يعمل في v2.0:

- ✅ الـ 20 وكيل من v1.5 موجودون كما هم
- ✅ الـ 24 references من v1.4/v1.5 موجودة
- ✅ `schemas/concept-deck.md` (v1.5) موجود
- ✅ `schemas/state/project-memory.md`، `schemas/state/asset-registry.md`، `schemas/state/decision-log.md`، `schemas/state/risk-register.md` (v1.5) موجودة
- ✅ `examples/coffee-short.md` (v1.x) موجود
- ✅ `_verify_structure.py` و `_verify_all.sh` يعملان

الإضافات الجديدة **تكمّل** ولا تستبدل.

---

## 🆕 الملفات الجديدة في v2.0

### Agents (11 جديد)

```
agents/21-creative-research-lab.md
agents/22-prompt-architecture.md
agents/23-narrative-architect.md
agents/24-shot-architect.md
agents/25-continuity-supervisor.md
agents/26-transition-engineer.md
agents/27-graphic-typography-director.md
agents/28-text-preservation-motion.md
agents/29-audio-decision-engine.md
agents/30-executive-producer.md
agents/31-quality-gate-controller.md
```

### Templates (5 جديد)

```
templates/01-production-blueprint.md
templates/02-image-prompts-package.md
templates/03-motion-prompts-package.md
templates/04-audio-package.md
templates/05-assembly-guide.md
```

### References (4 جديد)

```
references/prompt-architecture-spec.md
references/continuity-bible-schema.md
references/transition-types.md
references/audio-decision-tree.md
```

### State (3 جديد)

```
state/continuity-bible.md
state/frame-chain.md
state/quality-gates-log.md
```

### Examples (1 جديد)

```
examples/energy-drink-ad.md
```

### Documentation

```
SKILL.md (محدّث بالكامل لـ v2.0)
INDEX.md (محدّث)
CHANGELOGv2.0 (هذا الملف)
```

---

## 🐛 إصلاحات من v1.5

1. **هوية الشخصية تتغير بين المشاهد** → Continuity Bible + Identity String حرفي
2. **النصوص مشوهة في الفيديو** → Post-Production Overlay strategy
3. **الإضاءة غير متسقة** → Lighting Grammar + Color Script Map
4. **محور 180° مكسور** → Frame Chain مع Screen Direction
5. **انتقالات عشوائية** → 12 نوع موثّق + مصفوفة اختيار
6. **الصوت غير متناسق** → Audio Decision Tree + Mixing Plan
7. **Lip-Sync ضعيف** → 4 استراتيجيات + fallback hierarchy
8. **Master LUFS خاطئ** → Platform-specific mastering plan
9. **لا يوجد Decision Log** → state/decision-log.md
10. **لا يوجد Risk Register** → state/risk-register.md
11. **Quality Gates شكلية** → 8 Gates مع scoring صارم + Hard Gates
12. **الـ User يتوه في الإجابات** → 5 Output Files منظمة + Executive Producer

---

## 📈 مبادئ التصميم (ما الذي لم يتغير)

1. **جودة الـ Prompt أهم من الاختصار** — لا نختصر prompt "لتسريع التوليد"
2. **الـ Identity يجب أن يكون حرفيًا** — لا نُعيد صياغة
3. **الاستمرارية حجة ملكية** — Frame Chain هو جوهر العمل
4. **النص في الفيديو مشكلة** — نخطط لها مبكرًا
5. **الصوت يصلح الصورة** — نخطط له مبكرًا
6. **المستخدم أقل خبرة = المهارة أكثر قدرة** — كلما كان المستخدم أقل خبرة، المهارة تعوّض أكثر

---

## 🎓 كيف تستخدم v2.0

### للمستخدمين الجدد

1. ابدأ بـ `SKILL.md` (الـ overview الجديد)
2. اقرأ `docs/` (دليل الملفات)
3. ادرس `examples/energy-drink-ad.md` (مثال حي كامل)
4. ابدأ مشروعك الأول

### للمستخدمين القدامى (v1.5)

1. اقرأ CHANGELOG-v2.0 (هذا الملف)
2. راجع `workflows/M9a-executive-producer.md` (المنسق الجديد)
3. راجع `workflows/M9b-quality-gates.md` (البوابات الجديدة)
4. جرّب مشروع صغير باستخدام v2.0
5. تبنّى تدريجيًا

---

## 🤝 المساهمة

- 🐛 **بلاغات الأخطاء:** افتح issue
- 💡 **اقتراحات:** افتح discussion
- 🔧 **Pull Requests:** مرحب بها
- 📚 **تحسين التوثيق:** أولوية عالية

---

## 📄 الترخيص

MIT License — نفس v1.5

---

## 🙏 شكر وتقدير

شكر لكل من ساهم في v1.x و v2.0، ولكل من يستخدم المهارة في مشاريعه.

**AI Film Studio v2.0 — من Prompt Writer إلى AI Film Production System.**

**التاريخ:** 2026-01-15
**الإصدار:** v2.0.0
**الحالة:** Production-Ready

---

## v2.0.1 — Agent Skills Standard Restructure (2026-01-15)

**النوع:** Refactor Release (Backward Compatible)
**المحرّك:** مطابقة معيار Agent Skills Standard + Progressive Disclosure

### إعادة الهيكلة

| قبل (v2.0.0) | بعد (v2.0.1) | السبب |
|---|---|---|
| `agents/01-31-*.md` | `workflows/M0-M11-*.md` | تنظيم حسب المرحلة لا التخصص |
| `templates/01-05-*.md` | `schemas/*.md` | تمييز المخرجات عن القوالب |
| `state/*.md` | `schemas/state/*.md` | تجميع State مع Schemas |
| `references/*.md` (مسطّح) | `references/{protocols,specs,knowledge}/` | تصنيف حسب الوظيفة |
| `_verify_*.{py,sh}` (في الجذر) | `scripts/verify_*.{py,sh}` | فصل الأدوات القابلة للتنفيذ |
| `docs/` (مرجع قديم) | `workflows/intent-router.md` + `workflows/README.md` | Progressive Disclosure |
| CHANGELOG-v1.1 + v1.5 + v2.0 | `CHANGELOG.md` (موحّد) | ملف واحد للإصدارات |

### الجديد

- **`SKILL.md` ≤ 200 سطر** — Progressive Disclosure tier 1
- **`workflows/shortcuts/`** — 7 مسارات سريعة (concept, single-prompt, image, i2v, motion, lipsync, repair)
- **`quality/`** مجلد مستقل — `quality/quality-gates.md`, `quality/checklist.md`, `quality/self-audit.md`
- **`assets/`** — للأصول الثابتة (placeholders)
- **README.md** كنقطة دخول بشرية (158 سطر)
- **TAGS YAML frontmatter** في كل ملف (tier, when_to_load, parent)

### التحويلات الآلية

- 139 مرجع تم تحديثه في 44 ملف
- 30 ملف تم نقله من `agents/` إلى `workflows/`
- 23 ملف تم نقله من `templates/` و `state/` إلى `schemas/`
- 26 ملف تم نقله إلى `references/{protocols,specs,knowledge}/`
- 5 سكربتات تم نقلها إلى `scripts/` + chmod +x

### Backward Compatibility

- ✅ كل المحتوى محفوظ (لا حذف)
- ✅ `git mv` (التاريخ محفوظ)
- ✅ CHANGELOG يحوي الإصدارات السابقة

### الفحوص

- `bash scripts/verify_all.sh` → 4/4 ✅
  - structure: 80+ ملف
  - functional: 30/30
  - motion: 46/46
  - example: 29/29

### الملفات

| | قبل | بعد |
|---|---|---|
| مجلدات | 5 (agents, references, templates, state, examples) | 7 (+workflows, +quality, +scripts, +assets) |
| ملفات MD | 91 | 91 (محتوى محفوظ) |
| ROOT files | 9 (README, SKILL, INDEX, 3 CHANGELOG, 5 _verify) | 4 (SKILL, README, CHANGELOG, LICENSE) |
| SKILL.md | 232 سطر | 164 سطر (≤ 200) |

---

## v2.0.2 — Stage Model Unification (2026-01-15)

**النوع:** Structural Repair (Backward Compatible)
**الهدف:** حل تضاربات ترقيم المراحل بين الملفات (M0–M13 vs M0–M11) وتوفير orchestration spec تنفيذي.

### P0-1 — توحيد Production Stage Model

- **قبل:** `references/protocols/production-state-machine.md` يحوي M0–M13 (v1.1، 14 gates).
- **بعد:** v2.0.2 موحّد على **M0–M11** (12 مرحلة رئيسية، 31 workflow، 8 gates).
- هذا الملف الآن **المرجع الرسمي الوحيد** لتعريف المراحل.
- filesystem (`workflows/M*.md`) يبقى source of truth تشغيلي.

### P0-2 — Orchestration Runtime (جديد)

- **ملف جديد:** `references/protocols/orchestration-runtime.md` (≈450 سطر).
- يغطي **9 مسارات** (REPAIR، SINGLE_PROMPT، IMAGE_GEN، I2V، MOTION_GFX، LIPSYNC، CONCEPT، SHOT_BUILD، SCENE_BUILD، FULL_PRODUCTION).
- لكل مسار: route + load_context + run (ordered/parallelizable/skip) + validate + commit.
- مرجع تشغيلي لـ LLM agents، ليس مجرد توثيق وصفي.

### P0-3 — إصلاح تضارب M2/M3/M11

- **قبل:** M9a-EP يقول M2=Concept، M3=Narrative، M4=Shot، M5=Continuity، M6=Transitions، M7=Audio، M8=Image Prompts، M9=Motion، M11=Final Assembly.
- **بعد:** يطابق filesystem (M2=Narrative، M3=Shot، M4=Continuity، M5=Graphics، M6=Audio، M7=Image، M8=Motion، M9=Quality، M11=Final Delivery).
- كل من M9a و SKILL.md و README.md و intent-router.md يستخدم نفس التعريف.

### P1-4 — M4c إلزامي في المسارات المتعددة

- `workflows/intent-router.md` يحدد بوضوح: M4c required في SHOT_BUILD، SCENE، FULL.
- اختياري في SINGLE_PROMPT، IMAGE_GEN، I2V، MOTION_GFX، LIPSYNC، CONCEPT (لا multi-shot).

### إصلاحات بنيوية إضافية

- `quality/quality-gates.md` يحدد رسميًا: production-state-machine = AUTHORITATIVE للـ stages.
- `SKILL.md` و `README.md` يوضحان "12 stages / 31 workflows".
- `references/protocols/interaction-flow.md` و `workflows/M9d-localization.md` يحدّثان M13 → M11.

### Backward Compatibility

✅ كل المحتوى v2.0.1 محفوظ.
✅ v1.x paths (M0–M13) ما زالت تعمل عبر LLM interpreter.
✅ لا workflow حُذف ولا عُدّل.
✅ CHANGELOG يحوي v1.1، v1.2، v1.3، v1.4، v1.5، v2.0.0، v2.0.1، v2.0.2.

### ما لم يدخل v2.0.2 (ديون تقنية)

- ❌ Memory Conflict Resolution (P1#5 القديمة) — مؤجل.
- ❌ Story / Editorial QC (P1#7) — مؤجل.
- ❌ إعادة كتابة verify_functional.py (سيناريو happy path).
- ❌ إعادة هيكلة M8b / M8c (ملفات شبه فارغة).
- ❌ تحديثات prompt-compiler / model-adapters من v1.3.

### الفحوص

- `bash scripts/verify_all.sh` → 4/4 ✅
- `grep "M12\|M13" workflows/ references/ schemas/ quality/ scripts/` → 0 matches (في الملفات الجديدة/المعدّلة).
- تطابق M2/M3/M11 بين M9a و SKILL و README و intent-router: ✅

### الملفات المتأثرة

| نوع | عدد | أمثلة |
|---|---|---|
| معدّل | 7 | production-state-machine.md، M9a-executive-producer.md، SKILL.md، README.md، quality-gates.md، intent-router.md، interaction-flow.md، M9d-localization.md |
| جديد | 1 | orchestration-runtime.md |

---

## v2.1.0 — Memory + Prompt + Verify (2026-01-15)

**النوع:** Feature Release (Backward Compatible)
**الهدف:** إغلاق 3 فجوات بنيوية (Memory، Prompt Layer، Functional Verify) + قرار M8b/M8c.

### P0 — Memory Conflict Resolution Contract (جديد)

- **ملف جديد:** `references/knowledge/memory-conflict-contract.md` (~340 سطر).
- 6 أنواع تضارب مغطاة رسميًا:
  1. **No Conflict** — تنفيذ عادي.
  2. **Shot Override** — تغيير على لقطة واحدة، silent auto-promote.
  3. **Scene Override** — تغيير على مشهد، silent auto-promote.
  4. **Project / Canonical Update** — تغيير على character/wardrobe/style، silent + SUPERSEDED.
  5. **User-approved Supersession** — يتطلب موافقة صريحة قبل التنفيذ.
  6. **Ambiguous Conflict** — اسأل المستخدم إذا كان high-impact/irreversible.
- Source of Truth Hierarchy (6 مستويات).
- Scope Detection Rules (regex patterns).
- Override Lifetime (per conflict type).
- Superseded Decision Handling (lineage preservation).
- Decision Log Update Rules (12 field schema).
- Continuity Bible Update Rules (5-step protocol).
- Session Checkpoint Propagation (cross-session).
- Integration with Memory Lifecycle v1.4 (10 hooks).
- **AUTHORITATIVE للـ conflict resolution.**

### P0 — Prompt Layer Alignment (تنظيف v1.x)

- **`references/specs/prompt-compiler.md`** — v1.3 → v2.1.0:
  - ترتيب Pipeline: Model Adapter صار قبل Compiler (الترتيب الصحيح).
  - ربط صريح بـ 5 workflows تستدعيه.
  - Stage references: M2/M3a/M4a (لا v1.x).
  - "ما تغيّر / ما لم يتغيّر" موثّق.
- **`references/specs/prompt-quality-gate.md`** — v1.3 → v2.1.0:
  - G1-G7 → PG-1-PG-7 (لتجنب التضارب مع G0-G8 end-to-end).
  - ربط بـ G4 Hard Gate في v2.0.2.
  - 7 sub-criteria + scoring + repair logic.
- **`references/specs/model-adapters.md`** — v1.3 → v2.1.0:
  - Model Profiles table (12 عائلة).
  - Capability-Aware Translation (8 checks).
  - موقع في Pipeline (بين Canonical Spec و Compiler).
- **النتيجة:** الـ Interface النهائي: Workflow Output → Canonical Spec → Model Adapter → Compiler → Quality Gate.

### P1 — Functional Verification Rewrite (multi-fixture)

- **`scripts/verify_functional.py`** — 351 سطر (سيناريو واحد) → ~390 سطر (3 أنواع اختبارات + 4 fixtures).
- **1. Structural Validation** — 14 مجلد + 26 ملف مطلوب + 31 workflow.
- **2. Route / Contract Validation** — 10 routes في orchestration-runtime، 5 contract sections لكل route، M4c إلزامي في SHOT/FULL، 6 conflict types.
- **3. Integration Simulation** — 4 fixtures (قهوة TikTok، NOOR YouTube، موشن تايبوجرافي، lipsync عربي) + 5 negative tests.
- **النتيجة:** 95/95 نجاح (بدلاً من 30/30 سيناريو واحد).
- لم يعد يعتمد على USER_REQUEST واحد hard-coded.

### M8b / M8c Audit (قرار)

- **ملف جديد:** `docs/m8b-m8c-audit.md`.
- **القرار: الإبقاء منفصلين.** لكل منهما Input/Output Contract مستقل:
  - M8b = Motion Direction (creative spec للحركة، قبل M8a).
  - M8c = Animation Ready (technical spec للأصل، قبل M7b).
- لا تداخل، لا ازدواجية.

### Backward Compatibility

✅ كل المحتوى v2.0.2 محفوظ.
✅ v1.x paths (M0–M13) ما زالت تعمل.
✅ v1.3 prompt specs محتفظة بالسلوك (الـ 10 قواعد compilation + priority order + canonical schema).
✅ v1.4 memory schema محفوظ (memory-conflict-contract يضيف طبقة فوقها).

### الديون التقنية المتبقية (Roadmap)

- ❌ Story / Editorial QC
- ❌ Multi-agent real integration test (verify_functional لا يزال يحاكي)
- ❌ M8b (70 سطر) و M8c (63 سطر) — محتوى معقول لكن يمكن تعميقه
- ❌ Agent Skills Standard onboarding docs

### الفحوص

- `bash scripts/verify_all.sh` → 4/4 ✅
  - structure: 95 ملف
  - functional: 95/95 (3 test types + 4 fixtures)
  - example: 29/29
  - motion: 46/46

### الملفات المتأثرة

معدّل (6): SKILL.md، README.md، CHANGELOG.md،
            references/specs/prompt-compiler.md،
            references/specs/prompt-quality-gate.md،
            references/specs/model-adapters.md،
            scripts/verify_functional.py
جديد (2): references/knowledge/memory-conflict-contract.md،
          docs/m8b-m8c-audit.md

---

## 🛑 Roadmap Note — Stopping Architecture Reviews

**بعد v2.1.0، يتوقف الفريق عن المراجعات المعمارية والتحسينات النظرية.**

المهارة تنتقل إلى مرحلة **الاستخدام الفعلي** (Production Use):
- اختبارها على مشاريع حقيقية وأفلام واقعية.
- قياس الأداء على prompts، generations، time-to-deliver.
- جمع feedback من الاستخدام.

أي تحسين لاحق يجب أن يأتي من:
- مشكلة ظهرت أثناء الاستخدام.
- طلب مستخدم حقيقي.
- bottleneck في الـ pipeline (وليس تحسين نظري).

**لماذا؟** البنية الحالية:
- Stage Model موحّد (M0–M11، 31 workflow).
- 8 Quality Gates (G0–G8، Hard Gates: G4, G8).
- Orchestration Runtime (10 routes، contracts كاملة).
- Memory Conflict Contract (6 types، Source of Truth، lifecycle).
- Prompt Layer aligned (4 stages، 10 layers، G4 hard gate).
- 4 verify scripts (95 + 30 + 29 + 46 = 200+ test).
- 2 مثال حي.

الـ "1% النهائي" من التحسينات المعمارية لن يكون له أثر ملموس
مقارنة بـ "feedback من استخدام حقيقي".

---

## v3.0.0 — VOX Integration & Unified System (2026-09-10)

**أكبر تحديث في تاريخ المستودع:** دمج أربعة مستودعات سابقة في نظام واحد،
مع 17 إضافة جديدة كليًا.

### الهدف

بناء **نسخة نهائية موحّدة** تحتوي كل ما في الأنظمة السابقة (بلا فقد)،
تضيف **عقودًا ومسارات** جديدة، وتُنظَّم وفق **معايير بناء المهارات**
(Agent Skills Standard) لتكون جاهزة للعمل في **أي وكيل**.

### المستودعات المدمجة

| المستودع | الملفات | ما أُخذ |
|---|---|---|
| `ai-film-studio` v2.1.0 | 113 | العمود الفقري M0–M11 (31 workflow) · Prompt Architecture A–J · G0–G8 · Memory System |
| `vox-paper-engine` | 37 | محرك الوثائقيات · DNA الكتابة · حساب الـ Beats · الصوت · الثامبنيل · آلة الحالات التسع |
| `vox-commercial-director` | 69 | طاقم 9 أدوار · 10 مراحل · Big Idea · 8 عوالم · Product Reference · الهجين |
| `vox-commercial-director-skill` v3.0.0 | 20 | Brief بـ 12 حقلًا · T1–T4 · منحنى الطاقة · End Card · A/B · Edit Sheet |

### إضافات جديدة (B Added)

**بنية جديدة**
- `styles/` — مكتبة العوالم البصرية: **10 أقفال نصية حرفية (LOCK A–J)** + 3 خواتيم + Universal Video Prompt + قالب بناء قفل مخصص
- `workflows/engines/` — **5 محركات**: E1 Documentary · E2 Commercial · E3 Hybrid · E4 Series · E5 Bulk Pipeline
- `references/research/` — **5 أدوات بحث**: search-playbook · reference-mining · fact-verification · trend-research · query-library

**مواصفات جديدة (specs)**
- `beat-architecture.md` — حساب الـ Beats + منحنى الطاقة + جداول 6/10/15/30/60 ثانية
- `idea-engine.md` — 12 عدسة للجنون المنضبط + تصنيف الـ Hooks + مصفوفة التقييم
- `product-truth.md` — مستويات T1–T4 + Product Anchor + IMG-00
- `entity-ledger.md` — سجل الكيانات المقفولة
- `model-dialects.md` — لهجات 12 عائلة نماذج
- `thumbnail-dna.md` — حمض الثامبنيل + فحص الـ 200 بكسل
- `platform-specs.md` — مواصفات المنصات والمناطق الآمنة
- `brief-spec.md` — Brief بـ 12 حقلًا + سجل الافتراضات

**معارف جديدة (knowledge)**
- `narrative-writing-dna.md` — Cold Open · 5 أنماط Cliffhanger · انضباط الجملة
- `voice-system.md` — إعدادات ElevenLabs · الدفعات · ثبات الـ Voice ID
- `series-architecture.md` — معمارية السلاسل والقنوات
- `truth-and-safety.md` — الدقة · ضبط المآسي · الحقوق · الحساسية الثقافية

**بروتوكولات جديدة**
- `discovery-protocol.md` — الرد الأول: 3 اتجاهات + ≤3 أسئلة
- `style-lock-protocol.md` — النسخ الحرفي · الاستبدالات · الاستثناءات
- `engine-interop.md` — التكامل بين المحركات والمراحل

**مخططات إخراج جديدة (10)**
`brief` · `beat-table` · `shot-card` · `product-sheet` · `edit-sheet` · `end-card` ·
`thumbnail-pack` · `delivery-pack` · `series-bible` · `prompts-txt`

**بوابات جودة جديدة (G9–G13)**
- G9 Script & Narrative · G10 Beats & Timing · G11 Product Fidelity · G12 Platform & Delivery · G13 Series Consistency
- `quality/pre-flight-checklist.md` — 40 نقطة فحص في دقيقة
- `quality/ten-second-test.md` — اختبار العشر ثوانٍ لكل برومبت

**مسارات سريعة جديدة (4)**
`thumbnail` · `series` · `documentary` · `product-shot`

**أمثلة حية جديدة (2)**
- `examples/paper-collage-documentary.md` — حلقة وثائقية كاملة (E1)
- `examples/commercial-15s-lock-b.md` — إعلان 15 ثانية (E2)

**سكربتات فحص جديدة (4)**
- `verify_styles.py` · `verify_vox.py` · `verify_links.py` · `prompt_lint.py`
- `verify_all.sh` محدّث: **8 فحوص**

**وثائق جديدة (3)**
- `docs/gap-analysis-v3.md` — تحليل الفجوات الكامل بين النسخ السابقة و v3.0.0
- `docs/migration-v2-to-v3.md` — دليل الترقية
- `docs/architecture.md` — المعمارية الكاملة

**ملفات جذر**
- `LICENSE` (MIT © 2026 Waseem Alzobiri) · `CREDITS.md` · `CONTRIBUTING.md` · `.gitignore`
- `README.md` معاد كتابته بالكامل

### تغييرات (C Changed)

- **SKILL.md** — إعادة كتابة كاملة: v3.0.0، 5 محركات، 10 أقفال، 12 مبدأ، أوامر سريعة
- **workflows/intent-router.md** — إضافة قسم «المحركات» + 4 مسارات سريعة جديدة
- **verify_all.sh** — من 4 فحوص إلى **8 فحوص**

### إصلاحات (F Fixed)

- **333 رابطًا داخليًا مكسورًا → 0**
  - تحديث مراجع بُنى v1 (`agents/NN-*.md`, `state/*.md`, `templates/*.md`) إلى مساراتها الحالية
  - تطبيع المراجع المختصرة إلى مسارات كاملة من جذر المستودع
  - تحويل مراجع المجلدات (`protocols.md`, `specs.md`) إلى مراجع مجلد
- تكرار المحتوى بين النسخ السابقة (نسخة `vox/` مزدوجة + مجلد مكرر بالعربية) — **دُمج مرة واحدة**
- تضارب قواعد النص بين النسخ التجارية — **حُسم: البرومبتات بالإنجليزية دائمًا**

### قرارات محسومة

| التضارب | القرار |
|---|---|
| لغة البرومبتات (عربي vs إنجليزي) | **الإنجليزية دائمًا** — أدق للنماذج |
| بُنى المجلدات المتضاربة | **Agent Skills Standard** موحّد |
| قفل واحد (paper-engine) vs 8 أقفال (commercial) | **10 أقفال موحّدة** |
| 3 ملفات SKILL.md متضاربة | **SKILL.md واحد** في الجذر |

### المقارنة الكمية

| المقياس | v2.1.0 | v3.0.0 | النمو |
|---|---|---|---|
| ملفات المحتوى | 113 | ~180 | +59% |
| المراحل | 12 | 12 + 5 محركات | +42% |
| العوالم البصرية | 0 مقفلة | 10 بأقفال حرفية | ∞ |
| بوابات الجودة | 8 | 12 | +50% |
| المخططات | 13 | 23 | +77% |
| السكربتات | 5 | 9 | +80% |
| الأمثلة الحية | 2 | 4 | +100% |
| أدوات البحث | 0 | 5 | جديد |
| الروابط المكسورة | 333 | 0 | −100% |
| الفحوص | 4 | 8 | +100% |

### التوافق

**v3.0.0 إضافة فوقية (additive):** لا يحذف شيئًا من v2.x.
كل مشروع يعمل على v2.1.0 يعمل على v3.0.0 دون تعديل.
→ `docs/migration-v2-to-v3.md`

### الديون التقنية المعلنة

- لا يوجد وكيل تدقيق سردي مستقل (Story / Editorial QC)
- لا يوجد اختبار تكامل حقيقي متعدد الوكلاء
- محتوى M8b / M8c أقل عمقًا من باقي المراحل

### الاعتماد

**صُمّم وبُني بواسطة Waseem Alzobiri** · MIT
