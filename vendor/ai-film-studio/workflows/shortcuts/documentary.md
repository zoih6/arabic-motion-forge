---
name: shortcut-documentary
description: "حلقة وثائقية واحدة سريعة بأسلوب الكولاج الورقي — مدخل مختصر لمحرك E1."
tier: 2
parent: workflows/engines/E1-documentary-engine.md
duration: 20-45 min
style_lock: LOCK-A-documentary-archive.txt
quality_gates: [G9, G10, G4]
---

# Shortcut: Documentary — حلقة وثائقية

## Entry Conditions
- ✅ طلب: "وثائقي"، "حلقة عن..."، "قصة حقيقية"، "فيديو essay"، "قناة بدون وجه"
- ✅ لديه **موضوع محدد** مسبقًا (إن لم يكن → ابدأ من `E1` الحالة 1)
- ❌ يوجد منتج → `workflows/engines/E2` أو `E3`

## الاختصار عن E1 الكامل

```
E1 الكامل:  1 نيش → 2 عشر أفكار → 3 مدة → 4 سكربت → 5 صوت → 6 Beats → 7 prompts → 8 UVP → 9 ثامبنيل
هذا الاختصار:  ← الموضوع جاهز →  3 مدة → 4 سكربت → 5 صوت → 6 Beats → 7 prompts → 8 UVP → 9 ثامبنيل
```

**تتخطى الحالتين 1 و 2 فقط.** باقي الحالات **تُنفَّذ بالكامل** بتوقف بعد كل واحدة.

## Core Workflow

### 1. أكّد الموضوع بصمت
لا تسأل "هل هذا صحيح؟". استنتج النيش في سطر واحد داخليًا، وانتقل للمدة.

### 2. المدة (الحالة 3)
```
كم مدة الحلقة؟
30 ثانية · 1 دقيقة · 2 دقيقة · 3 دقائق · 5 دقائق
```

### 3. السكربت (الحالة 4)
- **Cold Open ثلاثي إجباري:** تاريخ + مكان + فعل صغير.
- كل جملة = Beat بصري واحد.
- **Cliffhanger إجباري** ≤ 12 كلمة بأحد الأنماط الخمسة.
- 2.5 كلمة/ثانية (±5%).
- ❌ لا CTA، لا مقدمات، لا em dash، لا إيموجي.

### 4. التعليق الصوتي (الحالة 5)
دفعات 20–25 ثانية · Stability 55 · Similarity 80 · Style منخفض · Speaker Boost.
→ `references/knowledge/voice-system.md`

### 5. Beats (الحالة 6)
جدول 3 أعمدة: Beat · التوقيت · الكلمات (حرفيًا من السكربت).
→ `references/specs/beat-architecture.md`

### 6. ملف البرومبتات (الحالة 7)
`[slug]-prompts.txt` — كتل مفصولة بسطر فارغ، كل كتلة:
`SCENE` (60–120 كلمة) + **LOCK A حرفيًا** + **CLOSER حرفيًا**.
→ `schemas/prompts-txt.md`

### 7. Universal Video Prompt (الحالة 8)
`UNIVERSAL-VIDEO-PROMPT.txt` كما هو، مع استبدال `{DURATION}` فقط.

### 8. الثامبنيلات (الحالة 9)
3 برومبتات بزوايا مختلفة.
→ `workflows/shortcuts/thumbnail.md`

## القواعد الحاكمة
1. ❌ **لا تطلب أي ملف أو مرفق** من المستخدم.
2. ❌ لا تدمج حالتين، ولا تتجاوز حالة.
3. ❌ الأقفال حرفية — لا تُعَد صياغتها.
4. ❌ لا اختراع حقائق. المتنازع عليه يُكتب "حوله".
5. ❌ لا دماء، لا معاناة، لا سخرية من الضحايا.

## Next Step
- للسلسلة → `workflows/engines/E4-series-engine.md`
- للتنفيذ بالجملة → `workflows/engines/E5-bulk-production-pipeline.md`
- المحرك الكامل → `workflows/engines/E1-documentary-engine.md`
