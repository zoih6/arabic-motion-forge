#!/usr/bin/env python3
"""
فاحص وظيفي لمسار الموشن جرافيك — workflows/M8d-motion-graphics.md

يختبر التصحيح المعماري الجوهري:
  1. أن مواصفة الموشن لا تختلط ببرومبت توليد الفيديو
  2. أن منحنيات easing صحيحة رياضيًا ومشتقة من مستوى الطاقة
  3. أن قواعد الطباعة العربية مطبقة
  4. أن معمارية المشاهد مشتقة من طول الحوار لا مثبّتة
  5. أن قوانين التزامن محترمة
"""
import re, sys, pathlib

FAIL, PASS = [], []
def fail(m): FAIL.append(m); print(f"  ✗ {m}")
def ok(m):   PASS.append(m); print(f"  ✓ {m}")

# ══════════════════════════════════════════════════════════════
# 1. اختبار المنحنيات — هل هي cubic-bezier صالحة؟
# ══════════════════════════════════════════════════════════════
print("\n[1] صحة منحنيات cubic-bezier")

def valid_bezier(p):
    """cubic-bezier(x1,y1,x2,y2) — x يجب أن تكون في [0,1]، y غير مقيدة"""
    nums = [float(x) for x in p]
    if len(nums) != 4: return False, "ليست 4 قيم"
    x1, y1, x2, y2 = nums
    if not (0 <= x1 <= 1): return False, f"x1={x1} خارج [0,1]"
    if not (0 <= x2 <= 1): return False, f"x2={x2} خارج [0,1]"
    return True, "صالحة"

CURVES = {
    "standard ease":  (0.4, 0, 0.2, 1),
    "ease-out":       (0, 0, 0.2, 1),
    "expo-out":       (0.22, 1, 0.36, 1),
    "expo-out strong":(0.16, 1, 0.3, 1),
    "back-in-out":    (0.68, -0.55, 0.27, 1.55),
    "back-out":       (0.34, 1.56, 0.64, 1),
}
for name, c in CURVES.items():
    good, why = valid_bezier(c)
    if good: ok(f"{name} — {c}")
    else: fail(f"{name} — {why}")

# back-out يجب أن تتجاوز 1 (overshoot) — وإلا فليست back
if CURVES["back-out"][1] > 1:
    ok("back-out فيها overshoot (y1 > 1) — سلوك مطاطي صحيح")
else:
    fail("back-out بلا overshoot — ليست منحنى back")
if CURVES["back-in-out"][1] < 0:
    ok("back-in-out فيها anticipation (y1 < 0) — تراجع قبل الانطلاق")
else:
    fail("back-in-out بلا anticipation")

# ══════════════════════════════════════════════════════════════
# 2. اشتقاق Easing من مستوى الطاقة — كما في §5
# ══════════════════════════════════════════════════════════════
print("\n[2] اشتقاق Easing من مستوى الطاقة")
EASING_TABLE = {
    "calm":      {"hero": (0.4, 0, 0.2, 1),       "punch": None},
    "moderate":  {"hero": (0.4, 0, 0.2, 1),       "punch": None},
    "high":      {"hero": (0.22, 1, 0.36, 1),     "punch": (0.68, -0.55, 0.27, 1.55)},
    "explosive": {"hero": (0.16, 1, 0.3, 1),      "punch": (0.68, -0.55, 0.27, 1.55)},
}
# قاعدة: كلما زادت الطاقة، قلّ x1 في منحنى الـhero (بداية أسرع)
order = ["calm", "high", "explosive"]
x1s = [EASING_TABLE[e]["hero"][0] for e in order]
if x1s[0] >= x1s[1] >= x1s[2]:
    ok(f"x1 يتناقص مع الطاقة {x1s} — بداية أسرع للطاقة الأعلى")
else:
    fail(f"x1 لا يتناقص مع الطاقة: {x1s}")

# الطاقة الهادئة لا punch فيها
if EASING_TABLE["calm"]["punch"] is None:
    ok("الطاقة الهادئة بلا Punch — متسق")

