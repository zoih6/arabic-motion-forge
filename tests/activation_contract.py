"""Static and functional checks for the activation/onboarding contract."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WELCOME = "مرحباً بك في استديو عربي موشن."
PROMPT = "وش تحب نصمم اليوم؟"


def main() -> int:
    router = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    start = (ROOT / "skills/start/SKILL.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    welcome = (ROOT / "skills/start/welcome.txt").read_text(encoding="utf-8").strip().splitlines()
    assert welcome == [WELCOME, PROMPT]
    assert "welcome.txt" in start and "Activation only" in start
    assert "welcome.txt" in agents and "activation-only" in agents
    assert WELCOME in router and PROMPT in router
    assert '"skills": "./skills/"' in (ROOT / ".claude-plugin/plugin.json").read_text()

    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp) / "demo"
        subprocess.run(
            [sys.executable, str(ROOT / "tools/new_project.py"), "--destination", str(project), "--name", "demo", "--topic", "اختبار", "--quick"],
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            [sys.executable, str(ROOT / "tools/onboarding.py"), "--project", str(project / "project.json"), "--answers-json", json.dumps({"purpose": "إعلان", "audience": "شباب"}, ensure_ascii=False)],
            check=True,
            capture_output=True,
            text=True,
        )
        brief = json.loads((project / "brief.json").read_text(encoding="utf-8"))
        assert brief["onboarding"]["status"] == "complete"
        assert brief["onboarding"]["answers"]["purpose"] == "إعلان"
        journal = (project / "journal.jsonl").read_text(encoding="utf-8")
        assert '"kind": "onboarding"' in journal
    print("activation contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
