---
name: shortcut-image-to-video
description: حرّك صورة موجودة عبر نموذج فيديو
tier: 2
parent: workflows/M7a-prompt-architecture.md
duration: 5-15 min
---

# Shortcut: Image to Video

## Entry Conditions
- ✅ صورة موجودة (input image)
- ✅ طلب: "حرّك"، "ولّد فيديو من هذه الصورة"
- ❌ لا تحتاج مشاهد أخرى (إلا إذا ذكر المستخدم)

## Core Workflow (7 خطوات)

### 1. اختر النموذج (1 min)
ارجع لـ `references/specs/model-matrix.md`:
- bytedance/seedance-2.0 (الأفضل لـ i2v)
- runwayml/gen4 (alternatives)
- kling-2.1 (open)
- veo-3 (مع audio)

### 2. حدد المدة (30 sec)
- 5s (minimal)
- 8-10s (standard)
- 15s (Seedance max)

### 3. اكتب Motion Prompt (3 min)
**الـ Motion Prompt منفصل عن Image Prompt.** يركّز على:
- character_motion: فعل واحد محدد
- camera_motion: static / dolly / pan
- secondary_motion: شعر، ملابس، بخار
- timing: beats per second
- end_state: كيف ينتهي

### 4. حدد المعلمات (30 sec)
- duration
- motion_strength (1-5)
- camera_motion_lock (true/false)

### 5. ولّد 3-5 نسخ (3-5 min)
- جرب prompt مختلف
- جرب motion_strength مختلف

### 6. تحقق من الاستمرارية (1 min)
- هل الشخصية ثابتة؟
- هل end_frame يطابق start_frame؟
- هل الإضاءة/اللون ثابتين؟

### 7. اختر وصدّر (1 min)
- اختر الأفضل
- صدّر بصيغة MP4 (H.264) عالي الجودة

## Quality Gate
- **G3.1:** Character matching مع الـ image
- **G3.2:** لا frame chain break غير مبرر
- **G4 (Hard):** Motion layer مفصّل

## Output
- 1-3 فيديوهات نهائية (MP4)
- motion prompt + parameters

## Common Mistakes
- ❌ استخدام Image Prompt كـ Motion Prompt
- ❌ حركة كاميرا + حركة شخصية في لقطة واحدة
- ❌ عدم تحديد end_state
- ❌ تجاهل model-specific constraints

## Next Step
- لإضافة صوت → `dialogue-lipsync.md` أو `workflows/M6-audio.md`
- لتجميع في فيلم → `workflows/M0-intake.md` (مشروع كامل)
- لقياس الجودة → `quality/checklist.md`
