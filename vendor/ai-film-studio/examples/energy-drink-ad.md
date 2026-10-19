# مثال v2.0 — "طاقة الفجر" (إعلان منتج طاقة، 30 ثانية)

> **هذا المثال يوضح المنظومة الكاملة v2.0 في مشروع واقعي.**
> **كل ملف من الـ 5 يُنتَج كما لو كنا ننفذ فعلًا، مع كل المخرجات الموثّقة.**

---

## ملخص المشروع

```yaml
project:
  id: "PROJ-ENERGY-01"
  title: "طاقة الفجر"
  type: "advertising"
  sub_type: "product_launch"
  duration: "30s"
  format: "9:16 (TikTok/Reels) + 16:9 (YouTube)"
  language: "ar"
  dialect: "خليجي/فصحى مبسطة"
  platform:
    primary: "TikTok"
    secondary: ["Instagram Reels", "YouTube Shorts"]
  target_audience: "شباب 18-30، مهتمون باللياقة والإنتاجية"
  product: "قرص طاقة جديد (NOOR ENERGY)"
  brand: "NOOR"
```

---

## 1. Production Blueprint (مختصر)

### Concept

```yaml
concept:
  logline: "شخص متعب في منتصف الليل يكتشف قرص طاقة، يأكله، فينقلب عالمه من السكون إلى الحركة"
  one_liner: "في لحظة، يتحول الظلام إلى فجر"
  core_message: "الطاقة قرار، وليست وقت"
  visual_metaphor: "القرص = شمس صغيرة تنبض في داخله"
  genre: "تحفيزي، تجريبي"
  tone: "هادئ ثم مفعم بالطاقة"
  pace: "بطيء (15s) → سريع (10s) → ذروة (5s)"
  
  inspiration:
    ads: ["Apple 'Crush' (تحويل)", "Nike 'Dream Crazy' (تحفيزي)"]
    films: ["Blade Runner 2049 (color)", "Everything Everywhere All at Once (تحول)"]
  
  why_this_works:
    - "استعارة بصرية فريدة (قرص = شمس)"
    - "تحول حقيقي في الشخصية"
    - "CTA قوي: 'NOOR. فعّل فجرك'"
```

### Story Structure

```yaml
story_structure:
  type: "Hook-Body-Payoff"
  
  story_spine:
    - beat: 1
      time: "0-3s"
      description: "شخصية مستلقية على سرير، عين على المنبه (3:00 AM)"
    - beat: 2
      time: "3-7s"
      description: "تنهض، تذهب للمطبخ، تبحث في الدرج"
    - beat: 3
      time: "7-12s"
      description: "تجد علبة NOOR، تخرج القرص، تدقق فيه"
    - beat: 4
      time: "12-18s"
      description: "تأكله، يحدث تحول بطيء (القرص ينبض في داخلها)"
    - beat: 5
      time: "18-25s"
      description: "تتحرك، تخرج، العالم يتحول من حولها"
    - beat: 6
      time: "25-30s"
      description: "تنظر للشمس المشرقة، ابتسامة، شعار NOOR"
  
  emotional_map:
    - time: "0%"
      emotion: "إرهاق، يأس"
      intensity: 7
    - time: "30%"
      emotion: "فضول"
      intensity: 5
    - time: "50%"
      emotion: "تردد ثم قرار"
      intensity: 6
    - time: "70%"
      emotion: "تحوّل"
      intensity: 8
    - time: "90%"
      emotion: "طاقة، يقظة"
      intensity: 9
    - time: "100%"
      emotion: "ثقة، فخر"
      intensity: 9
```

### Scenes

