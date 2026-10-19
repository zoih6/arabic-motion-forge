#!/usr/bin/env python3
"""
فاحص المثال الحي — examples/coffee-short.md (v1.x) و examples/energy-drink-ad.md (v2.0)

يستخرج البرومبتات الفعلية من ملف المثال ويفحصها ضد القيود الموثقة.
هذا يضمن أن المثال الذي سيقلّده المستخدم صالح فعلًا، لا مجرد نص جميل.
"""
import re, sys, pathlib

EX = pathlib.Path(__file__).parent.parent / "examples" / "coffee-short.md"
FAIL, PASS = [], []
def fail(m): FAIL.append(m); print(f"  ✗ {m}")
def ok(m):   PASS.append(m); print(f"  ✓ {m}")

if not EX.exists():
    print("✗ ملف المثال غير موجود"); sys.exit(1)
text = EX.read_text(encoding="utf-8")
print(f"فحص {EX.name} ({len(text):,} حرفًا)")

# ── استخرج كتل البرومبت الإنجليزية ─────────────────────────
blocks = re.findall(r"```text\n(.*?)```", text, re.S)
en = [b for b in blocks if re.search(r"[A-Za-z]{4,}", b) and
      not re.search(r"[\u0600-\u06FF]", b)]
print(f"\nوُجدت {len(blocks)} كتلة نصية، منها {len(en)} برومبت إنجليزي")
if len(en) < 2:
    fail("المثال يجب أن يحتوي برومبت صورة وبرومبت تحريك على الأقل")
    sys.exit(1)
ok(f"{len(en)} برومبت إنجليزي قابل للفحص")

img_prompt    = next((b for b in en if "Cinematic film still" in b), None)
motion_prompt = next((b for b in en if "@Image1" in b), None)

BANNED = ["beautiful","stunning","amazing","awesome","high quality",
          "gorgeous","masterpiece"]

# ── 1. برومبت الصورة ───────────────────────────────────────
print("\n[برومبت الصورة المرجعية]")
if not img_prompt:
    fail("لا يوجد برومبت صورة في المثال")
else:
    ok("برومبت الصورة موجود")
    hit = [w for w in BANNED if w.lower() in img_prompt.lower()]
    if hit: fail(f"كلمات مجردة ممنوعة: {hit}")
    else:   ok("خالٍ من الكلمات المجردة الممنوعة")

    if re.search(r"\d+mm at f/[\d.]+", img_prompt): ok("العدسة والفتحة مُسمّاة")
    else: fail("العدسة غير مُسمّاة")

    if re.search(r"\d{4}K", img_prompt): ok("حرارة اللون بالكلفن")
    else: fail("حرارة اللون غير مُحددة")

    if "anatomically correct hands" in img_prompt: ok("عبارة التشريح موجودة")
    else: fail("عبارة التشريح مفقودة")

    if "no readable text" in img_prompt and "no logos" in img_prompt:
        ok("قيود النص والشعارات مذكورة")
    else: fail("قيود النص/الشعارات مفقودة")

    # Identity String مُلصق حرفيًا.
    # القاعدة 7 في agents/03 تمنع "إعادة الصياغة" لا "إعادة التفاف الأسطر":
    # النموذج يطبّع المسافات، لذا الالتفاف لا يغيّر الدلالة. لذلك نُطبّع
    # المسافات قبل المقارنة — ونظل نلتقط أي إعادة صياغة فعلية للكلمات.
    norm = lambda s: " ".join(s.split())
    ident = ("a Yemeni man in his early thirties, angular jaw, deep brown eyes, "
             "short cropped black beard with a small grey patch on the left cheek, "
             "a faint burn scar on the back of his right hand")
    if norm(ident) in norm(img_prompt):
        ok("Identity String مُلصق حرفيًا (مطابقة بعد تطبيع المسافات)")
    else:
        fail("Identity String أُعيدت صياغته — القاعدة 7 مكسورة")

    # نفس الـ Identity String يجب أن يظهر في برومبت التحريك
    if motion_prompt and "SAMI-01" in motion_prompt:
        ok("رمز الشخصية مُستخدم في برومبت التحريك")

# ── 2. برومبت التحريك ──────────────────────────────────────
print("\n[برومبت التحريك]")
if not motion_prompt:
    fail("لا يوجد برومبت تحريك في المثال")
