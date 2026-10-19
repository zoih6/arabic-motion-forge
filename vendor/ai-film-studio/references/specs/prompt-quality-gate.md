---
name: prompt-quality-gate
description: |
  Prompt Quality Gate — AI Film Studio v2.1.0.
  Hard Gate (G4 في v2.0.2) على مستوى الـ Prompt بعد تجميعه وقبل تسليمه للنموذج.
  الهدف: منع prompt يبدو احترافيًا لكنه غير قابل للتنفيذ أو متناقض.
  مرتبط بـ: `references/specs/prompt-compiler.md` (المُجمِّع) + `references/specs/model-adapters.md` (نموذج) + `references/specs/prompt-architecture.md` (10 طبقات A-J) + `workflows/M9c-preflight.md` (preflight) + `workflows/M9b-quality-gates.md` (G4 controller).
  **G4 Hard Gate:** أي فشل هنا = prompt مرفوض.
tier: 3
when_to_load: "بعد Prompt Compiler وقبل التوليد الفعلي"
---

# Prompt Quality Gate — AI Film Studio v2.1.0 (G4 Hard Gate)

> **الإصدار 2.1.0:** إعادة ترقيم لتطابق نظام v2.0.2 الموحّد.
> G1-G7 الداخلية هنا = sub-criteria داخل **G4 (Prompt Quality)** في النظام end-to-end.
> **AUTHORITATIVE للـ 8-gate system:** `references/protocols/production-state-machine.md` § 3.
> **AUTHORITATIVE للـ 10 طبقات A-J:** `references/specs/prompt-architecture.md`.
> **AUTHORITATIVE للـ model fit:** `references/specs/model-adapters.md`.

---

## 1. الموقع في Pipeline

```text
M7a / M7b / M8a / M8d
    ↓ emit
compiled_prompt.md
    ↓
Prompt Quality Gate (G4 — Hard Gate) ← هذا الملف
    ↓
M9c Preflight (G5 model fit)
    ↓
TGeneration (to model API)
```

**Hard Gate:** أي FAIL هنا = prompt مرفوض، **لا يتجاوز**.

---

## 2. معايير الفحص (7 sub-criteria داخل G4)

### 2.1 PG-1 — Identity (الهوية)

```yaml
check:
  - "كل شخصية لها character_id معرّف"
  - "Identity String منسوخ حرفيًا من Continuity Bible (لا إعادة صياغة)"
  - "لا تعارض في العمر/الوجه/الشعر/الملابس/الهوية"
  - "يد مهيمنة محددة عند وجود دعامة"
fail_action: "REJECT — استبدل بـ identity_string من Bible"
severity: "critical"
```

### 2.2 PG-2 — Reference Roles (أدوار المراجع)

```yaml
check:
  - "كل مرجع له role واحد فقط (CHARACTER | STYLE | WORLD | PROP | FIRST_FRAME | LAST_FRAME | MOTION | AUDIO | TEXT)"
  - "لا خلط بين STYLE و IDENTITY"
  - "FIRST_FRAME و LAST_FRAME يحافظان على أدوارهما (لا يستخدمان كـ CHARACTER في نفس الوقت)"
  - "عدد المراجع ≤ سقف النموذج"
fail_action: "REJECT — أصلح role assignment"
severity: "critical"
```

### 2.3 PG-3 — Motion (الحركة، video فقط)

```yaml
check:
  - "فعل رئيسي واحد قابل للرصد"
  - "حركة كاميرا مهيمنة واحدة (أو static)"
  - "استبعاد صريح للحركات الأخرى: 'no rotation, no zoom'"
  - "لا dolly + zoom + orbit في لقطة واحدة"
  - "بداية → تطور → نهاية واضحة"
fail_action: "REJECT — اختر حركة واحدة واحذف الباقي"
severity: "critical"
```

### 2.4 PG-4 — Continuity (الاستمرارية)

```yaml
check:
  - "Scene DNA موروث من اللقطة السابقة (H_continuity.inherited_from_previous)"
  - "wardrobe/props/lighting/color_grading ثابتة"
  - "محور الشاشة محدد (screen direction)"
  - "خط النظر مسجّل"
  - "الطقس ثابت"
fail_action: "REJECT — استكمل inherited fields"
severity: "high"
```

### 2.5 PG-5 — Model Compatibility (توافق النموذج)

```yaml
check:
  - "النسبة (aspect_ratio) ضمن قدرات النموذج"
  - "المدة (duration) ضمن range النموذج"
  - "عدد المراجع ضمن السقف"
  - "الدقة (resolution) ضمن range النموذج"
  - "audio refs: نعم/لا حسب النموذج"
  - "negative_prompts: نعم/لا حسب النموذج"
fail_action: "REJECT — غيّر params أو غيّر النموذج (أبلغ المستخدم)"
severity: "high"
```

### 2.6 PG-6 — Text Integrity (سلامة النص)

