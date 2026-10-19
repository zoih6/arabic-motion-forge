#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prompt_lint.py — فاحص البرومبتات (Prompt Linter)

يطبّق «اختبار العشر ثوانٍ» و«قواعد الأقفال» آليًا على أي برومبت.

الفحوص:
  [1] الطول (120–220 كلمة قبل القفل · 60–120 للوثائقي)
  [2] الكلمات الفارغة المحرّمة
  [3] وجود قفل أسلوبي (LOCK) أو ما يعادله
  [4] الأقفال مطابقة حرفيًا لملفات styles/locks/
  [5] وجود Negative صريح (≤ 6 بنود)
  [6] المحظورات: وجوه · أيدٍ · نص طويل
  [7] (فيديو) ما يثبت مذكور صراحة · حركة كاميرا واحدة
  [8] الرموز غير المستبدلة {AR} · {PALETTE} · {DURATION}
  [9] الحقول الإلزامية لبرومبت الصورة (ترتيب 11)
  [10] em dash في المخرجات الإنجليزية

الاستخدام:
    python3 scripts/prompt_lint.py <file.txt|file.md>
    python3 scripts/prompt_lint.py --selftest    # فحص داخلي على عيّنة
    cat prompt.txt | python3 scripts/prompt_lint.py -
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCKS_DIR = ROOT / "styles" / "locks"

FORBIDDEN_WORDS = [
    "beautiful", "amazing", "stunning", "gorgeous", "masterpiece",
    "trending on artstation", "award winning", "best quality",
    "ultra quality", "hyperrealistic perfection", "8k masterpiece",
    "4k masterpiece", "perfect composition",
]

RISKY_PATTERNS = [
    (r"\b(face|faces)\b", "وجه/وجوه — استبدل بهالفتون أو ظل من الخلف"),
    (r"\b(hand|hands)\b(?![- ]?(cut|made|sculpted|crafted|drawn|painted|stitched|lettered|held))",
     "أيدٍ — استبدل أو أزل الفعل اليدوي"),
    (r"\btext reading [\"'][^\"']{25,}[\"']", "نص طويل داخل الصورة (> 4 كلمات) — ممنوع"),
    (r"\bfade to black\b", "fade to black — انتقال ممنوع"),
    (r"\bmorphing\b(?!\s*,\s*no)", "morphing بلا نفي صريح"),
    (r"[\u0600-\u06FF]", "نص عربي داخل البرومبت — يجب أن يكون إنجليزيًا"),
]

CAMERA_MOVES = [
    "push in", "pull back", "pulls back", "pan", "tilt", "orbit",
    "dolly", "track", "zoom", "crane", "handheld", "lateral slide",
    "top-down descent", "macro glide", "whip",
]

REQUIRED_FIELDS_HINTS = {
    "FRAME": [r"\b(16:9|9:16|1:1|4:5|2\.39:1|vertical|horizontal)\b"],
    "CAMERA": [r"\b(lens|mm macro|mm cinema|eye level|low angle|top-down|locked)\b"],
    "LIGHT": [r"\b(key light|rim light|soft fill|lighting|lit)\b"],
    "MOOD": [r"\b(calm|tactile|premium|warm|cool|moody|energetic|quiet|bold)\b"],
    "NEGATIVE": [r"\bno [a-z]+"],
}

results: list[tuple[str, bool, str]] = []


def add(severity: str, ok: bool, msg: str) -> None:
    results.append((severity, ok, msg))


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))


def load_locks() -> dict[str, str]:
    """يحمّل الأقفال (LOCK-*) والخواتيم (CLOSER-*) — كلها تُستثنى من جسم البرومبت."""
    locks = {}
    if LOCKS_DIR.is_dir():
        for p in sorted(LOCKS_DIR.glob("LOCK-*.txt")):
            locks[p.stem] = p.read_text(encoding="utf-8").strip()
        for p in sorted(LOCKS_DIR.glob("CLOSER-*.txt")):
            locks[p.stem] = p.read_text(encoding="utf-8").strip()
    return locks


def detect_lock(text: str, locks: dict[str, str]) -> tuple[str, float]:
    """يرجع (اسم القفل, نسبة التطابق) لأفضل قفل مطابق."""
    best, best_ratio = ("", 0.0)
    norm = re.sub(r"\s+", " ", text)
    for name, lock in locks.items():
        lock_norm = re.sub(r"\s+", " ", lock)
        # نسبة الكلمات الطويلة من القفل الموجودة في النص
        lw = [w for w in re.findall(r"[a-z]{5,}", lock_norm.lower())]
        if not lw:
            continue
        hit = sum(1 for w in set(lw) if w in norm.lower())
        ratio = hit / len(set(lw))
        if ratio > best_ratio:
            best, best_ratio = name, ratio
    return best, best_ratio


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z]{5,}", text.lower()))


