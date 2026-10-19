---
name: schema-product-sheet
description: "قالب Product Sheet (IMG-00): جملة التثبيت Product Anchor + برومبت الـ 6 زوايا (حقيقي/خيالي/توسيع) + تعليمات الاستخدام للمنفّذ."
tier: 3
when_to_load: "E2 المرحلة 5 · E3 المرحلة 5 · M4b · M11a"
---

# Product Sheet (IMG-00)

## 1. جملة التثبيت — PRODUCT ANCHOR

> جملة إنجليزية واحدة (**35–60 كلمة**). تُكتب **مرة واحدة** وتُلصق **حرفيًا** في كل برومبت.

### البنية

```
[the exact product name], a [form factor + size feel] [container type] in [primary color]
with [secondary color detail], [cap/closure description], [label/logo placement described
by position and shape, no invented text], [material + finish], [one distinctive detail],
rendered with exact real-world fidelity identical to the reference image.
```

### مثبت

```
ANCHOR: ______________________________________________________________
        ______________________________________________________________
        ______________________________________________________________
```

### مثال

```
the NIMBUS cold brew can, a slim 330ml aluminum can in matte midnight blue with a single
thin cream band around the upper third, a silver pull-tab lid, a small circular cream
emblem centered on the band, soft-touch matte finish with faint condensation, rendered
with exact real-world fidelity identical to the reference image.
```

---

## 2. برومبت الـ Product Sheet

### 2.1 منتج حقيقي (T1/T2)

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

### 2.2 منتج خيالي (T3)

```
Design an original [category] package: [PRODUCT ANCHOR without the "identical to reference"
clause]. No readable brand text on the label (a clean emblem shape only; the logo will be
added in post). Show it from six angles arranged in a clean grid: front, three-quarter left,
side profile, back, top-down, and one macro close-up of [distinctive detail]. Proportions,
geometry, colors, and emblem placement must be perfectly consistent across all views.
Neutral seamless studio background in [color], even professional studio lighting revealing
true materials, no props, no extra text. Photoreal, sharp, {AR}.
```

### 2.3 توسيع صورة واحدة

```
Using ONLY the product shown in the attached image, create additional reference views of
the exact same product with zero changes to its shape, colors, label, cap, or proportions:
three-quarter left, side profile, back, top-down, and one macro of [detail]. Match the
attached image's materials and finish precisely. Neutral seamless [color] studio background,
even lighting, no props, no extra text. Photoreal, {AR}.
```

### 2.4 خدمة/فكرة (T4) — Signature Element

```
Create a professional reference sheet of a single signature graphic element: [وصف الرمز].
No readable text, no brand marks. Show the identical element from six angles arranged in a
clean grid: front, three-quarter left, side profile, back, top-down, and one macro close-up
of [أكثر تفصيل مميّز]. Geometry, proportions, and color must be perfectly consistent across
all views. Neutral seamless studio background, even lighting, no props. Purpose: a locked
visual anchor for a campaign. {AR}.
```

---

## 3. سجل حقائق المنتج

```yaml
PRODUCT TRUTH — Tier [T1–T4]
──────────────────────────────────────
الاسم الرسمي:
الفئة:
الشكل / الحجم:
اللون الأساسي:
اللون الثانوي:
الغطاء / الإغلاق:
موضع الشعار:        [بالموضع والشكل — لا نص مخترع]
المادة والتشطيب:
التفصيل المميّز:     [واحد]
الادعاءات المسموحة:  [أو «لا شيء»]
مستند الحقيقة:       [رابط/صورة/برومبت البحث]
```

---

## 4. تعليمات الاستخدام للمنفّذ (تظهر في الحزمة)

> ولّد IMG-00 أولًا واحفظه. إن خرجت أي زاوية غير مطابقة لمنتجك الحقيقي،
> أعد التوليد أو استبدلها بصورتك — **الثبات أهم من الجمال هنا**.
>
> ارفع IMG-00 (أو صورتك) مع **كل** برومبت صورة وفيديو في الحزمة.
> في النماذج التي تدعم مراجع متعددة، ارفع **IMG-00 + صورة اللقطة السابقة** معًا.

---

## 5. نمط الرفع حسب النموذج

| النموذج | كيف يستهلك المرجع |
|---|---|
| Midjourney | `--oref [url]` للمنتج + `--sref` للأسلوب |
| Flux Kontext | صورة مرجع + تعليمات تعديل |
| Nano Banana | حتى 3 صور مرجع في الرسالة نفسها |
| GPT Image | صورة مرجع + تعليمات |
| Veo 3.x | Ingredients (حتى 3) أو first frame |
| Kling 2.x | Elements + start/end frames |
| Runway Gen-4 | References بـ `@product` |
| Sora 2 | صورة أولى + Anchor نصي حرفي إجباري |

→ `references/specs/product-truth.md` § 6

---

## 6. قائمة فحص Product Sheet

- [ ] الـ Anchor مكتوب (35–60 كلمة)؟
- [ ] الـ Anchor خالٍ من نص شعار مخترع؟
- [ ] 6 زوايا مطلوبة في البرومبت؟
- [ ] الخلفية محايدة ومحددة؟
- [ ] مستوى الحقيقة (T1–T4) موثّق؟
- [ ] الادعاءات: إما موثّقة أو محذوفة؟
- [ ] للـ T2: انتهى بـ `no invented details`؟
- [ ] تعليمات الاستخدام مرفقة في الحزمة؟

---

## Cross-Reference

- `references/specs/product-truth.md` — المرجع الكامل
- `references/specs/entity-ledger.md` — السجل
- `references/specs/model-dialects.md` — لهجات النماذج
