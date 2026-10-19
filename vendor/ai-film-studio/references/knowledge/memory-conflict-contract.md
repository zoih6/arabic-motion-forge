---
name: memory-conflict-contract
description: |
  Contract رسمي لحل تضاربات الذاكرة في AI Film Studio v2.1.0.
  يميّز بين 6 أنواع تضارب، يحدد Source of Truth، Scope Detection،
  Override Lifetime، Superseded Handling، Decision Log + Bible
  Update Rules، Session Checkpoint Propagation.
  مرتبط بـ: `references/knowledge/memory-lifecycle.md`، `references/knowledge/memory-schema.md`، `schemas/state/decision-log.md`، `schemas/state/continuity-bible.md`، `schemas/state/session-checkpoint.md`.
  AUTHORITATIVE للـ conflict resolution: هذا الملف.
tier: 3
when_to_load: "عند كل تحديث لذاكرة المشروع، أو عند تضارب بين instruction جديد و approved memory"
---

# Memory Conflict Contract — AI Film Studio v2.1.0

> **هذا هو المرجع الرسمي الوحيد لحل تضاربات الذاكرة.** أي تضارب بين instruction
> جديد (مستخدم أو generation) و memory معتمد يمر عبر هذا الملف.
>
> **مرتبط بـ memory lifecycle v1.4:** Supersede + Validate + Promote.

---

## 1. Source of Truth Hierarchy (الأعلى أولوية)

```yaml
source_of_truth:
  1_user_constraint_current:
    description: "تعليمات المستخدم الحالية الصريحة (turn الحالي)"
    applies_to: "العملية الحالية فقط"
    does_not_silently_rewrite: "approved project memory"
  2_approved_project_memory:
    description: "memory بحالة APPROVED (v1.4 schema)"
    source: "schemas/state/project-memory.md (Canonical Locks)"
  3_approved_scene_state:
    description: "Scene DNA / Shot DNA approved"
    source: "schemas/state/frame-chain.md + continuity-bible.md"
  4_latest_approved_asset:
    description: "آخر إصدار معتمد من asset (image, motion, audio)"
    source: "schemas/state/asset-registry.md"
  5_specialist_guidance:
    description: "توصية من workflow/agent متخصص"
    example: "M7a يوصي بـ negative_prompts معينة"
  6_default_studio_choice:
    description: "اختيار افتراضي من المهارة"
    note: "لا يُكتب لـ memory إلا بعد promote"
```

**القاعدة الحاكمة:** التعليمات الحالية الصريحة تفوز للـ turn الحالي، لكنها **لا تعيد كتابة** memory معتمد صامتًا. أي تغيير في lock → override/version جديد.

---

## 2. الـ 6 Conflict Types

### 2.1 No Conflict (لا تضارب)

```yaml
no_conflict:
  definition: "التعليمات الجديدة لا تتعارض مع أي memory معتمد"
  action: "تنفيذ عادي"
  memory_update: "لا شيء"
  log: "لا شيء"
  example: "صورة جديدة لشخصية بنفس الـ Identity String المعتمد"
```

### 2.2 Shot Override (تجاوز على لقطة واحدة)

```yaml
shot_override:
  definition: "التعليمات الجديدة تخص لقطة واحدة فقط (shot_id) ولا تتعارض مع مشاهد أخرى"
  detection:
    - "user mentions specific shot_id: 'in SC01_SH03...'"
    - "instruction is local: 'هذه اللقطة فقط'، 'هنا'، 'shot واحد'"
    - "scene/character/wardrobe references unchanged"
  scope: "shot"
  lifetime: "حتى نهاية المشروع أو override آخر على نفس shot"
  memory_update:
    file: "schemas/state/frame-chain.md"
    field: "shot.shot_overrides[]"
    status: "PROPOSED → APPROVED (no user confirm needed for non-critical)"
  bible_update: "لا شيء (لا تغيير في identity/wardrobe/character)"
  log: "decision-log.md → scope: shot, reversible: true"
  example: "في SC01_SH03 غيّر الإضاءة من key_light front إلى side_light"
```

### 2.3 Scene Override (تجاوز على مشهد)

