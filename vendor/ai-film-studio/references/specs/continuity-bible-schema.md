# Continuity Bible Schema — مخطط الـ Continuity Bible

## الهدف

توثيق المخطط الكامل (Schema) لملف **Continuity Bible** الذي يبنيه `workflows/M4c-continuity-qc.md`. هذا الـ reference هو القاموس الرسمي لكل قسم، حقوله، وقواعده.

---

## ما هي Continuity Bible؟

**القاموس البصري والسردي للفيلم.** كل ما يجب أن يبقى ثابتًا بين المشاهد يُسجَّل هنا. تُستخدم كمرجع إلزامي لـ `workflows/M7a-prompt-architecture.md`.

---

## الأقسام السبعة

### 1. Identity (الهوية)

**الغرض:** توثيق كل شخصية بشكل ثابت.

**Schema:**

```yaml
identity:
  - id: "CHAR-01"           # معرّف فريد
    role: "protagonist"     # دور في القصة
    name: "Sami"            # اسم الشخصية
    age: 32                 # العمر
    ethnicity: "يمني"        # الأصل
    gender: "male"          # الجنس
    
    # البصمة البصرية (Visual Signature)
    visual_signature: |
      Short trimmed beard with a distinctive gray patch
      on the LEFT cheek, faded burn scar on the back of
      the RIGHT hand, short curly black hair with a single
      gray streak at the front
    
    anatomy:
      face:
        - "Square jaw with defined cheekbones"
        - "Dark brown eyes with subtle wrinkles at the corners"
        - "Straight nose, slightly wide at the nostrils"
        - "Thin lips, defined cupid's bow"
      body:
        - "180cm tall, lean athletic build"
        - "Shoulders slightly wider than average"
        - "Long arms relative to torso"
        - "Hands: long, slender fingers"
      skin:
        - "Warm wheat-toned (Fitzpatrick Type IV)"
        - "Light freckles across the nose and cheeks"
        - "Slight tan line on left wrist (watch)"
        - "Small mole on right side of neck (below ear)"
      hair:
        - "Short curly black hair"
        - "Single gray streak at the front (above right temple)"
        - "Some strands fall over forehead when unstyled"
      facial_hair:
        - "Short trimmed beard, 5mm length"
        - "DISTINCTIVE GRAY PATCH on the LEFT cheek"
        - "Connected to sideburns"
        - "No mustache (clean-shaven upper lip)"
    
    expression_baseline: |
      Default expression: tired, calm, slightly hooded eyes.
      Slight downward turn of lips when neutral.
    
    forbidden_inconsistencies:
      - "The gray patch on left cheek MUST remain"
      - "The burn scar on right hand MUST remain"
      - "Eye color must NOT change"
      - "Skin tone must NOT change"
      - "Body type must NOT change (no weight gain/loss)"
      - "Age must NOT change visibly"
    
    reference_image_paths:
      - "assets/anchors/char-01_v2.png"     # صورة معتمدة
      - "assets/anchors/char-01_profile.png"  # صورة جانبية
    
    age_progression: "constant (no aging within film)"
  
  - id: "CHAR-02"
    role: "supporting"
    name: "..."
    # ... نفس البنية
```

**قواعد:**

- ✅ `visual_signature` يجب أن يحوي البصمات البصرية الفريدة
- ✅ `anatomy.face` يجب أن يكون مفصلًا (3+ سمات)
- ✅ `anatomy.body` يجب أن يحوي القياسات
- ✅ `forbidden_inconsistencies` يجب أن يحوي 4+ عناصر
- ❌ لا تكتب "handsome" أو "beautiful" — اكتب سمات بصرية محددة
- ❌ لا تنسَ `reference_image_paths` (1+ صور معتمدة)

---

### 2. Wardrobe (الملابس)

**Schema:**

