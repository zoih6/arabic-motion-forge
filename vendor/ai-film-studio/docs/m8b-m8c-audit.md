---
name: m8b-m8c-audit
description: |
  Audit قرار M8b (Motion Direction) و M8c (Animation Ready) في v2.1.0.
  يحدد بوضوح: لكل منهما Input/Output Contract مستقل.
  مرتبط بـ: `workflows/M8a-motion-prompts.md`، `workflows/M7b-image-prompts.md`.
tier: 3
when_to_load: "عند التشكيك في ضرورة M8b أو M8c، أو عند التخطيط لإعادة هيكلة"
---

# M8b / M8c Audit — v2.1.0

## السؤال
هل M8b و M8c يستحقان ملفًا مستقلاً، أم يُدمجان في M8a / M7b؟

## النتيجة: الإبقاء على الاثنين

## Contract لكل واحد

### M8b — Motion Direction
- **الموقع في Pipeline:** بعد M3a (Shot Design)، قبل M8a (Motion Prompts).
- **Input:** shot_cards (من M3a) + continuity_bible (من M4a).
- **Output:** `motion_direction_sheet` (5 حقول):
  1. `dominant_action` (فعل واحد، اتجاه، نقطة نهاية)
  2. `camera_movement` (حركة مهيمنة واحدة)
  3. `performance_beats` (3 beats: بداية → وسط → نهاية)
  4. `environment_response` (physics: cloth, dust, hair, ...)
  5. `end_state` (تركيب final للقطع القادم)
- **الفائدة:** يفصل "تصميم الحركة" (إبداعي) عن "كتابة prompt الحركة" (تقني).
- **Decision:** ✅ contract مستقل، الإبقاء.

### M8c — Animation Ready
- **الموقع في Pipeline:** بعد M4a (Continuity Bible)، قبل M7b (Image Prompts).
- **Input:** shot_cards (من M3a) + scene_dna + character_anchors.
- **Output:** `animation_ready_asset_card` (12 حقل):
  1. `asset_id`
  2. `frame_role` (start / end / identity_ref / prop_plate)
  3. `shot_size` + camera angle
  4. `subject_mask`
  5. `protected_zones` (face, hands, text, logo, props)
  6. `motion_corridor`
  7. `anchor_points` (eyes, shoulders, hand, product, horizon)
  8. `depth_layers` (FG / MG / BG)
  9. `lighting_lock`
  10. `text_policy` (burn-in vs compositing)
  11. `end_state`
  12. `pre_motion_test` (هل الفريم جاهز للحركة؟)
- **الفائدة:** يفصل "هندسة الأصل للتحريك" (تقني) عن "كتابة prompt الصورة" (إبداعي).
- **Decision:** ✅ contract مستقل، الإبقاء.

## ملخص

- M8b = Motion Direction (creative spec للحركة) — قبل M8a.
- M8c = Animation Ready (technical spec للأصل) — قبل M7b.
- لا تداخل، لا ازدواجية.
- **القرار النهائي:** الإبقاء منفصلين.
