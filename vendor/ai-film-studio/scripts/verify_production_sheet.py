#!/usr/bin/env python3
"""تحقق بنيوي خفيف من عقد ورقة الإنتاج المتكيفة."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def need(text, phrase, label):
    if phrase not in text:
        errors.append(f"{label}: missing {phrase}")

schema = (ROOT / "schemas/production-sheet.md").read_text(encoding="utf-8")
workflow = (ROOT / "workflows/adaptive-production-sheet.md").read_text(encoding="utf-8")
example = (ROOT / "examples/production-sheet-10s.md").read_text(encoding="utf-8")
for phrase in ["duration_seconds", "time_in", "time_out", "story_role", "viewer_takeaway", "visual_action", "reference_ids", "audio_plan", "continuity_locks", "acceptance_criteria"]:
    need(schema, phrase, "schema")
for phrase in ["نوع الطلب", "توزيع الزمن", "production sheet → Storyboard", "زر تصدير CSV", "10s شورت"]:
    need(workflow, phrase, "workflow")
for phrase in ["10 ثوانٍ", "SC01_SH01", "SC01_SH02", "SC01_SH03", "مجموع اللقطات = 10.0 ثانية"]:
    need(example, phrase, "example")

# Ensure the example's time boundaries form a contiguous 10-second sequence.
rows = re.findall(r"\| SC01 \| SC01_SH\d+ \| ([0-9.]+) \| ([0-9.]+) \| ([0-9.]+) \|", example)
if len(rows) != 3:
    errors.append(f"example: expected 3 shot rows, found {len(rows)}")
else:
    values = [(float(a), float(b), float(d)) for a, b, d in rows]
    if abs(values[0][0]) > 0.001 or any(abs(values[i][1] - values[i+1][0]) > 0.001 for i in range(2)):
        errors.append("example: shot timeline has a gap or overlap")
    if abs(values[-1][1] - 10.0) > 0.001 or abs(sum(v[2] for v in values) - 10.0) > 0.001:
        errors.append("example: shot durations do not total 10 seconds")

if errors:
    print("PRODUCTION SHEET VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PRODUCTION SHEET VALIDATION PASSED")
print("- adaptive schema present")
print("- workflow covers duration/type adaptation")
print("- 10-second example timeline is contiguous")
