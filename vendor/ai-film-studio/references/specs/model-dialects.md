---
name: model-dialects
description: |
  لهجات النماذج: كيف تُكتب نفس الفكرة بصيغة تناسب كل نموذج توليد (صور وفيديو).
  يشمل 6 عائلات صور + 6 عائلات فيديو، قواعد اختيار النموذج حسب المهمة،
  استهلاك المراجع، والقاعدة الذهبية: MASTER محايد + تنويعتا لهجة.
tier: 3
when_to_load: "قبل كتابة البرومبتات النهائية (E2 مرحلة 6 · E1 حالة 7 · M7b · M8a)"
---

# Model Dialects — لهجات النماذج

## 1. المبدأ

النماذج الحديثة تحتضن نماذج لغوية:

> **النثر البشري الواضح يتفوق على قوائم الكلمات المفتاحية.**

اكتب كما تشرح لمصوّر محترف ماذا تريد أن يرى، **بترتيب ثابت**.
لا `8K masterpiece trending` بلا سياق.

**البرومبت الواحد يصف حالته كاملة** — لا يعتمد على ذاكرة برومبت سابق.
الاستمرارية تأتي من: Anchor حرفي + Style Lock حرفي + Entity Ledger + Start Frame.

---

## 2. القاعدة الذهبية للتسليم

سلّم دائمًا:

```
MASTER   — نثر محايد يعمل في كل مكان
+ DIALECT-1 — تنويعة للنموذج الأنسب للمهمة
+ DIALECT-2 — تنويعة لثاني أنسب نموذج
```

❌ **لا تسمِّ نموذجًا بصيغة "استخدم X فقط"** — النماذج تتغير كل أشهر.

---

## 3. نماذج الصور

| النموذج | نقاط القوة | اللهجة |
|---|---|---|
| **Midjourney (v7+)** | جمالية، أسلوب، ملمس | نثر **أقصر** (60–100 كلمة) + بارامترات:<br>`--ar 9:16 --oref [product] --ow 300 --sref [style img] --stylize 150 --chaos 0`<br>❌ لا negative نثري — استخدم `--no hands, text` |
| **Flux (2 / Kontext)** | التزام حرفي بالنثر، تحرير بالمرجع | النثر الكامل كما هو.<br>Kontext: `Keep the product exactly as in the reference; place it on...`<br>❌ لا بارامترات |
| **Nano Banana / Gemini Image** | ثبات الكيان عبر لقطات متعددة، مراجع متعددة | محادثة: ارفع IMG-00 + اللقطة السابقة، ثم:<br>`Using the exact same product from image 1 and the same paper world from image 2, now show...`<br>⭐ **ممتاز للسلاسل** |
| **GPT Image** | فهم التعليمات المركبة، التركيب | النثر الكامل + `Match the attached product precisely`<br>جيد لتعليمات "لا تغيّر X" |
| **Ideogram 3** | **النص داخل الصورة** | استخدمه فقط عند طلب label/نص.<br>النص بين علامتَي تنصيص مزدوجة |
| **Imagen 4** | فوتوريالية، ضوء | النثر الكامل؛ يستفيد من مصطلحات التصوير (`100mm macro, f/2.8`) |
| **Seedream / Seedance (ByteDance)** | تنوع أسلوبي، سرعة | نثر متوسط؛ ممتاز للأساليب المسطحة والـ LOCK I |

---

## 4. نماذج الفيديو

| النموذج | نقاط القوة | اللهجة |
|---|---|---|
| **Veo 3.x** | **صوت أصلي مُولَّد**، فهم سينمائي، first/last frame، مراجع | النثر الكامل + قسم `Audio:` صريح.<br>الحوار بين تنصيص إن وُجد. أضف `(no subtitles)`.<br>8 ث افتراضي |
| **Kling 2.x** | Elements للثبات، start+end frame، حركة فيزيائية | نثر **أقصر** متمركز على الفعل والكاميرا.<br>حدّد `motion intensity: low/medium`.<br>Negative prompt منفصل. 5 أو 10 ث |
| **Runway Gen-4 / 4.5** | References متعددة بـ `@tags`، تحكم كاميرا | `@product` للمنتج، `@world` للأسلوب.<br>جمل قصيرة، فعل واحد، حركة كاميرا صريحة. 5 أو 10 ث |
| **Sora 2** | تسلسلات فيزيائية معقدة، صوت | النثر الكامل؛ صف الفيزياء بدقة.<br>الثبات عبر اللقطات **أضعف** → Anchor حرفي إجباري |
| **Hailuo / MiniMax** | حركة كاميرا ديناميكية | أوامر كاميرا بين أقواس مربعة: `[Push in]`، `[Static shot]` |
| **Luma Ray / Wan / Seedance** | سريع، keyframes | نثر متوسط + start/end frames.<br>❌ تجنّب التحولات الورقية المعقدة |

---

## 5. قاعدة اختيار النموذج حسب المهمة

