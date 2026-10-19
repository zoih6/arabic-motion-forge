---
name: schema-adaptive-production-sheet
description: "عقد ورقة إنتاج متكيفة تُنشأ لكل طلب فيديو قبل البرومبتات والتوليد."
tier: 3
when_to_load: "بعد تثبيت الـBrief وقبل الـStoryboard أو Prompts"
---
# Adaptive Production Sheet — ورقة الإنتاج المتكيفة

## الغرض
هذه الورقة هي **مصدر الحقيقة التنفيذي** لكل فيديو. تُنشأ حتى لو كانت المدة 10 ثوانٍ، لكن حجمها يتكيف مع المدة، نوع المحتوى، منصة النشر، نموذج الفيديو، وتعقيد الفعل. لا تُستخدم لعرض تفاصيل A–J؛ بل لتثبيت ماذا يحدث، ومتى، وبأي مرجع، وكيف ينتقل إلى اللقطة التالية.

> القاعدة: المدة تحدد عدد اللقطات وحدودها، لكنها لا تلغي التخطيط. لا توجد لقطة بلا وظيفة، ولا تتجاوز اللقطات مجموع المدة المستهدفة.

## قواعد التكيّف

| المدة | النطاق المقترح | قاعدة التقطيع |
|---|---:|---|
| 1–5s | 1 لقطة | فعل بصري واحد أو كشف واحد؛ لا تحشر قصة كاملة |
| 6–10s | 1–3 لقطات | خطاف + فعل/رد فعل؛ الأولوية للوضوح |
| 11–20s | 3–5 لقطات | خطاف، تصعيد، نتيجة، وقفة/دعوة عند الحاجة |
| 21–40s | 5–9 لقطات | بداية، تصعيد، عائق/تحول، إيفاء |
| 41–90s | 8–15 لقطة | بنية سردية كاملة مع مساحة للصوت والانتقالات |
| أكثر من 90s | حسب المشاهد | قسّم إلى مشاهد ثم أنشئ ورقة لكل مشهد وورقة إجمالية |

هذه الحدود إرشادية وليست قوالب جامدة. يجب أن تكون كل لقطة ضمن حدود النموذج المختار، وأن يُسجّل سبب أي استثناء.

## الغلاف (Metadata)

```yaml
production_sheet:
  sheet_id: "SHEET-<PROJECT_ID>-v1"
  project_id: "<PROJECT_ID>"
  version: 1
  status: "draft | in_review | approved | locked"
  created_from_request: "النص الأصلي لطلب المستخدم"
  content_type: "short | narrative | commercial | documentary | explainer | music_video"
  platform: "TikTok | Reels | Shorts | YouTube | TV | multi_platform"
  aspect_ratio: "9:16"
  duration_seconds: 10
  target_model: "bytedance/seedance-2.0"
  language: "ar"
  adaptation:
    recommended_shot_count: 2
    actual_shot_count: 2
    allocation_method: "hook-action-payoff"
    exception_reason: ""
  continuity_locks:
    identity: ["CHAR-01"]
    locations: ["LOC-01"]
    props: ["PROP-01"]
    style: ["STYLE-01"]
```

## أعمدة الشيت الإلزامية

| العمود | الغرض |
|---|---|
| `scene_id` | المشهد الذي تنتمي إليه اللقطة، مثل `SC01` |
| `shot_id` | معرف ثابت مثل `SC01_SH02` |
| `time_in` / `time_out` | بداية ونهاية اللقطة بالثواني |
| `duration_seconds` | مدة اللقطة؛ يجب أن تساوي `time_out - time_in` |
| `story_role` | hook / setup / action / escalation / reveal / payoff / end_card |
| `viewer_takeaway` | ما يجب أن يفهمه المشاهد عند نهاية اللقطة |
| `visual_action` | فعل مرئي واحد قابل للتنفيذ |
| `framing` | حجم اللقطة والزاوية |
| `camera_motion` | حركة كاميرا مهيمنة واحدة فقط |
| `subject_ids` | معرفات الشخصيات/المنتجات |
| `reference_ids` | anchors المستخدمة في هذه اللقطة |
| `start_state` / `end_state` | حالتا البداية والنهاية وسلسلة الإطارات |
| `motion_prompt_status` | pending / ready / approved |
| `audio_plan` | ambience / foley / SFX / dialogue / music / silence |
| `transition_in` / `transition_out` | طريقة الدخول والخروج |
| `continuity_locks` | ما يجب ألا يتغير |
| `model` | نموذج الفيديو المقترح |
| `acceptance_criteria` | شروط قبول اللقطة |
| `status` | draft / approved / generated / rejected |

## قالب صف واحد

```yaml
- scene_id: "SC01"
  shot_id: "SC01_SH01"
  time_in: 0.0
  time_out: 4.0
  duration_seconds: 4.0
  story_role: "hook"
  viewer_takeaway: "يفهم المشاهد المشكلة فورًا."
  visual_action: "الشخصية ترى العائق وتتخذ قرارًا واضحًا."
  framing: "medium wide, eye level"
  camera_motion: "slow tracking left-to-right; no zoom, no rotation"
  subject_ids: ["CHAR-01"]
  reference_ids: ["CHAR-01", "LOC-01"]
  start_state: "..."
  end_state: "..."
  motion_prompt_status: "pending"
  audio_plan: "jungle ambience; one decision cue; no dialogue"
  transition_in: "hard_cut"
  transition_out: "match_on_action"
  continuity_locks: ["CHAR-01 identity", "LOC-01 lighting", "screen direction →"]
  model: "bytedance/seedance-2.0"
  acceptance_criteria: ["الفعل مقروء", "الهوية ثابتة", "لا يوجد قطع داخلي"]
  status: "draft"
```

## بوابات الورقة

1. `duration_seconds > 0` لكل صف، و`sum(duration_seconds) == duration_seconds` في الغلاف (بهامش 0.05s).
2. لا يوجد تداخل زمني ولا فجوة غير مقصودة بين اللقطات.
3. لكل لقطة `story_role` و`viewer_takeaway` وفعل مرئي واحد.
4. لكل لقطة مرجعيات، وحالة بداية/نهاية، وخطة صوت حتى لو كانت `N/A` بسبب معلن.
5. كل `shot_id` فريد، وكل لقطة لها صف لاحق في الـStoryboard وPrompt الحركة.
6. لا يُعتمد الشيت قبل اعتماد `reference_manifest` في مشروع متعدد اللقطات.
7. مدة اللقطة توافق حدود النموذج؛ عند عدم التوافق تُقسّم أو تُسجّل خطة امتداد صريحة.

## ترتيب التسليم للمستخدم

1. ملخص التكييف: المدة، عدد اللقطات، طريقة التقسيم، والافتراضات.
2. جدول الشيت المختصر القابل للقراءة.
3. زر/ملف `CSV` بنفس الأعمدة، للنسخ إلى Google Sheets أو Excel.
4. بعد الاعتماد: Storyboard ثم Prompt صورة كامل لكل فريم ثم Prompt حركة كامل لكل لقطة.

لا يُطلب من المستخدم تركيب Prompts من أعمدة متعددة؛ الشيت للتخطيط والتتبع، وكل Prompt نهائي يبقى كتلة واحدة مكتملة.
