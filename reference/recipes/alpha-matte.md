# alpha-matte

**الحالة:** `implemented`

ألفا قناع مستقلة مضروبة في ألفا المحتوى؛ كشف العربية بعد تشكيلها.

المسميات المرتبطة: Character Reveal, Clipping Reveal, Line Reveal, Mask Reveal, Mask Transition, Mask Wipe, Matte Reveal, Reveal In, Slide Reveal, Split Reveal, Text Build, Wipe In, Wipe Transition, Word Reveal

## آلية التنفيذ

الدوال العامة: `maskedSprite`, `rtlMatte`. اقرأ عقودها في `runtime/core.mjs` و`runtime/canvas.mjs`. لا يوجد في هذه الوصفة تكوين مشهد جاهز أو هوية بصرية.

## عقد التوقيت

- Before: حالة واضحة خارج زمن الفعل، لا عنصر ظاهر بالخطأ.
- Active: مفاتيح أو دالة مستمرة مع easing مختار؛ اجعل المحتوى المؤكد مقروءًا.
- Settle: يصل العنصر إلى القيمة النهائية دون قفزة، أو يثبت في hold صريح.
- Secondary: ابدأ التسطير والمؤشر أو الظل في توقيت مستقل إذا خدم المعنى.

## اختبار القبول

اختبر الأزمنة قبل البداية، داخل الحركة، وعند الاستقرار، ثم اطلبها بترتيب مختلف. راجع نهاية المسار/الـ matte وحدود النص والاتصال العربي. لا تعتبر وجود اسم الدالة دليلًا على صلاحية كل فرع؛ راجع القيود والحالة أعلاه ونتيجة الاختبارات.

## رفض الاستخدام السطحي

لا تطبق هذه الحركة على مجموعة كاملة إذا احتاجت عناصرها إلى بناء مستقل. لا تعدّل النص أو الخط المعتمد لتجاوز عيب تقني. لا تدّعِ أن الآلية هي أداة AE الأصلية.

```js
const shaped = textSprite("المعنى أولاً", {size: 160, direction: "rtl"});
const mask = rtlMatte(shaped, smooth((t - 0.25) / 0.9), {bands: 3, slant: 22, target: reusableSurface});
ctx.drawImage(mask, x, y); // تبقى حروف المصدر متصلة
```
