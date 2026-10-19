# المكتبات: اختيار لا تجميع أعمى

المسار الافتراضي Canvas + runtime الخاص بالحزمة. أربع مكتبات صغيرة مضمّنة مع notices واختبارات محددة. البدائل الأخرى مراجع، لا ادعاء بأن كل APIs تعمل أو بأن كل مكتبة تدعم العربية.

| المصدر | commit | مراجعة الرخصة | تشغيله |
|---|---|---|---|
| animejs | 01b81be1df68 | MIT-like-verify-notice | اختبار واجهة محددة ضمن المكتبات المضمّنة |
| motion | ff9db96948e3 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| motion-canvas | 7b91435c301d | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| pixijs | 65552017d232 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| threejs | ad4f951a8643 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| lottie-web | bede03d25d23 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| gsap | 13e2b7905464 | GSAP-custom-not-OSI | مرجع، غير مثبت افتراضيًا |
| remotion | f8ab752182a8 | Remotion-custom-source-available | مرجع، غير مثبت افتراضيًا |
| bezier-easing | 3f59526ae6c1 | MIT-like-verify-notice | اختبار واجهة محددة ضمن المكتبات المضمّنة |
| svg-path-properties | d67531110946 | MIT-notice-with-ISC-package-metadata | اختبار واجهة محددة ضمن المكتبات المضمّنة |
| flubber | 0cadadf3eb15 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| harfbuzzjs | 6ab59f4ebe57 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| opentypejs | 5d65b6dcfab5 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| d3-ease | 4099c6d715f5 | BSD-3-Clause | اختبار واجهة محددة ضمن المكتبات المضمّنة |
| revideo | b5de67a009a5 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| theatrejs | 6ea82b938ea4 | root-AGPL-3.0-package-metadata-Apache-2.0-conflict | مرجع، غير مثبت افتراضيًا |
| motion-studio-reference | dcf7becca293 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |
| gsap-skills-reference | aed9cfd32777 | MIT-like-verify-notice | مرجع، غير مثبت افتراضيًا |

## قرارات مهمة
- GSAP مجاني لبعض الاستخدامات بشروط؛ لا يُضمّن افتراضيًا في منشئ مرئي منافس دون مراجعة.
- Remotion ترخيصه الأصلي ذو أهلية وشروط؛ لا نعتمد جداول SEO التي تصفه MIT أو تربط الأهلية بدخل لم يذكره الترخيص المقروء.
- Theatre: تعارض بين notice الجذر وmetadata الحزمة؛ لا تثبيت تلقائي قبل فحص المكون المحدد.
- svg-path-properties: notice الموزع MIT وmetadata يقول ISC؛ احتُفظ بكليهما وكُشف التعارض بدل إخفائه.
- لا تثبت كل المحركات. اختر الأقل الذي يحقق المطلب، مع اختبار للعربية والتصيير الحتمي.
