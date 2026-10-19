# Session Continuation Protocol — v1.4

When the user returns with a short command such as “كمّل”, “الآن المشهد 3”, “حرّكها”, or “عدّل آخر لقطة”:

1. Resolve the project from active memory.
2. Load the latest approved production state.
3. Load only the relevant Scene/Shot/Asset memory.
4. Recover the last actionable checkpoint.
5. Do not restart Intake unless the project identity is missing or corrupted.
6. Ask at most 3 questions only if a material ambiguity blocks execution.
7. Continue using the same identity/style/world locks unless explicitly overridden.

## Continuation Summary
Internally reconstruct:
`WHERE WE ARE → WHAT IS LOCKED → WHAT IS NEXT → WHAT CHANGED LAST → WHAT MUST NOT CHANGE`.

The user normally sees none of this internal reconstruction.
