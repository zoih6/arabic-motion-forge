# Transition Types — 12 نوع انتقال سينمائي

## الهدف

دليل مرجعي شامل لـ **12 نوع انتقال** يستخدمها `references/specs/transition-types.md`. كل نوع موثّق بـ: الوصف، الدلالة، متى يُستخدم، متى يُتجنب، وكيفية التنفيذ في Prompt Architecture.

---

## جدول المقارنة السريعة

| # | النوع | المدة | الدلالة | القوة | التكرار |
|---|---|---|---|---|---|
| 1 | Cut (قطع مباشر) | 0s | استمرار، حضور | ⭐⭐⭐⭐⭐ | 50%+ |
| 2 | Cross Dissolve | 0.5-2s | زمن، ذكرى | ⭐⭐⭐ | 10% |
| 3 | Fade to Black | 1-3s | نهاية، موت | ⭐⭐⭐ | 5% |
| 4 | Match Cut | 0s | ذكاء، ربط | ⭐⭐⭐⭐ | 10% |
| 5 | Whip Pan | 0.2-0.5s | سرعة، فوضى | ⭐⭐ | 5% |
| 6 | Morph | 1-3s | تحول | ⭐⭐⭐ | 5% |
| 7 | Zoom Transition | 1-2s | تعمق/انسحاب | ⭐⭐⭐ | 5% |
| 8 | Wipe | 0.5-1s | فصل زمني | ⭐⭐ | 3% |
| 9 | L-Cut / J-Cut | 0s | ربط ذهني | ⭐⭐⭐⭐ | 2% |
| 10 | Graphic Match | 0s | ربط مفاهيمي | ⭐⭐⭐⭐ | 3% |
| 11 | Sound Bridge | 0s | تداعي | ⭐⭐⭐⭐ | 1% |
| 12 | Hard Cut on Action | 0s | طاقة | ⭐⭐⭐⭐⭐ | متغير |

---

## 1. Cut (القطع المباشر)

### الوصف

انتقال فوري بدون أي مؤثر. المشهد الأول ينتهي، الثاني يبدأ فورًا.

### الدلالة السيمائية

- **استمرار** — لا انقطاع في الزمن
- **حضور** — العالم مستمر
- **صراحة** — لا تجميل
- **قوة** — المشاهد يبقى يقظًا
- **وثائقي** — أسلوب واقعي

### متى يُستخدم

✅ **استخدمه في:**

- الحركة المستمرة (شخصية تمشي، تتكلم)
- الحوار (بين شخصيات)
- الواقعية (مشهد وثائقي)
- الإيقاع السريع (إعلان، ريل)
- مشاهد التأسيس (establishing)
- مشاهد الرصد والمراقبة

### متى لا يُستخدم

❌ **تجنبه في:**

- تغير زمني كبير (سنة → أخرى)
- تغير مكان جذري (البيت → القمر)
- لحظة عاطفية هادئة (تأمل)
- بداية أو نهاية الفيلم (ما لم يكن أسلوب متعمد)

### التنفيذ في Prompt

```yaml
# prompt 1 (ينتهي)
final_prompt_suffix: |
  The shot holds for 1s on the final composition, 
  the character standing still, then the shot ends.

# prompt 2 (يبدأ)
opening_prompt_prefix: |
  The shot begins with the character in motion, 
  already in the middle of the action.
```

### التنفيذ في Assembly

- Premiere/DaVinci: ضع الـ clips متجاورين بدون transition
- Audio: crossfade قصير (5-10 frames) لتجنب click

---

## 2. Cross Dissolve (التلاشي المتبادل)

### الوصف

المشهد الأول يتلاشى تدريجيًا (opacity 100% → 0%) بينما الثاني يظهر (0% → 100%). يحدث في نفس الوقت.

### الدلالة السيمائية

- **زمن يمر** — الفترة بين المشهدين
- **تذكر** — داخل الذاكرة
- **حلم** — داخل اللاوعي
- **غموض** — انتقال ناعم
- **حنين** — لحظة تأمل
- **تخطي** — تم حذف وقت

