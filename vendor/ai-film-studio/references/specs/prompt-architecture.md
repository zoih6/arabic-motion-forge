# Prompt Architecture Specification — A-J Layers

## الهدف

توثيق تفصيلي لـ **10 طبقات A-J** التي يبني عليها `workflows/M7a-prompt-architecture.md` كل prompt. هذا الـ reference هو **القاموس المرجعي** لأي prompt يُكتب في المنظومة.

---

## نظرة عامة

كل prompt في منظومة AI Film Studio يجب أن يمر عبر **10 طبقات معمارية** A-J. كل طبقة تخدم قرارًا مختلفًا ولا يمكن إغفالها.

```
A — Intent         → لماذا هذا المشهد؟
B — Subject        → من/ما الموضوع؟
C — Environment    → أين ومتى؟
D — Composition    → كيف يُبنى الكادر؟
E — Camera         → بمَ نرى؟
F — Lighting       → كيف يُضاء؟
G — Motion         → ما الذي يتحرك؟ (video)
H — Continuity     → كيف يرتبط بما قبله/بعده؟
I — Style & DNA    → ما اللغة البصرية؟
J — Constraints    → ما الذي يجب الحفاظ عليه؟
```

---

## A — Intent (الهدف)

**الأسئلة التي تجيب عنها:**
- لماذا هذا المشهد موجود في الفيلم؟
- ما الـ beat السردي؟
- ما الذي يجب أن يشعر به المشاهد؟
- في أي نسبة زمنية من الفيلم نحن؟

**Schema:**

```yaml
A_intent:
  scene_purpose: "[السبب الوجودي للمشهد]"
  narrative_beat: "[كشف/قرار/تحول/إيفاء/خطاف/تصعيد/خاتمة]"
  visual_goal: "[ما الذي يجب أن يراه المشاهد]"
  emotional_target: "[المشاعر المستهدفة في هذه اللحظة]"
  time_position: "[نسبة 0-100% من الفيلم]"
  importance: "[high / medium / low]"
```

**أمثلة على narrative_beats:**

- **Hook (الخطاف):** جذب الانتباه في أول 3 ثوانٍ
- **Setup (التأسيس):** بناء العالم والشخصية
- **Inciting Incident (الحدث المحفّز):** ما يغيّر التوازن
- **Rising Action (تصعيد):** تصاعد التوتر
- **Climax (الذروة):** لحظة المواجهة أو الكشف
- **Falling Action (إنزال):** بعد الذروة
- **Resolution (الحل):** العالم الجديد
- **Twist (الانعطافة):** ما يقلب التوقعات
- **Reveal (الكشف):** ما كان مخفيًا
- **CTA:** Call to Action

**مثال كامل:**

```yaml
A_intent:
  scene_purpose: "تأسيس الشخصية والوضع المتعب"
  narrative_beat: "Setup"
  visual_goal: "رؤية رجل صنعاني يستيقظ متعبًا، عيون مغمضة جزئيًا"
  emotional_target: "تعب، هدوء، رتابة"
  time_position: "0-13% (أول مشهد)"
  importance: "high"
```

---

## B — Subject (الموضوع)

**الأسئلة:**
- من/ما هو العنصر الرئيسي؟
- ما هويته البصرية (Identity String)؟
- ما ملابسه؟
- ما الدعائم؟
- ما الوضعية/الفعل؟

**Schema:**

```yaml
B_subject:
  type: "[شخص / منتج / مكان / مجرّد / حيوان]"
  character_id: "[IDENTITY من Continuity Bible]"
  identity_string: "[يُلصق حرفيًا، لا يُعاد صياغه]"
  
  # للملابس
  wardrobe:
    items:
      - name: "..."
        color: "..."
        material: "..."
        condition: "..."
        fit: "..."
        position: "..."
  
  # للدعائم
  props:
    - id: "..."
      name: "..."
      state: "..."
      position: "..."
  
  # للوضعية والفعل
  pose:
    body: "[وضعية الجسم]"
    direction: "[اتجاه]"
    weight: "[كيف يوزع الوزن]"
  gesture:
    hands: "[وضعية اليدين]"
    arms: "[وضعية الذراعين]"
    face: "[تعبير الوجه]"
  expression:
    eyes: "[حالة العيون]"
    mouth: "[حالة الفم]"
    brows: "[حالة الحاجبين]"
  gaze:
    direction: "[أين ينظر]"
    focus: "[قريب/متوسط/بعيد]"
```

