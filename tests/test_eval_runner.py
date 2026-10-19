import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from eval_runner import EvalCase, build_report, parse_eval_cases, run_cases, write_report  # noqa: E402
WEIGHTS = {
    "job_clarity": 15, "interaction_model": 15, "information_architecture": 10,
    "task_efficiency": 10, "hierarchy": 10, "discoverability": 8,
    "state_completeness": 8, "error_and_recovery": 6, "progressive_disclosure": 5,
    "consistency": 5, "ux_copy": 3, "accessibility": 3, "visual_restraint": 2,
}


def scores_for(total):
    scores, remaining = {}, total
    for name, weight in WEIGHTS.items():
        scores[name] = min(remaining, weight)
        remaining -= scores[name]
    return scores


def result(index, pre, post):
    return {
        "schema_version": "1.0", "eval_id": f"eval-{index:02d}", "eval_type": "functional",
        "run": {"id": f"run-{index}", "started_at": "2026-10-18T19:00:00+00:00", "runtime": "test", "model": "test", "skill_version": "0.2", "condition": "wireframer"},
        "input": {"prompt": "Prompt", "source": "canonical", "reference_uris": []},
        "artifacts": [{"kind": "design_record", "uri": f"eval-{index:02d}.output.md"}],
        "rubric": {"before_critique": {"scores": scores_for(pre), "total": pre}, "after_critique": {"scores": scores_for(post), "total": post}},
        "checks": {"case_specific_pass": True, "critical_failure": False, "useful_without_unnecessary_clarification": index != 10, "alternatives_warranted": index <= 5, "alternatives_behaviorally_distinct": index <= 4 if index <= 5 else None},
        "critique": {"screens_removed": 0, "important_states_initially_missed": 0, "changes": []},
        "review": {"task_success": True, "preference": "not_compared", "corrections": []},
        "failure_categories": [],
    }


class EvalRunnerTests(unittest.TestCase):
    def test_parses_numbered_evals(self):
        source = """## Eval 1 — First case

**Prompt:** "Do it."

**Must:** include context.

**Fail if:** context is missing.

## Cross-eval measurements
"""
        self.assertEqual(parse_eval_cases(source), [EvalCase("eval-01", "First case", "Do it.", "include context.", "context is missing.")])

    def test_rejects_eval_without_prompt(self):
        with self.assertRaisesRegex(ValueError, "eval-01.*Prompt"):
            parse_eval_cases("## Eval 1 — Missing\n\n**Must:** act.\n")

    def test_run_writes_schema_valid_pending_result_and_raw_evidence(self):
        case = EvalCase("eval-01", "First", "Hello runtime", "Must", "Fail")
        with tempfile.TemporaryDirectory() as directory:
            paths = run_cases([case], [sys.executable, "-c", "import sys; print(sys.stdin.read().upper())"], Path(directory), runtime="test-runtime", model="test-model", skill_version="0.2")
            payload = json.loads(paths[0].read_text())
            self.assertEqual(payload["eval_id"], "eval-01")
            self.assertIsNone(payload["review"]["task_success"])
            self.assertEqual((Path(directory) / "eval-01.output.md").read_text().strip(), "HELLO RUNTIME")
            self.assertEqual(json.loads((Path(directory) / "eval-01.execution.json").read_text())["returncode"], 0)

    def test_report_computes_functional_launch_gates(self):
        results = [result(index, score - 2, score) for index, score in enumerate((90, 88, 87, 85, 85, 86, 90, 91, 89, 89), 1)]
        report = build_report(results, expected_case_count=10)
        self.assertEqual(report["summary"]["mean_post_critique_score"], 88.0)
        self.assertEqual(report["summary"]["useful_without_clarification_rate"], 0.9)
        self.assertEqual(report["summary"]["distinct_alternative_rate"], 0.8)
        self.assertTrue(report["overall_pass"])

    def test_pending_result_cannot_pass(self):
        pending = result(1, 0, 0)
        pending["review"]["task_success"] = None
        report = build_report([pending], expected_case_count=10)
        self.assertEqual(report["summary"]["completed"], 0)
        self.assertFalse(report["overall_pass"])

    def test_writes_both_report_formats(self):
        report = build_report([], 10)
        with tempfile.TemporaryDirectory() as directory:
            markdown = Path(directory) / "report.md"
            machine = Path(directory) / "report.json"
            write_report(report, markdown, machine)
            self.assertIn("# Wireframer eval report", markdown.read_text())
            self.assertEqual(json.loads(machine.read_text())["summary"]["expected"], 10)

    def test_cli_lists_all_canonical_cases(self):
        completed = subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "eval_runner.py"), "list"], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("eval-01\tAmbiguous founder idea", completed.stdout)
        self.assertIn("eval-10\tExisting design system", completed.stdout)


if __name__ == "__main__":
    unittest.main()
