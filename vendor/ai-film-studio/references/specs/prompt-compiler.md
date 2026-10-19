---
name: prompt-compiler
description: |
  Prompt Compiler — AI Film Studio v2.1.0.
  يحوّل Canonical Prompt Spec + Model-specific Spec إلى prompt نهائي قابل للتنفيذ.
  يحافظ على الـ 10 طبقات A-J ولا يُدخل تحسينات معمارية.
  مرتبط بـ: `references/specs/prompt-architecture.md` (A-J) + `references/specs/model-adapters.md` (model-specific) + `workflows/M7a-prompt-architecture.md` (workflow) + `workflows/M7b-image-prompts.md` (image prompts) + `workflows/M8a-motion-prompts.md` (motion prompts).
tier: 3
when_to_load: "قبل توليد أي prompt (image أو video). يستدعيه M7a-prompt-architecture بعد M3a و M4."
---

# Prompt Compiler — AI Film Studio v3.1.0

> **الإصدار 2.1.0:** مواءمة مع Stage Model الموحّد (M0–M11). لم يتغير السلوك
> الأساسي؛ التغيير فقط في الواجهة (Interface): MODEL ADAPTER صار يسبق COMPILER
> منطقيًا (يُحوّل spec إلى model-specific spec قبل التجميع).
>
> **AUTHORITATIVE للـ stage model:** `references/protocols/production-state-machine.md`.
> **AUTHORITATIVE للـ 10 طبقات A-J:** `references/specs/prompt-architecture.md`.

---

## 1. الـ Interface النهائي (Pipeline)

```text
Workflow Output (M2-M4)
    ↓
Canonical Prompt Spec (10-Layer A-J)
    ↓
Model Adapter (model-specific spec)
    ↓
Prompt Compiler (assemble + sanitize)
    ↓
Prompt Quality Gate (G4 — Hard Gate)
    ↓
Model-ready Prompt
```

| Step | Workflow / File | Output | Quality Gate |
|---|---|---|---|
| 1. Workflow Output | M2/M3a/M4a → مخرجات موثّقة | draft values per A-J | G0 (intake) — already passed |
| 2. Canonical Prompt Spec | `references/specs/prompt-architecture.md` | spec.yaml (10 layers) | G1/G2/G3 — already passed |
| 3. Model Adapter | `references/specs/model-adapters.md` | spec.model-specific.yaml | (none — pure transformation) |
| 4. Prompt Compiler | هذا الملف (prompt-compiler.md) | compiled-prompt.md | G4 (incoming) |
| 5. Prompt Quality Gate | `references/specs/prompt-quality-gate.md` | PASS / FAIL | G4 (Hard Gate) |
| 6. Model-ready Prompt | (external: to model API) | ready-to-send | G4 passed |

---

## 2. Compilation Chain (نظّم)

```text
WORKFLOW OUTPUT (M2/M3a/M4a)
    → CANONICAL PROMPT SPEC (10 layers A-J, model-agnostic)
    → MODEL ADAPTER (transform to model-specific syntax)
    → PROMPT COMPILER (assemble + sanitize + dedupe)
    → PROMPT QUALITY GATE (10-layer check + model fit)
    → MODEL-READY PROMPT (to generation API)
```

**ما تغيّر عن v1.3:** ترتيب Model Adapter صار **قبل** Compiler (كان بعده في v1.3). السبب: Adapter يُعدّل spec حسب قدرات النموذج، ثم Compiler يجمّع الإصدار النهائي.

---

## 3. Canonical Prompt Schema (Input)

```yaml
prompt_id: SC01_SH01_VIDEO_v001
output_type: image | image_to_video | text_to_video | edit | motion_graphics | dialogue
model_target: auto | named_model    # 'auto' → يختاره Model Adapter

# الطبقات الـ 10 (A-J) — من references/specs/prompt-architecture.md
A_intent: { ... }      # scene_purpose, narrative_beat, emotional_target
B_subject: { ... }     # identity_string (locked), wardrobe, props, pose
C_environment: { ... } # location, time, atmosphere
D_composition: { ... } # framing, subject_placement, visual_layers
E_camera: { ... }      # lens, aperture, focus, sensor
F_lighting: { ... }    # key, fill, rim, contrast, temp
G_motion: { ... }      # character_motion, camera_motion, timing, physics
H_continuity: { ... }  # inherited_from_previous, exit_state, entry_state_for_next
I_style: { ... }       # genre, color_palette, texture, color_grade
J_constraints: { ... } # identity_lock, wardrobe_lock, prop_lock, negative_prompts

references:
  - role: CHARACTER | STYLE | WORLD | PROP | FIRST_FRAME | LAST_FRAME | MOTION | AUDIO | TEXT
    source: <asset_id or path>

output_settings:
  aspect_ratio: "16:9" | "9:16" | ...
  duration: 10s           # video only
  model: <chosen by adapter>
  resolution: "1080p"
```

---

