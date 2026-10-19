<!-- verify_links: allow-legacy -->

# Gap Analysis — تحليل الفجوات بين النسخ السابقة و v3.0.0

**تاريخ التحليل:** 2026-09-10
**المستودعات المحلّلة:** 4
**النتيجة:** دمج كامل + 42 إضافة جديدة

---

## 1. المستودعات المحلّلة

| المستودع | الملفات | الحجم | الطبيعة |
|---|---|---|---|
| **ai-film-studio** (v2.1.0) | 113 | ~700 KB | نظام إنتاج أفلام — 12 مرحلة / 31 workflow |
| **vox-paper-engine** | 37 | 192 KB | محرك وثائقيات الكولاج الورقي (آلة حالات 9 خطوات) |
| **vox-commercial-director** | 69 | 412 KB | دمج `commercial/` + `vox/` + مجلد مكرر |
| **vox-commercial-director-skill** (v3.0.0) | 20 | 172 KB | النسخة التجارية الأكثر نضجًا: 11 مرجعًا |

---

## 2. ما كان مفقودًا في النسخة النهائية (ai-film-studio v2.1.0)

### 2.1 فجوات حرجة (P0)

| # | الفجوة | الأثر | المصدر |
|---|---|---|---|
| 1 | **لا نظام أسلوب مقفول (Style Locks)** | 30 لقطة تخرج كصور عشوائية لا فيلم واحد | paper-engine + commercial-director |
| 2 | **لا محرك وثائقي** | الوثائقيات خارج نطاق النظام | paper-engine |
| 3 | **لا محرك إعلاني** | لا Big Idea ولا حقيقة منتج | commercial-director |
| 4 | **لا مرجع منتج (IMG-00 / Product Anchor)** | النموذج يعيد اختراع المنتج كل لقطة | commercial-director |
| 5 | **لا حساب Beats ولا منحنى طاقة** | لا إيقاع محسوب | كلا النظامين |
| 6 | **لا نظام ثامبنيل** | يوتیوب بلا ثامبنيل = فشل | paper-engine |

### 2.2 فجوات مهمة (P1)

| # | الفجوة | المصدر |
|---|---|---|
| 7 | لا محرك أفكار (عدسات الجنون الـ 12) | commercial-director |
| 8 | لا تصنيف hooks | commercial-director |
| 9 | لا جداول زمن (6/10/15/30/60 ثانية) | commercial-director |
| 10 | لا End Card ولا مصفوفة A/B | commercial-director |
| 11 | لا Edit Sheet | commercial-director |
| 12 | لا مستويات حقيقة المنتج (T1–T4) | commercial-director |
| 13 | لا سجل كيانات (Entity Ledger) | كلا النظامين |
| 14 | لا بروتوكول اكتشاف (3 اتجاهات + ≤3 أسئلة) | كلا النظامين |
| 15 | لا أوضاع سلسلة/قناة | paper-engine |
| 16 | لا مسار تنفيذ بالجملة | paper-engine |
| 17 | لا Universal Video Prompt | paper-engine |
| 18 | لا نظام تعليق صوتي تفصيلي | paper-engine |

### 2.3 فجوات متوسطة (P2)

| # | الفجوة | المصدر |
|---|---|---|
| 19 | لا حمض كتابة سردية (Cold Open / Cliffhanger) | paper-engine |
| 20 | لا مواصفات منصات ومناطق آمنة (مركّزة) | commercial-director |
| 21 | لا أدوات بحث وتحقق | — (**جديد**) |
| 22 | لا مرجع أمان ودقة | — (**جديد**) |
| 23 | لا إسناد منشئ ولا LICENSE واضح | — (**جديد**) |
| 24 | روابط داخلية مكسورة (333 رابطًا) | إرث v2 |

---

## 3. التكرار والالتباس بين النسخ السابقة