```yaml
scenes:
  - id: "SC01"
    title: "الاستيقاظ المتعب"
    duration: "5s"
    purpose: "تأسيس الحالة المتعبة"
    location: "غرفة نوم بسيطة"
    characters: ["OMAR-01"]
    time: "3:00 AM"
    key_beats:
      - "0-2s: عين على المنبه (يظهر 3:00 AM)"
      - "2-4s: الشخصية تنهض ببطء"
      - "4-5s: تمشي نحو الباب"
    transition_out: "match_cut (يد الباب → يد الدرج)"
  
  - id: "SC02"
    title: "البحث في المطبخ"
    duration: "5s"
    purpose: "البحث عن حل"
    location: "مطبخ بسيط"
    key_beats:
      - "0-2s: تفتح الدرج، تبحث"
      - "2-4s: تجد علبة NOOR"
      - "4-5s: ترفع العلبة، تنظر لها"
    transition_out: "match_cut (يد ترفع العلبة → يد تخرج القرص)"
  
  - id: "SC03"
    title: "اكتشاف القرص"
    duration: "5s"
    purpose: "عرض المنتج"
    location: "المطبخ"
    key_beats:
      - "0-2s: تفتح العلبة، تخرج القرص (CU)"
      - "2-4s: تدقق فيه، القرص ينبض بطاقة"
      - "4-5s: تضعه في فمها"
    transition_out: "morph (القرص في الفم → تحوّل)"
  
  - id: "SC04"
    title: "التحوّل"
    duration: "5s"
    purpose: "لحظة التحوّل"
    location: "المطبخ (إضاءة تتغير)"
    key_beats:
      - "0-2s: الشخصية تتوقف، تتنفس (القرص يعمل)"
      - "2-4s: الإضاءة تتحول من cool إلى warm، لون البشرة يصير أكثر إشراقًا"
      - "4-5s: تفتح عينيها بحدة، تنظر حولها"
    transition_out: "whip_pan (نحو الباب)"
  
  - id: "SC05"
    title: "الخروج"
    duration: "5s"
    purpose: "العالم يعكس التحوّل"
    location: "شارع + شروق الشمس"
    key_beats:
      - "0-2s: تفتح الباب (نفس اليد، نفس التكوين)"
      - "2-4s: تخرج، المدينة تستقبلها"
      - "4-5s: تبدأ بالركض"
    transition_out: "cut مباشر (للختام)"
  
  - id: "SC06"
    title: "الشمس والختام"
    duration: "5s"
    purpose: "الشعار + الإقفال"
    location: "سطح أو منظر مفتوح"
    key_beats:
      - "0-3s: الشخصية تنظر للشمس المشرقة، ابتسامة"
      - "3-5s: الشعار يظهر (NOOR + CTA)"
    transition_out: "fade to black"
```

### Script

```yaml
script:
  total_words: 22
  total_duration: "30s"
  
  voiceover:
    - id: "VO-01"
      scene: "SC01"
      timestamp: "0-3s"
      text: "الساعة ثلاثة. والجسد يقول: لا."
      direction: "هادئ، يائس، هامس"
    
    - id: "VO-02"
      scene: "SC04"
      timestamp: "0-3s"
      text: "قررت. فُعّلت."
      direction: "قوي، حاسم، واثق"
    
    - id: "VO-03"
      scene: "SC06"
      timestamp: "0-3s"
      text: "NOOR. فعّل فجرك."
      direction: "حماسي، نظيف، brand voice"
  
  on_screen_text:
    - id: "OST-01"
      scene: "SC06"
      timestamp: "3-5s"
      text: "NOOR"
      execution_strategy: "post_overlay"
    
    - id: "OST-02"
      scene: "SC06"
      timestamp: "3-5s"
      text: "فعّل فجرك"
      execution_strategy: "post_overlay"
```

### Color Script

```yaml
color_script:
  "SC01": "cool_blue + dim_warm (تعب)"
  "SC02": "cool_blue + neutral (بحث)"
  "SC03": "cool_blue → warm_amber (القرص يدخل الدفء)"
  "SC04": "warm_amber burst (التحول)"
  "SC05": "warm_gold + orange (الشروق)"
  "SC06": "warm_gold + brand_orange (الذروة)"
```

---

## 2. Continuity Bible (مختصر)

