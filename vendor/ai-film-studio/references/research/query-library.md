---
name: query-library
description: |
  مكتبة استعلامات بحث جاهزة للنسخ والتعديل: منتجات، أساليب بصرية، مراجع،
  ترند، منصات، نماذج توليد، حقائق تاريخية، وسوق عربي.
  كل استعلام بصيغة قابلة للتخصيص مع المتغيرات بين أقواس.
tier: 3
when_to_load: "عند الحاجة لاستعلام بحث سريع (أي مرحلة بحث)"
---

# Query Library — مكتبة الاستعلامات

## كيف تستخدم

انسخ الاستعلام، استبدل المتغيرات بين `{ }`، نفّذ.

```
[الكيان الدقيق] + [الصفة المطلوبة] + [السياق/القيد]
```

---

## 1. المنتجات (T2 — شكل العبوة)

```
{BRAND} {PRODUCT} official packaging
{BRAND} {PRODUCT} {SIZE}ml dimensions color cap
{BRAND} {PRODUCT} product photography official
site:{brand}.com {PRODUCT}
{BRAND} {PRODUCT} label placement ingredients side
{BRAND} brand guidelines color palette official
```

**الهدف:** وصف دقيق للشكل، اللون، الغطاء، موضع الشعار، المادة.

---

## 2. الأساليب البصرية

```
{STYLE} editorial collage behance
{STYLE} {COLOR} palette hex codes
{STYLE} typography hierarchy condensed bold
{STYLE} lighting setup {raking/soft/high-key} photography
{MATERIAL} texture macro photography paper fiber
{STYLE} motion reel stop motion {YEAR}
{STYLE} composition negative space layout
```

**أمثلة مخصصة:**

```
paper collage documentary editorial behance
hand-cut cardstock texture macro photography
stop motion craft animation reel 2026
flat vector explainer infographic behance
arabic calligraphy geometric kufi modern design
claymation diorama miniature set photography
```

---

## 3. المراجع البصرية

```
{STYLE} reference {CATEGORY} advertising campaign
{STYLE} {MEDIUM} award winning {YEAR}
{STYLE} archive poster museum public domain
{STYLE} {CATEGORY} art direction breakdown
```

---

## 4. الترند والمنافسون

```
{CATEGORY} advertising trends {YEAR}
{CATEGORY} tiktok ads top performing {YEAR}
{BRAND} competitor advertising campaign {YEAR}
{CATEGORY} {PLATFORM} best performing ads {YEAR}
google trends {KEYWORD} {REGION} {YEAR}
```

---

## 5. المنصات والمواصفات

```
{PLATFORM} video specs {YEAR} official
{PLATFORM} safe zones aspect ratio ads {YEAR}
{PLATFORM} ad duration limits {YEAR}
{PLATFORM} thumbnail size dimensions {YEAR}
```

---

## 6. نماذج التوليد

```
{MODEL} {VERSION} reference image limit duration {YEAR}
{MODEL} official docs first frame last frame
{MODEL} vs {MODEL} consistency multi-shot comparison
{MODEL} prompt guide best practices {YEAR}
```

---

## 7. الحقائق التاريخية (للوثائقي)

```
{EVENT} {DATE} primary source archive
{EVENT} court records official report
{PERSON} {EVENT} official biography
{PLACE} {EVENT} historical archives
"{EVENT}" -conspiracy -theory
```

---

## 8. السوق العربي

```
{المنتج} {السوق} حملة إعلانية {السنة}
{المجال} ترندات التسويق {السنة} السعودية / مصر / الإمارات / اليمن
خطوط عربية مجانية مرخصة {Cairo/Tajawal/IBM Plex Sans Arabic}
تصميم هوية عربية معاصرة {المجال}
{المناسبة} حملات إعلانية عربية ملهمة
```

---

## 9. استعلامات الاستبعاد المفيدة

```
{QUERY} -pinterest          # لتجنب لوحات المزاج المتكررة
{QUERY} -ai -generated      # لتجنب المحتوى التوليدي
{QUERY} -template -freebie  # لتجنب القوالب الجاهزة
{EVENT} -conspiracy -hoax   # لتجنب نظريات المؤامرة
```

---

## 10. قوالب متقدمة

### بحث عن «القاعدة» لا «العنصر»

```
{STYLE} design principles rules
{STYLE} color theory palette
{STYLE} grid system composition rules
{STYLE} typography scale hierarchy rules
```

### بحث عن معيار الجودة المهني

```
D&AD {CATEGORY} {YEAR} winners
Cannes Lions {CATEGORY} {YEAR} shortlist
Effie {CATEGORY} effective campaigns {YEAR}
```

### بحث عن أخطاء شائعة (لتجنبها)

```
{MODEL} common failure modes prompt
{STYLE} mistakes to avoid design
{CATEGORY} advertising clichés overused
```

---

## Cross-Reference

- `references/research/search-playbook.md` — منهجية البحث
- `references/research/reference-mining.md` — تعدين المراجع
- `references/research/trend-research.md` — بحث الترند
- `references/research/fact-verification.md` — التحقق
