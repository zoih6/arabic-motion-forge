---
name: product-truth
description: |
  حقيقة المنتج وثبات الهوية: مستويات الحقيقة T1–T4، جملة التثبيت Product Anchor،
  IMG-00 Product Sheet (حقيقي/خيالي/توسيع زاوية)، نمط الرفع حسب النموذج،
  قواعد الفئة السريعة، وحزمة الثبات المكوّنة من 8 طبقات.
tier: 3
when_to_load: "قبل أي برومبت يحتوي منتجًا (E2 مرحلة 5 · E3 مرحلة 5 · M4b)"
---

# Product Truth — حقيقة المنتج وثبات الهوية

## 1. لماذا هذا المرجع حاسم؟

النماذج التوليدية **تعيد اختراع المنتج في كل لقطة** ما لم تُقيَّد بـ:

```
مرجع بصري (IMG-00)  +  وصف نصي حرفي (Product Anchor)
```

| الحالة | نسبة الثبات |
|---|---|
| المرجع + الـ Anchor معًا | **~90%** |
| أحدهما وحده | ~50% |
| بلا أي منهما | <20% — المنتج يتغير كل لقطة |

---

## 2. مستويات حقيقة المنتج (Product Truth Tiers)

| المستوى | الحالة | المسموح | الممنوع |
|---|---|---|---|
| **T1 — Verified** | المستخدم أرفق صورًا، أو المنتج مشهور وشكله معروف بيقين | وصف دقيق للعبوة | أي انحراف عن الشكل الحقيقي |
| **T2 — Known, unverified** | منتج حقيقي لكن العبوة غير مؤكدة | وصف عام + Product Sheet ببرومبت بحث + طلب صورة بسطر واحد | تحديد ألوان/شعار بالتخمين |
| **T3 — Fictional / Concept** | منتج خيالي أو تصميم جديد | تصميم عبوة أصلي كامل | أي ادعاء يبدو واقعيًا عن علامة حقيقية |
| **T4 — Service / Idea** | لا يوجد منتج مادي | تعريف **"رمز ثابت"** بديل (أيقونة، مكان، شخصية قصاصة) يعمل كمنتج | إعلان بلا عنصر ثابت متكرر |

**قاعدة T2:** اسأل عن الصورة **مرة واحدة فقط** بسطر واحد داخل الرد الأول،
ثم تابع بافتراض معلن. **لا توقف الإنتاج.**

**قاعدة T3:** بعد توليد IMG-00 — **هذا التصميم أصبح الحقيقة.** لا تعديل لاحقًا.

---

## 3. جملة التثبيت — PRODUCT ANCHOR

جملة إنجليزية واحدة (**35–60 كلمة**) تُكتب مرة وتُلصق **حرفيًا** في كل برومبت
عند أول ذكر للمنتج.

### البنية

```
[the exact product name], a [form factor + size feel] [container type] in [primary color]
with [secondary color detail], [cap/closure description], [label/logo placement described
by position and shape, no invented text], [material + finish], [one distinctive detail],
rendered with exact real-world fidelity identical to the reference image.
```

### مثال (منتج خيالي)

```
the NIMBUS cold brew can, a slim 330ml aluminum can in matte midnight blue with a single
thin cream band around the upper third, a silver pull-tab lid, a small circular cream
emblem centered on the band, soft-touch matte finish with faint condensation, rendered
with exact real-world fidelity identical to the reference image.
```

### القواعد

- ❌ **لا تغيّر كلمة واحدة** بين برومبت وآخر. الثبات النصي = ثبات بصري.
- ❌ لا تذكر نص الشعار الحرفي إلا إذا كان مؤكدًا **وقصيرًا** (≤ 2 كلمات) — النماذج تشوّه النصوص.
- ✅ للمنتج **T2** اختم بـ:
  `matching the official real-world packaging exactly, no invented details`
- ✅ للمنتج **T3** احذف عبارة `identical to the reference image` وأضف `original design`.

---

## 4. IMG-00 — Product Sheet

### 4.1 منتج حقيقي (T1/T2)

```
Create a professional product reference sheet of [PRODUCT ANCHOR]. Base every detail
strictly on the real product as sold by [BRAND]; do not invent, add, or alter any element
of the packaging, cap, label, proportions, or colors. Show the identical product from six
angles arranged in a clean grid: front, three-quarter left, side profile, back, top-down,
and one macro close-up of [the most distinctive detail]. Proportions, geometry, colors,
and label placement must be perfectly consistent across all views. Neutral seamless studio
background in [soft gray / warm white / deep charcoal], even professional studio lighting
revealing true materials and reflections, no props, no extra text, no other products.
Purpose: an accurate, locked visual reference for a commercial. Photoreal, sharp, {AR}.
```

### 4.2 منتج خيالي (T3)

```
Design an original [category] package: [PRODUCT ANCHOR without the "identical to reference"
clause]. No readable brand text on the label (a clean emblem shape only; the logo will be
added in post). Show it from six angles arranged in a clean grid: front, three-quarter left,
side profile, back, top-down, and one macro close-up of [distinctive detail]. Proportions,
geometry, colors, and emblem placement must be perfectly consistent across all views.
Neutral seamless studio background in [color], even professional studio lighting revealing
true materials, no props, no extra text. Photoreal, sharp, {AR}.
```

### 4.3 توسيع صورة واحدة إلى مرجع متعدد الزوايا

```
Using ONLY the product shown in the attached image, create additional reference views of
the exact same product with zero changes to its shape, colors, label, cap, or proportions:
three-quarter left, side profile, back, top-down, and one macro of [detail]. Match the
attached image's materials and finish precisely. Neutral seamless [color] studio background,
even lighting, no props, no extra text. Photoreal, {AR}.
```