```yaml
identity:
  - id: "OMAR-01"
    name: "Omar"
    age: 27
    ethnicity: "خليجي"
    role: "protagonist"
    
    visual_signature: |
      Short black hair, slight stubble, dark brown eyes
      with tired under-eye circles, defined jawline,
      light olive skin (Fitzpatrick III)
    
    anatomy:
      face: "Defined jawline, slight under-eye circles (fatigue), dark brown eyes"
      body: "175cm, lean athletic build, visible muscle definition"
      skin: "Light olive, slight tan"
      hair: "Short black, slightly messy"
    
    forbidden_inconsistencies:
      - "Under-eye circles must fade by SC04 (transformation)"
      - "Skin tone becomes more vibrant by SC04"
      - "Eye expression shifts from tired to alert"

wardrobe:
  - character_id: "OMAR-01"
    scene_range: "all"
    items:
      - name: "t-shirt"
        color: "charcoal gray"
        hex: "#36454F"
        material: "soft cotton"
        condition: "slightly worn, soft"
        fit: "relaxed"
        position: "main garment"
      - name: "shorts"
        color: "black"
        hex: "#1A1A1A"
        material: "athletic, moisture-wicking"
        condition: "fresh, clean"
        fit: "athletic, mid-thigh"
      - name: "shoes"
        color: "white/gray running shoes"
        material: "athletic mesh"
        condition: "new-looking"
        position: "worn throughout"

props:
  - id: "PROP-01-NOOR-BOX"
    name: "NOOR Energy Box"
    type: "product packaging"
    shape: "Small rectangular box (5cm x 3cm x 1cm), matte black with brand orange accent"
    material: "matte cardboard"
    color: "matte black with brand orange (#FF6B35)"
    condition: "new, crisp"
    position: "inside kitchen drawer initially, then in hand"
    visual_marks:
      - "NOOR logo (wordmark) in white on black"
      - "Small sun icon in brand orange"
    forbidden_changes: "Color must remain matte black + brand orange"

  - id: "PROP-02-NOOR-TABLET"
    name: "NOOR Energy Tablet"
    type: "product"
    shape: "Round, 1.5cm diameter, slight thickness. Glossy surface with subtle pulse pattern"
    material: "compressed powder, glossy coating"
    color: "Deep orange/amber (#FF6B35) with subtle gold flecks"
    condition: "new, pristine"
    size: "1.5cm diameter"
    position: "in box, then in hand, then in mouth"
    visual_marks:
      - "Subtle radial pattern (sun motif)"
      - "Glows slightly when active (in SC03-04)"
    forbidden_changes: "Must remain round, must remain brand orange"

  - id: "PROP-03-ALARM-CLOCK"
    name: "Digital Alarm Clock"
    type: "fixture"
    shape: "Small rectangular digital display"
    material: "plastic with LED display"
    color: "Black with red LED numbers"
    position: "bedside table"
    display: "3:00 AM (red LED)"

locations:
  - id: "LOC-01-BEDROOM"
    name: "Bedroom (modern, minimal)"
    type: "interior"
    architecture: "Plain white walls, dark wooden floor, simple bed, bedside table, door to hallway"
    fixed_elements: ["bed", "alarm clock", "window (curtains closed)", "door"]
    lighting: "Very dim, single bedside lamp off, faint pre-dawn from window"
    atmosphere: "Quiet, still, heavy"
    forbidden_changes: "No bright lighting in SC01-02"

  - id: "LOC-02-KITCHEN"
    name: "Kitchen (modern, minimal)"
    type: "interior"
    architecture: "White walls, dark countertop, simple cabinets, drawer"
    fixed_elements: ["counter", "drawer (where NOOR box is)", "sink", "window"]
    lighting: "Dim (SC02), gradually warm (SC03), bright (SC04)"
    atmosphere: "Functional, minimal, quiet"

  - id: "LOC-03-OUTDOOR"
    name: "City Street + Rooftop (sunrise)"
    type: "exterior"
    architecture: "Modern city buildings, rooftop view, golden hour sky"
    fixed_elements: ["sky", "buildings", "horizon", "sun rising"]
    lighting: "Golden hour (warm), sun visible in SC06"
    atmosphere: "Alive, energetic, fresh"

lighting_atmosphere:
  scene_range: "all"
  overall_scheme: "time_progression (cool pre-dawn → warm sunrise)"
  
  key_light_signature:
    SC01-02: "very dim, cool blue 6500K, single source (alarm clock LED + window)"
    SC03: "transitioning (NOOR tablet adds warm light)"
    SC04: "warm burst 3200K, dramatic shift"
    SC05-06: "golden hour 3000K, sun-lit"
  
  color_temperature_mix: "Time-progression: cool → warm"
  atmosphere:
    SC01-02: "Heavy, still, dust in minimal light"
    SC03-04: "Particles of light around NOOR tablet (glowing effect)"
    SC05-06: "Clear, vibrant, sun rays"

camera_grammar:
  default_lens: "35mm (versatile)"
  default_aperture: "f/2.0"
  default_dof: "shallow to medium"
  default_height: "eye_level"
  default_motion: "static or slow_dolly"
  
  allowed_motions:
    - "static (locked off)"
    - "slow_dolly_in (1-2cm/s)"
    - "slow_pan (intentional)"
  forbidden_motions:
    - "handheld (too unstable for this style)"
    - "whip_pan (except in SC04 for transition)"
    - "crane_shot"
    - "extreme_zoom"
  
  sensor_format: "ARRI Alexa 35 (or equivalent)"
  film_stock: "Kodak Vision3 500T (warm) or clean digital"
  frame_rate: "24 fps"

color_palette:
  primary:
    - name: "brand_orange"
      hex: "#FF6B35"
      usage: "NOOR product, energy, brand"
    - name: "deep_charcoal"
      hex: "#2C2C2C"
      usage: "wardrobe, shadows"
    - name: "cool_pre_dawn"
      hex: "#3A4A5C"
      usage: "early scenes (SC01-02)"
    - name: "golden_hour"
      hex: "#FFB347"
      usage: "later scenes (SC05-06)"
  forbidden:
    - "neon green"
    - "saturated red (different from brand orange)"
    - "pastel pinks"
    - "pure black (use deep_charcoal)"

sound_signature:
  scene_range: "all"
  
  ambience_baseline:
    SC01-02: "very quiet, slight hiss, low hum"
    SC03-04: "transition (subtle pulse with NOOR)"
    SC05-06: "city morning (birds, distant traffic, alive)"
  
  music_signature:
    primary: "score_electronic_building"
    style: "Modern electronic, building from quiet to powerful"
    structure: "intro (quiet) → build (SC03) → climax (SC04-05) → resolve (SC06)"
    volume_with_voiceover: "-18dB (ducked)"
    volume_without_voiceover: "-10dB"
  
  voice_direction:
    protagonist_voiceover:
      pace: "slow (2 words/second) initially, faster (3 words/second) by SC04"
      tone: "tired → confident"
      accent: "Gulf Arabic, clean"

  language: "ar"
  dialect: "خليجي / فصحى مبسطة"
```

