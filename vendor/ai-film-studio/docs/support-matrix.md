# Host Support Matrix

This matrix describes the package contract and the level of verification available in this repository. A manifest alone is not evidence that a host CLI has been installed or tested.

| Host or format | Package entry point | Status | Verification |
| --- | --- | --- | --- |
| Generic Agent Skills | `skills/ai-film-studio/SKILL.md` plus its bundled resource directories | Portable package | `python3 scripts/verify_package.py` checks resource parity |
| Root repository import | `SKILL.md` plus root resources | Portable source layout | `python3 scripts/verify_package.py` and `bash scripts/verify_all.sh` |
| Claude Code | `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` | Manifest-compatible; host CLI smoke test required | `claude plugin validate .` when Claude CLI is available |
| Codex | `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` | Manifest-compatible; host CLI smoke test required | `codex plugin list` after installation |
| Cursor | `.cursor/skills/ai-film-studio/SKILL.md` | Compatibility copy | Content parity is checked by `verify_package.py` |

## Canonical source

`SKILL.md` and the root resource directories are the source of truth. `skills/ai-film-studio/` is a standalone mirrored package for hosts that copy one skill directory. Update the canonical files first, then synchronize the portable package and run the validator.

## Known limitations

This repository does not claim to provide a renderer, provider API client, collaboration server, live task queue, visual continuity scorer, loudness analyzer, or rights-clearance service. Those are optional runtime integrations. Until an integration is installed and tested, label its output `not-yet-verified`.
