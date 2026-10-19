---
name: shortcut-repair
description: أصلح جزءًا محددًا من مشروع قائم
tier: 2
parent: workflows/M9b-quality-gates.md
duration: 5-15 min
---

# Shortcut: Repair

## Entry Conditions
- ✅ طلب: "هذا مكسور"، "أصلح"، "إعادة"
- ✅ الجزء المتضرر محدد
- ❌ لا تبدأ مشروع جديد

## Core Workflow (5 خطوات)

### 1. شخّص المشكلة (2 min)
اسأل/اقرأ:
- ما الذي لا يعمل؟
- متى بدأ الفشل؟
- ما النتيجة المتوقعة vs الحالية؟

ارجع لـ `references/knowledge/failure-modes.md` للأخطاء الشائعة.

### 2. حدد الوكيل المتضرر (1 min)
| المشكلة | الوكيل |
|---|---|
| هوية الشخصية تختلف | M4a-continuity |
| نص مشوّه | M5a-graphics + M5b-text-motion |
| إضاءة غير متسقة | M4a-continuity |
| محور 180 مكسور | M4a-continuity |
| lip-sync ضعيف | M6c-dialogue-lipsync |
| صوت منخفض/مرتفع | M6-audio |
| حركة غير سلسة | M7a-prompt-architecture |
| لون مختلف بين shots | M4a-continuity |

### 3. أصلح (5-10 min)
- أعد prompt بنفس القواعد (10 طبقات A-J)
- أضف/حدّث reference images
- حسّن الـ negative prompts
- ولّد 3-5 variants واختر

### 4. تحقق (1 min)
- شغّل الـ Quality Gate المناسب
- راجع مرة أخرى ضد prompt

### 5. وثّق (1 min)
- أضف لـ `schemas/state/decision-log.md`
- أضف لـ `schemas/state/risk-register.md` (إن كان جديدًا)

## Quality Gate
- حسب الوكيل المتضرر، نفس G الأصلي

## Output
- النسخة المُصلحة
- decision-log entry
- (اختياري) risk-register entry

## Common Mistakes
- ❌ إعادة بناء كل شيء (ابدأ من المشكلة فقط)
- ❌ عدم توثيق السبب الجذري
- ❌ عدم التحقق بعد الإصلاح