```yaml
wardrobe:
  - character_id: "CHAR-01"
    scene_range: "SC01-SC06"  # أو "all"
    
    items:
      - name: "apron"
        arabic_name: "مئزر"
        color: "charcoal gray"
        hex: "#36454F"
        material: "heavy linen"
        weave: "visible texture"
        condition: "worn edges, no tears"
        fit: "loose, tied at back"
        details:
          - "Two front pockets (visible at hip level)"
          - "Slight fraying at hem"
          - "Faint coffee stain on right pocket"
        position: "outermost layer (over shirt)"
      
      - name: "shirt"
        arabic_name: "قميص"
        color: "faded off-white"
        hex: "#F5F0E1"
        material: "light cotton"
        condition: "lightly ironed, sleeve cuffs visible"
        fit: "relaxed, slightly loose at shoulders"
        details:
          - "Sleeves rolled to forearms"
          - "Visible button placket"
          - "No collar (crew neck style)"
        position: "under apron"
      
      - name: "watch"
        arabic_name: "ساعة"
        color: "weathered brown"
        material: "leather strap, brass case"
        condition: "worn, faded"
        position: "left wrist"
        details:
          - "Vintage style (1970s look)"
          - "Round face, brass bezel"
          - "Brown leather strap, slightly cracked"
    
    hair_style:
      description: |
        Short curly black hair, slightly disheveled. A single
        gray streak falls above the right temple (visible from
        the left side of the face as a subtle lighter strand).
      state: "natural, unstyled (no product)"
    
    forbidden_changes:
      - "Apron color must NOT change"
      - "Watch position must remain LEFT wrist"
      - "Watch style must remain vintage brass"
      - "Shirt must remain crew neck (no collar change)"
      - "Sleeves must remain rolled to forearms"
  
  - character_id: "CHAR-02"
    # ... نفس البنية
```

**قواعد:**

- ✅ كل لون بـ hex (ليس فقط اسم)
- ✅ كل عنصر له `condition` (ليس فقط وصف)
- ✅ `forbidden_changes` يحدد ما لا يمكن تغييره
- ❌ لا تكتب "nice clothes" — اكتب وصف محدد
- ❌ لا تنسَ الإكسسوارات (ساعة، خاتم، نظارة)

---

### 3. Props (الدعائم)

**Schema:**

```yaml
props:
  - id: "PROP-01"
    name: "Brass Dallah"
    arabic_name: "ركوة نحاسية صنعانية"
    type: "coffee_pot"
    
    shape: |
      Round bulbous base (15cm diameter), gracefully
      tapering neck (10cm), curved handle on the side,
      pointed conical lid (5cm). Total height ~30cm.
    
    material: "polished brass"
    color_signature: "warm golden (#C9A66B)"
    hex: "#C9A66B"
    
    condition: "well-used, slight patina on base, polished lid"
    size: "medium (30cm height, 15cm base diameter)"
    
    position_in_scene: "central hearth, on hot coals"
    state_in_scene: "always on coals, always steaming"
    
    visual_marks:
      - "Faint maker's mark on base (illegible from camera)"
      - "Small dent on left side of base"
      - "Lid has small finial (decorative top)"
    
    references: "see IMG-PROP-01 for canonical image"
    
    forbidden_changes:
      - "Must remain BRASS (not silver, not copper)"
      - "Must remain TRADITIONAL SHAPE (not modern)"
      - "Must remain ON COALS (not on table, not held)"
      - "Color temperature in image: warm golden"
      - "Must remain SINGLE (not multiple dallahs)"
  
  - id: "PROP-02"
    name: "Brass Coffee Cup"
    arabic_name: "فنجان قهوة نحاسي"
    type: "cup"
    
    shape: |
      Small, no handle. Rounded base, slightly flared
      rim. 5cm height, 4cm rim diameter.
    
    material: "brass (same family as dallah)"
    color_signature: "warm golden (matches dallah)"
    hex: "#C9A66B"
    
    condition: "polished, light patina on rim"
    
    position_in_scene: "in front of SAMI-01 on the counter"
    state_in_scene: "empty initially, fills during SC03"
    
    visual_marks:
      - "Thin gold rim line (subtle decoration)"
      - "Same brass family as dallah (visual unity)"
    
    forbidden_changes:
      - "Must be BRASS (not ceramic, not glass)"
      - "Must be SMALL (5cm, not large mug)"
      - "Must have NO HANDLE"
      - "Must remain SINGLE"
```

