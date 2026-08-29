# Contributing

Wireframer improves through reproducible failures.

The preferred contribution starts with a real task where the skill made a poor product decision. Preserve the original input and output before changing anything.

## Contribution loop

1. Reproduce the failure on the current skill version.
2. Classify what failed.
3. Add or update an eval that captures the failure.
4. Make the smallest methodology change that addresses it.
5. Run the full eval suite and check for regressions.
6. Include the before and after result in the pull request.

Changes that only make one example look better are weak evidence. We want improvements that generalize without flattening the skill into a larger prompt.

## Useful evidence

A strong contribution includes the original brief, generated artifact, human correction, failure category, runtime, skill version, and any test result that followed.

## Scope

Wireframer should stay focused on product-design reasoning that produces low-fidelity wireframes. High-fidelity visual styling, code generation, and tool-specific canvas mechanics belong in specialist skills unless repeated evidence shows they need to change the canonical method.
