---
name: creative-direction
description: Generate and approve original concept directions with the inspiration engine, killing template-output risk. Use after intake and before layer planning or style lock, whenever a project needs its own visual identity. Enforces tools/direct.py + check_directions.py gates.
---

# Creative direction

The engine guarantees STRUCTURAL variety; you supply taste. Sequence:

1. `python3 tools/direct.py --topic "<subject>" --project <dir>` → three axis-combined directions (story device, metaphor, material, type architecture, camera, rhythm, accent, transition logic + palette set), self-checked for ≥4-axis distinctness.
2. Refine each into a one-screen proposal: keep the axis spine, rewrite rationales with topic-specific reasons, name the signature move the whole film will repeat, and what the film refuses to do. Fill every TODO — `check_directions.py` counts topic tokens and rejects empty prose.
3. Check style collisions: `--against ../previous-project/style.json` for any prior house style that must not be echoed (kit example style is auto-checked).
4. Present all three to the user (compact: id, spine, first-frame prompt, signature move; no images unless asked). If the user says "you choose", pick one, justify in 3 lines, and say so.
5. `python3 tools/check_directions.py <dir>/project.json` (add `--approved` marker in directions.json for the chosen one first). This writes style.json's `direction_axes`+palette; style lock = journal `style-lock`.
6. Turn axes into mechanics in the layer plan: each chosen option has a concrete implementation entry (which runtime primitive, which recipe file). An axis without a mechanism is decoration — the quality pass will flag shots with one flat motion.

Anti-patterns live in `catalog/dictionaries/direction-axes.json` — reread them if a direction feels "generated". Style families and their steal/never lines: `catalog/dictionaries/styles.json`.
