# Context Assembly — AI Film Studio v1.2

## الهدف
بناء سياق صغير ودقيق قبل الاستدلال بدل إغراق النموذج بكل ملفات المهارة.

## Context Tiers
### Tier 0 — Always
- `SKILL.md`
- `references/protocols/`
- `references/protocols/`
- `workflows/intent-router.md`
- `references/protocols/`

### Tier 1 — Task Specific
حمّل فقط المرجعيات المطلوبة للمسار: prompt patterns، shot contract، text matrix، model matrix، إلخ.

### Tier 2 — Project State
عند استمرار مشروع:
- production brief
- asset registry
- continuity ledger
- approval log عند الحاجة
- آخر versions المعتمدة

### Tier 3 — Specialist
حمّل agent file واحدًا أو أكثر فقط بناءً على Intent Router.

## Context Budget Rule
لا تضع جميع الوكلاء في السياق تلقائيًا. كل ملف إضافي يجب أن يجيب عن سؤال: «هل يحتاج التنفيذ هذه المعرفة الآن؟»

## Precedence
```text
explicit user constraint
> approved project state
> Scene DNA
> Shot DNA
> specialist guidance
> default studio choice
```

## Stale Context Protection
إذا تعارضت معلومة قديمة مع state أحدث معتمد، استخدم الأحدث. لا تعيد إحياء نسخة قديمة من الهوية أو اللقطة لمجرد وجودها في سياق سابق.