## 4. Compilation Rules

> **لم تتغيّر من v1.3** (السلوك الأساسي محفوظ). ما تغيّر هو الترتيب في Pipeline.

1. **Preserve identity string verbatim** — من Continuity Bible (canonical).
2. **Inherit Scene DNA before shot-specific details** — من `schemas/state/frame-chain.md`.
3. **One dominant subject action + one dominant camera movement per shot** — ما لم يدعم النموذج أكثر صراحة.
4. **Convert vague adjectives to observable production instructions** — beautiful → وصف إضاءة + تكوين + حركة.
5. **Remove duplicate constraints** — dedupe.
6. **Resolve contradictions before delivery** — لا prompt متناقض.
7. **High-priority instructions early** — identity → composition → action → camera → ... → style.
8. **Model-specific syntax in adapter layer, not canonical spec** — الـ spec يبقى model-agnostic.
9. **No invention of missing facts** — استنتج low-risk فقط، ضع علامة على high-impact assumptions.
10. **One canonical prompt unless variants requested** — لا تولّد 3 نسخ تلقائيًا.

---

## 5. Priority Order (ثابت)

```text
identity/reference locks
  > user constraints
    > composition
      > primary action
        > camera
          > lighting
            > environment
              > style
                > secondary detail
                  > optional aesthetics
```

---

## 6. Prompt Budget

- **Image prompt:** 60-200 كلمة (طبيعي)، 300+ عند الحاجة.
- **Video prompt:** 100-300 كلمة (طبيعي)، 400+ عند الحاجة.
- احذف prose الزخرفي الذي لا يؤثر على التوليد.

---

## 7. Final Form

الـ compiler يُخرج:
- `compiled-prompt` (النص النهائي + metadata).
- لا يُخرج schema الداخلي، routing، scoring، diagnostics ما لم يُطلب صراحة.

---

## 8. Integration with Workflows

| Workflow | يستدعي Compiler؟ | يمر على Quality Gate؟ |
|---|---|---|
| `workflows/M7a-prompt-architecture.md` | ✅ (per shot) | ✅ G4 |
| `workflows/M7b-image-prompts.md` | ✅ (per image) | ✅ G4 |
| `workflows/M8a-motion-prompts.md` | ✅ (per motion) | ✅ G4 |
| `workflows/M8d-motion-graphics.md` | ✅ (per MG) | ✅ G4 + G-M1 (motion) |
| `workflows/M6c-dialogue-lipsync.md` | ✅ (per shot) | ✅ G4 + G7 |
| `workflows/M9c-preflight.md` | لا (يفحص ناتج Compiler) | ✅ G4 + G5 (model fit) |
| `workflows/M9b-quality-gates.md` | لا (G4 hard gate) | ✅ G4 (final) |

---

## 9. ما لم يتغيّر عن v1.3

- الـ 10 قواعد compilation محفوظة حرفياً.
- الـ priority order محفوظ.
- الـ canonical prompt schema محفوظ (نفس الحقول).
- Prompt budget محفوظ.

## 10. ما تغيّر في v2.1.0

- **الترتيب:** Model Adapter صار قبل Compiler (منطقياً).
- **الواجهة (Interface):** ربط صريح بـ 5 workflows تستدعيه.
- **Stage references:** الإشارة إلى M2/M3a/M4a (لا M1/M2/M3 v1.x).
- **Source of Truth:** production-state-machine.md هو المرجع.

---

## 11. التنفيذ الفعلي

يوجد الآن Compiler حتمي قابل للتشغيل:

```bash
python3 scripts/prompt_compiler.py \
  examples/compiler-fixture.json \
  --output /tmp/compiled.json \
  --markdown /tmp/compiled-prompts.md
```

مدخلاته هي `reference_manifest` و`shots` وفق `schemas/prompt-compiler-input.schema.json`. لكل لقطة يقوم التنفيذ بـ:

1. التحقق من أن كل `anchor_id` موجود ومعتمد وله `approved_asset`.
2. ترتيب المراجع حسب الدور وتوليد `@Image1`, `@Image2`, ... تلقائيًا.
3. إنشاء `reference_map` يربط كل خانة بالـanchor والملف والدور.
4. ترجمة حركة الكاميرا من قاموس موحّد إلى لهجة Seedance أو Omni أو Veo.
5. توليد Timeline إذا لم تكن موجودة، مع فعل رئيسي واحد وحركة كاميرا واحدة.
6. رفض القيود غير المدعومة، مثل جمع first/last frame مع مراجع صور أخرى في Seedance.
7. إخراج JSON قابل للمعالجة وMarkdown قابل للنسخ.

الاختبار الحتمي:

```bash
python3 scripts/test_prompt_compiler.py
```

لا يُسمح بإضافة Adapter جديد اعتمادًا على التخمين؛ يجب أولًا إضافة profile موثّق في `scripts/prompt_compiler.py` و`references/specs/model-matrix.md`.
