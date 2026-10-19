---
name: orchestration-runtime
description: |
  قابل للتنفيذ specification لـ 9 مسارات إنتاج. يحدد لكل مسار:
  route (intent + entry/target state)، load_context، run (ordered workflows +
  skip conditions)، validate (quality gates)، commit (state files).
  المرجع الرسمي للـ Runtime: `references/protocols/production-state-machine.md`.
  مرجع المسارات: `workflows/intent-router.md`.
tier: 3
when_to_load: "عند بدء مشروع جديد، أو عند الشك في ترتيب تنفيذ workflow معين"
---

# Orchestration Runtime — AI Film Studio v2.0.2

> **هذا الملف هو الـ executable spec للـ orchestration layer.** يحدد لكل intent:
> ما يُحمَّل (state)، ما يُنفَّذ (workflows)، ما يُفحص (gates)، ما يُحدَّث (commits).
>
> **لا تتجاوز هذا الملف بـ "توليد حر".** اتبع الترتيب المنطقي والـ skip conditions.

---

## المسار 1: REPAIR (إصلاح)

```yaml
route:
  intent: REPAIR
  entry_state: existing_project_with_failed_or_broken_shot
  target_state: shot_pass_or_replaced
  trigger: "المستخدم يذكر عطل محدد (هوية مكسورة، نص مشوّه، حركة خاطئة)"

load_context:
  required_state:
    - "schemas/state/asset-registry.md"
    - "schemas/state/decision-log.md"
    - "schemas/state/quality-gates-log.md"
  optional_state:
    - "schemas/state/frame-chain.md"
    - "schemas/state/continuity-ledger.md"
  source_of_truth: "schemas/state/asset-registry.md (shot_id + failure_class)"

run:
  ordered_workflows:
    - "M9c-preflight.md"           # تشخيص: أي Gate فشل، ما المتغير المسؤول
    - "[target_workflow]"           # e.g. M7b, M8a, M4a (حسب الـ asset)
  parallelizable_workflows: []
  skip_conditions:
    - "لا تحتاج M0 (intake) — المشروع موجود"
    - "لا تحتاج M1-M2-M3 (creative/narrative/shot design) — هذه مكتملة"

validate:
  required_quality_gates:
    - "G4 (Prompt Quality) — إن كان الإصلاح في prompt"
    - "G3 (Continuity) — إن كان الإصلاح في continuity"
    - "G6 (Text) — إن كان الإصلاح في نص"
  hard_fail_conditions:
    - "Identity String مكسور بعد الإصلاح"
    - "Chain break غير مُبرَّر"
  repair_route: "M9c → أصلح المتغير الأصغر → M9c مرة أخرى"

commit:
  state_files_to_update:
    - "schemas/state/asset-registry.md (attempt + status)"
    - "schemas/state/generation-log.md"
    - "schemas/state/decision-log.md (قرار الإصلاح)"
  outputs_to_register: "asset جديد أو asset مُعدَّل"
  checkpoint_rules: "لا تتجاوز الإصلاح إلى الإعادة التامة؛ طبّق الحد الأدنى"
```

---

## المسار 2: SINGLE_PROMPT (برومبت واحد)

```yaml
route:
  intent: SINGLE_PROMPT
  entry_state: user_asks_one_prompt
  target_state: one_prompt_with_10_layers
  trigger: '"اكتب برومبت واحد"، "prompt لـ..."، "give me a prompt"'

load_context:
  required_state: []
  optional_state:
    - "schemas/state/project-memory.md" (إن وُجد مشروع سابق)
  source_of_truth: "prompt-architecture.md"

run:
  ordered_workflows:
    - "workflows/shortcuts/single-prompt.md"
  parallelizable_workflows: []
  skip_conditions:
    - "تخطَّ M0 إذا كان الطلب واضحًا (لا أسئلة)"
    - "تخطَّ M1-M11 ما عدا M7a"

validate:
  required_quality_gates:
    - "G4 (Prompt Quality) — 10 طبقات A-J"
  hard_fail_conditions:
    - "prompt يحوي كلمة ممنوعة (beautiful, cinematic, stunning, etc.)"
    - "prompt ينقصه 3+ طبقات"
  repair_route: "M7a-prompt-architecture → إصلاح → M9c preflight"

commit:
  state_files_to_update:
    - "(اختياري) schemas/state/asset-registry.md"
  outputs_to_register: "prompt واحد"
  checkpoint_rules: "إذا أصبح المشروع أكثر من prompt، انتقل لـ SHOT_BUILD"
```