---

## 3. Frame Chain (مختصر)

```yaml
frame_chain:
  total_shots: 14
  chain_breaks: 0
  status: "complete"
  
  shots_summary:
    - shot_id: "SC01_SH01"
      duration: "3s"
      start_frame: "FRAME-001 (alarm clock 3:00 AM)"
      end_frame: "FRAME-002 (Omar's eye opening)"
      links_to: "SC01_SH02 (FRAME-002 = FRAME-003)"
    - shot_id: "SC01_SH02"
      duration: "2s"
      start_frame: "FRAME-003 (Omar's eye opening, mid-blink)"
      end_frame: "FRAME-004 (Omar rising, hand reaching for bed edge)"
      links_to: "SC02_SH01 (FRAME-004 = FRAME-005, hand on drawer)"
    - shot_id: "SC02_SH01"
      duration: "3s"
      start_frame: "FRAME-005 (hand on drawer handle)"
      end_frame: "FRAME-006 (hand lifting NOOR box)"
      links_to: "SC02_SH02 (FRAME-006 = FRAME-007, hand opening box)"
    - shot_id: "SC02_SH02"
      duration: "2s"
      start_frame: "FRAME-007 (hand opening NOOR box)"
      end_frame: "FRAME-008 (Omar looking at the tablet, eyes wide)"
      links_to: "SC03_SH01 (FRAME-008 = FRAME-009, CU on tablet)"
    - shot_id: "SC03_SH01"
      duration: "3s"
      start_frame: "FRAME-009 (CU on NOOR tablet in hand)"
      end_frame: "FRAME-010 (tablet near mouth, glowing)"
      links_to: "SC03_SH02 (FRAME-010 = FRAME-011, putting in mouth)"
    - shot_id: "SC03_SH02"
      duration: "2s"
      start_frame: "FRAME-011 (tablet at mouth)"
      end_frame: "FRAME-012 (Omar's face after swallowing, neutral)"
      links_to: "SC04_SH01 (FRAME-012 = FRAME-013, transformation begins)"
    - shot_id: "SC04_SH01"
      duration: "3s"
      start_frame: "FRAME-013 (Omar's face, neutral, transformation starts)"
      end_frame: "FRAME-014 (Omar's eyes, now alert, transformation complete)"
      links_to: "SC04_SH02 (FRAME-014 = FRAME-015, head turning to door)"
    - shot_id: "SC04_SH02"
      duration: "2s"
      start_frame: "FRAME-015 (head turning to door)"
      end_frame: "FRAME-016 (whip pan motion blur)"
      links_to: "SC05_SH01 (FRAME-016 = FRAME-017, hand on door)"
    - shot_id: "SC05_SH01"
      duration: "2s"
      start_frame: "FRAME-017 (hand on door)"
      end_frame: "FRAME-018 (door opening, light flooding in)"
      links_to: "SC05_SH02 (FRAME-018 = FRAME-019, stepping out)"
    - shot_id: "SC05_SH02"
      duration: "2s"
      start_frame: "FRAME-019 (stepping out)"
      end_frame: "FRAME-020 (Omar in city, motion)"
      links_to: "SC05_SH03 (FRAME-020 = FRAME-021, running)"
    - shot_id: "SC05_SH03"
      duration: "1s"
      start_frame: "FRAME-021 (Omar running, side view)"
      end_frame: "FRAME-022 (Omar at rooftop edge, looking at sun)"
      links_to: "SC06_SH01 (FRAME-022 = FRAME-023, sun on face)"
    - shot_id: "SC06_SH01"
      duration: "3s"
      start_frame: "FRAME-023 (sun on Omar's face, smiling)"
      end_frame: "FRAME-024 (Omar in profile, looking at sun, peaceful)"
      links_to: "SC06_SH02 (FRAME-024 = FRAME-025, logo overlay position)"
    - shot_id: "SC06_SH02"
      duration: "2s"
      start_frame: "FRAME-025 (Omar in profile, logo overlay space ready)"
      end_frame: "FRAME-026 (final frame, Omar + logo + CTA)"
      links_to: "end (FRAME-026 holds for 1s, then fade to black)"

  chain_breaks: 0
  
  match_types_used:
    - "action_match: SC01→SC02 (hand on bed → hand on drawer)"
    - "action_match: SC02→SC03 (hand on box → hand on tablet)"
    - "morph: SC03→SC04 (tablet in mouth → face post-swallow)"
    - "whip_pan: SC04→SC05 (motion blur)"
    - "action_match: SC05→SC06 (running → still looking)"
```

---

## 4. Image Prompts (عينة — IMG-SC03-SH01)

