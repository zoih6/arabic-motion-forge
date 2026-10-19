# state/quality-gates-log.md

> **سجل بوابات الجودة: G0–G8 لكل مشروع.**
> **يُملأ ويُحدَّث من قبل `workflows/M9b-quality-gates.md` و `workflows/M9a-executive-producer.md`.**

---

## معلومات المشروع

```yaml
project:
  id: "[PROJECT_ID]"
  title: "[اسم المشروع]"
  version: "v[X.Y]"
  status: "[IN_DEVELOPMENT / COMPLETE / BLOCKED]"
  last_updated: "[ISO timestamp]"
  updated_by: "30-executive-producer + 31-quality-gate"
```

---

## ملخص البوابات (Gates Summary)

```yaml
gates_summary:
  G0_intake_clarity: "[PASS / REQUIRES_REVIEW / FAIL]"
  G1_idea_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G2_narrative_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G3_continuity_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G4_prompt_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G5_transition_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G6_text_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G7_audio_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  G8_master_quality: "[PASS / REQUIRES_REVIEW / FAIL]"
  
  overall: "[PASS / REQUIRES_REVIEW / FAIL]"
  ready_for_delivery: "[true / false]"
  blocking_issues: []
```

---

## G0 — Intake Clarity

```yaml
G0:
  applied_after: "M0"
  applied_at: "[ISO timestamp]"
  agent_responsible: "30-executive-producer"
  
  criteria_results:
    G0_1_request_clear:
      status: "[PASS / FAIL]"
      notes: "..."
    G0_2_contradictions_identified:
      status: "[PASS / FAIL]"
      notes: "..."
    G0_3_duration_platform_audience_defined:
      status: "[PASS / FAIL]"
      notes: "..."
    G0_4_language_dialect_defined:
      status: "[PASS / FAIL]"
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  issues: []
  questions_for_user: []
  action_taken: "[approved / needs clarification / rejected]"
```

---

## G1 — Idea Quality

```yaml
G1:
  applied_after: "M1"
  applied_at: "[ISO timestamp]"
  agent_responsible: "21-creative-research-lab"
  
  criteria_results:
    G1_1_logline_clear:
      status: "[PASS / FAIL]"
      notes: "..."
    G1_2_visual_metaphor_specific:
      status: "[PASS / FAIL]"
      notes: "..."
    G1_3_5_axes_researched:
      status: "[PASS / FAIL]"
      notes: "..."
    G1_4_evaluation_matrix_completed:
      status: "[PASS / FAIL]"
      notes: "..."
    G1_5_selected_direction_justified:
      status: "[PASS / FAIL]"
      notes: "..."
    G1_6_cultural_anchors_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G1_7_concept_deck_complete:
      status: "[PASS / FAIL]"
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  selected_direction: "[DIR-01 or similar]"
  issues: []
  action_taken: "[approved / needs revision / rejected]"
```

---

## G2 — Narrative Quality

```yaml
G2:
  applied_after: "M3"
  applied_at: "[ISO timestamp]"
  agent_responsible: "23-narrative-architect"
  
  criteria_results:
    G2_1_story_structure_appropriate:
      status: "[PASS / FAIL]"
      notes: "..."
    G2_2_every_scene_has_purpose:
      status: "[PASS / FAIL]"
      notes: "..."
    G2_3_character_arc_defined:
      status: "[PASS / FAIL]"
      notes: "..."
    G2_4_emotional_beats_complete:
      status: "[PASS / FAIL]"
      notes: "..."
    G2_5_dialogue_rules_respected:
      status: "[PASS / FAIL]"
      notes: "..."
    G2_6_word_count_appropriate:
      status: "[PASS / FAIL]"
      actual_words: [N]
      max_words: [N]
      notes: "..."
    G2_7_transitions_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G2_8_stakes_conflict_defined:
      status: "[PASS / FAIL]"
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  script_word_count: [N]
  scene_count: [N]
  issues: []
  action_taken: "[approved / needs revision / rejected]"
```

---

## G3 — Continuity Quality