---

## المسار 3: IMAGE_GENERATION (صورة/فريم واحد)

```yaml
route:
  intent: IMAGE_GENERATION
  entry_state: user_wants_one_image
  target_state: one_image_prompt_ready_to_generate
  trigger: '"صورة لـ..."، "سوّ لي صورة"، "generate image"'

load_context:
  required_state: []
  optional_state:
    - "schemas/state/project-memory.md"
  source_of_truth: "prompt-architecture.md + model-matrix.md"

run:
  ordered_workflows:
    - "workflows/shortcuts/image-generation.md"
  parallelizable_workflows: []
  skip_conditions:
    - "تخطَّ M1-M6 ما عدا M7a"

validate:
  required_quality_gates:
    - "G4 (Prompt Quality)"
    - "G5 (Model compatibility — aspects, sizes, refs)"
  hard_fail_conditions:
    - "model لا يدعم aspect_ratio المطلوب"
    - "negative_prompts مطلوبة لكن غائبة"
  repair_route: "M7a → M9c preflight → توليد"

commit:
  state_files_to_update:
    - "schemas/state/asset-registry.md (image_id + status)"
  outputs_to_register: "image asset"
  checkpoint_rules: "لا M4c ما لم يكن هناك مشروع متعدد اللقطات قائم"
```

---

## المسار 4: IMAGE_TO_VIDEO (تحريك صورة موجودة)

```yaml
route:
  intent: IMAGE_TO_VIDEO
  entry_state: user_has_image_and_wants_motion
  target_state: motion_prompt_ready + first/last_frame_locked
  trigger: '"حرّك هذه الصورة"، "animate this"، "حوّلها فيديو"'

load_context:
  required_state:
    - "schemas/state/asset-registry.md (image_id)"
  optional_state:
    - "schemas/state/frame-chain.md (إن كانت image في chain)"
  source_of_truth: "asset-registry.md (image reference)"

run:
  ordered_workflows:
    - "workflows/shortcuts/image-to-video.md"
  parallelizable_workflows: []
  skip_conditions:
    - "تخطَّ M1-M5 (لا concept جديد)"
    - "تخطَّ M6 (لا audio افتراضيًا)"

validate:
  required_quality_gates:
    - "G4 (Motion Prompt Quality — 10 layers + G motion)"
    - "G3 (Continuity — first_frame = image_anchor)"
  hard_fail_conditions:
    - "first_frame لا يطابق image المرجعية"
    - "حركة كاميرا + zoom + orbit في لقطة واحدة"
  repair_route: "M8a → M9c preflight → generation"

commit:
  state_files_to_update:
    - "schemas/state/asset-registry.md (motion_id)"
    - "schemas/state/frame-chain.md (إن كان في chain)"
  outputs_to_register: "video asset"
  checkpoint_rules: "أول motion يُسجَّل في frame-chain تلقائيًا"
```

---

## المسار 5: MOTION_GRAPHICS (موشن جرافيك / تايبوجرافي)

