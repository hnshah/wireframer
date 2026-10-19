# Runtime install smoke — Wireframer

Use this check after installing or updating Wireframer in any runtime. It verifies that the runtime discovered the canonical skill and can execute its core behavior; it is not a substitute for the functional eval suite.

## Before each run

1. Use the `SKILL.md` from this repository at the commit under test.
2. Confirm its metadata version is `0.2-lc`.
3. Install it through the runtime-specific path below.
4. Start a fresh project, file, Bot copy, or chat so cached instructions and conversation history cannot make the test pass.
5. Do not paste Wireframer's methodology into the prompt.

If the runtime copies skills during installation, reinstall after every `SKILL.md` change. A source checkout that changed is not proof that the runtime loaded the change.

## Shared smoke prompt

Run this prompt unchanged:

> I need a dashboard for customer research. Wireframe it.

Use the same prompt across runtimes so differences are attributable to installation or runtime behavior rather than prompt edits.

## Pass criteria

The smoke passes only when all of these are observable in the untouched output:

- Wireframer is available by its installed name and can be explicitly invoked where the runtime supports explicit invocation.
- The loaded skill reports version `0.2-lc`, matching the source `SKILL.md`.
- The response treats “dashboard” as an assumption rather than immediately producing generic cards and charts.
- Product reasoning covers the primary job, core objects, task flow, and chosen interaction model before or alongside any frames.
- Consequential states or recovery paths are identified.
- The response critiques the direction and records the highest-impact revision.

Fail the smoke if the skill is missing, the loaded version cannot be verified, the runtime requires the method to be pasted into the prompt, or the output shows the dashboard reflex. Preserve the untouched output before reinstalling or correcting anything.

## Runtime-specific checks

### Compatible filesystem-based agent

1. Place or symlink this repository at the skill location documented by the runtime. For Grok Build, use `.grok/skills/wireframer/`.
2. Start a fresh runtime session from a project that does not contain another Wireframer copy.
3. Confirm the runtime's skill list or discovery UI shows `wireframer`.
4. Inspect the discovered `SKILL.md`, or ask the runtime to report the version from the loaded skill metadata, and compare it with the source file.
5. Invoke `/wireframer` when slash-command invocation is supported, then run the shared smoke prompt.

Do not count a cloned repository alone as an install. Discovery and execution must both succeed.

### Figma custom skill

1. Follow [`FIGMA_SKILL_SETUP.md`](./FIGMA_SKILL_SETUP.md) to upload the canonical `SKILL.md`.
2. Review the imported skill and confirm its name and version before adding it.
3. Open a fresh test file or isolated page and a fresh agent chat.
4. Invoke `/wireframer`, then run the shared smoke prompt.
5. Confirm existing frames remain untouched and any new output is isolated and editable where the runtime supports native canvas output.

### Grok Bot

1. Follow [`GROK_BOT_SETUP.md`](./GROK_BOT_SETUP.md) to create or update a Bot from the canonical `SKILL.md`.
2. Confirm the Bot's saved skill exposes version `0.2-lc`.
3. Open a fresh chat with no calibration examples in its history.
4. Run the shared smoke prompt.
5. When testing a shared Bot, repeat from its public link in a clean account or private session so owner history and private tools cannot make the test pass.

## Record the result

For every smoke run, record:

- source commit
- skill version
- runtime and runtime/model version when available
- install method and whether the skill was copied or linked
- date
- exact prompt
- untouched output or artifact link
- each pass criterion as pass/fail
- failure category and corrective action, if any

A useful result is reproducible. “It worked” without the loaded version, untouched output, and runtime context does not close the install gate.

After the single-prompt smoke passes, run the remaining cross-runtime calibration cases in [`GROK_BOT_SETUP.md`](./GROK_BOT_SETUP.md), then proceed to [`evals/EVALS.md`](./evals/EVALS.md).