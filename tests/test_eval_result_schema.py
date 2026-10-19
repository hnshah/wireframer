import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
CASE_SCHEMA_PATH = ROOT / "evals" / "eval-case.schema.json"
CASE_EXAMPLE_PATH = ROOT / "evals" / "examples" / "eval-case.json"
INVALID_CASE_PATH = ROOT / "evals" / "examples" / "invalid" / "eval-case-missing-must.json"
SCHEMA_PATH = ROOT / "evals" / "eval-result.schema.json"
EXAMPLE_PATH = ROOT / "evals" / "examples" / "eval-result.json"
INVALID_RESULT_PATH = ROOT / "evals" / "examples" / "invalid" / "eval-result-wrong-total.json"
CASE_VALIDATOR_PATH = ROOT / "scripts" / "validate_eval_case.py"
VALIDATOR_PATH = ROOT / "scripts" / "validate_eval_result.py"


class EvalResultSchemaTests(unittest.TestCase):
    def load_schema_and_example(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        example = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))
        return schema, example

    def test_schema_is_valid_draft_2020_12(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_example_satisfies_schema(self):
        schema, example = self.load_schema_and_example()
        Draft202012Validator(schema).validate(example)

    def test_rubric_requires_every_weighted_dimension(self):
        schema, example = self.load_schema_and_example()
        invalid = copy.deepcopy(example)
        del invalid["rubric"]["after_critique"]["scores"]["job_clarity"]

        errors = list(Draft202012Validator(schema).iter_errors(invalid))

        self.assertTrue(errors)

    def test_rubric_dimension_cannot_exceed_its_weight(self):
        schema, example = self.load_schema_and_example()
        invalid = copy.deepcopy(example)
        invalid["rubric"]["after_critique"]["scores"]["visual_restraint"] = 3

        errors = list(Draft202012Validator(schema).iter_errors(invalid))

        self.assertTrue(errors)

    def test_runner_template_with_zero_scores_satisfies_schema(self):
        schema, example = self.load_schema_and_example()
        pending = copy.deepcopy(example)
        for phase in ("before_critique", "after_critique"):
            pending["rubric"][phase]["scores"] = {
                name: 0 for name in pending["rubric"][phase]["scores"]
            }
            pending["rubric"][phase]["total"] = 0
        pending["checks"].update(
            {
                "case_specific_pass": False,
                "useful_without_unnecessary_clarification": False,
                "alternatives_warranted": False,
                "alternatives_behaviorally_distinct": None,
            }
        )
        pending["review"]["task_success"] = None

        Draft202012Validator(schema).validate(pending)

    def test_result_rejects_unset_launch_gate(self):
        schema, example = self.load_schema_and_example()
        invalid = copy.deepcopy(example)
        invalid["checks"]["critical_failure"] = None

        errors = list(Draft202012Validator(schema).iter_errors(invalid))

        self.assertTrue(errors)

    def test_validator_accepts_example(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), str(EXAMPLE_PATH)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("valid:", result.stdout)

    def test_validator_rejects_total_that_does_not_match_dimension_sum(self):
        _, example = self.load_schema_and_example()
        invalid = copy.deepcopy(example)
        invalid["rubric"]["after_critique"]["total"] = 99

        with tempfile.TemporaryDirectory() as directory:
            result_path = Path(directory) / "invalid-result.json"
            result_path.write_text(json.dumps(invalid), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(result_path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("does not equal dimension sum", result.stderr)

    def test_case_schema_and_valid_fixture(self):
        schema = json.loads(CASE_SCHEMA_PATH.read_text(encoding="utf-8"))
        example = json.loads(CASE_EXAMPLE_PATH.read_text(encoding="utf-8"))

        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(example)

    def test_case_validator_accepts_valid_fixture_and_rejects_invalid_fixture(self):
        valid = subprocess.run(
            [sys.executable, str(CASE_VALIDATOR_PATH), str(CASE_EXAMPLE_PATH)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        invalid = subprocess.run(
            [sys.executable, str(CASE_VALIDATOR_PATH), str(INVALID_CASE_PATH)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(valid.returncode, 0, valid.stderr)
        self.assertIn("valid:", valid.stdout)
        self.assertNotEqual(invalid.returncode, 0)
        self.assertIn("'must' is a required property", invalid.stderr)

    def test_result_validator_rejects_committed_invalid_fixture(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), str(INVALID_RESULT_PATH)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("does not equal dimension sum", result.stderr)


if __name__ == "__main__":
    unittest.main()
