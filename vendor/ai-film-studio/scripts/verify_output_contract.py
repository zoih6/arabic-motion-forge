#!/usr/bin/env python3
"""Validate the top-level user-facing interaction and prompt contracts."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"missing: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

flow = read("references/protocols/user-facing-production-flow.md")
output = read("references/protocols/output-protocol.md")
interaction = read("references/protocols/interaction-flow.md")
router = read("workflows/intent-router.md")
frame = read("schemas/frame-prompt-contract.md")
storyboard = read("schemas/storyboard.md")

for name, text, required in [
    ("user-facing flow", flow, ["ONLY-NECESSARY QUESTIONS", "VISION SUMMARY", "REFERENCE PACK (CAST / LOCATIONS / PROPS / STYLE)", "ONE COMPLETE IMAGE PROMPT PER FRAME", "GENERATION CHOICE: EXTERNAL OR IN-PLATFORM", "ONE COMPLETE MOTION PROMPT PER SHOT"]),
    ("frame contract", frame, ["exactly one copy-ready prompt block", "add to the previous prompt", "one complete motion prompt"]),
    ("storyboard contract", storyboard, ["frame_id", "image_prompt_status", "لا تعرض Prompt الصورة في جدول الـStoryboard"]),
    ("router", router, ["user-facing-production-flow.md"]),
]:
    for phrase in required:
        if phrase not in text:
            errors.append(f"{name} missing contract phrase: {phrase}")

if "اسأل **سؤال واحد فقط" in router or "اسأل سؤالاً واحداً" in router:
    errors.append("router contains a conflicting one-question rule; it must defer to the up-to-3-question flow")

for forbidden in ["INPUT ARTIFACTS", "OUTPUT ARTIFACTS", "STATE UPDATE", "GATE", "NEXT"]:
    if forbidden in output and "internal" not in output.lower():
        errors.append(f"output protocol does not clearly mark internal field: {forbidden}")

if not re.search(r"بحد أقصى.?3 أسئلة|3 أسئلة", flow):
    errors.append("flow does not enforce a maximum of three questions")
if "كتلة Code واحدة فقط لكل فريم" not in flow:
    errors.append("flow does not enforce one code block per frame")

if errors:
    print("OUTPUT CONTRACT VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("OUTPUT CONTRACT VALIDATION PASSED")
print("- staged novice-friendly flow")
print("- storyboard before prompts")
print("- one complete prompt per frame/shot")
print("- external vs in-platform generation gate")