def build_lock_sentences(locks: dict[str, str]) -> list[set[str]]:
    """
    جمل الأقفال والخواتيم مُجزّأة — لأن الخاتمة الواحدة قد تتكوّن من عدة جمل،
    ومقارنة الجملة بكل القفل تُعطي نسبة منخفضة فلا تُكتشف.
    """
    out = []
    for lock in locks.values():
        for s in split_sentences(lock):
            toks = _tokens(s)
            if len(toks) >= 4:
                out.append(toks)
    return out


def lock_overlap(sentence: str, lock_sents: list[set[str]]) -> float:
    """أعلى نسبة تطابق بين الجملة وأي جملة قفل/خاتمة."""
    sw = _tokens(sentence)
    if not sw:
        return 0.0
    best = 0.0
    for lt in lock_sents:
        best = max(best, len(sw & lt) / len(lt))
    return best


def lint(text: str, label: str = "PROMPT") -> None:
    print(f"\n{'─' * 64}\n فحص: {label}\n{'─' * 64}")
    locks = load_locks()
    norm = re.sub(r"\s+", " ", text)

    # فصل جمل الأقفال (LOCK/CLOSER) عن جسم البرومبت — القاعدة تقيس الجسم فقط
    lock_tokens = build_lock_sentences(locks)
    body_sents, lock_sents = [], []
    for s in split_sentences(norm):
        (lock_sents if lock_overlap(s, lock_tokens) >= 0.6 else body_sents).append(s)
    body = " ".join(body_sents)
    body_low = body.lower()

    # [1] طول الجسم (120–220 هدفًا · 60–240 مقبول)
    n = words(body)
    ok = 60 <= n <= 240
    add("WARN", ok, f"[1] طول الجسم {n} كلمة"
                    + ("" if ok else " — خارج النطاق (60–240 قبل الأقفال)"))
    print(f"  {'✓' if ok else '⚠'} [1] طول الجسم: {n} كلمة"
          f" (+{len(lock_sents)} جملة قفل/خاتمة)")

    # [2] الكلمات الفارغة — على النص كله
    low = norm.lower()
    hits = [w for w in FORBIDDEN_WORDS if w in low]
    ok = not hits
    add("FAIL", ok, f"[2] كلمات فارغة: {hits}" if hits else "[2] خالٍ من الكلمات الفارغة")
    print(f"  {'✓' if ok else '✗'} [2] الكلمات الفارغة"
          + (f" → {hits}" if hits else ""))

    # [3/4] القفل
    lock_name, ratio = detect_lock(norm, locks)
    if lock_name and ratio >= 0.85:
        add("PASS", True, f"[4] القفل {lock_name} مطابق حرفيًا ({ratio:.0%})")
        print(f"  ✓ [4] القفل: {lock_name} — مطابق حرفيًا ({ratio:.0%})")
    elif lock_name and ratio >= 0.5:
        add("FAIL", False, f"[4] القفل {lock_name} مطابق جزئيًا ({ratio:.0%}) — يجب نسخه حرفيًا")
        print(f"  ✗ [4] القفل: {lock_name} — مطابق جزئيًا ({ratio:.0%}) — انسخه حرفيًا")
    else:
        add("FAIL", False, "[3] لا يوجد قفل أسلوبي — أضف LOCK من styles/locks/")
        print(f"  ✗ [3] لا يوجد قفل أسلوبي مطابق (أفضل تطابق {ratio:.0%})")

    # [5] Negative — يُعدّ في الجسم فقط، كبنود مفصولة بفواصل (الأقصى 6)
    neg = [n.strip() for n in re.findall(r"\bno\s+[a-z][^.,;]*", body_low)]
    ok = len(neg) > 0
    add("FAIL", ok, "[5] Negative موجود" if ok else "[5] لا يوجد Negative")
    print(f"  {'✓' if ok else '✗'} [5] Negative: {len(neg)} بند"
          + (" ⚠ أكثر من 6" if len(neg) > 6 else ""))
    if len(neg) > 6:
        add("WARN", False, f"[5] Negative {len(neg)} بندًا — الأقصى 6"
                           f" → {neg[:8]}")

    # [6] المحظورات — على الجسم فقط
    # (الأقفال معفاة: "hand-cut" مصطلح أسلوبي، "no faces" نفي مسموح)
    risky_hits = []
    for pat, why in RISKY_PATTERNS:
        for m in re.finditer(pat, body, re.I):
            ctx = body[max(0, m.start() - 14):m.start()].lower()
            if re.search(r"\b(no|not|without|never|free of|avoid|zero)\b\s*$", ctx):
                continue  # منفي صراحة — مسموح
            risky_hits.append(why)
            break
    ok = not risky_hits
    add("WARN", ok, "[6] محظورات: " + "; ".join(risky_hits) if risky_hits else "[6] لا محظورات")
    print(f"  {'✓' if ok else '⚠'} [6] المحظورات" + (f" → {risky_hits}" if risky_hits else ""))

    # [7] الفيديو
    is_video = bool(re.search(r"\b(clip|video|animation|-\s*second|\d+[- ]second)\b", low)) \
        and bool(re.search(r"\b(camera|motion|animation)\b", low))
    if is_video:
        still = bool(re.search(r"\b(stays? perfectly still|remain[s]? still|stays? completely locked|"
                               r"stay perfectly still|nothing else moves|stay still)\b", low))
        add("FAIL", still, "[7] ما يثبت مذكور صراحة")
        print(f"  {'✓' if still else '✗'} [7] الفيديو — ما يثبت مذكور صراحة")

        moves = [m for m in CAMERA_MOVES if re.search(rf"\b{re.escape(m)}\b", low)]
        locked = "stays completely locked" in low or "locked" in low
        distinct = set(moves)
        ok = locked or len(distinct) <= 1
        add("FAIL", ok, f"[7] حركات كاميرا: {sorted(distinct)}")
        print(f"  {'✓' if ok else '✗'} [7] الفيديو — حركة كاميرا واحدة"
              + (f" (وُجد: {sorted(distinct)})" if not ok else ""))

        endstate = bool(re.search(r"\b(end(s|ing)? with|end state|final frame|by \d+s|"
                                  r"at \d+s)\b", low))
        add("WARN", endstate, "[7] الحالة النهائية موصوفة")
        print(f"  {'✓' if endstate else '⚠'} [7] الفيديو — الحالة النهائية")

    # [8] الرموز غير المستبدلة
    leftover = re.findall(r"\{(AR|PALETTE|DURATION)\}", text)
    ok = not leftover
    add("FAIL", ok, f"[8] رموز غير مستبدلة: {set(leftover)}" if leftover else "[8] الرموز مستبدلة")
    print(f"  {'✓' if ok else '✗'} [8] الرموز غير المستبدلة"
          + (f" → {sorted(set(leftover))}" if leftover else " — لا شيء"))

    # [9] الحقول الإلزامية
    missing = []
    for field, pats in REQUIRED_FIELDS_HINTS.items():
        if not any(re.search(p, body, re.I) for p in pats):
            missing.append(field)
    ok = not missing
    add("WARN", ok, f"[9] حقول ناقصة: {missing}" if missing else "[9] الحقول الأساسية موجودة")
    print(f"  {'✓' if ok else '⚠'} [9] الحقول الأساسية"
          + (f" → ناقص: {missing}" if missing else ""))

    # [10] em dash
    em = "—" in text
    add("WARN", not em, "[10] شرطة طويلة (em dash) موجودة" if em else "[10] لا em dash")
    print(f"  {'✓' if not em else '⚠'} [10] em dash"
          + (" — استبدلها بفاصلة أو شرطة قصيرة" if em else ""))