**قاعدة Identity String:**

> الـ Identity String يجب أن يُلصق **حرفيًا** من Continuity Bible. لا تُعد صياغته. لا تختصره. لا تنسَ البصمات البصرية (النُدب، البقع، الشامات).

**مثال:**

```yaml
B_subject:
  type: "person"
  character_id: "SAMI-01"
  identity_string: |
    A 32-year-old Yemeni man, square jaw with defined
    cheekbones, dark brown eyes with subtle wrinkles
    at the corners, short curly black hair with a single
    gray streak at the front, a short trimmed beard
    with a distinctive gray patch on the left cheek,
    a faded burn scar on the back of the right hand,
    warm wheat-toned skin with light freckles across
    the nose
  wardrobe:
    items:
      - name: "مئزر"
        color: "رمادي فحمي (charcoal gray)"
        material: "كتان ثقيل"
        condition: "متآكل الأطراف، لا مزق"
        fit: "فضفاض، مربوط من الخلف"
      - name: "قميص"
        color: "أبيض باهت (off-white)"
        material: "قطن خفيف"
        condition: "مكوي خفيف، مكشوف من طرف الكم"
        fit: "مريح"
      - name: "ساعة"
        color: "بني جلد"
        material: "جلد طبيعي"
        condition: "متآكل، باهت"
        position: "اليد اليسرى"
  props:
    - id: "brass_dallah"
      name: "ركوة نحاسية صنعانية"
      state: "على الجمر، بخار خفيف يتصاعد"
      position: "الوسط، على الموقد"
  pose:
    body: "انحناء قليل للأمام، ثقل الجسم على الرجل الخلفية"
    direction: "نحو الكاميرا قليلًا"
  gesture:
    hands: "اليد اليمنى على حافة الطاولة، اليسرى في الجيب"
    face: "حاجبان مرفوعان قليلًا"
  expression:
    eyes: "مفتوحة ببطء، ثقيلة الجفون"
    mouth: "مغلق، مستقيم"
  gaze:
    direction: "نحو البخار المتصاعد من الركوة"
    focus: "متوسط"
```

---

## C — Environment (البيئة)

**الأسئلة:**
- أين نحن (location)؟
- متى (time of day)؟
- ما الطقس؟
- ما المواد المحيطة؟
- ما الإضاءة الطبيعية؟

**Schema:**

```yaml
C_environment:
  location:
    name: "[اسم المكان]"
    type: "[interior / exterior]"
    architecture: "[تفاصيل]"
    surfaces: "[المواد]"
    elements: "[العناصر الثابتة]"
  
  time:
    time_of_day: "[الساعة + الفترة]"
    season: "[الفصل]"
    weather: "[حالة الطقس]"
    natural_light_direction: "[اتجاه]"
  
  atmosphere:
    - "[غبار، بخار، دخان، حشرات، رياح]"
  
  depth:
    foreground: "[...]"
    midground: "[...]"
    background: "[...]"
  
  practical_lights:
    - "[مصادر إضاءة حقيقية في المشهد]"
```

**مثال:**

```yaml
C_environment:
  location:
    name: "مقهى صنعاني تقليدي"
    type: "interior"
    architecture: "سقف خشبي داكن مع نحت هندسي، جدران حجرية متآكلة، أرض من البلاط التقليدي"
    surfaces: "خشب متشرب بالقهوة، حجر رطب، بلاط متآكل، نحاس مصقول جزئيًا"
    elements: "موقد الفحم في الوسط، رف أكواب خشبي، طاولة دائرية، باب خلفي"
  time:
    time_of_day: "قبل الفجر (~5:00 AM)"
    season: "شتاء"
    weather: "لا رياح، نوافذ مغلقة، برودة خفيفة"
    natural_light_direction: "من نافذة عالية في الجدار البعيد"
  atmosphere:
    - "غبار يطفو في شعاع الضوء"
    - "بخار خفيف من الركوة"
    - "لا رياح (نوافذ مغلقة)"
  depth:
    foreground: "حافة كوب قهوة فارغ"
    midground: "طاولة + شخصية"
    background: "رف الأكواب + الباب الخلفي"
  practical_lights:
    - "مصباح نفطي يتدلى من السقف"
    - "جمر تحت الركوة"
```

---

## D — Composition (التكوين)

**الأسئلة:**
- ما نوع اللقطة؟
- أين الموضوع في الكادر؟
- ما العناصر الإضافية (FG/BG)؟
- ما الخطوط الرئيسية؟
- ما الفراغ السلبي؟