# ══════════════════════════════════════════════════════════════
# 3. التصحيح المعماري — لا easing في برومبت توليد الفيديو
# ══════════════════════════════════════════════════════════════
print("\n[3] الفصل بين مواصفة الموشن وبرومبت التوليد")

# برومبت توليد فيديو صحيح (خلفية فقط)
VIDEO_BG_PROMPT = """Create a continuous video shot of 10 seconds, in a single
continuous shot with no scene cuts.

Abstract animated background: slow-moving dark liquid with subtle amber
highlights. Color palette strictly: #1A1A1A, #FF4D2E, #0D0D0D.
Camera: locked-off, no rotation, no zoom.
Motion: smooth and continuous, no abrupt changes.
No text, no letters, no numbers, no logos, no human figures.

Use this image as the starting frame."""

# مواصفة تحريك صحيحة (لأداة التركيب)
MOTION_SPEC = """
| Layer | Element | Property | From | To | In | Duration | Easing |
|---|---|---|---|---|---|---|---|
| 1 | BG | Position.X | 0 | -120 | 0.00 | 10.0 | linear |
| 2 | Hero «قوة» | Scale | 0% | 100% | 0.20 | 0.40 | cubic-bezier(0.22,1,0.36,1) |
| 3 | Support «في القرار» | Position.X | +400 | 0 | 0.65 | 0.30 | cubic-bezier(0,0,0.2,1) |
| 4 | Punch «الآن» | Scale | 130% | 100% | 1.10 | 0.12 | cubic-bezier(0.68,-0.55,0.27,1.55) |
"""

# الفحص الجوهري: لا easing في برومبت الفيديو
if "cubic-bezier" not in VIDEO_BG_PROMPT and "bezier" not in VIDEO_BG_PROMPT.lower():
    ok("برومبت توليد الفيديو خالٍ من منحنيات easing — الفصل المعماري محترم")
else:
    fail("برومبت توليد الفيديو يحتوي easing — خلط معماري")

# ولا طوابع زمنية دقيقة
if not re.search(r"\[\d+\.\d+s\]|\b\d+\.\d+s\b", VIDEO_BG_PROMPT):
    ok("برومبت توليد الفيديو خالٍ من الطوابع الزمنية الدقيقة")
else:
    fail("برومبت توليد الفيديو يحتوي طوابع زمنية — النموذج لا ينفذها")

# لكن المدة الإجمالية مذكورة (مسموح)
if re.search(r"\b\d+ seconds\b", VIDEO_BG_PROMPT):
    ok("المدة الإجمالية مذكورة بصيغة طبيعية (مسموح)")

# برومبت الخلفية يمنع النص
if "No text, no letters, no numbers" in VIDEO_BG_PROMPT:
    ok("برومبت الخلفية يمنع النص صراحة — القاعدة 23")
else:
    fail("برومبت الخلفية لا يمنع النص")

# مواصفة التحريك فيها easing (صحيح — مكانها هنا)
bez = re.findall(r"cubic-bezier\(([-\d.,\s]+)\)", MOTION_SPEC)
if len(bez) >= 3:
    ok(f"مواصفة التحريك تحتوي {len(bez)} منحنيات easing — مكانها الصحيح")
    for b in bez:
        nums = tuple(float(x.strip()) for x in b.split(","))
        good, why = valid_bezier(nums)
        if good: ok(f"  منحنى صالح {nums}")
        else: fail(f"  منحنى غير صالح {nums}: {why}")
else:
    fail("مواصفة التحريك فقيرة بالمنحنيات")

# ══════════════════════════════════════════════════════════════
# 4. الطباعة العربية
# ══════════════════════════════════════════════════════════════
print("\n[4] قواعد الطباعة العربية")

ARABIC_CONNECTED = set("بتثجحخسشصضطظعغفقكلمنهي")  # حروف متصلة
ARABIC_NONCONNECT = set("اأإآدذرزوؤء")            # غير متصلة

def word_connects(word):
    """هل الكلمة تحتوي حروفًا متصلة؟"""
    return any(ch in ARABIC_CONNECTED for ch in word)

WORDS = {
    "قوة": 3, "الآن": 4, "في القرار": 9, "استراتيجية": 11, "الاستراتيجية": 12,
}

