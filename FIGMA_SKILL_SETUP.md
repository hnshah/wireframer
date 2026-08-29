# Figma custom skill setup — Wireframer

Figma Agent and Figma Make support custom Markdown skills. Wireframer is intentionally packaged so the canonical `SKILL.md` can be uploaded directly.

## Install privately

1. Open a Figma Design or Figma Make file where the agent is available.
2. In chat, open **Skills → Add skill**.
3. Choose **Upload a file**.
4. Upload `SKILL.md`.
5. Review the imported name, description, and instructions.
6. Add the skill.
7. Invoke it explicitly with `/wireframer` during testing.

Figma custom skills currently accept a standalone Markdown file rather than the optional `references/`, `scripts/`, or `assets/` directories used by some broader Agent Skills packages. Treat `SKILL.md` as the canonical portable core.

## Test in Figma

Run at least these four cases:

1. **Blank-file product idea** — confirm Wireframer reasons before it creates frames.
2. **Existing design system** — confirm it uses components without allowing component availability to determine product behavior.
3. **Existing workflow redesign** — confirm it preserves the original and creates a separate revised flow.
4. **State-heavy flow** — confirm loading/error/recovery/permission states are considered rather than rendering only the happy path.

## Publish to Figma Community

Once release gates pass:

1. Open **Add context → Skills → Manage skills**.
2. Select Wireframer.
3. Choose **More actions → Publish**.
4. Select **Community**.
5. Supply:
   - name
   - short tagline
   - description
   - category
   - thumbnail
   - optional screenshots / examples
   - support contact
6. Publish.

Recommended Community positioning:

**Name:** Wireframer

**Tagline:** Turn a product idea into a wireframe worth discussing.

**Description:** Wireframer makes the Figma agent reason through the user job, product objects, task flow, interaction model, screen set, important states, and failure recovery before it draws. It then critiques and revises the result. Built for product exploration, workflow redesign, and low-fidelity interaction design.

## Community media

Show the method, not just pretty output.

Recommended carousel:

1. input product idea
2. object model + task flow
3. two materially different interaction models
4. selected wireframe
5. missed-state / critique view
6. revised wireframe

A before/after screenshot without the reasoning layer undersells the skill and makes it look like another UI generator.
