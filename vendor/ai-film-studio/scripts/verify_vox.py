#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_vox.py — فحص تكامل أنظمة VOX داخل AI Film Studio v3.0.0

يفحص:
  [1] المحركات الخمسة (E1–E5) موجودة بـ frontmatter كامل
  [2] عقود التشغيل في كل محرك
  [3] المسارات الجديدة مسجّلة في intent-router
  [4] بروتوكول التكامل بين المحركات والمراحل
  [5] المواصفات الجديدة (beat, idea, product-truth, entity-ledger, ...)
  [6] المعارف الجديدة (narrative, voice, series, truth)
  [7] حزمة البحث (research) كاملة
  [8] المخططات الجديدة (brief, beat-table, shot-card, ...)
  [9] البوابات الموسّعة G9–G13 وقوائم الفحص
  [10] shortcuts جديدة (thumbnail, series, documentary, product-shot)

الاستخدام:
    python3 scripts/verify_vox.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ENGINES = {
    "E1-documentary-engine.md": ["name", "description", "tier", "parent"],
    "E2-commercial-engine.md": ["name", "description", "tier", "parent"],
    "E3-hybrid-commercial.md": ["name", "description", "tier", "parent"],
    "E4-series-engine.md": ["name", "description", "tier", "parent"],
    "E5-bulk-production-pipeline.md": ["name", "description", "tier", "parent"],
}

NEW_SPECS = [
    "beat-architecture.md", "idea-engine.md", "product-truth.md",
    "entity-ledger.md", "model-dialects.md", "thumbnail-dna.md",
    "platform-specs.md", "brief-spec.md",
]

NEW_KNOWLEDGE = [
    "narrative-writing-dna.md", "voice-system.md",
    "series-architecture.md", "truth-and-safety.md",
]

NEW_PROTOCOLS = [
    "discovery-protocol.md", "style-lock-protocol.md", "engine-interop.md",
]

RESEARCH = [
    "README.md", "search-playbook.md", "reference-mining.md",
    "fact-verification.md", "trend-research.md", "query-library.md",
]

NEW_SCHEMAS = [
    "brief.md", "beat-table.md", "shot-card.md", "product-sheet.md",
    "edit-sheet.md", "end-card.md", "thumbnail-pack.md",
    "delivery-pack.md", "series-bible.md", "prompts-txt.md",
]

NEW_QUALITY = ["gates-extended.md", "pre-flight-checklist.md", "ten-second-test.md"]

NEW_SHORTCUTS = ["thumbnail.md", "series.md", "documentary.md", "product-shot.md"]

results: list[tuple[bool, str]] = []


def check(ok: bool, msg: str) -> None:
    results.append((ok, msg))


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def has_frontmatter_field(text: str, field: str) -> bool:
    return bool(re.search(rf"^{field}:", text, re.M))


