---
name: style-index
description: |
  فهرس العوالم البصرية العشرة وشجرة قرار الاختيار + اللوحات الجاهزة.
  اقرأه قبل اختيار العالم البصري لأي مشروع.
tier: 3
when_to_load: "بعد تثبيت الفكرة، قبل بناء العالم البصري (المرحلة 2 / M1a / M4b)"
---

# فهرس العوالم البصرية — Style Index

## القاعدة الذهبية

**عالم واحد لكل مشروع.** التطور المسموح الوحيد هو **تطور مقصود واحد** عبر العمل
(ظلام→نور، رمادي→لون، فوضى→هدوء). الأقفال تُنسخ حرفيًا من `locks/`.

---

## شجرة قرار الاختيار (بالترتيب)

```
1. هل يوجد منتج مادي يجب أن يبقى قابلاً للتعرّف؟
   ├─ لا  → اذهب إلى 2
   └─ نعم → اذهب إلى 4

2. هل المحتوى وثائقي / سردي تحقيقي / قصة حقيقية؟
   ├─ نعم → LOCK A (Documentary Archive Collage)
   └─ لا  → اذهب إلى 3

3. هل المحتوى شرح معلوماتي / بيانات / تعليمي؟
   ├─ نعم → LOCK I (Flat Vector Explainer)
   └─ لا  → اذهب إلى 5

4. ما طبيعة المنتج؟
   ├─ فخامة / عطر / ساعة / مجوهرات → LOCK C (Paper Noir Luxury)
   ├─ سناكس / مشروبات / شباب / مرح  → LOCK D (Pop Cutout) أو LOCK H (Clay)
   ├─ تقنية / أجهزة / سيارات        → LOCK E (Miniature Tabletop)
   ├─ مجلات / أزياء / ثقافة         → LOCK G (Mixed Media Editorial)
   ├─ العميل رفض الأسلوب الورقي      → LOCK F (Photoreal Studio)
   └─ غير ذلك / الافتراضي           → LOCK B (Commercial Craft Collage)

5. هل الهوية عربية / تراثية / خطية؟
   ├─ نعم → LOCK J (Arabic Calligraphic)
   └─ لا  → إذا كان المطلوب ملصقًا عموديًا جريئًا بشخصية واحدة وشيء ضخم يغيّر الـsilhouette → LOCK K
             وإلا → LOCK B كافتراضي آمن، أو LOCK F للواقعية
```

---

## جدول العوالم العشرة

| القفل | العالم | الأفضل لـ | المنتج | مستوى الابتكار | سهولة التوليد |
|---|---|---|---|---|---|
| **A** | Documentary Archive Collage | وثائقي، essay، قضايا، تاريخ | لا يوجد / سياقي | متوسط | ⭐⭐⭐⭐⭐ |
| **B** | Commercial Craft Collage | **الافتراضي للمنتجات** | واقعي فوتوغرافي | متوسط | ⭐⭐⭐⭐⭐ |
| **C** | Paper Noir Luxury | عطور، ساعات، فخامة | واقعي | عالٍ | ⭐⭐⭐⭐ |
| **D** | Pop Cutout Playground | سناكس، مشروبات، شباب | واقعي | متوسط | ⭐⭐⭐⭐⭐ |
| **E** | Miniature Tabletop Cinematic | تقنية، أجهزة، سيارات | واقعي بمقياس مصغّر | عالٍ | ⭐⭐⭐ |
| **F** | Photoreal Studio | أي فئة ترفض الأسlopب | واقعي كامل | منخفض | ⭐⭐⭐⭐ |
| **G** | Mixed Media Editorial | مجلات، أزياء، ثقافة | واقعي | عالٍ | ⭐⭐⭐ |
| **H** | Tactile Clay Diorama | سناكس، أطفال، حملات دافئة | واقعي | عالٍ | ⭐⭐⭐ |
| **I** | Flat Vector Explainer | شروح، بيانات، تعليم، B2B | أيقوني مبسّط | متوسط | ⭐⭐⭐⭐⭐ |
| **J** | Arabic Calligraphic | هوية عربية، تراث، مناسبات | واقعي | عالٍ جدًا | ⭐⭐⭐ |
| **K** | Oversized Ink Editorial | ملصقات، أغلفة سوشيال، شخصيات مبسطة | stylized | عالٍ | ⭐⭐⭐⭐ |

