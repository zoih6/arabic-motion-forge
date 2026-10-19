---
name: arabic-motion-forge
description: Arabic-first motion production system for layered text, masks, paths, physics, maps, documentary graphics and original vertical or horizontal films. Routes the brief to verified tools, protects Arabic shaping, forbids recycling project compositions, renders deterministically, and preserves authorized checkpoints without heavy default downloads.
license: MIT for original code and documentation; third-party components retain their notices
---

# Arabic Motion Forge

## Start here

1. Read [AGENTS.md](AGENTS.md).
2. Follow [workflows/route.md](workflows/route.md). Do not load every vendor document.
3. Inspect `project.json` if continuing a project. Otherwise collect only missing brief fields.
4. Run `python tools/doctor.py`; install only the required profile using [INSTALL.md](INSTALL.md).
5. Write a new story, style fingerprint, asset plan, copy lock and layer plan for the subject. Use [templates/](templates/) as data contracts, **not** visual scene templates.
6. Route to the relevant skill, choose real supported mechanisms from [catalog/README.md](catalog/README.md), and verify the chosen path in [catalog/capabilities.json](catalog/capabilities.json).
7. Prototype the hardest technical shot, review meaningful motion samples, then render with checkpoints. Publish only to the explicitly authorized destination.
8. Finish with encoded-media checks, verified links/hashes and updated project state.

## One-link installation for a fresh agent

Repository: https://github.com/zoih6/arabic-motion-forge

Read this file and `INSTALL.md` first. The default release archive is **code, rules, schemas, tested primitives, fonts and the two supplied skills only**. It excludes the demonstration composition, old film media and rendered videos. A public install needs no token.

Use `tools/install_from_release.py` after inspecting it, or a sparse checkout of the documented core paths. Do not clone the Alhambra repository or automatically download Releases media.

## Non-negotiable design contract

- Motion serves information and emotion; it does not fill dead time.
- A title, its underline, ornament, matte and nearby picture have independent timing when their functions differ.
- Arabic letters remain correctly shaped and connected. Do not fake character animation by splitting strings.
- The camera cannot substitute for detailed element choreography.
- Do not claim a native After Effects operation when using Canvas/SVG or an unverified adapter.
- A technique name is a behavior description, not proof of a separate engine feature.
- Approved words, fonts and designs do not change to hide technical failures.
- Reuse generic infrastructure, **never a prior project's scene code, style, assets or shot sequence as the new project**.

## Progressive routes

- Brief: `skills/intake/SKILL.md`
- New identity: `skills/originality/SKILL.md`
- Layer/timing/camera design: `skills/motion-direction/SKILL.md`
- Arabic and typography: `skills/arabic-type/SKILL.md`
- Genuine/generated assets: `skills/asset-craft/SKILL.md`
- Voice, lyrics and score: `skills/audio-sync/SKILL.md`
- Tests and critique: `skills/quality/SKILL.md`
- Storage, publication and recovery: `skills/delivery/SKILL.md`

For the broader film-production workflow, load `vendor/ai-film-studio/SKILL.md` and its `workflows/intent-router.md`. For the supplied motion helper, load `vendor/motion-reel/SKILL.md`, but override its platform/fps/output assumptions with the current project's actual contract. Read `THIRD_PARTY.md` before redistributing vendor material.

## What this skill does not promise

It does not train the underlying model, guarantee creativity, create native `.aep` files without an actual AE environment, grant third-party media rights, or prove unsupported engines work. It provides a tested process, explicit failure gates, executable primitives, and reproducible recovery records.