```yaml
prompt_id: "IMG-SC03-SH01"
shot_id: "SC03_SH01"
type: "main_scene"
purpose: "اكتشاف القرص: CU على NOOR tablet في يد Omar"

identity_strings:
  character: "[from Continuity Bible - OMR-01]"
  wardrobe: "[from Continuity Bible - t-shirt + shorts]"
  prop: "NOOR Energy Tablet"
  location: "Kitchen (minimal, dim)"

full_prompt_10_layers: |
  Cinematic film still, single frame, extreme close-up.
  
  A. INTENT: The product reveal moment. This is the
  hero shot of the NOOR Energy Tablet. The audience
  should immediately read "this is the answer." The
  tablet is the visual protagonist of this frame.
  
  B. SUBJECT: A round NOOR Energy Tablet held between
  the thumb and index finger of a young man's hand.
  Identity of the hand (from Continuity Bible):
  - Light olive skin (Fitzpatrick III)
  - 27-year-old man
  - Clean, well-kept nails
  - No rings, no watch
  The hand holds the tablet delicately, with reverence.
  The tablet itself: 1.5cm diameter, perfectly round,
  deep orange-amber color (#FF6B35) with subtle gold
  flecks, glossy surface, faint radial pattern (sun
  motif), slightly glowing from within (subtle pulse).
  
  C. ENVIRONMENT: The hand and tablet are in focus
  against a softly blurred kitchen background. The
  kitchen is minimal: white walls, dark countertop
  visible in soft focus behind. Very dim pre-dawn
  lighting. No modern clutter visible.
  
  D. COMPOSITION: Extreme close-up (ECU) on the tablet.
  The tablet is in the center of the frame, taking up
  about 30% of the frame width. The hand occupies
  the lower third. The background is completely out of
  focus (bokeh). Leading lines: the radial pattern
  on the tablet itself draws the eye to the center.
  Visual hierarchy: the glowing tablet first, then the
  hand, then the background. Three depth layers: tablet
  (foreground), hand (midground), kitchen (background).
  
  E. CAMERA: ECU on the tablet, camera at table height
  looking slightly up. Lens: 100mm macro (for shallow
  DOF and product detail). Aperture: f/2.8. Depth of
  field: very shallow (only the tablet is sharp, the
  rest is bokeh). Sensor: ARRI Alexa 35 simulation.
  Film stock: clean digital.
  
  F. LIGHTING: The tablet itself appears to be a
  subtle light source (faint glow). Key light: dim
  ambient from above (4500K, cool). Fill: the tablet's
  own glow provides a subtle warm fill on the fingers
  (2400K). No rim light. Practical lights: none in
  this frame. Contrast: medium (5:1). The tablet should
  read as the brightest element despite the dim
  environment. Atmosphere: subtle dust motes visible
  in the dim light (very subtle).
  
  G. MOTION: N/A (still image)
  
  H. CONTINUITY: Inherits from SC02_SH02 end state
  (Omar has just opened the NOOR box, looking at the
  tablet). Exit state: the hand continues to hold the
  tablet in the same position, ready to bring it
  closer to the mouth in the next shot. Lighting
  starts to shift warmer.
  
  I. STYLE: Genre: product reveal, motivational.
  Visual movement: realistic cinematic. Color palette:
  brand_orange (#FF6B35) dominant on the tablet,
  warm_amber on the skin, deep_charcoal on background.
  Forbidden: any other bright colors, any logos other
  than the NOOR radial pattern. Texture: clean digital,
  no film grain. Color grade: vibrant on the tablet,
  slightly desaturated on the background. Reference:
  Apple product shots (clean, focused), Blade Runner
  2049 (warm-cool contrast).
  
  J. CONSTRAINTS:
  - Identity lock: OMR-01 hand (light olive skin, no
    rings, no watch, clean nails)
  - Wardrobe: not visible in this frame (only hand)
  - Prop lock: NOOR Energy Tablet (specific shape,
    color, radial pattern - see IMG-PROP-NOOR-TABLET)
  - The tablet MUST glow faintly from within
  - Hands: 5 fingers, correct anatomy, no extra fingers
  - The NOOR logo or any other text: NOT visible in
    this frame (the radial pattern only)
  - Other props: only the hand and tablet visible
  - Lighting: the tablet is the brightest element
  - negative_prompts:
    - "no other logos or text"
    - "no other props in frame"
    - "no extra fingers or distorted hand"
    - "no realistic human face (only hand)"
    - "no background clutter"

model:
  primary: "bytedance/seedream-4"
  fallback: "midjourney-v6"
  aspect_ratio: "9:16"
  resolution: "1080x1920"

reference_images:
  - path: "assets/anchors/prop-noor-tablet_v2.png"
    role: "prop_anchor"
    weight: "critical"
  - path: "assets/anchors/char-omar-hand_v1.png"
    role: "hand_reference"
    weight: "high"

acceptance_criteria:
  - "القرص في وسط الكادر"
  - "اللون brand_orange (#FF6B35) واضح"
  - "القرص يتوهج بشكل خفيف"
  - "اليد تحتفظ بالقرص بشكل طبيعي"
  - "الخلفية معتمة (bokeh)"
  - "لا شعارات أو نصوص مرئية"
  - "تشريح اليد صحيح"
  - "النمط الشعاعي (radial) مرئي"

rejection_criteria:
  - "القرص لا يتوهج"
  - "لون القرص مختلف"
  - "اليد مشوهة"
  - "شعارات أخرى ظاهرة"
  - "خلفية صاخبة"
  - "القرص غير واضح (motion blur)"

expected_attempts: 3
fallback_strategy:
  if_3_attempts_fail:
    - "ولّد الصورة بدون glow، أضف glow في post"
    - "ولّد الصورة بـ prompt أبسط: 'a glowing orange tablet in a hand'"
    - "إذا فشل: post-production composite (توليد القرص منفصلًا + يد منفصلة + دمج)"

generated_assets:
  - path: "assets/main/sc03_sh01_v1.png"
    attempt: 1
    status: "rejected"
    reason: "القرص لا يتوهج بشكل كافٍ"
  - path: "assets/main/sc03_sh01_v2.png"
    attempt: 2
    status: "approved"
    notes: "ممتاز، glow واضح، brand color صحيح"
```

