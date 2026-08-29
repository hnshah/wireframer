# Wireframer design record

The design record is the portable handoff object produced by Wireframer.

A wireframe shows a product direction. The design record preserves the decisions that made the wireframe useful enough to discuss, test, revise, implement, or hand to another agent.

Keep it concise. Preserve decisions and evidence without exposing private chain-of-thought.

## Why this exists

A Figma frame can become stranded inside Figma. A Bot conversation can become stranded inside the Bot. A design record gives the work a low-cost way to circulate between humans, design tools, coding agents, research, and future Wireframer runs.

The record should be useful even when the rendering tool changes.

## File format

Use Markdown with this frontmatter when the runtime can create files.

```yaml
---
wireframer_record_version: "0.1"
wireframer_skill_version: "0.2-lc"
runtime: "figma | grok-bot | grok-build | claude | codex | other"
status: "draft | reviewed | tested | shipped"
source: "short description or source link"
artifact: "Figma/file/prototype link when available"
---
```

When file creation is unavailable, return the same structure inline.

## Required sections

### Product interpretation

Record only the product context that changes the design.

- primary user
- trigger or context
- primary job
- desired outcome
- important constraints
- evidence supplied
- consequential assumptions

Separate supplied evidence from assumptions.

### Object model

For each durable product object, record its purpose, important relationships, and consequential lifecycle states.

Do not turn every UI element into an object.

### Task flow

Record the shortest useful path from trigger to outcome. Include consequential branches, approvals, interruptions, and recovery paths.

### Interaction alternatives

Include this section only when more than one model was credible.

For each materially different model, capture the central behavior, its best-fit condition, and its main risk.

### Decision

Record the chosen interaction model and a compact rationale grounded in the job, evidence, constraints, and tradeoffs.

List rejected alternatives only when remembering the rejection will prevent future rework.

### Screen map

For each required screen or surface, record its purpose and primary action. Avoid component inventories.

### State coverage

Record consequential non-happy-path states. Explicitly note important states that were considered and intentionally omitted from the drawn wireframes.

### Critique

Record the rubric score before revision when available, the highest-impact issues found, the changes made, and the score after revision.

Do not use the score as a substitute for the critique.

### Questions worth testing

Record questions that could change the product direction. Keep blockers separate from research questions.

## Human correction record

When a human materially rejects or changes a product decision, preserve the correction instead of silently replacing the prior decision.

Append:

```markdown
## Correction

- Date
- Runtime
- Skill version
- Failure category
- Original decision
- Human correction
- Why the correction changes the product
- Eval candidate: yes / no
```

A repeated correction should become an eval candidate.

## Reconstruction test

A design record is good when another competent human or agent can understand the product direction without needing the original chat transcript.

The record should answer:

1. What job is being designed?
2. What are the important product objects?
3. What interaction model was chosen?
4. What alternatives mattered?
5. What screens and states are required?
6. What assumptions could invalidate the direction?
7. What changed during critique or human correction?

If the record cannot answer those questions, it is not yet a portable handoff.

## What not to store

Do not preserve private model reasoning, hidden chain-of-thought, secrets, credentials, unrelated personal information, or decorative implementation details that do not affect the product decision.

The record exists to circulate useful product decisions.