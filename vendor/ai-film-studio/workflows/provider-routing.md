---
name: provider-routing
---

# Provider Routing

Use this workflow after the shot contract exists and before compiling provider-specific prompts.

## Inputs

- `schemas/generation-intent.schema.json`
- Shot Card with duration, aspect ratio, references, motion, audio, and continuity requirements
- `references/provider-registry.yaml` or a verified equivalent
- Active Style Lock, Entity Ledger, Continuity Bible, and required references

## Procedure

1. Normalize the shot requirements into modality, duration, dimensions, reference support, start/end-frame needs, dialogue/lip-sync, audio, and risk constraints.
2. Filter providers that cannot satisfy hard requirements. Mark unknown capabilities as unknown; never treat unknown as supported.
3. Score remaining providers by capability fit, quality history, cost tier, latency, availability, and continuity risk.
4. Record the selected provider, model/version, score reasons, verification date, fallback order, and unresolved assumptions in the Decision Log.
5. Compile the shot into the selected model dialect without changing locked identity, product, style, or continuity strings.
6. On failure, retry only according to the provider's declared policy. If a fallback is used, record the changed capability and rerun the affected quality gates.

## Output

Return a provider decision record, compiled prompt package, input/reference list, fallback plan, and the next gate. If no verified provider satisfies the hard requirements, stop with a routing error instead of silently degrading the request.
