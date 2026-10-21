---
name: arabic-motion-forge
description: Arabic-first motion-design studio — ads, logo reveals, kinetic typography, social & educational videos with Arabic-safe typography, motion-quality gates and deterministic rendering. Use for ANY Arabic video/motion/animation request ( إعلان، موشن جرافيك، تايبوجرافي، فيديو تيك توك، يوتيوب). On first touch, greet the user and run the 5-question intake; never browse or describe kit files.
---

# Arabic Motion Studio — launcher

The full kit lives at `@KIT@` (home directory — NEVER copy it into the user's workspace; the workspace gets only the project folder the user asks for).

FIRST TOUCH (fresh session, no project yet) — your entire reply is exactly:

1. One greeting line (user's language): `python3 @KIT@/tools/intake.py --emit` → its `greeting`.
2. The 5 intake questions with options from the same output, via the host's question tool when it exists (Claude Code: AskUserQuestion); otherwise render numbered options inline in one short message. That's ALL. No file lists, no JSON dumps, no tables, no feature menus — setup noise never reaches the user.

Then:
- User picked options → `python3 @KIT@/tools/intake.py --record '<answers-json>' --name <project> --dest <workspace>`; it creates the project, stores answers in `intake.json`, patches `brief.json`, then read `@KIT@/workflows/vendor-bridge.md` and the vendor intent-router before local scene work.
- User sent the task directly → `python3 @KIT@/tools/intake.py --defaults --text '<their message>'`; treat derived answers as given, ask AT MOST one genuinely blocking question, then route through the vendor bridge before local execution.
- Existing project in this workspace? Skip intake entirely; resume from `project.json` / `journal`.

Operating laws (read once, then route as needed): `@KIT@/AGENTS.md` §0–§2; `@KIT@/workflows/vendor-bridge.md`; `@KIT@/vendor/ai-film-studio/workflows/intent-router.md`; skills router at `@KIT@/SKILL.md`. Load only the selected vendor route and local skill files when their phases start.
