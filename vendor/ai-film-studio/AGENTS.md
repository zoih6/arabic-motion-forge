# Agent guide

This repository is **AI Film Studio**, a reusable agent skill and plugin for planning and producing AI-generated films, commercials, documentaries, motion graphics, and series.

## Start here

1. Read `README.md` for the user-facing overview and installation routes.
2. Read `SKILL.md` for the canonical behavior and entry point.
3. Follow `workflows/intent-router.md` before loading a specialized workflow.
4. Read only the relevant files under `workflows/`, `references/`, `schemas/`, `styles/`, and `quality/`.
5. Run `bash scripts/verify_all.sh` after changes to workflows, schemas, references, styles, or validation code.

## Source of truth

- `SKILL.md` is the canonical skill instruction file.
- `workflows/intent-router.md` is the canonical routing entry point.
- `skills/ai-film-studio/` is a self-contained portable package. Its `SKILL.md` and resource directories mirror the canonical root package; keep them synchronized and validate them with `scripts/verify_package.py`.
- `.cursor/skills/ai-film-studio/SKILL.md` is a readable compatibility copy; keep it byte-for-byte identical to the canonical file.
- Plugin manifests describe packaging only. Do not duplicate behavior in manifests.
- `README.md` and `INSTALL.md` are the user-facing installation contract.
- `references/protocols/user-facing-production-flow.md` is the highest-level user-facing behavior contract. Keep it above individual workflow details.
- `schemas/storyboard.md` and `schemas/frame-prompt-contract.md` define the visible sequence: Storyboard first, then one complete copy-ready prompt per frame/shot.

## Repository map

| Area | Location | Purpose |
| --- | --- | --- |
| Canonical skill | `SKILL.md` | Progressive-disclosure skill instructions and triggers |
| Routing | `workflows/intent-router.md` | Select the smallest suitable production path |
| Production workflows | `workflows/` | M0–M11 stages, engines, and shortcuts |
| Domain references | `references/` | Protocols, specifications, research, and knowledge |
| Output contracts | `schemas/` | Structured deliverable schemas and templates |
| Operational contracts | `schemas/` and `references/protocols/` | Intent, project state, provenance, provider capability, and agent handoffs |
| Visual systems | `styles/` | Style index, locks, and visual identity rules |
| Quality | `quality/` and `scripts/` | Gates, checklists, and deterministic verification |
| Plugin metadata | `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/` | Host-specific discovery and marketplace metadata |
| Compatibility links | `skills/`, `.cursor/skills/` | Standard skill import paths |
| Support claims | `docs/support-matrix.md` | Host status, package entry points, and known limitations |

## Safe change rules

- Preserve existing workflows, schemas, references, examples, and style locks unless the task explicitly requests a content change.
- Change `SKILL.md` first for behavior changes, then update only documentation that describes the changed behavior.
- Keep manifests, version strings, installation commands, and repository URLs aligned.
- Do not commit credentials, API keys, generated renders, local project state, or private media.
- Prefer adding a new style lock over editing an existing lock; existing locks are compatibility contracts.
- Use relative links so the repository remains forkable and works from any clone.
- Treat provider/model facts as time-sensitive: require a verification date and source URL; never store credentials in the registry.
- Do not claim media-level validation, rendering, collaboration, or provider execution unless the relevant runtime integration was actually tested.
- Keep internal research, rejected directions, stage names, artifact logs, and prompt fragments out of normal user-facing output.
- Do not change the one-prompt-per-frame rule into a multi-part template; users must never assemble prompts manually.

## Verification

Run the smallest relevant checks, then the complete suite for release changes:

```bash
python3 scripts/verify_package.py
python3 scripts/verify_output_contract.py
bash scripts/verify_all.sh
python3 scripts/verify_links.py

git diff --check
```

Report exact commands and results. Do not claim a host-specific plugin install was tested unless that host CLI is available and the install was actually performed.
