#!/usr/bin/env python3
"""Validate Wireframer eval case files."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "evals" / "eval-case.schema.json"


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


def validate(path: Path, schema_path: Path) -> List[str]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    instance = load_json(path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{format_path(error.absolute_path)}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases", nargs="+", type=Path, help="eval case JSON file(s)")
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
    for case_path in args.cases:
        try:
            errors = validate(case_path, args.schema)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            print(f"invalid: {case_path}: {error}", file=sys.stderr)
            exit_code = 1
            continue

        if errors:
            print(f"invalid: {case_path}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            exit_code = 1
        else:
            print(f"valid: {case_path}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
