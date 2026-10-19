---
name: shortcut-product-shot
description: "مرجع منتج مقفول (IMG-00) + جملة تثبيت (Product Anchor) — أساس ثبات الهوية في أي إعلان."
tier: 2
parent: references/specs/product-truth.md
duration: 5-10 min
quality_gates: [G11]
---

# Shortcut: Product Shot — مرجع المنتج المقفول

## Entry Conditions
- ✅ طلب: "صورة منتج"، "برومبت منتج"، "مرجع منتج"، "product reference"
- ✅ أو: على وشك كتابة أي برومبت يحتوي منتجًا

> **هذه الخطوة إجبارية قبل أي برومبت منتج.** بدونها يعيد النموذج اختراع المنتج كل لقطة.

## لماذا
| الحالة | نسبة الثبات |
|---|---|
| مرجع + Anchor معًا | **~90%** |
| أحدهما وحده | ~50% |
| بلا أي منهما | <20% |

## Core Workflow (4 خطوات)

### 1. حدّد مستوى الحقيقة (1 min)
| المستوى | الحالة | الإجراء |
|---|---|---|
| **T1** | صور واضحة | لا Product Sheet — Anchor من الصور |
| **T2** | منتج حقيقي، العبوة غير مؤكدة | Product Sheet + طلب صورة بسطر واحد |
| **T3** | خيالي | تصميم عبوة أصلي |
| **T4** | خدمة/فكرة | **رمز ثابت** بديل |

### 2. اكتب الـ Product Anchor (3 min)
جملة إنجليزية **35–60 كلمة**، تُكتب مرة وتُلصق حرفيًا:

```
[product name], a [form factor + size feel] [container type] in [primary color] with
[secondary color detail], [cap/closure], [label/logo placement by position and shape,
no invented text], [material + finish], [one distinctive detail], rendered with exact
real-world fidelity identical to the reference image.
```

**مثال:**
```
the NIMBUS cold brew can, a slim 330ml aluminum can in matte midnight blue with a single
thin cream band around the upper third, a silver pull-tab lid, a small circular cream
emblem centered on the band, soft-touch matte finish with faint condensation, rendered
with exact real-world fidelity identical to the reference image.
```

### 3. ولّد IMG-00 (3 min)
 six زوايا في شبكة: front · three-quarter left · side profile · back · top-down · macro.
خلفية محايدة · إضاءة استوديو متساوية · بلا بروبس · بلا نص زائد.
→ `schemas/product-sheet.md`

### 4. ثبّت الاستخدام (1 min)
- ارفع IMG-00 مع **كل** برومبت.
- ألصق الـ Anchor **حرفيًا** — لا تغيّر كلمة واحدة.
- أضف negative: `No changes to the product's shape, colors, proportions, cap, or label.`
- سجّل المنتج في Entity Ledger.

## قواعد الرفع حسب النموذج
| النموذج | النمط |
|---|---|
| Midjourney | `--oref [url]` |
| Nano Banana | حتى 3 صور في الرسالة |
| Kling | Elements + start/end frames |
| Runway Gen-4 | References بـ `@product` |
| Sora 2 | صورة أولى + Anchor نصي حرفي |

## Common Mistakes
- ❌ تغيير كلمة في الـ Anchor بين برومبت وآخر.
- ❌ ذكر نص الشعار الحرفي (النماذج تشوّهه).
- ❌ اختراع شكل عبوة لمنتج حقيقي.
- ❌ توليد المنتج بأسلوب الكولاج (المنتج يبقى فوتوغرافيًا واقعيًا).
- ❌ نسيان negative حماية المنتج.

## Next Step
- إعلان كامل → `workflows/engines/E2-commercial-engine.md`
- إعلان هجين → `workflows/engines/E3-hybrid-commercial.md`
- المرجع الكامل → `references/specs/product-truth.md`