**Schema:**

```yaml
D_composition:
  framing:
    shot_type: "[نوع اللقطة]"
    camera_position: "[...]"
  
  subject_placement:
    position: "[right_third / center / left_third / top / bottom]"
    rule_of_thirds: "[true / false + reason]"
  
  visual_layers:
    foreground: "[عنصر أمامي + وظيفته]"
    midground: "[الموضوع]"
    background: "[عنصر خلفي + وظيفته]"
  
  lines_and_shapes:
    leading_lines: "[خطوط تقود العين]"
    shapes: "[مربعات، دوائر، مثلثات]"
    symmetry: "[نوع التماثل]"
  
  negative_space:
    amount: "[نسبة 0-100%]"
    location: "[أين]"
    purpose: "[لماذا]"
  
  visual_hierarchy:
    primary: "[أين العين أولًا]"
    secondary: "[ثم]"
    tertiary: "[ثم]"
  
  framing_device: "[إطار داخل إطار؟]"
```

**أمثلة على shot_type:**

- **EWS (Extreme Wide Shot):** المشهد ككل، الشخصية صغيرة جدًا
- **WS (Wide Shot):** الشخصية في بيئتها
- **MWS (Medium Wide):** من الركبة فصاعدًا
- **MS (Medium Shot):** من الخصر فصاعدًا
- **MCU (Medium Close-Up):** من الصدر فصاعدًا
- **CU (Close-Up):** الرأس والكتفين
- **ECU (Extreme Close-Up):** العين، اليد، تفصيل
- **OTS (Over-the-Shoulder):** من فوق كتف شخصية
- **POV (Point of View):** من عيني الشخصية
- **Two-Shot:** شخصيتان في الكادر
- **Insert:** تفصيل حرج (ساعة، رسالة، منتج)
- **Cutaway:** قطع لشيء آخر (للتوضيح)

**مثال:**

```yaml
D_composition:
  framing:
    shot_type: "Medium Close-Up (MCU)"
    camera_position: "مستوى الصدر، زاوية مستقيمة"
  
  subject_placement:
    position: "right_third"
    rule_of_thirds: "true — العينان على نقطة تقاطع علوية-يمنى"
  
  visual_layers:
    foreground: "حافة كوب قهوة فارغ خارج التركيز (يسار-أسفل)"
    midground: "الشخصية SAMI-01 (وسط-يمين)"
    background: "رف أكواب نحاسية خارج التركيز (يمين-وسط)"
  
  lines_and_shapes:
    leading_lines: "حافة الطاولة تقود من أسفل-يسار إلى الشخصية"
    shapes: "دوائر (الفناجين، الأطباق) + مستطيلات (الأرفف)"
    symmetry: "غير متماثل — الشخصية على اليمين، فراغ على اليسار"
  
  negative_space:
    amount: "30%"
    location: "الثلث الأيسر العلوي"
    purpose: "يستقبل عين المشاهد قبل الشخصية، يوازن التكوين"
  
  visual_hierarchy:
    primary: "العينان (داخل الشخصية)"
    secondary: "اليد اليمنى مع الركوة"
    tertiary: "البخار المتصاعد"
  
  framing_device: "no (لا إطار داخل إطار)"
```

---

## E — Camera (الكاميرا)

**Schema:**

```yaml
E_camera:
  shot_size: "[EWS / WS / MWS / MS / MCU / CU / ECU / Insert / POV / OTS]"
  camera_angle: "[eye_level / low / high / dutch / bird_eye / worm_eye]"
  camera_height: "[نفس مستوى الشخصية / أقل / أعلى]"
  
  lens:
    focal_length: "[14mm / 24mm / 35mm / 50mm / 85mm / 100mm / 200mm]"
    character: "[normal / anamorphic / macro / tilt-shift / vintage]"
  
  aperture: "[f/1.2 - f/16]"
  depth_of_field: "[very_shallow / shallow / medium / deep / infinite]"
  
  focus:
    type: "[fixed / pull / rack / follow]"
    target: "[الشخصية / العنصر / ...]"
  
  sensor_format: "[S35 / Full Frame / Medium Format / 16mm / 8mm]"
  film_stock: "[Kodak Vision3 500T / Portra 400 / Tri-X / clean digital]"
  
  frame_rate: "[24 / 25 / 30 / 60 / 120]"
  shutter: "[normal 180° / slow / fast]"
```

**مثال:**