**قواعد:**

- ✅ كل prop له `id` فريد
- ✅ `shape` مفصّل (dimensions + parts)
- ✅ `hex` للألوان
- ✅ `visual_marks` للبصمات
- ✅ `forbidden_changes` يحدد القيود
- ❌ لا تنسَ `position_in_scene` (ثابت أم متغير)
- ❌ لا تُهمل `state_in_scene` (كيف يتغير عبر الفيلم)

---

### 4. Locations (الأماكن)

**Schema:**

```yaml
locations:
  - id: "LOC-01"
    name: "Sanaani Coffee House (Interior)"
    arabic_name: "مقهى صنعاني تقليدي"
    type: "interior"
    
    architecture:
      ceiling: |
        Dark wooden beams, hand-carved geometric patterns
        (Islamic motifs), 4m height. Exposed beams.
      walls: |
        Weathered stone walls, 3m height, slight texture
        from age. Faint plaster remnants in places.
      floor: |
        Traditional patterned tile (geometric, hand-painted),
        slightly worn, some tiles cracked. Light gray-blue
        base with red and brown accents.
      windows: |
        One high window (1m x 0.5m) on the back wall,
        3m above floor. Wood frame, traditional lattice
        work. Currently closed (it's pre-dawn).
      door: |
        Wooden door, traditional style, on the left side
        of the back wall. Slightly ajar in the film.
    
    fixed_elements:
      - "Central hearth (1m x 1m), raised 20cm, stone"
      - "Wooden counter (4m length, 1m height, 60cm depth)"
      - "Wooden shelf with brass cups (back wall, 2m height)"
      - "Hanging oil lamp (chain from ceiling, 2m height)"
      - "Small wooden stool (1, near counter)"
    
    practical_lights:
      - "Oil lamp: 2400K, hangs from chain, left of center"
      - "Coals in hearth: 1800K, beneath dallah, low glow"
      - "Window (natural, when opened): 8000K pre-dawn, 5600K day"
    
    acoustic_signature:
      - "Slight echo (stone walls)"
      - "Creaking wood floor (occasional)"
      - "Quiet hiss from coals"
      - "No traffic (interior, before dawn)"
    
    atmosphere:
      - "Dust motes visible in lamp/window light"
      - "Steam from dallah (constant)"
      - "Faint smell of coffee and wood (audio, not visual)"
    
    forbidden_changes:
      - "No modern elements (no electrical wiring, no plastic)"
      - "No additional furniture"
      - "Window must remain HIGH (not at ground level)"
      - "Ceiling must remain WOODEN BEAMS (not concrete)"
      - "Floor must remain TILE (not modern)"
      - "Door must remain WOODEN (not metal)"
      - "Lamp must remain OIL (not electric)"
    
    references: "see IMG-LOC-01 for canonical image"
    
    variations_through_film:
      - "SC01: door closed, lamp on, no character"
      - "SC02: door slightly ajar, lamp on, SAMI-01 enters"
      - "SC04: door open (after SAMI-01 leaves)"
      - "SC05: shot from outside (still LOC-01, but exterior view)"
  
  - id: "LOC-02"
    name: "City Street (Morning)"
    # ... same structure
```

**قواعد:**

- ✅ `architecture` مفصّل (أبعاد + مواد)
- ✅ `fixed_elements` قائمة كاملة
- ✅ `practical_lights` مع درجة حرارة
- ✅ `forbidden_changes` مفصّل
- ✅ `variations_through_film` (كيف يتغير المكان عبر الفيلم)
- ❌ لا تنسَ `acoustic_signature` (حتى لو internal)
- ❌ لا تنسَ `atmosphere` (غبار، بخار)

