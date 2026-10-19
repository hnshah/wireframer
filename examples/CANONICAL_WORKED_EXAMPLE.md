# Canonical worked example — human approval for risky AI changes

This example shows the complete Wireframer method on a canonical eval prompt. It is an authored reference specimen, not a benchmark result or evidence from a live runtime. Use it to judge whether an implementation preserves the method and produces a design record that another designer can continue.

## Input

> Wireframe a system where an AI proposes changes to a Shopify store but a human approves risky changes.

## Design interpretation

A store operator needs to let an AI improve the storefront without reviewing every harmless edit or surrendering control over changes that could affect revenue, trust, or compliance. The product should act as an exception-handling system: low-risk work can proceed under an explicit policy, while risky changes arrive with enough evidence for a person to approve, reject, or request a revision quickly. Success means the operator can understand what will change, why it was flagged, and how to recover if an approved change performs badly.

## Assumptions

Facts supplied by the prompt:

- An AI proposes changes to a Shopify store.
- A person must approve risky changes.

Consequential assumptions made for this example:

- The merchant has already connected a store and defined which changes may publish automatically.
- The AI assigns a risk level, but that classification is visible and contestable rather than treated as certain.
- Price, checkout, policy, navigation, and high-traffic template changes require approval by default.
- The system can preserve a version and roll back every published change.
- One operator may review changes on desktop; team permissions and mobile review are important follow-up questions, not blockers.

## Object model

| Object | Represents | Important attributes | Relationships and actions |
|---|---|---|---|
| Change proposal | One coherent store modification | title, rationale, affected surfaces, risk level, evidence, predicted effect, author, created time | belongs to a run; contains edits; can be approved, rejected, or sent for revision |
| Edit | A before/after modification to one store resource | resource, field, before value, after value, validation status | belongs to a proposal; shown in a diff |
| Risk policy | The merchant's approval boundary | rules, thresholds, protected resources, required role | classifies proposals; can be inspected from a proposal |
| Review decision | A person's disposition of a proposal | decision, reviewer, reason, time | approves, rejects, or requests revision; becomes part of the audit record |
| Release | A published version of approved edits | status, published time, affected resources, rollback point | created from a proposal; can be rolled back |
| AI run | The AI's bounded work session | goal, status, proposals, failures | creates proposals and links related changes |

Lifecycle:

```text
draft → assessed → awaiting approval → approved → publishing → published
                   ↘ rejected
                   ↘ revision requested → revised → awaiting approval
published → rolled back
```

## Task flow

Shortest useful path:

```text
Risky proposal detected
  → operator opens review queue
  → operator inspects impact, risk reason, and before/after diff
  → operator approves
  → system validates and publishes
  → operator sees confirmation and rollback window
```

Important branches:

- Low-risk proposal: publish automatically under policy and add to activity history.
- Insufficient evidence: request an AI revision with a reason; preserve the original proposal.
- Incorrect or unwanted change: reject with an optional reason.
- Permission failure: explain the required role and keep the proposal pending.
- Validation failure after approval: publish nothing, identify failed checks, and return the proposal for revision.
- Partial platform failure: restore the prior version or clearly identify any resources that need recovery.
- Bad outcome after publication: roll back the release and retain the audit trail.

Completion criteria:

- The reviewer knows the scope and consequence before deciding.
- The system records who decided and why.
- Publishing is atomic where possible and recoverable where it is not.

## Interaction alternatives

### A. Approval inbox

- Central model: a queue of proposals that need human judgment.
- Primary action: review the next risky proposal.
- Always visible: pending count, risk, affected surface, age, and current status.
- Deferred: full AI-run history and detailed policy editing.
- Strengths: efficient for recurring review, supports triage, makes stale work visible.
- Risks: can encourage shallow decisions if the detail view lacks evidence.
- Best fit: teams with recurring AI activity and several proposals per week.

### B. Run timeline

- Central model: each AI run is a timeline containing automatic and approval-gated steps.
- Primary action: intervene at a blocked step.
- Always visible: the AI's goal, completed work, current block, and downstream work.
- Deferred: unrelated proposals from other runs.
- Strengths: preserves causal context and helps reviewers understand why a change exists.
- Risks: inefficient when reviewers must triage many runs; urgent approvals can hide in timelines.
- Best fit: complex, infrequent projects where sequence matters more than throughput.

### C. Store-overlay review