---

## 5. Motion Prompts (عينة — MOT-SC04-SH01)

```yaml
prompt_id: "MOT-SC04-SH01"
shot_id: "SC04_SH01"
type: "main_scene"
input_image: "assets/main/sc04_sh01_v2.png"
duration: "3s"
purpose: "التحوّل: Omar بعد ابتلاع القرص، يبدأ التحول"

full_prompt_motion: |
  Cinematic film motion. The frame begins as the input
  image (Omar in the kitchen, expression neutral,
  having just swallowed the NOOR tablet).
  
  Motion (the TRANSFORMATION):
  - Omar stands still, eyes closed, breathing deeply
  - The lighting in the kitchen begins to shift:
    - Starts: very dim, cool blue 6500K
    - At 1s: warm amber 4000K begins to mix
    - At 2s: dominant warm amber 3000K
    - At 3s: golden warm 3000K, full transformation
  - Subtle particles of light begin to appear around
    Omar's body (very subtle, like dust catching
    golden light) — most visible in the now-warm
    light beam from the (unseen) window
  - Omar's skin tone becomes slightly more vibrant
    (subtle warming, more life in the complexion)
  - Omar's chest rises and falls (slow, deep breath)
  - At 2.5s: Omar's eyes open slowly, deliberately
  - At 3s (end of shot): eyes are fully open, alert,
    the transformation is visible
  
  Camera: static, locked, no motion. The frame
  composition is identical to the input image.
  
  Continuity: This shot continues from MOT-SC03_SH02
  (Omar's face after swallowing, eyes closed). Same
  location (kitchen), same character (Omar-01),
  same wardrobe.
  
  End state: Omar's eyes open, looking directly
  forward (toward the door, which is just out of
  frame), transformation visible. This is the start
  of the next shot (SC04_SH02 - head turning to door).

model:
  primary: "bytedance/seedance-2.0"
  fallback: "runwayml/gen4"
  aspect_ratio: "9:16"
  duration: "3s"

start_frame:
  matches: "input image (sc04_sh01_v2.png)"
  description: "Omar, eyes closed, dim cool light, kitchen"

end_frame:
  matches: "start of MOT-SC04-SH02"
  description: "Omar, eyes open, alert, warm golden light, kitchen"

lipsync:
  required: false
  text: "N/A"

text_preservation:
  required: false
  text: "N/A"

acceptance_criteria:
  - "التحول الضوئي يحدث تدريجيًا (cool → warm)"
  - "عيني Omar تُفتحان ببطء"
  - "جزيئات الضوء خفيفة، ليست مبالغًا فيها"
  - "نفس الشخصية (OMR-01) عبر اللقطة"
  - "نفس الملابس"
  - "Frame يبدأ = input image"
  - "Frame ينتهي = eyes open, looking toward door"
  - "Camera ثابتة (لا motion)"

rejection_criteria:
  - "الوجه يتغير"
  - "الملابس تتغير"
  - "التحول مفاجئ (يجب أن يكون تدريجي)"
  - "حركة كاميرا"
  - "إضاءة غير متدرجة"
  - "جزيئات الضوء مبالغ فيها"

expected_attempts: 4
fallback_strategy:
  if_3_attempts_fail:
    - "قسّم لثلاث لقطات: (1) cool, (2) mid, (3) warm — ثم cross dissolve"
    - "ولّد بـ prompt أبسط: 'eyes open, lighting changes warm'"
    - "post-production: غيّر color grade تدريجيًا في Premiere/DaVinci"

generated_assets:
  - path: "assets/motion/sc04_sh01_v1.mp4"
    attempt: 1
    status: "rejected"
    reason: "التحول مفاجئ جدًا"
  - path: "assets/motion/sc04_sh01_v2.mp4"
    attempt: 2
    status: "rejected"
    reason: "الملابس تغيرت"
  - path: "assets/motion/sc04_sh01_v3.mp4"
    attempt: 3
    status: "approved"
    notes: "ممتاز، التحول تدريجي، الشخصية ثابتة"
```

