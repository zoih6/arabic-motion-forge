---
name: example-paper-collage-documentary
description: "مثال حي كامل لحلقة وثائقية بأسلوب الكولاج الورقي (E1) — من Cold Open إلى الثامبنيل."
tier: 3
engine: E1-documentary-engine
style_lock: LOCK-A-documentary-archive
duration: "1:00"
---

# مثال حي — حلقة وثائقية: «البريد الذي لم يصل»

> **المعيار المقفول للجودة والصيغة.** كل حلقة E1 يجب أن تصل إلى هذا المستوى.
> الموضوع خيالي تعليمي — صُمّم ليوضّح البنية لا ليُنشر.

---

## المدخلات

| الحقل | القيمة |
|---|---|
| النيش | ألغاز واختفاءات |
| الموضوع | بريد اختفى في محطة فرز واحدة، 1974 |
| المدة | 1:00 |
| النسبة | 16:9 |
| القفل | LOCK-A |
| عدد الـ Beats | 24 |

---

## الحالة 4 — السكربت

**TARGET: 150 كلمة · FINAL: 148 كلمة**

```
في الرابع عشر من مارس 1974، غادرت شاحنة بريد محطة فرز في مدينة سالم وهي تحمل
أحد عشر ألف رسالة. وصلت تسعة آلاف وثمانمئة وأربعة وثمانون رسالة فقط.

المسافة بين المحطة ومكتب التوزيع اثنا عشر كيلومترًا، والطريق مستقيم لا يتفرع.
سجّل الحارس وقت الخروج ووقت الوصول، والفرق بينهما أربع وثلاثون دقيقة — أطول
بعشر دقائق من المعتاد. لم يُبلَّغ عن أي حادث في ذلك اليوم.

فتّش المفتشون الشاحنة، والطريق، والمحطة. لم يجدوا شيئًا. وصف أحد العمّال
الشاحنة بأنها بدت أخف عند الوصول، لكنه تراجع عن قوله في الإفادة الثانية.

أُغلقت القضية بعد أحد عشر شهرًا. ولم تُفتح قط.

ما زال سجلّ الحارس محفوظًا في أرشيف الولاية، وعليه سطر واحد مكتوب بخط اليد:
«الوزن لا يطابق». لا أحد يعرف ماذا كان يقصد.
```

**التحقق الداخلي:**
- ✅ Cold Open ثلاثي: تاريخ (14 مارس 1974) + مكان (محطة فرز في سالم) + فعل (شاحنة غادرت)
- ✅ Cliffhanger: النمط 1 (الشيء غير المحلول) — «لا أحد يعرف ماذا كان يقصد» (6 كلمات)
- ✅ 148 كلمة ≈ 150 (±5%)
- ✅ ❌ لا CTA، ❌ لا مقدمات، ❌ لا em dash، ❌ لا إيموجي

---

## الحالة 6 — جدول الـ Beats (مقتطف)

| Beat | التوقيت | الكلمات |
|---|---|---|
| 1 | 0.0s | "في الرابع عشر من مارس 1974،" |
| 2 | 1.6s | "غادرت شاحنة بريد محطة فرز في مدينة سالم" |
| 3 | 3.6s | "وهي تحمل أحد عشر ألف رسالة." |
| 4 | 5.6s | "وصلت تسعة آلاف وثمانمئة وأربعة وثمانون رسالة فقط." |
| 5 | 9.2s | "المسافة بين المحطة ومكتب التوزيع اثنا عشر كيلومترًا،" |
| ... | ... | ... |
| 24 | 56.4s | "لا أحد يعرف ماذا كان يقصد." |

> **كل كلمة مغطاة مرة واحدة بالضبط.** 24 Beat × ~6.2 كلمة ÷ 2.4 (عربي) ≈ 60 ثانية.

---

## الحالة 7 — كتلة برومبت (Beat 4)

```
SCENE: A single tan postal sack with a stenciled number sits slumped and half-empty at the
center of the frame, its mouth folded open showing only a few loose envelopes inside. Around it,
eleven tall stacks of cream envelopes arranged in a grid, each stack shorter than a human hand,
casting long soft shadows. The background is aged newsprint with visible print grain and a faint
coffee ring stain in the lower left. A single short label reading "9,984" on a paper strip sits
beneath the sack. Generous negative space above and to the right. One red cotton thread runs
from the sack off the right edge of the frame.

hand-cut documentary paper collage on aged newsprint and archival map surfaces, black and white
halftone photograph cutouts with rough scissor-cut edges and offset accent strokes, torn paper
edges, masking tape fragments, typewriter caption strips, rubber stamp marks, red string and
brass pins where the story calls for connections, desaturated archival palette of tan, ink black,
and halftone gray with ONE hot red signal accent and a restrained mustard yellow secondary,
condensed bold headline lettering only where a label is specified, visible print grain and paper
fiber, matte, flat even documentary lighting with soft cutout drop shadows.

Every element must appear physically hand-cut and layered from real paper, with visible cutout
edges, halftone print texture, and soft shadow separation between layers. The composition stays
clean, minimal, and editorial with generous negative space. NOT digital illustration, NOT
cartoon, NOT 3D render, NOT glossy, no gradients, no clutter, no watermark, no logos, no text
beyond the specified label. Premium documentary collage aesthetic, 16:9, ultra-detailed, 8K.
```

