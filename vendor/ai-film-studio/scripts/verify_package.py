#!/usr/bin/env python3
"""Validate the repository's skill and plugin packaging contract."""
from __future__ import annotations

import json
import pathlib
import sys
import filecmp

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(path: str) -> pathlib.Path:
    target = ROOT / path
    if not target.exists():
        errors.append(f"missing: {path}")
    return target


skill = require("SKILL.md")
install = require("INSTALL.md")
agents = require("AGENTS.md")
for path in [
    "references/protocols/user-facing-production-flow.md",
    "schemas/storyboard.md",
    "schemas/frame-prompt-contract.md",
    "schemas/prompt-compiler-input.schema.json",
    "scripts/verify_output_contract.py",
    "scripts/prompt_compiler.py",
]:
    require(path)
for path in ["plugin.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".codex-plugin/plugin.json", ".agents/plugins/marketplace.json"]:
    target = require(path)
    if target.exists():
        try:
            json.loads(target.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON: {path}: {exc}")

if skill.exists():
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "name: ai-film-studio" not in text:
        errors.append("SKILL.md lacks the expected frontmatter")
    if "workflows/intent-router.md" not in text:
        errors.append("SKILL.md does not point to workflows/intent-router.md")

if skill.exists():
    canonical = skill.read_text(encoding="utf-8")
    for path in ["skills/ai-film-studio/SKILL.md", ".cursor/skills/ai-film-studio/SKILL.md"]:
        target = ROOT / path
        if not target.is_file():
            errors.append(f"missing readable compatibility skill: {path}")
        elif target.read_text(encoding="utf-8") != canonical:
            errors.append(f"compatibility skill differs from SKILL.md: {path}")

required_dirs = ["workflows", "references", "schemas", "styles", "quality", "examples", "scripts", "assets"]
portable_root = ROOT / "skills" / "ai-film-studio"
for directory in required_dirs:
    source_dir = ROOT / directory
    portable_dir = portable_root / directory
    if not portable_dir.is_dir():
        errors.append(f"portable skill is missing resource directory: {directory}")
        continue
    source_files = sorted(p.relative_to(source_dir) for p in source_dir.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    portable_files = sorted(p.relative_to(portable_dir) for p in portable_dir.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    if source_files != portable_files:
        errors.append(f"portable resource listing differs: {directory}")
    for relative in source_files:
        if not filecmp.cmp(source_dir / relative, portable_dir / relative, shallow=False):
            errors.append(f"portable resource differs: {directory}/{relative}")

if install.exists():
    text = install.read_text(encoding="utf-8")
    for required in [
        "https://github.com/zoih6/ai-film-studio",
        "SKILL.md",
        "workflows/intent-router.md",
    ]:
        if required not in text:
            errors.append(f"INSTALL.md missing: {required}")

manifest = ROOT / "plugin.json"
if manifest.exists():
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("skill") != "SKILL.md":
        errors.append("plugin.json must point to SKILL.md")
    if data.get("entryPoint") != "workflows/intent-router.md":
        errors.append("plugin.json must point to workflows/intent-router.md")

if agents.exists() and "SKILL.md" not in agents.read_text(encoding="utf-8"):
    errors.append("AGENTS.md does not identify the skill source of truth")

if errors:
    print("PACKAGE VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("PACKAGE VALIDATION PASSED")
print("- canonical skill: SKILL.md")
print("- plugin manifests: Claude Code + Codex")
print("- compatibility links: standard + Cursor")
print("- installation guide: INSTALL.md")
