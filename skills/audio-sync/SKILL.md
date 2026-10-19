---
name: audio-sync
description: Preserve supplied speech and music, obey exact source intervals, align typography, and verify the encoded mix.
---

# audio-sync

اقرأ `../../AGENTS.md` أولًا. لا تحمّل هذا المسار إلا حين يحتاجه الطلب.

## الإجراء
1. افحص الملف الفعلي ومدته ووسومه وأخذ عيناته. مطابقة الكلمات لا تعني مطابقة الأداء أو النسخة المطلوبة.
2. التوقيت الذي حدده المستخدم أَولى من ذوق الوكيل. إن كان الأداء ملتبسًا، اطلب تحديدًا أو اعرض مقتطفًا بدل التخمين.
3. افصل sample-accurate cut عن frame-quantized video؛ سجل أي padding أو فرق تكميم.
4. في الغناء: دوّن هل يتوقف الراوي، وما النص المستبدل، ومن أين يعود. لا تطبق ducking فقط إذا طُلب إيقافه.
5. LRC/ASR قرائن. صحح الكلمات من النص الصحيح، وميّز التوقيت التقريبي والمدود. لا تدّعِ استماعًا لم تسمح به الأداة.
6. استخرج onsets/energy للرسوم المتفاعلة. لا تجعل موجة عشوائية تبدو كتحليل للصوت.
7. قِس LUFS/true peak بعد الترميز. عند الدمج استخدم mix مستمرًا بدل تكرار priming AAC لكل جزء.

## المخرجات
audio-edit-map.json، cue/word timing، mix report، حقوق ومصدر التسجيل.

اقرأ [الصوت](../../reference/audio.md).