| المهمة | الخيار الأول | البديل |
|---|---|---|
| **كولاج stop-motion** | Veo أو Kling (يفهمان `stepped easing`) | Runway |
| **صوت أصلي مُولَّد** | **Veo 3.x** | Sora 2 |
| **ثبات عبر 8+ لقطات** | Kling Elements أو Runway References | Nano Banana (صور) |
| **فوتوريال سينمائي** | Veo / Sora | Imagen (صور) |
| **نص داخل الصورة** | Ideogram 3 | GPT Image / Nano Banana |
| **سلسلة طويلة متسقة** | Nano Banana (صور) + Kling (فيديو) | Flux Kontext |
| **أسلوب مسطح / infographic** | Seedream / GPT Image | Midjourney |
| **تحرير صورة موجودة** | Flux Kontext | Nano Banana |

---

## 6. استهلاك المراجع (Reference Handling)

| النموذج | عدد المراجع | النمط |
|---|---|---|
| Nano Banana / Gemini | حتى 3 | صور في نفس الرسالة + وصف |
| Runway Gen-4 | حتى 3 | `@tag` لكل مرجع |
| Veo 3.x | حتى 3 | Ingredients |
| Kling 2.x | Elements + start/end | مرجع كيان منفصل |
| Midjourney | `--oref` + `--sref` | URL |
| Sora 2 | صورة أولى فقط | ضعيف في الثبات |
| Flux Kontext | صورة واحدة | تعليمات تعديل |

> **عند غياب دعم المراجع:** الـ Anchor النصي الحرفي هو خط الدفاع الوحيد — لا تختصره.

---

## 7. قواعد عابرة للنماذج

### النص داخل الصورة

- **الافتراضي: صفر نص.**
- عند الضرورة: label واحد، 1–4 كلمات، ALL CAPS إنجليزي، بين تنصيص مزدوجة:
  `a single paper strip with the label "COLD BREW"`
- **العربية ممنوعة تمامًا داخل الصورة** — تُضاف كطبقة نص حقيقية في المونتاج.
- **في الفيديو: لا تولّد نصًا أبدًا.**

### القيود السلبية (≤ 6 لكل برومبت)

```
No hands, no people, no faces.
No text, no letters, no watermark.
No changes to the product's shape, colors, proportions, cap, or label.
No other products or brands.
No elements not described here.
No morphing, no object replacement, no camera shake, no cuts, no transitions.
No gradients, no glossy CGI look, no 3D-render feel.
No lens flares, no bokeh balls.
```

❌ لا تناقض بين السلبي والإيجابي (مثال: تطلب ظلًا ناعمًا ثم تكتب `no shadows`).

### الطول

| النوع | الطول قبل القفل |
|---|---|
| برومبت صورة | **120–220 كلمة** |
| Midjourney | 60–100 كلمة (استثناء) |
| برومبت فيديو | 80–180 كلمة |
| وثائقي (Beat) | 60–120 كلمة للقسم المشهدي |

> أقل = غموض. أكثر = النموذج يتجاهل النصف الثاني.

---

## 8. Motion DNA (واحد للمشروع كله)

| DNA | الكتابة الحرفية | العالم |
|---|---|---|
| **Stop-motion craft** | `stop-motion cadence, stepped easing, 2-3 frame holds, the hand-made "on twos" feel, never smooth CGI motion` | Locks A, B, D, H |
| **Slow cinematic** | `slow, weighted, continuous cinematic motion, as if time itself slowed, no sudden movements` | Locks C, E, F |
| **Snap editorial** | `quick decisive snaps between held poses, energetic but controlled, each movement lands with a settle` | Lock D, G |
| **Living still** | `almost imperceptible life: light breathes, particles drift, edges lift a millimeter, nothing relocates` | Hero, Hooks |
| **Flat modular** | `crisp modular layer motion, each element moves on its own plane with clean stepped timing, no perspective drift` | Lock I, J |

---

## 9. توقيع الاستوديو — Build-On Assembly

أقوى مشهد كولاج: الإطار يبدأ فارغًا ويجمّع نفسه حتى يطابق الصورة النهائية.
القالب الكامل في `styles/locks/UNIVERSAL-VIDEO-PROMPT.txt`.

نسخة مختصرة قابلة للتضمين:

```
Transform the provided image into a {N}-second premium paper-collage animation. The provided
image is the FINISHED frame the animation builds toward; preserve its final composition
exactly. The camera stays completely locked. 0 to {N-3}s, build-on assembly: open on the
empty background surface only, then elements enter one by one back to front in narrative
order, each sliding or dropping in as a rigid paper piece with a tiny handcrafted bounce,
a 2-frame settle, and a real layered shadow. [PRODUCT ANCHOR] is placed LAST, lowered in
as a real photographic object, and nothing moves after it lands. {N-3} to {N}s, living
poster: everything holds; only paper corners lift a millimeter, shadows breathe.
Stop-motion cadence, stepped easing, never smooth CGI. Audio: close-up paper slides,
cardstock taps, one soft thud for the product, faint room tone; no music, no voice.
No morphing, no camera movement, no cuts.
```

---

## 10. اختبار العشر ثوانٍ

→ `quality/ten-second-test.md` — يُطبَّق على **كل** برومبت قبل التسليم.

---

## Cross-Reference

- `references/specs/prompt-architecture.md` — 10 طبقات A–J
- `references/specs/model-matrix.md` — المصفوفة الكاملة للنماذج
- `references/specs/prompt-compiler.md` — المصنّف
- `styles/locks/README.md` — الأقفال الحرفية