```yaml
route:
  intent: MOTION_GRAPHICS
  entry_state: user_wants_animated_text_or_kinetic_typography
  target_state: motion_graphics_package + text_layers_separated
  trigger: '"موشن تايبوجرافي"، "حركة نص"، "kinetic typography"'

load_context:
  required_state: []
  optional_state:
    - "schemas/state/project-memory.md"
  source_of_truth: "M8d-motion-graphics.md + copywriting-and-text-in-images.md"

run:
  ordered_workflows:
    - "workflows/shortcuts/motion-graphics.md"
    - "M8d-motion-graphics.md"
  parallelizable_workflows: []
  skip_conditions:
    - "تخطَّ M1-M4 ما عدا M4a (لو فيه character)"
    - "تخطَّ M6 (audio مدمج في motion graphics)"

validate:
  required_quality_gates:
    - "G4 (Prompt Quality)"
    - "G6 (Text Quality — حرجة للموشن)"
  hard_fail_conditions:
    - "نص عربي في video prompt بدون EXACT ARABIC TEXT"
    - "easing في video generation prompt"
    - "Hero < 0.8s على الشاشة"
  repair_route: "M8d → M5b (text strategy) → M9c"

commit:
  state_files_to_update:
    - "schemas/state/asset-registry.md"
  outputs_to_register: "motion_graphics_asset + text_layers"
  checkpoint_rules: "النص يتحرك في compositing (After Effects) لا في video generation"
```

---

## المسار 6: DIALOGUE_LIPSYNC (حوار / شفاه متحركة)

```yaml
route:
  intent: DIALOGUE_LIPSYNC
  entry_state: user_has_character_and_dialogue
  target_state: lipsync_video_with_synced_audio
  trigger: '"حوار بالعربي"، "lip-sync"، "شفاه متحركة"'

load_context:
  required_state:
    - "character_reference (image أو video)"
    - "dialogue_text (نص + لهجة)"
  optional_state:
    - "voice_clone_id"
  source_of_truth: "M6c-dialogue-lipsync.md + model-matrix.md (Veo 3 native / Hedra)"

run:
  ordered_workflows:
    - "workflows/shortcuts/dialogue-lipsync.md"
    - "M6c-dialogue-lipsync.md"
    - "M6b-sound-design.md (voice)"
  parallelizable_workflows:
    - "M6 + M6b (يمكن بالتوازي إذا أُعدّ الصوت مسبقًا)"
  skip_conditions:
    - "تخطَّ M1-M5 ما عدا M4a (Identity Lock)"

validate:
  required_quality_gates:
    - "G7 (Audio Quality)"
    - "G3 (Continuity — face identity locked)"
  hard_fail_conditions:
    - "هوية الوجه تختلف بين shots"
    - "الحوار داخل علامتي اقتباس في Seedance"
  repair_route: "M6c → M9c preflight → generation"

commit:
  state_files_to_update:
    - "schemas/state/asset-registry.md (lipsync_id)"
  outputs_to_register: "lipsync_video + voice_audio"
  checkpoint_rules: "voice_clone_id يُسجَّل في decision-log"
```

---

## المسار 7: CONCEPT_ONLY (فكرة فقط)

```yaml
route:
  intent: CONCEPT_ONLY
  entry_state: user_has_idea_wants_concept_only
  target_state: concept_deck + logline + visual_metaphor
  trigger: '"عندي فكرة، حوّلها concept"، "ابني concept deck"'

load_context:
  required_state: []
  optional_state: []
  source_of_truth: "M1a-creative-direction.md + M1b-concept-expansion.md"

run:
  ordered_workflows:
    - "workflows/shortcuts/concept-only.md"
    - "M1a-creative-direction.md"
    - "M1b-concept-expansion.md"
  parallelizable_workflows:
    - "M1a + M1b يمكن بالتوازي"
  skip_conditions:
    - "تخطَّ M2-M11 (لا narrative، لا shots، لا prompts)"

validate:
  required_quality_gates:
    - "G1 (Idea Quality)"
  hard_fail_conditions:
    - "logline ينقصه 3 من 4: شخصية + رغبة + عائق + ثمن"
    - "visual_metaphor = 'غير محدد'"
  repair_route: "M1b → إعادة صياغة logline"

commit:
  state_files_to_update:
    - "schemas/state/project-memory.md (concept فقط)"
  outputs_to_register: "concept_deck"
  checkpoint_rules: "إذا طلب المستخدم prompt، انتقل لـ SINGLE_PROMPT"
```

