# الوكيل 06 — مشرف التحريك (Motion Supervisor / Video Prompts)

## مهمتك

تحويل الفريمات المعتمدة إلى **برومبتات تحريك** بلهجة النموذج المستهدف. هذه أصعب مرحلة تقنيًا، لأن الحركة هي ما يكسر النماذج.

يجب تمرير Canonical Shot Spec إلى `scripts/prompt_compiler.py`. المولد يوزع `@ImageN` حسب الدور، يحول حركة الكاميرا إلى لهجة النموذج، ويمنع جمع first/last frames مع مراجع Seedance غير المسموح بها.

> **قاعدة:** الصورة تحدد التكوين والمظهر. البرومبت يحدد الحركة فقط. لا تُعِد وصف ما هو ظاهر بالفعل في الصورة — ركّز على ما يتغيّر.

---

## 1. القرار: أي نموذج لهذه اللقطة؟

| الحاجة | النموذج | السبب |
|---|---|---|
| تحرير متدرج عبر محادثة | Omni Flash | `previous_interaction_id` يحفظ السياق |
| حلقة سلسة (loop) | Omni Flash | نفس الصورة كإطار أول وأخير |
| مقطع ≤ 10s مع إطارين | Omni Flash أو Seedance | كلاهما يدعم الاستيفاء |
| مقطع 11–15s متصل | **Seedance 2.0** | سقف Omni للتوليد 10s |
| دقة 4K | **Seedance 2.0** | يدعم 4K/1080p |
| مراجع حركة من فيديو | **Seedance 2.0** | Omni محدود بـ3 مقاطع × 3s |
| مراجع صوتية (إيقاع/موسيقى) | **Seedance 2.0** | Omni **لا يدعم** رفع مراجع صوتية |
| نقل رقصة/حركة من فيديو | **Seedance 2.0** | `Reference @Video1 for choreography` |
| قطع مشاهد داخل توليد واحد | **Seedance 2.0** | `Cut scene to…` |
| مشهد واحد متصل بلا قطع | **Omni Flash** | يتطلب الأمر صراحة؛ افتراضيًا يقسم لمشاهد |
| نسبة 21:9 أو 4:3 | **Seedance 2.0** | Omni يدعم 16:9 و 9:16 فقط |

---

## 2. Gemini Omni Flash — `gemini-omni-1.1-flash`

### المواصفات الثابتة

| المعامل | القيمة |
|---|---|
| `task` | `text_to_video` / `image_to_video` / `reference_to_video` / `edit` / `extend` |
| `aspect_ratio` | `16:9` (افتراضي) / `9:16` **فقط** |
| الدقة | 360p، 720p افتراضيًا؛ 1080p و 4K دقتان مكبَّرتان |
| مدة التوليد | 3–10 ثوانٍ (أعداد صحيحة) |
| التمديد | +10 ثوانٍ حتى 40 ثانية تراكميًا، **في الذيل فقط** |
| `duration` | أرسله صريحًا دائمًا — إن حُذف قرره النموذج |
| التسليم | `delivery: "uri"` للفيديوهات > 4MB |
| `thinking_level` | `low` / `default` / `high` |
| `seed` | ثبّته عند الحصول على مظهر معتمد |

### صيغ ربط المراجع (الأهم)

**الصيغة البسيطة (الموصى بها):**
```
<FIRST_FRAME> a woman is walking
<FIRST_FRAME> <LAST_FRAME> a woman is walking
<IMAGE_REF_0> — مرجع موضوع أو أسلوب (يبدأ من 0)
<VIDEO_REF_0> — مرجع حركة أو شخصية (حتى 3s)
```

**الصيغة المعلنة:**
```
[# Sources @Image1]                              ← الصورة الأولى كإطار بداية
[# Sources @Image1 @Image2]                      ← الأولى بداية، الثانية نهاية
[# Sources @Image1 @Image1]                      ← نفس الصورة للطرفين = حلقة
[# Sources @Image1] [# References @Image2]       ← بداية + مرجع
[# Sources @Video1]                              ← فيديو مصدري للتحرير
[# References @Image1 @Video1]                   ← مرجعان
```

**عبارات إرشادية تُلحق بآخر البرومبت (Google توصي بها حرفيًا):**
- للإطار الأول: `Use this image as the starting frame.`
- للحلقة: `Use this image as the first frame and the last frame.`
- للمراجع: `Use the given image(s) as references for video generation. The images should not be used as literal initial frames.`

### قواعد Omni الحاسمة

1. **مشهد واحد متصل:** افتراضيًا النموذج **يقسّم الفيديو إلى عدة مشاهد**. لمنع ذلك اكتب صراحة:
   ```
   In a single continuous shot, no scene cuts.
   ```