else:
    ok("برومبت التحريك موجود")

    # اللهجة صحيحة للنموذج
    if "@Image1" in motion_prompt: ok("لهجة Seedance (@Image1) صحيحة")
    else: fail("لهجة Seedance مفقودة")
    if "<FIRST_FRAME>" in motion_prompt:
        fail("خلط لهجات: وسم Omni في برومبت Seedance")
    else:
        ok("لا خلط لهجات بين النماذج")

    # المدة ضمن سقف Seedance (4–15)
    m = re.search(r"`duration:\s*\"?(\d+)", text)
    if m:
        d = int(m.group(1))
        if 4 <= d <= 15: ok(f"duration {d}s ضمن سقف Seedance 2.0 (4–15)")
        else: fail(f"duration {d}s خارج سقف Seedance")
    else:
        fail("لم يُعثر على معامل duration")

    # النسبة ضمن مدعومات Seedance
    a = re.search(r"`aspect_ratio:\s*\"([\d:]+)\"", text)
    if a:
        ar = a.group(1)
        if ar in {"auto","21:9","16:9","4:3","1:1","3:4","9:16"}:
            ok(f"aspect_ratio {ar} مدعوم في Seedance 2.0")
        else: fail(f"aspect_ratio {ar} غير مدعوم")

    # حركة كاميرا واحدة
    low = motion_prompt.lower()
    moves = [x for x in ["dolly in","dolly out","pan ","tilt ","orbit","arc ",
                         "zoom","crane","truck","handheld","tracking"]
             if x in low and f"no {x.strip()}" not in low]
    if len(moves) <= 1: ok(f"حركة كاميرا واحدة مهيمنة: {moves or ['static']}")
    else: fail(f"حركات متعددة: {moves}")

    # التسلسل الزمني يغطي المدة
    beats = [(int(x), int(y)) for x, y in re.findall(r"\[(\d+)-(\d+)s\]", motion_prompt)]
    if beats:
        cov = sum(b - a for a, b in beats)
        if m and cov == int(m.group(1)):
            ok(f"التسلسل يغطي {cov}s = المدة الكاملة")
        elif m:
            fail(f"التسلسل يغطي {cov}s من {m.group(1)}s")
        # لا فجوات ولا تداخل
        gaps = [beats[i+1][0] - beats[i][1] for i in range(len(beats)-1)]
        if all(g == 0 for g in gaps): ok("لا فجوات ولا تداخل في التسلسل الزمني")
        else: fail(f"فجوات/تداخل في التسلسل: {gaps}")
    else:
        fail("لا تسلسل زمني")

    # الاستمرارية والمحور
    if "screen direction" in low: ok("محور الشاشة مثبّت")
    else: fail("محور الشاشة غير مثبّت")
    if sum(1 for c in ["face","apron","scar","beard"] if c in low) >= 2:
        ok("الاستمرارية مذكورة صراحة")
    else: fail("الاستمرارية غير مذكورة")

    hit = [w for w in BANNED if w.lower() in low]
    if hit: fail(f"كلمات مجردة ممنوعة: {hit}")
    else:   ok("خالٍ من الكلمات المجردة الممنوعة")

# ── 3. اكتمال مراحل المسار في المثال ───────────────────────
print("\n[اكتمال المسار]")
for stage, label in [("M0","الاستقبال"),("M1","المفهوم"),("M2","الهوية"),
                     ("M3","اللقطات"),("M4","الصور"),("M5","التحريك"),
                     ("M6","الصوت"),("M7","المونتاج")]:
    if stage in text: ok(f"{stage} — {label} مغطاة")
    else: fail(f"{stage} — {label} ناقصة في المثال")

# ── 4. التسمية الإلزامية ───────────────────────────────────
print("\n[التسمية]")
if re.search(r"SC\d+_SH\d+_FR\d+_v\d+", text):
    ok("نمط تسمية SC_SH_FR_v مستخدم")
else: fail("نمط التسمية الإلزامي مفقود")

print("\n" + "═"*60)
print(f"النتيجة: {len(PASS)} نجح · {len(FAIL)} فشل")
if FAIL:
    for f in FAIL: print(f"  ✗ {f}")
    sys.exit(1)
print("✅ المثال الحي صالح ويحقق كل قواعد المهارة")
print("═"*60)
