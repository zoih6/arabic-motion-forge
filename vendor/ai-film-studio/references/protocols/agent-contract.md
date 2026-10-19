# Agent Contract — v1.1

كل وكيل هو وحدة قابلة للتتبع، وليس مجرد Prompt.

## العقد الموحد
```yaml
agent_id: AGENT-XX
run_id: RUN-YYYYMMDD-###
input_artifacts:
  - id: ...
    version: ...
    status: APPROVED
task: ...
output_artifacts:
  - id: ...
    version: ...
    status: DRAFT|APPROVED|HOLD|FAIL
validation:
  - check: ...
    result: PASS|FAIL
state_updates:
  - field: ...
    value: ...
gate: PASS|FAIL|REQUIRES_REVIEW
next_agent: AGENT-XX
repair_if_failed:
  diagnosis: ...
  variable_to_change: ...
```

## قواعد
- لا تستخدم Artifact ID غير موجود.
- لا تجعل Version يتغير دون سبب مسجل.
- لا تستبدل أصلًا معتمدًا؛ أنشئ Version جديدًا.
- كل فشل يجب أن يحدد **سببًا قابلًا للاختبار** ومتغير الإصلاح.
- إذا لم يكن هناك تغيير في الحالة، اذكر `STATE_UPDATE: none`.