```yaml
scene_override:
  definition: "التعليمات الجديدة تخص مشهدًا واحدًا (scene_id) ولا تتعارض مع مشروع/شخصية/عالم"
  detection:
    - "user mentions specific scene_id: 'في SC02...'"
    - "instruction is scene-scoped: 'هذا المشهد'، 'هنا في scene 2'"
    - "all shots in scene inherit unless shot_override on top"
  scope: "scene"
  lifetime: "حتى نهاية المشروع أو override آخر على نفس scene"
  memory_update:
    file: "schemas/state/project-memory.md (Active Decisions)"
    field: "decisions[].scope = scene"
  bible_update: "لا شيء في character/identity، لكن continuity-bible.md يحوي scene_variants"
  log: "decision-log.md → scope: scene, reversible: true"
  example: "في SC02، أضف خلفية مطر، الملابس نفسها"
```

### 2.4 Project / Canonical Update (تحديث على مستوى المشروع)

```yaml
project_canonical_update:
  definition: "التعليمات الجديدة تغيّر حقيقة canonical (character، world، style، identity، wardrobe)"
  detection:
    - "user references canonical key: 'خله يلبس جاكيت أبيض' (الـ wardrobe الحالي = أسود)"
    - "change propagates to all scenes/shots using the key"
    - "old value becomes SUPERSEDED, new value becomes APPROVED"
  scope: "project"
  lifetime: "حتى project_canonical_update آخر"
  memory_update:
    file: "schemas/state/project-memory.md (Canonical Locks)"
    action: |
      1. اقرأ القيمة القديمة
      2. أنشئ memory جديد بحالة APPROVED و version جديد
      3. حدّث memory القديم إلى SUPERSEDED (لا تحذف)
      4. valid_to = updated_at
  bible_update:
    file: "schemas/state/continuity-bible.md"
    action: "استبدل القيمة في character/wardrobe (مع reference للـ superseded version)"
  log: "decision-log.md → scope: project, reversible: false (data lineage preserved)"
  example: "الشخصية تلبس جاكيت أبيض بدل القميص الأسود (بعد 5 لقطات)"
```

### 2.5 User-approved Supersession (استبدال بموافقة صريحة)

```yaml
user_approved_supersession:
  definition: "تغيير في memory معتمد، بموافقة صريحة من المستخدم، يُغيّر الحالة إلى SUPERSEDED"
  trigger:
    - "user explicitly says: 'احذف القديم'، 'غيّر الـ bible'، 'ابدأ من جديد'"
    - "user confirms when asked: 'نعم، احذف السابقة'"
  scope: "any (shot/scene/project)"
  lifetime: "نهائي — الـ memory القديم لا يعود تلقائيًا"
  memory_update:
    file: "schemas/state/project-memory.md"
    action: |
      1. user.approval_required = true
      2. لا تنفّذ قبل موافقة صريحة
      3. بعد الموافقة: SUPERSEDED القديم + APPROVED الجديد + parent_id
  bible_update: "نفس قواعد 2.4 لكن مع approval_id = timestamp + user"
  log: "decision-log.md → scope: <scope>, reversible: false, approved_by: user, approval_id: <ts>"
  example: "إزالة شخصية ثانوية من Bible + إزالتها من frame chain"
```

### 2.6 Ambiguous Conflict → Clarification (تضارب غامض)

```yaml
ambiguous_conflict:
  definition: "تضارب محتمل لكن لا يمكن تحديد scope/severity تلقائيًا"
  trigger:
    - "instruction contradicts memory لكن scope غير واضح"
    - "instruction could be shot or scene or project"
    - "decision is irreversible OR high-impact (brand/legal/dialogue)"
  
  ask_only_if:
    - "decision is irreversible (e.g. delete character)"
    - "decision is high-impact (brand logo, legal, dialogue wording)"
    - "decision changes a Hard Gate (G4 / G8)"
  do_not_ask_if:
    - "decision is reversible + low-impact (e.g. accent color tweak)"
    - "default can be inferred from context"
  
  action:
    - "اسأل سؤالاً واحدًا فقط مع 3-4 خيارات"
    - "لا تسأل أكثر من 3 أسئلة قبل اتخاذ قرار"
    - "بعد 3 أسئلة، اختر المشروع بأقل مخاطر (typically project_canonical_update) واطلب موافقة"
  
  example: |
    User: "غيّر ملابس الشخصية"
    Ambiguous: أي شخصية؟ أي مشهد؟ أي ملابس؟
    Ask: "أي شخصية تقصد؟ (CHAR-01 / CHAR-02 / الكل؟)"
    After answer: نفّذ project_canonical_update على character المحدد
```

