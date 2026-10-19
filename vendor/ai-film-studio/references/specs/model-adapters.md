---
name: model-adapters
description: |
  Model Adapter Layer — AI Film Studio v2.1.0.
  يفصل «ماذا نريد إنتاجه» عن «كيف نخاطب النموذج».
  الـCanonical Prompt Spec ثابت (10 layers A-J)؛ الـAdapter يترجمه إلى model-specific spec.
  مرتبط بـ: `references/specs/prompt-architecture.md` (canonical) + `references/specs/prompt-compiler.md` (compile بعد adapter) + `references/specs/prompt-quality-gate.md` (G4) + `references/specs/model-matrix.md` (capabilities).
tier: 3
when_to_load: "بعد Canonical Prompt Spec وقبل Prompt Compiler"
---

# Model Adapter Layer — AI Film Studio v2.1.0

> **الإصدار 2.1.0:** مواءمة مع Stage Model الموحّد (M0–M11).
> الموقع في Pipeline صار واضحًا: **بعد Canonical Spec، قبل Prompt Compiler**.
> **AUTHORITATIVE للـ capabilities:** `references/specs/model-matrix.md`.

---

## 1. الموقع في Pipeline

```text
Workflow Output (M2/M3a/M4a)
    ↓
Canonical Prompt Spec (10 layers A-J, model-agnostic)
    ↓
Model Adapter ← هذا الملف (transform to model-specific)
    ↓
Prompt Compiler (assemble + sanitize)
    ↓
Prompt Quality Gate (G4)
    ↓
Model-ready Prompt
```

**ما تغيّر عن v1.3:** الـ Adapter صار يسبق Compiler (ترتيب صحيح: نكيّف spec للنموذج أولاً، ثم نجمّع).

---

## 2. Adapter Contract

```yaml
adapter_id: ADAPTER-<MODEL_NAME>
input: canonical_prompt_spec    # 10 layers A-J, model-agnostic
output:
  prompt_syntax: <string>          # how to write prompt for this model
  reference_syntax: <string>      # how to attach references
  supported_controls: [...]        # what the model accepts
  unsupported_controls: [...]      # what to drop or replace
  settings: { aspect_ratio, duration, model, resolution, ... }
validation:
  - capability_check
  - reference_check
  - aspect_ratio_check
  - duration_check
  - text_check
  - audio_check
  - negative_prompt_check
```

---

## 3. Selection Policy

```yaml
selection:
  user_specified:
    - "إذا حدّد المستخدم نموذجًا، استخدمه ما لم يكن غير متوافق"
    - "عند التعارض: اشرح باختصار + اقترح البديل + ASK_USER"
  auto:
    - "اختر النموذج الأنسب بناءً على:"
    - "  - output_type (image / video / motion_graphics / dialogue)"
    - "  - aspect_ratio"
    - "  - duration"
    - "  - عدد المراجع المطلوبة"
    - "  - الحاجة لـ audio / lipsync / native_audio"
    - "  - الحاجة لـ negative_prompts"
  never_do:
    - "لا تغيّر Creative Spec لتناسب النموذج"
    - "غيّر الصياغة أولًا، وغيّر النموذج فقط إذا كانت القدرة غير مدعومة"
    - "لا تخترع capability (راجع model-matrix.md)"
```

---

## 4. Capability-Aware Translation

قبل تسليم spec مُكيَّف للـ Compiler، افحص:

1. **aspect_ratio** — هل النسبة مدعومة في النموذج؟
2. **duration** — هل المدة مدعومة (video)؟
3. **references** — نوع وعدد المراجع ضمن السقف؟
4. **audio/dialogue/lipsync** — مدعوم أصلًا؟ (Veo 3 native، Seedance مع image، Omni بدون audio)
5. **text in image** — مسار النموذج أم compositing خارجي؟
6. **first/last frame** — متاح؟ (Veo 3، Seedance 2.0)
7. **edit mode** — متاح؟ (Omni conversational)
8. **negative_prompts** — مدعوم؟ (Nano Banana 2 نعم، Omni لا)

