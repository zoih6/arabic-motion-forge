# مكتبة أنماط البرومبتات الجاهزة

أنماط مُختبرة قابلة للتعبئة. استبدل `[الأقواس]` وابقِ الباقي حرفيًا.

---

## 1. أنماط الصور المرجعية

### نمط: مرجع هوية — وجه أمامي
```text
Character reference sheet, identity lock. [IDENTITY_STRING]. Front-facing
portrait, neutral expression, eyes open and clearly visible, both eyebrows
visible. Even soft studio lighting from front-left at 5600K, no dramatic
shadows, no colored light. Plain light gray seamless background. Shot on
85mm at f/4, sharp focus on eyes, natural skin texture with visible pores.
No makeup stylization, no filters. 1:1 crop from chest up.
```

### نمط: مرجع هوية — متعدد الزوايا
```text
Character turnaround sheet on a plain light gray background. The same
person, [IDENTITY_STRING], wearing [COSTUME_STRING]. Four views in a single
row, left to right: front view, three-quarter left view, full side profile
view, back view. Identical lighting across all four views: even soft studio
light, 5600K, no dramatic shadows. Identical scale and camera height in all
views. Full body visible including feet. Neutral standing pose, arms relaxed
at sides. No text, no labels, no panel borders.
```

### نمط: مرجع دعامة
```text
Object reference sheet. [PROP_DESCRIPTION], placed alone on a plain light
gray seamless background. Even soft studio lighting from front-left, no
dramatic shadows. Full object visible with clear silhouette. Shot on 50mm
at f/8 for maximum sharpness. Three angles in one row: front, side,
top-down. Consistent scale. No text, no labels.
```

### نمط: مرجع أسلوب (بلا شخصيات)
```text
Lighting and color style reference, no people. [ENVIRONMENT_DESCRIPTION].
Key light from [DIRECTION] at [TEMPERATURE], [SOFT/HARD] quality. Color
palette: [DOMINANT] in shadows, [ACCENT] in highlights. Contrast ratio:
[LOW/HIGH]. Texture: [FILM_GRAIN/CLEAN_DIGITAL]. Shot on [LENS] at
[APERTURE]. No characters, no faces, no readable text, no logos.
```

---

## 2. أنماط الفريمات السينمائية

### نمط: بورتريه درامي
```text
Cinematic film still, single frame.

SUBJECT: [IDENTITY_STRING]. [COSTUME_STRING].
POSE: [الوضعية], gaze directed [الاتجاه], [تعبير محدد بالجسد لا بالصفة].
FRAMING: close-up, camera at eye level, subject in [الموضع], shallow
headroom, [ملاحظة الفراغ السلبي].
ENVIRONMENT: [المكان]، [الزمن]، [الطقس].
CAMERA: shot on 85mm at f/1.8, background dissolved into bokeh.
LIGHTING: Rembrandt setup — single hard key from camera-left at 45 degrees
and slightly above, 3200K tungsten, minimal fill, deep shadow on the
camera-right side of the face, small catchlight in both eyes.
COLOR & TEXTURE: [اللوحة], Kodak Vision3 500T grain, subtle halation.
CONSTRAINTS: no readable text, no logos, anatomically correct hands.
```

### نمط: لقطة واسعة تأسيسية
```text
Cinematic film still, single frame, establishing shot.

FRAMING: extreme wide shot, camera [الارتفاع والزاوية], [الشخصية] occupying
approximately [النسبة]% of the frame, positioned [الموضع], vast negative
space [الموضع].
ENVIRONMENT: [وصف مفصل للمكان — المواد، الأسطح، العمق، الطقس].
CAMERA: shot on 24mm at f/5.6, deep depth of field, foreground to horizon
in focus.
LIGHTING: [المصدر والاتجاه والحرارة]. [الظلال].
COLOR & TEXTURE: [اللوحة], [القوام].
CONSTRAINTS: no readable text, no logos, no additional characters,
[الشخصية] must be clearly identifiable despite the small scale.
```

### نمط: لقطة منتج إعلانية
```text
Commercial product photograph, single frame.

SUBJECT: [PRODUCT_DESCRIPTION — الشكل، الخامة، اللون، التفاصيل].
FRAMING: [الحجم], product centered or in [الموضع], [زاوية الكاميرا].
ENVIRONMENT: [السطح], [الخلفية], [العناصر المساندة].
CAMERA: shot on 100mm macro at f/8, focus stacked sharpness across the
entire product, [ملاحظة الانعكاسات].
LIGHTING: high-key studio setup — large softbox overhead at 5600K, two
strip lights at 45 degrees left and right for edge definition, subtle
gradient background, controlled specular highlights.
COLOR & TEXTURE: clean neutral palette, product colors accurate and
saturated, no color cast, crisp micro-detail on [الخامة].
CONSTRAINTS: no readable text unless specified, no logos other than the
product's own, no hands, no props competing with the product.
```

