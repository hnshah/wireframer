# Wireframer

**Turn a product idea into a wireframe worth discussing.**

Wireframer is a product design skill for turning ideas into wireframes worth discussing.

It works through the user job, product objects, task flow, interaction model, screen set, states, recovery, and hierarchy before drawing. The result stays low fidelity long enough to make product decisions visible.

This repository is the canonical source for the skill, its evals, and the runtime setup for Grok Bot and Figma.

> Current status  
> v0.2 Launch Candidate. We are testing it rigorously before the first public release.

## What Wireframer does

Give Wireframer a product idea, feature request, workflow, screenshot, existing interface, or product spec. It will

1. interpret the user job and constraints
2. identify the core product objects
3. map the shortest useful task flow
4. choose an interaction model
5. explore materially different models when the problem warrants it
6. define the minimum screen set
7. create low-fidelity wireframes
8. cover consequential states and recovery paths
9. critique the result with a 100-point rubric
10. revise the highest-impact failures

The output is meant for product review, design discussion, and usability testing.

## Why this exists

Generating a screen is getting cheap. Product decisions still determine whether the screen helps anyone accomplish the job.

Wireframer makes those decisions explicit enough to inspect and improve. It treats rendering as an execution layer that can change as tools improve.

## Repository map

- [`SKILL.md`](./SKILL.md) contains the canonical portable skill
- [`BOT_PROFILE.md`](./BOT_PROFILE.md) contains the standing profile for the Grok Bot
- [`GROK_BOT_SETUP.md`](./GROK_BOT_SETUP.md) covers Grok Bot setup and sharing
- [`FIGMA_SKILL_SETUP.md`](./FIGMA_SKILL_SETUP.md) covers Figma Agent and Figma Make setup
- [`evals/EVALS.md`](./evals/EVALS.md) contains the canonical functional evals
- [`evals/BENCHMARK.md`](./evals/BENCHMARK.md) defines the blind baseline comparison
- [`evals/ADVERSARIAL.md`](./evals/ADVERSARIAL.md) contains instruction-pressure and anti-pattern tests
- [`LAUNCH_CHECKLIST.md`](./LAUNCH_CHECKLIST.md) defines the public release gates
- [`ROADMAP.md`](./ROADMAP.md) describes the expansion path
- [`references/REFERENCES.md`](./references/REFERENCES.md) records source methodologies and complementary skills

## Product architecture

```text
                  Wireframer
                canonical skill
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Grok Bot   Figma Agent   other agents
          │           │
          └─────┬─────┘
                ▼
           real usage
                ▼
       failures + corrections
                ▼
              evals
                ▼
          better skill
```

The skill stays canonical. Runtime profiles should remain thin. Improvements usually belong in `SKILL.md` and the eval suite before they flow into Grok Bot, Figma, or another agent.

## Install in Grok Build

Grok discovers skills from its configured skill paths. Clone this repository and place or symlink it at

```text
.grok/skills/wireframer/
```

Then invoke

```text
/wireframer <your product idea or design problem>
```

## Use the Grok Bot

Follow [`GROK_BOT_SETUP.md`](./GROK_BOT_SETUP.md).

**Public Grok Bot** `COMING_SOON`

The Grok Bot will use the same canonical Wireframer skill rather than a separate methodology.

## Install in Figma

Figma custom skills accept a Markdown skill file. Upload [`SKILL.md`](./SKILL.md) as the Wireframer skill and follow [`FIGMA_SKILL_SETUP.md`](./FIGMA_SKILL_SETUP.md) for the test sequence.

**Figma Community skill** `COMING_SOON`

## Design principles

Wireframer favors

- behavior before appearance
- jobs and objects before screens
- fewer product concepts
- explicit states and recovery
- realistic interface language
- materially different alternatives
- reusable interaction mechanics
- low fidelity until the product logic holds up
- self-critique before delivery

It actively checks for common failure modes such as dashboard reflex, blank-chat reflex, reference-product cosplay, cosmetic alternatives, happy-path-only flows, and premature visual polish.

## Release standard

The first public release requires

- functional eval mean of at least 85 out of 100
- zero critical failures in the canonical eval set
- useful progress without unnecessary clarification in at least 90 percent of canonical cases
- behaviorally distinct alternatives in at least 80 percent of cases that warrant exploration
- measurable improvement from the self-critique pass
- stable core product logic across repeated runs
- at least 21 wins across 30 task-level blind comparisons against the unskilled baseline
- a clean public Bot configuration with no private data or credentials

The full protocol lives in [`evals/BENCHMARK.md`](./evals/BENCHMARK.md) and [`LAUNCH_CHECKLIST.md`](./LAUNCH_CHECKLIST.md).

## Help improve Wireframer

The most useful contribution is a reproducible failure.

When Wireframer gets a product decision wrong, open an issue with the input, the output, what you expected, and the smallest explanation of what failed. We will try to turn recurring failures into evals before changing the methodology.

Useful failure categories include product interpretation, object model, task flow, interaction model, hierarchy, missing states, permissions, recovery, copy, accessibility, reference misuse, premature styling, and Figma execution.

The goal is to build a growing record of product decisions that improves the skill over time.

## License

MIT
