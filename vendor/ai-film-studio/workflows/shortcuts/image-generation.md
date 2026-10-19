---
name: shortcut-image-generation
description: ولّد صورة/فريم واحد عبر نموذج صورة
tier: 2
parent: workflows/M7a-prompt-architecture.md
duration: 5-10 min
---

# Shortcut: Image Generation

## Entry Conditions
- ✅ طلب: "صورة لـ X"، "ولّد فريم"، "Generate image"
- ❌ لا تحتاج تحريك

## Core Workflow (6 خطوات)

### 1. حدد النموذج (1 min)
ارجع لـ `references/specs/model-matrix.md` لاختيار:
- bytedance/seedream-4 (الأفضل للجودة السينمائية)
- midjourney-v6 (للأسلوب الفني)
- stability/sdxl (مفتوح المصدر)
- gemini-3-pro-image (native)

### 2. اكتب Prompt (2 min)
اتبع `workflows/shortcuts/single-prompt.md` (10 طبقات A-J).

### 3. أضف Reference (1 min)
- Anchor images (شخصية، مكان) إن وُجدت
- Style references (cinematographer, film)

### 4. حدد المعلمات (30 sec)
- aspect_ratio: 16:9 / 9:16 / 1:1
- resolution: 1024x1024 / 1920x1080 / 4K
- quality: high / ultra
- style_strength: ضعيف/قوي

### 5. ولّد 3-5 نسخ (1 min)
لا تعتمد على نسخة واحدة. ولّد variants.

### 6. اختر وصدّر (1 min)
اختر الأفضل حسب:
- تطابق مع الـ prompt
- جودة فنية
- تماسك بصري

## Quality Gate
- **G4 (Hard):** prompt يحوي 10 طبقات
- **G6 (Text):** إن وُجد نص، post_overlay إن حرج

## Output
- 1-3 صور نهائية
- prompt + parameters record
- (اختياري) variants للاختيار

## Common Mistakes
- ❌ prompt < 60 كلمة
- ❌ عدم تجربة variants
- ❌ تجاهل Reference images
- ❌ استخدام aspect ratio خاطئ للمنصة

## Next Step
- لتحريك → `image-to-video.md`
- لمزيد من اللقطات → `workflows/M0-intake.md` (مشروع كامل)
- لقياس الجودة → `quality/checklist.md`
