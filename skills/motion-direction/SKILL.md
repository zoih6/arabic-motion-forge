---
name: motion-direction
description: Design independent layer choreography, masks, paths, parent controls, keyframes and motivated camera motion.
---

# motion-direction

اقرأ `../../AGENTS.md` أولًا. لا تحمّل هذا المسار إلا حين يحتاجه الطلب.

## الإجراء
1. اكتب وظيفة اللقطة ثم قائمة عناصرها المستقلة. افصل العنوان والتسطير والقصاصة والصورة والحامل والظل.
2. لكل عنصر: قبل الحركة، بداية، مراحل وسطية، اكتمال، hold أو خروج. حدد easing والقنوات الضرورية فقط.
3. اربط الخط برأسه عبر arc length نفسه. لا يظهر السهم كاملًا بينما يُرسم الخط.
4. استخدم parent لعلاقة حقيقية مع استقلال قنوات الأبناء؛ لا تجعل composition كلها طبقة تتحرك بنفس الإيقاع.
5. اختر الكاميرا بعد وضوح البؤرة. depth/parallax لا يعوض الحركة الداخلية.
6. صمم الانتقال من علاقة المشهدين. لا تعتمد preset انتقال عام على كل حد.

## المخرجات
`$project/layer-plan.json`، مفاتيح زمنية، render entry تقبل الزمن وحده.

## التحقق
البدء والنهاية والأزمنة الوسطى، اختلاف signatures القنوات، عدم تعارض النص والمؤشر، وحتمية seek.

اقرأ [القاموس](../../catalog/README.md) و[المكافئات](../../reference/ae-equivalence.md) و[الطبقات](../../reference/layer-design.md).