```yaml
E_camera:
  shot_size: "MCU (Medium Close-Up)"
  camera_angle: "eye_level"
  camera_height: "نفس مستوى العينين"
  
  lens:
    focal_length: "85mm (portrait lens)"
    character: "spherical, clean, modern"
  
  aperture: "f/1.8"
  depth_of_field: "shallow — face sharp, background soft bokeh"
  
  focus:
    type: "fixed"
    target: "العينان (always)"
  
  sensor_format: "Full Frame (ARRI Alexa 35 simulation)"
  film_stock: "Kodak Vision3 500T (warm balance, subtle grain)"
  
  frame_rate: "24 fps (cinematic)"
  shutter: "180° (normal)"
```

---

## F — Lighting (الإضاءة)

**Schema:**

```yaml
F_lighting:
  scheme: "[natural_only / studio / hybrid / practical_only / neon / candles]"
  
  key_light:
    source: "[sun / window / lamp / screen / practical]"
    direction: "[angle from camera: left / right / front / back]"
    height: "[eye / high / low]"
    quality: "[hard / soft / diffused]"
    intensity: "[low / medium / high]"
    color_temp: "[K]"
  
  fill_light:
    source: "[reflector / ambient / practical / none]"
    intensity: "[ratio of key: 50% / 30% / 0%]"
    direction: "[opposite of key]"
    color_temp: "[K]"
  
  rim_light:
    source: "[practical / off-camera / natural]"
    direction: "[behind subject, left or right]"
    purpose: "[separate from background]"
    color_temp: "[K]"
  
  practical_lights:
    - type: "[lamp / candle / screen / fire]"
      position: "[in scene]"
      color_temp: "[K]"
      intensity: "[visible / decorative]"
  
  contrast_ratio: "[low 2:1 / medium 4:1 / high 8:1 / very_high 16:1]"
  shadows: "[depth + direction + color]"
  atmosphere: "[haze / dust / smoke / steam]"
  temp_mix: "[monochromatic / warm_dominant_with_cool_rim / etc.]"
```

**قاعدة الإضاءة الثلاثية:**

- **Key:** الضوء الرئيسي (يحدد شكل الموضوع)
- **Fill:** الضوء المُكمِّل (يخفف الظلال)
- **Rim:** الضوء الفاصل (يفصل عن الخلفية)

**مثال:**

```yaml
F_lighting:
  scheme: "practical_only (إضاءة عملية فقط، واقعية)"
  
  key_light:
    source: "مصباح نفطي يتدلى من السقف"
    direction: "يسار الكاميرا، 45°"
    height: "فوق مستوى العين"
    quality: "soft (diffused through glass)"
    intensity: "medium"
    color_temp: "2400K (دافئ جدًا)"
  
  fill_light:
    source: "ambient room (no specific fill)"
    intensity: "0% (لا fill صريح)"
    direction: "natural"
    color_temp: "match ambient"
  
  rim_light:
    source: "window light (back)"
    direction: "خلف الشخصية، يسار"
    purpose: "فصل الشخصية عن رف الأكواب"
    color_temp: "5600K (بارد)"
  
  practical_lights:
    - type: "مصباح نفطي"
      position: "السقف، يسار الكاميرا"
      color_temp: "2400K"
      intensity: "visible in frame (key)"
    - type: "جمر تحت الركوة"
      position: "الموقد، وسط الكادر"
      color_temp: "1800K"
      intensity: "decorative + subtle fill from below"
  
  contrast_ratio: "4:1 (face lit, half in shadow)"
  shadows: "عميقة على الجانب الأيمن من الوجه، ناعمة"
  atmosphere: "غبار يطفو في شعاع المصباح، بخار من الركوة"
  temp_mix: "warm_dominant_with_cool_rim (2400K dominant, 5600K rim)"
```

---

## G — Motion (الحركة) — للفيديو فقط

**Schema:**