---

### 5. Lighting & Atmosphere (الإضاءة والجو)

**Schema:**

```yaml
lighting_atmosphere:
  scene_range: "all"  # أو "SC01-SC04"
  
  overall_scheme: "low_key_dramatic_practical"
  
  key_light_signature:
    primary_source: "oil_lamp_2400K"
    direction: "left of camera, 45° down"
    quality: "soft (diffused through glass)"
    color_temperature_k: 2400
  
  fill_light_signature:
    primary_source: "ambient_room"
    intensity_ratio: "0.2 (subtle)"
    color_temperature_k: 2400
  
  rim_light_signature:
    primary_source: "window_back_5600K"
    direction: "behind subject, left"
    color_temperature_k: 5600
  
  contrast_ratio: "4:1"
  
  practical_lights_in_scene:
    - source: "oil lamp"
      position: "ceiling, left of center"
      color_temp: "2400K"
      intensity: "key (visible in frame)"
    - source: "coals under dallah"
      position: "central hearth"
      color_temp: "1800K"
      intensity: "decorative + subtle fill from below"
  
  atmosphere:
    - element: "dust motes"
      behavior: "float slowly in lamp and window light"
      visibility: "subtle but visible in key light beam"
    - element: "steam from dallah"
      behavior: "rises slowly, drifts right with air movement"
      visibility: "continuous from SC01 to SC06"
  
  color_temperature_mix: "warm_dominant_with_cool_rim (2400K + 5600K)"
  
  forbidden_lighting:
    - "no bright daylight (must remain pre-dawn)"
    - "no fluorescent or LED"
    - "no colored gels (no red, blue, green lights)"
    - "no strobe or flashing"
    - "no shadows from off-screen characters"
  
  time_consistency:
    note: "Time of day is pre-dawn, doesn't progress significantly"
    exceptions: "SC04 has slight brightness increase (sunrise beginning)"
```

**قواعد:**

- ✅ `color_temperature_k` بالأرقام (ليس وصف)
- ✅ `contrast_ratio` محددة
- ✅ `practical_lights_in_scene` كاملة
- ✅ `atmosphere` مفصلة (dust, steam, fog)
- ✅ `forbidden_lighting` صارمة
- ❌ لا تنسَ `time_consistency` (هل الوقت يتقدم أم لا؟)

---

### 6. Camera & Lens Grammar (لغة الكاميرا)

**Schema:**

```yaml
camera_grammar:
  
  # القيم الافتراضية
  default_lens: "85mm"
  default_aperture: "f/1.8"
  default_dof: "shallow (portrait)"
  default_height: "eye_level"
  default_motion: "static_or_slow_dolly"
  
  # حدود
  allowed_lens_range: "35mm-100mm"
  forbidden_lenses:
    - "macro (extreme close-up of texture)"
    - "14mm ultra-wide (distortion)"
    - "200mm+ (compressed telephoto)"
  
  # الحركة
  allowed_motions:
    - "static (locked off)"
    - "slow_dolly_in (1-2cm/s)"
    - "slow_dolly_out (1-2cm/s)"
    - "slow_pan (2-5°/s)"
  forbidden_motions:
    - "handheld (unless documentary scene)"
    - "whip_pan (too fast)"
    - "360_orbit (too dramatic)"
    - "dolly_zoom (Hitchcock effect — too stylized)"
    - "crane_shot (too elaborate)"
    - "zoom (in/out — only dolly allowed)"
  
  # الحساس والفلم
  sensor_format: "ARRI Alexa 35 (or equivalent)"
  film_stock: "Kodak Vision3 500T"
  frame_rate: "24 fps"
  shutter: "180° (normal)"
  
  # التركيز
  focus:
    default: "on_eyes (for character shots)"
    rack_focus: "allowed if serving narrative"
    focus_pull: "minimal (only when explicitly designed)"
  
  # Color Grading
  color_grade_signature:
    shadows: "cool_teal"
    midtones: "natural_warm"
    highlights: "warm_amber"
    saturation: "natural_slightly_muted"
    contrast: "S-curve cinematic"
    black_point: "0,0,5 (not pure black)"
    white_point: "250,250,250 (not pure white)"
  
  forbidden_camera_practices:
    - "no dutch angle (tilted horizon)"
    - "no jump cuts (unless montage)"
    - "no fast zooms"
    - "no extreme handheld shake"
  
  cinematography_references:
    - "Emmanuel Lubezki (natural light)"
    - "Roger Deakins (precision)"
    - "Bradford Young (low-light, warm)"
```