### متى يُستخدم

✅ **استخدمه في:**

- تغيّر زمني (صباح → مساء، يوم → يوم آخر)
- داخل العقل (تذكر، كابوس، حلم)
- مونتاج (تخطي فترات)
- لحظات تأمل
- مشاعر هادئة
- مقدمات الأفلام

### متى لا يُستخدم

❌ **تجنبه في:**

- حركة سريعة (يُبطئ الإيقاع)
- إعلان منتج (يضعف CTA)
- مشهد حركة
- لحظة توتر عالية
- ريل (نادر)

### المدة المثالية

- سريع: 0.5s
- قياسي: 1s
- تأملي: 1.5-2s
- بطيء (نادر): 2-3s

### التنفيذ في Prompt

```yaml
final_prompt_suffix: |
  The image gradually fades out over 1 second, becoming
  completely transparent by the end. The last visible
  element is the steam from the cup.

next_prompt_prefix: |
  The image gradually fades in from transparency over 1
  second, starting completely transparent. The first
  visible element is the new environment.
```

### التنفيذ في Assembly

- Premiere: Cross Dissolve (1s)
- DaVinci: Cross Dissolve
- تأكد من 24fps minimum للنعومة

---

## 3. Fade to Black (تلاشي للأسود)

### الوصف

المشهد يتلاشى للأسود تمامًا. أو من الأسود يظهر المشهد التالي.

### الدلالة السيمائية

- **نهاية** — فصل انتهى
- **موت** — رمزي أو حقيقي
- **وقت مستقطع** — break
- **اكتمال** — مهمة انتهت
- **حداد** — لحظة حزينة
- **فاصل** — إعلاني

### متى يُستخدم

✅ **استخدمه في:**

- نهاية الفصل/المشهد
- نهاية الفيلم
- نهاية فاصل إعلاني
- لحظة موت
- انتقال بين قوسين زمنيين بعيدين
- التأكيد على نهاية حدث

### متى لا يُستخدم

❌ **تجنبه في:**

- وسط الفيلم (يوقف الإيقاع)
- إعلان قصير
- ريل (نادر)
- مشهد افتتاحي (إلا إذا كان أسلوب فني)

### المتغيرات

```yaml
fade_to_black:
  description: "تلاشي للأسود"
  when: "نهاية فصل، نهاية فيلم"

fade_to_white:
  description: "تلاشي للأبيض"
  when: "نقاء، انتقال روحاني، بداية جديدة"
  note: "نادر، أسلوب فني"

fade_to_color:
  description: "تلاشي للون معين (أحمر مثلًا)"
  when: "استثنائي، أسلوب فني"
  note: "نادر جدًا"

dip_to_black:
  description: "لحظة قصيرة من الأسود بين المشاهد"
  when: "فصل واضح، cut قاسي مع تأكد"
  note: "أقدم من fade، نادر اليوم"
```

### التنفيذ في Prompt

```yaml
final_prompt_suffix: |
  The image gradually fades to complete black over 2
  seconds, ending in total darkness. No light remains.

next_prompt_prefix: |
  The image begins in complete black, then gradually
  fades up over 1.5 seconds to reveal the new scene.
  The first element to become visible is the [X].
```

### التنفيذ في Assembly

- Premiere: Dip to Black (1-2s)
- DaVinci: Dip to Black
- الصوتي: fade out للصوت بنفس المدة

---

## 4. Match Cut (قطع بالتطابق)

### الوصف

عنصرين متشابهين (بصريًا، صوتيًا، أو في الحركة) يربطان مشهدين. القطع يحدث في لحظة التطابق.

### الدلالة السيمائية

- **ذكاء** — المشاهد يلاحظ
- **ربط مفاهيمي** — أكثر من مجرد انتقال
- **استمرارية** — العالم متصل
- **أناقة** — صناعة سينمائية
- **مفهوم** — ما يربط ليس الشكل فقط

### الأنواع الفرعية

#### 4.1 Action Match

