# state/continuity-bible.md

> **هذا الملف يُملأ ويُحدَّث من قبل `workflows/M4c-continuity-qc.md` عبر دورة حياة المشروع.**
> **القالب الكامل موجود في `references/specs/`.**

---

## معلومات المشروع

```yaml
project:
  id: "[PROJECT_ID]"
  title: "[اسم المشروع]"
  version: "v[X.Y]"
  status: "[IN_DEVELOPMENT / LOCKED]"
  last_updated: "[ISO timestamp]"
  updated_by: "25-continuity-supervisor"
```

---

## 1. Identity (الشخصيات)

### CHAR-01 — [Name]

```yaml
id: "CHAR-01"
role: "protagonist"
name: "[Name]"
age: [XX]
ethnicity: "[...]"
gender: "[...]"

visual_signature: |
  [الوصف البصري المميز]

anatomy:
  face:
    - "[...]"
    - "[...]"
  body:
    - "[...]"
  skin:
    - "[...]"
  hair:
    - "[...]"

forbidden_inconsistencies:
  - "[...]"
  - "[...]"

reference_image_paths:
  - "assets/anchors/char-01_v[X].png"
```

### CHAR-02 — [Name] (إن وُجد)

[نفس البنية]

---

## 2. Wardrobe (الملابس)

### CHAR-01

```yaml
character_id: "CHAR-01"
scene_range: "[SC01-SCXX or all]"

items:
  - name: "..."
    color: "..."
    hex: "..."
    material: "..."
    condition: "..."
    fit: "..."
    details: [...]

forbidden_changes:
  - "..."
```

---

## 3. Props (الدعائم)

### PROP-01 — [Name]

```yaml
id: "PROP-01"
name: "..."
shape: "..."
material: "..."
color_signature: "..."
hex: "..."
condition: "..."
size: "..."
position_in_scene: "..."

visual_marks:
  - "..."

forbidden_changes:
  - "..."
```

---

## 4. Locations (الأماكن)

### LOC-01 — [Name]

```yaml
id: "LOC-01"
name: "..."
type: "interior / exterior"

architecture:
  ceiling: "..."
  walls: "..."
  floor: "..."
  windows: "..."
  door: "..."

fixed_elements:
  - "..."

practical_lights:
  - "..."

acoustic_signature:
  - "..."

atmosphere:
  - "..."

forbidden_changes:
  - "..."

variations_through_film:
  - "SC01: ..."
  - "SC02: ..."
```

---

## 5. Lighting & Atmosphere

```yaml
scene_range: "[...]"
overall_scheme: "..."

key_light_signature:
  primary_source: "..."
  direction: "..."
  color_temperature_k: [K]

fill_light_signature:
  primary_source: "..."
  intensity_ratio: "..."

rim_light_signature:
  primary_source: "..."
  direction: "..."
  color_temperature_k: [K]

contrast_ratio: "..."

practical_lights_in_scene:
  - source: "..."
    position: "..."
    color_temp: "[K]"

atmosphere:
  - element: "..."
    behavior: "..."

color_temperature_mix: "..."

forbidden_lighting:
  - "..."

time_consistency:
  note: "..."
  exceptions: "..."
```

---

## 6. Camera & Lens Grammar

```yaml
default_lens: "..."
default_aperture: "..."
default_dof: "..."
default_height: "..."
default_motion: "..."

allowed_lens_range: "..."
forbidden_lenses:
  - "..."

allowed_motions:
  - "..."
forbidden_motions:
  - "..."

sensor_format: "..."
film_stock: "..."
frame_rate: "..."

focus:
  default: "..."

color_grade_signature:
  shadows: "..."
  midtones: "..."
  highlights: "..."
  saturation: "..."
  contrast: "..."

forbidden_camera_practices:
  - "..."

cinematography_references:
  - "..."
```

---

## 7. Sound Signature

```yaml
scene_range: "[...]"

ambience_baseline:
  primary: "..."
  elements: [...]
  volume_db: -XX
  consistency: "..."

foley_baseline:
  primary: "..."
  elements: [...]

sfx_signature:
  primary: "..."
  key_sounds: [...]
  forbidden_sounds: [...]

music_signature:
  primary: "..."
  presence: "..."
  style: "..."
  structure: "..."
  volume_with_dialogue: -XX
  volume_without_dialogue: -XX

silence_points: [...]

language: "ar / en / ..."
dialect: "..."

voice_direction:
  protagonist:
    pace: "..."
    tone: "..."
    accent: "..."

forbidden_audio:
  - "..."
```

---

## 8. Color Palette

```yaml
primary:
  - name: "..."
    hex: "#..."
    usage: "..."

secondary:
  - name: "..."
    hex: "#..."
    usage: "..."

accent:
  - name: "..."
    hex: "#..."
    usage: "..."

forbidden:
  - "..."

color_script_map:
  "SC01": "..."
  "SC02": "..."
  ...
```

---

## 9. ملاحظات الإصدار

```yaml
changelog:
  - version: "v1.0"
    date: "[ISO]"
    changes:
      - "Initial creation"
  - version: "v1.1"
    date: "[ISO]"
    changes:
      - "..."
```

---

## 10. Cross-References

- Production Blueprint: `schemas/production-blueprint.md`
- Frame Chain: `schemas/state/frame-chain.md`
- Image Prompts: `schemas/image-prompts-package.md`
- Motion Prompts: `schemas/motion-prompts-package.md`
- Audio Package: `schemas/audio-package.md`
- Assembly Guide: `schemas/assembly-guide.md`

---

> **حالة التعبئة:**
> - [ ] Identity (شخصيات)
> - [ ] Wardrobe (ملابس)
> - [ ] Props (دعائم)
> - [ ] Locations (أماكن)
> - [ ] Lighting & Atmosphere
> - [ ] Camera & Lens Grammar
> - [ ] Sound Signature
> - [ ] Color Palette
