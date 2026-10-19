# 02 — Image Prompts Package (حزمة برومبتات الصور)

## الهدف

**الملف الثاني من حزمة الإنتاج الخماسية.** يحوي **كل prompt صورة** جاهز للتوليد، مع المراجع، معايير القبول، ومحاولات التوليد.

> **يُنتَج من قبل:** `30-executive-producer` (مع `22-prompt-architecture`).

---

## كيف تستخدمه

1. املأ كل prompt عند M8
2. مرّر كل prompt عبر `19-preflight-check` ثم `31-quality-gate` (G4)
3. سجّل محاولات التوليد في `generated_assets`
4. اختر النسخة المعتمدة

---

## القالب الكامل

```markdown
# Image Prompts Package — [اسم المشروع]

**التاريخ:** [ISO]
**الحالة:** [DRAFT / APPROVED_FOR_GENERATION / GENERATED / APPROVED]
**عدد الـ Prompts:** [N]
**النماذج المستهدفة:** [bytedance/seedream-4, midjourney-v6, ...]

---

## 0. Generation Strategy

```yaml
strategy:
  primary_model: "..."
  fallback_models: ["..."]
  aspect_ratio: "16:9 / 9:16 / 1:1"
  resolution: "..."
  quality_settings: "high / ultra / max"
  expected_attempts_per_prompt: 3
  selection_criteria: "أفضل تطابق مع prompt + Identity match + Color match"
  
  generation_order:
    1: "Character Anchors (IMG-CHAR-01..N)"
    2: "Wardrobe Anchors"
    3: "Location Anchors"
    4: "Prop Anchors"
    5: "Frame Anchors (لحظات حرجة)"
    6: "Main Scene Prompts"
```

---

## 1. Anchor Prompts (المراجع)

### IMG-CHAR-01 — SAMI-01 (الشخصية الرئيسية)

```yaml
prompt_id: "IMG-CHAR-01"
type: "character_anchor"
purpose: "تثبيت مظهر الشخصية الرئيسي"

identity_string: |
  A 32-year-old Yemeni man, square jaw with defined cheekbones,
  dark brown eyes with subtle wrinkles at the corners,
  short curly black hair with a single gray streak at the front,
  a short trimmed beard with a distinctive gray patch on the left
  cheek, a faded burn scar on the back of the right hand,
  warm wheat-toned skin with light freckles across the nose

composition:
  shot_size: "CU (Close-Up, head and shoulders)"
  angle: "eye_level"
  background: "neutral soft out-of-focus"
  expression: "subtle fatigue, eyes slightly hooded, calm"

lighting:
  key: "soft window light from left, 4500K"
  fill: "subtle reflector on right"
  contrast: "low (3:1)"
  style: "natural, soft, intimate"

camera:
  lens: "85mm portrait"
  aperture: "f/1.8"
  dof: "very shallow (background bokeh)"

style:
  realism: "photorealistic"
  color_palette: "warm neutrals, no saturation"
  film_stock: "Kodak Portra 400 (warm skin tones)"
  references: "Steve McCurry portraiture, National Geographic"

reference_outputs:
  total: 5
  selected_index: 1  # يُحدّث بعد التوليد

model:
  primary: "midjourney-v6 / bytedance/seedream-4"
  fallback: "stability/sdxl"

acceptance_criteria:
  - "نفس الوجه عبر كل المحاولات"
  - "البقعة الرمادية على الخد ظاهرة"
  - "ندبة المحروق ظاهرة (إذا اليد مرئية)"
  - "تعبيرات طبيعية"
  - "إضاءة دافئة موحدة"
  
rejection_criteria:
  - "تغير ملامح الوجه"
  - "اختفاء البقعة الرمادية"
  - "تغير لون البشرة"
  - "إضاءة قاسية"