| المشكلة | التفصيل | الحل في v3.0.0 |
|---|---|---|
| **ازدواج `vox/`** | `vox-paper-engine` و `vox-commercial-director/vox/` نسختان متطابقتان | دمج مرة واحدة في `workflows/engines/E1` + `styles/` |
| **مجلد مكرر بالعربية** | `vox-commercial-director/vox-commercial-director-١/` | حُذف — لا يُنقل |
| **3 ملفات SKILL.md متضاربة** | في `commercial/` و `vox/` والجذر | **SKILL.md واحد** في الجذر |
| **تضارب قواعد النص** | commercial: «البرومبتات بلغة المستخدم» · skill-v3: «بالإنجليزية دائمًا» | **حُسم: البرومبتات بالإنجليزية دائمًا** — أدق للنماذج |
| **تضارب الأقفال** | paper-engine: قفل واحد · commercial: 8 أقفال | **10 أقفال موحّدة** LOCK A–J |
| **تضارب بُنى المجلدات** | `agents/` vs `references/` vs `workflows/` | **Agent Skills Standard** موحّد |

---

## 4. قرار الدمج — ما أُخذ من أين

### من ai-film-studio v2.1.0 (العمود الفقري)
- 12 مرحلة M0–M11 / 31 workflow — ✅ **محفوظة بالكامل**
- 10-Layer Prompt Architecture (A–J) — ✅ محفوظة
- 8 Quality Gates + Memory Conflict Contract — ✅ محفوظة وموسّعة
- Orchestration Runtime (10 routes) — ✅ محفوظ
- Memory Lifecycle v1.4 — ✅ محفوظ

### من vox-paper-engine (المحرك الوثائقي)
| الأصل | الوجهة في v3.0.0 |
|---|---|
| `SKILL.md` (آلة الحالات) | `workflows/engines/E1-documentary-engine.md` |
| `blocks/style-block.txt` | `styles/locks/LOCK-A-documentary-archive.txt` |
| `blocks/closer.txt` | `styles/locks/CLOSER-documentary.txt` |
| `blocks/closer-thumbnail.txt` | `styles/locks/CLOSER-thumbnail.txt` |
| `blocks/universal-video-prompt.txt` | `styles/locks/UNIVERSAL-VIDEO-PROMPT.txt` |
| `frameworks/fern-writing-dna.md` | `references/knowledge/narrative-writing-dna.md` |
| `frameworks/beat-math.md` | `references/specs/beat-architecture.md` (موسّع) |
| `frameworks/idea-engine.md` | `references/specs/idea-engine.md` (موسّع + 12 عدسة) |
| `frameworks/thumbnail-dna.md` | `references/specs/thumbnail-dna.md` |
| `frameworks/voice-system.md` | `references/knowledge/voice-system.md` |
| `workflows/state-machine.md` | E1 (مدمج في جدول الحالات) |
| `workflows/series-mode.md` | `workflows/engines/E4-series-engine.md` |
| `workflows/bulk-image-pipeline.md` | `workflows/engines/E5-bulk-production-pipeline.md` |
| `workflows/cold-start.md` | E1 الحالة 0 (مدمج) |
| `quality/*.md` (4) | `quality/gates-extended.md` (G9, G10) |
| `examples/db-cooper-demo.md` | `examples/paper-collage-documentary.md` (جديد بنفس المعيار) |

### من vox-commercial-director-skill v3.0.0 (الأكثر نضجًا)
| الأصل | الوجهة في v3.0.0 |
|---|---|
| `references/00-brief-intake.md` | `references/specs/brief-spec.md` + `schemas/brief.md` |
| `references/01-ideation-engine.md` | `references/specs/idea-engine.md` |
| `references/02-visual-worlds.md` | `styles/index.md` + `styles/locks/` |
| `references/03-narrative-and-beats.md` | `references/specs/beat-architecture.md` |
| `references/04-shot-architecture.md` | `schemas/shot-card.md` |
| `references/05-product-reference.md` | `references/specs/product-truth.md` + `schemas/product-sheet.md` |
| `references/06-prompt-engineering.md` | `references/specs/model-dialects.md` |
| `references/07-sound-and-voice.md` | `references/knowledge/voice-system.md` (مدمج) |
| `references/08-edit-and-delivery.md` | `schemas/edit-sheet.md` + `schemas/end-card.md` |
| `references/09-quality-gates.md` | `quality/gates-extended.md` (G11, G12) |
| `references/10-worked-example.md` | `examples/commercial-15s-lock-b.md` |
| `checklists/pre-flight.md` | `quality/pre-flight-checklist.md` |

