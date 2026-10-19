# Install AI Film Studio

AI Film Studio is distributed as a repository-based Skill/Plugin. Install the repository, let the host discover its manifest, and use the root `SKILL.md` as the canonical behavior.

## One-line install instruction for an agent

```text
Install the AI Film Studio skill/plugin from https://github.com/zoih6/ai-film-studio.
Read AGENTS.md, use SKILL.md as the canonical behavior, and start at workflows/intent-router.md.
```

## Claude Code

Use the repository as a local/plugin marketplace source according to the Claude Code version installed:

```bash
claude plugin marketplace add zoih6/ai-film-studio
claude plugin install ai-film-studio@ai-film-studio
```

Validate the package from its checkout:

```bash
claude plugin validate .
claude plugin list
```

The Claude-specific manifest is `.claude-plugin/plugin.json`; its marketplace entry is `.claude-plugin/marketplace.json`.

## Codex

```bash
codex plugin marketplace add zoih6/ai-film-studio --ref main
codex plugin add ai-film-studio@ai-film-studio
codex plugin list
```

The Codex-specific manifest is `.codex-plugin/plugin.json`; its marketplace entry is `.agents/plugins/marketplace.json`.

## Generic Agent Skills

Install the repository directory as a skill. The canonical entry point is:

```text
SKILL.md
```

The standard compatibility entry point is:

```text
skills/ai-film-studio/SKILL.md
```

The directory `skills/ai-film-studio/` is self-contained and includes the workflows, references, schemas, styles, quality checks, examples, scripts, and assets referenced by its skill file. Hosts that install one skill directory should copy this directory as a whole, not only the Markdown file.

After installation, use a request such as:

```text
Use AI Film Studio to create a 15-second Arabic coffee commercial for Reels. Deliver the brief, big idea, shot cards, image prompts, motion prompts, audio plan, end card, and quality checks.
```

## Manual local installation

For a host that loads skills from a folder:

```bash
mkdir -p ~/.claude/skills/ai-film-studio
cp SKILL.md ~/.claude/skills/ai-film-studio/SKILL.md
cp -R workflows references schemas styles quality examples ~/.claude/skills/ai-film-studio/
```

## Update and removal

Pull the latest repository and refresh the installed plugin using the same host command. For a manual installation, replace the skill directory with the new checkout. To remove the manual copy:

```bash
rm -rf ~/.claude/skills/ai-film-studio
```

## First run

1. Read `SKILL.md`.
2. Route the request through `workflows/intent-router.md`.
3. Load only the selected workflow and its required references.
4. Preserve style locks, product truth, entity continuity, and hard quality gates.
5. Run the relevant checks before delivery.
