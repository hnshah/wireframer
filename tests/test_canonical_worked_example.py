from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_canonical_example.py"
EXAMPLE = ROOT / "examples" / "CANONICAL_WORKED_EXAMPLE.md"


class CanonicalWorkedExampleValidationTests(unittest.TestCase):
    def run_validator(self, example: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(example)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_canonical_example_contains_the_complete_design_record(self) -> None:
        result = self.run_validator(EXAMPLE)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "canonical worked example: valid")

    def test_validator_reports_a_missing_required_section(self) -> None:
        source = EXAMPLE.read_text(encoding="utf-8")
        incomplete = source.replace("## Critique", "## Review notes", 1)

        with tempfile.TemporaryDirectory() as directory:
            example = Path(directory) / "incomplete.md"
            example.write_text(incomplete, encoding="utf-8")
            result = self.run_validator(example)

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required section: ## Critique", result.stderr)


if __name__ == "__main__":
    unittest.main()
