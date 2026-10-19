---
name: shortcut-series
description: "تخطيط سلسلة أو قناة أو موسم: النيش، الأقاليم الفرعية، توقيع القناة المقفول، خطة الحلقات."
tier: 2
parent: workflows/engines/E4-series-engine.md
duration: 15-30 min للخطة
quality_gates: [G1, G13]
---

# Shortcut: Series — تخطيط سلسلة/قناة

## Entry Conditions
- ✅ طلب: "سلسلة"، "قناة"، "موسم"، "خطة شهر"، "تقويم محتوى"، "عدة حلقات"
- ❌ حلقة واحدة فقط → `workflows/engines/E1-documentary-engine.md`

## Core Workflow (5 خطوات)

### 1. حدد النيش (2 min)
**نيش واحد** للسلسلة كلها. لا تخلط نيشين.

### 2. وزّع الأقاليم الفرعية (5 min)
3–5 أقاليم من بنك النيش:

| النيش | الأقاليم الفرعية |
|---|---|
| جريمة | سرقة، اختفاء، احتيال، مطاردة، قضية باردة، تجسس، هروب |
| تاريخ | معركة، سقوط إمبراطورية، قرار مصيري، اختراع، مؤامرة |
| مال وسلطة | انهيار، احتيال ضخم، صعود أسطورة، صفقة غامضة |
| ألغاز | اختفاء غير مفهوم، رصد غير مفسر، رمز غير محلول |
| تقنية | انهيار نظام، اختراع غيّر كل شيء، سباق، خرق أمني |

### 3. اقفل توقيع القناة (5 min)
7 كيانات بوصف إنجليزي حرفي واحد، تُستخدم في كل الحلقات:

```
PAPER-STOCK        "aged newsprint with visible print grain and tan staining"
SIGNATURE-RED      "one hot red marker circle drawn with a rough hand"
LABEL-SYSTEM       "condensed bold all-caps typewriter caption strips"
MAP-BASE           "a folded archival map base with visible crease lines"
THUMBNAIL-DEVICE   "a rough red marker circle around the key element"
LIGHT-RULE         "flat even documentary lighting with soft cutout drop shadows"
VOICE-ID           [ElevenLabs Voice ID]
```

### 4. خطّط الحلقات (10 min)
| # | العنوان | الإقليم | المرساة الملموسة | المدة |
|---|---|---|---|---|
| 01 | [العنوان] | سرقة | [تاريخ · مكان · رقم] | 2:00 |

**قواعد الترتيب:**
1. الحلقة **الأقوى هوكًا** أولًا.
2. ❌ لا حلقتان متتاليتان من نفس الإقليم.

### 5. حدد الوتيرة (2 min)
| المستوى | الوتيرة |
|---|---|
| مبتدئ | 1–2 حلقة/أسبوع |
| متوسط | 2–3 حلقة/أسبوع |
| متقدم | 4–7 حلقة/أسبوع |
| حملة | كل الأجزاء جاهزة قبل الإطلاق |

## ما يُعرض للمستخدم
✅ **قائمة العناوين + سطر مرساة لكل حلقة** فقط.
❌ لا تُعرض الخطة الداخلية (الأقاليم، الكيانات، السجل).

## Common Mistakes
- ❌ إنتاج حلقتين في رد واحد.
- ❌ تكرار موضوع أنتجته (راجع السجل).
- ❌ تغيير توقيع القناة "للتنويع".
- ❌ عرض الخطة الداخلية للمستخدم.

## Next Step
- تنفيذ الحلقات → `workflows/engines/E4-series-engine.md`
- الوثائقي → `workflows/engines/E1-documentary-engine.md`
- القالب → `schemas/series-bible.md`