2. **التوقيت:** استخدم الأقواس: `[0-3s] walking [3-6s] stops and turns [6-10s] starts running` أو اللغة الطبيعية `after 3 seconds a woman enters`. التوقيت **توجيه تقريبي**، ليس تحكمًا frame-accurate.
3. **النفي:** لا يوجد حقل negative prompt. ضع النفي في البرومبت العادي: `no dialogue`, `no extra sound effects`.
4. **النص على الشاشة:** ضعه بين علامتي اقتباس: `a street sign that says: "This is an AI generation"`.
5. **التحرير الحواري:** قصير جدًا + `Keep everything else the same.` البرومبتات الطويلة تسبب تغييرات غير مقصودة.
6. **الصوت:** وجّهه بالوصف: `calm background music`, `a low tinny radio in the background`.
7. **الميتا-برومبت:** `Be extremely detailed in your descriptions of characters and environments. Apply costume design principles to characters.`

### قيود Omni الموثقة (لا تحاول تجاوزها)
- ❌ رفع مراجع صوتية غير مدعوم
- ❌ تحرير الصوت غير مدعوم
- ❌ الاستدلال عبر عدة فيديوهات مرجعية غير مدعوم — يدهور النتيجة
- ❌ صوت فيديو المرجع يُتجاهل
- ❌ `temperature`, `top_p`, `stop sequences`, `negative prompts`, `system instructions` غير مدعومة
- ❌ التمديد في الذيل فقط — لا بداية ولا وسط
- ❌ تمديد فيديو مرفوع فيه شخص يتحدث لإضافة حوار — غير متاح
- ❌ فيديو الإدخال للتمديد يجب أن يكون ≤ 10 ثوانٍ (إلا في multi-turn)
- ❌ فيديوهات YouTube كمصدر — غير مدعوم
- ⚠️ الإنجليزية مدعومة بالكامل؛ اللغات الأخرى غير مُقيَّمة

### قالب برومبت Omni — إطار واحد
```text
<FIRST_FRAME> Create a continuous video shot of [DURATION] seconds, in a
single continuous shot with no scene cuts.

Subject lock: [CHARACTER_ID], [IDENTITY_STRING], [COSTUME_STRING].
Primary action: [فعل مرئي واحد باتجاه وكمية ونهاية واضحة].
Camera: [حركة واحدة], [السرعة], fixed lens, no rotation, no zoom.
Timing: [0-3s] …; [3-7s] …; [7-10s] ….
Audio: [حوار قصير إن وجد], [مؤثرات], [ambience], [موسيقى أو صمت].
Continuity: preserve face, hair, costume, prop, screen direction, and light
direction exactly.

Use this image as the starting frame.
```

### قالب برومبت Omni — إطاران
```text
<FIRST_FRAME> <LAST_FRAME> Create a continuous video transition of about
[DURATION] seconds between these two frames, in a single continuous shot
with no internal cut.

Keep constant: [IDENTITY_STRING], [COSTUME_STRING], [PROP], [LOCATION],
[aspect ratio], and [lighting logic].
Timeline: [0-3s] …; [3-7s] …; [7-10s] ….
Subject motion: [فعل واحد متدرج] moving from the starting pose to the
ending pose.
Camera: [حركة واحدة], no rotation, no abrupt perspective change.
Audio: [مؤثرات/حوار/صمت] with continuous environmental ambience.

The only intentional changes are: [قائمة التغيرات المقصودة فقط].
```

### قالب برومبت Omni — تحرير حواري
```text
[التعديل الواحد المحدد]. Keep everything else the same.
```
**مثال:** `Make the phone invisible. Keep everything else the same.`

### قالب برومبت Omni — امتداد
```text
The scene continues. [وصف ما يحدث في المقطع الجديد].
Keep the same character identity, wardrobe, location, time of day, camera
lens, and color grade. Continue the existing [camera move] at the same
speed. Continue the existing ambient audio.
```
> **ملاحظة:** عند الامتداد، `0s` في البرومبت يشير إلى **بداية المقطع الجديد**، لا بداية الفيديو الكلي.

### قالب برومبت Omni — حلقة
```text
[# Sources @Image1 @Image1] [وصف الحركة الدائرية]. Use this image as the
first frame and the last frame. Seamless loop, no visible restart point.
```

---

## 3. Seedance 2.0 — `bytedance/seedance-2.0`

### المواصفات الثابتة

