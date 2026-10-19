#!/usr/bin/env python3
"""AI Film Studio prompt compiler.

Compiles a model-agnostic shot specification into model-ready image/video
prompts. The compiler is intentionally deterministic: reference slots and
camera instructions are generated from structured input, never guessed from
free-form prompt fragments.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

VERSION = "1.0.0"

MODEL_ALIASES = {
    "nano-banana-2": "gemini-3.1-flash-image",
    "nano-banana-2-pro": "gemini-3-pro-image-preview",
    "nano_banana_2": "gemini-3.1-flash-image",
    "gpt-image-2": "gpt-image-2",
    "seedance-2": "bytedance/seedance-2.0",
    "seedance-2.0": "bytedance/seedance-2.0",
    "omni": "gemini-omni-1.1-flash",
    "omni-flash": "gemini-omni-1.1-flash",
    "veo": "veo-3",
}

PROFILES: dict[str, dict[str, Any]] = {
    "gemini-3.1-flash-image": {"kind": "image", "max_images": 10, "syntax": "natural"},
    "gemini-3-pro-image-preview": {"kind": "image", "max_images": 14, "syntax": "natural"},
    "gpt-image-2": {"kind": "image", "max_images": 16, "syntax": "natural"},
    "bytedance/seedance-2.0": {"kind": "video", "max_images": 9, "max_duration": 15, "syntax": "seedance"},
    "gemini-omni-1.1-flash": {"kind": "video", "max_images": 10, "max_duration": 10, "syntax": "omni"},
    "veo-3": {"kind": "video", "max_images": 10, "max_duration": 8, "syntax": "veo"},
    "runwayml/gen4": {"kind": "video", "max_images": 3, "max_duration": 10, "syntax": "natural"},
    "kling-2.1": {"kind": "video", "max_images": 4, "max_duration": 10, "syntax": "natural"},
    "sora": {"kind": "video", "max_images": 4, "max_duration": 20, "syntax": "natural"},
}

ROLE_ORDER = {
    "first_frame": 0,
    "last_frame": 1,
    "identity_reference": 10,
    "character_reference": 10,
    "costume_reference": 20,
    "prop_reference": 30,
    "location_reference": 40,
    "style_reference": 50,
    "motion_reference": 60,
    "audio_reference": 70,
}

CAMERA_TYPES = {
    "static": "locked-off static camera",
    "pan": "a slow pan",
    "tilt": "a slow tilt",
    "dolly_in": "a slow forward dolly",
    "dolly_out": "a slow backward dolly",
    "truck_left": "a smooth truck left",
    "truck_right": "a smooth truck right",
    "arc_left": "a controlled arc to camera-left",
    "arc_right": "a controlled arc to camera-right",
    "crane_up": "a slow crane up",
    "crane_down": "a slow crane down",
    "handheld": "subtle handheld movement",
}


def fail(message: str) -> None:
    raise ValueError(message)


def text(value: Any, default: str = "") -> str:
    if value is None:
        return default
    if isinstance(value, (list, tuple)):
        return ", ".join(text(x) for x in value if text(x))
    if isinstance(value, dict):
        return "; ".join(f"{k}: {text(v)}" for k, v in value.items() if text(v))
    return str(value).strip()


def normalize_model(model: str) -> str:
    normalized = MODEL_ALIASES.get(model.lower().strip(), model.strip())
    if normalized not in PROFILES:
        fail(f"Unsupported model '{model}'. Add a verified profile before compiling.")
    return normalized


def normalize_shots(payload: dict[str, Any]) -> list[dict[str, Any]]:
    shots = payload.get("shots")
    if not isinstance(shots, list) or not shots:
        fail("Input must contain a non-empty 'shots' array.")
    return shots


def normalize_refs(shot: dict[str, Any], manifest: dict[str, Any], model: str) -> list[dict[str, Any]]:
    anchors = {a.get("anchor_id"): a for a in manifest.get("anchors", []) if a.get("anchor_id")}
    entries = shot.get("references")
    if entries is None:
        entries = shot.get("anchor_ids")
    # When a shot does not provide a subset, use all locked anchors. This is
    # the automatic mode: the compiler still assigns a role from the anchor
    # kind and validates the provider limit before emitting @ImageN.
    if not entries:
        entries = []
        for anchor_id, anchor in anchors.items():
            kind = text(anchor.get("kind")).lower()
            role = "identity_reference"
            if "location" in kind or "world" in kind:
                role = "location_reference"
            elif "style" in kind or "light" in kind:
                role = "style_reference"
            elif "costume" in kind or "wardrobe" in kind:
                role = "costume_reference"
            elif "prop" in kind or "object" in kind:
                role = "prop_reference"
            entries.append({"anchor_id": anchor_id, "role": role})
    if not isinstance(entries, list):
        fail(f"{shot.get('shot_id', '<shot>')}: references must be an array.")
    refs: list[dict[str, Any]] = []
    for entry in entries:
        if isinstance(entry, str):
            anchor_id, role = entry, "identity_reference"
        elif isinstance(entry, dict):
            anchor_id = entry.get("anchor_id") or entry.get("id")
            role = entry.get("role", "identity_reference")
        else:
            fail(f"Invalid reference entry in {shot.get('shot_id')}: {entry!r}")
        if anchor_id not in anchors:
            fail(f"{shot.get('shot_id')}: reference '{anchor_id}' is not defined in manifest.")
        anchor = deepcopy(anchors[anchor_id])
        if anchor.get("status") not in {"approved", "locked"}:
            fail(f"{shot.get('shot_id')}: reference '{anchor_id}' is not approved or locked.")
        if not anchor.get("approved_asset"):
            fail(f"{shot.get('shot_id')}: reference '{anchor_id}' has no approved_asset.")
        refs.append({"anchor_id": anchor_id, "role": role, "asset": anchor["approved_asset"], "description": anchor.get("locked_description", "")})

    # First/last frames are explicit shot fields and are inserted before general references.
    for key, role in (("first_frame", "first_frame"), ("last_frame", "last_frame")):
        if shot.get(key):
            anchor_id = shot[key]
            if anchor_id not in anchors:
                fail(f"{shot.get('shot_id')}: {key} '{anchor_id}' is not defined in manifest.")
            anchor = anchors[anchor_id]
            if anchor.get("status") not in {"approved", "locked"} or not anchor.get("approved_asset"):
                fail(f"{shot.get('shot_id')}: {key} '{anchor_id}' is not an approved asset.")
            refs.insert(0 if role == "first_frame" else 1, {"anchor_id": anchor_id, "role": role, "asset": anchor["approved_asset"], "description": anchor.get("locked_description", "")})

    refs.sort(key=lambda r: (ROLE_ORDER.get(r["role"], 90), r["anchor_id"]))
    if len(refs) > PROFILES[model]["max_images"]:
        fail(f"{shot.get('shot_id')}: {len(refs)} image references exceed {model}'s limit of {PROFILES[model]['max_images']}.")
    for index, ref in enumerate(refs, 1):
        ref["slot"] = f"@Image{index}"
        ref["provider_index"] = index - 1 if model == "gemini-omni-1.1-flash" else index
    return refs


def camera_instruction(camera: dict[str, Any], model: str) -> tuple[str, dict[str, Any]]:
    camera = camera or {}
    move = text(camera.get("movement", "static"))
    if move not in CAMERA_TYPES:
        fail(f"Unsupported camera movement '{move}'. Use one of: {', '.join(CAMERA_TYPES)}")
    speed = text(camera.get("speed", "slow"))
    direction = text(camera.get("direction"))
    duration = text(camera.get("duration"))
    lens = text(camera.get("lens", "50mm"))
    aperture = text(camera.get("aperture", "f/2.8"))
    angle = text(camera.get("angle", "eye level"))
    parts = [CAMERA_TYPES[move]]
    if direction and move in {"pan", "tilt", "dolly_in", "dolly_out", "truck_left", "truck_right", "arc_left", "arc_right"}:
        parts.append(direction)
    parts.append(f"at {speed} speed")
    if duration:
        parts.append(f"over {duration}")
    movement = " ".join(parts)
    common = {"movement": move, "speed": speed, "lens": lens, "aperture": aperture, "angle": angle}
    if model == "bytedance/seedance-2.0":
        rendered = f"Camera: {movement}. Lens: {lens} at {aperture}; {angle} angle. One camera move only; no zoom, no rotation."
    elif model == "gemini-omni-1.1-flash":
        rendered = f"Camera: {movement}, fixed {lens} lens at {aperture}, {angle} angle, no rotation and no zoom."
    elif model == "veo-3":
        rendered = f"Cinematography: {movement}, {lens} lens at {aperture}, {angle} camera angle. Keep the move physically smooth and continuous."
    else:
        rendered = f"Camera: {movement}, {lens} lens at {aperture}, {angle} angle."
    return rendered, common


def reference_lines(refs: list[dict[str, Any]], model: str, first_frame: bool = False) -> list[str]:
    lines = []
    for ref in refs:
        role = ref["role"].replace("_", " ")
        if model == "bytedance/seedance-2.0":
            role = {
                "identity reference": "character reference",
                "location reference": "background environment",
                "costume reference": "costume reference",
                "prop reference": "prop reference",
                "style reference": "style reference",
            }.get(role, role)
            if ref["role"] == "first_frame":
                lines.append(f"{ref['slot']} as the exact first frame.")
            elif ref["role"] == "last_frame":
                lines.append(f"{ref['slot']} as the exact last frame.")
            else:
                lines.append(f"{ref['slot']} as {role}; use it only for {role}, not for other identities.")
        elif model == "gemini-omni-1.1-flash":
            if ref["role"] in {"first_frame", "last_frame"}:
                continue
            lines.append(f"[# References {ref['slot']}] Use {ref['slot']} as the {role}.")
        else:
            lines.append(f"Reference {ref['slot']} ({role}) is the approved asset for {ref['anchor_id']}: {ref['asset']}.")
    return lines


def timeline(shot: dict[str, Any], duration: int) -> list[str]:
    beats = shot.get("timing") or shot.get("beats") or []
    if isinstance(beats, dict):
        beats = [{"range": k, "action": v} for k, v in beats.items()]
    if beats:
        out = []
        for beat in beats:
            if isinstance(beat, str):
                out.append(beat)
            else:
                out.append(f"[{text(beat.get('range', '0s'))}] {text(beat.get('action', beat.get('description', '')))}")
        return out
    action = text(shot.get("action", "the subject performs one clear controlled action"))
    midpoint = max(1, duration // 2)
    return [f"[0-{midpoint}s] begin the action: {action}.", f"[{midpoint}-{duration}s] complete the action and settle into the defined end state."]


def common_sections(shot: dict[str, Any], refs: list[dict[str, Any]], model: str) -> tuple[list[str], dict[str, Any]]:
    subject = shot.get("subject", {})
    environment = shot.get("environment", {})
    style = shot.get("style", {})
    constraints = shot.get("constraints", [])
    camera, camera_meta = camera_instruction(shot.get("camera", {}), model)
    identity = text(subject.get("identity_string"))
    if not identity and any(r["role"] in {"identity_reference", "character_reference"} for r in refs):
        identity = "preserve the approved character identity exactly from the identity reference"
    sections = [
        f"Intent: {text(shot.get('intent', shot.get('purpose', 'Create the specified shot.')))}",
        f"Subject: {identity or text(subject.get('description', 'the specified subject'))}.",
    ]
    wardrobe = text(subject.get("wardrobe"))
    props = text(subject.get("props"))
    if wardrobe:
        sections.append(f"Wardrobe: {wardrobe}.")
    if props:
        sections.append(f"Props: {props}.")
    pose = text(subject.get("pose"))
    if pose:
        sections.append(f"Pose and gaze: {pose}.")
    composition = text(shot.get("composition", ""))
    if composition:
        sections.append(f"Composition: {composition}.")
    location = text(environment.get("location", environment.get("description", "")))
    environment_bits = ", ".join(filter(None, [location, text(environment.get("time_of_day")), text(environment.get("weather")), text(environment.get("materials")), text(environment.get("atmosphere"))]))
    if environment_bits:
        sections.append(f"Environment: {environment_bits}.")
    sections.append(camera)
    lighting = text(shot.get("lighting", environment.get("lighting", "")))
    if lighting:
        sections.append(f"Lighting: {lighting}.")
    palette = text(style.get("palette", style.get("color_palette", "")))
    texture = text(style.get("texture", ""))
    if palette or texture:
        sections.append(f"Color and texture: {', '.join(filter(None, [palette, texture]))}.")
    if constraints:
        sections.append(f"Constraints: {text(constraints)}.")
    metadata = {"camera": camera_meta, "references": refs}
    return sections, metadata


def compile_image(shot: dict[str, Any], refs: list[dict[str, Any]], model: str) -> tuple[str, dict[str, Any]]:
    sections, metadata = common_sections(shot, refs, model)
    prompt = "Cinematic film still, single frame.\n\n" + "\n".join(sections)
    prompt += "\nAnatomically correct hands, natural limb proportions, no unintended people, no extra limbs, no gibberish text."
    metadata.update({"output_type": "image", "model": model, "aspect_ratio": shot.get("aspect_ratio", "16:9")})
    return prompt, metadata


def compile_video(shot: dict[str, Any], refs: list[dict[str, Any]], model: str) -> tuple[str, dict[str, Any]]:
    profile = PROFILES[model]
    duration = int(shot.get("duration", 8))
    if not profile.get("max_duration") or duration < 3 or duration > profile["max_duration"]:
        fail(f"{shot.get('shot_id')}: duration {duration}s is not supported by {model} (max {profile.get('max_duration')}).")
    sections, metadata = common_sections(shot, refs, model)
    action = text(shot.get("action", "one clear primary action"))
    lines = reference_lines(refs, model)
    lines += sections[:2]
    if model == "bytedance/seedance-2.0":
        if any(r["role"] == "first_frame" for r in refs) and any(r["role"] not in {"first_frame", "last_frame"} for r in refs):
            fail(f"{shot.get('shot_id')}: Seedance cannot combine first/last frames with other image references.")
        lines += [f"Primary action: {action}."] + timeline(shot, duration) + sections[2:]
        lines += ["Keep identity, wardrobe, props, lighting, and screen direction identical. Avoid jitter, bent limbs, teleportation, and unexplained cuts.", f"Sound: {text(shot.get('sound', 'continuous natural ambience, no extra dialogue'))}."]
    elif model == "gemini-omni-1.1-flash":
        if not any(r["role"] == "first_frame" for r in refs):
            lines.insert(0, "Create a continuous video shot with no scene cuts.")
        else:
            lines.insert(0, "Use the supplied image as the starting frame.")
        lines += [f"Primary action: {action}.", "Timing: " + "; ".join(timeline(shot, duration)), camera_instruction(shot.get("camera", {}), model)[0], f"Audio: {text(shot.get('sound', 'continuous environmental ambience, no music'))}.", "Preserve face, hair, costume, props, screen direction, and light direction exactly. No dialogue unless explicitly specified."]
    elif model == "veo-3":
        lines += [f"Action: {action}.", "Timeline: " + "; ".join(timeline(shot, duration)), sections[2:], f"Sound and dialogue: {text(shot.get('sound', 'natural synchronized sound'))}.", "One continuous shot, coherent physical motion, preserve the approved references exactly."]
    else:
        lines += [f"Action: {action}.", "Timeline: " + "; ".join(timeline(shot, duration)), sections[2:], "Preserve all identity and continuity locks; one dominant camera move only."]
    prompt = "\n".join(x for x in lines if x)
    metadata.update({"output_type": "video", "model": model, "duration": duration, "aspect_ratio": shot.get("aspect_ratio", "16:9")})
    return prompt, metadata


def compile_payload(payload: dict[str, Any]) -> dict[str, Any]:
    manifest = payload.get("reference_manifest") or payload.get("manifest")
    if not isinstance(manifest, dict):
        fail("Input must contain 'reference_manifest'.")
    model = normalize_model(payload.get("model", "bytedance/seedance-2.0"))
    outputs = []
    for shot in normalize_shots(payload):
        shot_id = shot.get("shot_id")
        if not shot_id:
            fail("Every shot must contain shot_id.")
        refs = normalize_refs(shot, manifest, model)
        output_type = shot.get("output_type", "video" if PROFILES[model]["kind"] == "video" else "image")
        if output_type == "image":
            prompt, metadata = compile_image(shot, refs, model)
        elif output_type in {"video", "image_to_video", "text_to_video"}:
            prompt, metadata = compile_video(shot, refs, model)
        else:
            fail(f"{shot_id}: unsupported output_type '{output_type}'.")
        outputs.append({"shot_id": shot_id, "prompt_id": f"{shot_id}_{output_type}_v1", "prompt": prompt, "metadata": metadata, "reference_map": refs})
    return {"compiler": {"name": "ai-film-studio-prompt-compiler", "version": VERSION}, "model": model, "outputs": outputs}


def markdown(result: dict[str, Any]) -> str:
    chunks = [f"# Compiled Prompt Package\n\n**Compiler:** {result['compiler']['name']} v{result['compiler']['version']}  \n**Model:** `{result['model']}`\n"]
    for item in result["outputs"]:
        meta = item["metadata"]
        chunks.append(f"## {item['shot_id']}\n\n**Prompt ID:** `{item['prompt_id']}`  \n**Output:** `{meta['output_type']}`  \n**References:** " + ", ".join(f"`{r['slot']}` = `{r['anchor_id']}` ({r['role']})" for r in item["reference_map"]) + "\n\n```text\n" + item["prompt"] + "\n```\n")
    return "\n".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile AI Film Studio canonical shot specs into model-ready prompts")
    parser.add_argument("input", type=Path, help="canonical JSON input")
    parser.add_argument("-o", "--output", type=Path, help="JSON output path")
    parser.add_argument("--markdown", type=Path, help="optional Markdown package output")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        result = compile_payload(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"PROMPT COMPILER ERROR: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    if args.markdown:
        args.markdown.write_text(markdown(result), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
