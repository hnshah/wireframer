# Soleio Luck v1.0 assessment — Wireframer

Applied sequentially. A serious failure at any facet is a reason to change the assembly rather than rationalize it.

## 1. Solvency — HIGH

**Question:** Can this sustain its pattern against dissipation?

The portable skill is inexpensive to reproduce and maintain. A public skill can be sustained by actual usage, corrections, examples, community contributions, and reputation/distribution. The Grok Bot is a runnable instance rather than the only place the value lives.

**Risk:** maintenance becomes stylistic churn or depends on one model/vendor.

**Design response:** keep the methodology model- and runtime-portable; promote recurring corrections into evals; minimize dependencies.

## 2. Gradient coupling — VERY HIGH

The assembly couples to several independent active gradients:

- founders/PMs want to make product ideas concrete quickly
- designers need faster exploration and critique
- engineers increasingly prototype before dedicated design work
- AI-agent users need higher-quality product judgment rather than generic UI generation
- design tools are becoming agent-operable
- portable skills are becoming a distribution primitive

**Risk:** "AI wireframes" becomes commodity.

**Design response:** position the durable job as product-design reasoning; treat rendering as replaceable infrastructure.

## 3. Structural compatibility — VERY HIGH

A markdown/YAML skill has low reconstruction cost and snaps into emerging agent skill conventions. Grok supports skill folders and Claude-compatible skills. Grok Bot can expose the same job as a public copyable Bot. Figma is already where many product teams work.

**Risk:** installation friction across runtimes.

**Design response:** ship canonical `SKILL.md`, runnable public Bot, install snippets, examples, and tool-agnostic outputs.

## 4. Niche construction — POTENTIALLY EXCEPTIONAL

This is the facet that determines whether Wireframer becomes more than a useful prompt.

Desired loop:

usage → wireframe → human correction → categorized failure → eval/example → skill improves → more trust/use → more corrections

Additional niche construction:

- users share Bot outputs
- skill references public Bot
- Bot references canonical skill/repo
- design teams contribute patterns/evals
- compatible tools adopt the skill
- adjacent agents (Product Designer, UX Critic) reuse the same design record/rubric

**Risk:** outputs are consumed privately and no learning returns to the system.

**Design response:** make critique records, correction categories, eval contributions, and shareable examples first-class artifacts.

## 5. Circulation — HIGH IF DESIGNED, LOW IF IGNORED

Luck requires return paths. The product must deliberately circulate knowledge.

Target circulation:

skill repo → Grok Bot → user task → artifact → feedback/correction → eval/PR/example → skill update → Bot update → new users

**Bottleneck:** private corrections trapped in individual Bot conversations.

**Design response:** create a lightweight contribution/export path for anonymized eval cases, patterns, and corrections. Publish change logs showing what real usage taught the skill.

## 6. Integration — VERY HIGH

Wireframer can connect currently fragmented systems:

- product thinking
- UX methodology
- design critique
- Figma execution
- agent skill ecosystems
- design systems
- research/evidence
- prototyping/engineering handoff

This integration is more valuable than any single generation feature.

**Risk:** becoming an incoherent mega-skill.

**Design response:** Wireframer remains the orchestrating product-design method; specialist skills stay modular and stage-specific.

## 7. Path sensitivity — EXCEPTIONALLY GOOD, WITH URGENCY

The precursors now exist:

- capable multimodal models
- reusable skill formats
- agents with persistent context/computers
- Figma agent/MCP execution
- public shareable Grok Bots
- widespread dissatisfaction with generic AI-generated UI

The window for generic wireframe generation is already closing because native design products can generate frames themselves. The window for a trusted cross-runtime design method is open now.

**Design response:** ship the method publicly before the category collapses into tool-native generation.

## Verdict

### Is "AI wireframing" a huge standalone opportunity?
Probably not. Rendering will commoditize quickly.

### Is Wireframer a potentially huge wedge?
Yes.

The high-upside assembly is:

**portable product-design method → public runnable Bot → correction/eval network → trusted design reasoning layer → adjacent Product Designer / UX Critic agents**

The strongest moat is not pixels. It is an improving corpus of product decisions, failure modes, interaction patterns, evals, and real-world corrections that can travel across models and design tools.

## Failure-mode watch

