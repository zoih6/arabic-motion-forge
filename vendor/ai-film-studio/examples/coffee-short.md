# مثال حي — تشغيل كامل للمهارة

> هذا مخرَج فعلي ناتج عن تطبيق مسار المهارة على طلب غامض من سطر واحد.
> استُخدم كمعيار لما يجب أن يبدو عليه التسليم.

---

# طلب المستخدم

> **«أبغى فيديو عن القهوة»**

---

## M0 — الاستقبال والتفكيك

### التحليل الثلاثي

**المعلوم:**
- الموضوع: القهوة

**المجهول الحرج 🔴:**
- الغرض (إعلان؟ محتوى عضوي؟ قصة؟)
- المنصة ونسبة الأبعاد
- الجمهور

**المجهول المهم 🟠:**
- الطول، النبرة البصرية، البطل

**المتناقض:** لا يوجد

### التفسير المقترح
> **ما فهمته:** تريد فيديو قصيرًا عن القهوة، على الأرجح محتوى سوشيال، بإحساس دافئ وحميمي.
>
> **ما افترضته:** شورت عمودي 9:16، 15 ثانية، بطله باريستا، بلا حوار.
>
> **ما أحتاجه منك:** 6 أسئلة.

### الأسئلة الستة (بافتراضاتها)
| # | السؤال | الافتراضي إن لم تُجب |
|---|---|---|
| 1 | الغرض: إعلان / سوشيال عضوي / قصة قصيرة / شرح؟ | سوشيال عضوي |
| 2 | المنصة: TikTok / YouTube / Instagram؟ | TikTok → 9:16 |
| 3 | الطول: 8–15s / 20–30s / 45–60s؟ | 15 ثانية |
| 4 | النبرة: واقعي سينمائي / إعلاني أنيق / درامي داكن؟ | واقعي سينمائي |
| 5 | البطل: شخص / منتج / أجواء؟ | باريستا |
| 6 | قيود أو ممنوعات؟ | لا قيود |

### الملخص المعتمد (بعد الإجابات)
| الحقل | القيمة |
|---|---|
| عنوان العمل | أول رشفة |
| نوع المحتوى | شورت/ريل |
| الغرض | محتوى سوشيال عضوي — تفاعل |
| الجمهور | 20–35، مهتمون بالقهوة المختصة |
| المنصة | TikTok |
| نسبة الأبعاد | 9:16 |
| المدة | 15 ثانية |
| عدد اللقطات | 1 (متصلة) |
| النبرة | واقعي سينمائي دافئ |
| البطل | باريستا (شخص) |
| الحوار | لا |
| نموذج الصور | Nano Banana 2 (`gemini-3.1-flash-image`) |
| نموذج الفيديو | Seedance 2.0 (`bytedance/seedance-2.0`) |

**سبب اختيار النماذج:**
- Nano Banana 2 لأنه يدعم 9:16 أصلًا (GPT Image 2 لا يدعمها)، وبسرعة تكرار عالية.
- Seedance 2.0 لأن المدة 15 ثانية — **Omni Flash سقفه 10 ثوانٍ**.

---

## M1 — المفهوم الإبداعي

### اللوجلاين
> باريستا في مقهى صنعاني قديم يسكب أول رشفة من اليوم، وفي لحظة ارتفاع البخار يرى في الفنجان وجه المدينة التي لم يستيقظ أحد فيها بعد.

### البنية (نموذج الخطاف الثلاثي)
| القسم | الزمن | المحتوى |
|---|---|---|
| الخطاف | 0–4s | بخار يخترق ضوء نافذة — تكوين غير مألوف |
| الجسم | 4–9s | السكب، امتلاء الفنجان، استرخاء الكتفين |
| الدفع | 9–15s | يرفع نظره إلى النافذة ويثبّت النظرة |

### الهوية البصرية
| الحقل | القيمة |
|---|---|
| النوع البصري | واقعي سينمائي |
| المرجعيات | إضاءة Emmanuel Lubezki الطبيعية، حميمية Wong Kar-wai |
| العدسة | 50mm |
| الفتحة | f/2.0 |
| اللون المهيمن | amber في الإضاءات |
| اللون المضاد | بني عميق في الظلال |
| الممنوع | أبيض بارد، أزرق مشبع |
| مصدر الإضاءة | نافذة يسار الكادر |
| الجودة | hard key بلا fill |
| الحرارة | 3200K |
| التباين | عالٍ |
| القوام | 35mm film grain + halation |
| الحركة | dolly ناعم |

---

## M2 — قفل الهوية

### بطاقة شخصية: SAMI-01

**Identity String (يُلصق حرفيًا في كل برومبت — لا يُعاد صياغه ولا يُعاد التفاف أسطره):**
```
a Yemeni man in his early thirties, angular jaw, deep brown eyes, short cropped black beard with a small grey patch on the left cheek, a faint burn scar on the back of his right hand
```