```yaml
description: "حركة تكمل في اللقطة التالية"
example: |
  Shot 1: يد تصل لمقبض الباب (نهاية)
  Shot 2: يد على مقبض الباب (بداية، في مكان مختلف)
semantic: "نفس الفاعل، سياق مختلف، استمرارية"
```

#### 4.2 Graphic Match

```yaml
description: "شكل/نمط بصري يتكرر"
example: |
  Shot 1: شكل دائري (دوائر القهوة في فنجان)
  Shot 2: شكل دائري (دوائر في عيني الشخصية)
semantic: "ربط بصري، مفهوم مجرد"
```

#### 4.3 Sound Match

```yaml
description: "صوت يربط المشهدين"
example: |
  Shot 1: صوت أقدام في الداخل
  Shot 2: صوت أقدام في الخارج (نفس الإيقاع)
semantic: "ربط سمعي، انتقال"
```

#### 4.4 Position Match

```yaml
description: "الشخصية في نفس موقع الكادر"
example: |
  Shot 1: شخصية في وسط الكادر (تضع شيئًا)
  Shot 2: شخصية أخرى في وسط الكادر (تلتقط شيئًا)
semantic: "تماثل مكاني، علاقة"
```

#### 4.5 Color Match

```yaml
description: "اللون يربط"
example: |
  Shot 1: عنصر أحمر في الكادر
  Shot 2: عنصر أحمر آخر (سيارة، فستان، شيء)
semantic: "ربط لوني، عاطفي"
```

### متى يُستخدم

✅ **استخدمه في:**

- ربط مفاهيم
- مشاهد فنية (Brand Film)
- ربط مشهدين زمنيين/مكانيين
- إبراز الاستمرارية

### متى لا يُستخدم

❌ **تجنبه في:**

- مشهد وثائقي (يبدو مصطنعًا)
- مشاهد واقعية بحتة
- كل مكان (التكرار يضعف الأثر)

### التنفيذ في Prompt

```yaml
# shot 1: ينتهي بعنصر
final_prompt_suffix: |
  The character's hand reaches the doorknob, fingers
  curl around the brass handle, the shot holds for
  0.5s on this position.

# shot 2: يبدأ بنفس العنصر (في موقع مختلف)
opening_prompt_prefix: |
  The shot begins with a hand on a doorknob, fingers
  curled around the brass handle. The character pushes
  the door open and the new environment is revealed.
```

### التنفيذ في Assembly

- Cut مباشر (في لحظة التطابق)
- لضمان التطابق: استخدم الـ editing points بدقة

---

## 5. Whip Pan / Swish (المسح السريع)

### الوصف

حركة كاميرا أفقية سريعة جدًا (أو مقطع قصير جدًا ضبابي) من اليسار لليمين (أو العكس). يخفي القطع.

### الدلالة السيمائية

- **سرعة** — لا وقت للتوقف
- **فوضى** — العالم يتحرك بسرعة
- **طاقة** — نشاط عالٍ
- **مفاجأة** — انتقال مفاجئ
- **إعلان** — أسلوب إعلاني
- **كوميديا** — أحيانًا

### متى يُستخدم

✅ **استخدمه في:**

- إعلان طاقة
- مشهد حركة
- انتقال مفاجئ بين شخصيات
- بداية مفاجئة

### متى لا يُستخدم

❌ **تجنبه في:**

- لحظة عاطفية
- بداية الفيلم (التشويش يزعج)
- مشهد تأملي
- Brand Film هادئ

### التنفيذ في Prompt

```yaml
final_prompt_suffix: |
  At the end of the shot, the camera rapidly whips
  to the right with extreme motion blur, creating
  a streaking effect of light and color.

next_prompt_prefix: |
  The shot begins with motion blur resolving, the
  camera settling on a new composition in a new
  location. The first 0.3s has motion blur, then
  stabilizes on the new scene.
```

### المخاطر

- صعب التنفيذ في النماذج
- يحتاج 3-5 محاولات للنتيجة الجيدة
- قد يبدو غير احترافي إذا فشل

### Fallback

