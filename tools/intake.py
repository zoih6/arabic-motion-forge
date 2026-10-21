#!/usr/bin/env python3
"""First-touch intake: greet + exactly 5 option-questions, record answers into a new project,
or auto-derive answers from the user's own request when they skip the form. Stdlib only."""
import argparse, json, re, subprocess, sys, time
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
GREETING = "مرحبًا! أنت الآن داخل استوديو عربي موشن — وش تحب نصمم اليوم؟"

QUESTIONS = [
    {"id": "q1", "label": "نوع العمل", "options": ["إعلان منتج", "إعلان مطعم/متجر", "كشف شعار (logo reveal)", "محتوى تعليمي"]},
    {"id": "q2", "label": "المدة", "options": ["15 ثانية", "30 ثانية", "60 ثانية", "90+"]},
    {"id": "q3", "label": "المنصة", "options": ["تيك توك/ريلز (9:16)", "يوتيوب (16:9)", "مربع (1:1)", "شاشة عرض كبيرة (16:9)"]},
    {"id": "q4", "label": "الصوت", "options": ["عندي تعليق صوتي", "أولّد تعليقًا", "صامت + موسيقى", "نقرره لاحقًا"]},
    {"id": "q5", "label": "الأسلوب", "options": ["سينمائي فخم", "سريع حماسي", "تعليمي نظيف", "تجريبي فني"]},
]

DUR = {"15": 15, "30": 30, "60": 60, "90+": 90, "15 ثانية": 15, "30 ثانية": 30, "60 ثانية": 60}


def emit():
    print(json.dumps({
        "greeting": GREETING,
        "ask_via": "host question tool (Claude Code: AskUserQuestion) when available; else numbered options inline",
        "free_text_allowed": True,
        "questions": QUESTIONS,
    }, ensure_ascii=False, indent=2))


def apply(answers):
    out = {}
    if answers.get("q2"):
        value = DUR.get(str(answers["q2"]).strip())
        if value:
            out["seconds"] = value
    platform = str(answers.get("q3", ""))
    if "9:16" in platform or "تيك" in platform or "ريلز" in platform:
        out["width"], out["height"] = 1080, 1920
    elif "16:9" in platform:
        out["width"], out["height"] = 1920, 1080
    elif "1:1" in platform:
        out["width"], out["height"] = 1080, 1080
    if answers.get("q1"):
        out["topic_hint"] = answers["q1"]
    if answers.get("q4"):
        out["audio"] = answers["q4"]
    if answers.get("q5"):
        out["style"] = answers["q5"]
    return out


def record(answers, name, dest):
    flags = apply(answers)
    proj = Path(dest).expanduser().resolve() / name
    cmd = [sys.executable, str(KIT / "tools/new_project.py"), "--destination", str(proj), "--name", name]
    if flags.get("topic_hint"):
        cmd += ["--topic", flags["topic_hint"]]
    for key in ("width", "height", "seconds"):
        if key in flags:
            cmd += [f"--{key}", str(flags[key])]
    if not flags.get("seconds") or flags.get("seconds", 0) <= 30:
        cmd += ["--quick"]
    subprocess.run(cmd, check=True, capture_output=True)

    route = "MOTION_GRAPHICS" if answers.get("q1") in {"كشف شعار (logo reveal)", "محتوى تعليمي"} else "COMMERCIAL"
    subprocess.run([
        sys.executable, str(KIT / "tools/vendor_bridge.py"), "init",
        "--project", str(proj / "project.json"), "--route", route,
    ], check=True, capture_output=True)

    (proj / "intake.json").write_text(json.dumps({"answers": answers, "derived": flags}, ensure_ascii=False, indent=2) + "\n")
    brief_path = proj / "brief.json"
    brief = json.loads(brief_path.read_text()) if brief_path.exists() else {}
    brief["intake"] = {"answers": answers, "assumed": [key for key, value in (answers or {}).items() if value in (None, "default")]}
    brief.setdefault("onboarding", {})["status"] = "complete"
    brief["onboarding"]["answers"] = answers
    brief_path.write_text(json.dumps(brief, ensure_ascii=False, indent=2) + "\n")

    event = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "kind": "onboarding",
        "event": "intake answers saved; vendor bridge initialized",
        "fields": sorted(answers),
        "next": "vendor intent-router + production handoff, then reframe and directions",
    }
    with (proj / "journal.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    print(json.dumps({
        "project": str(proj),
        "ok": True,
        "one_line": f"مشروع «{name}» جاهز — {flags.get('seconds', '?')}s · {flags.get('width', '?')}×{flags.get('height', '?')} — أبدأ بمسار vendor ثم التنفيذ",
    }, ensure_ascii=False))


def defaults(text):
    answers = {}
    lowered = text.lower()
    match = re.search(r"(\d{1,3})\s*(?:ث(?:انية)?|s(?:ec|econds?)?)\b", lowered)
    if match:
        answers["q2"] = next((key for key in DUR if DUR[key] == min(max(int(match.group(1)), 15), 90)), "30")
    if any(key in lowered for key in ("تيك", "tiktok", "ريلز", "reels", "shorts", "عمودي", "رأسية")):
        answers["q3"] = "تيك توك/ريلز (9:16)"
    elif any(key in lowered for key in ("يوتيوب", "youtube", "عرض", "سينمائي")):
        answers["q3"] = "يوتيوب (16:9)"
    if any(key in lowered for key in ("شعار", "logo", "لوجو", "هوية")):
        answers["q1"] = "كشف شعار (logo reveal)"
    elif any(key in lowered for key in ("مطعم", "متجر", "عرض", "قهوة", "كوفي")):
        answers["q1"] = "إعلان مطعم/متجر"
    elif "تعليم" in lowered or "شرح" in lowered:
        answers["q1"] = "محتوى تعليمي"
    elif "إعلان" in lowered or "ad" in lowered:
        answers["q1"] = "إعلان منتج"
    if any(key in lowered for key in ("بصوتي", "صوتي موجود", "voiceover", "تعليقي")):
        answers["q4"] = "عندي تعليق صوتي"
    elif "صامت" in lowered or "silent" in lowered:
        answers["q4"] = "صامت + موسيقى"
    print(json.dumps({"answers": answers, "mode": "auto-derived from user request; do not re-ask these"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--emit", action="store_true")
    group.add_argument("--record", metavar="ANSWERS_JSON")
    group.add_argument("--defaults", action="store_true")
    parser.add_argument("--text")
    parser.add_argument("--name")
    parser.add_argument("--dest", default=".")
    args = parser.parse_args()
    if args.emit:
        emit()
    elif args.defaults:
        defaults(args.text or "")
    else:
        if not args.name:
            raise SystemExit("--record needs --name")
        record(json.loads(args.record), args.name, args.dest)
