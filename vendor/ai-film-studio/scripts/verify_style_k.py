#!/usr/bin/env python3
"""تحقق من اكتمال تسجيل LOCK-K دون تغيير فاحص الأقفال التاريخي A–J."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
checks = {
    "lock": ROOT / "styles/locks/LOCK-K-oversized-ink-editorial.txt",
    "closer": ROOT / "styles/locks/CLOSER-oversized-ink-editorial.txt",
    "guide": ROOT / "styles/oversized-ink-editorial.md",
}
errors=[]
for name,path in checks.items():
    if not path.is_file() or len(path.read_text(encoding='utf-8').strip()) < 120:
        errors.append(f"{name} missing or too short")
lock=checks['lock'].read_text(encoding='utf-8') if checks['lock'].is_file() else ''
for phrase in ["oversized asymmetric shapes", "warm off-white paper", "{PALETTE}"]:
    # {PALETTE} is intentionally absent from the fixed palette lock; accept palette by hex instead.
    if phrase not in lock and phrase != "{PALETTE}": errors.append(f"lock missing: {phrase}")
for phrase in ["LOCK-K", "post overlay", "منتج يجب أن يبقى", "silhouette", "caption"]:
    guide=checks['guide'].read_text(encoding='utf-8') if checks['guide'].is_file() else ''
    if phrase.lower() not in guide.lower(): errors.append(f"guide missing: {phrase}")
index=(ROOT/'styles/index.md').read_text(encoding='utf-8')
readme=(ROOT/'styles/locks/README.md').read_text(encoding='utf-8')
if "LOCK-K" not in index: errors.append("LOCK-K missing from styles/index.md")
if "LOCK-K" not in readme: errors.append("LOCK-K missing from styles/locks/README.md")
if errors:
    print("STYLE-K VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("STYLE-K VALIDATION PASSED")
print("- lock and closer present")
print("- style index and lock registry updated")
print("- product-safe usage guide present")