```yaml
G_motion:
  character_motion:
    primary_action: "[فعل واحد محدد]"
    direction: "[from → to]"
    amount: "[distance / magnitude / duration]"
    endpoint: "[وضعية نهائية]"
    weight: "[خفيف / متوسط / ثقيل]"
    speed: "[بطيء / متوسط / سريع]"
  
  secondary_motion:
    - element: "[hair / cloth / steam / dust / leaves]"
      behavior: "[يتأثر بـ...]"
  
  camera_motion:
    type: "[static / pan / tilt / dolly / truck / track / arc / crane / handheld / dolly_zoom]"
    direction: "[in / out / left / right / up / down / no_motion]"
    speed: "[بطيء (1cm/s) / متوسط (3cm/s) / سريع (10cm/s)]"
    acceleration: "[constant / accelerating / decelerating]"
    start_state: "[وضعية البداية]"
    end_state: "[وضعية النهاية]"
  
  timing:
    beats:
      - "[0-3s]: ..."
      - "[3-7s]: ..."
      - "[7-10s]: ..."
    total_duration: "[Xs]"
  
  physics:
    weight_response: "[light / medium / heavy]"
    gravity_response: "[free_fall / resistance / float]"
    environmental_response: "[cloth responds to wind, etc.]"
  
  facial_motion: "[تعبيرات وجه أثناء الفعل]"
  lip_sync: "[yes / no / with dialogue reference]"
```

**أنواع حركات الكاميرا (الرئيسية):**

| الحركة | الوصف | متى |
|---|---|---|
| Static | ثابتة تمامًا | تأسيس، مراقبة |
| Pan | دوران أفقي | كشف، متابعة |
| Tilt | دوران رأسي | حجم، علو |
| Dolly In | اقتراب من الموضوع | عاطفة، كشف |
| Dolly Out | ابتعاد | نهاية، وحدة |
| Truck | موازاة أفقية | مواكبة |
| Track | متابعة | حركة مستمرة |
| Arc | دوران حول الموضوع | أهمية |
| Crane Up | ارتفاع | تأسيس، نهاية |
| Crane Down | نزول | كشف، انتقال |
| Handheld | يدوية (اهتزاز خفيف) | وثائقي، واقعية |
| Dolly-Zoom (Hitchcock) | تكبير + تحريك | انهيار نفسي |

**مثال:**

```yaml
G_motion:
  character_motion:
    primary_action: "يمسك الركوة بيده اليمنى، يرفعها ببطء، يصب في الكوب، يعيدها"
    direction: "من الموقد إلى الكوب"
    amount: "3 ثوانٍ للرفع، 4 ثوانٍ للسكب، 3 ثوانٍ للإعادة"
    endpoint: "الركوة تعود للنار، الكوب ممتلئ، اليد اليمنى قرب الكوب"
    weight: "medium (الركوة ثقيلة نسبيًا)"
    speed: "بطيء (كل الحركة محسوبة)"
  
  secondary_motion:
    - element: "بخار الركوة"
      behavior: "يتصاعد أثناء الرفع، يقل عند العودة"
    - element: "مئزر الشخصية"
      behavior: "يتحرك قليلًا مع رفع الذراع (fabric physics)"
    - element: "غبار"
      behavior: "يطفو ببطء في شعاع الضوء (لا يتأثر كثيرًا)"
  
  camera_motion:
    type: "static (no motion)"
    direction: "no_motion"
    speed: "0"
    acceleration: "constant"
    start_state: "MCU, eye level, fixed lens"
    end_state: "نفس التكوين"
  
  timing:
    beats:
      - "0-3s: اليد اليمنى تصل للركوة، تمسك المقبض"
      - "3-6s: ترفع الركوة ببطء نحو الكوب"
      - "6-10s: تصب في الكوب، تيار القهوة واضح"
      - "10-13s: تعيد الركوة للنار، اليد تبتعد"
    total_duration: "13s"
  
  physics:
    weight_response: "medium (الركوة لها وزن محسوس)"
    gravity_response: "تيار القهوة ينزل بشكل طبيعي"
    environmental_response: "المئزر يتحرك مع الذراع"
  
  facial_motion: "الحاجبان مرفوعان قليلًا (تركيز)، الفم مغلق"
  lip_sync: "no (لا حوار)"
```

---

## H — Cinematic Continuity (الاستمرارية)

**Schema:**

```yaml
H_continuity:
  inherited_from_previous:
    lighting: "[نفس أم تطور؟]"
    wardrobe: "[نفس أم تطور؟]"
    props: "[نفس أم تطور؟]"
    color_grading: "[نفس]"
    camera_grammar: "[نفس]"
    character_position: "[نفس أم انتقل؟]"
  
  exit_state:
    character_position: "[أين ينتهي]"
    character_expression: "[التعبير النهائي]"
    character_gesture: "[وضعية الجسم]"
    environment_state: "[حالة البيئة]"
    frame_composition: "[تكوين الإطار]"
    lighting_state: "[حالة الإضاءة]"
  
  entry_state_for_next:
    note: "[ما يجب أن يبدأ به المشهد التالي]"
  
  axis_180: "[ثابت / مكسور عمدًا]"
  screen_direction: "[ثابت]"
  eyeline_match: "[محفوظ]"
  
  continuity_notes: "[ملاحظات خاصة]"
  chain_breaks: "[إن وُجدت، مع الأسباب]"
```