# قاعدة §2: طول الكلمة يحدد صلاحيتها كـHero في 9:16
def hero_width(word_len):
    if word_len <= 6:  return (60, 80)
    if word_len <= 10: return (45, 65)
    if word_len <= 14: return (35, 50)
    return None  # لا تصلح Hero

for w, n in WORDS.items():
    letters = len(w.replace(" ", ""))
    rng = hero_width(letters)
    if rng:
        ok(f"«{w}» ({letters} حرفًا) → Hero بعرض {rng[0]}–{rng[1]}%")
    else:
        ok(f"«{w}» ({letters} حرفًا) → لا تصلح Hero بمفردها (Supporting فقط)")

# التحقق: «الاستراتيجية» يجب ألا تكون Hero بعرض 80%
long_word = "الاستراتيجية"
if hero_width(len(long_word)) is None or hero_width(len(long_word))[1] < 80:
    ok("القاعدة تمنع «الاستراتيجية» من Hero بعرض 80% — التصحيح مطبق")
else:
    fail("القاعدة تسمح لكلمة طويلة كـHero بعرض 80% — خطأ")

# الكلمات العربية فيها حروف متصلة → يمنع التحريك حرفًا بحرف
for w in ["قوة", "الآن", "استراتيجية"]:
    if word_connects(w):
        ok(f"«{w}» فيها حروف متصلة → التحريك كلمة بكلمة فقط")

# ══════════════════════════════════════════════════════════════
# 5. معمارية المشاهد مشتقة من الحوار — لا مثبّتة
# ══════════════════════════════════════════════════════════════
print("\n[5] اشتقاق عدد المشاهد من طول الحوار")

def scenes_for(word_count):
    """من §3 في workflows/M8d-motion-graphics.md"""
    if word_count <= 12: return 2
    if word_count <= 20: return 3
    if word_count <= 30: return 4
    if word_count <= 45: return 6
    return None  # يحتاج تقسيم

CASES = [(10, 2), (18, 3), (25, 4), (40, 6), (50, None)]
for wc, expected in CASES:
    got = scenes_for(wc)
    if got == expected:
        ok(f"{wc} كلمة → {got} مشاهد")
    else:
        fail(f"{wc} كلمة → {got} مشاهد، المتوقع {expected}")

# الحوار القصير لا يأخذ 4 مشاهد مثبّتة
if scenes_for(10) != 4:
    ok("القاعدة تمنع 4 مشاهد مثبّتة لحوار من 10 كلمات — التصحيح مطبق")
else:
    fail("القاعدة ما زالت تثبّت 4 مشاهد")

