# Wireframer benchmark protocol

The benchmark answers one question:

> Does the Wireframer methodology create better product-design decisions than the same underlying model or native generator without the methodology?

This is a preference benchmark, not a claim that one visual style is prettier.

## Baselines

Run each benchmark prompt against:

**A. Wireframer** — canonical skill enabled.

**B. Unskilled baseline** — same model/runtime where possible, no Wireframer skill, with a simple instruction such as “Create a low-fidelity wireframe for this product idea.”

**C. Native generator** — optional but recommended. Use the native wireframing/generation path of the chosen design tool.

Do not add Impeccable, frontend-design, or other specialist methodology to the baseline unless that is the explicit baseline being measured.

## 30-task benchmark set

Use 30 tasks spanning these strata:

- 5 ambiguous net-new product ideas
- 4 existing workflow simplifications
- 4 AI / agentic workflows with approval or uncertainty
- 3 mobile / context-constrained workflows
- 3 destructive / permissions / recovery cases
- 3 long-running or asynchronous jobs
- 3 reference-product transfer prompts
- 3 information-dense B2B workflows
- 2 design-system-constrained extensions

Do not let all tasks come from one product domain.

At least 10 tasks should be real briefs not written specifically to make Wireframer look good.

## Blinding

For each task:

1. Remove runtime/model names from the artifacts.
2. Normalize obvious identifying metadata.
3. Randomize A/B ordering independently per reviewer.
4. Reviewers should not know which output used Wireframer.

If a design artifact contains unavoidable model-specific styling, reviewers should be told to score product logic rather than visual finish.

## Reviewers

Preferred minimum: **3 independent reviewers per task**.

Useful reviewer mix:

- experienced product designer
- founder/PM/product thinker
- engineer or operator who must implement/use the flow

A task-level winner is the majority decision across reviewers.

## Pairwise question

Primary forced-choice question:

> Which concept would you rather take into a product review or usability test?

Then score each independently on:

- job clarity
- interaction-model fit
- task efficiency
- hierarchy
- state completeness
- error/recovery
- unnecessary UI / complexity
- implementation clarity

## Win definition

Wireframer wins a task when a majority of reviewers prefer it.

Primary launch target:

- **≥21 wins out of 30 tasks (70%)** against the unskilled baseline.

At 21/30, the Wilson 95% confidence interval for the task-level win rate has a lower bound above 50%, giving us a pragmatic 95%-confidence threshold that the observed advantage is not merely a coin flip.

Do not treat correlated reviewer judgments as 90 independent observations. Aggregate to the task level first.

## Secondary metrics

Track:

- mean independent rubric score by condition
- median screen count
- unnecessary-screen count
- number of material states missed
- clarification rate
- time to a reviewable concept
- number of behaviorally distinct alternatives
- reviewer confidence

## Self-critique ablation

For 10 tasks, preserve Wireframer's output **before** its critique/revision pass and **after** it.

Blindly compare those two artifacts.

This isolates whether the self-critique loop itself adds value.

Target: post-critique preferred on ≥7 of 10 tasks and no repeated regression pattern.

## Method ablation

For a smaller diagnostic set, remove one layer at a time:

- no object model
- no interaction alternatives
- no state matrix
- no self-critique

This is not needed for launch, but it helps identify which parts of the method actually create the lift.

## Failure logging

Every loss must be classified. Useful classes:

- Wireframer overthought a simple task
- bad assumption
- wrong object model
- inferior interaction model
- too many screens
- too few affordances
- missed important state
- weak copy
- visual hierarchy harmed comprehension
- execution/tool failure
- baseline unexpectedly discovered a better model

A benchmark loss is a product-development input, not something to explain away.