### نمط: لقطة ليلية حضرية
```text
Cinematic film still, single frame.

SUBJECT: [IDENTITY_STRING]. [COSTUME_STRING].
POSE: [الوضعية والحركة].
FRAMING: [الحجم], [الزاوية], subject in [الموضع].
ENVIRONMENT: [المدينة]، night، [الطقس]، wet asphalt reflecting light,
steam rising from [المصدر], distant traffic bokeh.
CAMERA: shot on 35mm at f/1.4, shallow depth of field, anamorphic
character with horizontal lens flare from [المصدر].
LIGHTING: mixed sources — cyan neon sign backlight at 6500K from
camera-right, warm sodium street lamp at 2200K from camera-left, practical
window light in the background. High contrast, deep blacks.
COLOR & TEXTURE: teal-and-amber split toning, 35mm grain, halation around
all light sources.
CONSTRAINTS: no readable text, no real brand logos, anatomically correct
hands.
```

---

## 3. أنماط التحريك — Omni Flash

### نمط: صورة واحدة إلى فيديو
```text
<FIRST_FRAME> Create a continuous video shot of [DURATION] seconds, in a
single continuous shot with no scene cuts.

Subject lock: [CHARACTER_ID], [IDENTITY_STRING], [COSTUME_STRING].
Primary action: [فعل واحد باتجاه وكمية ونهاية].
Camera: [حركة واحدة], [السرعة], fixed lens, no rotation, no zoom.
Timing: [0-3s] …; [3-7s] …; [7-10s] ….
Audio: [مؤثرات], [ambience], [موسيقى أو صمت].
Continuity: preserve face, hair, costume, prop, screen direction, and light
direction exactly.

Use this image as the starting frame.
```

### نمط: إطاران — تحول درامي
```text
<FIRST_FRAME> <LAST_FRAME> Create a continuous video transition of about
[DURATION] seconds between these two frames, in a single continuous shot
with no internal cut.

Keep constant: [IDENTITY_STRING], [COSTUME_STRING], [PROP], [LOCATION],
and [lighting logic].
Timeline: [0-3s] …; [3-7s] …; [7-10s] ….
Subject motion: [فعل متدرج واحد] moving from the starting pose to the
ending pose.
Camera: [حركة واحدة], no rotation, no abrupt perspective change.
Audio: [الصوت] with continuous environmental ambience.

The only intentional changes are: [قائمة التغيرات].
```

### نمط: حلقة سلسة
```text
[# Sources @Image1 @Image1] [وصف الحركة الدائرية المتكررة]. Use this image
as the first frame and the last frame. Seamless loop with no visible
restart point, constant motion speed throughout.
```

### نمط: تحرير حواري
```text
[التعديل الواحد المحدد والمرئي]. Keep everything else the same.
```

### نمط: امتداد مشهد
```text
The scene continues. [وصف ما يحدث في المقطع الجديد].
Keep the same character identity, wardrobe, location, time of day, camera
lens, and color grade. Continue the existing [camera move] at the same
speed. Continue the existing ambient audio. No new dialogue. End on a
stable [الحجم] shot.
```

### نمط: منتج دوّار
```text
<FIRST_FRAME> Create a continuous video shot of [DURATION] seconds, in a
single continuous shot.

The product rotates slowly on [السطح], one full turn, keeping the logo
readable throughout. Soft key light stays fixed as the product turns.
Shallow depth of field maintained. Camera locked off, no camera movement.
Sound design: quiet ambient studio tone only, no music, no dialogue.

Use this image as the starting frame.
```

---

## 4. أنماط التحريك — Seedance 2.0

### نمط: صورة إلى فيديو مع مرجع
```text
@Image1 as the first frame and character reference.

[0-4s] [الفعل الرئيسي مع الاتجاه]. Camera: [حركة واحدة], [السرعة].
[4-8s] [التطور]. Lighting stays [وصف الإضاءة].
[8-12s] [النتيجة].

Keep [CHARACTER_ID]'s face, hair, and clothing identical to @Image1.
Anatomically correct hands. Avoid jitter and bent limbs.
Sound: [مؤثرات], [ambience], no music.
```

### نمط: إطاران
```text
@Image1 is the exact first-frame composition: [الوصف].
@Image2 is the exact last-frame composition: [الوصف].

[Timeline]
0-2s: [الافتتاح].
2-6s: [الفعل المتدرج في حركة واحدة متصلة].
6-8s: [الاستقرار على الإطار الأخير].

Keep [المكان، الاتجاه، الملابس، الدعامة] consistent. Do not override
either anchor with other references. No teleportation, no reverse entry,
no unexplained camera cut.
```

### نمط: نقل حركة من فيديو
```text
@Image1 as character reference. @Image2 as environment reference.
Reference @Video1 for camera movement and performance rhythm only, not for
appearance.

[وصف المشهد الجديد]. [حركة الكاميرا]. [الإضاءة].
```

