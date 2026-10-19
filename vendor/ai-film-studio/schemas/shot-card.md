---
name: schema-shot-card
description: "قالب بطاقة اللقطة ذات الحقول الستة + خريطة Start/End Frames + مواصفات Hero Shot + قاموس الكاميرا."
tier: 3
when_to_load: "E2 المرحلة 4 · E3 المرحلة 6 · M3a · M7b"
---

# Shot Card — بطاقة اللقطة

## القالب (6 حقول إجبارية)

```
SHOT S03
PURPOSE      هدف واحد: "إشعال الرغبة عبر ملمس الغطاء المعدني"
COMPOSITION  المنتج يمين الثلث، 40% من الإطار، خلفية ورقية كريمية، مساحة سلبية يسار
CAMERA       slow push-in (واحدة فقط)   LENS: 100mm macro
ACTION       فعل واحد: قطرة تكاثف تنزلق على الغطاء
LIGHT        single warm key from upper left, thin rim light on the cap edge
END STATE    القطرة تصل لقاعدة الغطاء وتلمس الورق → بقعة تتسع (يمهّد S04)
TRANSITION   Color Wipe: البقعة تتسع حتى تملأ الإطار
```

**القواعد الحاكمة:**
- **لقطة بلا PURPOSE تُحذف.**
- **لقطة بحركتَي كاميرا تُقسَّم.**
- **لقطة بلا END STATE تكسر الوصل مع التالية.**

---

## الحقول

| الحقل | القاعدة | مثال |
|---|---|---|
| **PURPOSE** | **هدف واحد**، جملة، يبدأ بفعل | "إشعال الرغبة عبر ملمس الغطاء" |
| **COMPOSITION** | موضع + نسبة + خلفية + مساحة سلبية | "يمين الثلث، 40%، كريمي، سلبية يسار" |
| **CAMERA** | **حركة واحدة** + عدسة | `slow push-in` · `100mm macro` |
| **ACTION** | **فعل واحد** بتسلسل زمني | "قطرة تنزلق من الأعلى للقاعدة" |
| **LIGHT** | **نفس جملة المشروع** (إلا تطور مقصود) | `single warm key from upper left` |
| **END STATE** | حالة الإطار الأخير + تمهيد التالي | "بقعة تتسع → تمهّد S04" |
| **TRANSITION** | النوع + السبب البصري | `Color Wipe` |

---

## قاموس الكاميرا (حركة واحدة لكل مشهد)

| الحركة | متى | الكتابة في البرومبت |
|---|---|---|
| **Locked-off static** | Hook الماكرو، Hero، الكولاج المتجمّع | `the camera stays completely locked` |
| **Slow push-in** | الانجذاب، الكشف التدريجي | `the camera pushes in very slowly toward` |
| **Slow pull-back** | كشف العالم، detail → scene | `the camera pulls back slowly revealing` |
| **Lateral slide** | تتبع، المرور على عناصر | `the camera slides laterally at a steady pace` |
| **Orbital quarter-turn** | إبراز الحجم، فخامة | `a slow controlled quarter orbit around` |
| **Top-down descend** | الكولاج على الطاولة | `a slow top-down descent toward the tabletop` |
| **Macro glide** | خامات، ملمس | `a macro glide across the surface` |

**العدسات:**
| العدسة | الاستخدام |
|---|---|
| `100mm macro` | التفاصيل والخامات |
| `50mm cinema` | الإطارات العامة |
| `35mm` | العوالم المصغّرة |

❌ **لا أوسع من 35mm** — التشوّه يفسد نسب المنتج.

**الزوايا:** `eye-level` افتراضي · `low angle` لهيبة المنتج · `top-down` لعالم الطاولة.
❌ لا زوايا هولندية إلا لعدسة Wrong Room.

---

## أحجام اللقطات وحضور المنتج

| الحجم | المنتج | الاستخدام |
|---|---|---|
| **ECU** (Extreme Close-Up) | جزء من الخامة | Hook |
| **CU** | الغطاء/الشعار/الفوهة | Desire |
| **MS** | المنتج كامل + محيط قريب | Reveal, Trigger |
| **WS** | المنتج داخل العالم | Escalation, Payoff |
| **Hero** | المنتج كامل، مركزي، بلا منافس | النهاية |

**قانون التصاعد:** `ECU → CU → MS → WS → Hero`
❌ لا ترجع خطوة للوراء إلا لـ **الصمت قبل الذروة**.

---

## خريطة Start / End Frames

```
S01  start: IMG-01   end: —         (Hook, static)
S02  start: IMG-01   end: IMG-02    (pull-back reveal — البداية هي نهاية S01)
S03  start: IMG-02   end: IMG-03
S04  start: IMG-03   end: IMG-04
```

**القواعد:**
- **End Frame لقطة = Start Frame التالية** كلما أمكن.
- Start و End من **نفس زاوية الكاميرا تقريبًا**.
- ❌ لا تستخدم End Frame عند التحول الورقي المعقد (النموذج سيمورف بشكل سيء)
  — صف الحالة النهائية بالنص بدلًا منه.
- **عدد الصور المطلوبة = عدد اللقطات + 1** عادة.

---

## Hero Shot — مواصفات ثابتة

```
HERO SHOT
──────────────────────────────────
المنتج        كامل، مركزي، بلا منافس، تغطية 0%
المساحة       محفوظة للشعار (الثلث الأدنى أو الزاوية)
الإضاءة       calm · هادئة · ثابتة
الحركة        locked-off أو حركة دقيقة جدًا
الصوت         resolve ناعم · لا percussive
المدة         2–3 ثوانٍ
```

> **الذاكرة تحتاج صمتًا.** Hero Shot هادئ دائمًا.

---

## المناطق الآمنة (9:16)

```
┌─────────────────┐ ← أعلى 14% محجوز
│                 │
│   ┌─────────┐   │
│   │  منطقة  │   │ ← يمين 12% محجوز
│   │  الفعل  │   │
│   │  الآمنة │   │
│   └─────────┘   │
│                 │
└─────────────────┘ ← أسفل 20% محجوز
```

**منطقة الفعل الآمنة:** المركز **70% عموديًا**، **85% أفقيًا**.
المنتج والـ Trigger داخلها **دائمًا**.

→ `references/specs/platform-specs.md`

---

## قائمة فحص بطاقة اللقطة

- [ ] PURPOSE محدد بهدف واحد؟
- [ ] COMPOSITION يذكر موضعًا ونسبة؟
- [ ] CAMERA: حركة واحدة + عدسة؟
- [ ] ACTION: فعل واحد بتسلسل؟
- [ ] LIGHT: نفس جملة المشروع؟
- [ ] END_STATE يوصّل بالتالية؟
- [ ] TRANSITION له سبب بصري مسمّى؟
- [ ] المنتج داخل المنطقة الآمنة؟
- [ ] Start/End frames محددان؟

---

## Cross-Reference

- `references/specs/shot-contract.md` — عقد اللقطة الكامل
- `references/specs/beat-architecture.md` — من Beat لبطاقة
- `references/specs/platform-specs.md` — المناطق الآمنة
