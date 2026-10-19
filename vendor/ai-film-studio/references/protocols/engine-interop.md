---
name: engine-interop
description: |
  بروتوكول التكامل بين المحركات (E1–E5) والعمود الفقري (M0–M11): جدول التكافؤ الكامل،
  قواعد الاستدعاء، من يملك القرار عند التعارض، بوابات الجودة المزدوجة،
  ونقل الحالة بين المحرك والمراحل.
tier: 3
when_to_load: "عند تشغيل أي محرك، أو عند الحاجة لمرحلة M من داخل محرك"
---

# Engine Interop — التكامل بين المحركات والمراحل

## 1. العلاقة البنيوية

```
        ┌─────────────────────────────────────────┐
        │   ENGINES (E1–E5)                       │  ← رحلة المستخدم
        │   عقد تشغيل · توقف · إرشاد تنفيذ        │
        └──────────────┬──────────────────────────┘
                       │ يستدعي
                       ▼
        ┌─────────────────────────────────────────┐
        │   WORKFLOWS (M0–M11 · 31 workflow)      │  ← العمود الفقري
        │   تخصص · بوابات · مواصفات               │
        └──────────────┬──────────────────────────┘
                       │ يستدعي
                       ▼
        ┌─────────────────────────────────────────┐
        │   SPEC / SCHEMAS / STYLES / QUALITY     │  ← tier 3
        └─────────────────────────────────────────┘
```

**المحرك لا يستبدل المرحلة — يستدعيها.**

---

## 2. جدول التكافؤ الكامل

### E1 — Documentary Engine

| حالة E1 | تكافئ M | الملاحظة |
|---|---|---|
| 0 (إقلاع) | — | تحميل الأصول فقط |
| 1–3 (نيش/أفكار/مدة) | **M0 + M1b + M1c** | الاستقبال + توسيع المفهوم + بحث |
| 4 (سكربت) | **M2-narrative** | تطبَّق قواعد `references/knowledge/narrative-writing-dna.md` |
| 5 (صوت) | **M6-audio** | + `references/knowledge/voice-system.md` |
| 6 (Beats) | **M3b-shot-list** | + `references/specs/beat-architecture.md` |
| 7 (برومبتات صور) | **M7b-image-prompts** | + LOCK A حرفيًا |
| 8 (UVP) | **M8a-motion-prompts** | القالب من `styles/locks/` |
| 9 (ثامبنيل) | **M5a + M11b** | + `references/specs/thumbnail-dna.md` |

### E2 — Commercial Engine

| مرحلة E2 | تكافئ M | الملاحظة |
|---|---|---|
| 0 Brief | **M0-intake** | Brief 12 حقلًا |
| 1 Ideation | **M1a + M1b** | + `references/specs/idea-engine.md` |
| 2 Visual World | **M4b + M11a** | + اختيار القفل من `styles/` |
| 3 Beats | **M2 + M3b** | + `references/specs/beat-architecture.md` |
| 4 Shot Cards | **M3a** | + `references/specs/shot-contract.md` |
| 5 Product Ref | **M11a / M4b** | IMG-00 + Anchor |
| 6 Prompts | **M7b + M8a** | + `references/specs/model-dialects.md` |
| 7 Sound | **M6 + M6b** | + `references/specs/audio-decision-tree.md` |
| 8 Edit | **M10b + M10c** | + `references/specs/platform-specs.md` |
| 9 Gates | **M9b + M9c** | + `quality/gates-extended.md` |

### E3 — Hybrid Commercial

| مرحلة E3 | تكافئ M |
|---|---|
| 0 إقلاع | — |
| 1 Discovery | **M0** |
| 2 فكرة + منتج | **M1a + M11a** |
| 3 Treatment | **M2 + M1a** |
| 4 Beats | **M2 + M3b** |
| 5 Product Ref | **M11a** |
| 6 صور + مشاهد | **M7b + M8a** (بقفلين A و B) |
| 7 صوت ونص | **M6 + M5b** |
| 8 QA | **M9b + M9c** |

### E4 — Series Engine

| مرحلة E4 | تكافئ M |
|---|---|
| خطة السلسلة | **M1c-research-lab** |
| كل حلقة | **E1 أو E2 أو E3 كاملة** |
| توقيع القناة | **M4b-character-world** + `references/specs/entity-ledger.md` |

### E5 — Bulk Pipeline

| مرحلة E5 | تكافئ M |
|---|---|
| أ (توليد صور) | — (إرشاد للمستخدم) |
| ب (توليد فيديو) | **M8a** |
| ج (مونتاج) | **M10b + M10c** |

---

## 3. قواعد الاستدعاء

### 3.1 متى يستدعي المحرك مرحلة M؟

```
المحرك يحتاج مخرجًا متخصصًا
        ↓
هل المرحلة M المقابلة تقدّم مواصفة أدق؟
   ├─ نعم → استدعها، ثم طبّق مواصفتها
   └─ لا  → اكتفِ بقواعد المحرك
```