### نمط: لقطات متعددة بتقطيع
```text
@Image1 [الوصف]. Cut scene to @Image1 [الوصف الجديد]. Cut scene to [الثالث].
Use timestamps: at 5 seconds [الحدث].
```

### نمط: إعلان منتج بثلاث نبضات
```text
@Image1 as the first frame and product reference.

[0-5s] المشكلة: [الوصف]. Camera: [حركة].
[5-10s] الكشف: [المنتج يدخل المشهد]. Camera: [حركة].
[10-15s] الحل: [النتيجة]. Camera: [حركة].

Keep the product's shape, color, and label identical to @Image1 across all
three beats. Sound: [مؤثرات متصاعدة], no dialogue.
```

### نمط: امتداد
```text
Continue from @Video1. [وصف المشهد الجديد]. Maintain exact same lighting,
character appearance, and style from the previous clip.
```

---

## 5. أنماط حسب نوع المحتوى

### إعلان منتج — 15 ثانية (Seedance)
```text
@Image1 as product reference, @Image2 as first frame.

[0-3s] Extreme close-up on [تفصيل المنتج], slow dolly in, soft key light
sweeping across the surface.
[3-8s] Cut scene to medium shot — [المنتج أثناء الاستخدام], camera orbits
slightly, [الأثر المرئي].
[8-12s] Cut scene to close-up on [النتيجة], warm light shift, shallow
depth of field.
[12-15s] Final pack shot, product centered, camera locked, clean background.

Keep the product identical to @Image1 in every beat. Sound: [مؤثرات],
[subtle music], no dialogue.
```

### شورت/ريل — 20 ثانية (Seedance أو Omni)
```text
[0-3s] [خطاف يكسر التوقع — حركة مفاجئة أو تكوين غير مألوف]. Camera: [حركة
سريعة واحدة].
[3-9s] [التصعيد الأول]. Camera: [حركة].
[9-15s] [الذروة]. Camera: [حركة].
[15-20s] [الوقفة الأخيرة]. Camera: locked.

Sound: [إيقاع متصاعد], [مؤثر عند الذروة], no dialogue.
```

### فيلم قصير — لقطة درامية (Omni)
```text
<FIRST_FRAME> Create a continuous video shot of 10 seconds, in a single
continuous shot with no scene cuts.

Subject lock: [CHARACTER_ID], [IDENTITY_STRING].
Primary action: [فعل واحد متدرج يعبر عن الانفعال بالجسد].
Camera: slow forward dolly, fixed lens, no rotation, no zoom.
Timing: [0-3s] [الوضع]; [3-7s] [الفعل]; [7-10s] [رد الفعل — نقطة القطع].
Audio: [ambience مستمر], [مؤثر واحد عند نقطة التحول], no dialogue, no music.
Continuity: preserve face, hair, costume, screen direction, and light
direction exactly.

Use this image as the starting frame.
```

### شرح/تعليمي
```text
<FIRST_FRAME> Create a continuous video shot of [DURATION] seconds, in a
single continuous shot.

Subject: [المقدّم أو اليدين].
Action: [خطوة واحدة واضحة — ابدأ، نفّذ، أنهِ].
Camera: [locked أو slow dolly in], no rotation.
Lighting: even, high-key, no harsh shadows, subject clearly visible.
Audio: clear [voiceover/ambience], no music under the explanation.

Use this image as the starting frame.
```
> **⚠️ تحذير:** الواجهات والنصوص داخل الفيديو تحدٍّ معروف. صوّر الواجهة الحقيقية وحرّكها، أو ابنِ النص في المونتاج.

---

## 6. عبارات إلزامية تُضاف دائمًا

### في كل برومبت صورة
```
anatomically correct hands with five fingers, natural joint articulation,
no extra limbs, no readable text, no logos
```

### في كل برومبت تحريك
```
In a single continuous shot, no scene cuts.          ← Omni فقط
Anatomically correct hands. Avoid jitter and bent limbs.
Preserve face, hair, costume, screen direction, and light direction.
```

### في كل تحرير حواري (Omni)
```
Keep everything else the same.
```

---

## 7. عبارات ممنوعة

| ممنوع | البديل |
|---|---|
| beautiful, stunning, amazing | وصف العدسة والإضاءة |
| cinematic (وحدها) | `shot on ARRI Alexa, 35mm anamorphic at f/2.8` |
| high quality | `2K resolution, sharp focus, natural texture` |
| emotional, sad, happy | وصف الجسد: `shoulders drop, gaze falls to the floor` |
| epic, dramatic | `low angle, 24mm wide, subject at 5% of frame` |
| fast | `2-second duration, rapid lateral camera truck, motion blur` |
| smooth | `slow 10-second dolly, no acceleration, fluid motion` |
| dark mood | `low-key lighting, single hard key, 80% of frame in shadow` |
| realistic | `natural skin texture with visible pores, no airbrushing` |
| don't move the camera | `camera completely static, locked-off frame` |