إذا فشل whip pan، استخدم **fast cut** مع صوت whoosh.

---

## 6. Morph (التحول التدريجي)

### الوصف

عنصر (شكل، لون، حجم) يتحول تدريجيًا لعنصر آخر. يحدث داخل اللقطة.

### الدلالة السيمائية

- **تحول** — في الشخصية أو العالم
- **اكتشاف** — ما كان خفيًا يظهر
- **إبداع** — أسلوب فني
- **ربط مفاهيمي** — القهوة = اليقظة مثلًا
- **إعلان منتج** — شكل يتحول لآخر

### متى يُستخدم

✅ **استخدمه في:**

- تحول المنتج (خام → نهائي)
- لحظة الكشف (مغلق → مفتوح)
- إعلانات فنية
- Brand Film إبداعي
- مشاهد الخيال

### متى لا يُستخدم

❌ **تجنبه في:**

- واقعية صارمة
- مشاهد درامية يومية
- وثائقي

### التنفيذ في Prompt

```yaml
morph_example:
  initial: "raw coffee beans"
  final: "brewed coffee in cup"
  duration: "2s"
  
  full_prompt: |
    Close-up of raw coffee beans. The beans begin
    to slowly transform — they crack, darken, and
    melt into dark liquid. Over 2 seconds, the
    transformation completes: where there were
    beans, there is now brewed coffee in a brass
    cup. The morph is smooth, organic, with
    no visible seam.
```

### المخاطر

- يتطلب نموذج قوي (Veo 3, Runway Gen-4)
- 3-5 محاولات عادةً
- قد يبدو غير طبيعي إذا فشل

### Fallback

إذا فشل morph:
- **Two shots with cross dissolve** (أبسط)
- **Post-production morph** (After Effects)

---

## 7. Zoom Transition (انتقال بالتكبير/التبعيد)

### الوصف

تكبير على عنصر حتى يملأ الكادر. اللقطة التالية تبدأ من نفس العنصر مكبّرًا، ثم تبتعد.

### الدلالة السيمائية

- **دخول** — إلى التفاصيل
- **تعمق** — في الموضوع
- **تركيز** — على عنصر واحد
- **انسحاب** — من التفاصيل
- **ربط** — من عام إلى خاص

### الأنواع الفرعية

#### 7.1 Zoom In Match (داخل)

```yaml
description: "تكبير في المشهد 1، اللقطة 2 تبدأ مكبّرة"
example: |
  Shot 1: WS للمقهى، الكاميرا تكبّر على حافة الكوب
  Shot 2: ECU لحافة الكوب، ثم تبتعد لتكشف الكوب ممتلئًا
semantic: "من عام إلى خاص، ثم ربط"
```

#### 7.2 Zoom Out Match (خارج)

```yaml
description: "تبعيد في المشهد 1، اللقطة 2 تبدأ بعيدة"
example: |
  Shot 1: CU على عين الشخصية، الكاميرا تبتعد
  Shot 2: WS يظهر الشخصية في موقع جديد
semantic: "من خاص إلى عام، تحول"
```

### التنفيذ في Prompt

```yaml
# shot 1
final_prompt_suffix: |
  The camera rapidly zooms into the brass dallah's
  lid over 1.5 seconds, the lid fills the entire
  frame at the end.

# shot 2
opening_prompt_prefix: |
  The shot begins with an extreme close-up of the
  brass dallah's lid. The camera then slowly zooms
  out over 1.5 seconds to reveal the full scene
  with the character holding the dallah.
```

### المدة

- 1-2s (سريع، مفعم بالطاقة)
- 2-3s (تأملي)

### المخاطر

- قد يبدو "infomercial" إذا أُسيء استخدامه
- يحتاج model يفهم الـ zoom بدقة

---

## 8. Wipe (المسح)

### الوصف

عنصر (خط، شكل) يمسح الكادر أفقيًا أو رأسيًا أو بشكل مخصص، ليكشف المشهد التالي.

### الدلالة السيمائية

