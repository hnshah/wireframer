import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "launch_readiness.py"


class LaunchReadinessTests(unittest.TestCase):
    def test_report_is_blocked_by_missing_links_and_benchmark_evidence(self):
        sys.path.insert(0, str(REPO_ROOT))
        try:
            from scripts.launch_readiness import build_readiness
        finally:
            sys.path.pop(0)

        report = build_readiness(REPO_ROOT)

        self.assertEqual(report["overall_status"], "blocked")
        gates = {gate["id"]: gate for gate in report["gates"]}
        self.assertEqual(gates["canonical_skill"]["status"], "passed")
        self.assertEqual(gates["public_grok_bot_link"]["status"], "failed")
        self.assertEqual(gates["figma_community_link"]["status"], "failed")
        self.assertEqual(gates["benchmark_evidence"]["status"], "unverified")
        self.assertEqual(gates["runtime_smoke_tests"]["status"], "external_manual")
        self.assertEqual(
            set(report["summary"]),
            {"passed", "failed", "unverified", "external_manual"},
        )

    def test_eval_evidence_can_pass_numeric_gates_but_not_external_gates(self):
        sys.path.insert(0, str(REPO_ROOT))
        try:
            from scripts.launch_readiness import build_readiness
        finally:
            sys.path.pop(0)

        with tempfile.TemporaryDirectory() as temp_dir:
            evidence_path = Path(temp_dir) / "eval-report.json"
            evidence_path.write_text(
                json.dumps(
                    {
                        "summary": {
                            "mean_post_critique_score": 91,
                            "critical_failures": 0,
                            "useful_without_clarification_rate": 0.95,
                            "distinct_alternative_rate": 0.9,
                        },
                        "benchmark": {"wins": 23, "tasks": 30},
                    }
                ),
                encoding="utf-8",
            )
            report = build_readiness(REPO_ROOT, evidence_path)

        gates = {gate["id"]: gate for gate in report["gates"]}
        self.assertEqual(gates["functional_eval_evidence"]["status"], "passed")
        self.assertEqual(gates["benchmark_evidence"]["status"], "passed")
        self.assertEqual(report["overall_status"], "blocked")

    def test_cli_writes_json_and_markdown_and_exits_nonzero_when_blocked(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            json_path = Path(temp_dir) / "readiness.json"
            markdown_path = Path(temp_dir) / "readiness.md"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo-root",
                    str(REPO_ROOT),
                    "--json-output",
                    str(json_path),
                    "--markdown-output",
                    str(markdown_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertTrue(json_path.exists())
            self.assertTrue(markdown_path.exists())
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["overall_status"], "blocked")
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("# Wireframer launch readiness", markdown)
            self.assertIn("Remaining external/manual steps", markdown)
            self.assertIn("Public Grok Bot link", markdown)


if __name__ == "__main__":
    unittest.main()