---

## اللوحات الجاهزة (اكتبها في `{PALETTE}`)

3–5 ألوان بالضبط: **قاعدة + ثانوي + محايد + لون المنتج + accent واحد يُحفظ للذروة**.

| النية | اللوحة |
|---|---|
| دفء / قهوة / خبز | `warm kraft brown, cream, burnt sienna, with the product's own colors` |
| انتعاش / ماء / نعناع | `ice white, pale aqua, deep teal, with a single citrus accent` |
| فخامة | `matte black, charcoal, antique gold, with the product's own colors` |
| مرح / سناكس | `sunflower yellow, coral, sky blue, white` |
| تقنية | `slate gray, off-white, graphite, with one electric accent` |
| طبيعي / عضوي | `sage green, oat, terracotta, linen white` |
| ليلي / طاقة | `midnight navy, deep violet-free black, neon lime accent, white` |
| تراث عربي | `deep ink, warm sand, aged brass, with one saturated royal accent` |
| بيانات / مؤسسي | `off-white, slate, deep navy, with one signal orange` |

> **قاعدة الـ accent:** لا يظهر إلا في **Trigger** و **Hero Shot**. ظهوره في كل لقطة يفقده قيمته.

---

## التطور المقصود الواحد (مسموح)

| الانتقال | كيف يُكتب في البرومبت |
|---|---|
| رمادي → لون | الأقفال نفسها؛ اللوحة تتوسع تدريجيًا عبر اللقطات |
| ظلام → نور | `the key light strengthens from near-darkness in S01 to full warm light by S06` |
| فوضى → هدوء | عدد العناصر المساندة يتناقص: 3 → 2 → 1 → 0 في الـ Hero |
| مسطح → ثلاثي الأبعاد | يُستخدم فقط مع LOCK I عند الانتقال لقفل آخر — **لا يُنصح به** |

---

## مصفوفة التوافق: القفل × نوع المحتوى

| | وثائقي | إعلان | essay/شرح | موشن جرافيك | سلسلة | سوشيال |
|---|---|---|---|---|---|---|
| **A** | ★★★★★ | ★★ | ★★★★★ | ★★ | ★★★★★ | ★★★ |
| **B** | ★★ | ★★★★★ | ★★ | ★★★ | ★★★★ | ★★★★★ |
| **C** | ★ | ★★★★★ | ★ | ★★ | ★★ | ★★★ |
| **D** | ★ | ★★★★★ | ★★ | ★★★★ | ★★★ | ★★★★★ |
| **E** | ★★ | ★★★★ | ★★★ | ★★ | ★★★ | ★★★ |
| **F** | ★★★ | ★★★★★ | ★★ | ★ | ★★★★ | ★★★★ |
| **G** | ★★★ | ★★★★ | ★★★★ | ★★★ | ★★★ | ★★★★ |
| **H** | ★ | ★★★★ | ★★ | ★★★ | ★★★ | ★★★★ |
| **I** | ★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ |
| **J** | ★★ | ★★★★ | ★★★ | ★★★★ | ★★★ | ★★★★ |
| **K** | ★★ | ★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★★★ |

---

## الأخطاء القاتلة في اختيار العالم

- ❌ اختيار LOCK A لإعلان منتج (المنتج سيضيع في الأرشيف).
- ❌ تغيير القفل في منتصف المشروع "للتنويع".
- ❌ استخدام accent في أكثر من لقطتين.
- ❌ خلط خامات قفلين (ورق + طين) في نفس اللقطة.
- ❌ ترك `{PALETTE}` بدون استبدال.
- ❌ استخدام LOCK J مع توليد نص عربي داخل الصورة (النماذج تشوّه العربية دائمًا).

---

## التالي

- القفل K ودليل استخدامه → `styles/locks/LOCK-K-oversized-ink-editorial.txt` + `styles/oversized-ink-editorial.md`
- الأقفال الحرفية → `styles/locks/`
- بروتوكول الأقفال → `references/protocols/style-lock-protocol.md`
- بناء عالم مخصص → `styles/style-pack-template.md`
