# Wireframer roadmap

The first product is deliberately narrow: product-design reasoning whose primary artifact is a wireframe.

## v0.x — Make Wireframer reliable

Focus:

- stronger object modeling
- interaction-model selection
- state completeness
- fewer unnecessary screens
- reliable Figma execution
- cross-runtime parity
- benchmark advantage over unskilled/native baselines

Do not broaden until the core loop wins.

## v1 — UX Critic

Input: existing screenshot, product flow, or Figma selection.

Output:

- reconstructed job and interaction model
- prioritized product/UX failures
- alternative model when necessary
- revised low-fidelity wireframe
- before/after rationale

Why it matters: existing artifacts provide a concrete comparison point and create high-quality correction data.

## v2 — Product Designer

Input: product problem or opportunity.

Output:

- evidence / assumption map
- product-object model
- 2–3 genuinely different interaction models
- wireframes / prototypes
- evaluation plan
- recommended direction

The transition from Wireframer to Product Designer should happen only when the skill demonstrates reliable decision quality beyond layout.

## Potential specialist skills

- `wireframer` — product idea → interaction model → low-fi artifact
- `ux-critic` — existing interface → diagnosis → revised model
- `interaction-modeler` — product problem → competing behavioral models
- `state-designer` — happy path → complete asynchronous/error/permission/recovery system
- `product-mechanics` — retrieve and adapt reusable interaction mechanics
- `design-system-adapter` — product model → native system primitives without component prison

Prefer composable specialist skills over one giant product-design prompt.

## Compounding asset

The long-term asset should be a corpus of **product decisions**, not screenshots.

Capture:

- input problem
- context / constraints
- chosen interaction model
- alternatives rejected
- wireframe
- reviewer correction
- test result where available
- failure category
- eventual shipped choice where known

Over time this can answer questions such as:

- Which interaction models work for exception-heavy agent workflows?
- When does an inbox beat a dashboard?
- When does conversational control become inferior to structured controls?
- Which approval patterns preserve autonomy without overwhelming the operator?
- Which states are routinely missed by generic generators?

That corpus can become more defensible than the public skill itself.
