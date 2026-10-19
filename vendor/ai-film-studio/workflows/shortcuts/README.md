---
name: shortcuts
description: |
  خريطة المسارات السريعة. عندما يطلب المستخدم مهمة محددة (برومبت واحد، صورة، lip-sync، إلخ)
  لا تشغّل الـ pipeline الكامل. اقرأ الـ shortcut المناسب فقط.
tier: 2
---

# Workflow Shortcuts — مسارات سريعة

> **القاعدة:** لا تشغّل M0–M11 لمهمة محددة. استخدم الـ shortcut المناسب.

| الـ Shortcut | متى يُستخدم | الملف |
|---|---|---|
| Concept Only | "عندي فكرة" | `concept-only.md` |
| Single Prompt | "اكتب برومبت" | `single-prompt.md` |
| Image Generation | "صورة واحدة" | `image-generation.md` |
| Image to Video | "حرّك هذه الصورة" | `image-to-video.md` |
| Motion Graphics | "موشن تايبوجرافي" | `motion-graphics.md` |
| Dialogue / Lip-Sync | "حوار متحرك" | `dialogue-lipsync.md` |
| Repair | "هذا مكسور، أصلحه" | `repair.md` |

## كيف تختار

```
1. اقرأ طلب المستخدم
2. اسأل نفسك: هل هو:
   - مهمة واحدة؟ → استخدم shortcut
   - مشروع متعدد المراحل؟ → ارجع لـ M0
3. حمّل الـ shortcut المناسب فقط
4. نفّذ خطواته المختصرة (3-7 خطوات)
5. سلّم المخرج (prompt / image / video / file)
```

## المدة المتوقعة

| Shortcut | المدة المتوقعة | المخرج |
|---|---|---|
| Concept Only | 10-15 min | concept_deck |
| Single Prompt | 2-5 min | prompt واحد |
| Image Generation | 5-10 min | صورة + variants |
| Image to Video | 5-15 min | فيديو + variants |
| Motion Graphics | 10-20 min | موشن + variants |
| Dialogue / Lip-Sync | 5-10 min | فيديو مع حوار |
| Repair | 5-15 min | إصلاح الجزء المحدد |

## عند الفشل

إذا فشلت الـ shortcut (مثلاً: نموذج لا يدعم)، لا تترقَّ لـ M0 تلقائيًا. اقترح للمستخدم:
- نموذج بديل
- تقييد النطاق
- أو: بدء مشروع كامل إذا كان الطلب معقدًا فعلًا