---

## المسار 8: SHOT_BUILD (لقطة واحدة في مشروع قائم)

```yaml
route:
  intent: SHOT_BUILD
  entry_state: existing_project_user_wants_one_shot
  target_state: one_shot_prompts_ready
  trigger: '"أضف لقطة"، "سوّ لقطة واحدة"، "shot from existing project"'

load_context:
  required_state:
    - "schemas/state/project-memory.md"
    - "schemas/state/continuity-bible.md (إن وُجد)"
    - "schemas/state/frame-chain.md"
  optional_state:
    - "schemas/state/character-world.md"
  source_of_truth: "project-memory.md + continuity-bible.md"

run:
  ordered_workflows:
    - "M4e-reference-orchestration.md (إن كان المرجع/الكيان جديدًا؛ وإلا حمّل manifest القائم)"
    - "M3a-shot-design.md (shot card فقط)"
    - "M4a-continuity.md (تحديث bible)"
    - "M4c-continuity-qc.md (MANDATORY — تحقق أن اللقطة لا تكسر chain)"
    - "M7b-image-prompts.md"
    - "M8a-motion-prompts.md"
  parallelizable_workflows:
    - "M7b + M8a (يمكن بالتوازي)"
  skip_conditions:
    - "تخطَّ M0 (السياق معروف)"
    - "تخطَّ M1-M2 (concept + narrative موجود)"
    - "تخطَّ M5-M6 (graphics + audio تُضاف فقط عند الحاجة)"

validate:
  required_quality_gates:
    - "G3 (Continuity) — first_frame = last_frame of previous shot"
    - "G4 (Prompt Quality) — 10 layers A-J"
    - "M4c إلزامي في SHOT_BUILD"
  hard_fail_conditions:
    - "chain break غير مُبرَّر"
    - "Identity String لا يطابق bible"
  repair_route: "M9c preflight → إصلاح → M4c مرة أخرى → M9c"

commit:
  state_files_to_update:
    - "schemas/state/frame-chain.md (اللقطة الجديدة)"
    - "schemas/state/continuity-bible.md (إن تغيّر شيء)"
    - "schemas/state/asset-registry.md"
    - "schemas/state/decision-log.md"
  outputs_to_register: "shot_card + image_prompt + motion_prompt"
  checkpoint_rules: "اسأل: هل اللقطة تتطلب APPROVAL؟ (نعم إن كانت حاسمة)"
```

---

## المسار 9: SCENE_BUILD (مشهد متعدد اللقطات)

```yaml
route:
  intent: SCENE_BUILD
  entry_state: user_wants_complete_scene
  target_state: scene_with_3_8_shots
  trigger: '"مشهد"، "scene"، "سوّ مشهد كامل"'

load_context:
  required_state:
    - "schemas/state/project-memory.md"
  optional_state:
    - "schemas/state/continuity-bible.md (إن وُجد)"
  source_of_truth: "project-memory.md"

run:
  ordered_workflows:
    - "M0-intake.md (محدود — context refresh فقط)"
    - "M4e-reference-orchestration.md (CAST/ENTITIES ثم anchors ثم shot_reference_map)"
    - "M1c-research-lab.md (concept refresh إن لزم)"
    - "M2-narrative.md (scene في story)"
    - "M3a-shot-design.md + M3b-shot-list.md"
    - "M4a-continuity.md + M4b-character-world.md + M4c-continuity-qc.md (MANDATORY)"
    - "M4d-transitions.md"
    - "M5a-graphics.md (إن وُجد نص)"
    - "M6-audio.md (إن وُجد حوار/موسيقى)"
    - "M7a-prompt-architecture.md + M7b-image-prompts.md"
    - "M8a-motion-prompts.md"
    - "M9b-quality-gates.md (G3 + G4)"
    - "M9c-preflight.md (قبل التوليد)"
  parallelizable_workflows:
    - "M5a + M6 (graphics + audio — بعد script)"
    - "M7b لكل shot (متوازي)"
  skip_conditions:
    - "تخطَّ M10-M11 (delivery على مستوى المشروع الكامل)"

validate:
  required_quality_gates:
    - "G1 (Concept)"
    - "G2 (Narrative)"
    - "G3 (Continuity) — M4c إلزامي"
    - "G4 (Prompts)"
    - "G5 (Transitions)"
    - "G6 (Text) — إن وُجد نص"
    - "G7 (Audio) — إن وُجد صوت"
  hard_fail_conditions:
    - "G4 fail → REJECT prompt"
    - "G3 fail + chain break → REJECT scene"
    - "G-APPROVAL (user) قبل بدء generation"
  repair_route: "G-APPROVAL → FAIL → ارجع لـ M المناسبة → REPAIR"

commit:
  state_files_to_update:
    - "schemas/state/frame-chain.md (كامل للمشهد)"
    - "schemas/state/continuity-bible.md (محدّث)"
    - "schemas/state/asset-registry.md (كل assets المشهد)"
    - "schemas/state/decision-log.md"
    - "schemas/state/quality-gates-log.md"
  outputs_to_register: "scene_package (blueprint section + prompts)"
  checkpoint_rules: "G-APPROVAL إلزامي بعد M4c وقبل M7"
```

