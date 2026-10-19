# Arabic Motion Forge
### نظام إنتاج موشن جرافيك عربي — لا مكتبة قوالب يعاد تلوينها

حزمة تعليمات ومهارات وكود تنفيذي لبناء فيديوهات جديدة بطبقات مستقلة، كشف طباعي سليم، حركة مقصودة، وتصـيير قابل للتحقق. **الفيديو التجريبي منجز: 80 ثانية، 1080×1920، 32fps، 4.7 MB.** **الإصدار 1.0.0 جُرّب بتثبيت نظيف**: الحزمة لا تحمل الفيديو أو كود مشاهد المثال، وتعيد اختبارات النواة بنجاح. راجع تقارير `research/` لنطاق الإثبات والقيود.

## التنزيل والتشغيل

- [حزمة التثبيت الخفيفة — نحو 1.1 MB](https://github.com/zoih6/arabic-motion-forge/releases/download/v1.0.0/arabic-motion-forge-core-1.0.0.zip)
- [الفيديو العمودي الكامل — 80 ثانية](https://github.com/zoih6/arabic-motion-forge/releases/download/v1.0.0/meaning-first-portrait-1080p32.mp4)
- [مختبر مستقل قابل للتمرير الزمني](https://github.com/zoih6/arabic-motion-forge/releases/download/v1.0.0/motion-lab.html)
- [تعليمات التثبيت والمنصات](INSTALL.md) · [المصادر والتراخيص](THIRD_PARTY.md) · [البحث](research/README.md)

الفيديو يعرض الفئات الثماني بأمثلة منتقاة، وليس كل تسمية من 104 كأنها تقنية مستقلة. المختبر التشخيصي يعرض أربع آليات فعلية؛ بقية النطاق موثّق في القاموس والاختبارات.

## ابدأ من هنا

- **[AGENTS.md — عقد تشغيل الوكيل](AGENTS.md)**
- **[SKILL.md — المدخل المحمول لأي وكيل](SKILL.md)**
- **[مسار الإنتاج](workflows/route.md)**
- **[قاموس 104 مداخل / 103 مسميات / 33 آلية](catalog/README.md)**
- **[سجل 18 مستودعًا ومراجعة تراخيصها](catalog/libraries.lock.json)**
- **[المكتبات الأربع المضمّنة والمثبتة](catalog/bundled-libraries.json)**

## هيكلة فعلية للمهارة والإضافة

```text
.claude-plugin/
  plugin.json                 # تعريف Claude Code plugin
  marketplace.json            # فهرس تثبيت الإضافة
.agents/skills/arabic-motion-forge/
  SKILL.md                    # مدخل Codex / Agent Skills
  agents/openai.yaml          # بيانات اكتشاف المهارة
AGENTS.md                     # قواعد الإنتاج والأمان والتسليم
SKILL.md                      # العقد المحمول ونقطة البداية
CLAUDE.md                     # إدخال تعليمات المستودع
skills/
  start/                      # /arabic-motion-forge:start
  intake/                     # brief وأسئلة ونطاق
  originality/                # هوية جديدة ومنع استنساخ الأمثلة
  motion-direction/           # طبقات ومفاتيح وكاميرا ومسارات
  arabic-type/                # shaping وRTL وmatte reveals
  asset-craft/                # أصول حقيقية/مولدة وقص وظلال
  audio-sync/                 # صوت وتوقيت وغناء ووصلات
  quality/                    # اختبارات ومراجعة الفيلم المرمّز
  delivery/                   # ميزانية وحفظ ونشر واستعادة
runtime/                      # رياضيات ورسم عام، لا تكوينات جاهزة
catalog/                      # القاموس والقدرات والتراخيص
reference/recipes/            # عقود سلوك الحركات وقيودها
vendor/ai-film-studio/         # نظام الفيلم المقدم من المستخدم
vendor/motion-reel/            # المهارة المساعدة مع بيان ترخيصها
vendor/primitives/             # مكتبات صغيرة مع إشعاراتها
examples/vertical-showcase/    # دراسة تطبيقية، ممنوع استعمالها قالبًا
```

## تثبيت Claude Code plugin

```text
/plugin install arabic-motion-forge --marketplace zoih6/arabic-motion-forge
/arabic-motion-forge:start
```

هذه بنية توزيع وفق توثيق المنصة، وليست ادعاءً بتشغيل وكيل Claude أو نموذج مدفوع هنا. اختبار manifest واختبار workflow حي مرحلتان مختلفتان.

## تشغيل وفحص الأدوات البرمجية

```bash
python tools/bootstrap.py --install
npm test
python tests/browser_checks.py
```

إضافة `--system-deps` اختيار صريح لتثبيت تبعيات Chromium على Linux. لا تفترض Windows ولا تتبع أبعاد أو fps ملفات vendor آليًا.

## ما هو منفذ وما هو مرجع فقط؟

- نواة حتمية: keyframes، منحنيات Bezier، نوابض تحليلية، سقوط وارتداد، قص مسارات، تتبع رأس السهم، morph برؤوس متقابلة، parent transforms، وأقنعة ألفا وسطوع محددة النموذج.
- **20 اختبار Node ناجحًا و18 اختبار متصفح ناجحًا**، مع ملفات النتائج داخل `research/`.
- المكتبات المضمّنة: Anime.js، Bezier Easing، d3-ease، svg-path-properties. اختُبرت واجهات محددة منها، لا كل ميزاتها.
- بقية المحركات مراجع مدققة وليست جميعها مثبتة أو مختبرة. GSAP وRemotion لا يُصنّفان تلقائيًا كرخص MIT. سجلات التعارضات الترخيصية محفوظة.
- لا تشغيل أصلي لـAfter Effects ولا إنشاء `.aep` مزعوم. المكافئات البرمجية تُسمّى بآلياتها، والقيود ظاهرة.

## لماذا لا يعيد إنتاج الحمراء؟

الأمثلة للتعلّم فقط. ممنوع نقل أسلوب الحمراء أو أصولها أو كود مشاهدها، وممنوع نسخ تكوين العرض العمودي ثم تبديل كلماته. المسموح هو البنية الرياضية وأدوات الرسم والتصيير العامة. كل موضوع يبدأ بفكرة وهوية وأصول وخطة طبقات جديدة.

## التثبيت الخفيف والحفظ

الفيديوهات لا تدخل git؛ رُفعت الأجزاء إلى **[Releases](https://github.com/zoih6/arabic-motion-forge/releases)**. التنزيل الأساسي للإصدار يستثني الوسائط وكود composition التجريبي. تثبيت plugin من Git يحمل المصدر الصغير، لا ملفات الفيديو. لا يُحمّل النظام مستودع الحمراء كاملًا.

كل مشروع جديد يحتاج إذنًا ووجهة نشر خاصة به. لا تنشر مواد المستخدم تلقائيًا في مستودع المهارة. لا توكنات في المصدر أو الأوامر الملتزمة أو روابط git.

**الترخيص:** الكود الأصلي منفصل عن تراخيص vendor؛ احتفظ بكل إشعارات المصادر. لا تفترض أن حزمة مجانية تعني أن جميع مكوناتها OSI open-source.
