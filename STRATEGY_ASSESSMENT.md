# Wireframer product strategy assessment

## Summary

Wireframer has a strong opportunity as a portable product-design method rather than a wireframe generator tied to one tool.

The durable value is the reasoning layer that helps an agent identify the user job, model the product objects, choose an interaction model, cover consequential states, and critique the result before rendering.

The main strategic risk is commoditization at the rendering layer. Native design tools will continue to get better at generating screens. Wireframer should therefore keep execution replaceable and invest in the method, evals, correction loop, and portable design records.

## Current binding constraint

The biggest constraint is now circulation.

A strong Wireframer run can produce a useful conversation and a useful design artifact, then stop inside the runtime that created them. Downstream humans and agents have to reconstruct the product job, object model, interaction choice, state coverage, and corrections.

The proposed portable design record gives those decisions a reusable handoff format.

## Distribution and compatibility

The repository should remain the canonical source. Figma and Grok Bot are distribution and execution surfaces rather than separate methodologies.

The root `SKILL.md` also supports a simple install path for compatible agent runtimes:

```bash
npx skills add hnshah/wireframer
```

Reducing installation and reconstruction cost increases the number of places Wireframer can be used without creating runtime-specific forks.

## Compounding loop

Desired loop:

```text
usage
  ↓
wireframe + design record
  ↓
human correction or downstream outcome
  ↓
classified failure / survivor
  ↓
eval, example, or method change
  ↓
better Wireframer
```

Failure collection is necessary but incomplete. The stronger corpus also captures product decisions that survived review, usability testing, implementation, or launch.

Useful records include:

- input problem
- constraints and assumptions
- interaction alternatives
- chosen model
- wireframe
- human corrections
- usability result where available
- implementation changes
- eventual shipped choice where known

## Portable design record

The design record should act as the handoff contract between product-design agents and downstream work.

A future UX Critic can read it before revising an interface. A builder can read it before implementation. A research agent can attach evidence to assumptions. A design-system adapter can map screen and state requirements to components without changing the product model.

The record should include the Wireframer version and runtime so failures remain reproducible after the method changes.

## Public beta sequencing

The stronger sequence is:

1. pass the canonical functional evals
2. clear critical Grok Bot and Figma execution failures
3. validate design-record reconstruction and tiny-task overhead
4. publish a clearly labeled public beta
5. invite reproducible failures
6. continue consistency, adversarial, ablation, and blinded benchmark work in public
7. call the method v0.1 only after the stronger evidence exists

This preserves rigor while allowing real usage to improve the method earlier.

## Main failure modes

### Useful but non-compounding
People try Wireframer, get good output, and nothing returns to the method.

### Private learning
Teams make strong corrections in private conversations and those corrections never become evals or examples.

### Runtime drift
Figma, Grok Bot, and other installations quietly evolve into different methodologies.

### Mega-skill expansion
Wireframer absorbs every adjacent design task and becomes harder to invoke, test, and maintain.

### Rendering dependency
The method becomes coupled to one design tool and loses portability as execution technology changes.

## Current strategic moves

1. Keep `SKILL.md` canonical and portable.
2. Make the portable design record part of substantive runs only if reconstruction tests validate it.
3. Add the one-line Agent Skills install path.
4. Pass the canonical eval suite in Grok Bot and Figma.
5. Publish both as public beta once critical failures are gone.
6. Capture failures and successful downstream outcomes.
7. Run the deeper benchmark in the open.
8. Keep rendering replaceable.
9. Add adjacent specialist skills only when real corrections reveal stable boundaries.

## Direction

Wireframer should optimize to become the lowest-cost way for product-design decisions to become explicit, portable, testable, and reusable across agent runtimes.