---

## 6. Audio Package (مختصر)

```yaml
audio_package:
  total_layers: 7
  total_duration: "30s"
  target_platform: "TikTok (-14 LUFS)"
  master_lufs: -14
  
  layers:
    
    - layer_id: "AMBIENCE-01"
      type: "ambience"
      source: "ElevenLabs SFX"
      prompt: "very quiet interior room tone at 3:00 AM, slight low hum, no traffic, almost silence"
      duration: "0-15s (SC01-04, very quiet)"
      volume_db: -24
      fade_in: "0.5s"
      fade_out: "1s"
    
    - layer_id: "AMBIENCE-02"
      type: "ambience"
      source: "ElevenLabs SFX"
      prompt: "early morning city ambience at dawn, distant birds, very light traffic, alive but quiet"
      duration: "18-30s (SC05-06, transitioning in)"
      volume_db: -20
      fade_in: "1s"
    
    - layer_id: "VO-01"
      type: "voiceover"
      text: "الساعة ثلاثة. والجسد يقول: لا."
      language: "ar"
      dialect: "خليجي / فصحى مبسطة"
      timestamps: "0-3s"
      voice_model: "ElevenLabs"
      voice_id: "arabic_male_calm_v2"
      parameters:
        stability: 0.65
        similarity_boost: 0.80
        style: 0.40
      processing: "Adobe Podcast enhance"
      volume_db: -3
    
    - layer_id: "VO-02"
      type: "voiceover"
      text: "قررت. فُعّلت."
      timestamps: "12-15s (during SC04 transformation)"
      voice_model: "ElevenLabs"
      voice_id: "arabic_male_confident_v1"
      parameters:
        stability: 0.55
        style: 0.65
      processing: "Adobe Podcast enhance"
      volume_db: -3
    
    - layer_id: "VO-03"
      type: "voiceover"
      text: "NOOR. فعّل فجرك."
      timestamps: "25-28s (during SC06)"
      voice_model: "ElevenLabs"
      voice_id: "arabic_male_brand_v1"
      parameters:
        stability: 0.75
        style: 0.50
      processing: "Adobe Podcast enhance"
      volume_db: -3
    
    - layer_id: "MUSIC-01"
      type: "music"
      source: "Suno v3.5"
      prompt: |
        Modern electronic music for a 30-second energy
        product ad. Starts very quiet, contemplative,
        minimal synth pad with a single piano note.
        Builds gradually from 10s with added percussion.
        At 18s, drops into a powerful, energetic
        electronic section with driving beat (120 BPM),
        confident and modern. Resolves at 28s with
        a brand-friendly final chord. Instrumental only.
      structure: "intro (0-10s) → build (10-18s) → drop/climax (18-25s) → resolve (25-30s)"
      volume_db: -12
      duck_under_voiceover: "-6dB during VO-01, VO-02, VO-03"
      tags: "electronic, modern, advertising, building, energetic"
    
    - layer_id: "SFX-01"
      type: "sfx"
      source: "ElevenLabs SFX"
      prompt: "subtle magical pulse, like a tablet activating, low and soft"
      timestamps: "13-15s (during transformation start)"
      volume_db: -10
    
    - layer_id: "SFX-02"
      type: "sfx"
      source: "ElevenLabs SFX"
      prompt: "warm magical whoosh, energy gathering, ascending"
      timestamps: "18-20s (during transition from kitchen to outdoor)"
      volume_db: -8
    
    - layer_id: "SFX-03"
      type: "sfx"
      source: "ElevenLabs SFX"
      prompt: "subtle brand sting, modern and confident, 2 seconds, distinctive"
      timestamps: "28-30s (final brand sound)"
      volume_db: -6
  
  lipsync_plan:
    total_scenes_with_lipsync: 0  # كل الـ VO voiceover، لا lip-sync
  
  mixing_plan:
    master_target: "TikTok (-14 LUFS)"
    
    levels:
      dialogue: -3
      voiceover: -3
      music: -12
      sfx: -8 to -10 (variable)
      ambience: -20 to -24
    
    ducking:
      music_under_voiceover:
        amount: "-6dB"
        attack: "200ms"
        release: "500ms"
        trigger: "VO-01, VO-02, VO-03"
    
    eq_zones:
      voiceover: "boost 3kHz presence, 8kHz air, cut 200Hz"
      music: "subtle high-shelf +3dB at 10kHz"
      ambience: "cut 50Hz, cut 12kHz"
  
  mastering_plan:
    target_platforms:
      tiktok:
        target_lufs: -14
        peak_dbfs: -1
      instagram:
        target_lufs: -16
        peak_dbfs: -1
    processing:
      final_eq: "subtle smile curve"
      final_compression: "1.5:1 master bus"
      limiter: "true peak -1dBFS"
    output_formats:
      master: "WAV 48kHz 24bit"
      social: "MP4 with AAC 320kbps"
  
  total_lipsync_scenes: 0
```