**مثال:** E2 مرحلة 6 (Prompts) تستدعي **M7b** للحصول على الترتيب الإلزامي
للحقول الإحدى عشر، ثم تطبّق قواعد E2 (Anchor، القفل، لهجة النموذج).

### 3.2 متى تعود المرحلة M إلى محرك؟

عندما يكتشف الـ workflow أن الطلب **ليس** في نطاقه:

| الاكتشاف | الإحالة |
|---|---|
| M0 يكتشف منتجًا واضحًا + طلب إعلان | → `E2` أو `E3` |
| M0 يكتشف طلبًا وثائقيًا/قناة | → `E1` |
| M7b يكتشف أن المشروع سلسلة | → `E4` |
| أي مرحلة تكتشف أن المستخدم في مرحلة التنفيذ | → `E5` |

---

## 4. من يملك القرار عند التعارض؟

### التسلسل الهرمي (Source of Truth)

```
1. القواعد الصارمة في SKILL.md (المبادئ الـ 12)
        ↓
2. عقد تشغيل المحرك (E*) — فيما يخص التوقف والتسليم
        ↓
3. مواصفة المرحلة (M*) — فيما يخص جودة المخرج المتخصص
        ↓
4. المرجع المتخصص (references/specs/*)
        ↓
5. القالب (schemas/*)
```

### أمثلة محلولة

| التعارض | الحل | لماذا |
|---|---|---|
| E1 يقول "توقف بعد كل حالة" vs M2 يقول "أكمل السرد" | **E1** | عقد التسليم يملكه المحرك |
| E2 يقول "120–220 كلمة" vs M7b يقول "10 طبقات A–J" | **الاثنان** | الطول من E2، الترتيب من M7b |
| القفل يقول "tan and ink" vs المستخدم طلب أزرق | **المستخدم** | الطلب الصريح يعلو |
| `beat-architecture` vs `M3b` في عدد اللقطات | **`beat-architecture`** | المرجع المتخصص أدق |

---

## 5. بوابات الجودة المزدوجة

المشروع الذي يمر بمحرك يخضع لـ **مستويين**:

| المستوى | البوابة | من يطبّقها |
|---|---|---|
| **المحرك** | G9 (Script) · G10 (Beats) · G11 (Product) · G12 (Platform) · G13 (Series) | المحرك، عند كل تسليم |
| **العمود الفقري** | G0–G8 (خصوصًا **G4 Hard** و **G8 Hard**) | المرحلة M المستدعاة |

**القاعدة:** أي FAIL في **G4** أو **G8** يحجب التسليم — حتى لو اجتازت بوابات المحرك.

→ `quality/gates-extended.md`

---

## 6. نقل الحالة (State Handoff)

عند انتقال المشروع من محرك إلى مرحلة أو العكس، تُسلَّم هذه الحزمة الدنيا:

```
ENGINE STATE HANDOFF
─────────────────────────────────
engine_id           E1 / E2 / E3 / E4 / E5
current_state       رقم الحالة أو المرحلة
style_lock          LOCK-[X] (+ LOCK-[Y] في الهجين)
palette             {PALETTE} المستبدلة
product_anchor      [الجملة الحرفية] إن وُجد
truth_tier          T1 / T2 / T3 / T4
entity_ledger       [قائمة الكيانات المقفولة]
beat_table          [مسار الجدول]
shot_cards          [مسار البطاقات]
duration / aspect   [المدة] / [النسبة]
target_platform     [المنصة]
assumptions         CONFIRMED / PROPOSED / NEEDS REF
```

→ يُخزَّن في `schemas/state/session-checkpoint.md`

---

## 7. منع الازدواجية

| المحرك | لا يكرر | السبب |
|---|---|---|
| E1 | لا يعيد صياغة LOCK A | القفل مسجّل في `styles/locks/` |
| E2 | لا يعيد اختراع ترتيب البرومبت | موجود في `M7b` + `references/specs/model-dialects.md` |
| E3 | لا يكرر قواعد E1 أو E2 | يحيل إليهما |
| E4 | لا ينتج محتوى | يستدعي E1/E2/E3 |
| E5 | لا يعيد كتابة البرومبتات | يستهلك ما أنتجه E1/E2 |

---

## 8. مسار القرار السريع

```
طلب جديد
   ↓
intent-router.md
   ↓
├─ shortcut → workflows/shortcuts/*
├─ محرك     → workflows/engines/E*  → يستدعي M* عند الحاجة
└─ M-Stage  → workflows/M*          → قد يحيل إلى محرك
```

---

## Cross-Reference

- `workflows/intent-router.md` — التوجيه
- `references/protocols/orchestration-runtime.md` — الـ executable spec للمسارات
- `references/protocols/production-state-machine.md` — نموذج المراحل الرسمي
- `quality/gates-extended.md` — البوابات المزدوجة
