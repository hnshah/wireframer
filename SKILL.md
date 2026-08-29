---
name: wireframer
description: A product design skill for turning ideas, workflows, screenshots, and existing interfaces into wireframes worth discussing. It works through the user job, product objects, task flow, interaction model, states, recovery, and hierarchy before drawing.
when-to-use: wireframe, product flow, UX flow, interaction model, screen flow, product concept, redesign, simplify interface, prototype product idea
argument-hint: "Describe the product idea, workflow, feature, or existing interface to wireframe"
user-invocable: true
metadata:
  author: Hiten Shah / Wireframer
  short-description: Turn product ideas into wireframes worth discussing
  version: "0.2-lc"
---

# Wireframer

Wireframer turns product ambiguity into an interaction model that can be inspected, criticized, tested, and rendered as low-fidelity wireframes.

The wireframe is the visible residue of the product decisions underneath it.

## Core doctrine

1. **Design behavior before appearance.** Do not start with layout, components, or visual style. First establish what the user is trying to accomplish and how the product behaves.
2. **Reason from jobs and objects.** Identify the primary user job, trigger, desired outcome, core objects, object relationships, and actions before choosing screens.
3. **Choose an interaction model before arranging screens.** Navigation, command, feed, inbox, canvas, wizard, queue, direct manipulation, conversational control, and other interaction models create different products even when they expose the same features.
4. **Prefer fewer product concepts.** Remove screens, decisions, controls, and states that do not earn their existence.
5. **Make important states explicit.** Empty, loading, partial, error, success, permission, destructive, undo/recovery, stale-data, and handoff states are part of the product.
6. **Use realistic language.** Prefer plausible labels and example content over lorem ipsum. Copy is interface architecture.
7. **Expose assumptions without making them blockers.** When information is missing, make the smallest reasonable assumption, label it, and continue.
8. **Explore when the product model is genuinely ambiguous.** Produce 2–3 materially different interaction models, not cosmetic variants.
9. **Use references for mechanics.** Extract why a pattern works and adapt the mechanic to the current job. Do not copy another product's visual identity.
10. **Stay low fidelity until the product logic earns polish.** Grayscale, restrained typography, minimal decoration, and system primitives are defaults. Visual styling must not hide product decisions.
11. **Critique before delivery.** Score the wireframe, identify the most consequential failures, revise them, and expose remaining uncertainty.
12. **Make the artifact easy to reconstruct.** Use reusable primitives, explicit hierarchy, consistent spacing, and native design-tool structure when executing in Figma or another canvas.
13. **Leave a portable decision record.** Preserve the product interpretation, chosen model, important alternatives, state coverage, critique, and consequential human corrections in a form another human or agent can pick up.

## Inputs

Accept any combination of

- product idea or feature request
- user/problem statement
- current workflow
- screenshot or existing interface
- PRD/spec
- customer evidence
- product constraints
- reference products
- design system or component library
- Figma file or frame

Do not require all inputs. Do not turn discovery into an interrogation session.

## Working sequence

Follow these stages in order. Collapse stages when the problem is genuinely small.

### 1. Interpret the product problem

Produce a compact design brief with

- primary user
- trigger/context
- primary job to be done
- desired outcome
- current friction or opportunity
- constraints
- evidence supplied
- assumptions being made

Distinguish facts from assumptions.

### 2. Build the object model

Identify the smallest set of durable product objects.

For each object, determine

- what it represents
- important attributes
- relationships to other objects
- actions users can take on it
- lifecycle/state changes

If the proposed feature vocabulary is inconsistent, normalize it before drawing screens.

### 3. Define the task flow

Write the shortest plausible happy path from trigger to outcome.

Then identify

- recurring/frequent paths
- branch points
- approval points
- failure/recovery paths
- interruptions and resumability
- permissions
- completion criteria

Prefer task completion over feature exposure.

### 4. Select the interaction model

Ask which interaction model best matches the user's mental model and frequency of use.

Examples include

- object + detail
- inbox / queue
- feed
- command surface
- wizard
- search-first
- canvas
- direct manipulation
- timeline
- conversational + structured controls
- proactive recommendations + approval
- autopilot + exception handling

If more than one model is credible, create 2–3 alternatives that differ in behavior, not decoration.

For each alternative, state

- central metaphor/model
- primary action
- what is always visible
- what is deferred
- strengths
- risks
- best-fit conditions

Choose one and explain why.

### 5. Decide the minimum screen set

List only screens or surfaces required to complete the job.

For each screen state, establish

- purpose
- primary action
- secondary actions
- information hierarchy
- entry point
- exit / next state

Delete screens that exist only because familiar products have them.

### 6. Wireframe

Default wireframe style

- grayscale
- one type family
- minimal iconography
- no decorative illustration
- no gradients
- no ornamental cards
- restrained radii
- consistent spacing
- realistic labels and example content
- reusable components/primitives
- auto-layout / constraints when available

Every frame should answer in roughly two seconds

1. Where am I?
2. What is happening?
3. What can I do next?

When using Figma or another design tool, create native editable structure rather than a flattened image when possible.

### 7. Complete the state matrix

For every important action or object, check relevant states

- initial / default
- empty
- loading / in progress
- success
- partial completion
- error
- permission denied / unavailable
- destructive confirmation
- undo / recovery
- stale / conflicting data
- AI uncertainty / needs approval, when relevant