---

## 7. Assembly Guide (مختصر)

```yaml
assembly_guide:
  tools_required:
    primary: "DaVinci Resolve (free) / Adobe Premiere"
    audio: "DaVinci Fairlight / Audition"
    effects: "After Effects (للنصوص والشعارات)"
    compositing: "RunwayML / ComfyUI (للتعديلات)"
  
  workflow:
    
    step_1_organize:
      duration_minutes: 5
      actions:
        - "Create project folder structure"
        - "Import all 14 video shots (from motion_prompts)"
        - "Import all 7 audio layers"
        - "Import NOOR logo PNG (transparent)"
    
    step_2_timeline_rough_cut:
      duration_minutes: 10
      actions:
        - "Place 14 shots in scene order (SC01 → SC06)"
        - "Apply transitions per frame_chain map"
        - "Initial pacing: 3-5s per shot"
        - "Total target: 30s"
    
    step_3_audio_mix:
      duration_minutes: 15
      actions:
        - "Layer 7 audio tracks (VO-01, VO-02, VO-03, MUSIC-01, SFX-01-03, AMBIENCE-01-02)"
        - "Apply ducking (music -6dB under VO)"
        - "Mix levels per audio_package"
        - "Master to -14 LUFS (TikTok target)"
    
    step_4_text_and_graphics:
      duration_minutes: 10
      actions:
        - "Add NOOR logo overlay at SC06 (3-5s)"
        - "Add 'فعّل فجرك' subtitle (post_overlay)"
        - "Verify legibility on mobile (small text test)"
        - "Add brand orange color treatment to text"
    
    step_5_color_grading:
      duration_minutes: 10
      actions:
        - "Apply base LUT (cinematic warm)"
        - "Manual adjustment: cool blue for SC01-02, warm gold for SC04-06"
        - "Ensure color script map is followed"
        - "Skin tone check (warm, vibrant by SC04+)"
    
    step_6_polish:
      duration_minutes: 5
      actions:
        - "Final review"
        - "Add subtle film grain (optional)"
        - "Add final brand sting timing"
    
    step_7_export:
      duration_minutes: 5
      actions:
        - "Export TikTok version (9:16, 1080x1920, H.264, -14 LUFS)"
        - "Export Instagram Reels version (9:16, same)"
        - "Export master (ProRes 422 HQ)"
  
  final_qa:
    checklist:
      - "All 14 shots in order"
      - "Total duration: 30s"
      - "Aspect ratio: 9:16 (TikTok/Reels)"
      - "No missing transitions"
      - "Audio levels: VO clear, music ducked, ambience subtle"
      - "Text legible on mobile"
      - "Color progression: cool → warm"
      - "Brand visible (logo + tagline)"
      - "No spelling errors"
      - "Master LUFS: -14"
  
  troubleshooting:
    - issue: "Text in video is distorted"
      fix: "Remove from video, add as post_overlay"
    - issue: "Color shift between shots"
      fix: "Apply same LUT, manually match"
    - issue: "Music too loud vs VO"
      fix: "Increase ducking to -8dB"
    - issue: "Audio levels inconsistent across platforms"
      fix: "Export platform-specific versions"
```

---

## ملخص تنفيذي

| المرحلة | الوكيل | المخرج | الحالة |
|---|---|---|---|
| M0 | 01-intake | intake_brief | ✅ |
| M1 | 21-creative-research-lab | concept_deck | ✅ |
| M2 | 30-executive-producer | approved_concept | ✅ |
| M3 | 23-narrative-architect | story + script | ✅ |
| M4 | 24-shot-architect | shot_cards | ✅ |
| M5 | 25-continuity-supervisor | bible + frame_chain | ✅ |
| M6 | 26-transition-engineer | transition_map | ✅ |
| M6.5 | 27-typography + 28-text-motion | text_plan | ✅ |
| M7 | 29-audio-decision-engine | audio_package | ✅ |
| M8 | 22-prompt-architecture | image_prompts | ✅ |
| M9 | 22-prompt-architecture | motion_prompts | ✅ |
| M10 | 30-EP + 31-QG | 5 output files | ✅ |
| M11 | 30-EP | final_delivery | ✅ |

**Quality Gates:**
- G0: PASS ✅
- G1: PASS ✅
- G2: PASS ✅
- G3: PASS ✅
- G4: PASS ✅ (10/10 prompts)
- G5: PASS ✅
- G6: PASS ✅ (post_overlay for NOOR logo)
- G7: PASS ✅
- G8: PASS ✅ (5/5 files)

**النتيجة:** مشروع جاهز للإنتاج، 30 ثانية، 14 لقطة، 5 ملفات تسليم، كل Quality Gates passed.
