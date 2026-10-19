---
name: ai-film-studio
description: |
  AI Film Studio v3.2.0 — نظام إنتاج مرئي متكامل بالذكاء الاصطناعي (فيلم + إعلان + وثائقي + موشن).
  يحوّل فكرة بسيطة إلى حزمة إنتاج كاملة: Concept + Script + Shot List + Beats + Prompts (10-Layer A-J)
  + Audio + Edit Sheet + Delivery Pack.
  يحتوي: 12 مرحلة إنتاج (M0–M11 / 32 workflow)، 5 محركات متخصصة (E1–E5)، 11 عوالم بصرية بأقفال نصية
  حرفية (LOCK A–K)، 12 بوابة جودة، أدوات بحث وتحقق، وذاكرة مشروع مع حلّ تضارب بـ 6 أنواع.
  يُستخدم للأفلام القصيرة، الإعلانات، Brand Films، الوثائقيات، فيديوهات الـ essay، الموشن جرافيك،
  الشورتس، والقنوات بدون وجه (faceless channels).
license: MIT
---

# AI Film Studio v3.2.0

> **نقطة الدخول.** اقرأ هذا الملف، ثم اذهب إلى `workflows/intent-router.md` فورًا.

## الفلسفة

> **"كلما كان المستخدم أقل خبرة، يجب أن تكون المهارة أكثر قدرة على تعويض هذه الخبرة داخليًا."**
>
> **"البرومبت هو الخطوة رقم 10، وليس رقم 1."**

المهارة تُحاكي **استوديو إنتاج حقيقي**: 31 تخصصًا عبر 12 مرحلة (M0–M11)، **5 محركات متخصصة**،
**11 عوالم بصرية بأقفال نصية حرفية**، و **12 بوابة جودة**.

## التوجيه السريع (اختر واحدًا)

| إذا كان طلبك... | المسار | الوقت |
|---|---|---|
| برومبت واحد / صورة / تحريك صورة / لبسِنك | `workflows/shortcuts/` | 2–15 د |
| ثامبنيل لفيديو | `workflows/shortcuts/thumbnail.md` | 5 د |
| **وثائقي / فيديو essay / قناة بدون وجه** | `workflows/engines/E1-documentary-engine.md` | 20–45 د |
| **إعلان منتج / حملة / brand film** | `workflows/engines/E2-commercial-engine.md` | 15–40 د |
| **إعلان بأسلوب وثائقي/كولاج** (هجين) | `workflows/engines/E3-hybrid-commercial.md` | 25–50 د |
| **سلسلة أو قناة كاملة** | `workflows/engines/E4-series-engine.md` | per episode |
| **توليد صور بالجملة + تجميع** | `workflows/engines/E5-bulk-production-pipeline.md` | 10 د |
| مشهد متعدد اللقطات | `M0-intake` → `M3` (`M4c` إلزامي) | 30 د |
| فيلم قصير / فيلم سردي كامل | `M0-intake` → `M11` | 90 د |

## بنية المستودع (Progressive Disclosure)

```
tier 1 — يُحمَّل دائمًا (≤ 8KB)
  ├─ SKILL.md / README.md / CHANGELOG.md

tier 2 — يُحمَّل عند بدء مشروع
  ├─ workflows/intent-router.md     ← نقطة التوجيه
  ├─ workflows/M0..M11/             ← 12 مرحلة / 32 workflow (العمود الفقري)
  ├─ workflows/engines/E1..E5/      ← 5 محركات متخصصة (وثائقي، إعلان، هجين، سلسلة، جملة)
  └─ workflows/shortcuts/           ← 11 مسارًا سريعًا

tier 3 — يُحمَّل عند الحاجة المتخصصة
  ├─ styles/                        ← 11 عوالم بصرية + أقفال حرفية (LOCK A–K)
  ├─ references/protocols/          ← 10 بروتوكولات تشغيل
  ├─ references/specs/              ← 21 مواصفة تقنية
  ├─ references/knowledge/          ← 10 معارف متخصصة
  ├─ references/research/           ← 5 أدوات بحث وتحقق
  ├─ schemas/                       ← 23 هيكل بيانات / قالب مخرج
  ├─ quality/                       ← 12 بوابة جودة + قوائم فحص
  ├─ examples/                      ← 4 أمثلة حية كاملة
  └─ scripts/                       ← أدوات فحص + Prompt Compiler قابلة للتنفيذ
```