- **فصل زمني** — انتقال واضح
- **احترافية** — أسلوب إعلاني/تلفزيوني
- **فصل فصول** — تغيير
- **إعلاني** — أسلوب كلاسيكي
- **بصري صريح** — لا تخفِ القطع

### الأنواع

```yaml
horizontal_wipe:
  description: "خط أفقي يمسح من اليسار لليمين (أو العكس)"
  when: "فصل فصول، تغيّر زمني"
  modern_use: "نادر، يبدو قديم"

vertical_wipe:
  description: "خط عمودي يمسح من الأعلى للأسفل"
  when: "نادر، أسلوب فني"

diagonal_wipe:
  description: "خط مائل"
  when: "إعلان، أسلوب فني"

circle_wipe:
  description: "دائرة تكبر أو تصغر"
  when: "كوميدي، قديم، انتقال ساخر"
  modern_use: "نادر جدًا (Star Wars أسلوب)"

shape_wipe:
  description: "شكل مخصص (نجمة، قلب، حرف)"
  when: "إعلان إبداعي، عيد، مناسبات"
```

### متى يُستخدم

✅ **استخدمه في:**

- فصل فصول
- تغيّر زمني واضح
- إعلان احترافي
- Brand Film (بعض الأساليب)

### متى لا يُستخدم

❌ **تجنبه في:**

- سينما حميمية
- مشاهد واقعية
- Brand Film هادئ
- الرومانسي

### التنفيذ

```yaml
# في المونتاج فقط (ليس في prompt)
# Premiere/DaVinci:
#   - Wipe (1s)
#   - Dip to White (0.5s) ثم Wipe
# لا يمكن توليده في video model بسهولة
```

---

## 9. L-Cut / J-Cut (قطع صوتي متقدم)

### الوصف

قطع صوتي متقدم حيث الصوت يبدأ قبل الصورة (J-Cut) أو يستمر بعدها (L-Cut).

### الدلالة السيمائية

#### J-Cut (الصوت قبل الصورة)

- **توقع** — ما الذي سيحدث؟
- **استمرار ذهني** — الرابط الذهني يبقى
- **انتقال سلس** — لا قطيعة
- **تشويق** — نسمع ما لا نراه بعد

#### L-Cut (الصوت بعد الصورة)

- **تأمل** — اللحظة تبقى
- **وداع** — ما يذهب لكن صوته يبقى
- **حنين** — صوت الماضي
- **وحدة** — الشخصية وحدها مع الصوت

### متى يُستخدم

✅ **استخدمه في:**

- J-Cut: انتقال بين مكانين (صوت الشخص الثاني يدخل قبل أن نراه)
- L-Cut: لحظة وداع، نهاية محادثة
- مشاهد تذكر (صوت الحاضر + صورة الماضي)
- مشاهد داخل العقل

### التنفيذ

```yaml
# J-Cut
audio_edit:
  - "صوت المشهد 2 يبدأ قبل القطع بـ 0.5-2s"
  - "ثم القطع للصورة الجديدة"

# L-Cut
audio_edit:
  - "صوت المشهد 1 يستمر بعد القطع بـ 0.5-2s"
  - "ثم يتلاشى تدريجيًا"
```

### التنفيذ

```yaml
# في المونتاج فقط
# Premiere: Audio track منفصل، مد/قص الصوت
# لا يمكن توليده في video model تلقائيًا
```

---

## 10. Graphic Match (التطابق الرسومي)

### الوصف

شكل، نمط، أو لون بصري يتكرر بين المشهدين. يختلف عن Match Cut بأنه يؤكد على **العلاقة البصرية** لا الحركة.

### الدلالة السيمائية

- **ربط مفاهيمي** — أكثر من مجرد تشابه
- **أناقة** — صناعة سينمائية
- **إيقاع** — يُنشئ نمطًا
- **هجاء** — أحيانًا (دلالي)

### الأنواع

