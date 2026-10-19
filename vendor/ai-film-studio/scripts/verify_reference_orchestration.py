#!/usr/bin/env python3
"""Validate that multi-shot production has an explicit reference orchestration contract."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"missing: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

workflow = read("workflows/M4e-reference-orchestration.md")
router = read("workflows/intent-router.md")
runtime = read("references/protocols/orchestration-runtime.md")
flow = read("references/protocols/user-facing-production-flow.md")
storyboard = read("schemas/storyboard.md")

required = [
    "Reference Manifest", "shot_reference_map", "@image_role", "identity_reference",
    "location_reference", "style_reference", "بوابة الخروج", "approved_asset",
]
for phrase in required:
    if phrase not in workflow:
        errors.append(f"reference workflow missing: {phrase}")

for name, text in [("router", router), ("runtime", runtime), ("user-facing flow", flow), ("storyboard", storyboard)]:
    if "M4e-reference-orchestration" not in text and name != "storyboard":
        errors.append(f"{name} does not require M4e reference orchestration")

if "reference_manifest" not in storyboard or "shot_reference_map" not in storyboard:
    errors.append("storyboard schema missing reference manifest linkage")
if not re.search(r"مراجع.*Storyboard|المرجعيات.*Storyboard|Reference.*Storyboard", flow, re.I):
    errors.append("user-facing flow missing reference pack before storyboard")

if errors:
    print("REFERENCE ORCHESTRATION VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)

print("REFERENCE ORCHESTRATION VALIDATION PASSED")
print("- anchors are explicit and role-bound")
print("- @image slots map to approved assets")
print("- reference gate precedes storyboard and generation")
