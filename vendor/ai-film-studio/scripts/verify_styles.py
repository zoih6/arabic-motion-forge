#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_styles.py — فحص سلامة مكتبة الأنماط البصرية (v3.0.0)

يفحص:
  [1] وجود الأقفال العشرة (LOCK A–J)
  [2] طول كل قفل (20–120 كلمة)
  [3] خلو الأقفال من الكلمات الفارغة المحظورة
  [4] وجود بند معاملة المنتج في الأقفال التجارية
  [5] الرموز: {AR} موجود · {PALETTE} أو لوحة مثبّتة
  [6] تسجيل كل قفل في styles/index.md
  [7] الخواتيم الثلاثة موجودة
  [8] برومبت الفيديو الموحد سليم
  [9] فهرس الأنماط + القالب موجودان

الاستخدام:
    python3 scripts/verify_styles.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCKS_DIR = ROOT / "styles" / "locks"
INDEX = ROOT / "styles" / "index.md"
STYLES_README = ROOT / "styles" / "README.md"
TEMPLATE = ROOT / "styles" / "style-pack-template.md"

# الأقفال التي يجب أن تحتوي بند المنتج الصريح
PRODUCT_LOCKS = {"B", "C", "D", "E", "G", "H", "J"}
# الأقفال التي تستخدم {PALETTE} (البقية لوحتها مثبّتة داخل النص)
PALETTE_LOCKS = {"B", "D", "F", "H", "I", "J"}
# الأقفال ذات اللوحة المثبّتة — يجب أن تذكر ألوانًا/إضاءة صريحة
FIXED_PALETTE_LOCKS = {"A", "C", "E", "G"}
COLOR_HINT = re.compile(
    r"\b(tan|ink|black|sand|brass|gold|gray|grey|white|cream|blue|green|"
    r"neutral|daylight|haze|warm|cool|charcoal)\b", re.I)
# الكلمات الفارغة المحظورة داخل الأقفال
FORBIDDEN = ["beautiful", "amazing", "stunning", "masterpiece",
             "trending", "award winning", "best quality", "ultra quality"]

results: list[tuple[bool, str]] = []


