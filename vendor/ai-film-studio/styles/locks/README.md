---
name: style-locks
description: |
  الأقفال النصية الحرفية للعوالم البصرية العشرة (LOCK A–J) + الخواتيم (Closers) +
  برومبت الفيديو الموحد. هذه الملفات تُنسخ حرفيًا داخل البرومبتات، ولا تُقرأ فقط.
tier: 3
when_to_load: "عند كتابة أي برومبت صورة أو فيديو — بعد اختيار العالم البصري"
---

# الأقفال النصية (Style Locks)

## ⚠️ القاعدة الذهبية — غير قابلة للتفاوض

**هذه الملفات تُنسخ حرفيًا (verbatim). يُمنع إعادة صياغتها أو ترجمتها أو اختصارها.**

السبب: النماذج التوليدية حسّاسة جدًا للصياغة. تغيير كلمة واحدة في القفل بين لقطة وأخرى
يجعل النموذج يولّد عالمين مختلفين — فيبدو الإعلان كـ 12 صورة عشوائية بدل فيلم واحد.

| ✅ افعل | ❌ لا تفعل |
|---|---|
| انسخ القفل كما هو في كل برومبت | أعد صياغته "ليكون أجمل" |
| استبدل `{PALETTE}` و `{AR}` فقط | أضف صفات من عندك داخل القفل |
| استخدم نفس القفل لكل لقطات المشروع | بدّل الأقفال بين اللقطات |
| أنشئ `LOCK-K` جديدًا إن احتجت تعديلًا | عدّل ملف قفل موجود |

## الملفات

| الملف | الوصف | يُنسخ إلى |
|---|---|---|
| `LOCK-A-documentary-archive.txt` | كولاج وثائقي أرشيفي — توقيع VOX | كل برومبت وثائقي |
| `LOCK-B-commercial-craft.txt` | كولاج ورقي تجاري — **الافتراضي للمنتجات** | كل برومبت منتج |
| `LOCK-C-noir-luxury.txt` | ورق أسود مطفي + ذهب — فخامة | عطور، ساعات |
| `LOCK-D-pop-cutout.txt` | ألوان مسطحة نطّاطة — مرح | سناكس، مشروبات، شباب |
| `LOCK-E-miniature-tabletop.txt` | ديوراما طاولة مصغّرة سينمائية | تقنية، أجهزة، سيارات |
| `LOCK-F-photoreal-studio.txt` | تصوير استوديو واقعي بلا ورق | عند رفض الكولاج |
| `LOCK-G-mixed-media-editorial.txt` | ميديا مختلطة تحريرية | مجلات، أزياء، ثقافة |
| `LOCK-H-clay-diorama.txt` | طين/صلصال مصغّر | سناكس، أطفال، حملات دافئة |
| `LOCK-I-flat-vector-explainer.txt` | **Flat Vector — نمط VOX المسطح** | شروح، بيانات، infographic |
| `LOCK-J-arabic-calligraphic.txt` | هوية عربية معاصرة | مشاريع عربية، تراث، رمضان |
| `LOCK-K-oversized-ink-editorial.txt` | ملصق تحريري بأشكال ضخمة وحبر مطبوع | ملصقات 9:16، سوشيال، شخصيات مبسطة |
| `CLOSER-master.txt` | الخاتمة العامة (تجاري/عام) | آخر سطر في برومبت الصورة |
| `CLOSER-documentary.txt` | الخاتمة الوثائقية | آخر سطر في برومبت وثائقي |
| `CLOSER-thumbnail.txt` | خاتمة الثامبنيل | آخر سطر في برومبت ثامبنيل |
| `UNIVERSAL-VIDEO-PROMPT.txt` | برومبت الفيديو الموحد (Build-On Assembly) | كل صورة → فيديو |

## الاستبدالات المسموحة

| الرمز | يستبدل بـ | مثال |
|---|---|---|
| `{AR}` | نسبة الأبعاد | `16:9` / `9:16` / `1:1` / `4:5` / `2.39:1` |
| `{PALETTE}` | 3–5 ألوان بالضبط | `warm kraft brown, cream, burnt sienna` |
| `{DURATION}` | مدة المقطع بالثواني | `10` |

> **تنبيه:** القفلان A و J لا يحتويان على `{PALETTE}` — لوحتهما مثبّتة بداخلهما.
> القفل A يثبّت `16:9` داخل النص؛ للعمودي غيّر الرقم داخل القفل لهذه الحلقة فقط
> وأبلِغ المستخدم بسطر واحد أن الوضع العمودي حالة خاصة.

## تبديلات الخاتمة حسب القفل

| القفل | السطر الأول من الخاتمة |
|---|---|
| A, B, D, E, G | `CLOSER-master.txt` كما هو |
| C | استبدل: `minimalist luxury paper-craft finish, deep matte black surfaces, one warm gold accent` |
| F | استبدل: `Physically accurate, photoreal, no stylization.` |
| H | استبدل: `Every element must appear physically hand-sculpted from real clay with visible thumb texture and soft rounded forms; the product the only photoreal object.` |
| I | استبدل: `Crisp flat-vector execution, solid fills, clean edges, modular grid, infographic clarity.` |
| J | استبدل: `Contemporary Arabic editorial execution, flat confident fields, calligraphic architecture, all text added in post.` |
| K | استخدم `CLOSER-oversized-ink-editorial.txt` حرفيًا |

## موضع القفل داخل البرومبت

```
[1 FRAME]      →  [2 ANCHOR]  →  [3 SCENE]  →  [4 COMPOSE]  →  [5 CAMERA]
→  [6 LIGHT]  →  [7 MATERIALS]  →  [8 MOOD]  →  [9 STYLE LOCK ← هنا]  →  [10 CLOSER]  →  [11 NEGATIVE]
```

الطول المستهدف قبل القفل: **120–220 كلمة**. أقل = غموض. أكثر = النموذج يتجاهل النصف الثاني.

## بروتوكول الأقفال الكامل

→ `references/protocols/style-lock-protocol.md`
→ اختيار العالم: `styles/index.md`
