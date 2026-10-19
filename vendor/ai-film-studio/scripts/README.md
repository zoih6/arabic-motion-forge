# Scripts — أدوات فحص قابلة للتنفيذ

> **فاحصات آلية** تتأكد من سلامة المهارة. شغّلها قبل أي commit.

## المتاح

| السكربت | الوظيفة | المدة |
|---|---|---|
| `verify_structure.py` | يفحص البنية (151 ملفًا) + الروابط + YAML | ~5s |
| `verify_functional.py` | يفحص المسار الوظيفي (95 حالة · 4 fixtures) | ~10s |
| `verify_motion.py` | يفحص مسار الموشن جرافيك (46 حالة) | ~5s |
| `verify_example.py` | يفحص الأمثلة الحية (29 حالة) | ~5s |
| `verify_styles.py` | **v3** — الأقفال العشرة + الخواتيم + UVP | ~1s |
| `verify_vox.py` | **v3** — المحركات الخمسة + مراجع v3 | ~1s |
| `verify_links.py` | **v3** — سلامة الروابط الداخلية | ~1s |
| `prompt_lint.py` | **v3** — فاحص البرومبتات (اختبار العشر ثوانٍ) | ~1s |
| `prompt_compiler.py` | يحول Canonical Shot Spec إلى Prompts جاهزة حسب النموذج مع `@ImageN` تلقائيًا | <1s |
| `test_prompt_compiler.py` | اختبارات المحولات والمرجعيات وتعارضات الإطارات | <1s |
| `verify_all.sh` | يشغّل الكل (8 فحوص) | ~30s |

## الاستخدام

```bash
# فحص بنية فقط
python3 scripts/verify_structure.py

# فحص شامل (8 فحوص)
bash scripts/verify_all.sh

# فحص مسار محدد
python3 scripts/verify_motion.py

# ── v3.0.0 ──
python3 scripts/verify_styles.py              # الأقفال النصية
python3 scripts/verify_vox.py                 # المحركات والتكامل
python3 scripts/verify_links.py               # الروابط الداخلية
python3 scripts/prompt_lint.py prompt.txt     # فحص برومبت واحد
python3 scripts/prompt_lint.py --selftest     # اختبار ذاتي
python3 scripts/prompt_compiler.py examples/compiler-fixture.json --markdown /tmp/compiled.md
python3 scripts/test_prompt_compiler.py
```

## فاحص البرومبتات (v3.0.0)

يطبّق «اختبار العشر ثوانٍ» و«قواعد الأقفال» آليًا:

| # | الفحص |
|---|---|
| 1 | طول الجسم قبل الأقفال (60–240 كلمة) |
| 2 | الكلمات الفارغة المحرّمة |
| 3/4 | وجود القفل ومطابقته الحرفية لملفات `styles/locks/` |
| 5 | Negative موجود و ≤ 6 بنود |
| 6 | المحظورات: وجوه · أيدٍ · نص طويل · fade to black · عربي داخل الصورة |
| 7 | (فيديو) ما يثبت · حركة كاميرا واحدة · الحالة النهائية |
| 8 | الرموز غير المستبدلة `{AR}` · `{PALETTE}` · `{DURATION}` |
| 9 | الحقول الإلزامية (FRAME · CAMERA · LIGHT · MOOD · NEGATIVE) |
| 10 | شرطة طويلة (em dash) في المخرجات الإنجليزية |

> **ملاحظة:** الجُمَل التي تُطابق الأقفال والخواتيم تُستثنى تلقائيًا من قياس الطول
> ومن عدّ بنود الـ Negative — لأنها أصول ثابتة لا جزء من صياغة البرومبت.


## Prompt Compiler التنفيذي

يقرأ `reference_manifest` و`shots`، يختار المراجع المقفلة تلقائيًا، يوزع `@ImageN`، ويحوّل قاموس الكاميرا إلى صيغة Seedance أو Omni أو Veo. مدخلاته موثقة في `schemas/prompt-compiler-input.schema.json`.

```bash
python3 scripts/prompt_compiler.py examples/compiler-fixture.json \
  --output /tmp/compiled.json --markdown /tmp/compiled-prompts.md
python3 scripts/test_prompt_compiler.py
```

## آخر نتيجة (v3.2.0)

```
1/8  الفحص البنيوي (structure + YAML)          ✅ 151 ملفًا مطلوبًا
2/8  الفحص الوظيفي (المسار السردي)             ✅ 95/95 · 4 fixtures
3/8  فحص المثال الحي                           ✅ 29/29
4/8  الفحص الوظيفي (مسار الموشن جرافيك)        ✅ 46/46
5/8  مكتبة الأنماط (LOCK A–J + Closers)        ✅ 71/71
6/8  المحركات والتكامل (E1–E5)                 ✅ 84/84
7/8  سلامة الروابط الداخلية                    ✅ 162 ملفًا · 156 رابطًا · 0 مكسور
8/8  فاحص البرومبتات (اختبار ذاتي)             ✅ 8/8 · 0 تحذير

✅ كل الاختبارات نجحت (8/8)
```
