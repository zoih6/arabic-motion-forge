"""Static and functional checks for the activation/onboarding contract."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WELCOME = "مرحبًا! أنت الآن داخل استوديو عربي موشن — وش تحب نصمم اليوم؟"


def main() -> int:
    router = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    start = (ROOT / "skills/start/SKILL.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "tools/intake.py --emit" in router and "exactly 5" in router
    assert "intake" in start and "5 intake questions" in start
    assert "FIRST-REPLY TEMPLATE" in agents and "exactly 5" in agents
    emitted = json.loads(subprocess.run([sys.executable, str(ROOT / "tools/intake.py"), "--emit"], check=True, capture_output=True, text=True).stdout)
    assert emitted["greeting"] == WELCOME and len(emitted["questions"]) == 5
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
            [sys.executable, str(ROOT / "tools/intake.py"), "--record", json.dumps({"q1": "إعلان منتج", "q2": "15 ثانية"}, ensure_ascii=False), "--name", "intake-demo", "--dest", str(project.parent)],
            check=True,
            capture_output=True,
            text=True,
        )
        intake_project = project.parent / "intake-demo"
        brief = json.loads((intake_project / "brief.json").read_text(encoding="utf-8"))
        assert brief["onboarding"]["status"] == "complete"
        assert brief["onboarding"]["answers"]["q1"] == "إعلان منتج"
        journal = (intake_project / "journal.jsonl").read_text(encoding="utf-8")
        assert '"kind": "onboarding"' in journal
    print("activation contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