**قائمة فحص الكتلة:**
- ✅ بطل واحد (الكيس) ~70% من الثقل
- ✅ 3 عناصر مساندة (الأكوام، الخلفية، الخيط)
- ✅ تسمية واحدة 1 كلمة ("9,984")
- ✅ LOCK A حرفيًا · CLOSER حرفيًا
- ✅ 74 كلمة للقسم المشهدي (60–120)
- ✅ سجل الكيانات: "a single tan postal sack with a stenciled number" — نفس العبارة في كل ظهور

---

## الحالة 8 — Universal Video Prompt

يُسلَّم `UNIVERSAL-VIDEO-PROMPT.txt` كما هو، مع `{DURATION}` = 10.

**قاعدة التطبيق:** نفس البرومبت على كل الصور بلا أي تغيير.

---

## الحالة 9 — الثامبنيلات (3 زوايا)

### 01 — البطل مهيمن
```
A single tan postal sack as the dominant hero cutout in high-contrast black and white halftone
with rough scissor-cut edges and a red offset accent stroke, set on aged torn newsprint that
bleeds off frame, a huge condensed all-caps torn-label headline reading "VANISHED" in black on
a red bar, a second smaller stamp-box label reading "1974", one rough red marker circle around
the sack, desaturated tan and ink palette with hot red and mustard accents, extreme contrast,
poster-scale readability.
+ [CLOSER-THUMBNAIL حرفيًا]
```

### 02 — الرقم مهيمن
```
The number 9,984 as a massive torn typewriter-strip cutout dominating the upper two thirds of
the frame in high-contrast halftone, a much smaller postal sack cutout in the lower right corner,
a second stamp-box label reading "1974", one rough red marker underline beneath the number,
desaturated tan and ink palette, extreme contrast, poster-scale readability.
+ [CLOSER-THUMBNAIL حرفيًا]
```

### 03 — زاوية غير متوقعة (الوثيقة)
```
A single handwritten guard log page as the hero cutout, torn at the right edge, the words
rendered as an abstract halftone scribble rather than readable text, one rough red marker circle
around a single underlined line, a postal sack silhouette cutout reduced to a small shape in the
lower left, desaturated tan and ink palette with one hot red accent, extreme contrast,
poster-scale readability.
+ [CLOSER-THUMBNAIL حرفيًا]
```

**فحص الـ 200 بكسل:**
1. البطل مميز فورًا؟ ✅ كيس/رقم/صفحة — كلها أشكال كبيرة بسيطة
2. النصوص مقروءة؟ ✅ كلمة واحدة أو رقم في كل ثامبنيل
3. جهاز التمييز ظاهر؟ ✅ دائرة حمراء / تسطير

---

## الحالة 5 — التعليق الصوتي

| الإعداد | القيمة |
|---|---|
| الصوت | راوي رزين، مدى متوسط، هيبة خفيفة |
| السرعة | ~150 كلمة/دقيقة |
| Stability | 55 |
| Similarity | 80 |
| Style | منخفض |
| Speaker Boost | مفعّل |

**الدفعات (20–25 ثانية ≈ 50–60 كلمة):**
```
د 1 (0–22s):   "في الرابع عشر من مارس 1974، غادرت شاحنة بريد محطة فرز في مدينة سالم
                وهي تحمل أحد عشر ألف رسالة. وصلت تسعة آلاف وثمانمئة وأربعة وثمانون
                رسالة فقط."
د 2 (22–44s):  "المسافة بين المحطة ومكتب التوزيع اثنا عشر كيلومترًا، والطريق مستقيم
                لا يتفرع. سجّل الحارس وقت الخروج ووقت الوصول، والفرق بينهما أربع
                وثلاثون دقيقة. لم يُبلَّغ عن أي حادث في ذلك اليوم."
د 3 (44–60s):  "فتّش المفتشون الشاحنة، والطريق، والمحطة. لم يجدوا شيئًا. أُغلقت القضية
                بعد أحد عشر شهرًا. ما زال سجلّ الحارس محفوظًا، وعليه سطر واحد:
                «الوزن لا يطابق». لا أحد يعرف ماذا كان يقصد."
```

> **دفعة البداية الباردة (د 1) أعلى أولوية** — تُعاد توليدها 5 مرات.

---

## قائمة فحص الحلقة (G9 · G10 · G4)

- [x] Cold Open ثلاثي
- [x] Cliffhanger ≤ 12 كلمة
- [x] 148 كلمة (الهدف 150 ±5%)
- [x] 24 Beat داخل النطاق (22–30 لدقيقة)
- [x] كل كلمة مغطاة مرة واحدة
- [x] كل كتلة برومبت مستقلة
- [x] LOCK A + CLOSER حرفيان
- [x] سجل كيانات موحّد
- [x] 3 ثامبنيلات بزوايا مختلفة
- [x] لا نص عربي داخل الصور
- [x] لا وجوه، لا أيدٍ

---

## التالي

- المحرك الكامل → `workflows/engines/E1-documentary-engine.md`
- ملف البرومبتات → `schemas/prompts-txt.md`
- للسلسلة → `workflows/engines/E4-series-engine.md`
