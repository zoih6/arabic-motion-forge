# Project Memory Schema — v1.4

Use structured records conceptually; Markdown tables are acceptable for human-readable state.

## Core Record
```yaml
memory_id: MEM-YYYYMMDD-###
project_id: PROJECT-YYYYMMDD-###
type: project|character|world|style|scene|shot|asset|audio|decision|constraint|failure|approval|session
key: canonical_key
value: canonical_value
status: PROPOSED|APPROVED|SUPERSEDED|REJECTED|INFERRED
source: user|studio|generation|approval
parent_id: null
version: v001
confidence: high|medium|low
valid_from: null
valid_to: null
updated_at: YYYY-MM-DDTHH:MM
notes: null
```

## Identity Record
Character records should reference `character_id`, identity locks, approved reference assets, wardrobe state, and known continuity constraints.

## Scene Record
Scene records should reference `scene_id`, Scene DNA, approved shots, continuity anchors, and scene-specific overrides.

## Shot Record
Shot records should reference `shot_id`, Shot DNA, source/target assets, prompt lineage, generation runs, dialogue/audio links, QC state, and approved version.

## Decision Record
Store the decision, alternatives rejected when useful, reason, scope, and whether it is reversible.

## Failure Record
Store failure class, affected asset/shot, changed variable, repair result, and reusable lesson.