**Costume String:**
```
charcoal-grey apron over a faded white henley, sleeves rolled to the forearm
```

**الدعائم:** إبريق نحاسي باليد اليمنى (يمين اليد مهيمنة)
**السلوك:** كتفان متوترا قليلًا، نظره لا يفارق ما تصنع يداه
**العلامات المميزة:** ① رقعة شيب في الخد الأيسر ② أثر حرق على ظهر اليد اليمنى

### حزمة المراجع
| المعرّف | المحتوى |
|---|---|
| `SAMI-01_ID_FR_v001` | وجه أمامي، إضاءة محايدة |
| `SAMI-01_ID_34_v001` | ثلاثة أرباع يسار |
| `SAMI-01_FULL_v001` | كامل الجسم + الملابس |
| `SAMI-01_PROP_v001` | الإبريق النحاسي |

### كتاب العالم: CAFE-SANAA-01
| الحقل | القيمة |
|---|---|
| المكان | مقهى صنعاني قديم، داخلي |
| الزمن | فجر، قبل الشروق |
| المواد | نحاس معتّق، خشب داكن ظاهر الألياف، جص أبيض متشقق |
| الضوء | نافذة واحدة يسار الكادر فقط |
| قواعد صارمة | لا مصابيح حديثة، لا شعارات مقروءة، لا هواتف |
| الممنوعات | إضاءة LED بيضاء، أثاث حديث |

---

## M3 — قائمة اللقطات

| SHOT_ID | الغرض | الحجم | المدة | الفعل | الكاميرا | النموذج |
|---|---|---|---|---|---|---|
| SC01_SH01 | طقس كامل: سكب + نظرة | MCU | 15s | يسكب، ثم يرفع نظره | slow dolly in | Seedance 2.0 |

### بطاقة اللقطة
```
SHOT_ID:        SC01_SH01
الغرض الدرامي:  طقس الصباح الكامل في حركة واحدة
المدة:          15.00s
ما يجب أن يفهمه المشاهد: هذه لحظة خاصة قبل أن تستيقظ المدينة
التأطير/الزاوية: لقطة متوسطة قريبة، الكاميرا على مستوى الصدر
العدسة:         50mm @ f/2.0
الموضوع:        SAMI-01، مريلة رمادية فحمية
الفعل:          يرفع الإبريق، يسكب ببطء، يضعه، يرفع نظره
حركة الكاميرا:  slow dolly in, fixed lens, no rotation, no zoom
البيئة:         مقهى صنعاني، فجر، ذرات غبار في الهواء
الإضاءة:        مفتاح قاسٍ واحد من نافذة يسار الكاميرا 3200K، بلا fill
البداية:        واقف خلف الطاولة، الإبريق بيده اليمنى
النهاية:        الإبريق موضوع، النظر مثبّت على النافذة
التسلسل:        [0-4s] يرفع ويبدأ السكب ; [4-9s] الفنجان يمتلئ ;
                [9-15s] يضع الإبريق ويرفع نظره
الصوت:          سكب، ambience منخفض، حركة شارع بعيدة؛ لا حوار ولا موسيقى
المحور:         ← يمين (من اليسار إلى اليمين)
خط النظر:       لأسفل ثم لأعلى
الاستمرارية:    الندبة على اليد اليمنى، رقعة الشيب، المريلة
نقطة القطع:     بعد تثبيت النظرة بثانية
النموذج:        Seedance 2.0 (15s)
معيار القبول:   الوجه ثابت، اليدان سليمتان، البخار طبيعي، النظر يثبت
معيار الرفض:    تبدل الوجه، أصابع زائدة، قطع داخلي، إبريق متغير الشكل
```

---

## M4 — برومبت الصورة المرجعية

### [SC01_SH01_FR01] — الإطار الأول
**النموذج:** `gemini-3.1-flash-image`
**المعاملات:** `aspect_ratio: "9:16"` · `image_size: "2K"`
**المراجع:** `SAMI-01_FULL_v001` (شخصية) · `SAMI-01_PROP_v001` (إبريق)
**الملف:** `SC01_SH01_FR01_v001.png`

```text
Cinematic film still, single frame, no text overlay.

SUBJECT: SAMI-01, a Yemeni man in his early thirties, angular jaw, deep brown eyes, short cropped black beard with a small grey patch on the left cheek, a faint burn scar on the back of his right hand. Charcoal-grey apron
over a faded white henley, sleeves rolled to the forearm.
POSE: standing behind a dark wood counter, both hands steady on a brass
kettle at chest height, weight on the back foot, gaze fixed downward on the
empty cup below.
FRAMING: medium close-up, camera at chest height, subject in the right
third of frame, steam rising through the upper left negative space.
ENVIRONMENT: an old Sanaa coffee house at dawn, dust motes suspended in
the air, worn brass fittings, dark wood counter with visible grain, cracked
white plaster walls.
CAMERA: shot on 50mm at f/2.0, moderate depth of field, background softly
out of focus.
LIGHTING: single hard key light from a window camera-left at 3200K, no
fill, deep shadow on the camera-right side of the face, small catchlight in
both eyes.
COLOR & TEXTURE: amber-dominant highlights with deep brown shadows, 35mm
film grain, subtle halation around the window light.
CONSTRAINTS: no readable text, no logos, no additional characters,
anatomically correct hands with five fingers, natural joint articulation.
```