**قواعد:**

- ✅ `default_lens` و `default_aperture` ثابتين
- ✅ `forbidden_motions` و `allowed_motions` قائمة كاملة
- ✅ `sensor_format` و `film_stock` ثابتين
- ✅ `color_grade_signature` مفصّل
- ❌ لا تكتب "professional" — اكتب values محددة
- ❌ لا تنسَ `cinematography_references` (مرجعيات الأسلوب)

---

### 7. Sound Signature (البصمة الصوتية)

**Schema:**

```yaml
sound_signature:
  scene_range: "all"
  
  ambience_baseline:
    primary: "quiet_interior_pre_dawn"
    elements:
      - "very low city hum (distant)"
      - "soft hiss of hot coals"
      - "occasional creak of old wood"
    volume_db: -22
    consistency: "constant throughout film (no major changes)"
  
  foley_baseline:
    primary: "minimal_realistic"
    elements:
      - "footsteps (when character moves)"
      - "cloth movement (apron, shirt)"
      - "object interactions (cup, dallah)"
    consistency: "matches visual actions"
  
  sfx_signature:
    primary: "minimal_subtle"
    key_sounds:
      - "brass dallah on coals (metallic, soft)"
      - "coffee pouring (liquid, smooth)"
      - "cup placement (ceramic on wood, soft)"
    forbidden_sounds:
      - "no exaggerated sound effects"
      - "no modern electronic sounds"
      - "no car horns or city noise (pre-dawn)"
  
  music_signature:
    primary: "score_piano_strings_arabic_maqam"
    presence: "from SC01 (intro), fades out at SC06"
    style: "cinematic emotional"
    structure: "intro → build → climax → resolve"
    volume_with_dialogue: "-18dB (ducked)"
    volume_without_dialogue: "-12dB (visible)"
  
  silence_points:
    - "before first dialogue (1-2s)"
    - "after climax (3-5s before resolution)"
    - "final shot (1-2s before fade to black)"
  
  language: "ar"
  dialect: "yemeni_sanaani"
  
  voice_direction:
    protagonist:
      pace: "slow (2-3 words/second)"
      tone: "contemplative, tired, then awakening"
      accent: "Yemeni Sanaani (light, authentic)"
    narrator:  # إن وُجد
      pace: "moderate (3 words/second)"
      tone: "intimate, warm, like a memory"
  
  forbidden_audio:
    - "no music during natural dialogue (ducking required)"
    - "no electronic music (out of style)"
    - "no pop or rock (out of style)"
    - "no ambient modern sounds (phones, cars)"
```

**قواعد:**

- ✅ `ambience_baseline` بـ volume_db
- ✅ `foley_baseline` و `sfx_signature` مفصّلين
- ✅ `music_signature` مع structure
- ✅ `voice_direction` لكل شخصية
- ✅ `forbidden_audio` صارم
- ❌ لا تنسَ `silence_points` (حتى لو قليلة)
- ❌ لا تنسَ `language` و `dialect`

---

## Cross-Sections

### Color Palette Cross-Reference

