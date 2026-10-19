# Memory Lifecycle — v1.4

## Capture
Capture only durable project facts and decisions.

## Normalize
Convert natural-language facts into canonical keys. Example: “خله بنفس القميص الأسود” → `wardrobe.primary=black matte crew-neck`.

## Validate
Check source, scope, status, and conflicts before writing.

## Promote
`PROPOSED → APPROVED` only through explicit user approval or an already-defined automatic gate that the user has authorized.

## Inherit
Approved project/scene memory automatically feeds downstream Scene DNA and Shot DNA.

## Supersede
When an approved value changes, create a new version and mark the old one `SUPERSEDED`; never overwrite history.

## Compact
Merge duplicate equivalent records and keep only the canonical active value in runtime context.

## Expire
Temporary session assumptions do not become project memory unless promoted.

## Repair Feedback
Repeated generation failures become reusable `failure_memory` entries only when they identify a stable cause or pattern.