---

## المسار 10: FULL_PRODUCTION (فيلم/إعلان كامل)

```yaml
route:
  intent: FULL_PRODUCTION
  entry_state: user_wants_full_film_or_ad
  target_state: 5_output_files_complete
  trigger: '"فيلم كامل"، "إعلان 30s"، "full production"، "أفلام متعدد المشاهد"'

load_context:
  required_state: []
  optional_state:
    - "schemas/state/project-memory.md (مشروع سابق — للـ continuation)"
  source_of_truth: "production-state-machine.md (المرجع الرسمي)"

run:
  ordered_workflows:
    - "M0-intake.md"
    - "M1a-creative-direction.md + M1b-concept-expansion.md + M1c-research-lab.md"
    - "G-APPROVAL (Concept Deck)"
    - "M2-narrative.md"
    - "G-APPROVAL (Script — إن وُجد حوار)"
    - "M4e-reference-orchestration.md (CAST/ENTITIES ثم anchors ثم shot_reference_map)"
    - "G-APPROVAL (Reference Pack)"
    - "M3a-shot-design.md + M3b-shot-list.md"
    - "M4a-continuity.md + M4b-character-world.md + M4c-continuity-qc.md (MANDATORY)"
    - "M4d-transitions.md"
    - "G-APPROVAL (Pre-Production)"
    - "M5a-graphics.md + M5b-text-motion.md"
    - "M6-audio.md + M6b-sound-design.md + M6c-dialogue-lipsync.md"
    - "M7a-prompt-architecture.md + M7b-image-prompts.md"
    - "M8a-motion-prompts.md + M8b-motion-direction.md + M8c-animation-ready.md + M8d-motion-graphics.md (إن وُجد)"
    - "M9a-executive-producer.md (تطبيق 8 gates)"
    - "M9b-quality-gates.md (G4 + G8 hard gates)"
    - "M9c-preflight.md (قبل كل generation)"
    - "M9d-localization.md (إن كانت لغة غير الإنجليزية)"
    - "M10a-production-architecture.md + M10b-hybrid-assembly.md + M10c-edit-color.md"
    - "G-APPROVAL (Final)"
    - "M11a-reference-analyst.md + M11b-visual-research.md"
  parallelizable_workflows:
    - "M5a + M6 بعد M2"
    - "M7b لكل shot"
    - "M8a لكل shot (بعد M7b)"
  skip_conditions:
    - "لا skip في FULL_PRODUCTION — كل workflow يجب أن يُنفَّذ"
    - "ما يمكن تخطيه: M8d (motion graphics) إن لم يكن في المشروع motion graphics"

validate:
  required_quality_gates:
    - "G0 (Intake)"
    - "G1 (Idea)"
    - "G2 (Narrative)"
    - "G3 (Continuity) — M4c MANDATORY"
    - "G4 (Prompts) — HARD GATE"
    - "G5 (Transitions)"
    - "G6 (Text) — M5 MANDATORY"
    - "G7 (Audio) — M6 MANDATORY"
    - "G8 (Master) — HARD GATE — 5 output files complete"
  hard_fail_conditions:
    - "أي G4 fail → REJECT prompt"
    - "أي G8 fail → REJECT project"
    - "M4c غير منفَّذ → REJECT scene"
    - "مرجع متكرر بلا anchor_id أو @image بلا role → REJECT scene/project"
  repair_route: "FAIL → DIAGNOSE → REPAIR → REVALIDATE → PASS"

commit:
  state_files_to_update:
    - "schemas/state/frame-chain.md (كامل)"
    - "schemas/state/continuity-bible.md (مكتمل)"
    - "schemas/state/asset-registry.md (كامل)"
    - "schemas/state/decision-log.md (مكتمل)"
    - "schemas/state/quality-gates-log.md (مكتمل)"
    - "schemas/state/risk-register.md (مكتمل)"
    - "schemas/state/project-memory.md (COMPLETED)"
  outputs_to_register:
    - "01-production-blueprint.md"
    - "02-image-prompts-package.md"
    - "03-motion-prompts-package.md"
    - "04-audio-package.md"
    - "05-assembly-guide.md"
  checkpoint_rules:
    - "3 اعتمادات بشرية إلزامية: بعد M1 (concept)، بعد M2 (script إن وُجد حوار)، بعد M10 (final)"
    - "session-checkpoint يُحدَّث بعد كل M-stage"
```