### 4.4 الخدمة أو الفكرة (T4)

لا Product Sheet للمنتج — بل **Signature Element Sheet**: عرّف رمزًا ثابتًا،
وصمّمه من 6 زوايا بنفس منطق IMG-00، وعامله معاملة المنتج تمامًا
(Anchor + Entity Ledger + حضور دوري).

---

## 5. جدول القرار

| الحالة | الفعل |
|---|---|
| صور واضحة متعددة من المستخدم | **لا Product Sheet.** اكتب الـ Anchor من الصور، وارفع صور المستخدم مع كل برومبت |
| صورة واحدة بزاوية واحدة | IMG-00 "توسيع زوايا" (§4.3) |
| منتج حقيقي معروف بلا صور (T2) | IMG-00 ببرومبت بحث + منع اختراع (§4.1) + اطلب صورة بسطر واحد |
| منتج خيالي (T3) | IMG-00 تصميم أصلي (§4.2)، ثم اقفل هويته كأنه حقيقي |
| خدمة/فكرة (T4) | Signature Element Sheet (§4.4) |

---

## 6. نمط الرفع حسب النموذج

| النموذج | كيف يستهلك المرجع |
|---|---|
| **Midjourney (v7+)** | `--oref [url]` للمنتج (Omni Reference) + `--sref` للأسلوب |
| **Flux (2 / Kontext)** | صورة مرجع + تعليمات تعديل؛ يحافظ على الهوية ممتازًا |
| **Nano Banana / Gemini Image** | حتى 3 صور مرجع في الرسالة نفسها + وصف — **الأفضل للثبات متعدد اللقطات** |
| **GPT Image** | صورة مرجع + تعليمات؛ جيد للتركيب |
| **Veo 3.x** | Ingredients/reference images (حتى 3) أو first frame |
| **Kling 2.x** | Elements (مرجع للكيان) + start/end frames |
| **Runway Gen-4** | References (حتى 3 صور) + وصف يربط `@product` |
| **Sora 2** | صورة أولى + وصف؛ الثبات أضعف — **اعتمد على الـ Anchor النصي** |

> **عندما لا يدعم النموذج مرجعًا:** الـ Anchor النصي الحرفي هو **خط الدفاع الوحيد** — لا تختصره.

---

## 7. حزمة الثبات (Consistency Stack) — 8 طبقات

| # | الطبقة | ما تحميه |
|---|---|---|
| 1 | **Anchor حرفي** في كل برومبت | هوية المنتج (نص) |
| 2 | **IMG-00 مرفوع** مع كل برومبت | هوية المنتج (بصري) |
| 3 | **Style Lock حرفي** | الأسلوب |
| 4 | **Entity Ledger** | الكيانات المتكررة |
| 5 | **Seed ثابت** حيث يتوفر (`--seed 1234`) | التشابه العشوائي |
| 6 | **الصورة السابقة كمرجع ثانٍ** | الاستمرارية بين اللقطات |
| 7 | **زاوية كاميرا موحدة** بين Start/End frames | الاستمرارية الزمنية |
| 8 | **جملة ضوء واحدة** في كل لقطة | وحدة المكان |

> **الضوء المختلف = مكان مختلف في عين المشاهد.**

---

## 8. قواعد الفئة السريعة (Category Heuristics)

| الفئة | الخاصية الحسية المحورية | خطر شائع |
|---|---|---|
| طعام/مشروبات | الملمس، البخار، القرمشة، السيلان | ادعاءات صحية؛ أطعمة تبدو بلاستيكية |
| عطور/تجميل | الضوء على الزجاج، السائل، البشرة الانطباعية | وجوه واقعية؛ ادعاءات نتائج |
| تقنية/أجهزة | الدقة، الحواف، الضوء البارد، الواجهة | UI مخترعة؛ نص على الشاشة |
| أزياء/إكسسوارات | القماش، الحركة، الملمس | أيدٍ وأجساد مشوّهة |
| تطبيقات/خدمات | الرمز البديل، الأثر في الحياة | إعلان بلا عنصر ثابت |
| سيارات | الانعكاسات، الخط الجانبي، الضوء | نسب الهيكل؛ شعارات مقلدة |
| منزل/أثاث | المادة، الضوء الطبيعي، المقياس | مقاييس غير منطقية |
| عناية/صحة | النقاء، الماء، اللمسة الناعمة، البياض | ادعاءات طبية؛ قبل-بعد؛ أجساد واقعية |
| أطفال/ألعاب | المرح، الألوان، الحركة النطّاطة | وجوه أطفال واقعية؛ أمان الرسالة |
| فخامة | الثقل، الصمت، المساحة السلبية، الضوء الواحد | over-design؛ كثرة العناصر |

---

## 9. قواعد التغطية والحضور

- المنتج **لا يُغطَّى أبدًا** بأكثر من **15%** من مساحته في أي لقطة.
- في **Hero Shot**: تغطية **0%**.
- المنتج/أثره يظهر كل ≤ 3 ثوانٍ (≤ 2 ث في 6–10 ثوانٍ).
  → `references/specs/beat-architecture.md` § 8

---

## 10. القيود السلبية الإجبارية للمنتج

اختر ≤ 6 لكل برومبت، ولا تناقض الإيجابي:

```
No changes to the product's shape, colors, proportions, cap, or label.
No other products or brands.
No text, no letters, no watermark.
No hands, no people, no faces.
No elements not described here.
No morphing, no object replacement, no camera shake, no cuts, no transitions.
```

---

## Cross-Reference

- `references/specs/entity-ledger.md` — سجل الكيانات
- `references/specs/model-dialects.md` — لهجة كل نموذج
- `schemas/product-sheet.md` — قالب Product Sheet
- `references/specs/copywriting-and-text-in-images.md` — قواعد النص
