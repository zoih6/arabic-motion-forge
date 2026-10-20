# تثبيت خفيف واختيار واضح للمنصة · Lightweight install

**Fastest (v2):** `curl -fsSL https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/install.sh | sh` → verified latest core zip (<60 s, no history/media), then `python3 ./motion-forge/tools/doctor.py`. Pin: `sh install.sh ./mf v1.0.0`. Troubleshooting: `reference/install-troubleshooting.md`.

## المسار الموصى به لأي وكيل

1. اقرأ AGENTS.md وSKILL.md.
2. نزّل الإصدار core فقط؛ لا يحتوي أفلامًا أو كود composition العرض.
3. افتح المساحة الجديدة مع هذه الملفات، ثم افحص البيئة.

```bash
python tools/install_from_release.py --destination ./motion-forge-installed
cd motion-forge-installed
python tools/doctor.py
python tools/bootstrap.py --install
npm test
python tests/browser_checks.py
```

إذا كان Chromium يحتاج حزم نظام Linux، استعمل `--system-deps` صراحة بعد التأكد من صلاحية تثبيت حزم النظام. لا تعني كتابة الملفات أن إضافة سُجلت عالميًا داخل Arena.

## Claude Code plugin

```text
/plugin install arabic-motion-forge --marketplace zoih6/arabic-motion-forge
/arabic-motion-forge:start
```

وللإصدارات التي تستخدم المسار التقليدي:

```text
/plugin marketplace add zoih6/arabic-motion-forge
/plugin install arabic-motion-forge@arabic-motion-forge
```

ملفا manifest وmarketplace داخل `.claude-plugin/`، والمهارات التسع في `skills/` بجانبهما. لا تفترض أن root CLAUDE.md يُحمّل كـplugin context؛ مهارة start تقرأ العقد صراحة. تثبيت plugin من Git يحمل المصدر الصغير، بما فيه المثال النصي، لكنه لا يحمل الفيديو. لتجنب كود المثال أيضًا استعمل core archive.

## Codex أو standalone Claude skill

```bash
python tools/install_agent.py --host codex --project /path/to/new-project
python tools/install_agent.py --host claude-skill --project /path/to/new-project
```

هذه أوامر adapter محلي وليست ادعاء بتشغيل نموذج أو تسجيل plugin أصلي. يتصل المدخل بموقع الحزمة الحقيقي ولا ينسخ الفيديوهات. لا تنقل الحزمة بعد إنشاء المؤشر دون تحديثه.

## مشروع جديد بلا قالب

```bash
python tools/new_project.py --destination /path/to/new-project --name fresh-topic --topic 'موضوع جديد'
python tools/check_project.py /path/to/new-project/project.json
```

يفشل الفحص أولًا عمدًا: املأ brief والهوية والنص وخطة الطبقات وألف المشهد. لا تولد الأداة مشهدًا من المثال. اجعل الموافقة render_allowed صحيحة فقط بعد إذن المستخدم.

## النشر الاختياري لكل مشروع

`tools/publish_session.py` يقبل `--root` و`--session-dir` مستقلين لكل مشروع، و`--visibility` الافتراضي private. التوكن يأتي من بيئة العملية المؤقتة فقط. استعمل نفس session directory في `tools/render.py --publish-session`. لا تنشر مشروع المستخدم داخل مستودع المهارة. لا توجد خدمات نموذج مدفوعة تُستدعى تلقائيًا.

## حدود التحقق

تم تشغيل Renderer و38 فحصًا برمجيًا/بصريًا في بيئة Linux الموضحة في research. ملف `research/plugin-validation.json` يميز فحص البنية بالأداة الأصلية من تشغيل workflow داخل وكيل مدفوع؛ لم يُدعَ الأخير. لم يُشغّل After Effects ولا يُعد ملف aep موجودًا.