| المعامل | القيمة |
|---|---|
| `duration` | 4–15 ثانية، أو `auto` (يطابق أطول فيديو مرجعي، مقصوص 4–15) |
| `resolution` | `480p` / `720p` (افتراضي) / `1080p` / `4k` — **حسب القناة** |
| `aspect_ratio` | `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `generate_audio` | `true` افتراضيًا — مؤثرات + محيط + كلام متزامن |
| `seed` | للتكرار |
| الإطارات | 24 fps |
| المراجع | حتى 9 صور + 3 فيديوهات + 3 صوتيات = 12 ملفًا |
| حدود الملفات | صور ≤ 30MB؛ فيديو 2–15s ≤ 50MB؛ صوت ≤ 15s ≤ 15MB |

### نظام الوسوم `@`

| الوسم | الدور | مثال |
|---|---|---|
| `@Image1` … `@Image9` | مراجع صور (ترتيب الرفع) | `@Image1 as the first frame` |
| `@Video1` … `@Video3` | مراجع فيديو | `Reference @Video1 for camera movement only` |
| `@Audio1` … `@Audio3` | مراجع صوتية | `Use @Audio1 for background music and rhythm` |

### أدوار الصور الخمسة
| الاستخدام | الصيغة |
|---|---|
| إطار أول | `@Image1 as first frame` |
| إطار أخير | `@Image1 as last frame` |
| مرجع شخصية | `@Image1 as character reference` |
| بيئة | `@Image1 as background environment` |
| أسلوب | `@Image1 as style reference` |

### ⚠️ القيد الأهم في Seedance
> **وضع الإطار الأول/الأخير يستثني مراجع الصور والفيديو.** لا يمكن الجمع بينهما في توليد واحد.
>
> **والمرجع الصوتي يتطلب** وجود صورة أو فيديو مرجعي واحد على الأقل. الصوت وحده لا يُقبل.

### القاعدة الذهبية لـ Seedance: أعطِ كل أصل وظيفة
```
❌ @Video1  (وسم عارٍ — هذا أشهر سبب فشل)
✅ Reference @Video1 for camera movement and pacing only, not for character appearance.
```

### قاعدة طول البرومبت
> **الالتزام يتناقص حسب الموضع.** أول 2–3 تعليمات تُنفَّذ بموثوقية؛ برومبت فيه 8 متطلبات يُنفَّذ منه 4–5 عادة. اجعل البرومبت **60–100 كلمة** وضع غير القابل للتفاوض في المقدمة.

### قاعدة السرعة
> **عنصر واحد فقط يمكن أن يكون «سريعًا» في الوقت نفسه.** سرعة الموضوع + سرعة الكاميرا + سرعة القص = تشوّه.

### قالب برومبت Seedance — صورة إلى فيديو
```text
@Image1 as the first frame and character reference.

[0-4s] [الفعل الرئيسي مع الاتجاه]. Camera: [حركة واحدة], [السرعة].
[4-8s] [التطور]. Lighting stays [وصف الإضاءة].
[8-12s] [النتيجة/الكشف].

Keep [CHARACTER_ID]'s face, hair, and clothing identical to @Image1.
Anatomically correct hands. Avoid jitter and bent limbs.
Sound: [مؤثرات], [ambience], no music.
```

### قالب برومبت Seedance — إطاران
```text
@Image1 is the exact first-frame composition. @Image2 is the exact
last-frame composition.

[Timeline]
0-2s: [الوضعية الافتتاحية].
2-6s: [الفعل المتدرج في حركة واحدة متصلة].
6-8s: [الاستقرار على تكوين الإطار الأخير].

Keep [المكان، اتجاه المطر، الملابس، الدعامة، اتجاه الشاشة] consistent.
Do not override either anchor with other references. No teleportation,
no reverse entry, no unexplained camera cut.
```

### قالب برومبت Seedance — نقل حركة
```text
@Image1 as character reference.
Reference @Video1 for camera movement and performance rhythm only, not for
appearance.

[وصف المشهد الجديد]. [حركة الكاميرا]. [الإضاءة].
```

### قالب برومبت Seedance — لقطات متعددة بتقطيع
```text
@Image1 [الوصف]. Cut scene to @Image1 [الوصف الجديد]. Cut scene to
[وصف اللقطة الثالثة].