---

## 3. Decision Tree (شجرة القرار)

```
new_user_instruction arrives
    ↓
compare_with_approved_memory
    ↓
no_overlap → NO_CONFLICT → execute
    ↓
overlap detected
    ↓
determine_scope (regex on instruction + lookup in memory)
    ↓
┌─────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ shot    │ scene        │ project      │ approved     │ ambiguous    │
│ only    │ only         │ canonical    │ supersession │              │
├─────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ SHOT_   │ SCENE_       │ PROJECT_     │ USER_        │ ASK_USER     │
│ OVERRIDE│ OVERRIDE     │ CANONICAL    │ APPROVED     │ (if high-    │
│         │              │ UPDATE       │ SUPERSESSION │ impact)      │
└─────────┴──────────────┴──────────────┴──────────────┴──────────────┘
    ↓              ↓              ↓              ↓              ↓
no approval    no approval   no approval    approval        clarification
needed         needed        needed (silent required        question
(silent        (silent       SUPERSEDED     BEFORE          (1-3 max)
PROPOSED→      PROPOSED→     of old)        action)
APPROVED)      APPROVED)
    ↓              ↓              ↓              ↓              ↓
update         update         update +       update +        execute chosen
frame-chain    project-memory bible update   bible update    path
shot only      Active         character/     + approval_id   after response
               Decisions      wardrobe       
                              
log to         log to         log to         log to          log to
decision-log   decision-log   decision-log   decision-log    decision-log
scope: shot    scope: scene   scope: project scope: <any>    scope: <any>
reversible:true reversible:true reversible:false reversible:false reversible:?
```

---

## 4. Scope Detection Rules

```yaml
scope_detection:
  
  shot_patterns:
    regex_examples:
      - "in SC\\d+_SH\\d+"
      - "هذه اللقطة|shot واحد|here only"
      - "في لقطة"
    confidence: "high if shot_id mentioned, medium if 'هذه/هذا'"
  
  scene_patterns:
    regex_examples:
      - "in SC\\d+ (without _SH)"
      - "هذا المشهد|scene|في scene"
      - "هنا في مشهد"
    confidence: "high if scene_id mentioned, medium if 'هذا/هذه'"
  
  project_patterns:
    regex_examples:
      - "الشخصية|القميص|الستايل|brand|character"
      - "كل المشاهد|everywhere|في كل مكان"
      - "from now on|من الآن"
    confidence: "high if canonical key mentioned, medium if 'كل/دائمًا'"
  
  supersession_patterns:
    regex_examples:
      - "احذف|remove|delete|ابدأ من جديد|start over"
      - "غيّر الـ bible|change the bible"
    confidence: "high — always user-approved"
  
  ambiguous_patterns:
    indicators:
      - "instruction references 1+ characters but scope unclear"
      - "instruction is in past tense ('used to be')"
      - "instruction changes wardrobe/identity partially"
    action: "ASK_USER (per 2.6 rules)"
```

---

## 5. Override Lifetime

```yaml
override_lifetime:
  
  shot_override:
    duration: "حتى project end أو override آخر على نفس shot"
    auto_expire_on: "scene_break أو chain_break موثّق"
    can_be_replaced: "نعم (shot_override جديد على نفس shot)"
  
  scene_override:
    duration: "حتى project end أو override آخر على نفس scene"
    auto_expire_on: "scene_break أو chain_break موثّق"
    can_be_replaced: "نعم (scene_override جديد)"
  
  project_canonical_update:
    duration: "حتى project_canonical_update آخر على نفس key"
    auto_expire_on: "لا — يبقى حتى تحديث جديد"
    can_be_replaced: "نعم (SUPERSEDED القديم + APPROVED الجديد)"
  
  user_approved_supersession:
    duration: "نهائي"
    auto_expire_on: "لا"
    can_be_replaced: "لا (إلا بموافقة user أخرى)"
```

---

## 6. Superseded Decision Handling