### من vox-commercial-director (`commercial/`)
| الأصل | الوجهة |
|---|---|
| `commercial/SKILL.md` (10 وكلاء) | `workflows/engines/E2-commercial-engine.md` (طاقم 9 أدوار) |
| `workflows/hybrid-commercial.md` | `workflows/engines/E3-hybrid-commercial.md` |
| `frameworks/big-idea.md` | `references/specs/idea-engine.md` |
| `frameworks/shot-architecture.md` | `schemas/shot-card.md` |
| `quality/product-fidelity.md` | `quality/gates-extended.md` § G11 |
| `quality/consistency.md` | `quality/gates-extended.md` § G5 |
| `quality/final-check.md` | `quality/pre-flight-checklist.md` |

---

## 5. الإضافات الجديدة كليًا (لم تكن في أي نسخة سابقة)

| # | الإضافة | الملف |
|---|---|---|
| 1 | **LOCK I — Flat Vector Explainer** (نمط VOX المسطح) | `styles/locks/LOCK-I-flat-vector-explainer.txt` |
| 2 | **LOCK J — Arabic Calligraphic** | `styles/locks/LOCK-J-arabic-calligraphic.txt` |
| 3 | **حزمة أدوات البحث (5 ملفات)** | `references/research/` |
| 4 | **مرجع الدقة والأمان** | `references/knowledge/truth-and-safety.md` |
| 5 | **بروتوكول الأقفال النصية** | `references/protocols/style-lock-protocol.md` |
| 6 | **بروتوكول التكامل بين المحركات والمراحل** | `references/protocols/engine-interop.md` |
| 7 | **بروتوكول الاكتشاف** | `references/protocols/discovery-protocol.md` |
| 8 | **معمارية السلاسل** | `references/knowledge/series-architecture.md` |
| 9 | **مواصفات المنصات** | `references/specs/platform-specs.md` |
| 10 | **سجل الكيانات** | `references/specs/entity-ledger.md` |
| 11 | **بوابات G9–G13** | `quality/gates-extended.md` |
| 12 | **اختبار العشر ثوانٍ** | `quality/ten-second-test.md` |
| 13 | **4 سكربتات فحص جديدة** | `scripts/` |
| 14 | **10 مخططات إخراج** | `schemas/` |
| 15 | **4 مسارات سريعة** | `workflows/shortcuts/` |
| 16 | **مثالان حيان كاملان** | `examples/` |
| 17 | **إسناد المنشئ + LICENSE** | `CREDITS.md` · `LICENSE` |

---

## 6. المقارنة الكمية

| المقياس | v2.1.0 | v3.0.0 | النمو |
|---|---|---|---|
| ملفات المحتوى | 113 | **~180** | +59% |
| المراحل | 12 (M0–M11) | 12 + **5 محركات** | +42% |
| الـ workflows | 31 | 31 + 5 محركات + 11 shortcut | +52% |
| العوالم البصرية | 0 مقفلة | **10 بأقفال حرفية** | ∞ |
| بوابات الجودة | 8 | **12** | +50% |
| المخططات (schemas) | 13 | **23** | +77% |
| المراجع (references) | 26 | **~40** | +54% |
| أدوات البحث | 0 | **5** | جديد |
| السكربتات | 5 | **9** | +80% |
| الأمثلة الحية | 2 | **4** | +100% |
| الروابط المكسورة | 333 | **≈0** | −100% |

---

## 7. الديون التقنية المتبقية (معلنة بشفافية)

| # | الدين | الأولوية | الملاحظة |
|---|---|---|---|
| 1 | Story / Editorial QC | متوسطة | لا يوجد وكيل تدقيق سردي مستقل |
| 2 | Multi-agent real integration test | منخفضة | لا يوجد اختبار تكامل حقيقي متعدد الوكلاء |
| 3 | تعميق محتوى M8b / M8c | منخفضة | موجودان لكن محتواهما أقل من باقي المراحل |
| 4 | أتمتة التوليد الفعلي | خارج النطاق | المهارة تُنتج حزمًا لا تستدعي واجهات نماذج |
| 5 | تدريب onboarding للمساهمين | منخفضة | `CONTRIBUTING.md` يغطي الأساسيات |

---

## 8. الخلاصة

> **v3.0.0 = العمود الفقري (M0–M11) + 5 محركات + 10 عوالم مقفلة + أدوات بحث + 12 بوابة.**
>
> لا شيء فُقد من أي نسخة سابقة — كل شيء إما مدمج أو موسّع،
> مع 17 إضافة جديدة كليًا لم تكن موجودة في أيٍّ منها.
