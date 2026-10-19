# AI Film Studio System Upgrade — 2026-09-14

## Executive summary

AI Film Studio already provides a strong declarative creative system: intent routing, M0–M11 production stages, specialized engines, style/entity/continuity locks, shot contracts, state templates, and quality gates. The comparison identified the highest-risk gap as **packaging and execution boundaries**: a standalone installer could receive only `SKILL.md` without the workflows and references it names, while production-oriented systems additionally expose durable artifacts, provider capabilities, resumable state, render contracts, and measurable review outcomes.

This upgrade preserves the existing content and adds a portable package, structured agent protocol, project/artifact contracts, provider-routing guidance, and explicit capability boundaries. It does not claim that the repository itself renders media or provides a multi-user production service.

## Implemented in this release

| Area | Change |
| --- | --- |
| Portable packaging | `skills/ai-film-studio/` now contains its own `workflows/`, `references/`, `schemas/`, `styles/`, `quality/`, `examples/`, `scripts/`, and `assets/` resources. |
| Agent interaction | Added `schemas/generation-intent.schema.json` and `references/protocols/agent-protocol.md`. |
| State and provenance | Added `schemas/project-manifest.schema.json`, `artifact-record.schema.json`, and `artifact-provenance.schema.json`. |
| Provider routing | Added `schemas/provider-capability.schema.json`, `references/provider-registry.yaml`, and `workflows/provider-routing.md`. |
| Skill behavior | Added a concise operating contract to `SKILL.md` covering minimal routing, planning-before-prompts, explicit provider decisions, first-defect repair, and honest delivery states. |

## Research signals

Open-source systems repeatedly use the following patterns:

1. A portable Skill is a directory with `SKILL.md` and all relative resources needed by that file; host-specific plugin manifests are an optional layer.
2. Video agents separate intent extraction, planning, generation, review, repair, and delivery rather than relying on one prompt.
3. Durable artifact IDs, dependency edges, provenance, checkpoints, and resumability prevent approved work from being regenerated after a failure.
4. Provider/model selection is capability-aware and records fallbacks, versions, evidence, cost, latency, and unknowns.
5. Render systems require machine-readable frame/timeline contracts; planning documents alone do not prove renderability.
6. Production tools add storyboard/animatic, review states, editorial interchange, and audio-stem handoff as explicit artifacts.

## Sources

- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills reference repository](https://github.com/agentskills/agentskills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [ViMax](https://github.com/HKUDS/ViMax)
- [AI Video Production Editor](https://github.com/LudwigKienle/ai-video-production-editor)
- [Remotion schemas](https://www.remotion.dev/docs/schemas) and [rendering](https://www.remotion.dev/docs/renderer/render-media)
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO)
- [Kitsu](https://kitsu.cg-wire.com/)
- [Storyboarder](https://github.com/wonderunit/storyboarder)

## Deliberate boundaries

The repository remains a Skill/Plugin and production-orchestration specification. Provider APIs, media rendering, visual similarity, loudness, rights clearance, collaboration permissions, and real-time review require host/runtime integrations and must be marked `not-yet-verified` until an executable adapter and test exist.