generated_assets:
  - path: "assets/anchors/sami-01_v1.png"
    attempt: 1
    status: "rejected"
    reason: "الملامح أنثوية قليلًا"
  - path: "assets/anchors/sami-01_v2.png"
    attempt: 2
    status: "approved"
    notes: "مثالي، ملامح واضحة، البقعة ظاهرة"
```

### IMG-WARD-01 — SAMI-01's Wardrobe

```yaml
prompt_id: "IMG-WARD-01"
type: "wardrobe_anchor"
purpose: "تثبيت الملابس عبر الفيلم"

clothing_description: |
  Charcoal gray linen apron tied at the back over a faded
  off-white cotton shirt with sleeves rolled to the forearms,
  brown leather vintage watch on left wrist (weathered),
  no other accessories

composition:
  shot_size: "MS (Medium, waist up)"
  focus: "on clothing details"
  background: "neutral"

style:
  realism: "photorealistic"
  texture_focus: "linen weave, cotton softness, leather wear"
  lighting: "soft, even (to show texture)"
```

### IMG-LOC-01 — Sanaani Coffee House (interior)

```yaml
prompt_id: "IMG-LOC-01"
type: "location_anchor"
purpose: "تثبيت مكان التصوير"

location_description: |
  Interior of a traditional Yemeni coffee house (qahwa),
  dark wooden ceiling beams with hand-carved geometric
  patterns, weathered stone walls, traditional patterned
  tile floor. A single brass dallah (coffee pot) sits on
  hot coals in the central hearth. A high window admits
  soft pre-dawn light. A wooden counter runs along one
  side, with a shelf of small brass cups in the background.
  Dust motes suspended in the light. A single traditional
  oil lamp hangs from the ceiling.

composition:
  shot_size: "WS (Wide)"
  angle: "low chest-height, looking slightly up"
  aspect: "preserve depth, 3 layers visible"

lighting:
  key: "high window 5600K cool + brass lamp 2400K warm"
  contrast: "high (6:1)"
  atmosphere: "dusty, contemplative"

style:
  realism: "photorealistic"
  reference: "old Sanaani architecture, before dawn"
```

### IMG-PROP-01 — Brass Dallah

```yaml
prompt_id: "IMG-PROP-01"
type: "prop_anchor"
purpose: "تثبيت مظهر الركوة النحاسية"

prop_description: |
  A traditional Yemeni brass coffee pot (dallah), 
  round bulbous base, long graceful neck, curved handle
  on the side, pointed conical lid. Polished brass
  with warm golden color, slight patina on the base.
  Approximately 30cm tall. Reflects warm light.

composition:
  shot_size: "MS"
  angle: "slightly low, hero shot"
  background: "blurred dark"

style:
  realism: "photorealistic"
  lighting: "warm directional (show brass reflection)"
  detail_focus: "high (sharp details of carving, patina)"
```

### IMG-FRAME-001..N — Frame Anchors (إطارات مرجعية)

```yaml
- prompt_id: "IMG-FRAME-001"
  type: "frame_anchor"
  purpose: "إطار مرجعي لبداية SC01_SH01 (بداية الفيلم)"
  description: |
    Wide shot of empty Sanaani coffee house interior,
    pre-dawn, dust in window light, brass lamp hanging,
    dallah on coals steaming. The composition establishes
    the world before the character enters.
  
- prompt_id: "IMG-FRAME-XXX"
  type: "frame_anchor"
  purpose: "..."
  description: "..."
```

---

## 2. Main Scene Prompts (لقطات المشاهد)

### IMG-SC01-SH01

```yaml
prompt_id: "IMG-SC01-SH01"
shot_id: "SC01_SH01"
type: "main_scene"
purpose: "اللقطة الافتتاحية: تأسيس العالم"

identity_strings:
  character: "N/A (no character in this frame)"
  wardrobe: "N/A"
  prop: "brass_dallah (from IMG-PROP-01)"
  location: "sanaani_coffee_house (from IMG-LOC-01)"

