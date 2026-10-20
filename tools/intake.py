#!/usr/bin/env python3
"""First-touch intake: greet + exactly 5 option-questions, record answers into a new project,
or auto-derive answers from the user's own request when they skip the form. Stdlib only."""
import argparse, json, re, subprocess, sys
from pathlib import Path
import os
KIT = Path(__file__).resolve().parent.parent

GREETING = "مرحبًا! أنت الآن داخل استوديو عربي موشن — وش تحب نصمم اليوم؟"

QUESTIONS = [
 {"id":"q1","label":"نوع العمل","options":["إعلان منتج","إعلان مطعم/متجر","كشف شعار (logo reveal)","محتوى تعليمي"]},
 {"id":"q2","label":"المدة","options":["15 ثانية","30 ثانية","60 ثانية","90+"]},
 {"id":"q3","label":"المنصة","options":["تيك توك/ريلز (9:16)","يوتيوب (16:9)","مربع (1:1)","شاشة عرض كبيرة (16:9)"]},
 {"id":"q4","label":"الصوت","options":["عندي تعليق صوتي","أولّد تعليقًا","صامت + موسيقى","نقرره لاحقًا"]},
 {"id":"q5","label":"الأسلوب","options":["سينمائي فخم","سريع حماسي","تعليمي نظيف","تجريبي فني"]},
]

def emit():
    print(json.dumps({"greeting":GREETING,
      "ask_via":"host question tool (Claude Code: AskUserQuestion) when available; else numbered options inline",
      "free_text_allowed":True,"questions":QUESTIONS}, ensure_ascii=False, indent=2))

DUR = {"15":15,"30":30,"60":60,"90+":90,"15 ثانية":15,"30 ثانية":30,"60 ثانية":60}

def apply(answers):
    out = {}
    if answers.get("q2"):
        v = DUR.get(str(answers["q2"]).strip())
        if v: out["seconds"] = v
    plat = str(answers.get("q3",""))
    if "9:16" in plat or "تيك" in plat or "ريلز" in plat: out["width"],out["height"] = 1080,1920
    elif "16:9" in plat: out["width"],out["height"] = 1920,1080
    elif "1:1" in plat: out["width"],out["height"] = 1080,1080
    if answers.get("q1"): out["topic_hint"] = answers["q1"]
    if answers.get("q4"): out["audio"] = answers["q4"]
    if answers.get("q5"): out["style"] = answers["q5"]
    return out

def record(answers, name, dest):
    flags = apply(answers)
    proj = Path(dest).expanduser().resolve() / name
    cmd = [sys.executable, str(KIT/"tools/new_project.py"), "--destination", str(proj), "--name", name]
    if flags.get("topic_hint"): cmd += ["--topic", flags["topic_hint"]]
    for k in ("width","height","seconds"):
        if k in flags: cmd += [f"--{k}", str(flags[k])]
    if not flags.get("seconds") or flags.get("seconds",0) <= 30: cmd += ["--quick"]
    subprocess.run(cmd, check=True, capture_output=True)
    (proj/"intake.json").write_text(json.dumps({"answers":answers,"derived":flags}, ensure_ascii=False, indent=2)+"\n")
    bp = proj/"brief.json"
    brief = json.loads(bp.read_text()) if bp.exists() else {}
    brief["intake"] = {"answers":answers,"assumed":[k for k,v in (answers or {}).items() if v in (None,"default")]}
    bp.write_text(json.dumps(brief, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"project":str(proj),"ok":True,"one_line":f"مشروع «{name}» جاهز — {flags.get('seconds','?')}s · {flags.get('width','?')}×{flags.get('height','?')} — أبدأ بإعادة الصياغة"}, ensure_ascii=False))

def defaults(text):
    a = {}
    t = text.lower()
    m = re.search(r"(\d{1,3})\s*(?:ث(?:انية)?|s(?:ec|econds?)?)\b", t)
    if m: a["q2"] = next((k for k in DUR if DUR[k]==min(max(int(m.group(1)),15),90)), "30")
    if any(k in t for k in ("تيك","tiktok","ريلز","reels","shorts","عمودي","رأسية")): a["q3"]="تيك توك/ريلز (9:16)"
    elif any(k in t for k in ("يوتيوب","youtube","عرض","سينمائي")): a["q3"]="يوتيوب (16:9)"
    if any(k in t for k in ("شعار","logo","لوجو","هوية")): a["q1"]="كشف شعار (logo reveal)"
    elif any(k in t for k in ("مطعم","متجر","عرض","قهوة","كوفي")): a["q1"]="إعلان مطعم/متجر"
    elif "تعليم" in t or "شرح" in t: a["q1"]="محتوى تعليمي"
    elif "إعلان" in t or "ad" in t: a["q1"]="إعلان منتج"
    if any(k in t for k in ("بصوتي","صوتي موجود","voiceover","تعليقي")): a["q4"]="عندي تعليق صوتي"
    elif "صامت" in t or "silent" in t: a["q4"]="صامت + موسيقى"
    print(json.dumps({"answers":a,"mode":"auto-derived from user request; do not re-ask these"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    p = argparse.ArgumentParser(); g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--emit", action="store_true"); g.add_argument("--record", metavar="ANSWERS_JSON")
    g.add_argument("--defaults", action="store_true")
    p.add_argument("--text"); p.add_argument("--name"); p.add_argument("--dest", default=".")
    a = p.parse_args()
    if a.emit: emit()
    elif a.defaults: defaults(a.text or "")
    else:
        if not a.name: sys.exit("--record needs --name")
        record(json.loads(a.record), a.name, a.dest)
