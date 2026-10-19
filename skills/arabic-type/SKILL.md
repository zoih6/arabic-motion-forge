---
name: arabic-type
description: Preserve Arabic joining, bidi, approved copy and font metrics while designing matte and word-level typography.
---

# arabic-type

اقرأ `../../AGENTS.md` أولًا. لا تحمّل هذا المسار إلا حين يحتاجه الطلب.

## الإجراء
1. اقفل النص والخط بعد الاعتماد. حمّل الخط قبل التصيير، واضبط RTL وbidi للمقاطع المختلطة والأرقام.
2. شكّل الكلمة أو السطر كاملًا ثم حرّك القناع. لا تعكس Unicode أو تفصل الحروف المتصلة بـ split('').
3. قِس actualBoundingBoxAscent/Descent واترك هوامش للتشكيل؛ لا يكفي font-size لحساب صندوق النص.
4. استخدم word/line selectors للعربية افتراضيًا. لا تدّعِ دعم character transforms إلا إذا ثبتت سلامة التشكيل والوصل.
5. الكتابة بالقلم تحتاج stroke trajectories معروفة؛ لا تسمِّ outline أو wipe كتابة يد حقيقية.
6. اختبر النص داخل الحركة وعند القراءة بالحجم الصغير، لا في لقطة النهاية فقط.

## اختبارات إلزامية
قناع 0 شفاف تمامًا، قناع 1 مطابق للنص المشكّل، lam-alef/diacritics سليمة، no unexpected copy، وحروف متصلة لا تتباعد.

اقرأ [العربية](../../reference/arabic.md) و[اختبارات المتصفح](../../tests/browser_checks.py).
