---
name: agent-protocol
---

# Agent Interaction Protocol

Use this protocol when an agent invokes AI Film Studio. It separates conversational intent from production artifacts and keeps recovery deterministic.

## 1. Extract intent

Create a `generation-intent` object before selecting a workflow. Preserve the user's wording in `request`; do not invent missing facts. Use `approval_mode: checkpointed` when the project is multi-shot, factual, sensitive, or expensive.

## 2. Route minimally

Start at `workflows/intent-router.md`. Choose the smallest sufficient scope: prompt, shot, scene, sequence, full production, repair, or localization. Do not run M0–M11 for a bounded prompt or single-shot request.

## 3. Plan before prompts

For scene or larger scopes, create or update the brief, concept, beats, entity/style/continuity state, and shot package before compiling model prompts. Keep stable IDs for scenes, shots, assets, and decisions.

## 4. Validate handoffs

Every handoff must state: input artifact IDs, output artifact IDs, selected workflow, required locks, unresolved assumptions, and the next validation gate. On failure, return a structured error with `code`, `location`, `cause`, and `repair_action`.

## 5. Choose providers explicitly

Use a verified provider capability entry when available. Record the selected provider/model, capability match, fallback order, reason, verification date, and any unknowns. Never claim a provider capability from an unverified registry entry.

## 6. Review and repair

Use the first-defect rule: identify the earliest failing gate, repair only the affected artifact and its downstream dependents, then rerun the relevant checks. Do not silently regenerate approved upstream work.

## 7. Deliver honestly

Label results `candidate`, `qualified`, or `not-yet-verified`. A document-level pass does not prove media playback, visual continuity, loudness, lip-sync, or rights clearance unless those checks were actually performed.
