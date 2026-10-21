#!/usr/bin/env python3
"""Create/check the project-local contract between AI Film Studio and Motion Forge."""
from __future__ import annotations
import argparse, hashlib, json, time
from pathlib import Path

BRIDGE_VERSION = "1.0"
REQUIRED = ["production-brief.md", "production-sheet.md", "audio-plan.md"]

def project_root(value: str) -> Path:
    p = Path(value).expanduser().resolve()
    if p.name == "project.json":
        return p.parent
    if (p / "project.json").exists():
        return p
    raise SystemExit("project must be a project directory or project.json")

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def init(root: Path, route: str) -> None:
    path = root / "vendor-bridge.json"
    if path.exists():
        raise SystemExit("vendor-bridge.json already exists; refusing to overwrite")
    data = {
        "bridge_version": BRIDGE_VERSION,
        "vendor": {"name": "ai-film-studio", "source": "vendor/ai-film-studio", "route": route, "status": "pending"},
        "local": {"name": "arabic-motion-forge", "status": "waiting_for_vendor_handoff"},
        "required_artifacts": REQUIRED + ["reference-manifest.json"],
        "artifacts": {},
        "approvals": {"direct_execution": False, "vision": "pending", "storyboard": "not_applicable"},
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"created": str(path), "next": REQUIRED}, ensure_ascii=False))

def check(root: Path) -> int:
    path = root / "vendor-bridge.json"
    if not path.exists():
        print(json.dumps({"passed": False, "errors": ["Missing vendor-bridge.json"]}, ensure_ascii=False))
        return 1
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    if data.get("bridge_version") != BRIDGE_VERSION:
        errors.append("Unsupported bridge_version")
    for name in data.get("required_artifacts", REQUIRED):
        f = root / name
        if not f.exists():
            errors.append(f"Missing {name}")
        elif not f.read_text(encoding="utf-8").strip():
            errors.append(f"Empty {name}")
        else:
            data.setdefault("artifacts", {})[name] = {"sha256": sha(f), "bytes": f.stat().st_size}
    if data.get("vendor", {}).get("status") not in {"approved", "complete"}:
        errors.append("Vendor handoff is not approved")
    if not data.get("local", {}).get("status") in {"ready", "in_progress", "complete"}:
        errors.append("Local handoff is not ready")
    if not errors:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0

def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    i = sub.add_parser("init"); i.add_argument("--project", required=True); i.add_argument("--route", required=True)
    c = sub.add_parser("check"); c.add_argument("--project", required=True)
    a = p.parse_args(); root = project_root(a.project)
    if a.command == "init": init(root, a.route); return 0
    return check(root)

if __name__ == "__main__":
    raise SystemExit(main())