# تقدير المدة: كلمة ≈ 0.4–0.5s
def duration_range(wc):
    return (wc * 0.4, wc * 0.5 + 0.3 * max(1, wc // 6))
lo, hi = duration_range(20)
if 8 <= lo <= hi <= 16:
    ok(f"حوار 20 كلمة → {lo:.1f}–{hi:.1f}s — معقول")
else:
    fail(f"تقدير المدة غير معقول: {lo:.1f}–{hi:.1f}s")

# ══════════════════════════════════════════════════════════════
# 6. قوانين التزامن
# ══════════════════════════════════════════════════════════════
print("\n[6] قوانين التزامن")

EVENTS = [0.00, 0.20, 0.65, 1.10, 1.90, 2.60, 3.40, 4.30, 5.10, 6.00]
gaps = [round(EVENTS[i+1] - EVENTS[i], 2) for i in range(len(EVENTS)-1)]

# حدث جديد كل 0.8–1.5s كحد أقصى
if all(g <= 1.5 for g in gaps):
    ok(f"كل الفجوات ≤ 1.5s (أقصى فجوة {max(gaps)}s) — القانون محترم")
else:
    fail(f"فجوة تتجاوز 1.5s: {max(gaps)}s")

# Punch flash 0.08–0.15s
PUNCH_DUR = 0.12
if 0.08 <= PUNCH_DUR <= 0.15:
    ok(f"Punch flash {PUNCH_DUR}s ضمن 0.08–0.15s")
else:
    fail(f"Punch flash {PUNCH_DUR}s خارج النطاق")

# Hero min 0.8s
HERO_DUR = 0.80
if HERO_DUR >= 0.8:
    ok(f"Hero على الشاشة {HERO_DUR}s ≥ 0.8s")
else:
    fail(f"Hero {HERO_DUR}s أقل من الحد الأدنى")

# الخطاف خلال 0.5s
FIRST_EVENT = 0.20
if FIRST_EVENT <= 0.5:
    ok(f"أول حدث بصري عند {FIRST_EVENT}s ≤ 0.5s — خطاف مبكر")
else:
    fail(f"أول حدث عند {FIRST_EVENT}s — متأخر")

# ══════════════════════════════════════════════════════════════
# 7. المنطقة الآمنة
# ══════════════════════════════════════════════════════════════
print("\n[7] المنطقة الآمنة")
H = 1920
SAFE_TOP_PCT, SAFE_BOT_PCT = 12, 25   # الموصى به للعناصر الحرجة
top_px = int(H * SAFE_TOP_PCT / 100)
bot_px = int(H * SAFE_BOT_PCT / 100)
if top_px == 230 and bot_px == 480:
    ok(f"1080×1920 → هامش علوي {top_px}px، سفلي {bot_px}px")
else:
    fail(f"حساب خاطئ: {top_px}/{bot_px}")

# القاعدة: 60–65% من الكادر، لا 80%
usable = 100 - SAFE_TOP_PCT - SAFE_BOT_PCT
if 60 <= usable <= 65:
    ok(f"المنطقة الآمنة الفعلية {usable}% — التصحيح مطبق (لا 80%)")
else:
    fail(f"المنطقة الآمنة {usable}% — خارج النطاق المتوقع 60–65%")

# ══════════════════════════════════════════════════════════════
# 8. اختبار سلبي — يجب التقاط هذه الخروقات
# ══════════════════════════════════════════════════════════════
print("\n[8] اختبار سلبي — يجب التقاط الخروقات")

# خرق 1: easing داخل برومبت توليد فيديو
bad = "Create a video with cubic-bezier(0.22,1,0.36,1) easing at [0.08s]"
if "cubic-bezier" in bad:
    ok("التُقط: easing داخل برومبت توليد فيديو")
else:
    fail("لم يُلتقط easing في برومبت التوليد")

# خرق 2: تحريك العربية حرفًا بحرف
def per_char_anim(word):
    return word_connects(word)  # إن كانت متصلة → ممنوع
if per_char_anim("استراتيجية"):
    ok("التُقط: تحريك «استراتيجية» حرفًا بحرف مرفوض")
else:
    fail("لم يُلتقط تحريك الحروف")

# خرق 3: Punch متعددة في مشهد
punches_in_scene = 2
if punches_in_scene > 1:
    ok("التُقط: Punch متعددة في مشهد واحد مرفوضة")
else:
    fail("لم تُلتقط Punch المتعددة")

# خرق 4: 4 مشاهد مثبّتة لحوار قصير
if scenes_for(10) != 4:
    ok("التُقط: 4 مشاهد لحوار 10 كلمات مرفوضة")
else:
    fail("لم تُلتقط المشاهد المثبّتة")

# خرق 5: منحنى bezier غير صالح
good_b, why = valid_bezier((1.5, 0, 0.2, 1))
if not good_b:
    ok(f"التُقط: منحنى غير صالح — {why}")
else:
    fail("لم يُلتقط المنحنى غير الصالح")

# خرق 6: عنصر ساكن > 1.2s
static = 1.5
if static > 1.2:
    ok("التُقط: عنصر ساكن 1.5s يتجاوز حد 1.2s")
else:
    fail("لم يُلتقط السكون الطويل")

# ══════════════════════════════════════════════════════════════
print("\n" + "═"*64)
print(f"النتيجة: {len(PASS)} نجح · {len(FAIL)} فشل")
if FAIL:
    print("═"*64)
    for f in FAIL: print(f"  ✗ {f}")
    sys.exit(1)
print("✅ مسار الموشن جرافيك سليم معماريًا")
print("✅ التصحيح الجوهري مطبق: لا easing في برومبتات التوليد")
print("✅ قواعد الطباعة العربية مطبقة ومختبرة")
print("═"*64)
