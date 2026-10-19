---
name: shortcut-single-prompt
description: اكتب prompt واحد فقط (A-J) لمشهد أو لقطة
tier: 2
parent: workflows/M7a-prompt-architecture.md
duration: 2-5 min
---

# Shortcut: Single Prompt

## Entry Conditions
- ✅ طلب: "اكتب prompt"، "برومبت لـ [X]"، "كيف أصف [Y]"
- ❌ لا تحتاج Continuity Bible (إلا إذا ذكر المستخدم سياق)

## Core Workflow (4 خطوات)

### 1. فهم الطلب (30 sec)
- ما الهدف؟ (صورة / فيديو)
- أي نموذج؟ (bytedance/seedream-4, midjourney-v6, kling, ...)
- ما الطول المرغوب؟

### 2. طبق A-J (3 min)
اقرأ `references/specs/prompt-architecture.md`، طبّق 10 طبقات:

| الطبقة | السؤال |
|---|---|
| A | لماذا هذا المشهد؟ |
| B | من/ما الموضوع؟ (Identity String إذا شخصية) |
| C | أين ومتى؟ |
| D | كيف يُبنى الكادر؟ |
| E | بمَ نرى؟ (lens, angle) |
| F | كيف يُضاء؟ (key, fill, rim) |
| G | ما الذي يتحرك؟ (فيديو) |
| H | ما الموروث/الخارج؟ (إن وجد) |
| I | ما اللغة البصرية؟ (palette, texture) |
| J | ما القيود؟ (negative prompts) |

### 3. Output (1 min)
اكتب الـ prompt بالإنجليزية، 100-300 كلمة.
- علامات اقتباس للنص
- hex للألوان
- numbers للقياسات
- لا صفات مجردة

### 4. Self-Audit (30 sec)
تحقق:
- ✅ 10 طبقات حاضرة
- ✅ Identity String منسوخ (إن وجد)
- ✅ Reference images مذكورة
- ✅ Negative prompts
- ✅ Model + aspect ratio محدد

## Quality Gate
- **G4 (Hard):** كل 10 طبقات موجودة
- لا Hard Gate failures مقبولة

## Output
- prompt واحد مُنسَّق
- (اختياري) reference images list

## Common Mistakes
- ❌ صفات مجردة ("جميل", "مؤثر")
- ❌ عدم ذكر النموذج
- ❌ Identity String مُعاد صياغته
- ❌ اختصار < 60 كلمة

## Next Step
- لتوليد → اتبع `image-generation.md` أو `image-to-video.md`
- لمزيد من المشاهد → ارجع لـ M0 (مشروع كامل)
