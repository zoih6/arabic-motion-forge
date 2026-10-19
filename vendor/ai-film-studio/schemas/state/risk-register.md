# state/risk-register.md

> **سجل المخاطر.** يُحدَّث من قبل `30-executive-producer` و `31-quality-gate-controller`.

```yaml
project:
  id: "[PROJECT_ID]"
  status: "[...]"
  last_updated: "[ISO]"

risks:
  - id: "RISK-01"
    risk: "[...]"
    probability: "[high / medium / low]"
    impact: "[critical / high / medium / low]"
    mitigation: "[...]"
    owner: "[...]"
    status: "[mitigated / open / closed]"
```

راجع `workflows/M9a-executive-producer.md` للقالب الكامل.