```yaml
shape_repetition:
  description: "نفس الشكل في موقعين مختلفين"
  example: |
    Shot 1: دوائر القهوة في الفنجان
    Shot 2: دوائر في عيني الشخصية
  semantic: "القهوة = اليقظة"

color_repetition:
  description: "نفس اللون يربط"
  example: |
    Shot 1: عنصر أحمر
    Shot 2: عنصر أحمر آخر
  semantic: "ربط عاطفي"

pattern_repetition:
  description: "نفس النمط"
  example: |
    Shot 1: نقش على الحائط
    Shot 2: نقش على القميص
  semantic: "استمرارية بصرية"

texture_repetition:
  description: "نفس الملمس"
  example: |
    Shot 1: سطح خشبي
    Shot 2: سطح خشبي آخر
  semantic: "ربط حسّي"
```

### متى يُستخدم

✅ **استخدمه في:**

- Brand Film (إيقاع بصري)
- مشاهد فنية
- ربط مفاهيم

### متى لا يُستخدم

❌ **تجنبه في:**

- واقعية صارمة
- كل مشهد (التكرار يضعف)

---

## 11. Sound Bridge (الجسر الصوتي)

### الوصف

صوت يربط مشهدين مختلفين. قد يكون من المشهد 1 يمتد للمشهد 2، أو العكس.

### الدلالة السيمائية

- **تداعي** — صوت يستحضر صورة
- **حلم** — داخل اللاوعي
- **رابط ذهني** — الشخصية تفكر
- **انتقال زمني** — نفس الأصوات في زمنين

### متى يُستخدم

✅ **استخدمه في:**

- مشاهد تذكر
- تداعي الأفكار
- انتقال بين زمنين (نفس الموسيقى، صور مختلفة)
- داخل العقل

### التنفيذ

```yaml
# في المونتاج (لا يمكن توليده في النموذج)
audio_track:
  - track: "MUSIC-01"
    edit:
      - "يبدأ في المشهد 1، يستمر خلال القطع"
      - "يستمر في المشهد 2 (مع صورة جديدة)"
  
  - track: "AMBIENCE-01"
    edit:
      - "يتلاشى من المشهد 1"
      - "يبدأ AMBIENCE-02 (outdoor) في المشهد 2"
      - "التداخل الصوتي يربط"
```

---

## 12. Hard Cut on Action (قطع على الفعل)

### الوصف

قطع في **ذروة الحركة**، حيث الفعل في أعلاه. يخفي القطع.

### الدلالة السيمائية

- **طاقة** — لا توقف
- **ديناميكية** — العالم في حركة
- **خفية** — القطع غير ملحوظ
- **احترافية** — صناعة كلاسيكية

### متى يُستخدم

✅ **استخدمه في:**

- إعلان
- مشهد حركة
- مشهد أكشن
- إخفاء حدود

### متى لا يُستخدم

❌ **تجنبه في:**

- مشاهد هادئة جدًا
- بداية الفعل (يجب أن تكون في الذروة)

### التنفيذ في Prompt

```yaml
# shot 1: يصل لذروة الحركة في النهاية
final_prompt_suffix: |
  The character's hand is mid-swing, the cup is
  mid-air, the action is at its peak. Hold for
  0.3s on this peak position.

# shot 2: يبدأ في نفس الذروة
opening_prompt_prefix: |
  The shot begins at the peak of the action: the
  cup is mid-air, mid-swing. The action then
  completes in this new shot.
```

---

## مصفوفة الاختيار السريع

### حسب نوع المحتوى

| المحتوى | الانتقالات المُفضَّلة |
|---|---|
| إعلان طاقة | whip, hard cut, morph, zoom |
| قصة عاطفية | dissolve, fade, L-cut |
| إعلان منتج | match cut, hard cut, graphic |
| Brand Film | fade, match cut, dissolve |
| موشن جرافيك | wipe, morph, graphic |
| وثائقي | hard cut, L-cut |
| فيديو موسيقي | whip, hard cut, graphic |
| تعليمي/شرح | hard cut, dissolve, graphic |

### حسب الإيقاع