- Central model: review risky changes directly on a preview of the storefront.
- Primary action: inspect changed regions and approve in context.
- Always visible: preview, changed regions, and customer-facing effect.
- Deferred: technical metadata and cross-resource dependencies.
- Strengths: concrete and easy to understand for visual content changes.
- Risks: weak for invisible changes such as checkout rules, metadata, or policy logic.
- Best fit: mostly visual merchandising edits.

## Chosen model + rationale

Choose the approval inbox with an evidence-rich detail view. Approval is recurring exception work, so a queue minimizes navigation and makes urgency visible. The detail view borrows the run timeline's causal context and a preview when the change is visual, but neither becomes the primary navigation model. This avoids a generic dashboard and avoids forcing every decision through chat.

## Screen map

| Surface | Purpose | Primary action | Entry | Exit / next state |
|---|---|---|---|---|
| Approval inbox | Triage proposals needing judgment | Open highest-priority proposal | Notification or product navigation | Proposal review |
| Proposal review | Understand scope, evidence, and consequence | Approve, request revision, or reject | Approval inbox | Publishing status or next proposal |
| Publishing status | Show validation and release progress | Continue reviewing other work | Approved proposal | Published confirmation or recoverable failure |
| Release record | Confirm outcome and preserve recovery | Roll back | Publishing status or activity history | Rollback confirmation / restored release |

The product does not need a separate AI-agent directory, analytics dashboard, or chat screen to complete this job.

## Initial wireframes

### 1. Approval inbox

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Store AI                                      3 need review          │
├──────────────┬───────────────────────────────────────────────────────┤
│ Needs review │  Approval queue                         Sort: Risk ▼   │
│ Activity     │                                                       │
│ Policies     │  HIGH  Change checkout free-shipping threshold       │
│              │        Checkout · 12 min ago · Blocks campaign run    │
│              │        AI confidence: 78%                       [→]   │
│              │                                                       │
│              │  HIGH  Rewrite returns policy                        │
│              │        Policy page · 34 min ago                  [→]   │
│              │                                                       │
│              │  MED   Reorder summer collection navigation          │
│              │        Navigation · Yesterday                    [→]   │
└──────────────┴───────────────────────────────────────────────────────┘
```

### 2. Proposal review

```text
┌──────────────────────────────────────────────────────────────────────┐
│ ← Approval queue                 Change checkout shipping threshold  │
├────────────────────────────────────────────┬─────────────────────────┤
│ WHY THIS CHANGE                            │ REVIEW                   │
│ Reduce checkout abandonment during the     │ HIGH RISK                │
│ summer campaign.                           │ Affects checkout totals  │
│                                            │ and margin.               │
│ EVIDENCE                                   │                         │
│ 18% of carts are between $65 and $74.99.   │ Policy rule              │
│ Campaign target: free shipping at $65.     │ Checkout changes require │
│ Source: campaign brief + last 30 days.     │ approval. [View policy]  │
│                                            │                         │
│ PROPOSED EDIT                              │ [Approve and publish]   │
│ Checkout › Shipping threshold              │ [Request revision]      │
│                                            │ [Reject]                │
│ Before                         After        │                         │
│ Free shipping over $75          $65         │                         │
│                                            │                         │
│ ESTIMATED EFFECT                           │                         │
│ +6–9% eligible checkouts; margin impact    │                         │
│ estimated at $1,100–$1,600 for campaign.   │                         │
└────────────────────────────────────────────┴─────────────────────────┘
```

### 3. Publishing status

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Publishing approved change                                          │
├──────────────────────────────────────────────────────────────────────┤
│ ✓ Approval recorded — Maya Chen, 10:42                              │
│ ✓ Checkout configuration validated                                  │
│ ● Publishing to Online Store                                        │
│ ○ Verifying live checkout                                           │
│                                                                      │
│ You can leave this page. We will notify you when verification ends. │
│                                            [Review next proposal]     │
└──────────────────────────────────────────────────────────────────────┘
```

## State coverage

| State | Treatment |
|---|---|
| Empty | “No changes need review” with a link to recent automatic and approved activity. |
| Loading | Preserve queue structure with explicit loading labels; never imply a proposal is safe before evidence loads. |
| Awaiting approval | Show age, risk, affected surface, and whether downstream work is blocked. |
| Stale/conflicting | Stop approval if the store resource changed after the proposal; regenerate the diff. |
| Permission denied | Keep the proposal pending, name the required role, and provide a route to an authorized reviewer. |
| Revision requested | Preserve the original diff, reviewer reason, and a link between proposal versions. |
| Rejected | Record reviewer and reason; do not silently resubmit the same change. |
| Publishing | Show validation and publish steps; allow the reviewer to leave safely. |
| Validation error | Publish nothing; name the failed check and return the proposal for revision. |
| Partial failure | Prefer automatic restoration; otherwise show exactly what changed and the recovery action. |
| Published | Show release time, live verification, audit record, and rollback availability. |
| Rolled back | Show the restored version, reason, initiator, and whether the AI run remains paused. |