---

## خريطة المسارات (نفس ترتيب intent-router)

| # | intent | أول workflow | آخر workflow | Approvals |
|---|---|---|---|---|
| 1 | REPAIR | M9c | M9c | 0 |
| 2 | SINGLE_PROMPT | shortcuts/single-prompt | M7a | 0 |
| 3 | IMAGE_GENERATION | shortcuts/image-gen | M7a → M9c | 0 |
| 4 | IMAGE_TO_VIDEO | shortcuts/i2v | M8a → M9c | 0 |
| 5 | MOTION_GRAPHICS | shortcuts/motion-gfx | M8d → M9c | 0 |
| 6 | DIALOGUE_LIPSYNC | shortcuts/lipsync | M6c → M9c | 0 |
| 7 | CONCEPT_ONLY | shortcuts/concept | M1b | 0 |
| 8 | SHOT_BUILD | M3a | M9c | 0–1 |
| 9 | SCENE_BUILD | M0 (refresh) | M9c | 1 (G-APPROVAL بعد M4c) |
| 10 | FULL_PRODUCTION | M0 | M11 | 3 (concept, script, final) |

---

## قواعد عامة (لكل المسارات)

1. **M4c إلزامي** في SHOT_BUILD، SCENE_BUILD، FULL_PRODUCTION.
2. **M4c اختياري** في SINGLE_PROMPT، IMAGE_GENERATION، IMAGE_TO_VIDEO، MOTION_GRAPHICS، DIALOGUE_LIPSYNC، CONCEPT_ONLY (لا يوجد multi-shot).
3. **M9c preflight إلزامي** قبل أي generation فعلي.
    4. **G-APPROVAL لحزمة المرجعيات إلزامي** في SCENE_BUILD وFULL_PRODUCTION قبل M3؛ وG-APPROVAL آخر بعد M4c وقبل M5 في FULL_PRODUCTION.
5. **G4 و G8 hard gates** — لا يتجاوزان.
6. **Backward compat**: v1.x paths تعمل كما هي (LLM يفسر القديم).
7. **Source of truth**: `production-state-machine.md` (المراحل)، `references/specs/prompt-architecture.md` (10 طبقات)، `references/specs/model-matrix.md` (النماذج).
