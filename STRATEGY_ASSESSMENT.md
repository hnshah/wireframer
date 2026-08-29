# Wireframer product strategy assessment

## Summary

Wireframer has a strong opportunity as a portable product-design method rather than a wireframe generator tied to one tool.

The durable value is the reasoning layer that helps an agent identify the user job, model the product objects, choose an interaction model, cover consequential states, and critique the result before rendering.

The main strategic risk is commoditization at the rendering layer. Native design tools will continue to get better at generating screens. Wireframer should therefore keep execution replaceable and invest in the method, evals, correction loop, and portable design records.

## Sustainability

A Markdown skill is inexpensive to reproduce and maintain. The canonical repository can stay small while real usage supplies corrections, examples, evals, and evidence.

Risks include stylistic churn, dependence on one model or vendor, and methodology changes that are not backed by failures.

Current response:

- keep one canonical `SKILL.md`
- version the method
- turn repeated corrections into evals
- keep runtime-specific instructions thin

## Active demand

Wireframer connects to several active needs:

- founders and PMs need to make product ideas concrete quickly
- designers need faster exploration and critique
- engineers increasingly prototype before dedicated design work
- AI-agent workflows create unfamiliar interaction problems
- design tools are becoming directly operable by agents
- reusable agent skills are becoming a distribution primitive

The opportunity weakens if Wireframer is positioned as generic AI wireframe generation. It strengthens when the job is product-design reasoning that can travel across tools.

## Compatibility and distribution

The skill format has low adoption cost and can be used across multiple agent environments. Figma gives the method a native design surface. Grok Bot gives it a persistent, shareable runtime. GitHub provides a canonical source and contribution surface.

The product should reduce reconstruction cost wherever possible:

- root-level `SKILL.md`
- simple install paths
- public runnable Bot
- Figma skill
- examples and evals
- portable design records

## Compounding loop

Wireframer becomes more valuable when use creates material that improves later use.

Desired loop:

```text
usage
  ↓
wireframe + design record
  ↓
human correction or outcome
  ↓
classified failure / survivor
  ↓
eval, example, or method change
  ↓
better Wireframer
```

The strongest long-term asset is a corpus of product decisions rather than a gallery of screenshots.

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

## Circulation

This is currently the most important strategic constraint.

A useful product decision can easily get trapped inside a Figma file or agent conversation. That produces local value without improving the wider system.

The portable design record is intended to keep decisions moving between people, agents, design tools, implementation, testing, and future runs.

Failures should return through reproducible issues and evals. Successful decisions should also return when there is evidence that a model survived product review, testing, implementation, or real use.

## Integration

Wireframer can connect product thinking, UX critique, Figma execution, design systems, research, implementation, and evaluation without trying to perform every specialist job itself.

The core method should stay narrow. Specialist skills can compose around it for accessibility, high-fidelity design, design-system adaptation, research, and implementation.

A shared design record can become the handoff contract between those roles.

## Timing

The necessary building blocks now exist:

- capable multimodal models
- portable skill formats
- persistent agent runtimes
- agent-operable design tools
- public Bot distribution
- growing dissatisfaction with generic generated UI

Generic wireframe generation is likely to become a native feature everywhere. A trusted cross-runtime product-design method has a more durable opening.

This argues for shipping a public beta once the canonical functional gates pass, then using real public usage to strengthen consistency tests, adversarial evals, and the deeper benchmark.

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
2. Ship a public Grok Bot using the same method.
3. Publish the Figma skill when the functional gates pass.
4. Use reciprocal links between the repo and runnable surfaces.
5. Make the portable design record part of substantive runs if reconstruction tests validate it.
6. Invite reproducible failures rather than generic feedback.
7. Track successful product decisions as well as failures when outcomes are available.
8. Run the deeper benchmark in public after the beta gate rather than delaying all circulation until the benchmark is complete.
9. Keep rendering replaceable.
10. Split adjacent specialist skills only after real usage reveals stable boundaries.