```yaml
superseded_handling:
  
  on_supersede:
    1_read_old_value_from_memory
    2_create_new_memory_record:
        version: "old.version + 1"
        status: "APPROVED"
        valid_from: "now"
        parent_id: "old.memory_id"
    3_update_old_record:
        status: "SUPERSEDED"
        valid_to: "now"
    4_write_both_to_memory_schema
    5_log_to_decision_log:
        action: "SUPERSEDED"
        old_memory_id: "<id>"
        new_memory_id: "<id>"
        scope: "<shot|scene|project>"
        reversible: "false"
  
  on_query:
    return: "active APPROVED version (never SUPERSEDED)"
    unless: "explicit query for lineage → return both with version history"
  
  on_compaction:
    keep: "active APPROVED records only"
    keep_lineage: "SUPERSEDED records in archive (memory-schema.md valid_to field)"
    exclude_from_context: "SUPERSEDED records (per memory-context-policy.md)"
  
  on_repair:
    allow: "rollback to SUPERSEDED version IF user_approved_supersession for current value"
    action: "create new version with previous_value, mark current SUPERSEDED"
```

---

## 7. Decision Log Update Rules

```yaml
decision_log_update:
  
  file: "schemas/state/decision-log.md"
  
  when_to_log:
    - "any supersession (shot/scene/project/user_approved)"
    - "any ambiguous_conflict resolved via ASK_USER"
    - "any repair that changes a memory value"
    - "any G4/G8 hard fail + recovery"
  
  format:
    id: "DEC-YYYYMMDD-###"
    timestamp: "ISO 8601"
    scope: "shot|scene|project|user_approved|ambiguous"
    decision: "human-readable summary"
    conflict_type: "one of 6 types"
    old_memory_id: "<if applicable>"
    new_memory_id: "<if applicable>"
    reversible: "true|false"
    approved_by: "user|studio|automatic"
    approval_id: "<timestamp+user if user_approved>"
    reason: "why this decision"
    agent: "workflow that triggered"
  
  example:
    - id: "DEC-20260115-001"
      timestamp: "2026-01-15T14:30:00Z"
      scope: "project"
      decision: "CHAR-01 wardrobe: black shirt → white jacket"
      conflict_type: "project_canonical_update"
      old_memory_id: "MEM-20260110-005"
      new_memory_id: "MEM-20260115-008"
      reversible: "false"
      approved_by: "user"
      approval_id: "USER-20260115-1430"
      reason: "user said 'خله يلبس جاكيت أبيض' at scene 3+"
      agent: "M2-narrative (update propagated)"
```

---

## 8. Continuity Bible Update Rules

```yaml
bible_update_rules:
  
  file: "schemas/state/continuity-bible.md"
  
  triggers:
    project_canonical_update:
      - "identity field changed"
      - "wardrobe.primary changed"
      - "world.location changed"
      - "style changed"
    user_approved_supersession:
      - "character removed"
      - "location removed"
      - "wardrobe item removed"
  
  update_protocol:
    1_identify_section: "أي قسم في Bible يتأثر (identity / wardrobe / world / ...)"
    2_update_value: "استبدل بالقيمة الجديدة (مع مرجع للـ version)"
    3_add_changelog_entry: |
        version: "v[X.Y]"
        date: "<ISO>"
        changes:
          - "<field>: <old> → <new>"
    4_propagate_to_frame_chain: "إذا كان التغيير يؤثر على لقطات موجودة، حدّث frame-chain.md"
    5_propagate_to_prompts: "إذا تم توليد prompts، أعد بناءها (G4 hard gate)"
  
  no_update_needed:
    - "shot_override (لا يغيّر Bible)"
    - "scene_override (لا يغيّر Bible، يضيف scene_variant)"
    - "scene_variant: لا يغيّر Bible، يحفظ في Active Decisions"
  
  hard_gate_check:
    after_bible_update: "G3 (Continuity) → RE-VALIDATE → REPAIR prompts if needed"
    propagate_to: "M7b + M8a (rebuild affected prompts)"
```

---

## 9. Session Checkpoint Propagation