full_prompt_10_layers: |
  Cinematic film still, single frame, establishing shot.
  
  A. INTENT: Establishing shot. Anchors the audience in the
  world before introducing the character. Sets tone, place,
  time. No character present.
  
  B. SUBJECT: Empty traditional Sanaani coffee house
  interior. The space itself is the subject. A single brass
  dallah sits on the hot coals in the central hearth,
  beginning to steam.
  
  C. ENVIRONMENT: Old Sanaani coffee house (qahwa), before
  dawn prayer, winter. Dark wooden ceiling beams with
  hand-carved geometric patterns overhead. Weathered stone
  walls. Traditional patterned tile floor (partially visible).
  A single high window admits the first hint of pre-dawn
  light (cool blue, 8000K). Dust motes suspended in the
  air. The brass fitting of the dallah catches the window
  light. No modern elements whatsoever.
  
  D. COMPOSITION: Wide shot, low camera angle (chest height).
  Foreground: edge of a dark wooden counter running from
  bottom-left to center-right. Midground: the empty space
  where the barista will appear in the next shot. Background:
  the dallah on coals, with the window above it as the
  brightest element in the frame. Negative space: 70% of
  frame is architecture and atmosphere, establishing
  emptiness before the character arrives. Leading lines:
  the wooden beams converge toward the window, drawing the
  eye there. Visual hierarchy: window light → dallah →
  counter edge. Three depth layers: foreground counter,
  midground floor, background hearth with dallah and window.
  
  E. CAMERA: Wide shot (WS), camera height at chest level
  of an imagined standing person. Lens: 24mm wide angle
  (Panavision C-series anamorphic equivalent). Depth of
  field: deep, foreground to background in focus. Sensor:
  ARRI Alexa 35 simulation. Film stock: Kodak Vision3 500T
  simulation.
  
  F. LIGHTING: Practical only. Key light: the single high
  window behind the dallah, camera-back direction, cool
  blue 8000K, soft quality. Fill: minimal — the coals
  provide a faint warm glow (1800K) on the underside of
  the dallah. Rim: window light on the brass fitting.
  Practical lights in frame: window + coal glow. Contrast
  ratio: 6:1 (window bright, foreground in deep shadow).
  Atmosphere: visible dust motes in the window light,
  faint steam from the dallah.
  
  G. MOTION: N/A (still image)
  
  H. CONTINUITY: This is the opening frame. No inheritance.
  Exit state: empty room with dallah steaming. Next shot
  will introduce the character from the left.
  
  I. STYLE: Genre: contemplative drama. Visual movement:
  realistic cinematic. Realism level: photorealistic.
  Color palette: cool blue dominant (pre-dawn), warm amber
  secondary (coals), deep brown tertiary (wood). Forbidden:
  any saturated red, any modern fixture, any logos, any
  anachronism. Texture: 35mm film grain subtle, halation
  subtle on window light. Color grade: cool shadows, warm
  highlights, gentle S-curve. Reference works: Blade Runner
  2049 (color), Roma (natural light), Yomeddine (daily
  moments). Reference DP: Emmanuel Lubezki (natural light
  philosophy).
  
  J. CONSTRAINTS: Identity lock: N/A (no character).
  Wardrobe: N/A. Prop lock: traditional brass dallah
  (specific shape — see IMG-PROP-01). Location lock: this
  Sanaani coffee house is the only location for the entire
  film. Hands: N/A. Extra limbs: N/A. Modern fixtures:
  FORBIDDEN (no electrical lighting, no appliances, no
  plastic, no modern signage). Readable text: NONE in this
  frame. No other characters.

model:
  primary: "bytedance/seedream-4"
  fallback: "midjourney-v6"
  aspect_ratio: "16:9"
  resolution: "1920x1080"
  quality: "high"

reference_images:
  - path: "assets/anchors/loc-01_v2.png"
    role: "location_anchor"
    weight: "high"
  - path: "assets/anchors/prop-01_v1.png"
    role: "prop_anchor"
    weight: "medium"