```yaml
G3:
  applied_after: "M5"
  applied_at: "[ISO timestamp]"
  agent_responsible: "25-continuity-supervisor"
  
  part_1_shot_architecture:
    G3_1_shot_cards_complete:
      status: "[PASS / FAIL]"
      notes: "..."
    G3_2_blocking_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G3_3_edit_handles_defined:
      status: "[PASS / FAIL]"
      notes: "..."
    G3_4_camera_grammar_consistent:
      status: "[PASS / FAIL]"
      notes: "..."
  
  part_2_continuity:
    G3_5_continuity_bible_seven_sections:
      status: "[PASS / FAIL]"
      notes: "..."
    G3_6_frame_chain_complete:
      status: "[PASS / FAIL]"
      chain_breaks: [N]
      notes: "..."
    G3_7_color_palette_defined:
      status: "[PASS / FAIL]"
      notes: "..."
    G3_8_image_anchors_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G3_9_audit_score_90_plus:
      status: "[PASS / FAIL]"
      actual_score: [N]
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  audit_score: [N]
  chain_breaks: [N]
  issues: []
  action_taken: "[approved / needs revision / rejected]"
```

---

## G4 — Prompt Quality (HARD GATE)

```yaml
G4:
  applied_after: "M8 (image) and M9 (motion)"
  applied_at: "[ISO timestamp]"
  agent_responsible: "22-prompt-architecture + 31-quality-gate"
  gate_type: "HARD GATE"
  
  per_prompt_results:
    - prompt_id: "IMG-SC01-SH01"
      status: "[PASS / FAIL]"
      layers_present: "10/10"
      identity_string_verified: "yes"
      abstract_words_removed: "yes"
      negative_prompts_present: "yes"
      reference_images_listed: "yes"
      word_count_appropriate: "yes (185 words)"
      model_specified: "yes"
      continuity_refs: "yes"
      notes: "..."
    
    - prompt_id: "..."
      status: "..."
  
  summary:
    total_prompts: [N]
    passed: [N]
    failed: [N]
    pass_rate: "[X%]"
  
  critical_failures: []
  high_failures: []
  medium_failures: []
  
  overall_status: "[PASS / FAIL]"
  rejected_prompts: []
  issues: []
  action_taken: "[approved / needs revision / rejected]"
  
  warning: "This is a HARD GATE. Any critical failure = FAIL."
```

---

## G5 — Transition Quality

```yaml
G5:
  applied_after: "M6"
  applied_at: "[ISO timestamp]"
  agent_responsible: "26-transition-engineer"
  
  criteria_results:
    G5_1_every_transition_has_reason:
      status: "[PASS / FAIL]"
      notes: "..."
    G5_2_alternatives_rejected_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G5_3_transitions_compatible_with_content:
      status: "[PASS / FAIL]"
      notes: "..."
    G5_4_risks_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G5_5_executable_in_models:
      status: "[PASS / FAIL]"
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  transition_count: [N]
  risky_transitions: []
  issues: []
  action_taken: "[approved / needs revision / rejected]"
```

---

## G6 — Text Quality

```yaml
G6:
  applied_after: "M6.5"
  applied_at: "[ISO timestamp]"
  agent_responsible: "27-graphic-typography-director + 28-text-preservation-motion"
  
  criteria_results:
    G6_1_every_text_has_strategy:
      status: "[PASS / FAIL]"
      notes: "..."
    G6_2_every_text_has_backup:
      status: "[PASS / FAIL]"
      notes: "..."
    G6_3_text_in_safe_areas:
      status: "[PASS / FAIL]"
      notes: "..."
    G6_4_brand_logo_post_overlay:
      status: "[PASS / FAIL]"
      weight: "critical"
      notes: "..."
    G6_5_safe_motion_patterns:
      status: "[PASS / FAIL]"
      notes: "..."
    G6_6_prompt_patterns_correct:
      status: "[PASS / FAIL]"
      notes: "..."
    G6_7_reference_images_for_critical_text:
      status: "[PASS / FAIL]"
      weight: "high"
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  text_elements: [N]
  critical_text_handling: "..."
  issues: []
  action_taken: "[approved / needs revision / rejected]"
```

---

## G7 — Audio Quality

```yaml
G7:
  applied_after: "M7"
  applied_at: "[ISO timestamp]"
  agent_responsible: "29-audio-decision-engine"
  
  criteria_results:
    G7_1_all_layers_documented:
      status: "[PASS / FAIL]"
      notes: "..."
    G7_2_audio_models_specified:
      status: "[PASS / FAIL]"
      notes: "..."
    G7_3_lipsync_planned:
      status: "[PASS / FAIL]"
      weight: "high"
      notes: "..."
    G7_4_master_lufs_per_platform:
      status: "[PASS / FAIL]"
      notes: "..."
    G7_5_ducking_planned:
      status: "[PASS / FAIL]"
      notes: "..."
    G7_6_mixing_plan_realistic:
      status: "[PASS / FAIL]"
      notes: "..."
    G7_7_post_production_steps_documented:
      status: "[PASS / FAIL]"
      notes: "..."
  
  overall_status: "[PASS / REQUIRES_REVIEW / FAIL]"
  layers: [N]
  lipsync_scenes: [N]
  issues: []
  action_taken: "[approved / needs revision / rejected]"
```