def check(ok: bool, msg: str) -> None:
    results.append((ok, msg))


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def main() -> int:
    print()
    print("=" * 64)
    print(" فحص مكتبة الأنماط — Style Locks (v3.0.0)")
    print("=" * 64)

    if not LOCKS_DIR.is_dir():
        print("❌ مجلد styles/locks/ غير موجود")
        return 1

    # [1] وجود الأقفال
    print("\n[1] وجود الأقفال العشرة (LOCK A–J)")
    lock_files = {}
    for letter in "ABCDEFGHIJ":
        matches = sorted(LOCKS_DIR.glob(f"LOCK-{letter}-*.txt"))
        ok = len(matches) == 1
        check(ok, f"LOCK-{letter} {'موجود' if ok else 'مفقود أو مكرر'}")
        print(f"  {'✓' if ok else '✗'} LOCK-{letter}"
              + (f" — {matches[0].name}" if matches else " — غير موجود"))
        if matches:
            lock_files[letter] = matches[0]

    # [2] الطول
    print("\n[2] طول القفل (20–120 كلمة)")
    for letter, path in lock_files.items():
        text = read(path).strip()
        n = words(text)
        ok = 20 <= n <= 120
        check(ok, f"LOCK-{letter} الطول {n} كلمة")
        print(f"  {'✓' if ok else '✗'} LOCK-{letter} — {n} كلمة")

    # [3] الكلمات الفارغة
    print("\n[3] خلو الأقفال من الكلمات الفارغة")
    for letter, path in lock_files.items():
        text = read(path).lower()
        hits = [w for w in FORBIDDEN if w in text]
        ok = not hits
        check(ok, f"LOCK-{letter} خالٍ من الكلمات الفارغة"
                  + (f" (وُجد: {', '.join(hits)})" if hits else ""))
        print(f"  {'✓' if ok else '✗'} LOCK-{letter}"
              + (f" — كلمة فارغة: {hits}" if hits else " — نظيف"))

    # [4] بند المنتج
    print("\n[4] بند معاملة المنتج (الأقفال التجارية B,C,D,E,G,H)")
    for letter in sorted(PRODUCT_LOCKS):
        if letter not in lock_files:
            continue
        text = read(lock_files[letter])
        ok = "REAL PHOTOGRAPHIC OBJECT" in text
        check(ok, f"LOCK-{letter} يحتوي بند المنتج الواقعي")
        print(f"  {'✓' if ok else '✗'} LOCK-{letter} — بند المنتج")

    # [5] الرموز واللوحة
    # ملاحظة معمارية: نسبة الأبعاد {AR} تُحدَّد في الخاتمة (Closer) لا في القفل،
    # بينما اللوحة {PALETTE} تُحدَّد في القفل. لذلك يُفحص كلٌّ في موضعه.
    print("\n[5] اللوحة في الأقفال · {AR} في الخواتيم")
    for letter in sorted(PALETTE_LOCKS):
        if letter not in lock_files:
            continue
        ok = "{PALETTE}" in read(lock_files[letter])
        check(ok, f"LOCK-{letter} يستخدم {{PALETTE}}")
        print(f"  {'✓' if ok else '✗'} LOCK-{letter} — {{PALETTE}}")

    for letter in sorted(FIXED_PALETTE_LOCKS):
        if letter not in lock_files:
            continue
        ok = bool(COLOR_HINT.search(read(lock_files[letter])))
        check(ok, f"LOCK-{letter} لوحته مثبّتة داخل النص")
        print(f"  {'✓' if ok else '✗'} LOCK-{letter} — لوحة مثبّتة داخل النص")

    # [6] التسجيل في الفهرس
    print("\n[6] تسجيل الأقفال في styles/index.md")
    index_text = read(INDEX)
    for letter in "ABCDEFGHIJ":
        ok = f"LOCK-{letter}" in index_text or f"**{letter}**" in index_text
        check(ok, f"LOCK-{letter} مسجّل في index.md")
        print(f"  {'✓' if ok else '✗'} LOCK-{letter} — مسجّل في الفهرس")

    # [7] الخواتيم
    print("\n[7] الخواتيم")
    for name in ["CLOSER-master.txt", "CLOSER-documentary.txt", "CLOSER-thumbnail.txt"]:
        path = LOCKS_DIR / name
        ok = path.is_file() and "{AR}" in read(path)
        check(ok, f"{name} موجود ويحتوي {{AR}}")
        print(f"  {'✓' if ok else '✗'} {name}")

    # [8] برومبت الفيديو الموحد
    print("\n[8] برومبت الفيديو الموحد (UVP)")
    uvp = LOCKS_DIR / "UNIVERSAL-VIDEO-PROMPT.txt"
    uvp_text = read(uvp)
    uvp_low = uvp_text.lower()
    for label, cond in [
        ("يحتوي {DURATION}", "{DURATION}" in uvp_text),
        ("الكاميرا مقفولة صراحة", "camera stays completely locked" in uvp_low),
        ("قسم BUILD-ON ASSEMBLY", "build-on assembly" in uvp_low),
        ("قسم LIVING PAPER POSTER", "living paper poster" in uvp_low),
        ("قسم AUDIO", "audio:" in uvp_low),
        ("يمنع الحركة السلسة", "never smooth cgi motion" in uvp_low),
        ("stop-motion cadence", "stop-motion cadence" in uvp_low),
    ]:
        check(cond, f"UVP — {label}")
        print(f"  {'✓' if cond else '✗'} UVP — {label}")

    # [9] ملفات المكتبة
    print("\n[9] ملفات مكتبة الأنماط")
    for label, path in [
        ("styles/README.md", STYLES_README),
        ("styles/index.md", INDEX),
        ("styles/style-pack-template.md", TEMPLATE),
        ("styles/locks/README.md", LOCKS_DIR / "README.md"),
    ]:
        ok = path.is_file() and len(read(path)) > 200
        check(ok, f"{label} موجود وغير فارغ")
        print(f"  {'✓' if ok else '✗'} {label}")

    # النتيجة
    passed = sum(1 for ok, _ in results if ok)
    failed = [(m) for ok, m in results if not ok]
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
    print("✅ مكتبة الأنماط سليمة — كل الأقفال والخواتيم صالحة")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