**مثال:**

```yaml
H_continuity:
  inherited_from_previous:
    lighting: "نفس (pre-dawn, 2400K + 5600K rim)"
    wardrobe: "نفس (المئزر، القميص، الساعة)"
    props: "الركوة في نفس الموقع"
    color_grading: "نفس (cool shadows, warm highlights)"
    camera_grammar: "نفس (35mm-85mm range, eye level)"
    character_position: "انتقل من الموقد إلى الطاولة"
  
  exit_state:
    character_position: "جالس، ظهر للكاميرا، يداه على ركبتيه"
    character_expression: "عيون مغمضة، تأمل"
    character_gesture: "ثابت، لا حركة"
    environment_state: "نفس (إضاءة pre-dawn)"
    frame_composition: "WS من الخلف، الشخصية في الوسط"
    lighting_state: "نفس"
  
  entry_state_for_next:
    note: |
      المشهد التالي (SC04) يجب أن يبدأ بـ:
      - نفس التكوين (WS من الخلف) لمدة 2s (hold)
      - ثم ينتقل ببطء إلى MCU من الجانب
      - أو: cut مباشر (المونتير يقرر)
  
  axis_180: "ثابت (الشخصية دائمًا تواجه الكاميرا من نفس الجانب)"
  screen_direction: "ثابت (right-to-left motion across screen)"
  eyeline_match: "محفوظ"
  
  continuity_notes: |
    - البخار يستمر (نفس الموقع، نفس المصدر)
    - الغبار يستمر (نفس مصدر الضوء)
    - الإضاءة لم تتغير (الوقت يتقدم ببطء)
  
  chain_breaks: "none"
```

---

## I — Style & Visual DNA (الأسلوب)

**Schema:**

```yaml
I_style:
  genre: "[درامي / وثائقي / تجريبي / تجريدي / كوميدي / رعب / رومانسي / حركة]"
  visual_movement: "[واقعي سينمائي / أسلوبي / تجريدي / أنيميشن / معاصر]"
  realism_level: "[فوتوغرافي واقعي / فوتوريالستيك / أسلوبي مبالغ / كرتوني]"
  
  color_palette:
    dominant: ["color + hex"]
    secondary: ["color + hex"]
    accent: ["color + hex"]
    forbidden: ["color names"]
  
  texture:
    grain: "[35mm / 16mm / digital clean / no grain / halation]"
    halation: "[yes / no / subtle / strong]"
    lens_character: "[anamorphic flare / spherical clean / vintage]"
  
  color_grade:
    shadows: "[teal / cool / warm / neutral / desaturated]"
    midtones: "[natural / pushed / desaturated]"
    highlights: "[warm / cool / blown / soft]"
    s_curve: "[subtle / strong / flat / film print]"
    saturation: "[natural / desaturated / oversaturated]"
  
  reference_films: ["فيلم 1", "فيلم 2"]
  reference_ads: ["إعلان 1"]
  reference_dps: ["اسم مدير تصوير"]
  reference_artists: ["اسم فنان"]
```

**مثال:**

```yaml
I_style:
  genre: "درامي حميمي (intimate drama)"
  visual_movement: "واقعي سينمائي (cinematic realism)"
  realism_level: "فوتوغرافي واقعي (photorealistic)"
  
  color_palette:
    dominant: 
      - name: "primary_brown"
        hex: "#3B2F2F"
        usage: "الخشب، الظلال الأساسية"
      - name: "warm_amber"
        hex: "#C9A66B"
        usage: "الإضاءة، النحاس"
    secondary:
      - name: "deep_teal"
        hex: "#2F4F4F"
        usage: "الظلال الباردة، الخلفية"
      - name: "off_white"
        hex: "#F5F0E1"
        usage: "القماش، الإضاءة الناعمة"
    accent:
      - name: "charcoal"
        hex: "#36454F"
        usage: "المئزر"
    forbidden:
      - "أحمر مشبع"
      - "أصفر فلوري"
      - "أزرق نيون"
      - "أسود خالص"
  
  texture:
    grain: "35mm film grain subtle"
    halation: "subtle on window light"
    lens_character: "anamorphic subtle on horizontal flares"
  
  color_grade:
    shadows: "cool_teal"
    midtones: "natural"
    highlights: "warm_amber"
    s_curve: "gentle film print curve"
    saturation: "natural, slightly muted"
  
  reference_films:
    - "Blade Runner 2049 (color palette)"
    - "Roma (natural light)"
    - "Yomeddine (daily moments)"
  
  reference_dps:
    - "Emmanuel Lubezki (natural light philosophy)"
  
  reference_artists: []
```