```yaml
session_checkpoint_propagation:
  
  file: "schemas/state/session-checkpoint.md"
  
  when_to_update:
    - "after any memory write (shot/scene/project/supersession)"
    - "after any bible update"
    - "after any decision log entry"
    - "at end of every M-stage"
  
  fields_to_update:
    must_preserve: "list of canonical keys that must not change in next session"
    open_blocker: "ambiguous_conflict awaiting user answer"
    last_delivered_artifact: "what was just produced"
    next_action: "what to do next"
  
  propagation_rules:
    cross_session:
      rule: "checkpoint + project-memory = minimum state to resume"
      read_priority: "checkpoint first, then memory"
    
    multi_agent:
      rule: "every M-stage agent reads checkpoint before writing"
      write_back: "every M-stage agent updates checkpoint at end"
    
    conflict_pending:
      rule: "if ambiguous_conflict awaiting user, set open_blocker"
      on_resume: "ASK_USER immediately with reference to decision-log id"
  
  example_after_user_approved_supersession:
    - project_id: "PROJECT-20260110-001"
      state: "project_canonical_update applied"
      last_user_request: "remove CHAR-02 from Bible"
      last_delivered_artifact: "decision-log DEC-20260115-001 + updated bible"
      latest_approved_version: "v1.4 (CHAR-02 SUPERSEDED)"
      next_action: "M4a (rebuild frame-chain without CHAR-02)"
      unresolved_questions: "—"
      must_preserve: "CHAR-01 identity, world.location_01, palette"
```

---

## 10. Integration with Memory Lifecycle v1.4

```yaml
lifecycle_integration:
  
  capture:
    - "apply scope_detection on every new fact"
    - "decide conflict_type based on detected scope"
    - "no_conflict → capture normally"
    - "shot/scene_override → capture as PROPOSED, auto-promote to APPROVED (reversible)"
    - "project_canonical_update → capture as PROPOSED, write to bible, then auto-promote"
    - "user_approved_supersession → capture as PROPOSED, REQUIRE approval, then promote"
    - "ambiguous → ask user, then treat as one of above"
  
  normalize:
    - "use canonical keys from bible when available"
    - "convert natural language to canonical_key (e.g. 'الجاكيت الأبيض' → 'wardrobe.primary=white jacket')"
  
  validate:
    - "check conflict_type consistency with scope_detection"
    - "if project_canonical_update: ensure SUPERSEDED handling done"
    - "if user_approved_supersession: ensure approval_id recorded"
  
  promote:
    - "PROPOSED → APPROVED only after conflict_type-specific conditions"
    - "shot/scene_override: silent auto-promote"
    - "project_canonical: silent auto-promote (with SUPERSEDED on old)"
    - "user_approved: REQUIRE explicit user approval before promote"
  
  inherit:
    - "approved project memory → feeds Scene DNA + Shot DNA"
    - "scene/shot overrides → do NOT inherit upward (local only)"
    - "SUPERSEDED → never inherits (excluded from context)"
  
  supersede:
    - "follow superseded_handling section above"
    - "preserve lineage in memory-schema (valid_to + parent_id)"
  
  compact:
    - "active APPROVED records only"
    - "SUPERSEDED → archive (not in active context)"
    - "REJECTED → never inject"
  
  expire:
    - "session-only assumptions → expire at session end unless promoted"
    - "shot/scene_override → persist until project end"
    - "project_canonical → persist until next project_canonical_update"
  
  repair_feedback:
    - "if G4 fail due to conflict: log to decision-log, repair prompt, propagate"
    - "if user_approved_supersession was wrong: create new version (old back as SUPERSEDED)"
```

---

## 11. Cross-References

- **Memory Schema (canonical record):** `references/knowledge/memory-schema.md`
- **Memory Lifecycle:** `references/knowledge/memory-lifecycle.md`
- **Project Memory (state template):** `schemas/state/project-memory.md`
- **Session Checkpoint:** `schemas/state/session-checkpoint.md`
- **Decision Log:** `schemas/state/decision-log.md`
- **Continuity Bible (update rules):** `schemas/state/continuity-bible.md`
- **Frame Chain (propagation):** `schemas/state/frame-chain.md`
- **Source of Truth Hierarchy:** `references/protocols/production-state-machine.md` § 8
- **Orchestration (write timing):** `references/protocols/orchestration-runtime.md` (commit section per route)

---

## 12. Summary

| Conflict Type | Scope | Approval | Reversible | Bible Update | Log |
|---|---|---|---|---|---|
| **No Conflict** | — | none | — | no | no |
| **Shot Override** | shot | silent | yes | no | decision-log |
| **Scene Override** | scene | silent | yes | no (scene_variant) | decision-log |
| **Project Canonical Update** | project | silent | no (lineage preserved) | yes | decision-log + bible version |
| **User-approved Supersession** | any | **required** | no | yes + approval_id | decision-log + bible version |
| **Ambiguous Conflict** | ? | ask if high-impact | depends | depends on chosen path | decision-log |

**AUTHORITATIVE للـ conflict resolution في AI Film Studio v2.1.0+.**
