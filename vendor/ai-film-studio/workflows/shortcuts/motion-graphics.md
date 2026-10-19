---
name: shortcut-motion-graphics
description: موشن تايبوجرافي / kinetic typography / animated text
tier: 2
parent: workflows/M5a-graphics.md
duration: 10-20 min
---

# Shortcut: Motion Graphics

## Entry Conditions
- ✅ طلب: "موشن تايبوجرافي"، "نص متحرك"، "kinetic typography"
- ❌ لا شخصية رئيسية (نص هو البطل)

## Core Workflow (6 خطوات)

### 1. حدّد النص (1 min)
- ما النص بالضبط؟ (نسخ حرفي)
- كم كلمة؟ (1-2 / 3-5 / 6+)
- ما اللغة؟ (ar, en, mixed)

### 2. اختر استراتيجية التنفيذ (2 min)
ارجع لـ `workflows/M5a-graphics.md` § 5 استراتيجيات:

| الاستراتيجية | متى |
|---|---|
| **Burn-In** | نص بسيط، قصير، في لقطة ثابتة |
| **Post-Production Overlay** | نص حرج (شعار، CTA، 100% دقة) |
| **i2v Locked** | نص في لقطة، البيئة تتحرك |
| **V2V Masked** | إضافة نص على فيديو موجود |
| **Typography as Architecture** | نص في المشهد (neon, sign, building) |

### 3. اختر الخط (1 min)
ارجع لـ `workflows/M5a-graphics.md` § Typography:

**للعربي:**
- Tajawal (حديث), Cairo (متعدد), Lalezar (عناوين)
- Aref Ruqaa (تقليدي), Reem Kufi (تراثي)

**للإنجليزي:**
- Bebas Neue (عنوان), Montserrat (حديث)
- Playfair Display (فخم), Futura (هندسي)

**القاعدة:** لا تخلط أكثر من 2-3 خطوط.

### 4. طبّق قواعد RTL/الحركة (1 min)
**حرج للعربي:**
- direction: RTL
- animation: كلمة بكلمة (لا حرف بحرف)
- engine: لا تعتمد على "Middle Eastern text engine" — استخدم post_overlay

### 5. حدد Animation (2 min)
- safe_patterns: fade_in/out, slide_in/out, scale_pulse
- risky: rotate, 3D_flip
- impossible: path_follow, char_react_to_env

### 6. نفّذ (5-10 min)
- إن post_overlay: After Effects / Motion / DaVinci
- إن burn_in: prompt + model
- إن hybrid: الاثنين

## Quality Gate
- **G6 (Text):** استراتيجية + backup
- **G6.4 (critical):** Brand logo في post_overlay
- **G6.6:** Prompt patterns صحيحة (اقتباسات)

## Output
- فيديو مع نص متحرك (MP4)
- prompt + After Effects project (إن وُجد)
- typography spec

## Common Mistakes
- ❌ تحريك عربي حرف بحرف
- ❌ brand logo في burn_in
- ❌ font choice عشوائي
- ❌ تجاهل safe areas

## Next Step
- للدمج في فيلم → `workflows/M0-intake.md` (مشروع كامل)
- لإضافة صوت → `workflows/M6-audio.md`
- لقياس الجودة → `quality/checklist.md`