**قاعدة التحميل:** لا تُحمَّل tier 2/3 إلا بعد أن يُحدد `workflows/intent-router.md` المسار.

## العمود الفقري — 12 مرحلة / 32 workflow

| المرحلة | الاسم | الـ Workflows | الجودة |
|---|---|---|---|
| **M0** | Intake | `M0-intake` | G0 |
| **M1** | Research + Concept | `M1a` `M1b` `M1c` | G1 |
| **M2** | Narrative | `M2-narrative` | G2 |
| **M3** | Shot Architecture | `M3a` `M3b` | G3.1 |
| **M4** | Continuity + Transitions | `M4a` `M4b` `M4c` `M4d` | G3.2, G5 |
| **M5** | Graphics + Text | `M5a` `M5b` | G6 |
| **M6** | Audio | `M6` `M6b` `M6c` | G7 |
| **M7** | Image Prompts | `M7a` `M7b` | **G4 (Hard)** |
| **M8** | Motion Prompts | `M8a` `M8b` `M8c` `M8d` | **G4 (Hard)** |
| **M9** | Quality + Orchestration | `M9a` `M9b` `M9c` `M9d` | **G4, G8 (Hard)** |
| **M10** | Pre-Production Review | `M10a` `M10b` `M10c` | **G8 (Hard)** |
| **M11** | Final Delivery | `M11a` `M11b` | Final |

## المحركات الخمسة (Engines)

المحركات **لا تستبدل** M0–M11 — هي **طبقات تنظيم وتسليم** فوقها، لكل منها عقد تشغيل خاص:

| المحرك | الملف | العقد | متى |
|---|---|---|---|
| **E1** | `workflows/engines/E1-documentary-engine.md` | آلة حالات 9 خطوات، توقف بعد كل حالة | وثائقي / essay / faceless |
| **E2** | `workflows/engines/E2-commercial-engine.md` | 10 مراحل، طاقم 9 أدوار | إعلان منتج / حملة |
| **E3** | `workflows/engines/E3-hybrid-commercial.md` | أسلوب هجين وثائقي وتجاري | إعلان بسرد وثائقي |
| **E4** | `workflows/engines/E4-series-engine.md` | خطة سلسلة + توقيع قناة مقفول | قناة / موسم / مجموعة حلقات |
| **E5** | `workflows/engines/E5-bulk-production-pipeline.md` | ملف txt + Universal Video Prompt | توليد بالجملة |

> المصدر المنهجي للمراحل: `references/protocols/production-state-machine.md`
> الـ Orchestration Executable Spec: `references/protocols/orchestration-runtime.md`
> التكامل بين المحركات والمراحل: `references/protocols/engine-interop.md`

## العوالم البصرية (Style Locks) — 10 أقفال

كل عالم = **قفل نصي يُنسخ حرفيًا** في كل برومبت. إعادة الصياغة تكسر الثبات بين 20 لقطة.

| القفل | العالم | الاستخدام |
|---|---|---|
| **A** | Documentary Archive Collage | توقيع VOX — وثائقي، essay |
| **B** | Commercial Craft Collage | **الافتراضي للمنتجات** |
| **C** | Paper Noir Luxury | عطور، ساعات، فخامة |
| **D** | Pop Cutout Playground | سناكس، مشروبات، شباب |
| **E** | Miniature Tabletop Cinematic | تقنية، أجهزة، سيارات |
| **F** | Photoreal Studio | واقعية كاملة بلا ورق |
| **G** | Mixed Media Editorial | مجلات، أزياء، ثقافة |
| **H** | Tactile Clay Diorama | طين/صلصال، سناكس، أطفال |
| **I** | Flat Vector Explainer | **VOX المسطح**: infographic، بيانات، شرح |
| **J** | Arabic Calligraphic | هوية عربية، خط، تراث |

