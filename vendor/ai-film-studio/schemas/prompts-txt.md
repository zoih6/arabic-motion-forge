---
name: schema-prompts-txt
description: "مواصفة ملف prompts.txt: بنية الكتلة، فواصل، ترتيب، التسمية، وإرشاد التنفيذ بالجملة."
tier: 3
when_to_load: "E1 الحالة 7 · E5 · M7b"
---

# Prompts TXT — مواصفة ملف البرومبتات

## 1. الغرض

ملف نصي واحد يحتوي برومبتًا لكل Beat، جاهز للرفع في أداة توليد بالجملة.

**الاسم:** `[topic-slug]-prompts.txt`

---

## 2. بنية الكتلة الواحدة

```
SCENE: [وصف البطل الدقيق] [التسمية إن وُجدت] [2-3 عناصر مساندة] [الخلفية والهوامش].

[LOCK حرفيًا]

[CLOSER حرفيًا]
```

### مثال

```
SCENE: A single black fiberglass suitcase with a brass latch and a scuffed corner stands
open on a warm oak tabletop with fine grain, revealing stacks of aged banknotes bound in
paper bands. Behind it, a folded archival map base with visible crease lines and coffee
staining, and a single short label reading "NOV 24 1971" on a paper strip. Two supporting
elements: a typewriter caption strip and one brass pin. Generous negative space above.

hand-cut documentary paper collage on aged newsprint and archival map surfaces, black and
white halftone photograph cutouts with rough scissor-cut edges and offset accent strokes,
torn paper edges, masking tape fragments, typewriter caption strips, rubber stamp marks,
red string and brass pins where the story calls for connections, desaturated archival
palette of tan, ink black, and halftone gray with ONE hot red signal accent and a
restrained mustard yellow secondary, condensed bold headline lettering only where a label
is specified, visible print grain and paper fiber, matte, flat even documentary lighting
with soft cutout drop shadows.

Every element must appear physically hand-cut and layered from real paper, with visible
cutout edges, halftone print texture, and soft shadow separation between layers. The
composition stays clean, minimal, and editorial with generous negative space. NOT digital
illustration, NOT cartoon, NOT 3D render, NOT glossy, no gradients, no clutter, no
watermark, no logos, no text beyond the specified label. Premium documentary collage
aesthetic, 16:9, ultra-detailed, 8K.
```

---

## 3. قواعد الملف

| القاعدة | التطبيق |
|---|---|
| **الفاصل** | **سطر فارغ واحد** بين الكتل |
| **الترقيم** | ❌ بلا ترقيم |
| **التعليقات** | ❌ بلا تعليقات ولا عناوين |
| **الترتيب** | = ترتيب جدول الـ Beats = ترتيب التجميع (ثلاثتها واحدة) |
| **الاستقلال** | كل كتلة **مستقلة ذاتيًا** — لا تعتمد على السابقة |
| **الطول** | 60–120 كلمة للقسم المشهدي قبل القفل |
| **اللغة** | إنجليزية دائمًا |
| **الأقفال** | حرفية — نفس النص في كل كتلة |

---

## 4. قواعد المحتوى داخل الكتلة

### قانون التركيب
| العنصر | الوزن |
|---|---|
| البطل (Hero) | ~70% من الثقل البصري |
| عناصر مساندة | **2–3 كحد أقصى** |
| اهتمام خلفية | ~10% |
| مساحة سلبية | سخية |

### ترتيب أولوية البطل
1. **شيء مادي** يحمل القصة (تذكرة، مظلة، حقيبة، مفتاح)
2. **وثيقة** (مغلق، خريطة، صورة مقصوصة، شيك، تقرير)
3. **خريطة أو مخطط زمني** (للانتقالات والمسافات)
4. **شخصية هالفتون** — من الخلف أو مع شريط رقابة، ❌ لا وجوه واضحة
5. **مكان** (صورة جوية، واجهة، غرفة)

### قانون النص داخل الصورة
- الافتراضي: **لا نص إطلاقًا**.
- الاستثناء: **تسمية واحدة 1–4 كلمات** إذا حمل الـ Beat تاريخًا أو اسمًا أو رقمًا مهمًا.
- الصيغة: `a single short label reading "..." on a paper strip` (ALL CAPS).
- ❌ فوق 4 كلمات ممنوع منعًا باتًا.

### سجل الكيانات
أي عنصر يتكرر عبر الـ Beats **يُوصف بنفس الكلمات حرفيًا** في كل مرة.
→ `references/specs/entity-ledger.md`

---

## 5. إرشاد التنفيذ (يُلحق بالرد)

```
طريقة التنفيذ:
1. افتح أداة التوليد بالجملة (Textify أو أي أداة تقبل ملف txt فيه برومبتات مفصولة بسطر فارغ).
2. ارفع الملف وولّد كل الصور دفعة واحدة، بنفس الأبعاد 16:9.
3. افحص سريعًا: أي صورة خرجت "ديجيتال" أو ملونة أو فيها نص زيادة = أعد توليدها وحدها.
4. رتب الصور بنفس ترتيب جدول الـ Beats.
```

---

## 6. قائمة الإصلاح السريع

| العرض | الإصلاح |
|---|---|
| الصور "ديجيتال" لا كولاج | القفل مفقود أو مبتور — أعد التوليد بالبرومبت كاملًا |
| ملونة زاهية | قفل خاطئ — راجع `styles/index.md` |
| نص زائد | تسمية غير معلنة — أعد التوليد |
| وجوه مشوّهة | استبدل بهالفتون أو ظل من الخلف |
| تكررت المشكلة | `redo 7` بجمل حادة في وصف المشهد |

---

## 7. قائمة فحص الملف

- [ ] الاسم `[slug]-prompts.txt`؟
- [ ] كتلة لكل Beat؟
- [ ] سطر فارغ واحد بين الكتل؟
- [ ] بلا ترقيم ولا تعليقات؟
- [ ] الترتيب = ترتيب الـ Beats؟
- [ ] كل كتلة مستقلة ذاتيًا؟
- [ ] القفل والخاتمة حرفيان في كل كتلة؟
- [ ] `{AR}` مستبدل؟
- [ ] بطل واحد + ≤ 3 مساند؟
- [ ] الكيانات المتكررة بوصف مقفل؟

---

## Cross-Reference

- `workflows/engines/E1-documentary-engine.md` — الحالة 7
- `workflows/engines/E5-bulk-production-pipeline.md` — التنفيذ
- `references/protocols/style-lock-protocol.md` — الأقفال