def main() -> int:
    print()
    print("=" * 64)
    print(" فحص تكامل أنظمة VOX — AI Film Studio v3.0.0")
    print("=" * 64)

    # [1] المحركات
    print("\n[1] المحركات الخمسة (E1–E5)")
    engines_dir = ROOT / "workflows" / "engines"
    for fname, fields in ENGINES.items():
        path = engines_dir / fname
        text = read(path)
        exists = path.is_file()
        print(f"  {'✓' if exists else '✗'} {fname}"
              + (f" ({len(text)} حرف)" if exists else " — غير موجود"))
        check(exists, f"المحرك {fname} موجود")
        if exists:
            for f in fields:
                ok = has_frontmatter_field(text, f)
                check(ok, f"{fname}: حقل {f} في frontmatter")
            # عقد تشغيل: entry_conditions تُحدد متى يُستخدم المحرك
            ok = has_frontmatter_field(text, "entry_conditions")
            check(ok, f"{fname}: عقد تشغيل (entry_conditions)")
            print(f"     {'✓' if ok else '✗'} عقد تشغيل (entry_conditions)")

    readme = engines_dir / "README.md"
    ok = readme.is_file()
    check(ok, "workflows/engines/README.md موجود")
    print(f"  {'✓' if ok else '✗'} engines/README.md")

    # [2] المسارات في intent-router
    print("\n[2] المسارات الجديدة في intent-router.md")
    router = read(ROOT / "workflows" / "intent-router.md")
    for route in ["E1", "E2", "E3", "E4", "E5", "VOX", "DOCUMENTARY", "COMMERCIAL"]:
        ok = route in router
        check(ok, f"intent-router يذكر {route}")
        print(f"  {'✓' if ok else '✗'} {route}")

    # [3] بروتوكول التكامل
    print("\n[3] بروتوكولات v3")
    for fname in NEW_PROTOCOLS:
        path = ROOT / "references" / "protocols" / fname
        ok = path.is_file() and len(read(path)) > 500
        check(ok, f"protocols/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} protocols/{fname}")

    # [4] المواصفات
    print("\n[4] المواصفات الجديدة (specs)")
    for fname in NEW_SPECS:
        path = ROOT / "references" / "specs" / fname
        ok = path.is_file() and len(read(path)) > 500
        check(ok, f"specs/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} specs/{fname}")

    # [5] المعارف
    print("\n[5] المعارف الجديدة (knowledge)")
    for fname in NEW_KNOWLEDGE:
        path = ROOT / "references" / "knowledge" / fname
        ok = path.is_file() and len(read(path)) > 500
        check(ok, f"knowledge/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} knowledge/{fname}")

    # [6] حزمة البحث
    print("\n[6] حزمة البحث (research)")
    for fname in RESEARCH:
        path = ROOT / "references" / "research" / fname
        ok = path.is_file() and len(read(path)) > 400
        check(ok, f"research/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} research/{fname}")

    # [7] المخططات
    print("\n[7] المخططات الجديدة (schemas)")
    for fname in NEW_SCHEMAS:
        path = ROOT / "schemas" / fname
        ok = path.is_file() and len(read(path)) > 400
        check(ok, f"schemas/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} schemas/{fname}")

    # [8] الجودة
    print("\n[8] بوابات الجودة الموسّعة")
    for fname in NEW_QUALITY:
        path = ROOT / "quality" / fname
        ok = path.is_file() and len(read(path)) > 500
        check(ok, f"quality/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} quality/{fname}")

    gates = read(ROOT / "quality" / "gates-extended.md")
    for g in ["G9", "G10", "G11", "G12", "G13"]:
        ok = g in gates
        check(ok, f"gates-extended يحدد {g}")
        print(f"  {'✓' if ok else '✗'} البوابة {g}")

    # [9] الاختصارات
    print("\n[9] المسارات السريعة الجديدة (shortcuts)")
    for fname in NEW_SHORTCUTS:
        path = ROOT / "workflows" / "shortcuts" / fname
        ok = path.is_file() and len(read(path)) > 300
        check(ok, f"shortcuts/{fname} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} shortcuts/{fname}")

    # [10] الإسناد
    print("\n[10] إسناد المنشئ")
    credits = read(ROOT / "CREDITS.md")
    ok = "Waseem Alzobiri" in credits
    check(ok, "CREDITS.md يذكر Waseem Alzobiri")
    print(f"  {'✓' if ok else '✗'} CREDITS.md")

    skill = read(ROOT / "SKILL.md")
    ok = "3.2.0" in skill and "Waseem Alzobiri" in skill
    check(ok, "SKILL.md بالإصدار 3.2.0 وبإسناد المنشئ")
    print(f"  {'✓' if ok else '✗'} SKILL.md v3.2.0")

    # النتيجة
    passed = sum(1 for ok, _ in results if ok)
    failed = [m for ok, m in results if not ok]
    total = len(results)

    print()
    print("=" * 64)
    print(f"النتيجة: {passed} نجح · {len(failed)} فشل (من {total})")
    if failed:
        print("\nالفاشلة:")
        for m in failed:
            print(f"  ✗ {m}")
        print("=" * 64)
        return 1
    print("✅ تكامل أنظمة VOX مكتمل — كل المحركات والمراجع الجديدة سليمة")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
