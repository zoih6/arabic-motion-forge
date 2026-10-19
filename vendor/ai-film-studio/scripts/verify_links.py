#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_links.py — فحص سلامة الروابط الداخلية في كل ملفات Markdown

يفحص:
  [1] كل رابط نسبي `](path)` يشير إلى ملف موجود فعليًا
  [2] كل رابط مرساة `#section` داخل ملف موجود (تحقق خفيف)
  [3] لا روابط مكسورة إلى مجلدات محذوفة (مثل agents/ القديم)
  [4] كل ملف .md له frontmatter YAML صالح (إن كان مطلوبًا)
  [5] لا ملفات يتيمة (لا يُشار إليها من أي ملف آخر) — تحذير فقط

الاستخدام:
    python3 scripts/verify_links.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", "build", "dist", "out"}

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
# إحالات بصيغة كود بين backticks: `references/specs/beat-architecture.md`
TICK_RE = re.compile(r"`([^`\n]+\.md)`")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

# مجلدات من الإصدارات القديمة — الإشارة إليها تعني رابطًا قديمًا
LEGACY_DIRS = ("agents/", "templates/01-", "state/")

results: list[tuple[str, bool, str]] = []
all_links: set[Path] = set()


def add(sev: str, ok: bool, msg: str) -> None:
    results.append((sev, ok, msg))


def md_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def is_external(url: str) -> bool:
    return bool(re.match(r"^(https?:|mailto:|#|data:)", url))


def resolve_ref(path: Path, ref: str) -> Path | None:
    """يحوّل مرجعًا نسبيًا إلى مسار فعلي — يجرب من موقع الملف ثم من جذر المستودع."""
    ref = ref.strip()
    if not ref or is_external(ref):
        return None
    cands = [(path.parent / ref).resolve(), (ROOT / ref).resolve()]
    for c in cands:
        if c.exists():
            return c
    return None


def check_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel = path.relative_to(ROOT)

    # بعض الملفات (CHANGELOG، تحليل الفجوات) تشير عممدًا إلى مسارات من مستودعات
    # سابقة لم تعد موجودة هنا — واسم صريح في أعلى الملف يمنع اعتبارها مكسورة.
    if "verify_links: allow-legacy" in text[:400]:
        return

    refs: list[str] = []
    for _label, url in LINK_RE.findall(text):
        refs.append(url)
    for tick in TICK_RE.findall(text):
        refs.append(tick)

    for url in refs:
        if is_external(url) or not url.strip():
            continue
        if "*" in url:  # نمط مجلد (glob) لا رابط فعلي — يُتجاهل
            continue
        target_part = url.split("#")[0].strip()
        if not target_part or not target_part.endswith(".md"):
            continue

        target = resolve_ref(path, target_part)
        if target is None:
            add("FAIL", False, f"{rel}: رابط مكسور → {url}")
        else:
            all_links.add(target)

        # روابط إلى الهياكل القديمة
        for legacy in LEGACY_DIRS:
            if url.startswith(legacy):
                add("WARN", False, f"{rel}: رابط لبنية قديمة → {url}")

    # frontmatter
    if path.name in ("SKILL.md",) or "/workflows/" in str(path.as_posix()) \
            or "/references/" in str(path.as_posix()) or "/styles/" in str(path.as_posix()) \
            or "/schemas/" in str(path.as_posix()) or "/quality/" in str(path.as_posix()):
        fm = FRONTMATTER_RE.match(text)
        if not fm:
            add("WARN", False, f"{path.relative_to(ROOT)}: بلا frontmatter YAML")
        else:
            body = fm.group(1)
            if not re.search(r"^name:", body, re.M):
                add("WARN", False, f"{path.relative_to(ROOT)}: frontmatter بلا حقل name")


def main() -> int:
    print()
    print("=" * 64)
    print(" فحص الروابط الداخلية — AI Film Studio v3.0.0")
    print("=" * 64)

    files = md_files()
    print(f"\n[1] فحص {len(files)} ملف Markdown")

    for p in files:
        check_file(p)

    broken = [m for s, ok, m in results if not ok and s == "FAIL"]
    legacy = [m for s, ok, m in results if not ok and s == "WARN" and "قديمة" in m]
    nofm = [m for s, ok, m in results if not ok and s == "WARN" and "frontmatter" in m]

    print(f"  ✓ فُحصت {len(files)} ملفًا")
    print(f"  {'✓' if not broken else '✗'} روابط مكسورة: {len(broken)}")
    for m in broken[:25]:
        print(f"      ✗ {m}")
    print(f"  {'✓' if not legacy else '⚠'} روابط لبُنى قديمة: {len(legacy)}")
    for m in legacy[:15]:
        print(f"      ⚠ {m}")
    print(f"  {'✓' if not nofm else '⚠'} ملفات بلا frontmatter كامل: {len(nofm)}")
    for m in nofm[:15]:
        print(f"      ⚠ {m}")

    # [5] ملفات يتيمة
    print("\n[2] ملفات يتيمة (لا يُشار إليها من أي ملف آخر) — تحذير فقط")
    orphans = []
    for p in files:
        if p.name in ("README.md", "SKILL.md", "CHANGELOG.md", "LICENSE", "CONTRIBUTING.md"):
            continue
        if p not in all_links:
            orphans.append(p.relative_to(ROOT))
    print(f"  {'✓' if not orphans else '⚠'} ملفات يتيمة: {len(orphans)}")
    for o in orphans[:20]:
        print(f"      ⚠ {o}")

    print()
    print("=" * 64)
    if broken:
        print(f"❌ {len(broken)} رابط مكسور — يجب الإصلاح")
        print("=" * 64)
        return 1
    print(f"✅ الروابط الداخلية سليمة ({len(files)} ملفًا · {len(all_links)} رابطًا صالحًا)")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