acceptance_criteria:
  - "الركوة ظاهرة في الخلفية"
  - "النوافذ العالية هي مصدر الضوء الرئيسي"
  - "إضاءة pre-dawn باردة"
  - "الأسطح المعمارية واضحة (خشب، حجر، بلاط)"
  - "لا أجهزة حديثة"
  - "dust motes مرئية"
  - "بخار خفيف من الركوة"
  - "تكوين 3 طبقات (FG / MG / BG)"
  - "negative space 70%"

rejection_criteria:
  - "شخصية في الكادر"
  - "إضاءة دافئة ساطعة (يجب أن تكون pre-dawn)"
  - "أجهزة كهربائية ظاهرة"
  - "نص أو شعارات"
  - "مساحة فارغة بدون تفاصيل معمارية"

expected_attempts: 3

fallback_strategy:
  if_3_attempts_fail:
    - "غيّر prompt: زِد specificity في layer D"
    - "جرّب النموذج البديل"
    - "إذا فشل كل شيء: ابدأ من prompt أبسط وأضف تدريجيًا"

generated_assets:
  - path: "assets/main/sc01_sh01_v1.png"
    attempt: 1
    status: "rejected"
    reason: "الإضاءة دافئة جدًا، ليست pre-dawn"
  - path: "assets/main/sc01_sh01_v2.png"
    attempt: 2
    status: "approved"
    notes: "تطابق ممتاز، الإضاءة صحيحة، التكوين 3 طبقات"
```

### IMG-SC01-SH02

```yaml
prompt_id: "IMG-SC01-SH02"
shot_id: "SC01_SH02"
type: "main_scene"
purpose: "دخول الشخصية"

identity_strings:
  character: "[من IMG-CHAR-01]"
  wardrobe: "[من IMG-WARD-01]"
  prop: "brass_dallah"
  location: "sanaani_coffee_house"

full_prompt_10_layers: |
  [Prompt كامل بـ 10 طبقات A-J]
  
  A. INTENT: Character entrance. The protagonist appears in
  the world established in IMG-SC01-SH01. The audience
  should immediately read fatigue and routine.
  
  B. SUBJECT: [Identity String من IMG-CHAR-01]
  - 32-year-old Yemeni man
  - square jaw, defined cheekbones
  - dark brown eyes, hooded
  - short curly black hair with single gray streak at front
  - short trimmed beard with gray patch on LEFT cheek
  - faded burn scar on back of right hand
  - warm wheat-toned skin, light freckles on nose
  - expression: tired, eyes slightly closed, calm
  - pose: standing at the counter, hands on edge
  - gaze: down at the brass dallah on the coals
  
  C. ENVIRONMENT: [Location من IMG-LOC-01]
  Same Sanaani coffee house, before dawn. The character
  is now visible, standing at the wooden counter. The
  dallah is in the background, steaming.
  
  D. COMPOSITION: Medium shot, slightly low angle. The
  character is in the right third of the frame, looking
  down at the dallah in the background-left. Foreground:
  the brass cup he will fill. Midground: the character.
  Background: dallah on coals. The composition echoes
  the previous frame but with character.
  
  E. CAMERA: 35mm lens, f/2.0, shallow DOF focused on
  the character's face, background slightly soft.
  
  F. LIGHTING: Same as IMG-SC01-SH01 — pre-dawn window
  light from the back-left, warm oil lamp glow from
  below (1800K), minimal fill.
  
  G. MOTION: N/A (still image)
  
  H. CONTINUITY: Inherits all from IMG-SC01-SH01 (same
  location, lighting, time). Exit state: character at
  counter, looking at dallah. Next shot will continue
  the action (SC01_SH03: he picks up the cup).
  
  I. STYLE: [نفس grammar المشروع]
  
  J. CONSTRAINTS:
  - Identity lock: EXACT match to IMG-CHAR-01
  - Wardrobe lock: charcoal apron, off-white shirt
  - Watch on left wrist (weathered brown leather)
  - Prop lock: brass dallah (from IMG-PROP-01)
  - Hands: 5 fingers each, correct anatomy
  - No extra limbs
  - No modern elements
  - No text in frame

