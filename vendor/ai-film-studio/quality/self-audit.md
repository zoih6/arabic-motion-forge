---
name: self-audit
description: Prompt self-audit يُستخدم قبل إعلان PASS على أي Quality Gate
tier: 3
---

# Self-Audit Prompt

## قبل إعلان PASS

اقرأ هذا الـ prompt بصوت عالٍ، أو اطلب من النموذج الإجابة عليه.

## Prompt

```
أنا الآن في Quality Gate [G_X]. المخرج الذي أنتجته:
[أدخل المخرج هنا]

قيّمه بدقة:

1. **هل حقق كل معايير الـ Gate؟**
   - اذكر كل criterion موثّق
   - قيّم: PASS / FAIL / PARTIAL

2. **هل هناك critical failures؟**
   - G4: هل كل prompt يحوي 10 طبقات A-J؟
   - G4: هل Identity String منسوخ حرفيًا؟
   - G6.4: هل Brand Logo في post_overlay؟
   - G8: هل 5 Output Files مكتملة؟
   - G8: هل كل G السابقة = PASS؟

3. **هل النتيجة موثقة؟**
   - schemas/state/quality-gates-log.md محدّث
   - decision-log محدّث (إن قرار جديد)
   - risk-register محدّث (إن خطر جديد)

4. **هل المستخدم راضٍ؟**
   - موافقة على Concept Deck (M2)
   - موافقة على Script (M3)
   - موافقة نهائية (M11)

## النتيجة المتوقعة

- **PASS:** كل المعايير ✓ + 0 critical failures + موثّق + رضا المستخدم
- **REQUIRES_REVIEW:** 1-2 soft failures (مقبول إذا المستخدم راضٍ)
- **FAIL:** أي critical failure أو 3+ soft failures

## عند FAIL

لا تنتقل. أصلح ثم أعد الفحص.
وثّق السبب في quality-gates-log.md.
```

## مثال: G4 Self-Audit

```
أنا في G4 (Prompt Quality).

المخرج: 12 prompt، كل واحد بالـ 10 طبقات A-J.

1. المعايير:
   ✓ كل prompt يحوي A-J (10/10)
   ✓ Identity String منسوخ حرفيًا
   ✓ Negative Prompts في كل prompt
   ✓ Reference Images مذكورة
   ✓ Model + Aspect Ratio محدد
   ✓ Continuity refs

2. Critical failures: 0

3. التوثيق:
   ✓ generation-log.md محدّث
   ✓ quality-gates-log.md محدّث

4. المستخدم: راضٍ (لم يُطلب تعديل)

النتيجة: PASS ✅
```