---

## J — Constraints (القيود)

**Schema:**

```yaml
J_constraints:
  identity_lock:
    character_id: "SAMI-01"
    locked_fields:
      - "facial_features: square jaw, defined cheekbones"
      - "beard: gray patch on LEFT cheek"
      - "scar: burn scar on back of RIGHT hand"
      - "eyes: dark brown, hooded"
      - "hair: curly black with single gray streak at front"
  
  wardrobe_lock:
    - "charcoal_apron"
    - "off_white_shirt"
    - "weathered_brown_leather_watch (left wrist)"
  
  prop_lock:
    - "brass_dallah (from IMG-PROP-01)"
    - "brass_cup (from IMG-PROP-02)"
  
  location_lock:
    - "sanaani_coffee_house (from IMG-LOC-01)"
  
  text_preservation:
    - text: "النص هنا"
      exact: "yes"
      position: "..."
      size: "..."
      font: "..."
  
  product_lock:
    - "the product: shape, color, logo"
  
  brand_lock:
    - "the brand: official logo, exact"
  
  hands_anatomy:
    - "5 fingers each"
    - "no extra fingers"
    - "no missing fingers"
    - "correct joint angles"
  
  extra_limbs_forbidden: true
  
  mirror_reversal:
    - "no (unless intentional)"
  
  lighting_consistency:
    - "match previous shot's lighting"
  
  negative_prompts:
    - "no anachronism"
    - "no modern fixtures"
    - "no extra limbs"
    - "no extra heads"
    - "no text other than locked_text"
    - "no logos other than brand_lock"
    - "no distortion of identity"
  
  specific_exclusions:
    - "no readable text beyond the exact text listed"
    - "no logos other than the character's wardrobe"
    - "no modern electrical fixtures"
    - "no mobile phones or modern devices"
```

**مثال:**

```yaml
J_constraints:
  identity_lock:
    character_id: "SAMI-01"
    locked_fields:
      - "square_jaw_with_defined_cheekbones"
      - "short_trimmed_beard_with_gray_patch_on_LEFT_cheek"
      - "burn_scar_on_back_of_RIGHT_hand"
      - "dark_brown_eyes_with_subtle_wrinkles_at_corners"
      - "short_curly_black_hair_with_single_gray_streak_at_front"
      - "warm_wheat_toned_skin_with_light_freckles_across_nose"
  
  wardrobe_lock:
    - "charcoal_gray_linen_apron_tied_at_back (no tears, worn edges only)"
    - "faded_off_white_cotton_shirt (sleeves rolled to forearms)"
    - "weathered_brown_leather_watch_on_LEFT_wrist"
    - "no_other_accessories"
  
  prop_lock:
    - "brass_dallah (specific shape, see IMG-PROP-01)"
    - "brass_cup (small, 5cm, see IMG-PROP-02)"
    - "no_other_dallah_visible"
  
  location_lock:
    - "sanaani_coffee_house (only location for entire film)"
    - "no_modern_elements"
    - "no_appliances"
    - "no_plastic"
  
  text_preservation:
    - "no_text_in_this_frame (SC01_SH01 is purely visual)"
  
  product_lock: "N/A (no product in this shot)"
  brand_lock: "N/A (no brand in this shot)"
  
  hands_anatomy:
    - "5_fingers_per_hand"
    - "no_extra_fingers"
    - "no_missing_fingers"
    - "correct_joint_angles"
    - "burn_scar_visible_on_right_hand_back"
  
  extra_limbs_forbidden: true
  mirror_reversal: "no"
  lighting_consistency: "must_match_SC01_sh01 (pre-dawn window light + oil lamp)"
  
  negative_prompts:
    - "no anachronism (no modern items, no cars, no phones)"
    - "no modern electrical fixtures"
    - "no plastic items"
    - "no extra limbs or extra heads"
    - "no text or logos"
    - "no distortion of character's face"
    - "no missing beard or scar"
  
  specific_exclusions:
    - "no readable text (frame is text-free)"
    - "no logos (frame is logo-free)"
    - "no modern signage or branding"
    - "no electrical appliances"
    - "no plastic"
```

