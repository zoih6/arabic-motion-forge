---
name: quality
description: Test actual implementations and encoded motion; distinguish numeric, visual, audio, native-host and user approval evidence.
---

# quality

اقرأ `../../AGENTS.md` أولًا. لا تحمّل هذا المسار إلا حين يحتاجه الطلب.

## الإجراء
1. اختبر أصعب آلية قبل بناء الفيلم كله، ولا تجعل نجاح الوثائق دليلًا على نجاح الوسائط.
2. الدورة الأولى: hook، hierarchy، typography، asset edges، سبب كل حركة.
3. الثانية: الحركة الوسطية، speed/value curves، فصل التوقيت، التداخل، استقرار الكاميرا والـ holds.
4. الثالثة: الملف المرمّز، frame count، fps الكسري، PTS، decoder، الصوت، وصلات الأجزاء والقراءة الفعلية.
5. أصلح أول فشل والأجزاء التابعة له فقط؛ احتفظ بالإصدارات.
6. سجّل ما فُحص وما لم يُفحص. لا تملأ درجات 10/10 أو claims دعم لجميع المكتبات دون تشغيل.

## المخرجات
test-report.json، review.md، media-report.json، artifact hashes.

## بوابات
كل شرط hard يفشل يغلق التصدير النهائي. الاختبارات لا تثبت الأصالة وحدها أو خبرة كل وكيل مستقبلًا.

اقرأ [الجودة](../../reference/quality-gates.md) وشغّل اختبارات runtime والمتصفح و`tools/validate_kit.py`.