def selftest() -> None:
    print("=" * 64)
    print(" اختبار ذاتي — عيّنة برومبت صورة إعلانية")
    print("=" * 64)
    sample = """A commercial product still, medium shot, 9:16 vertical. the NIMBUS cold brew can, a slim
330ml aluminum can in matte midnight blue with a single thin cream band around the upper third, a
silver pull-tab lid, a small circular cream emblem centered on the band, soft-touch matte finish with
faint condensation, rendered with exact real-world fidelity identical to the reference image. It stands
upright on a three-layer kraft paper hill with torn top edge and soft drop shadow, centered in the
middle 70% of the vertical frame. Behind it, a hand-cut sunflower-yellow cardstock sun with 12 blunt
triangular rays occupies the upper right quadrant; a two-layer white cardstock cloud with a pale gray
lower layer sits upper left. The lower left quadrant stays empty cream paper. 100mm macro lens, eye
level, shallow depth of field. Single warm key from upper left, thin rim light tracing the can.
Calm, tactile, premium. """ + \
        (LOCKS_DIR / "LOCK-B-commercial-craft.txt").read_text(encoding="utf-8").strip().replace(
            "{PALETTE}", "warm kraft brown, cream, burnt sienna") + " " + \
        (LOCKS_DIR / "CLOSER-master.txt").read_text(encoding="utf-8").strip().replace("{AR}", "9:16") + \
        " No hands, no people, no faces. No text, no watermark. No changes to the product's shape, colors, proportions, cap, or label."
    lint(sample, "SELFTEST — commercial image prompt")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    if args[0] == "--selftest":
        selftest()
    elif args[0] == "-":
        lint(sys.stdin.read(), "STDIN")
    else:
        for a in args:
            p = Path(a)
            if not p.is_file():
                print(f"❌ الملف غير موجود: {a}")
                return 1
            lint(p.read_text(encoding="utf-8"), p.name)

    fails = [m for s, ok, m in results if not ok and s == "FAIL"]
    warns = [m for s, ok, m in results if not ok and s == "WARN"]
    passed = sum(1 for _, ok, _ in results if ok)

    print("\n" + "=" * 64)
    print(f"الملخّص: {passed} نجح · {len(fails)} فشل · {len(warns)} تحذير")
    if fails:
        print("\n❌ فشل (يجب الإصلاح قبل التسليم):")
        for m in fails:
            print(f"   • {m}")
    if warns:
        print("\n⚠️  تحذيرات:")
        for m in warns:
            print(f"   • {m}")
    print("=" * 64)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