**عند أي fail:** ارجع لـ prompt-compiler.md (الحد الأدنى من التغيير) أو اطلب تغيير النموذج.

---

## 5. Model Profiles (Source: model-matrix.md)

> **لا تثق بأي مواصفة من الذاكرة.** ارجع دائمًا لـ `references/specs/model-matrix.md`.
> اعتبر بيانات Preview قابلة للتغير.

| Family | Model | output_type | audio | negative_prompts | first_frame | edit |
|---|---|---|---|---|---|---|
| Image (fast) | `gemini-3.1-flash-image` (Nano Banana 2) | image | no | yes | no | no |
| Image (Pro) | `gemini-3-pro-image-preview` (Nano Banana 2 Pro) | image | no | yes | no | no |
| Image (creative) | `gpt-image-2` | image | no | yes | no | no |
| Video (native audio) | `veo-3` | video | **yes (native)** | yes | yes | no |
| Video (high quality) | `bytedance/seedance-2.0` | video | optional | yes | yes (excludes refs) | no |
| Video (conversational) | `gemini-omni-1.1-flash` | video | no | **no** | yes | yes |
| Video (artistic) | `runwayml/gen4` | video | no | yes | yes | limited |
| Video (long) | `kling-2.1` | video | no | yes | yes | no |
| Video (latest) | `sora` | video | no | yes | yes | no |
| Lip-sync | `hedra`, `omniverse-audio2face` | video | yes (sync) | n/a | yes | n/a |
| Audio (voice) | `elevenlabs`, `cartesia` | audio | n/a | n/a | n/a | n/a |
| Audio (music) | `suno`, `udio` | audio | n/a | n/a | n/a | n/a |

**لـ capabilities تفصيلية (aspects, sizes, durations, refs):** راجع `references/specs/model-matrix.md`.

---

## 6. Adapter Principle

```text
ONE CANONICAL PROMPT SPEC
    ├── Adapter A (Veo 3)        → syntax + settings لـ Veo 3
    ├── Adapter B (Seedance 2.0) → syntax + settings لـ Seedance
    ├── Adapter C (Omni Flash)   → syntax + settings لـ Omni
    └── Adapter D (Nano Banana)  → syntax + settings لـ Nano Banana
```

**المستخدم لا يرى طبقة الـ Adapter** إلا إذا طلب مقارنة النماذج أو سبب اختلاف الصياغة.

---

## 7. Integration with Stage Model v2.0.2

```yaml
stage_integration:
  called_by:
    - "M7a-prompt-architecture.md (per shot — once)"
    - "M7b-image-prompts.md (per image — once)"
    - "M8a-motion-prompts.md (per motion — once)"
    - "M8d-motion-graphics.md (per MG — once)"
  feeds_into: "Prompt Compiler (next stage)"
  validated_by: "M9c-preflight.md (G5 model fit)"
  hard_gate: "Prompt Quality Gate (G4) — catches adapter mistakes"
```

---

## 8. ما لم يتغيّر عن v1.3

- Adapter Contract (input/output) محفوظ.
- Selection Policy محفوظ.
- "لا تغيّر Creative Spec لتناسب النموذج" محفوظ.
- "لا تثق بالذاكرة" → ارجع لـ model-matrix.md محفوظ.

## 9. ما تغيّر في v2.1.0

- **الترتيب:** Adapter صار قبل Compiler (صحيح منطقياً).
- **Model Profiles table:** 12 عائلة + capabilities سريعة.
- **Stage reference:** M7a/M7b/M8a/M8d (لا v1.x).
- **Source of Truth:** model-matrix.md هو المرجع الرقمي.
- **Integration map:** مَن يستدعي Adapter ومَن يفحصه.
