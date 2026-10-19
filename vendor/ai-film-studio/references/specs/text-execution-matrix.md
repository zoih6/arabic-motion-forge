# Text Execution Matrix — v1.1

| نوع النص | مكان التنفيذ | السبب |
|---|---|---|
| عنوان ثابت داخل Poster/Key Visual | Image model | يحافظ على علاقة النص بالتكوين |
| Copy ثابت داخل صورة مطلوبة كمرجع نهائي | Image model | النص جزء من الفريم |
| Kinetic Typography | Motion/Editing layer | يحتاج توقيتًا وeasing قابلين للتحرير |
| Legal / أرقام / بيانات دقيقة | Editing layer | قابلية التصحيح أهم من التوليد |
| UI / captions / subtitles | Editing layer | دقة حرفية وتزامن |
| Dialogue spoken | Audio + lipsync | النص صوت، وليس Typography |

## قاعدة القرار
إذا كان النص **جزءًا ثابتًا من الصورة** → ولّده داخل الصورة. إذا كان **يتغير مع الزمن أو يحتاج توقيتًا دقيقًا** → نفذه كطبقة خارجية. إذا كان **رقمًا/قانونيًا** ولا يحتمل الخطأ → طبقة قابلة للتحرير.
