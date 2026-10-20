---
name: request-reframe
description: Professional brief engineering — transform messy, vague, contradictory or single-sentence user requests into a complete professional production spec with inferred defaults and resolved conflicts. MANDATORY first step for every project; executing any raw unclear request directly is strictly forbidden.
---

# Request reframe (spec engineer — hard gate)

The user may supply one chaotic sentence. That is fine — your job is to make it professional, NOT to obey it literally. **No tool call, no scene, no asset download may start before `spec.md` is authored and confirmed.**

## Procedure
1. Parse the raw message into slots: subject/message, audience, duration, format (orientation/width/height/fps), on-screen copy, audio source & sync intent, style references (extract RULES only — e.g. "their text-reveal technique", never "their files"), deliverables & size budget, publishing, approval mode, deadline pressure.
2. PRESERVE EVERYTHING: copy every distinct user demand into `## User requirements` as a numbered item with status `preserved | converted | corrected` — a song, a photo, a word, an odd detail. Nothing disappears because it was awkward. Corrections CONVERT to compliant equivalents citing the rule; they never delete. Mutually-exclusive demands BOTH stay with a recorded trade-off question.
3. Detect contradictions against the kit contract and auto-correct with a visible note. Standing examples:
   - "a single-word approval a single-word approval" (letter-level Arabic) → replaced by per-word shaped reveals + WHY in spec.
   - "a single-word approval a single-word approval" → map to `runtime/spatial.mjs` 3D or 2.5D multi-plane by whether rotation is the idea (cite spatial-3d.json rule).
   - "a single-word approval a single-word approval a single-word approval a single-word approval" → downgrade to studied rules + original direction via engine; state this to the user plainly.
   - file-size demand without duration → derive duration/bitrate pair and show the math.
   - missing facts → invent sensible defaults, mark `"assumed": true` (intake skill may ask AT MOST one round for things you truly cannot assume, ≤4 questions).
4. Write `spec.md` (seeded by new_project.py) with sections: `## Objective`, `## Confirmed understanding`, `## Constraints & format`, `## Content & copy`, `## Motion & style`, `## Deliverables`, `## Assumptions (veto in one word)`, `## Refusals & corrections`. Every section ≥2 sentences; `Confirmed understanding` restates the user's intent in their own words + what CHANGED and why.
5. Sync `brief.json` from spec; when the user approves (even with one word a user wording like «SOME-ARABIC-PHRASE»), set `spec_approved:true` + `brief.approval:"approved"` + copy into `copy.txt` and record `copy_sha256` (any user wording change later re-hashes copy and re-checks).
6. `python3 tools/gate.py <dir>/project.json --stage style` (aggregated) must pass with the spec sections before direction generation is allowed to become style lock.

Anti-randomness law (AGENTS §1.5): executing the literal text of an ambiguous brief is a failure mode this gate exists to kill — even if the user insists "execute it exactly as I wrote it", you resolve contradictions technically first, log it in Refusals & corrections, and never silently produce broken Arabic/3D/size output.