```yaml
color_palette:
  primary:
    - name: "primary_brown"
      hex: "#3B2F2F"
      usage: "wood, dark surfaces"
    - name: "warm_amber"
      hex: "#C9A66B"
      usage: "lamp light, brass, highlights"
    - name: "deep_teal"
      hex: "#2F4F4F"
      usage: "shadows, cool accents"
    - name: "off_white"
      hex: "#F5F0E1"
      usage: "shirt, soft light"
    - name: "charcoal"
      hex: "#36454F"
      usage: "apron, dark fabrics"
  
  skin_tones:
    - name: "warm_wheat"
      hex: "#C9A66B"
      usage: "SAMI-01 skin"
    - name: "tan"
      hex: "#A8794F"
      usage: "alternative if needed"
  
  forbidden:
    - "saturated red (#FF0000 or similar)"
    - "fluorescent yellow"
    - "neon blue"
    - "neon green"
    - "pure black (#000000)"
    - "pure white (#FFFFFF)"
  
  color_script_map:
    "SC01": "warm_amber + deep_teal (contemplative)"
    "SC02": "warm_amber + primary_brown (deeper)"
    "SC03": "primary_brown + charcoal (tension)"
    "SC04": "warm_amber burst (awakening)"
    "SC05": "warm_amber + off_white (clarity)"
    "SC06": "off_white + warm_amber (resolve)"
```

---

## File Template (Markdown)

```markdown
# Continuity Bible — [Project Name]

**Project:** [Name]
**Date:** [ISO]
**Version:** v1.0
**Prepared by:** AI Film Studio v2.0 (Continuity Supervisor)

---

## 1. Identity (الشخصيات)

### CHAR-01 — [Name]

[content from schema]

### CHAR-02 — [Name] (إن وُجد)

[content from schema]

---

## 2. Wardrobe (الملابس)

### CHAR-01

[content from schema]

---

## 3. Props (الدعائم)

### PROP-01 — [Name]

[content from schema]

---

## 4. Locations (الأماكن)

### LOC-01 — [Name]

[content from schema]

---

## 5. Lighting & Atmosphere

[content from schema]

---

## 6. Camera & Lens Grammar

[content from schema]

---

## 7. Sound Signature

[content from schema]

---

## 8. Color Palette

[content from schema]

---

## 9. Cross-References

- Frame Chain: `schemas/state/frame-chain.md`
- Production Blueprint: `schemas/production-blueprint.md`
- Image Prompts: `schemas/image-prompts-package.md`
- Motion Prompts: `schemas/motion-prompts-package.md`
- Audio Package: `schemas/audio-package.md`
```

---

## Best Practices

1. **Update immediately** عند أي تغيير في الشخصية/المكان
2. **Cross-reference** كل قسم بالأقسام الأخرى
3. **Validate** مع 22-prompt-architecture قبل كل prompt
4. **Version** كل تغيير برقم إصدار
5. **Reference images** لـ Identity, Wardrobe, Props, Locations
6. **Forbidden changes** مفصّلة لكل عنصر
7. **Acoustic signature** و Atmosphere لا تُهمل

---

## Common Mistakes

- ❌ Identity String غير مكتمل (نسيان الندبة، البقعة)
- ❌ Forbidden changes غير محددة
- ❌ Reference images غير موجودة
- ❌ لا acoustic signature
- ❌ لا forbidden lighting
- ❌ لا color temperature mix
- ❌ لا variations through film

---

## Validation Checklist

- [ ] كل شخصية لها identity_string كامل
- [ ] كل شخصية لها wardrobe مع hex colors
- [ ] كل prop له shape مفصّل
- [ ] كل location له forbidden_changes
- [ ] كل قسم له forbidden_* قائمة
- [ ] color_palette محدد بـ hex
- [ ] sound_signature كامل
- [ ] camera_grammar مع allowed/forbidden
- [ ] cross-references تعمل
