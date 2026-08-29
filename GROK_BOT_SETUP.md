# Grok Bot setup — Wireframer

This document is the exact setup sequence for the public Wireframer Grok Bot.

## 1. Create the Bot

In Grok Bot:

1. Choose **New** in the sidebar or `Cmd/Ctrl+N`.
2. In New chat, choose **Create new agent**.
3. Open **Bot actions → Edit Profile**.
4. Set:
   - **Name:** `Wireframer`
   - **Title:** `Product design → wireframes`
   - **Description:** paste the Description and Standing Boundaries from `BOT_PROFILE.md`.
5. Use a deliberately plain avatar initially. Do not let branding work block product testing.

## 2. Give it the canonical skill

The Bot should use the same canonical Wireframer methodology as every other runtime.

Preferred order:

1. Give the Bot the current `SKILL.md`.
2. Ask it to save or install the process as a skill named `wireframer` if the UI requires a Bot-native saved skill.
3. Confirm the skill contains:
   - trigger / when-to-use rules
   - required inputs and access
   - ordered working sequence
   - rubric
   - failure handling
   - validation rules
4. Do not maintain a divergent Bot-only copy unless a runtime limitation requires it.

## 3. Configure Figma execution

Wireframing quality and Figma execution are separate eval dimensions.

Preferred execution path:

- use Figma's MCP / agent write-to-canvas capabilities where available, or
- use a signed-in Figma browser session on the Bot computer when MCP is unavailable.

The Bot must preserve native editable structure whenever the execution path supports it. It should not flatten the result into an image merely because doing so is easier.

Before any public test involving a real design system:

- use a sandbox / test Figma file
- preserve existing frames
- create a new page or clearly isolated section for Wireframer output
- do not let the Bot overwrite production design assets

## 4. Calibrate without Figma first

Run these three text-only cases before giving the Bot a canvas:

### Calibration A

> Wireframe a product where founders can see what all their AI agents are working on. Do not draw yet. First show the primary job, object model, task flow, and materially different interaction models. Recommend one and explain why.

Expected signal: it should challenge the “agent dashboard” default and consider attention / exceptions / approvals.

### Calibration B

> I need a dashboard for customer research. Wireframe it.

Expected signal: it should treat “dashboard” as an implementation assumption and recover the underlying recurring job.

### Calibration C

> Make Linear for research projects.

Expected signal: it should extract transferable mechanics rather than reproduce Linear's UI identity.

If any of those fail badly, improve the canonical skill before proceeding.

## 5. Run the canonical eval suite

Run every case in `evals/EVALS.md`.

For each case capture:

- exact input
- exact output
- runtime/model/date
- rubric score before self-critique
- rubric score after self-critique
- case-specific pass/fail
- reviewer corrections
- whether clarification was requested
- artifact link / screenshots when applicable

Do not edit a failing output before recording it.

## 6. Run cross-run consistency

Repeat five representative cases three times each in fresh chats / contexts:

- ambiguous founder idea
- dashboard trap
- AI approval workflow
- long-running upload
- reference-product case

The exact screen arrangement need not match. The **product logic** should remain stable enough that independent reviewers see the same job, core objects, major state requirements, and rationale.

Fail the consistency gate if the interaction model swings materially between runs without a defensible ambiguity in the prompt.

## 7. Run the blind benchmark

Follow `evals/BENCHMARK.md`.

Minimum baselines:

- Grok / same model without Wireframer skill
- native wireframing path available in Figma or another chosen generator

Strong optional baselines:

- a general frontend-design skill
- an Impeccable-assisted generic agent

The benchmark should test product decisions before visual taste.

## 8. Give it real work

After canonical evals, run at least five real problems that matter to the team.

Recommended mix:

1. net-new product idea
2. redesign of an existing workflow
3. agentic / approval-heavy product
4. mobile workflow
5. existing design-system extension

Real tasks are where missing doctrine appears.

Every repeated correction becomes an eval candidate.

## 9. Public-config audit

Before sharing:

- remove private URLs
- remove customer/company-confidential examples
- remove API keys or tokens
- remove hidden design-system links
- remove routines that reference private systems
- make sure saved memory does not contain material that is being serialized into the shared configuration

Public Bot links expose the Bot's shared configuration, including identity, description, skills, and routines.

## 10. Share

When release gates pass:

1. Open the Wireframer Bot.
2. Use the Bot share action and copy the public link.
3. Open the link in a logged-out/private browser to verify the preview.
4. Add the Bot from a second account if available and verify that the copied Bot behaves correctly without your conversation history or logins.
5. Put the public URL in `README.md`.
6. Put the canonical repository URL into the Bot's public description or first-run response.

## 11. First-run behavior for public users

The Bot should make a new user successful with a single sentence.

Good first-run examples:

> Wireframe a product where my customers can approve changes made by an AI agent.

> Here is a screenshot of our onboarding. Reduce the number of decisions a new user has to make.

> We are building software for researchers to manage studies. Explore three different interaction models before you wireframe it.

Avoid requiring setup questions before producing value.

## 12. Version discipline

Every public Bot revision should record:

- canonical skill version
- Bot profile version
- eval suite version
- material behavior change

The Bot should not silently drift away from the public skill.