---

## G8 — Master Quality (HARD GATE)

```yaml
G8:
  applied_after: "M10"
  applied_at: "[ISO timestamp]"
  agent_responsible: "30-executive-producer + 31-quality-gate"
  gate_type: "HARD GATE"
  
  criteria_results:
    G8_1_5_output_files_complete:
      status: "[PASS / FAIL]"
      weight: "critical"
      files:
        - "01-production-blueprint.md: present"
        - "02-image-prompts-package.md: present"
        - "03-motion-prompts-package.md: present"
        - "04-audio-package.md: present"
        - "05-assembly-guide.md: present"
      notes: "..."
    
    G8_2_all_previous_gates_passed:
      status: "[PASS / FAIL]"
      weight: "critical"
      g0: "..."
      g1: "..."
      g2: "..."
      g3: "..."
      g4: "..."
      g5: "..."
      g6: "..."
      g7: "..."
      notes: "..."
    
    G8_3_decision_log_complete:
      status: "[PASS / FAIL]"
      notes: "..."
    
    G8_4_risk_register_updated:
      status: "[PASS / FAIL]"
      notes: "..."
    
    G8_5_cross_references_valid:
      status: "[PASS / FAIL]"
      notes: "..."
    
    G8_6_assembly_guide_executable:
      status: "[PASS / FAIL]"
      notes: "..."
    
    G8_7_time_estimate_realistic:
      status: "[PASS / FAIL]"
      notes: "..."
    
    G8_8_user_approvals_received:
      status: "[PASS / FAIL]"
      weight: "critical"
      approvals:
        concept: "[...]"
        script: "[...]"
        final: "[...]"
      notes: "..."
  
  overall_status: "[PASS / FAIL]"
  ready_for_delivery: "[true / false]"
  issues: []
  final_score: 0-100
  
  warning: "This is a HARD GATE. Any critical failure = FAIL."
```

---

## Final Status

```yaml
final_status:
  all_gates_passed: "[true / false]"
  total_issues: [N]
  blocking_issues: [N]
  approved_for_delivery: "[true / false]"
  approved_by: "user"
  approval_date: "[ISO]"
  
  final_summary: |
    [ملخص قصير: المشروع جاهز للتسليم / يحتاج إصلاحات / مرفوض]
```

---

## Audit Trail (السجل الزمني)

```yaml
audit_trail:
  - timestamp: "[ISO]"
    action: "G0 applied"
    result: "PASS"
    agent: "30-executive-producer"
  
  - timestamp: "[ISO]"
    action: "G1 applied"
    result: "PASS"
    agent: "21-creative-research-lab"
  
  - timestamp: "[ISO]"
    action: "G2 applied"
    result: "REQUIRES_REVIEW"
    issues: ["G2.6: word count exceeded"]
    resolution: "user approved +10s extension"
  
  - timestamp: "[ISO]"
    action: "G3 applied"
    result: "PASS"
    agent: "25-continuity-supervisor"
  
  - timestamp: "[ISO]"
    action: "G4 applied"
    result: "PASS"
    agent: "31-quality-gate"
  
  - timestamp: "[ISO]"
    action: "G5 applied"
    result: "PASS"
    agent: "26-transition-engineer"
  
  - timestamp: "[ISO]"
    action: "G6 applied"
    result: "PASS"
    agent: "27-graphic-typography-director"
  
  - timestamp: "[ISO]"
    action: "G7 applied"
    result: "PASS"
    agent: "29-audio-decision-engine"
  
  - timestamp: "[ISO]"
    action: "G8 applied"
    result: "PASS"
    agent: "30-executive-producer + 31-quality-gate"
  
  - timestamp: "[ISO]"
    action: "Final approval"
    result: "approved"
    approved_by: "user"
```

---

## Cross-References

- Production Blueprint: `schemas/production-blueprint.md`
- Continuity Bible: `schemas/state/continuity-bible.md`
- Frame Chain: `schemas/state/frame-chain.md`
- Risk Register: `schemas/state/risk-register.md`
- Decision Log: `schemas/state/decision-log.md`
- Project Memory: `schemas/state/project-memory.md`