```yaml
check:
  - "النص الحرفي محفوظ verbatim"
  - "يحدد مكان تنفيذ النص: image model / video model / compositing"
  - "لا يُطلب من video model تنفيذ typography دقيقة"
  - "EXACT ARABIC TEXT TO RENDER مستخدم للنص العربي الثابت"
  - "اتصال الحروف العربية (RTL، تشكيل، علامات ترقيم) مذكور"
fail_action: "REJECT — حدد مكان التنفيذ الصحيح"
severity: "critical"  # brand logo / dialogue text
```

### 2.7 PG-7 — Prompt Hygiene (النظافة اللغوية)

```yaml
check:
  - "لا كلمات ممنوعة: beautiful, stunning, amazing, cinematic, emotional, dramatic, epic, high quality, very nice, gorgeous, masterpiece"
  - "لا تكرار جوهري"
  - "لا حشو إنشائي"
  - "لا تعليمات متعارضة"
  - "لا افتراضات عالية التأثير غير معلنة"
fail_action: "REJECT — حوّل المجرد لـ production instructions"
severity: "high"
```

---

## 3. Scoring

```yaml
scoring:
  fail_classification:
    any_critical_fail: "REJECT (Hard Gate)"
    high_fails_le_1: "PASS"
    high_fails_2_plus: "REQUIRES_REVIEW"
    medium_fails_le_2: "PASS"
  
  soft_score_0_100:
    computed: "yes (for internal use)"
    not_shown_to_user: "by default"
    any_hard_fail: "score = 0 (regardless of soft score)"
  
  output:
    status: "PASS | REQUIRES_REVIEW | REJECT"
    failed_criteria: ["PG-3", "PG-5"]
    scores_per_criterion: { PG-1: 100, PG-2: 100, ... }
```

---

## 4. Repair Logic (إصلاح موجّه)

```text
FAIL detected
    ↓
Classify: أي sub-criterion فشل (PG-1, PG-2, ...)
    ↓
Identify: المتغير الأصغر المسؤول (لا تعيد كتابة الـ prompt)
    ↓
Suggest: إصلاح مقترح (text + scope)
    ↓
Return: prompt معدّل (الحد الأدنى من التغيير)
    ↓
Re-validate
    ↓
PASS → output
```

**مثال — فشل PG-3 (Motion):**
- العرض: `slow dolly in while orbiting left and zooming in`
- التشخيص: 3 حركات (dolly + orbit + zoom) — لا تتوافق مع "one dominant camera movement"
- الإصلاح: اختر dolly in فقط، أضف: `no rotation, no zoom`

**مثال — فشل PG-5 (Model — GPT Image 2 + 16:9):**
- العرض: `aspect_ratio: 16:9` مع `model: gpt-image-2`
- التشخيص: GPT Image 2 لا يدعم 16:9 أصلًا
- الإصلاح: غيّر النموذج إلى Nano Banana 2، أو غيّر النسبة إلى 3:2 مع توضيح cropping

**مثال — فشل PG-1 (Identity):**
- العرض: ملابس مختلفة عن Bible
- التشخيص: wardrobe drift
- الإصلاح: **لا** تضيف وصف إضاءة. استبدل بـ wardrobe_string من Bible.

---

## 5. Integration with Stage Model v2.0.2

```yaml
stage_integration:
  G4_in_v2.0.2:
    - "M7 (Image Prompts) → G4"
    - "M8 (Motion Prompts) → G4"
  controller: "M9b-quality-gates.md (8-gate controller)"
  preflight_after: "M9c-preflight.md (G5 model fit)"
  
  hard_gate_propagation:
    - "G4 fail → REJECT prompt (no generate)"
    - "G4 REQUIRES_REVIEW → ask user, no generate"
    - "G4 PASS → proceed to M9c"
```

---

## 6. مع G4 vs sub-criteria

| G4 sub-criterion | Severity | Old v1.3 name |
|---|---|---|
| PG-1 | critical | G1 (Identity) |
| PG-2 | critical | G2 (Reference Roles) |
| PG-3 | critical | G3 (Motion) |
| PG-4 | high | G4 (Continuity) |
| PG-5 | high | G5 (Model Compatibility) |
| PG-6 | critical | G6 (Text Integrity) |
| PG-7 | high | G7 (Prompt Hygiene) |

**ملاحظة v2.1.0:** sub-criteria لا تتعارض مع G0–G8 في v2.0.2 (هي internal). تم تغيير الاسم من G1-G7 إلى PG-1-PG-7 لتجنب الالتباس.

---

## 7. ما لم يتغيّر عن v1.3

- الـ 7 معايير فحص محفوظة.
- Repair logic (المتغير الأصغر) محفوظ.
- "لا تعالج فشل الهوية بإضافة أوصاف إضاءة" محفوظ.
- Soft score 0-100 محفوظ (internal).

## 8. ما تغيّر في v2.1.0

- **الاسم:** G1-G7 → PG-1-PG-7 (لتجنب التضارب مع G0-G8 end-to-end).
- **Stage reference:** M7 / M8 / M9c / M9b (لا M0-M13 v1.x).
- **Source of Truth:** production-state-machine.md (لا state-machine.md v1.1).
- **Hard gate propagation:** G4 hard gate propagation موثّق.
