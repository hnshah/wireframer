# Executable eval contracts

`eval-case.schema.json` is the canonical machine-readable input contract for one Wireframer eval case. It records the case ID and type, title, prompt, required behavior, failure condition, references, and tags.

`eval-result.schema.json` is the canonical machine-readable output contract for one Wireframer eval run. It records the prompt and runtime, artifact locations, weighted rubric scores before and after critique, launch-gate checks, critique changes, reviewer outcomes, and failure categories.

Copy `examples/eval-case.json` or `examples/eval-result.json`, then validate from the repository root:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_eval_case.py path/to/eval-case.json
python3 scripts/validate_eval_result.py path/to/eval-result.json
```

Both validators apply JSON Schema Draft 2020-12 constraints, accept multiple paths, and exit nonzero if any file is invalid. The result validator also verifies that each declared rubric total equals the sum of its 13 dimensions.

Committed negative fixtures under `examples/invalid/` demonstrate rejected contracts. They are intentionally invalid and should only be used to test consumers and validators. Runtime integration is tracked separately from these portable contracts.

Keep raw reasoning only when the runtime permits it. Runtime output and concise reviewer notes are sufficient evidence; do not add secrets or private data to result files.
