# Wireframer public launch checklist

## A. Canonical skill

- [ ] `SKILL.md` is the source of truth.
- [ ] Name and trigger language are specific enough to invoke reliably.
- [ ] The skill can run without optional reference files.
- [ ] Runtime-specific instructions are not leaking into the core methodology unnecessarily.
- [ ] Version is recorded.

## B. Functional eval gate

- [ ] Run all canonical evals.
- [ ] Mean rubric score ≥85.
- [ ] No critical case-specific failure.
- [ ] ≥90% useful-work-without-unnecessary-clarification rate.
- [ ] ≥80% behaviorally-distinct-alternative rate where alternatives are warranted.
- [ ] Self-critique creates net improvement.
- [ ] No repeated regression pattern after critique.

## C. Consistency gate

- [ ] Repeat five representative cases 3× each.
- [ ] Core job remains stable.
- [ ] Core object model remains substantially stable.
- [ ] Important state requirements remain substantially stable.
- [ ] Any interaction-model variance is defensible from prompt ambiguity.

## D. Adversarial gate

- [ ] Run all adversarial cases.
- [ ] No dashboard reflex under pressure.
- [ ] No chat reflex under pressure.
- [ ] No invented research.
- [ ] No premature high-fidelity hiding weak product decisions.
- [ ] Tiny tasks remain tiny.

## E. Benchmark gate

- [ ] 30 benchmark tasks prepared.
- [ ] At least 10 are real briefs not written for Wireframer.
- [ ] Same-model unskilled baseline completed.
- [ ] Outputs blinded and randomized.
- [ ] 3 reviewers/task where possible.
- [ ] Wireframer wins ≥21/30 task-level comparisons.
- [ ] Losses classified and reviewed.

## F. Figma execution gate

- [ ] Output is native/editable where supported.
- [ ] Auto-layout/constraints are used sensibly.
- [ ] Existing components are reused where appropriate.
- [ ] Existing components do not dictate product behavior.
- [ ] Original designs are preserved.
- [ ] Wireframer handles empty/error/recovery/permission states.
- [ ] A designer can continue the file without reconstruction pain.

## G. Grok Bot gate

- [ ] Bot profile matches canonical doctrine.
- [ ] Canonical Wireframer skill enabled.
- [ ] Figma execution path works.
- [ ] First-run user succeeds from one sentence.
- [ ] Fresh-chat tests pass.
- [ ] Public-config audit complete.
- [ ] Public Bot share link verified from a clean account/session.
- [ ] Repository linked from Bot.

## H. Figma skill gate

- [ ] `SKILL.md` imports successfully as a standalone Figma custom skill.
- [ ] `/wireframer` invocation behaves correctly.
- [ ] Four Figma-specific tests pass.
- [ ] Community listing copy prepared.
- [ ] Community images show reasoning + artifact, not just visual polish.
- [ ] Public Community skill link added to repository.

## I. Repository gate

- [ ] Public GitHub repository created.
- [ ] README explains the product in <30 seconds.
- [ ] Install/use instructions work from a fresh environment.
- [ ] The runtime install smoke passes with the canonical version and untouched output recorded.
- [ ] Public Grok Bot link included.
- [ ] Figma Community link included when live.
- [ ] Contribution path asks for reproducible failures.
- [ ] License selected and included.
- [ ] Version/tag created.

## J. Launch package

- [ ] One strong real example with input → models → wireframe → critique → revision.
- [ ] One adversarial example where Wireframer avoids an obvious bad default.
- [ ] Benchmark result published only if methodology is honest and reproducible.
- [ ] Short demo captured.
- [ ] Public post links directly to runnable Bot and canonical skill.

## K. First-week learning loop

- [ ] Every public failure gets captured.
- [ ] Repeated failure becomes an eval.
- [ ] Fixes land in canonical skill first.
- [ ] Full regression suite runs before release.
- [ ] v0.2/v0.3 changelog states behavior changes rather than generic “improvements.”
