#!/usr/bin/env python3
"""Deterministic tests for prompt_compiler.py."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from prompt_compiler import compile_payload  # noqa: E402

fixture = json.loads((ROOT / "examples/compiler-fixture.json").read_text(encoding="utf-8"))
result = compile_payload(fixture)
item = result["outputs"][0]
prompt = item["prompt"]
refs = item["reference_map"]

assert result["model"] == "bytedance/seedance-2.0"
assert [r["slot"] for r in refs] == ["@Image1", "@Image2", "@Image3", "@Image4", "@Image5"]
assert "@Image1" in prompt and "@Image5" in prompt
assert "@Image1 as character reference" in prompt
assert "@Image4 as background environment" in prompt
assert "Camera: a slow forward dolly" in prompt
assert "one camera move only" in prompt.lower()
assert "[2-5s] the hero takes one step forward" in prompt

# First/last-frame plus regular references must fail for Seedance.
bad = json.loads(json.dumps(fixture))
bad["shots"][0]["first_frame"] = "CHAR-01-ID"
try:
    compile_payload(bad)
except ValueError as exc:
    assert "cannot combine first/last frames" in str(exc)
else:
    raise AssertionError("Seedance frame/reference conflict was not rejected")

# Omni uses zero-based provider indexes and emits its native reference syntax.
omni = json.loads(json.dumps(fixture))
omni["model"] = "omni-flash"
omni["shots"][0]["duration"] = 8
omni_result = compile_payload(omni)
omni_item = omni_result["outputs"][0]
assert omni_item["reference_map"][0]["provider_index"] == 0
assert "[# References @Image1]" in omni_item["prompt"]
assert "continuous video shot" in omni_item["prompt"]

print("PROMPT COMPILER TESTS PASSED")
print("- automatic @Image slot assignment: 5 references")
print("- model-specific camera translation: Seedance")
print("- model-specific reference syntax: Omni")
print("- unsupported Seedance frame/reference combination rejected")
