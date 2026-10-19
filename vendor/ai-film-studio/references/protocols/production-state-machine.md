---
name: production-state-machine
description: |
  المرجع الرسمي الوحيد لتعريف مراحل الإنتاج الـ 12 (M0–M11) و sub-workflows الـ 31.
  أي تضارب مع هذا الملف = خطأ يُسجَّل في issue ويُصلَح.
  Source of truth: filesystem في `workflows/M*.md` (يحدد ما هو موجود فعلاً).
tier: 3
when_to_load: "عند بدء مشروع، عند شك في رقم مرحلة، عند تضارب بين ملفين"
---

# Production State Machine — AI Film Studio v2.0.2

> **هذا الملف هو المرجع الرسمي الوحيد لتعريف المراحل والـ gates.**
> أي ملف آخر (SKILL.md، M9a، README، إلخ) يشير إلى المراحل يجب أن يتطابق مع هذا الملف.
> **Source of truth تشغيلي:** `workflows/M*.md` (filesystem).

---

## 1. النموذج الرسمي: 12 مرحلة رئيسية، 31 sub-workflow

| المرحلة | الاسم | Workflows | الوصف |
|---|---|---|---|
| **M0** | Intake | `workflows/M0-intake.md` | استقبال الطلب + تحليل ثلاثي + 3 أسئلة |
| **M1** | Research + Concept | `workflows/M1a-creative-direction.md`، `workflows/M1b-concept-expansion.md`، `workflows/M1c-research-lab.md` | البحث + توسعة الفكرة + Concept Deck |
| **M2** | Narrative Architecture | `workflows/M2-narrative.md` | البنية السردية + المشاهد + السكريبت + Character Arc |
| **M3** | Shot Architecture | `workflows/M3a-shot-design.md`، `workflows/M3b-shot-list.md` | هندسة اللقطات + Shot List + Blocking + Edit Handles |
| **M4** | Continuity + Transitions | `workflows/M4a-continuity.md`، `workflows/M4b-character-world.md`، `workflows/M4c-continuity-qc.md`، `workflows/M4d-transitions.md` | Continuity Bible + Frame Chain + Character/World Bible + QC + Transitions Map |
| **M5** | Graphics + Text | `workflows/M5a-graphics.md`، `workflows/M5b-text-motion.md` | استراتيجية النص + Typography + Text Preservation |
| **M6** | Audio | `workflows/M6-audio.md`، `workflows/M6b-sound-design.md`، `workflows/M6c-dialogue-lipsync.md` | الطبقات الصوتية + Sound Design + Lip-Sync |
| **M7** | Image Prompts | `workflows/M7a-prompt-architecture.md`، `workflows/M7b-image-prompts.md` | 10 طبقات A-J + Image Prompts Package |
| **M8** | Motion Prompts | `workflows/M8a-motion-prompts.md`، `workflows/M8b-motion-direction.md`، `workflows/M8c-animation-ready.md`، `workflows/M8d-motion-graphics.md` | Motion Prompts Package + Motion Direction + Animation Ready + Motion Graphics |
| **M9** | Quality + Orchestration | `workflows/M9a-executive-producer.md`، `workflows/M9b-quality-gates.md`، `workflows/M9c-preflight.md`، `workflows/M9d-localization.md` | Executive Producer + 8 Quality Gates + Pre-flight + Localization |
| **M10** | Pre-Production Review | `workflows/M10a-production-architecture.md`، `workflows/M10b-hybrid-assembly.md`، `workflows/M10c-edit-color.md` | مراجعة ما قبل الإنتاج + Assembly Hybrid + Edit/Color |
| **M11** | Final Delivery | `workflows/M11a-reference-analyst.md`، `workflows/M11b-visual-research.md` | تحليل المراجع + البحث البصري + تسليم الحزم الخمس |

**إجمالي:** 12 مرحلة × 31 workflow.

---

## 2. الـ State Machine الرئيسي

```text
M0 → M1 → M2 → M3 → M4 → M4c(QC) → APPROVAL → M5 → M6 → M7 → M8 → M9c(Preflight) → M10 → M11
                                  │                                                  │
                                  └─ REJECT → أي مرحلة سابقة حسب سبب الرفض            └─ M9(EP)→ M9b(Gates)→ M9d(Localization)
```

