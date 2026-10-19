---
name: reference-orchestration
description: |
  يبني حزمة مرجعيات إنتاجية قبل الـStoryboard والـprompts، ويربط كل مرجع
  بدور واضح ووسم @image قابل للتنفيذ حسب مزود التوليد.
tier: 2
when_to_load: "إلزامي لأي scene/sequence/full-production أو أي مشروع يتكرر فيه كيان بصري"
---

# M4e — Reference & Prompt Orchestration

## الهدف

هذه المرحلة هي **بوابة المرجعيات**. لا نبدأ من اللقطة ولا نترك النموذج يخمّن الشخصيات أو المكان. نحوّل الفكرة إلى سجل قابل للتنفيذ يحدد: من يظهر، كيف يبدو، أين يوجد، ما الذي يتكرر، وما الصورة التي تثبّت كل ذلك.

القاعدة العملية:

> **صمّم المرجع أولًا، ثبّت النسخة المعتمدة، ثم اكتب الـStoryboard، ثم ابنِ prompt اللقطة مع أدوار `@image` صريحة.**

## متى تكون إلزامية؟

- فيلم قصير، مشهد متعدد اللقطات، إعلان سردي، أو سلسلة.
- أي مشروع فيه شخصية/مخلوق/منتج/مكان يتكرر.
- لا تُستخدم في صورة مستقلة لا تحتوي كيانًا متكررًا.

## ترتيب التشغيل

```text
INTAKE
  → CAST & ENTITY INVENTORY
  → CHARACTER / CREATURE / PRODUCT SHEETS
  → LOCATION & STYLE ANCHORS
  → REFERENCE PROMPTS (one per anchor)
  → REFERENCE APPROVAL + LOCK
  → REFERENCE MAP (@image roles per shot)
  → STORYBOARD
  → IMAGE PROMPTS
  → MOTION PROMPTS
```

## حزمة المرجعيات المطلوبة

| النوع | المعرّف | الوظيفة | الحد الأدنى |
|---|---|---|---|
| هوية شخصية | `CHAR-01-ID` | الوجه والجسم والعلامات الثابتة | front + 3/4 + side/back |
| ملابس | `CHAR-01-COSTUME` | الخامة واللون والحالة | turnaround أو detail sheet |
| مخلوق/منتج | `ENTITY-01-ID` | الشكل والنسب والمواد | front/side/detail |
| مكان | `LOC-01-ANCHOR` | layout ومواد المكان | wide empty location |
| أسلوب | `STYLE-01-ANCHOR` | اللون والضوء والقوام | بدون الشخصيات |
| دعامة متكررة | `PROP-01-ANCHOR` | شكلها وموقعها واليد المستخدمة | isolated object sheet |

لا تُنشأ كل الأنواع آليًا إذا لم تظهر في المشروع، لكن أي كيان يتكرر يجب أن يملك `anchor_id` ونسخة معتمدة.

## عقد المرجع (Reference Manifest)

```yaml
reference_manifest:
  project_id: "PROJECT-001"
  status: "draft | approved | locked"
  model_profile: "seedance-2 | nano-banana-2 | gpt-image-2 | provider-unknown"
  anchors:
    - anchor_id: "CHAR-01-ID"
      kind: "character_identity"
      entity_id: "CHAR-01"
      purpose: "exact face, body proportions, hair, distinctive marks"
      source: "generated | uploaded | existing_asset"
      approved_asset: "assets/anchors/char-01-id-v1.png"
      locked_description: "verbatim identity string"
      generation_prompt: "one complete copy-ready prompt"
      @image_role: "identity_reference"
      applies_to: ["SC01_SH01", "SC01_SH02"]
      status: "pending | approved | rejected"
    - anchor_id: "LOC-01-ANCHOR"
      kind: "location"
      entity_id: "LOC-01"
      purpose: "layout, materials, spatial continuity"
      approved_asset: "assets/anchors/loc-01-v1.png"
      @image_role: "location_reference"
      applies_to: ["SC01_SH01", "SC01_SH02"]
  shot_reference_map:
    - shot_id: "SC01_SH01"
      refs:
        - slot: "@image1"
          anchor_id: "CHAR-01-ID"
          role: "identity_reference"
        - slot: "@image2"
          anchor_id: "LOC-01-ANCHOR"
          role: "location_reference"
        - slot: "@image3"
          anchor_id: "STYLE-01-ANCHOR"
          role: "style_reference"
      prompt_reference_sentence: "@image1 is the character identity; @image2 is the location layout; @image3 is the lighting/style reference."
```

## قواعد `@image`

1. لا تكتب `@image` بلا رقم، ولا تستخدم الرقم لمرجع غير موجود في `shot_reference_map`.
2. لكل مرجع دور واحد: `identity_reference` أو `costume_reference` أو `location_reference` أو `prop_reference` أو `style_reference` أو `frame_reference`.
3. لا تُرسل مرجع الأسلوب على أنه هوية شخصية، ولا صورة درامية مظلمة كمرجع هوية أساسي.
4. ترتيب الخانات يختلف حسب المزود؛ يجب أن يسجل النظام `provider_slot` مع `role`، لا يعتمد على الرقم وحده.
5. إذا كان المزود لا يدعم خانات `@image`، تُحوّل الخريطة إلى وصف لفظي: `use image 1 for face...` مع تسجيل ذلك في metadata.
6. الـmotion prompt يعيد استخدام مرجعيات اللقطة نفسها، ويضيف `first_frame` و`last_frame` كأدوار مستقلة.

## قواعد تصميم احترافية

- الشخصية الرئيسية: identity sheet + costume sheet + prop sheet عند الحاجة.
- الشخصيات الثانوية المتكررة: cast lineup لا يغني عن sheet منفصل إذا كانت الشخصية تتكلم أو تقود حدثًا.
- المجموعات/الحشود: مرجع lineup مع قواعد تنويع، لا ستة أشخاص مجهولين يعاد اختراعهم في كل لقطة.
- المكان: صورة واسعة فارغة أولًا، ثم تُستخدم للحفاظ على layout والإضاءة.
- كل prompt مرجعي مستقل وقابل للنسخ، ولا يُبنى من أجزاء مبهمة.
- بعد اعتماد المرجع، يُقفل `locked_description` حرفيًا؛ أي تعديل يرفع نسخة جديدة ويعيد فحص اللقطات التابعة.

## بوابة الخروج

لا تنتقل إلى Storyboard/Generation في مشروع متعدد اللقطات إذا:

- لا توجد شخصية/كيان مرجعي لكل عنصر متكرر.
- توجد لقطة فيها `@image` غير معرّفة أو بلا دور.
- لا توجد صورة مكان للقطات التي تتطلب استمرارية مكانية.
- المرجع الأساسي للشخصية غير محايد أو يخفي العلامات المميزة.
- المرجع غير معتمد أو عدد المراجع يتجاوز قدرة المزود.

المخرج الداخلي هو `reference_manifest + anchor_prompts + shot_reference_map`. يظهر للمستخدم كـ **حزمة المراجع** مختصرة قبل الـStoryboard، مع سؤال اعتماد واحد.