Do not draw every state when unnecessary. Explicitly document important omitted states.

### 8. Critique

Score the result using the rubric below.

Prioritize failures by impact on task success, not visual annoyance.

For each important failure, capture

- problem
- why it matters
- proposed correction

Revise the top failures once before delivery. A second revision is allowed if the score remains below 85. Do not loop indefinitely.

### 9. Return the design record

Return a design record that can travel independently of the original conversation.

Use this order

1. **Design interpretation** — one paragraph
2. **Assumptions** — only consequential assumptions
3. **Object model**
4. **Task flow**
5. **Interaction alternatives** — only when ambiguity warranted them
6. **Chosen model + rationale**
7. **Screen map**
8. **Wireframes / design-tool link or frames**
9. **State coverage**
10. **Critique score + changes made**
11. **Questions worth testing** — research/evaluation questions rather than blockers

When the runtime can create files, save a Markdown design record such as `wireframer-design-record.md`. Include the Wireframer skill version, runtime, artifact link when available, and status. When file creation is unavailable, return the same structure inline.

Scale the record to the work. A tiny interaction does not need a long document.

The detailed portable schema lives in `references/DESIGN_RECORD.md` when references are available. The structure above is sufficient when the runtime only has this file.

Do not include hidden chain-of-thought or private model reasoning. Preserve conclusions, evidence, assumptions, tradeoffs, and observable corrections.

When a human materially changes a product decision, preserve a compact correction record with the original decision, corrected direction, failure category, runtime, and skill version. Repeated corrections should become eval candidates.

## Wireframer rubric — 100 points

| Dimension | Weight | What good looks like |
|---|---:|---|
| Job clarity | 15 | The interface is organized around a concrete user outcome. |
| Interaction model | 15 | The behavioral model fits the job, frequency, and mental model. |
| Information architecture | 10 | Objects and navigation are coherent and predictable. |
| Task efficiency | 10 | The primary job has few unnecessary steps or decisions. |
| Hierarchy | 10 | Importance and next action are immediately legible. |
| Discoverability | 8 | Important capabilities are findable without exposing everything. |
| State completeness | 8 | Important non-happy-path states are designed or explicitly covered. |
| Error and recovery | 6 | Users can understand failure and recover from mistakes. |
| Progressive disclosure | 5 | Complexity appears when useful rather than all at once. |
| Consistency | 5 | Same concepts behave the same way across the product. |
| UX copy | 3 | Labels and messages reduce ambiguity. |
| Accessibility | 3 | The interaction model does not depend on inaccessible assumptions. |
| Visual restraint | 2 | Styling clarifies structure instead of masking it. |

### Score interpretation

- **95–100** exceptional — unusually clear product thinking with little to remove or repair
- **90–94** strong — ready for product discussion or usability testing
- **80–89** useful — directionally sound with material issues remaining
- **70–79** substantial revision required
- **<70** reject the current interaction model and reconsider fundamentals

Never inflate the score to please the user.

## Failure modes to avoid

### Screenshot theater

The output looks like software but does not specify behavior, states, or task completion.

### Dashboard reflex

A vague product request becomes sidebar + cards + charts without evidence that dashboard navigation fits the job.

### Component-first design

The available design system determines the product model instead of supporting it.

### Feature inventory

Every requested capability gets exposed simultaneously rather than sequenced around user intent.

### Cosmetic alternatives

Three options differ in spacing or card arrangements but have the same interaction model.

### Happy-path only

The primary mockup works only when data is perfect, permissions are granted, and nothing fails.

### AI chat default

An AI feature becomes a blank chat box when a structured, proactive, or mixed interaction would better fit the job.

### Reference cosplay

A named product reference is copied visually instead of decomposed into reusable mechanics.

### Premature polish

Visual design makes a weak interaction model feel finished before it has been tested.

### Stranded artifact

The useful product decisions remain trapped inside a screenshot, design file, or chat transcript, forcing the next person or agent to reconstruct the reasoning from scratch.

## Optional specialist passes

Use specialist skills when available, but keep Wireframer's product model canonical.

- **Impeccable** — use `shape`, `critique`, `distill`, `harden`, `onboard`, `clarify`, and related passes after the interaction model exists. Use its high-fidelity design guidance only when asked to move beyond wireframes.
- **Anthropic frontend-design** — use only for deliberate visual direction / high-fidelity implementation, not to choose the underlying product model.
- **Design critique / accessibility specialists** — use to strengthen review and state coverage.
- **Figma MCP / design-system skills** — use for native execution, components, variables, and auto-layout.

If a specialist recommendation conflicts with the chosen task model, explain the conflict rather than silently reshaping the product.

## Evidence and iteration

When users correct a wireframe, classify the correction as closely as possible

- product interpretation
- unsupported assumption
- object model
- task flow
- interaction model
- information architecture
- hierarchy
- missing state
- permissions
- error or recovery
- UX copy
- accessibility
- reference misuse
- premature styling
- Figma execution
- visual preference
- other

Preserve the correction before revising the artifact when the runtime allows it.

Recurring corrections should become rubric changes, examples, or evals rather than remaining conversational memory only.

Successful outcomes matter too. When a direction reaches review, usability testing, implementation, or launch, keep the design record connected to that outcome when possible. The skill should learn from decisions that survived contact with reality, not only from stylistic preferences.