→ `styles/index.md` لقرار الاختيار · `styles/locks/*.txt` للأقفال الحرفية
→ بروتوكول الأقفال: `references/protocols/style-lock-protocol.md`

## المبادئ المؤسِّسة (12 مبدأ)

1. **الفكرة قبل الجمال** — لا تكتب برومبتًا قبل تثبيت الفكرة والوعد.
2. **جودة الـ Prompt أهم من الاختصار** — لا تختصر لتوفير الوقت.
3. **Identity String حرفي** — لا تُعد صياغة صفات الشخصية/المنتج أبدًا.
4. **المنتج مقدّس** — الشكل والنسب واللون والشعار لا تتغير في أي ظهور.
5. **Reference Pack إلزامي** — كل شخصية/مخلوق/منتج/مكان متكرر له anchor معتمد، وكل `@imageN` له دور وخريطة لقطة قبل الـStoryboard.
6. **Frame Chain إلزامي** — `SC(N+1)_START = SC(N)_END` بصريًا.
7. **النص في الفيديو = Single Locked Visual Plane** — طبقة واحدة محكومة.
8. **الصوت يصلح الصورة** — خطط للصوت مبكرًا، لا في النهاية.
9. **كل ثانية تُدفع ثمنها** — Beat بلا وظيفة يُحذف حتى لو كان جميلًا.
10. **الصمت قبل الذروة** — التباين هو ما يجعل الذروة ذروة.
11. **الحقيقة مقدسة** — لا اختراع أسماء أو تواريخ أو أرقام أو ادعاءات.
12. **Hard Gates (G4, G8) لا تُتجاوز** — أي FAIL يحجب التسليم.
13. **التفكير داخلي دائمًا** — المستخدم يرى المخرجات النظيفة فقط.

## المرجعيات الحرجة

| الحاجة | الملف |
|---|---|
| Prompt Compiler التنفيذي وخريطة `@ImageN` | `scripts/prompt_compiler.py` + `schemas/prompt-compiler-input.schema.json` |
| 10 طبقات Prompt Architecture (A–J) | `references/specs/prompt-architecture.md` |
| حساب الـ Beats ومنحنى الطاقة | `references/specs/beat-architecture.md` |
| لهجات النماذج (12 عائلة) | `references/specs/model-dialects.md` |
| مستويات حقيقة المنتج (T1–T4) | `references/specs/product-truth.md` |
| سجل الكيانات (Entity Ledger) | `references/specs/entity-ledger.md` |
| حمض الثامبنيل | `references/specs/thumbnail-dna.md` |
| مواصفات المنصات والمناطق الآمنة | `references/specs/platform-specs.md` |
| محرك الأفكار (12 عدسة جنون) | `references/specs/idea-engine.md` |
| DNA الكتابة السردية | `references/knowledge/narrative-writing-dna.md` |
| نظام التعليق الصوتي | `references/knowledge/voice-system.md` |
| أدوات البحث والتحقق | `references/research/` |
| حل تضارب الذاكرة | `references/knowledge/memory-conflict-contract.md` |
| أنماط الفشل | `references/knowledge/failure-modes.md` |

## عقد التشغيل والتفاعل

**طبقة الإخراج العليا إلزامية:** `references/protocols/user-facing-production-flow.md` هي المرجع الحاكم لما يراه المستخدم، وتعلو على تفاصيل الوكلاء والمراحل.

للاستخدام الاحترافي داخل الوكلاء، طبّق هذا التسلسل قبل التوليد:

