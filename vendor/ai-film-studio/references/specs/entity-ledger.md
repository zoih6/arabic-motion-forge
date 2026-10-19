---
name: entity-ledger
description: |
  سجل الكيانات: الوصف الحرفي المقفل لكل عنصر يتكرر عبر اللقطات أو الحلقات.
  الآلية التي تجعل 30 لقطة تبدو فيلمًا واحدًا بدل 30 صورة عشوائية.
  يشمل: بنية السجل، قواعد القفل، مستويات السجل (لقطة/مشروع/سلسلة)، وأخطاء شائعة.
tier: 3
when_to_load: "قبل كتابة أي برومبت يحتوي عنصرًا متكررًا (E1 حالة 7 · E2 مرحلة 2 · M4a)"
---

# Entity Ledger — سجل الكيانات

## 1. المشكلة التي يحلّها

> **الخطأ الأكثر شيوعًا في الإنتاج بالذكاء الاصطناعي:**
> وصف الشيء نفسه بكلمات مختلفة في لقطتين → النموذج يولّد شيئين مختلفين
> → الإعلان يبدو كـ 12 صورة عشوائية.

النماذج التوليدية **لا تملك ذاكرة**. كل برومبت يبدأ من الصفر.
الاستمرارية لا تأتي من "النموذج يتذكر" — بل من **نص متطابق حرفيًا** في كل مرة.

```
"a sunflower-yellow paper sun"     (اللقطة 3)
"a golden paper sun with rays"     (اللقطة 7)
        ↓
شيئان مختلفان تمامًا ❌
```

---

## 2. القاعدة الذهبية

> **أي عنصر يظهر أكثر من مرة عبر اللقطات يجب أن يُوصف بنفس الكلمات حرفيًا في كل ظهور.**

لا مرادفات، لا إعادة صياغة، لا تحسين أسلوبي، لا ترجمة between ظهورين.

---

## 3. بنية السجل

يُبنى **داخليًا** قبل كتابة أي برومبت. لا يُعرض للمستخدم.

```
ENTITY             LOCKED DESCRIPTION (English, verbatim)
─────────────────────────────────────────────────────────────────
PRODUCT            [Product Anchor من product-truth.md]
HERO-OBJECT        "a black fiberglass suitcase with a brass latch and a scuffed corner"
SURFACE            "a warm oak tabletop with fine grain"
PAPER-SUN          "a hand-cut sunflower-yellow cardstock sun with 12 blunt triangular rays"
PAPER-CLOUD        "a two-layer white cardstock cloud with a pale gray lower layer"
MAP-BASE           "a folded archival map base with visible crease lines and coffee staining"
CHARACTER-X        "a man in a dark 1970s suit seen from behind, halftone, no visible face"
SIGNATURE-RED      "one hot red marker circle drawn with a rough hand"
LABEL-SYSTEM       "condensed bold all-caps typewriter caption strips on cream paper"
```

### حقول اختيارية

| الحقل | متى |
|---|---|
| `FIRST_SEEN` | رقم أول لقطة ظهر فيها |
| `SEMANTIC_ROLE` | hero / supporting / background |
| `VARIATION_RULE` | ما يُسمح بتغييره (الإضاءة فقط، الزاوية فقط...) |

---

## 4. مستويات السجل الثلاثة

| المستوى | النطاق | يُبنى متى | يُخزَّن في |
|---|---|---|---|
| **Shot Ledger** | لقطة واحدة | عند كتابة برومبت اللقطة | داخل البرومبت نفسه |
| **Project Ledger** | مشروع كامل | بعد تثبيت العالم البصري | `schemas/state/continuity-bible.md` |
| **Series Ledger** | سلسلة/قناة | قبل أول حلقة | `schemas/series-bible.md` |

> **السلسلة = توقيع القناة.** الكيانات المقفولة هناك تظهر في **كل** الحلقات:
> نفس خامة الورق، نفس نظام التسميات، نفس التوقيع الأحمر، نفس الـ Voice ID.

