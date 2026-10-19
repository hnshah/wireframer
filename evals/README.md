# Executable eval results

`eval-result.schema.json` is the canonical machine-readable contract for one Wireframer eval run. It records the prompt and runtime, artifact locations, weighted rubric scores before and after critique, launch-gate checks, critique changes, reviewer outcomes, and failure categories. The same contract is emitted and consumed by `scripts/eval_runner.py`.

Copy `examples/eval-result.json` for a new run, then validate it from the repository root:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_eval_result.py path/to/eval-result.json
```

The validator applies JSON Schema Draft 2020-12 constraints and verifies that each declared rubric total equals the sum of its 13 dimensions. It accepts multiple result paths and exits nonzero if any file is invalid.

Keep raw reasoning only when the runtime permits it. Runtime output and concise reviewer notes are sufficient evidence; do not add secrets or private data to result files.