1. **استخرج النية** في `schemas/generation-intent.schema.json`، وحدد نوع المشروع ونطاقه والقيود ووضع الموافقة.
2. **وجّه بأقل مسار كافٍ** عبر `workflows/intent-router.md`؛ لا تشغّل M0–M11 لطلب prompt أو لقطة واحدة.
3. **خطط قبل البرومبت**: ثبّت الـBrief والـBeats، ثم أنشئ `workflows/adaptive-production-sheet.md` بورقة مشاهد/لقطات متكيفة مع المدة والنوع، ثم نفّذ `workflows/M4e-reference-orchestration.md` لبناء الـanchors و`shot_reference_map`، ثم الهوية البصرية وسجل الكيانات والاستمرارية وبطاقات اللقطات.
4. **اختر المزود صراحةً** عبر `workflows/provider-routing.md` وسجل القدرة والنسخة والدليل والبدائل؛ اعتبر القدرة المجهولة غير مدعومة.
5. **سلّم عبر عقود قابلة للتتبع** في `schemas/project-manifest.schema.json` و`schemas/artifact-record.schema.json` مع IDs وتبعيات وحالة ومصدر.
6. **أصلح أول فشل فقط**: أعد تشغيل البوابة المتأثرة وما بعدها، ولا تعِد توليد مخرجات معتمدة بلا سبب مسجل.
7. **صنّف النتيجة بصدق**: `candidate` أو `qualified` أو `not-yet-verified`؛ نجاح فحص المستندات لا يثبت صلاحية الوسائط ما لم تُفحص فعليًا.

**ترتيب الإخراج للمشاريع متعددة المشاهد:** فهم مختصر وأسئلة ضرورية → رؤية مختصرة → **ورقة إنتاج متكيفة مع المدة والنوع قابلة للتصدير CSV** → **حزمة المرجعيات واعتمادها/قفلها** → Storyboard → اعتماد → **Prompt كامل واحد لكل فريم مع خريطة `@image`** → اختيار التوليد الخارجي/داخل المنصة → **Prompt كامل واحد لكل لقطة** → الصوت والسكريبت عند الحاجة.

التفاصيل التشغيلية: `references/protocols/agent-protocol.md` · تدفق المستخدم: `references/protocols/user-facing-production-flow.md` · عقد الـStoryboard: `schemas/storyboard.md` · عقد الفريم: `schemas/frame-prompt-contract.md` · سجل المزودين: `references/provider-registry.yaml`.

## أوامر سريعة

```bash
python3 scripts/verify_structure.py     # البنية + YAML (tier 1)
python3 scripts/verify_styles.py        # سلامة الأقفال النصية الأحد عشر
python3 scripts/verify_vox.py           # المحركات الخمسة + المسارات الجديدة
python3 scripts/verify_functional.py    # 95/95 وظيفي (3 أنواع + 4 fixtures)
python3 scripts/verify_motion.py        # 46/46 مسار الموشن جرافيك
python3 scripts/verify_example.py       # 29/29 الأمثلة الحية
python3 scripts/prompt_lint.py          # فحص أي برومبت قبل التسليم
bash    scripts/verify_all.sh           # الكل (9 فحوص)
```

## متى لا تستخدم هذه المهارة

- ❌ صورة ثابتة بسيطة (استخدم image generation مباشرة)
- ❌ ترجمة/صياغة نصوص بحتة
- ❌ سؤال تقني عن نموذج (ارجع لـ `references/specs/model-matrix.md`)
- ❌ مشروع يحتاج أكثر من ساعة حوسبة بدون automation

## الاعتماد والتوافق

- **License:** MIT · **Version:** 3.2.0
- **التصميم والبناء:** Waseem Alzobiri
- **التوافق:** Claude Sonnet/Opus, GPT-4+, Gemini Pro/Ultra — أي وكيل يدعم Agent Skills Standard
- **الحالة:** Production-ready