---

## M5 — برومبت التحريك

### [SC01_SH01] — تحريك
**النموذج:** `bytedance/seedance-2.0`
**المعاملات:** `duration: "15"` · `aspect_ratio: "9:16"` · `resolution: "720p"` · `generate_audio: true`
**المدخلات:** `SC01_SH01_FR01_v001.png` → `@Image1`
**الملف:** `SC01_SH01_v001_rough.mp4`

```text
@Image1 as the first frame and character reference.

[0-4s] SAMI-01 lifts the brass kettle and begins a slow, steady pour; steam
rises through the window light and drifts toward camera-left. Camera: slow
dolly in, fixed lens, no rotation, no zoom.
[4-9s] The stream of coffee thickens and the cup fills; his shoulders
relax, gaze still on the pour. Lighting stays a single hard 3200K key from
camera-left.
[9-15s] He sets the kettle down on the counter and looks up toward the
window, holding the look through the final beat.

Keep SAMI-01's face, beard, apron, and the burn scar on his right hand
identical to @Image1. Anatomically correct hands with five fingers. Avoid
jitter and bent limbs. Screen direction: left to right. Sound: kettle pour,
low room ambience, distant street traffic, no dialogue, no music.
```

### دورة التكرار المقررة
| # | التمريرة | ما يُغيَّر |
|---|---|---|
| 1 | Baseline | لا شيء — تقييم أولي |
| 2 | Motion pass | فعل السكب فقط |
| 3 | Camera pass | سرعة الـ dolly |
| 4 | Continuity pass | الندبة، الشيب، المريلة |
| 5 | Audio pass | توقيت السكب |
| 6 | Edit pass | داخل السياق |

---

## M6 — الصوت

### SC01_SH01
| الطبقة | المحتوى | التوقيت |
|---|---|---|
| **Ambience** | غرفة منخفضة، حركة شارع بعيدة مكتومة | 0–15s مستمر |
| **Foley** | احتكاك الإبريق بالطاولة | 0.4s |
| **Foley** | سكب مستمر | 0.8–9.0s |
| **Foley** | وضع الإبريق على الخشب | 9.3s |
| **SFX** | — | — |
| **Dialogue** | لا يوجد | — |
| **Music** | لا توجد | — |

**ذروة الصوت:** 9.3s (وضع الإبريق) — تفتح الصمت الذي يسبق النظرة.
**نقطة الصمت:** 9.5–10.5s قبل رفع النظر.

**قرار الموسيقى:** بلا موسيقى. الطقس حميمي والمؤثرات تكفي.

---

## M7 — المونتاج والتسليم

| الحقل | القيمة |
|---|---|
| timebase | 24 fps (مطابق لمخرج Seedance) |
| المدة | 15.00s = 360 إطارًا |
| نقطة القطع | 14.5s — بعد تثبيت النظرة |
| الانتقالات | لا شيء (لقطة واحدة) |
| التدرج | تصحيح أولًا، ثم amber/brown مع رفع السواد إلى IRE 8 |

### مواصفات التصدير
| النسخة | الحاوية | الترميز | الدقة | FPS | الصوت |
|---|---|---|---|---|---|
| Master | MP4 | H.264 High | 1080×1920 | 24 | PCM 48kHz |
| TikTok | MP4 | H.264 | 1080×1920 | 24 | AAC-LC |

### QC
- [ ] تقنية: المدة 15.00s مقروءة من خصائص الملف
- [ ] بصرية: الوجه ثابت، اليدان بخمسة أصابع، الندبة ظاهرة، الإبريق لم يتغير
- [ ] سمعية: السكب يبدأ قبل الصورة ويستمر بعد القطع (sound bridge)

---

## ملاحظات الإنتاج

- **لماذا لم يُستخدم Omni Flash؟** المدة 15 ثانية تتجاوز سقفه (10 ثوانٍ). لو طلب المستخدم 10 ثوانٍ أو أقل، لكان Omni خيارًا أفضل بسبب التحكم الأدق.
- **لماذا لم يُستخدم GPT Image 2؟** لا يدعم 9:16 أصلًا — كان سيتطلب قصًّا من 2:3.
- **العلامة المائية:** المخرجات تحمل SynthID (صور) و C2PA (فيديو) غير مرئية.
- **النص:** لو أراد المستخدم عنوانًا، يُبنى في GPT Image 2 ويُركَّب في المونتاج — لا يُولَّد داخل الفيديو.