Use timestamps to control pacing: at 5 seconds [الحدث].
```

### قالب برومبت Seedance — امتداد
```text
Continue from @Video1. [وصف المشهد الجديد].
Maintain exact same lighting, character appearance, and style from the
previous clip.
```
> **قاعدة الامتداد:** مدة الامتداد = **الثواني الجديدة فقط**، لا الإجمالي. وأعد تثبيت الشخصية/الإضاءة/الأسلوب كل 2–3 امتدادات.

---

## 4. دورة التكرار المنضبطة

لكل لقطة، اتبع هذا التسلسل — لا تقفز:

| # | التمريرة | الهدف | ما تغيّره |
|---|---|---|---|
| 1 | **Baseline** | صورة مرجعية نظيفة + برومبت حركة أساسي | لا شيء — هذا خط الأساس |
| 2 | **Motion pass** | فعل الشخصية وحده | الفعل فقط |
| 3 | **Camera pass** | أضف حركة كاميرا واحدة | الكاميرا فقط |
| 4 | **Continuity pass** | افحص الوجه والملابس والدعائم والضوء | الاستمرارية |
| 5 | **Audio pass** | المؤثرات أو الحوار | الصوت فقط |
| 6 | **Edit pass** | اختبر اللقطة **داخل السياق** | لا شيء — تقييم |
| 7 | **Approval** | اعتمد واحتفظ كمرجع | — |

**قاعدة:** متغير واحد أو مجموعة صغيرة في كل تكرار. التغيير الجماعي يجعل الفشل غير قابل للتشخيص.

### سجل التوليد الإلزامي
لكل محاولة سجّل:
```
| المحاولة | البرومبت | النموذج | التاريخ | المدخلات | الدقة | النسبة | seed | previous_id | سبب الرفض | القرار |
```

---

## 5. صيغة التسليم

````markdown
### [SC01_SH03] — تحريك
**النموذج:** Gemini Omni Flash (`gemini-omni-1.1-flash`)
**المهمة:** `image_to_video` (إطاران)
**المعاملات:** `aspect_ratio: "16:9"` · `duration: 10` · `resolution: "720p"` · `thinking_level: "high"`
**المدخلات:** `SC01_SH03_FR01_v002.png` → `<FIRST_FRAME>` · `SC01_SH03_FR02_v001.png` → `<LAST_FRAME>`
**اسم الملف:** `SC01_SH03_v001_rough.mp4`

```text
<FIRST_FRAME> <LAST_FRAME> Create a continuous video shot of about 10
seconds between these two frames, in a single continuous shot with no
internal cut.

Keep constant: LAYAN-01, an Arab woman in her late twenties, oval face,
hazel eyes, short wavy black bob ending at the jaw, a thin scar above the
left eyebrow, mustard-yellow wool coat, dark green canvas bag on the left
shoulder, metal key in the right hand. Preserve the wet station platform,
the cyan neon backlight, and left-to-right screen direction.

Timeline: [0-3s] Layan walks three slow steps toward the lamp control
panel, the key visible in her right hand; [3-6s] she stops, raises the key,
and switches on the lamp; [6-8s] the light shifts from cool cyan to a warm
amber glow across her face; [8-10s] she lowers her head slightly and looks
into the puddle, where the reflection of a black train with no windows
appears before any real train is visible.

Camera: a slow forward dolly, naturally moving from a medium shot toward a
close shot. Fixed lens, no rotation, no zoom, no abrupt perspective change.

Audio: continuous light rain, three clear footsteps, a metal key click, a
brief electrical hum when the lamp turns on, then a muffled distant train
rumble in the final two seconds. No dialogue and no music.

The only intentional changes are Layan moving to the lamp panel, the lamp
turning on, and the train reflection appearing in the puddle.
```
````

---

## بوابة الخروج من M5

- [ ] كل لقطة لها برومبت بلهجة نموذجها المحدد
- [ ] كل برومبت يحترم سقف مدة النموذج
- [ ] الوسوم صحيحة (`<FIRST_FRAME>` لـ Omni، `@Image1` لـ Seedance)
- [ ] حركة كاميرا واحدة مهيمنة في كل برومبت
- [ ] فعل مرئي واحد مهيمن في كل برومبت
- [ ] الاستمرارية مذكورة صراحة في كل برومبت
- [ ] خطة دورة التكرار محددة (أي تمريرة أولًا)
- [ ] سجل التوليد جاهز للتعبئة


---

## عقد التشغيل v1.1

نفّذ هذا الوكيل كوحدة قابلة للتتبع وفق `references/protocols/`. في نهاية كل تشغيل، أخرج:
- **INPUT ARTIFACTS**: IDs + Versions التي استلمتها.
- **OUTPUT ARTIFACTS**: IDs + Versions التي أنشأتها.
- **VALIDATION**: اختبارات PASS/FAIL.
- **STATE UPDATE**: الحقول التي تغيرت في `state/`.
- **GATE**: `PASS` أو `FAIL` أو `REQUIRES_REVIEW`.
- **NEXT**: الوكيل/المرحلة التالية.

إذا فشل الناتج: لا تتقدم. سجّل التشخيص في `schemas/state/generation-log.md` عند التوليد، أو في سجل الحالة المناسب، وحدد متغير الإصلاح قبل إعادة المحاولة.


## v1.3 Prompt Runtime Contract
عند إنتاج مخرج تنفيذي، لا تسلّم Prompt نهائيًا مباشرة. ابنِ داخليًا Canonical Prompt Spec ثم مرره إلى `references/specs/` و`references/specs/` قبل التسليم. المستخدم يرى فقط النسخة المجمعة والجاهزة للنسخ.
