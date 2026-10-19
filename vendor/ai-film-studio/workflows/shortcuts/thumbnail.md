---
name: shortcut-thumbnail
description: "ثامبنيل واحد أو ثلاثة لفيديو — من خطاف الفيديو نفسه. للوثائقي والإعلان."
tier: 2
parent: references/specs/thumbnail-dna.md
duration: 5-10 min
style_lock: CLOSER-thumbnail.txt
quality_gates: [G12, G6]
---

# Shortcut: Thumbnail — الثامبنيل

## Entry Conditions
- ✅ طلب: "ثامبنيل"، "صورة مصغّرة"، "غلاف الفيديو"، "thumbnail"
- ❌ ليس فيديو كاملًا (راجع المحركات)

## Core Workflow (5 خطوات)

### 1. استخرج الخطاف (1 min)
من عنوان الفيديو أو أول Hook:
- الكلمة الحسّية الأقوى (VANISHED · EXPOSED · FOUND · STOLEN)
- السنة أو الرقم الصادم (1971 · $200,000.00)
- للعربية: كلمة إلى كلمتين قصيرتين (اختفى · مكشوف · 200 ألف)

### 2. حدّد البطل (1 min)
| النوع | البطل |
|---|---|
| وثائقي | شيء / شخصية هالفتون / مكان |
| إعلان | المنتج أو أثره الأقوى |

### 3. املأ القالب (2 min)
```
A [وصف الموضوع] as the dominant hero cutout in high-contrast black and white halftone
with rough scissor-cut edges and a red offset accent stroke, [شريط رقابة إن كان شخصًا],
set on aged torn newsprint that bleeds off frame, a huge condensed all-caps torn-label
headline reading [1-3 WORDS] in black on a [red or yellow] bar, a second smaller
stamp-box label reading [1-3 WORDS], one rough red marker [circle or underline] around
the key element, desaturated tan and ink palette with hot red and mustard accents,
extreme contrast, poster-scale readability.

[CLOSER-THUMBNAIL حرفيًا]
```

### 4. فحص الـ 200 بكسل (1 min)
صغّر ذهنيًا لعرض 200 بكسل:
1. البطل ما زال مميزًا فورًا؟
2. النصوص مقروءة؟
3. جهاز التمييز ظاهر؟

أي "لا" → بسّط: أقص عناصر، كبّر الخط، زد التباين.

### 5. سلّم 3 زوايا (2 min)
| # | الزاوية |
|---|---|
| 01 | البطل مهيمن + كلمة واحدة |
| 02 | الرقم/السنة مهيمن + البطل جزئيًا |
| 03 | زاوية غير متوقعة (الوثيقة، المكان، الأثر) |

> ❌ **3 زوايا مختلفة، لا نفس الفكرة بظلال مختلفة.**

## القوانين الستة
1. بطل هالفتون مهيمن **واحد**.
2. نص **≤ عنصرين**، **3 كلمات** لكل عنصر.
3. جهاز تمييز **واحد** فقط.
4. قاعدة نشرات ممزقة تنزف خارج الإطار، تباين حاد.
5. ❌ بلا تفاصيل صغيرة · ❌ بلا علامة مائية · ❌ بلا شعارات.
6. المبالغ المالية بكسور سنتات دائمًا ($200,000.00).

## Common Mistakes
- ❌ أكثر من عنصري نص.
- ❌ أكثر من جهاز تمييز.
- ❌ وجه حقيقي واضح بلا شريط رقابة.
- ❌ توليد نص عربي داخل الصورة — استخدم طبقة نص في المونتاج.
- ❌ نسخ نفس الفكرة ثلاث مرات.

## Next Step
- للسلسلة → `workflows/engines/E4-series-engine.md` (جهاز تمييز موحّد)
- للوثائقي الكامل → `workflows/engines/E1-documentary-engine.md`
- للإعلان → `workflows/engines/E2-commercial-engine.md`
- القالب → `schemas/thumbnail-pack.md`
