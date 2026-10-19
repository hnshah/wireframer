#!/usr/bin/env python3
"""Validate Wireframer eval result files."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "evals" / "eval-result.schema.json"


def load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("top-level JSON value must be an object")
    return value


def format_path(parts: Iterable[Any]) -> str:
    rendered = "$"
    for part in parts:
        rendered += f"[{part}]" if isinstance(part, int) else f".{part}"
    return rendered


def semantic_errors(instance: Dict[str, Any]) -> List[str]:
    errors = []
    rubric = instance.get("rubric")
    if not isinstance(rubric, dict):
        return errors

    for phase in ("before_critique", "after_critique"):
        result = rubric.get(phase)
        if not isinstance(result, dict):
            continue
        scores = result.get("scores")
        total = result.get("total")
        if not isinstance(scores, dict) or isinstance(total, bool) or not isinstance(total, (int, float)):
            continue
        dimension_sum = sum(
            value
            for value in scores.values()
            if not isinstance(value, bool) and isinstance(value, (int, float))
        )
        if total != dimension_sum:
            errors.append(
                f"$.rubric.{phase}.total: {total} does not equal dimension sum {dimension_sum}"
            )
    return errors


def validate(path: Path, schema_path: Path) -> List[str]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    instance = load_json(path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = [
        f"{format_path(error.absolute_path)}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    ]
    return schema_errors + semantic_errors(instance)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", nargs="+", type=Path, help="eval result JSON file(s)")
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help=f"schema path (default: {DEFAULT_SCHEMA.relative_to(ROOT)})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    exit_code = 0
    for result_path in args.results:
        try:
            errors = validate(result_path, args.schema)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            print(f"invalid: {result_path}: {error}", file=sys.stderr)
            exit_code = 1
            continue

        if errors:
            print(f"invalid: {result_path}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            exit_code = 1
        else:
            print(f"valid: {result_path}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
