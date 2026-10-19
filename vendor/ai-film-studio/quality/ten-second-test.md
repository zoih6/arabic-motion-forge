---
name: ten-second-test
description: |
  اختبار العشر ثوانٍ: خمسة أسئلة تُقرأ على كل برومبت بعين النموذج قبل اعتماده.
  يلتقط الغموض والازدواجية والمستحيل قبل أن يضيع وقت التوليد.
tier: 3
when_to_load: "قبل اعتماد أي برومبت (E2 المرحلة 6 · E1 الحالة 7 · M7b · M8a)"
---

# Ten-Second Test — اختبار العشر ثوانٍ

## الطريقة

> **اقرأ البرومبت كأنك النموذج، في عشر ثوانٍ، وأجب عن خمسة أسئلة.**

الهدف: التقاط ما سيفشل في التوليد **قبل** إضاعة الوقت والحوسبة.

---

## الأسئلة الخمسة

### 1. هل أعرف بالضبط ماذا يوجد في كل ربع من الإطار؟

قسّم الإطار ذهنيًا إلى أربعة أرباع:

```
┌─────────┬─────────┐
│  أعلى   │  أعلى   │
│  يسار   │  يمين   │
├─────────┼─────────┤
│  أسفل   │  أسفل   │
│  يسار   │  يمين   │
└─────────┴─────────┘
```

| ❌ راسب | ✅ ناجح |
|---|---|
| "جميلة، فنية، احترافية" | "المنتج يمين الثلث بارتفاع 40%، خلفية كريمية، مساحة فارغة يسار" |

**القاعدة:** كل ربع يجب أن يكون له وصف — حتى لو كان "فارغ".

---

### 2. هل توجد جملة يمكن تفسيرها بطريقتين؟

| ❌ ملتبس | ✅ واضح |
|---|---|
| "بعض الورق الملون في الخلفية" | "cutouts in three flat colors: sunflower yellow, coral, sky blue" |
| "إضاءة جميلة" | "single warm key from upper left with soft fill" |
| "حركة سلسة" | "stop-motion cadence, stepped easing, 2-3 frame holds" |
| "منتج أنيق" | Product Anchor الحرفي |

**القاعدة:** كل صفة يجب أن تُترجم إلى **قيمة** (لون، زاوية، نسبة، مادة، زمن).

---

### 3. هل يُطلب مني شيء لا أستطيعه؟

| المستحيل/الخطير | البديل |
|---|---|
| نص عربي داخل الصورة | طبقة نص حقيقية في المونتاج |
| وجه إنسان واقعي معبّر | هالفتون / ظل من الخلف / شريط رقابة |
| يد في لقطة قريبة | قصاصة / أزل الفعل اليدوي |
| نص طويل (> 4 كلمات) | ≤ 4 كلمات أو احذف |
| فيزياء مستحيلة معقدة | بديل بصري بسيط |
| شعار علامة حقيقية دقيق | من الملف الأصلي في المونتاج |
| تحول ورقي معقد في End Frame | صف الحالة النهائية بالنص |

---

### 4. هل المنتج محمي بـ Anchor + negative صريح؟

| الفحص | مثال |
|---|---|
| Anchor حرفي موجود؟ | ✓ نفس 45 كلمة في كل برومبت |
| negative يحميه؟ | `No changes to the product's shape, colors, proportions, cap, or label.` |
| ذُكر أنه فوتوغرافي واقعي؟ | `THE PRODUCT ITSELF REMAINS A REAL PHOTOGRAPHIC OBJECT` |
| تغطيته محددة؟ | "40% من الإطار، غير مغطى" |

---

### 5. (فيديو) هل أعرف ما يتحرك وما يثبت والحالة النهائية؟

| الفحص | الصيغة |
|---|---|
| **ما يتحرك** | "At 0–1s the cap begins to lift... by 3s it floats 5cm above" |
| **ما يثبت** | "The can, the paper hill, and the clouds stay perfectly still." |
| **الكاميرا** | "The camera stays completely locked" — حركة واحدة فقط |
| **الحالة النهائية** | "End with the cap resting..., matching the provided end frame" |
| **المدة** | "A 5-second commercial clip, 9:16." |

> **القاعدة الذهبية:** ما لا تذكره سيتحرك.
> اذكر صراحة **كل** ما يجب أن يبقى ثابتًا.

---

## الحكم

| النتيجة | الإجراء |
|---|---|
| **5/5 نعم** | ✅ اعتمد البرومبت |
| **أي "لا" أو "ربما"** | ❌ أعد الصياغة قبل التسليم |

---

## أمثلة محلولة

### ❌ راسب

```
A beautiful paper collage with the product looking amazing in warm light,
professional commercial style, high quality, 8K.
```

**التشخيص:**
1. ❌ لا توجد أرباع محددة
2. ❌ "beautiful/amazing/professional" — كلمات فارغة
3. ❌ "the product" بلا Anchor
4. ❌ لا negative
5. ❌ (ليس فيديو)

---

### ✅ ناجح

```
A commercial product still, medium shot, 9:16 vertical. the NIMBUS cold brew can, a slim
330ml aluminum can in matte midnight blue with a single thin cream band around the upper
third, a silver pull-tab lid, a small circular cream emblem centered on the band,
soft-touch matte finish with faint condensation, rendered with exact real-world fidelity
identical to the reference image. It stands upright on a three-layer kraft paper hill with
torn top edge and soft drop shadow, centered in the middle 70% of the vertical frame.
Behind it, a hand-cut sunflower-yellow cardstock sun with 12 blunt triangular rays occupies
the upper right quadrant; a two-layer white cardstock cloud with a pale gray lower layer
sits upper left. The lower left quadrant stays empty cream paper. 100mm macro lens, eye
level, shallow depth of field. Single warm key from upper left, thin rim light tracing the
can. Calm, tactile, premium. [LOCK-B حرفيًا] [CLOSER حرفيًا] No hands, no people, no faces.
No text, no letters, no watermark. No changes to the product's shape, colors, proportions,
cap, or label. No other products or brands.
```

**التشخيص:**
1. ✅ الأرباع الأربعة موصوفة
2. ✅ كل صفة قيمة
3. ✅ لا وجوه/أيدٍ/نص
4. ✅ Anchor حرفي + negative صريح
5. ✅ (صورة — غير مطبق)

---

## Cross-Reference

- `references/specs/model-dialects.md` — تشريح البرومبت
- `references/specs/prompt-architecture.md` — 10 طبقات A–J
- `quality/gates-extended.md` § G4
- `scripts/prompt_lint.py` — الفحص الآلي
