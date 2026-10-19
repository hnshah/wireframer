#!/usr/bin/env python3
"""Deterministically validate the canonical worked example contract."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXAMPLE = ROOT / "examples" / "CANONICAL_WORKED_EXAMPLE.md"
REQUIRED_SECTIONS = (
    "## Input",
    "## Design interpretation",
    "## Object model",
    "## Task flow",
    "## Interaction alternatives",
    "## Chosen model + rationale",
    "## Screen map",
    "## Initial wireframes",
    "## State coverage",
    "## Critique",
    "## Revised wireframes",
)
REQUIRED_ALTERNATIVES = ("### A.", "### B.", "### C.")


def validate(example: Path) -> list[str]:
    if not example.is_file():
        return [f"artifact not found: {example}"]

    text = example.read_text(encoding="utf-8")
    lines = set(text.splitlines())
    errors = [
        f"missing required section: {section}"
        for section in REQUIRED_SECTIONS
        if section not in lines
    ]

    for alternative in REQUIRED_ALTERNATIVES:
        if not any(line.startswith(alternative) for line in lines):
            errors.append(f"missing interaction alternative: {alternative}")

    if text.count("```text") < 5:
        errors.append("wireframe representation must contain at least five text diagrams")
    if "authored reference specimen" not in text:
        errors.append("example must identify itself as an authored reference specimen")
    if "### Initial score:" not in text or "### Revised score:" not in text:
        errors.append("critique must record both initial and revised scores")

    return errors


def main(argv: list[str]) -> int:
    example = Path(argv[1]) if len(argv) > 1 else DEFAULT_EXAMPLE
    errors = validate(example)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("canonical worked example: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