Omitted from the drawn frames but not from the design record: empty queue, permission denied, stale proposal, rejection, revision, validation failure, partial failure, and rollback confirmation.

## Critique

### Initial score: 84/100

| Dimension | Score | Finding |
|---|---:|---|
| Job clarity | 14/15 | Approval is clearly framed as exception handling. |
| Interaction model | 14/15 | Queue fits recurring review; embedded run context is still thin. |
| Information architecture | 9/10 | Proposal, policy, decision, and release are coherent. |
| Task efficiency | 9/10 | A reviewer can decide from one detail surface. |
| Hierarchy | 8/10 | Risk is prominent, but approval is visually stronger than consequences. |
| Discoverability | 7/8 | Revision and rejection are available without crowding the queue. |
| State completeness | 7/8 | Important states are recorded; recovery is not yet visible in a frame. |
| Error and recovery | 3/6 | The initial wireframes promise recoverability but do not show its control or boundary. |
| Progressive disclosure | 4/5 | Detail is deferred appropriately. |
| Consistency | 4/5 | Status language is mostly stable. |
| UX copy | 2/3 | “Approve and publish” is concrete, but the decision lacks an explicit consequence summary. |
| Accessibility | 2/3 | Text labels accompany status, but the diff relies partly on columns. |
| Visual restraint | 1/2 | Low fidelity is preserved; no decoration obscures behavior. |

Highest-impact failures:

1. The approval action does not restate scope or recovery, so a consequential click can be too easy to make without noticing the margin impact.
2. The design record describes rollback but the delivered frames do not prove where or how recovery works.
3. The before/after diff needs explicit labels that remain understandable in a linear reading order, not only a two-column visual comparison.

## Revised wireframes

### Revised proposal decision area

The rest of the proposal review remains unchanged. Replace the right-hand decision area with:

```text
┌──────────────────────────────────┐
│ REVIEW                           │
│ HIGH RISK                        │
│ Checkout totals and margin       │
│                                  │
│ This publishes one change:       │
│ Free shipping: $75 → $65         │
│ Estimated campaign cost:         │
│ $1,100–$1,600                    │
│                                  │
│ A release snapshot will be kept  │
│ for rollback.                    │
│                                  │
│ [Approve 1 change and publish]   │
│ [Request revision]               │
│ [Reject]                         │
└──────────────────────────────────┘
```

The diff also gains a linear summary above the columns: “Change free-shipping threshold from $75 to $65.” This survives narrow screens and screen-reader reading order.

### Revised published confirmation

```text
┌──────────────────────────────────────────────────────────────────────┐
│ ✓ Checkout shipping threshold published                             │
├──────────────────────────────────────────────────────────────────────┤
│ Free shipping changed from $75 to $65                               │
│ Approved by Maya Chen · Published 10:44 · Live checkout verified     │
│                                                                      │
│ Rollback available until Jul 31, 11:59 PM                            │
│ [Roll back this release]                    [View audit record]       │
│                                                                      │
│ Rolling back restores the $75 threshold. No other campaign changes  │
│ are affected.                                                       │
│                                            [Review next proposal]     │
└──────────────────────────────────────────────────────────────────────┘
```

### Revised score: 91/100

The revision improves hierarchy, error and recovery, UX copy, accessibility, and state completeness. Remaining uncertainty is mainly empirical: whether reviewers need more source evidence before approving and whether rollback should be time-limited for this class of change.

## Questions worth testing

- Can a store operator correctly explain the scope and margin consequence before approving?
- Does showing the risk-policy reason increase trust or merely add noise?
- Can reviewers distinguish “request revision” from “reject” without training?
- Is a queue still the best model for merchants with fewer than one risky proposal per week?
- Which change types require a rendered storefront preview in addition to a structured diff?
- Should approval require a second reviewer above a configurable financial threshold?
- How long should rollback remain available, and what dependencies can make rollback unsafe?

## What this example demonstrates

- The prompt is interpreted as exception handling, not as a generic dashboard or AI chat.
- Three alternatives differ in behavior, not styling.
- The chosen queue model includes enough evidence for a real decision.
- Risk classification remains inspectable and fallible.
- Failure, stale data, permissions, asynchronous publishing, and recovery are part of the product.
- Critique changes the artifact rather than merely assigning a score.