**M4c (Continuity QC) إلزامي** بعد M4 وقبل APPROVAL في أي مشروع متعدد اللقطات (SCENE، FULL).
M4c **اختياري** للمشاريع المستقلة (SINGLE_PROMPT، IMAGE_GENERATION، IMAGE_TO_VIDEO).

---

## 3. Quality Gates (نموذج v2.0.2 الموحّد)

> **عدد الـ gates: 8** (G0–G8) للنظام end-to-end.
> الـ sub-gates (G1.5، G3.1، G3.2) ليست gates مستقلة بل sub-tests داخل gate رئيسي.

| Gate | الاسم | بعد المرحلة | Hard/Soft | المسؤول |
|---|---|---|---|---|
| **G0** | Intake Clarity | M0 | Soft | M9a (EP) |
| **G1** | Idea Quality | M1 | Soft | M1c (Research Lab) |
| **G2** | Narrative Quality | M2 | Soft | M2 (Narrative) |
| **G3** | Continuity Quality | M4 (M4a + M4b + M4c) | Soft | M4a (Continuity Supervisor) |
| **G4** | **Prompt Quality (10-Layer A-J)** | M7 + M8 | **HARD** | M7a (Prompt Architecture) + M9b (QG Controller) |
| **G5** | Transition Quality | M4d | Soft | M4d (Transitions) |
| **G6** | Text Quality | M5 (M5a + M5b) | Soft (critical على G6.4 Brand Logo) | M5a (Graphics) |
| **G7** | Audio Quality | M6 (M6a + M6b + M6c) | Soft | M6 (Audio) |
| **G8** | **Master Quality (5 Output Files)** | M10 + M11 | **HARD** | M9a (EP) + M9b (QG Controller) |

**Hard Gates: G4 و G8.** أي critical failure = مشروع مرفوض، لا استثناءات.

---

## 4. Approval Rule

**اعتماد بشري إلزامي واحد** بعد M4c (Continuity QC) وقبل بدء M5. هذا الـ gate يُسمى G-APPROVAL.

اعتمادات إضافية **اختيارية** فقط للحالات:
- Brand/legal/rights حساسة.
- قرار غير قابل للعكس (مثل: حذف شخصية من Continuity Bible).
- Scope expansion (مثل: زيادة عدد المشاهد بعد بدء M7).

**لا اعتمادات** للقرارات الإبداعية العادية (لون، زاوية كاميرا، نص حوار).

---

## 5. Repair / Revalidate Loop

```
أي FAIL في M5..M11:
  ↓
DIAGNOSE (حدد Gate + السبب + المتغير الأصغر)
  ↓
REPAIR (طبّق الحد الأدنى من التغيير على المتغير)
  ↓
REVALIDATE (أعد فحص الـ Gate فقط)
  ↓
PASS → استأنف من نقطة الفشل
```

**القاعدة:** لا تُعد كتابة prompt كاملاً. أصلح أصغر متغير مسؤول عن الفشل.

---

## 6. Transition Record (لكل انتقال مرحلة)

كل انتقال مرحلة يُسجَّل في `schemas/state/decision-log.md` بـ:
- `from`، `to`، `timestamp`، `reason`، `operator`، `artifacts`، `approval_id`، `state_version`.

---

## 7. Backward Compatibility

- أي مشروع v1.x يعمل كما هو (M0..M11 من قِبل الـ LLM interpreter).
- v1.x ما زال يستخدم M13 في CHANGELOG التاريخي — هذا مقصود ولا يُعدَّل.
- هذا الملف (v2.0.2) هو المرجع للإصدارات v2.0+.

---

## 8. Source of Truth Resolution

عند التضارب بين ملفين:
1. **filesystem** (`workflows/M*.md`) يحدد ما هو موجود.
2. **production-state-machine.md** (هذا الملف) يحدد كيف يُسمّى.
3. أي ملف آخر (SKILL.md، M9a، README) يتبع (1) و(2).

**عند اكتشاف تضارب:** سجّل issue، أصلح الملف المخالف، لا تُعد كتابة هذا الملف.
