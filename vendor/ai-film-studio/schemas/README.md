# Schemas

> **Tier 3 — هياكل البيانات (Data Structures).** تُحمَّل عند إنتاج المخرجات.

كل ملف هنا هو **قالب فارغ** أو **مثيل حي** لمخرج معيّن. الـ schemas ليست برومبتات — هي **هياكل بيانات** تُملأ ثم تُسلّم.

## التصنيف

### مخرجات الإنتاج (Production Outputs)

| الملف | متى يُستخدم | يُنتَج من |
|---|---|---|
| `production-blueprint.md` | نهاية M0–M9 | Executive Producer |
| `image-prompts-package.md` | M7 | Prompt Architecture |
| `motion-prompts-package.md` | M8 | Prompt Architecture |
| `audio-package.md` | M6 | Audio Decision Engine |
| `assembly-guide.md` | M10 | Executive Producer |
| `concept-deck.md` | M1 (Concept) | Research Lab |
| `style-dna-sheet.md` | M4b | Character-World |
| `delivery-package.md` | M10 | EP (قديم) |
| `production-brief.md` | M0 | Intake (قديم) |

### State Files (Runtime State)

في `state/`:
- `references/knowledge/project-memory.md` — ذاكرة المشروع الدائمة
- `schemas/state/continuity-bible.md` — قاموس الهوية البصرية
- `schemas/state/frame-chain.md` — Start/End Frame Registry
- `schemas/state/asset-registry.md` — كل الأصول المُنتجة
- `schemas/state/decision-log.md` — كل القرارات المهمة
- `schemas/state/risk-register.md` — المخاطر + mitigation
- `schemas/state/quality-gates-log.md` — G0–G8 log
- `production-brief.md` — موجز المشروع
- `production-blueprint.md` — نسخة state من blueprint
- `schemas/state/reference-library.md` — مرجعيات بصرية
- `schemas/state/continuity-ledger.md` — سجل اتساق
- `schemas/state/approval-log.md` — الموافقات
- `schemas/state/generation-log.md` — محاولات التوليد
- `schemas/state/session-checkpoint.md` — checkpoint للجلسات

## كيف تستخدم

1. **انسخ** الـ schema المناسب إلى مشروعك
2. **املأ** كل قسم (لا تترك حقول فارغة)
3. **اربط** cross-references بين الـ schemas
4. **سلّم** عبر EP
