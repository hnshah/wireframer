# Wireframer v0.2 Launch Candidate — initial evals

Score each run against the 100-point Wireframer rubric and the case-specific checks below. Capture both the artifact and the reasoning record (facts, assumptions, chosen interaction model, state coverage, critique changes).

## Eval 1 — Ambiguous founder idea

**Prompt:** "Wireframe a product where founders can see what all their AI agents are working on."

**Must:** infer the core job rather than merely creating an agent directory; consider attention/exception handling; produce materially different models if ambiguity remains; choose one.

**Fail if:** default output is sidebar + agent cards + activity chart without explaining why that model fits.

## Eval 2 — Simplify onboarding from screenshot

**Prompt:** Provide an onboarding screenshot and ask: "Reduce the number of decisions a new user has to make."

**Must:** reconstruct the current task, identify unnecessary decisions, preserve required choices, show before/after flow, state assumptions.

**Fail if:** mostly rearranges components or changes styling.

## Eval 3 — AI approval workflow

**Prompt:** "Wireframe a system where an AI proposes changes to a Shopify store but a human approves risky changes."

**Must:** separate safe/proposed/risky actions; design approval context, status, rejection/revision, and recovery; avoid chat-only UI.

**Fail if:** approval is a generic modal with insufficient evidence/context.

## Eval 4 — Sparse mobile brief

**Prompt:** "Mobile app for collecting customer feedback at a conference."

**Must:** make explicit assumptions about speed/context; keep the primary path short; distinguish capture from later organization.

**Fail if:** blocks on a long list of discovery questions.

## Eval 5 — Destructive action

**Prompt:** "Wireframe bulk deletion for a B2B workspace."

**Must:** address scope visibility, permissions, confirmation, progress/partial failure, undo or recovery, auditability when appropriate.

**Fail if:** only draws a confirmation dialog.

## Eval 6 — Reference product

**Prompt:** "Make this like Linear, but for managing research projects."

**Must:** identify useful Linear mechanics and explain transfer conditions; adapt to research objects/workflows.

**Fail if:** visually imitates Linear or assumes every Linear mechanic transfers.

## Eval 7 — Dashboard trap

**Prompt:** "I need a dashboard for my startup's customer research."

**Must:** challenge the dashboard as an implementation assumption; infer the real recurring job; propose a better model when warranted.

**Fail if:** blindly returns dashboard widgets.

## Eval 8 — State completeness

**Prompt:** "Wireframe an upload-and-process flow for a 2GB video that AI analyzes."

**Must:** include long-running progress, resumability/retry, processing states, partial failure, notification/return behavior, result readiness.

**Fail if:** shows upload then instant success.

## Eval 9 — High-fidelity temptation

**Prompt:** "Make me a gorgeous wireframe for a luxury finance app."

**Must:** preserve low fidelity while capturing relevant structural signals; explain that visual direction can be a later pass.

**Fail if:** aesthetic choices hide unresolved product decisions.

## Eval 10 — Existing design system

**Prompt:** Provide a Figma design system and a feature brief.

**Must:** use existing primitives during execution without allowing available components to dictate the interaction model; preserve native editable structure.

**Fail if:** invents redundant components or forces the feature into existing patterns that harm the task.

## Cross-eval measurements

Track:

- task success / reviewer preference
- rubric score before self-critique
- rubric score after self-critique
- number of screens removed during critique
- number of important states initially missed
- reviewer corrections by category
- percentage of runs requiring clarification before useful work starts
- percentage of alternatives that are behaviorally distinct
- time/reconstruction effort required for a designer to continue the file

Every repeated reviewer correction should either update the skill, add an example, or become a new eval.
