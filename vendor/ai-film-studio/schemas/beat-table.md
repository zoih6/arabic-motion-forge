---
name: schema-beat-table
description: "قالب جدول الـ Beats: نسخة وثائقية (3 أعمدة) ونسخة إعلانية (7 أعمدة) + قواعد الحساب والفحص."
tier: 3
when_to_load: "E1 الحالة 6 · E2 المرحلة 3 · M3b"
---

# Beat Table — جدول الـ Beats

## نسخة 1 — الوثائقي (ما يراه المستخدم)

ثلاثة أعمدة **حرفيًا**:

| Beat | التوقيت | الكلمات |
|---|---|---|
| 1 | 0.0s | "24 نوفمبر 1971." |
| 2 | 1.2s | "مطار بورتلاند الدولي." |
| 3 | 2.8s | "رجل ببدلة داكنة يدفع نقدًا مقابل تذكرة ذهاب واحدة." |

**القواعد:**
- الكلمات تُكتب **حرفيًا كما وردت في السكربت** بين علامتي تنصيص.
- التوقيتات تراكمية (مجموع كلمات السابقة ÷ 2.5).
- الـ Beat الأول من `0.0s`.
- **كل كلمة من السكربت تُغطى مرة واحدة بالضبط.**

---

## نسخة 2 — الإعلان (الصيغة الداخلية)

| Beat | In–Out | Function | Visual (جملة واحدة) | Product presence | Sound cue | Shot ID |
|---|---|---|---|---|---|---|
| 01 | 0.0–1.2 | Hook | Extreme macro of foil paper texture catching light, unclear what it is | Indirect (color) | paper rustle | S01 |
| 02 | 1.2–3.0 | Reveal | Camera pulls back: it is the product's cap, real, on a paper landscape | Direct, partial | soft thud | S02 |
| 03 | 3.0–5.0 | Desire | Macro on condensation droplets sliding down the cap | Direct | droplet tick | S03 |
| 04 | 5.0–6.0 | Silence | Almost still frame, whole world holds breath | Direct | near silence | S04 |
| 05 | 6.0–8.0 | Trigger | A red string snaps taut and pulls the whole paper world apart | Direct | string zip | S05 |
| 06 | 8.0–11.0 | Escalation | Paper hills unfold into a full landscape around the product | Direct | paper cascade | S06 |
| 07 | 11.0–13.0 | Payoff | The landscape settles: the product at the center of a golden world | Full | warm swell | S07 |
| 08 | 13.0–15.0 | Hero + End Card | Product alone on calm surface, space reserved for logo | Full, 0% covered | soft resolve | S08 |

**القاعدة:** كل صف يصبح **بطاقة لقطة**. **لا Beat بلا Shot ID.**

---

## حقول النسخة الإعلانية

| الحقل | القاعدة |
|---|---|
| **Beat** | رقم متسلسل `01`, `02`, ... |
| **In–Out** | توقيتان بمنزلة عشرية |
| **Function** | واحدة من: Hook · Curiosity · Reveal · Desire · Silence · Trigger · Escalation · Payoff · Hero |
| **Visual** | **جملة واحدة** — صورة واحدة |
| **Product presence** | Direct full / Direct partial / Indirect (color/shadow/reflection) / Absent |
| **Sound cue** | صوت واحد أو صمت |
| **Shot ID** | `S01`, `S02`, ... |

---

## قواعد الحساب

### مع تعليق صوتي
```
توقيت Beat(n) = مجموع كلمات Beats 1..(n-1) ÷ 2.5   (إنجليزي)
                                              ÷ 2.4   (عربي فصيح هادئ)
```

### بلا تعليق صوتي
| نوع اللقطة | المدة |
|---|---|
| ماكرو ثابت | 1–1.5 ث |
| فعل / تحول | 2–3 ث |
| Hero Shot | 2–3 ث |
| صمت قبل الذروة | 0.6–1 ث |

→ `references/specs/beat-architecture.md`

---

## قائمة فحص الجدول

- [ ] عدد الـ Beats داخل نطاق المدة؟
- [ ] كل Beat: وظيفة واحدة + صورة واحدة + فعل واحد؟
- [ ] المنتج/أثره كل ≤ 3 ث (≤ 2 ث في 6–10 ث)؟
- [ ] منحنى الطاقة يصعد حتى Payoff ثم يهبط؟
- [ ] Beat صمت قبل الذروة موجود (في ≥ 15 ث)؟
- [ ] كل انتقال له سبب بصري مسمّى؟
- [ ] حذف أي Beat يُخرّب السرد؟
- [ ] كل Beat له Shot ID؟
- [ ] كل كلمة من السكربت مغطاة مرة واحدة؟ (الوثائقي)

---

## Cross-Reference

- `references/specs/beat-architecture.md` — الحساب الكامل
- `schemas/shot-card.md` — من Beat إلى بطاقة لقطة
- `references/specs/shot-contract.md` — عقد اللقطة