model:
  primary: "bytedance/seedream-4"
  fallback: "midjourney-v6"
  aspect_ratio: "16:9"

reference_images:
  - path: "assets/anchors/char-01_v2.png"
    role: "character_anchor"
    weight: "high"
  - path: "assets/anchors/ward-01_v1.png"
    role: "wardrobe_anchor"
    weight: "high"
  - path: "assets/anchors/loc-01_v2.png"
    role: "location_anchor"
    weight: "high"

acceptance_criteria: [...]
rejection_criteria: [...]

expected_attempts: 3
fallback_strategy: "..."

generated_assets: []
```

### IMG-SC01-SH03, SC01-SH04, ... (باقي اللقطات)

[نفس النمط لكل لقطة]

---

## 3. Inventory (جرد الـ Prompts)

```yaml
inventory:
  anchors:
    - IMG-CHAR-01 (character)
    - IMG-CHAR-02 (character B, if any)
    - IMG-WARD-01 (wardrobe)
    - IMG-PROP-01..N (props)
    - IMG-LOC-01 (location)
    - IMG-FRAME-001..N (frame anchors)
  
  main_scenes:
    SC01:
      - IMG-SC01-SH01
      - IMG-SC01-SH02
      - ...
    SC02:
      - IMG-SC02-SH01
      - ...
    ...
  
  total_prompts: N
  expected_total_assets: 3x  # 3 attempts per prompt average
  total_disk_estimate: "..."
```

---

## 4. Generation Workflow

```yaml
workflow:
  step_1_generate_anchors:
    duration_minutes: 30-60
    description: "ولّد كل الـ Anchors (Character, Wardrobe, Location, Props)"
    output: "5-15 approved anchor images"
  
  step_2_select_best_anchors:
    duration_minutes: 15
    description: "اختر أفضل صورة من كل anchor (3 attempts each)"
    criteria: "Identity match + Style match + Technical quality"
  
  step_3_generate_main_scenes:
    duration_minutes: 60-120
    description: "ولّد كل الـ main scenes بالترتيب"
    notes: "ابدأ بالمشاهد الأولى (SC01) لتأكيد الـ continuity"
  
  step_4_review_continuity:
    duration_minutes: 30
    description: "افحص تطابق الشخصية/المكان بين كل اللقطات"
    action: "إذا تطابق ضعيف → أعد التوليد بـ anchors أقوى"
  
  step_5_final_selection:
    duration_minutes: 15
    description: "اختر النسخة النهائية لكل لقطة"
  
  step_6_export:
    duration_minutes: 10
    description: "صدّر بصيغ متعددة (PNG max quality + JPG web)"
```

---

## Cross-References

- **Production Blueprint:** `schemas/production-blueprint.md`
- **Continuity Bible:** `schemas/state/continuity-bible.md`
- **Frame Chain:** `schemas/state/frame-chain.md`
- **Asset Registry:** `schemas/state/asset-registry.md`
- **Motion Prompts:** `schemas/motion-prompts-package.md` (تستخدم هذه الصور كـ input)
- **Assembly Guide:** `schemas/assembly-guide.md`
```

---

## معايير الجودة

- ✅ كل prompt يحوي 10 طبقات A-J
- ✅ Identity String منسوخ حرفيًا
- ✅ Reference Images مذكورة
- ✅ Acceptance + Rejection Criteria واضحة
- ✅ Model + Aspect Ratio محدد
- ✅ Fallback Strategy موجودة
- ✅ Generated Assets مُسجَّلة

---

## ما لا تفعله

- ❌ لا prompt بدون 10 طبقات
- ❌ لا تترك Acceptance Criteria فارغة
- ❌ لا تنسَ Reference Images
- ❌ لا تنسَ تسجيل محاولات التوليد
- ❌ لا تسلّم بدون Final Selection لكل prompt
