# Project Memory — AI Film Studio v1.4

## Purpose
Project Memory is the persistent source of truth for an ongoing film project. It stores approved facts, decisions, constraints, relationships, failures, and current production state so a new session can continue without reconstructing the project from chat history.

## Memory Hierarchy
```text
PROJECT MEMORY
├── Project Identity
├── Creative Locks
├── Character Memory
├── World Memory
├── Style Memory
├── Scene Memory
├── Shot Memory
├── Asset Memory
├── Audio / Dialogue Memory
├── Decision Memory
├── Approval Memory
├── Failure / Repair Memory
└── Session Continuation
```

## Source-of-Truth Order
```text
explicit user constraint
> latest approved project memory
> approved scene/shot state
> latest approved asset version
> specialist guidance
> default studio choice
```

## Memory Status
Every durable fact has one status:
- `PROPOSED` — generated but not approved.
- `APPROVED` — authoritative for downstream work.
- `SUPERSEDED` — retained for lineage but no longer authoritative.
- `REJECTED` — must not be reused unless explicitly restored.
- `INFERRED` — safe working assumption; never silently promoted to APPROVED.

## Write Policy
Write to memory only when a fact is:
1. explicitly supplied by the user,
2. explicitly approved by the user, or
3. a durable production decision that must remain consistent across later shots.
Do not store transient prose, brainstorming noise, or every generated prompt.

## Read Policy
On continuation, retrieve only memory relevant to the requested operation. Do not dump the entire project memory into context.

## Conflict Resolution
When two memories conflict:
1. explicit current user instruction wins for the current task;
2. otherwise latest approved version wins;
3. otherwise ask only if the conflict can materially damage output;
4. never merge contradictory values into a new guess.

## Memory Compaction
Repeated facts are normalized into one canonical record. Old versions remain in lineage but are not injected into active context unless needed for repair or audit.
