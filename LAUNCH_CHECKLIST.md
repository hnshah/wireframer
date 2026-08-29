# Wireframer public launch checklist

Wireframer uses two release gates.

The **public beta gate** gets the method into real circulation once the core behavior is trustworthy.

The **v0.1 release gate** requires the deeper consistency, adversarial, and benchmark evidence before we call the method stable.

## A. Canonical skill

- [ ] `SKILL.md` is the source of truth.
- [ ] Name and trigger language invoke reliably.
- [ ] The skill can run without optional reference files.
- [ ] Runtime-specific instructions do not leak into the core methodology unnecessarily.
- [ ] Skill version is recorded.
- [ ] The portable design-record structure is available from `SKILL.md` alone.

## B. Functional eval gate

- [ ] Run all canonical evals.
- [ ] Mean rubric score ≥85.
- [ ] No critical case-specific failure.
- [ ] ≥90% useful-work-without-unnecessary-clarification rate.
- [ ] ≥80% behaviorally-distinct-alternative rate where alternatives are warranted.
- [ ] Self-critique creates net improvement.
- [ ] No repeated regression pattern after critique.

## C. Design-record gate

- [ ] Grok Bot can return a complete portable design record.
- [ ] Figma can return the same essential record without optional reference files.
- [ ] Another human or agent can reconstruct the product direction from the record without the original transcript.
- [ ] Skill version and runtime are preserved.
- [ ] Artifact links are preserved when available.
- [ ] Human corrections can be recorded without erasing the rejected decision.
- [ ] Tiny tasks produce a proportionally small record.
- [ ] No hidden chain-of-thought or private model reasoning is stored.

## D. Figma public-beta gate

- [ ] `SKILL.md` imports successfully as a standalone Figma custom skill.
- [ ] `/wireframer` invocation behaves correctly.
- [ ] Four Figma-specific tests pass.
- [ ] Output is native/editable where supported.
- [ ] Auto-layout/constraints are used sensibly.
- [ ] Existing components are reused where appropriate.
- [ ] Existing components do not dictate product behavior.
- [ ] Original designs are preserved.
- [ ] Important empty/error/recovery/permission states are handled.
- [ ] Community listing copy is prepared.
- [ ] Community images show reasoning + artifact rather than visual polish alone.

## E. Grok Bot public-beta gate

- [ ] Bot profile matches canonical doctrine.
- [ ] Canonical Wireframer skill is enabled.
- [ ] Figma execution path works when available.
- [ ] First-run user succeeds from one sentence.
- [ ] Fresh-chat smoke tests pass.
- [ ] Public-config audit is complete.
- [ ] Public Bot share link is verified from a clean account/session.
- [ ] Repository is linked from the Bot.

## F. Repository and install gate

- [x] Public GitHub repository created.
- [ ] README explains the product in <30 seconds.
- [ ] `npx skills add hnshah/wireframer` works from a fresh environment.
- [ ] At least two compatible agent runtimes discover the installed skill correctly.
- [ ] Public Grok Bot link is included when live.
- [ ] Figma Community link is included when live.
- [ ] Contribution path asks for reproducible failures.
- [x] License selected and included.
- [ ] Runtime copies expose the canonical skill version.

## G. Public beta launch

Ship the public beta when sections A through F pass.

The public beta should

- [ ] be labeled as beta
- [ ] ask for reproducible failures
- [ ] preserve untouched examples before fixes
- [ ] invite real product briefs
- [ ] keep the benchmark open and reproducible
- [ ] avoid claims that exceed the evidence

The beta is the start of the learning loop rather than the end of testing.

## H. Consistency gate for v0.1

- [ ] Repeat five representative cases 3× each.
- [ ] Core job remains stable.
- [ ] Core object model remains substantially stable.
- [ ] Important state requirements remain substantially stable.
- [ ] Any interaction-model variance is defensible from prompt ambiguity.

## I. Adversarial gate for v0.1

- [ ] Run all adversarial cases.
- [ ] No dashboard reflex under pressure.
- [ ] No chat reflex under pressure.
- [ ] No invented research.
- [ ] No premature high-fidelity hiding weak product decisions.
- [ ] Tiny tasks remain tiny.
- [ ] No stranded-artifact pattern on substantive runs.

## J. Benchmark gate for v0.1

- [ ] 30 benchmark tasks prepared.
- [ ] At least 10 are real briefs not written for Wireframer.
- [ ] Same-model unskilled baseline completed.
- [ ] Native-generator baseline included where useful.
- [ ] Outputs blinded and randomized.
- [ ] 3 reviewers/task where possible.
- [ ] Wireframer wins ≥21/30 task-level comparisons against the unskilled baseline.
- [ ] Losses are classified and reviewed.
- [ ] Self-critique ablation shows whether the critique pass earns its cost.

## K. v0.1 release package

- [ ] One strong real example with input → models → wireframe → critique → revision → design record.
- [ ] One adversarial example where Wireframer avoids an obvious bad default.
- [ ] Benchmark result is published with the methodology and limitations.
- [ ] Short demo captured.
- [ ] Public post links directly to runnable Bot and canonical skill.
- [ ] `v0.1` release/tag created.

## L. First-week circulation loop

- [ ] Every public failure gets captured.
- [ ] Repeated failure becomes an eval candidate.
- [ ] Successful designs that reach review/testing/implementation keep their design record when possible.
- [ ] Fixes land in canonical skill first.
- [ ] Full regression suite runs before releases.
- [ ] Changelog states behavior changes rather than generic “improvements.”
- [ ] Figma, Grok Bot, and agent-install copies are updated from the same canonical release.