---

## 5. قواعد القفل

| ✅ افعل | ❌ لا تفعل |
|---|---|
| انسخ الوصف المقفل كما هو | أعد صياغته "لتجنب التكرار" |
| استخدم نفس التهجئة ونفس المسافات | استبدل مرادفًا (`golden` مكان `sunflower-yellow`) |
| أضف تفاصيل جديدة **إلى جانب** الوصف المقفل | احذف كلمة من الوصف المقفل |
| ثبّت الصفات بالترتيب نفسه | غيّر ترتيب الصفات |
| حدّث السجل ثم طبّقه على **كل** الظهورات | حدّث لقطة واحدة فقط |

**مسموح بالتغيير:** الإضاءة، الزاوية، المسافة، الحالة (مغلق/مفتوح، فارغ/ممتلئ).
**ممنوع التغيير:** المادة، اللون، الشكل، العدد، النسب.

---

## 6. مثال تطبيقي كامل

```
PROJECT: إعلان قهوة مختصة — 15 ثانية — LOCK B

ENTITY          LOCKED DESCRIPTION
──────────────────────────────────────────────────────────
PRODUCT         the NIMBUS cold brew can, a slim 330ml aluminum can in matte midnight
                blue with a single thin cream band around the upper third, a silver
                pull-tab lid, a small circular cream emblem centered on the band,
                soft-touch matte finish with faint condensation, rendered with exact
                real-world fidelity identical to the reference image.

SURFACE         a warm oak tabletop with fine grain and a visible paper cutout edge

PAPER-HILL      a three-layer kraft paper hill with torn top edge and soft drop shadow

PAPER-SUN       a hand-cut sunflower-yellow cardstock sun with 12 blunt triangular rays

PAPER-CLOUD     a two-layer white cardstock cloud with a pale gray lower layer

STRING-RED      a single red cotton thread drawn taut from a brass pin to another

LIGHT-RULE      single warm key from upper left with soft fill and a thin rim light
```

**الاستخدام:** كل برومبت يذكر `PAPER-HILL` يستخدم العبارة المقفولة نفسها حرفيًا،
حتى لو تكررت 8 مرات في الحزمة.

---

## 7. التكامل مع باقي آليات الثبات

| الآلية | تحمي |
|---|---|
| **Product Anchor** | هوية المنتج |
| **Style Lock** | الأسلوب العام |
| **Entity Ledger** | الكيانات المتكررة |
| **Seed ثابت** | التشابه العشوائي |
| **Start/End Frames** | الاستمرارية الزمنية |
| **جملة ضوء واحدة** | وحدة المكان |

→ `references/specs/product-truth.md` § 7 (حزمة الثبات — 8 طبقات)

---

## 8. أخطاء شائعة

| الخطأ | النتيجة | الإصلاح |
|---|---|---|
| مرادف بين لقطتين | شيئان مختلفان | انسخ حرفيًا |
| ترتيب صفات مختلف | اختلاف دقيق لكن ملحوظ | ثبّت الترتيب |
| حذف صفة في بعض الظهورات | العنصر "يفقد" جزءًا من هويته | الوصف المقفل كاملًا دائمًا |
| ترجمة الوصف للعربية في برومبت | النموذج يفقد الدقة | البرومبتات بالإنجليزية دائمًا |
| تحديث السجل دون تطبيقه على الظهورات السابقة | عدم اتساق داخل الحزمة | حدّث الكل أو لا تُحدِّث |
| كيان متكرر بلا سجل | تخمين عشوائي | كل عنصر يتكرر ≥ 2 مرة → سجّله |

---

## Cross-Reference

- `references/specs/product-truth.md` — Anchor + IMG-00
- `references/protocols/style-lock-protocol.md` — الأقفال النصية
- `schemas/state/continuity-bible.md` — تخزين السجل على مستوى المشروع
- `schemas/series-bible.md` — توقيع القناة
