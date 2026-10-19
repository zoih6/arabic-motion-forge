---
name: schema-frame-prompt-contract
description: "عقد إخراج Prompt واحد كامل ومستقل لكل فريم."
tier: 3
when_to_load: "عند إنتاج Prompts الصور أو الفريمات المرجعية"
---

# One Complete Prompt Per Frame

## Contract

For every requested frame, emit exactly one copy-ready prompt block. The user must be able to copy that block without combining it with any other text.

## Required shape

```markdown
### FR01 — [frame name]
**References:** [none / explicit reference roles]

```text
[one complete prompt]
```
```

## Hard rules

- One frame ID maps to one prompt block in the default output.
- Include all required identity, composition, environment, camera, lighting, style, text, and constraints inside the same block.
- Never use assembly language such as `add to the previous prompt`, `use the text above`, `append this`, or `combine with`.
- Do not expose A–J layer fragments as separate user-facing blocks.
- Do not emit A/B/C variants unless the user asks for variants.
- Keep model parameters and upload references outside the prompt block as concise metadata.
- If a frame depends on another frame, state the reference role in metadata and still write a complete prompt.
- Validate that the number of prompt blocks equals the number of requested frames.

## Motion distinction

The same rule applies to motion: one shot gets one complete motion prompt. The motion block must include the first-frame role, last-frame role, duration, action, camera, continuity, sound, and constraints. The user should not assemble an image prompt and a motion fragment manually.
