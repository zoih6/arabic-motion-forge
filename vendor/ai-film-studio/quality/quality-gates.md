---
name: quality-gates
description: |
  توثيق شامل لـ 8 بوابات الجودة (G0–G8). كل Gate لها معايير، scoring، وإجراء الفشل.
  Hard Gates: G4 + G8. لا تُتجاوز أبدًا.
  **AUTHORITATIVE للـ stages:** `references/protocols/production-state-machine.md`.
  هذا الملف = نظرة عامة + scoring + Fail Action Protocol.
  التفاصيل الكاملة لكل Gate: `workflows/M9b-quality-gates.md`.
tier: 3
---

# Quality Gates — 8 بوابات جودة (v2.0.2)

> **Authoritative للـ stages:** `references/protocols/production-state-machine.md` (v2.0.2).
> **Authoritative للـ scoring:** هذا الملف.
> **Authoritative للتفاصيل الكاملة:** `workflows/M9b-quality-gates.md`.
> عند التضارب: state-machine يحدد المرحلة، quality-gates يحدد القواعد.

## Source of Truth Hierarchy

```
production-state-machine.md  → يحدد "متى" (بعد أي M-stage)
           ↓
quality-gates.md (هذا)       → يحدد "كم" (PASS / REVIEW / FAIL scoring)
           ↓
M9b-quality-gates.md         → يحدد "كيف" (criteria تفصيلية لكل gate)
```

## نظرة عامة (8 Gates)

| Gate | الاسم | بعد المرحلة | المسؤولية | النوع |
|---|---|---|---|---|
| **G0** | Intake Clarity | M0 | Executive Producer | Soft |
| **G1** | Idea Quality | M1 | Research Lab | Soft |
| **G2** | Narrative Quality | M2 | Narrative Architect | Soft |
| **G3** | Continuity Quality | M4 (M4a + M4b + M4c) | Continuity Supervisor + M4c QC | Soft |
| **G4** | **Prompt Quality** | M7 + M8 | Prompt Architecture | **HARD** |
| **G5** | Transition Quality | M4d | Transition Engineer | Soft |
| **G6** | Text Quality | M5 (M5a + M5b) | Graphics + Text | Soft (critical on G6.4) |
| **G7** | Audio Quality | M6 (M6a + M6b + M6c) | Audio | Soft |
| **G8** | **Master Quality** | M10 + M11 | EP + QG | **HARD** |

## Hard Gates

**G4 (Prompt Quality):** لا prompt بدون 10 طبقات A-J. Identity String حرفي. Reference images إلزامية.
**G8 (Master Quality):** لا تسليم بدون 5 Output Files كاملة. كل Quality Gates السابقة PASS.

**أي critical failure على G4 أو G8 = مشروع مرفوض. لا استثناءات.**

## Scoring

| الفشل | النتيجة |
|---|---|
| 0 | PASS |
| 1-2 (soft) | REQUIRES_REVIEW |
| 3+ (soft) | FAIL |
| 1+ (critical) | FAIL (Hard Gate) |
| 1+ (G6.4 Brand Logo) | FAIL |

## التفاصيل لكل Gate

راجع `workflows/M9b-quality-gates.md` للتفاصيل الكاملة.

## Self-Audit Prompt

```
قبل إعلان PASS، اسأل نفسك:
1. هل هذا الـ Gate يحقق المعايير الموثقة؟
2. هل هناك أي critical failure؟
3. هل النتيجة موثّقة في quality-gates-log.md؟
4. هل المستخدم راضٍ (للمراحل التي تتطلب موافقته)؟
```

## Fail Action Protocol

```
عند FAIL:
1. أوقف المشروع
2. وثّق الفشل في quality-gates-log.md
3. حدد الوكيل المتضرر
4. أعد المرحلة من نقطة الفشل
5. أعد الفحص
6. لا تنتقل أبدًا بـ FAIL
```

## Cross-Reference

- Stage model (AUTHORITATIVE): `references/protocols/production-state-machine.md`
- Orchestration (executable spec): `references/protocols/orchestration-runtime.md`
- Implementation (تفاصيل كل gate): `workflows/M9b-quality-gates.md`
- Log: `schemas/state/quality-gates-log.md`
- Checklist: `quality/checklist.md`
- Self-audit prompt: `quality/self-audit.md`