---

## ملخص أولويات الطبقات

| الطبقة | الأولوية | السبب |
|---|---|---|
| A — Intent | حرج | بدونه لا معنى للمشهد |
| B — Subject | حرج | يحدد ما يصنع المحتوى |
| C — Environment | حرج | يحدد السياق |
| D — Composition | عالي | يؤثر على القراءة البصرية |
| E — Camera | عالي | يؤثر على الإحساس |
| F — Lighting | عالي | يؤثر على الجو |
| G — Motion | حرج (للفيديو) | يحدد الفعل |
| H — Continuity | حرج | يضمن الاتساق |
| I — Style | عالي | يحدد اللغة |
| J — Constraints | حرج | يحمي من الأخطاء |

---

## القواعد الذهبية

1. **لا prompt بدون 10 طبقات** — حتى لو لقطة بسيطة
2. **Identity String حرفي** — لا تُعد صياغته
3. **Continuity Bible مرجع** — لا تُضف شخصية/مكان بدون تسجيل
4. **الطول مقبول** — 60-200 كلمة طبيعي، 300+ عند الحاجة
5. **لا انتزاع** — لا تأخذ كلمات من prompt آخر
6. **لا تكرار** — لا تكرر في Prompt ما هو واضح في الـ reference image
7. **بالإنجليزية** — في prompts النموذج، الطبقات الـ 10 دائمًا بالإنجليزية

---

## مثال كامل مُجمَّع (للصورة)

```text
Cinematic film still, single frame, master composition.

A. INTENT: Establishing shot. Anchors the audience in the world
before introducing the character. Sets tone, place, time. The
space itself is the subject — no character present.

B. SUBJECT: Empty traditional Sanaani coffee house interior.
The space is the subject. A single brass dallah sits on hot
coals in the central hearth, beginning to steam. No character.

C. ENVIRONMENT: Old Sanaani coffee house, before dawn prayer,
winter. Dark wooden ceiling beams with hand-carved geometric
patterns overhead. Weathered stone walls. Traditional patterned
tile floor. A single high window admits the first hint of
pre-dawn light (cool blue, 8000K). Dust motes suspended in the
air. The brass fitting of the dallah catches the window light.
No modern elements whatsoever.

D. COMPOSITION: Wide shot, low camera angle (chest height).
Foreground: edge of a dark wooden counter running from
bottom-left to center-right. Midground: the empty space where
the barista will appear. Background: the dallah on coals, with
the window above it as the brightest element. Negative space:
70% of frame is architecture and atmosphere, establishing
emptiness. Leading lines: the wooden beams converge toward the
window. Visual hierarchy: window light → dallah → counter edge.
Three depth layers: foreground counter, midground floor,
background hearth with dallah and window.

E. CAMERA: Wide shot (WS), camera height at chest level. Lens:
24mm wide angle (Panavision C-series anamorphic equivalent).
Depth of field: deep, foreground to background in focus.
Sensor: ARRI Alexa 35 simulation. Film stock: Kodak Vision3
500T simulation.

F. LIGHTING: Practical only. Key: single high window behind
dallah, camera-back direction, cool blue 8000K, soft quality.
Fill: minimal — coals provide faint warm glow (1800K) on
underside of dallah. Rim: window light on brass fitting.
Practical: window + coal glow. Contrast: 6:1 (window bright,
foreground in deep shadow). Atmosphere: visible dust motes,
faint steam.

I. STYLE: Genre: contemplative drama. Visual movement:
realistic cinematic. Color palette: cool blue dominant, warm
amber secondary, deep brown tertiary. Forbidden: saturated
red, modern fixtures, logos, anachronism. Texture: 35mm film
grain subtle, halation subtle. Color grade: cool shadows, warm
highlights, gentle S-curve. Reference: Blade Runner 2049 (color),
Roma (natural light), Yomeddine (daily moments). Reference DP:
Emmanuel Lubezki.

J. CONSTRAINTS: Identity: N/A. Wardrobe: N/A. Prop: traditional
brass dallah (specific shape — see IMG-PROP-01). Location:
sanaani_coffee_house (only location for entire film). Hands: N/A.
Extra limbs: forbidden. Modern fixtures: FORBIDDEN. Readable
text: NONE in this frame. No other characters.
```

---

## مثال كامل مُجمَّع (للفيديو)

[نفس النمط + إضافة G. Motion و H. Continuity]
