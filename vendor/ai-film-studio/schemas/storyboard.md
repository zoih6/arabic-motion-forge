---
name: schema-storyboard
description: "عقد الـStoryboard المرئي: مشاهد وفريمات مرتبة قبل Prompts الصور."
tier: 3
when_to_load: "بعد اعتماد الرؤية وقبل توليد Prompts الصور"
---

# Storyboard Contract

الـStoryboard هو طبقة العرض الأولى قبل البرومبتات. هدفه أن يفهم المستخدم تسلسل العمل دون إغراقه في تفاصيل التنفيذ.

## الحقول الإلزامية

```yaml
storyboard:
  project_id: "..."
  aspect_ratio: "16:9"
  total_duration_seconds: 15
  reference_manifest: # defined by workflows/M4e-reference-orchestration.md
    status: "draft | approved | locked"
    manifest_id: "REF-MANIFEST-001"
    required_anchor_ids: ["CHAR-01-ID", "LOC-01-ANCHOR", "STYLE-01-ANCHOR"]
  shot_reference_map: "defined in reference_manifest for every shot_id"
  scenes:
    - scene_id: "SC01"
      title: "..."
      purpose: "وظيفة المشهد"
      frames:
        - frame_id: "FR01"
          shot_id: "SC01_SH01"
          role: "opening"
          visual_description: "وصف بصري مختصر"
          duration_seconds: 2
          start_state: "..."
          end_state: "..."
          reference_slots:
            - slot: "@image1"
              anchor_id: "CHAR-01-ID"
              role: "identity_reference"
            - slot: "@image2"
              anchor_id: "LOC-01-ANCHOR"
              role: "location_reference"
          image_prompt_status: "pending"
```

## قواعد العرض

- اعرض المشاهد بالترتيب الزمني.
- اجعل الوصف البصري مختصرًا وقابلًا للتخيل.
- لا تعرض Prompt الصورة في جدول الـStoryboard.
- اربط كل فريم بـ`frame_id` ثابت سيظهر لاحقًا في Prompt الصورة والتحريك.
- اربط كل فريم بخريطة `reference_slots`؛ كل `@imageN` يجب أن يملك `anchor_id` و`role` ومرجعًا معتمدًا.
- لا تقبل حالة `approved` للـStoryboard إذا كانت `reference_manifest.status` أقل من `approved` في مشروع متعدد اللقطات.
- لا تنشئ فريمات إضافية لمجرد تغطية طبقات Prompt.
- عدد الفريمات يخدم القصة والانتقال، لا حجم النظام.

## بوابة الانتقال

لا تبدأ Prompts الصور حتى يعتمد المستخدم الـStoryboard في مشروع متعدد المشاهد. إذا طلب المستخدم التنفيذ المباشر، اعتبر الـStoryboard معتمدًا ضمنيًا بعد عرض ملخصه المختصر.
