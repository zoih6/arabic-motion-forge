# state/frame-chain.md

> **Frame Chain Registry: سجل كل Start/End Frame بين اللقطات.**
> **يُملأ ويُحدَّث من قبل `workflows/M4c-continuity-qc.md`.**

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

## ملخص السلسلة (Chain Summary)

```yaml
chain_summary:
  total_shots: [N]
  chain_breaks: [N]
  status: "[complete / partial / has_breaks]"
  break_reasons: []
```

---

## السلسلة الكاملة (Full Chain)

```yaml
frame_chain:
  
  - shot_id: "SC01_SH01"
    type: "establishing"
    start_frame:
      id: "FRAME-001"
      description: "[...]"
      key_elements:
        position: "[...]"
        composition: "[...]"
        lighting: "[...]"
        subject_state: "[...]"
        missing_for_chain: "no (opening)"
      reference_image: "[path or null]"
      reference_lock: "no_anchor"
    
    end_frame:
      id: "FRAME-002"
      description: "[...]"
      key_elements:
        position: "[...]"
        composition: "[...]"
        lighting: "[...]"
        subject_state: "[...]"
        hand_state: "[...]"
        eye_state: "[...]"
      reference_image: "[path or null]"
      reference_lock: "anchor_for_SC01_SH02"
    
    chain_status: "complete"
    next_shot: "SC01_SH02"
    next_start_matches: "FRAME-002 (exact match)"
  
  - shot_id: "SC01_SH02"
    type: "main"
    start_frame:
      id: "FRAME-003"
      description: "[same as FRAME-002]"
      key_elements: [...]
      reference_image: "[path or null]"
      reference_lock: "anchor_from_SC01_SH01"
      match_with: "FRAME-002"
    
    end_frame:
      id: "FRAME-004"
      description: "[...]"
      key_elements: [...]
      reference_lock: "anchor_for_SC01_SH03"
    
    chain_status: "complete"
    next_shot: "SC01_SH03"
    next_start_matches: "FRAME-004 (exact match)"
  
  - shot_id: "SC01_SH03"
    type: "main"
    start_frame: [...]
    end_frame: [...]
    chain_status: "complete"
    next_shot: "..."
  
  # ... باقي اللقطات
  
  - shot_id: "SCXX_SHXX"
    type: "ending"
    start_frame: [...]
    end_frame: [...]
    chain_status: "complete"
    next_shot: null  # آخر لقطة
    next_start_matches: null
```

---

## Chain Breaks (كسور السلسلة الموثقة)

```yaml
chain_breaks:
  
  - id: "BREAK-01"
    between:
      from_shot: "SC03_SH02"
      to_shot: "SC04_SH01"
    reason: "time_jump"
    reason_description: "انتقال زمني من نهار إلى مساء"
    coverage: "..."
    visual_bridge:
      - "تغير الإضاءة (daylight → dusk)"
      - "تغير الملابس"
    acceptable: true
    note: "مقصود، يخدم القصة"
  
  - id: "BREAK-02"
    between:
      from_shot: "..."
      to_shot: "..."
    reason: "..."
    ...
```

---

## مطابقة الإطارات (Frame Matching)

### أنواع المطابقة

```yaml
matching_types:
  
  exact_match:
    description: "نفس التكوين، الإضاءة، الشخصية"
    when: "cut مباشر"
    success_rate_target: "95%+"
  
  action_match:
    description: "حركة تكمل في اللقطة التالية"
    when: "match on action"
    success_rate_target: "90%+"
  
  mood_match:
    description: "نفس الإضاءة والعاطفة"
    when: "cross-cut"
    success_rate_target: "85%+"
  
  graphic_match:
    description: "شكل/نمط/لون يتكرر"
    when: "transiciones إبداعية"
    success_rate_target: "80%+"
  
  eyeline_match:
    description: "اتجاه النظر محفوظ"
    when: "قطع بين شخصيات"
    success_rate_target: "90%+"
  
  position_match:
    description: "الشخصية في نفس موقع الكادر"
    when: "قطع بين شخصيات"
    success_rate_target: "85%+"
  
  sound_bridge:
    description: "صوت يربط"
    when: "تداعي، حلم"
    success_rate_target: "100% (audio only)"
  
  color_match:
    description: "اللون يربط"
    when: "transiciones إبداعية"
    success_rate_target: "85%+"
```

---

## سجل الكسور (Break Log)

```yaml
break_log:
  - break_id: "BREAK-01"
    severity: "intentional"
    type: "time_jump"
    between: ["SC03_SH02", "SC04_SH01"]
    handled_in: "transitions: fade to black + title card"
    status: "approved"
  
  - break_id: "BREAK-02"
    severity: "intentional"
    type: "place_jump"
    between: ["SC05_SH03", "SC06_SH01"]
    handled_in: "transitions: match cut (outdoor → indoor)"
    status: "approved"
```

---

## Image Anchors (المرجعيات)

```yaml
image_anchors:
  
  character_anchors:
    - character_id: "CHAR-01"
      anchor_paths:
        - "assets/anchors/char-01_v2.png"
        - "assets/anchors/char-01_profile.png"
        - "assets/anchors/char-01_three_quarter.png"
      used_in_shots: ["SC01_SH02", "SC01_SH03", "SC02_SH01", ...]
  
  wardrobe_anchors:
    - character_id: "CHAR-01"
      anchor_paths:
        - "assets/anchors/ward-01_v1.png"
      used_in_shots: ["SC01_SH02", ...]
  
  prop_anchors:
    - prop_id: "PROP-01"
      anchor_paths:
        - "assets/anchors/prop-01_v1.png"
      used_in_shots: ["SC01_SH01", "SC01_SH02", ...]
  
  location_anchors:
    - location_id: "LOC-01"
      anchor_paths:
        - "assets/anchors/loc-01_v2.png"
        - "assets/anchors/loc-01_alt.png"
      used_in_shots: ["SC01_SH01", "SC01_SH02", ...]
  
  frame_anchors:
    - frame_id: "FRAME-001"
      anchor_paths:
        - "assets/anchors/frame-001_v1.png"
      used_in_shots: ["SC01_SH01"]
    - frame_id: "FRAME-002"
      anchor_paths:
        - "assets/anchors/frame-002_v1.png"
      used_in_shots: ["SC01_SH01 (end) + SC01_SH02 (start)"]
```

---

## Audit Summary

```yaml
audit:
  last_audit_date: "[ISO]"
  last_auditor: "25-continuity-supervisor + 31-quality-gate"
  overall_score: 0-100
  per_shot_scores:
    - shot_id: "SC01_SH01"
      score: 95
      issues: []
    - shot_id: "SC01_SH02"
      score: 90
      issues: ["hand_state: slight inconsistency, fixed in v3"]
    - ...
  
  chain_breaks_unintended: 0
  chain_breaks_intentional: 2
  total_chain_completeness: "98%"
```

---

## Cross-References

- Production Blueprint: `schemas/production-blueprint.md`
- Continuity Bible: `schemas/state/continuity-bible.md`
- Image Prompts: `schemas/image-prompts-package.md`
- Motion Prompts: `schemas/motion-prompts-package.md`
- Asset Registry: `schemas/state/asset-registry.md`
- Decision Log: `schemas/state/decision-log.md`

---

> **حالة التعبئة:**
> - [ ] Chain Summary
> - [ ] Full Chain (لكل shot)
> - [ ] Chain Breaks (إن وُجدت)
> - [ ] Frame Matching Types
> - [ ] Break Log
> - [ ] Image Anchors
> - [ ] Audit Summary
