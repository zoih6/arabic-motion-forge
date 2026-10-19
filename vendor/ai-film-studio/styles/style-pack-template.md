---
name: style-pack-template
description: |
  قالب بناء عالم بصري مخصص (LOCK K+) عندما لا تكفي الأقفال العشرة.
  يحوّل أي أسلوب بصري إلى قفل نصي قابل للنسخ الحرفي.
tier: 3
when_to_load: "عند الحاجة لعالم بصري خارج الأقفال العشرة، أو عند بناء هوية قناة"
---

# قالب بناء عالم بصري مخصص (Style Pack)

استخدم هذا القالب عندما:
- العميل يطلب أسلوبًا خارج LOCK A–J.
- تبني هوية بصرية خاصة بقناة (Channel Signature).
- تستخرج أسلوبًا من مراجع بصرية (`workflows/M11a-reference-analyst.md`).

---

## 1. بطاقة العالم

```yaml
lock_id: LOCK-K-[slug]
name: "[اسم العالم بالإنجليزية]"
name_ar: "[الاسم بالعربية]"
category: [collage | photoreal | vector | clay | mixed | typographic]
product_treatment: [photoreal_real_object | stylized | absent]
best_for: "[الفئات]"
generative_difficulty: [1-5]
palette_slots: [PALETTE]        # أم حذوفة ومثبّتة داخل النص؟
ar_placeholder: true            # يستبدل 16:9 / 9:16
```

---

## 2. بنية القفل النصي (الترتيب الإلزامي داخل الجملة)

القفل الفعّال جملة نثرية واحدة متصلة (لا قائمة نقاط) بهذا الترتيب:

```
[1 MEDIUM]      المادة/الوسيط         "hand-cut layered paper" / "soft-sculpted polymer clay"
[2 SURFACE]     الأسطح والخلفيات      "on aged newsprint and archival map surfaces"
[3 TECHNIQUE]   التقنية والحواف       "with rough scissor-cut edges and offset accent strokes"
[4 ELEMENTS]    العناصر المميّزة      "torn edges, masking tape, typewriter strips, rubber stamps"
[5 PALETTE]     اللوحة (حرفية أو {PALETTE})
[6 ACCENT RULE] قاعدة لون الإشارة     "ONE hot red signal accent"
[7 TYPO RULE]   قاعدة الخط/التسمية    "condensed bold headline lettering only where a label is specified"
[8 TEXTURE]     الملمس                "visible print grain and paper fiber"
[9 LIGHT]       الضوء                 "flat even documentary lighting with soft cutout drop shadows"
[10 PRODUCT]    معاملة المنتج (إن وُجد) "THE PRODUCT ITSELF REMAINS A REAL PHOTOGRAPHIC OBJECT..."
```

**الطول المستهدف:** 60–110 كلمة. أقصر = يفقد التميّز. أطول = النموذج يتجاهل نهايته.

---

## 3. الخاتمة المخصصة

كل عالم يحتاج خاتمة تُختم بها البرومبتات:

```
CLOSER-[K]: Every element must appear physically [hand-made/hand-cut/hand-sculpted/drawn] and layered
from real [materials] with visible [edges] and soft real shadow separation. Clean, intentional, editorial
composition with generous negative space. NOT digital illustration, NOT cartoon, NOT 3D render, NOT glossy
CGI, no gradients, no clutter, no watermark, no text beyond the specified label. Premium [production]
quality, {AR}, ultra-detailed.
```

---

## 4. مفردات العالم (Vocabulary Bank)

املأ هذه البنوك — تُستخدم لتنويع وصف المشاهد **داخل** القفل الثابت:

| البنك | أمثلة |
|---|---|
| **الخامات** | `layered cardstock`, `torn kraft edge`, `vellum overlay`, `foil paper glint`, `corrugated card` |
| **الضوء** | `single warm key from upper left with soft fill`, `thin rim light tracing the silhouette`, `raking side light revealing texture` |
| **الكاميرا** | `locked-off static`, `slow push-in`, `slow pull-back reveal`, `gentle lateral slide`, `macro glide` |
| **الحركة** | `stop-motion cadence, stepped easing, 2-3 frame holds`, `slow fluid cinematic motion`, `quick decisive snaps between held poses` |
| **المزاج** | 3 كلمات بالضبط: `calm, tactile, premium` |

---

## 5. اختبار صلاحية القفل (5 أسئلة قبل الاعتماد)

| # | السؤال | الراسب |
|---|---|---|
| 1 | هل يمكن للنموذج تمييز هذا العالم عن LOCK A–J في 3 كلمات؟ | غامض — أعد الكتابة |
| 2 | هل كل حقل قابل للتحويل إلى قيمة بصرية (لا كلمات مجردة)؟ | مجرد — استبدل بصورة |
| 3 | هل القفل خالٍ من الكلمات الممنوعة (`beautiful`, `amazing`, `8K masterpiece` بلا سياق)؟ | حشو — احذف |
| 4 | هل معاملة المنتج محددة صراحة؟ | ناقص — أضف بند PRODUCT |
| 5 | هل اللوحة محددة (حرفية أو `{PALETTE}`)؟ | ناقص — ثبّتها |

---

## 6. اعتماد القفل

بعد اجتياز الاختبار:

1. احفظه في `styles/locks/LOCK-K-[slug].txt` — **ملف مستقل، لا تعدّل الموجود**.
2. سجّله في `styles/index.md` (الجدول + شجرة القرار).
3. أضف خاتمته في `styles/locks/README.md` (جدول تبديلات الخاتمة).
4. شغّل `python3 scripts/verify_styles.py` للتأكد من سلامة التسجيل.

---

## 7. مثال مصغر — LOCK K: Blueprint Technical

```yaml
lock_id: LOCK-K-blueprint
name: "Blueprint Technical"
category: vector
product_treatment: photoreal_real_object
best_for: "تقنية، هندسة، معماري، B2B"
```

القفل:
```
precision technical blueprint illustration on deep cyan-blue drafting paper, crisp white line work and
thin measured annotation strokes, faint grid ruling and dimension arrows, isometric exploded-view
components with callout leader lines, a disciplined palette of {PALETTE} with ONE amber signal accent
reserved for the key component, flat matte ink rendering with no gradients and no highlights, subtle
paper grain and drafting-table shadow, clean condensed technical lettering only where a label is
specified, even flat overhead light, THE PRODUCT REMAINS A REAL PHOTOGRAPHIC OBJECT rendered exactly,
never converted into line art.
```

الخاتمة:
```
Every element must appear precisely drafted and printed on real blueprint paper with crisp line weight
and measured spacing. Clean, technical, intentional composition with generous negative space. NOT 3D
render, NOT glossy, no gradients, no clutter, no watermark, no text beyond the specified label. Premium
technical production quality, {AR}, ultra-detailed.
```