- **Flash in the pan:** viral skill, no learning/return loop
- **Premature artifact:** overbuilt platform before enough real tasks
- **Institutional zombie:** skill becomes a frozen checklist while tools/models improve
- **Pooled fortune:** lots of private usage but insights never circulate back
- **Fragmented ecology:** Wireframer, Bot, Figma workflow, critique, and evals evolve separately

## Immediate luck-maximizing moves

1. Ship v0 as a public portable skill.
2. Ship one public Grok Bot using the same canonical method.
3. Put reciprocal links between skill and Bot.
4. Publish 10 evals and invite failure cases, not generic feedback.
5. Capture every correction by failure category.
6. Publish before/after examples showing product-model improvements, not pretty screens.
7. Keep Figma as an execution target, not a dependency.
8. Split adjacent roles only after real usage shows stable boundaries.

---

# Second pass after repo creation — 2026-08-29

The first pass asked whether Wireframer had the right ingredients. The repo now exists, the skill is portable, the eval loop is explicit, and public distribution surfaces are available. The binding constraint has moved.

## Binding constraint now — circulation

The most important failure to prevent is pooled fortune.

A good Wireframer run currently produces a useful conversation and a useful design artifact. Both can terminate inside the runtime that created them. That forces downstream humans and agents to reconstruct the job, object model, interaction choice, state coverage, and corrections.

The new assembly should produce a **portable design record** with every substantive run.

That record becomes the circulatory object connecting:

- the product brief
- Figma
- Grok Bot
- coding agents
- product review
- usability testing
- human corrections
- future Wireframer runs
- the public eval corpus

A wireframe can be replaced by another renderer. A decision record can survive the renderer.

## Structural compatibility move — one-line install

The open Skills CLI discovers a root `SKILL.md`. Wireframer already has the right repository shape.

That makes this possible:

```bash
npx skills add hnshah/wireframer
```

This should become a primary install path for compatible agent runtimes. Figma and Grok Bot remain additional surfaces with their own native setup.

Lower reconstruction cost increases the number of places Wireframer can enter without creating runtime-specific forks.

## Path-sensitivity move — public beta before perfect benchmark

Figma's public skill ecosystem is newly available. Waiting for the full 30-task benchmark before allowing public use would trade away path sensitivity and circulation.

The better sequence is:

1. pass the canonical functional evals
2. clear critical Grok Bot and Figma execution failures
3. publish a clearly labeled public beta
4. invite reproducible failures
5. run consistency, adversarial, and blinded benchmark work while real usage starts
6. call the method v0.1 only after the stronger evidence exists

This keeps rigor without making rigor a reason to miss the early distribution window.

## Niche-construction move — learn from success too

Failure collection is necessary but incomplete.

The more defensible corpus includes decisions that survived product review, usability testing, implementation, or launch. A future product-design intelligence layer should know which interaction choices survived contact with reality, not only which outputs people disliked.

The design record should therefore be able to accumulate outcome links over time.

## Integration move — define the handoff contract early

Wireframer should become easy for adjacent skills and agents to consume.

The design record is that contract.

A future UX Critic can read it before revising an interface. A builder can read it before implementation. A research agent can attach evidence to its assumptions. A design-system adapter can map its screen/state requirements to components without changing the product model.

This creates integration density without turning Wireframer into a mega-skill.

## Solvency move — prevent runtime drift

Figma, Grok Bot, local agent installs, and future marketplaces can each hold a copy of the method. That creates a new dissipation risk.

Every runtime should expose the canonical skill version. Updates should originate in the repository, pass regression tests, then propagate outward. Runtime-specific profiles stay thin.

The design record should also record the skill version and runtime so failures remain reproducible after the method changes.

## New highest-leverage sequence

1. Keep `SKILL.md` canonical.
2. Make the portable design record part of every substantive run.
3. Add the one-line Agent Skills install path.
4. Pass the canonical eval suite in Grok Bot and Figma.
5. Publish both as public beta once critical failures are gone.
6. Capture failures and successful downstream outcomes.
7. Run the deeper benchmark in the open.
8. Promote repeated product mechanics into a shared pattern library only after evidence accumulates.
9. Add adjacent specialist skills only when real corrections reveal stable boundaries.

## Updated verdict

Wireframer should not optimize to become the best wireframe generator.

It should optimize to become the **lowest-cost way for product-design decisions to become explicit, portable, testable, and reusable across agent runtimes**.

That assembly has more viable next steps than a rendering tool and creates the conditions for the broader Product Designer system to emerge from evidence rather than ambition.
