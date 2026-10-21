"""Persist conversational onboarding answers without changing production gates.

Usage:
  python3 tools/onboarding.py --project <project>/project.json \
    --answers-json '{"purpose":"...","audience":"..."}'

The agent may ask fewer than four questions. Answers are merged into brief.json,
marked as user-supplied, and recorded in the append-only journal.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="path to project.json")
    parser.add_argument("--answers-json", required=True, help="JSON object of onboarding answers")
    args = parser.parse_args()

    project_path = Path(args.project).expanduser().resolve()
    if project_path.name != "project.json":
        raise SystemExit("--project must point to project.json")
    root = project_path.parent
    brief_path = root / "brief.json"
    journal_path = root / "journal.jsonl"
    if not brief_path.is_file() or not journal_path.is_file():
        raise SystemExit("project is missing brief.json or journal.jsonl")

    try:
        answers = json.loads(args.answers_json)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid --answers-json: {exc}") from exc
    if not isinstance(answers, dict) or not answers:
        raise SystemExit("--answers-json must be a non-empty JSON object")

    brief = json.loads(brief_path.read_text(encoding="utf-8"))
    onboarding = brief.setdefault("onboarding", {})
    saved = onboarding.setdefault("answers", {})
    saved.update(answers)
    onboarding["status"] = "complete"
    onboarding["source"] = "user"
    onboarding["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    brief_path.write_text(json.dumps(brief, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    event = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "kind": "onboarding",
        "event": "answers saved",
        "fields": sorted(answers),
        "next": "reframe brief into spec.md, then directions",
    }
    with journal_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    print(json.dumps({"saved": sorted(answers), "brief": str(brief_path), "journal": str(journal_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
