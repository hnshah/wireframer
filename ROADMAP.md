# Wireframer roadmap

The first product is deliberately narrow. Wireframer makes product-design decisions explicit and renders them as low-fidelity wireframes.

## v0.x — Make Wireframer reliable and portable

Focus

- stronger object modeling
- interaction-model selection
- state completeness
- fewer unnecessary screens
- reliable Figma execution
- cross-runtime parity
- a portable design record
- one-line installation across compatible agent runtimes
- benchmark advantage over unskilled/native baselines

The design record is part of the core loop. A useful product direction should survive outside the chat or design file that created it.

Do not broaden the product role until the core loop wins.

## Public beta — Start circulation early

Once the canonical evals pass and critical Grok Bot/Figma failures are cleared, publish a public beta.

Use the beta to collect

- reproducible failures
- real product briefs
- cross-runtime inconsistencies
- design records that reached product review
- downstream outcomes from testing and implementation

Run the deeper consistency, adversarial, and blinded benchmark work while the beta is in circulation.

## v0.1 — Prove the method

Call the method v0.1 only after

- repeated runs preserve the core product logic
- adversarial prompts do not collapse the method into familiar AI defaults
- self-critique earns its execution cost
- the blinded benchmark clears the defined win threshold
- the portable design record reconstructs the direction reliably

## v1 — UX Critic

Input

- existing screenshot
- product flow
- Figma selection
- existing Wireframer design record when available

Output

- reconstructed job and interaction model
- prioritized product/UX failures
- alternative model when necessary
- revised low-fidelity wireframe
- before/after rationale
- updated design record

Why it matters

Existing artifacts provide a concrete comparison point and create high-quality correction data.

## v2 — Product Designer

Input

- product problem or opportunity
- evidence and constraints
- prior design records when available

Output

- evidence / assumption map
- product-object model
- 2–3 genuinely different interaction models
- wireframes / prototypes
- evaluation plan
- recommended direction
- design record that can move into research or implementation

The transition from Wireframer to Product Designer should happen only when the skill demonstrates reliable decision quality beyond layout.

## Potential specialist skills

- `wireframer` — product idea → interaction model → low-fi artifact + design record
- `ux-critic` — existing interface → diagnosis → revised model
- `interaction-modeler` — product problem → competing behavioral models
- `state-designer` — happy path → complete asynchronous/error/permission/recovery system
- `product-mechanics` — retrieve and adapt reusable interaction mechanics
- `design-system-adapter` — product model → native system primitives without component prison

Prefer composable specialist skills over one giant product-design prompt.

## Shared handoff contract

The design record should become the common object between these skills.

That allows a future workflow such as

```text
product evidence
      ↓
interaction-modeler
      ↓
wireframer
      ↓
design record
   ↙       ↘
UX Critic   builder
   ↓          ↓
updated record
      ↓
research / shipped outcome
```

Each specialist can improve one part without forcing the next stage to reconstruct the whole product decision.

## Compounding asset

The long-term asset should be a corpus of **product decisions**, not screenshots.

Capture

- input problem
- context / constraints
- chosen interaction model
- alternatives rejected
- wireframe
- design record
- reviewer correction
- test result where available
- failure category
- eventual shipped choice where known

Over time this can answer questions such as

- Which interaction models work for exception-heavy agent workflows?
- When does an inbox beat a dashboard?
- When does conversational control become inferior to structured controls?
- Which approval patterns preserve autonomy without overwhelming the operator?
- Which states are routinely missed by generic generators?
- Which decisions survive product review and implementation?

That corpus can become more defensible than the public skill itself.

## Do not build yet

Avoid premature infrastructure for

- a hosted Wireframer platform
- a custom rendering engine
- a giant product-mechanics database
- automated training pipelines
- many adjacent design Bots

Let repeated real-world failures and successful design records reveal which infrastructure deserves to exist.