| الإيقاع | الانتقالات |
|---|---|
| سريع (3s/shot) | hard cut, whip, zoom |
| متوسط (5-8s) | hard cut, match, graphic |
| بطيء (10s+) | dissolve, fade, L-cut |
| تأملي | dissolve, fade, sound bridge |

### حسب الوظيفة السردية

| الوظيفة | الانتقالات |
|---|---|
| استمرارية | hard cut, match, action |
| تذكر/حلم | dissolve, morph |
| تغير زمني كبير | fade, dissolve, wipe |
| انتقال مفاجئ | whip, smash cut |
| نهاية | fade, dissolve |
| تحوّل | morph, graphic |

---

## Common Mistakes

### ❌ 1. Whip Pan في سياق عاطفي

```yaml
problem: "whip pan في مشهد وداع"
fix: "استخدم L-cut أو dissolve"
```

### ❌ 2. Dissolve في إعلان طاقة

```yaml
problem: "dissolve في كل مشهد"
fix: "استخدم hard cut أو whip، الـ dissolve يبطئ"
```

### ❌ 3. Fade to Black وسط الفيلم

```yaml
problem: "fade to black بين كل مشهدين"
fix: "احتفظ به للنهايات فقط، استخدم hard cut"
```

### ❌ 4. Match Cut للتأثير فقط

```yaml
problem: "match cut لا يخدم القصة"
fix: "إذا لم يكن له معنى، استخدم hard cut"
```

### ❌ 5. Wipe في Brand Film هادئ

```yaml
problem: "wipe يكسر النبرة"
fix: "استخدم dissolve أو hard cut"
```

---

## Advanced: Multi-Model Strategy

```yaml
multi_model_transition:
  
  strategy_A_pure_video:
    models: "video model فقط"
    when: "hard cut, slow dissolve, simple fade"
    pros: "بسيط"
    cons: "محدود"
  
  strategy_B_video_plus_image:
    models: "image model + video model"
    when: "match cut, morph, zoom"
    pros: "تحكم أكثر"
    cons: "خطوتين"
  
  strategy_C_post_production:
    models: "video model + compositing"
    when: "wipe, color match, complex transitions"
    pros: "100% تحكم"
    cons: "يحتاج خبرة بعد الإنتاج"
  
  strategy_D_audio_focused:
    models: "video model + audio editing"
    when: "J-cut, L-cut, sound bridge"
    pros: "ربط ذهني قوي"
    cons: "لا يمكن توليده تلقائيًا"
```

---

## Decision Tree

```yaml
transition_decision:
  
  q1_is_there_time_jump:
    if_yes:
      - "small jump (same day): dissolve"
      - "large jump (different era): fade to black + title"
    if_no:
      go_to_q2
  
  q2_is_there_place_jump:
    if_yes:
      - "nearby (interior → exterior): graphic match, dissolve"
      - "far (continent): fade, title card"
    if_no:
      go_to_q3
  
  q3_what_emotional_shift:
    - "continuation: hard cut, action match"
    - "tension rise: whip, smash cut"
    - "calm → tense: hard cut on action"
    - "tense → calm: dissolve"
    - "sadness: slow dissolve, fade"
    - "joy: whip, zoom out"
  
  q4_what_genre:
    - "documentary: hard cut, L-cut"
    - "drama: dissolve, L-cut"
    - "thriller: hard cut on action"
    - "music video: whip, hard cut, graphic"
    - "advertising: whip, morph, zoom"
  
  q5_complexity:
    if_high:
      consider_post_production: true
    if_low:
      do_in_video_prompt: true
```

---

## ملخص القاعدة الذهبية

> **الانتقال ليس ديكورًا. الانتقال يحمل معنى.**

- Cut المباشر = قسوة، حضور، قوة
- Match cut = ذكاء، ربط، أناقة
- Dissolve = حنين، زمن، تأمل
- Fade = نهاية، اكتمال
- Whip = طاقة، سرعة
- Morph = تحوّل، اكتشاف
- L/J-Cut = ربط ذهني

اختر بناءً على **ما تريد أن يشعر به المشاهد**، لا بناءً على ما يبدو جميلاً.
