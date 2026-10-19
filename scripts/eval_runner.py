#!/usr/bin/env python3
"""Run Wireframer eval prompts and generate launch-gate reports."""

import argparse
import json
import re
import shlex
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any, Dict, List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVALS_PATH = REPO_ROOT / "evals" / "EVALS.md"
DEFAULT_RESULTS_DIR = REPO_ROOT / "evals" / "results"
RUBRIC_DIMENSIONS = {
    "job_clarity": 15, "interaction_model": 15, "information_architecture": 10,
    "task_efficiency": 10, "hierarchy": 10, "discoverability": 8,
    "state_completeness": 8, "error_and_recovery": 6, "progressive_disclosure": 5,
    "consistency": 5, "ux_copy": 3, "accessibility": 3, "visual_restraint": 2,
}

@dataclass(frozen=True)
class EvalCase:
    case_id: str
    title: str
    prompt: str
    must: str
    fail_if: str


def _field(section: str, label: str) -> Optional[str]:
    match = re.search(r"^\*\*" + re.escape(label) + r":\*\*\s*(.+?)(?=\n\s*\n|\Z)", section, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return None
    value = " ".join(line.strip() for line in match.group(1).splitlines()).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def parse_eval_cases(source: str) -> List[EvalCase]:
    headings = list(re.finditer(r"^## Eval\s+(\d+)\s+[—-]\s+(.+?)\s*$", source, re.MULTILINE))
    cases = []
    for index, heading in enumerate(headings):
        case_id = "eval-{0:02d}".format(int(heading.group(1)))
        end = headings[index + 1].start() if index + 1 < len(headings) else len(source)
        section = source[heading.end():end]
        prompt, must, fail_if = _field(section, "Prompt"), _field(section, "Must"), _field(section, "Fail if")
        missing = [label for label, value in (("Prompt", prompt), ("Must", must), ("Fail if", fail_if)) if not value]
        if missing:
            raise ValueError("{0} is missing required field(s): {1}".format(case_id, ", ".join(missing)))
        cases.append(EvalCase(case_id, heading.group(2).strip(), prompt or "", must or "", fail_if or ""))
    if not cases:
        raise ValueError("No canonical eval sections found")
    duplicates = [case_id for case_id, count in Counter(case.case_id for case in cases).items() if count > 1]
    if duplicates:
        raise ValueError("Duplicate eval IDs: {0}".format(", ".join(duplicates)))
    return cases


def load_eval_cases(path: Path = DEFAULT_EVALS_PATH) -> List[EvalCase]:
    return parse_eval_cases(path.read_text(encoding="utf-8"))


def _empty_rubric() -> Dict[str, Any]:
    return {"scores": {name: 0 for name in RUBRIC_DIMENSIONS}, "total": 0}


def run_cases(cases: Sequence[EvalCase], command: Sequence[str], output_dir: Path, *, runtime: str, model: str, skill_version: str, condition: str = "wireframer", force: bool = False, timeout: Optional[float] = None) -> List[Path]:
    if not command:
        raise ValueError("Runtime command cannot be empty")
    output_dir.mkdir(parents=True, exist_ok=True)
    targets = [output_dir / (case.case_id + ".json") for case in cases]
    existing = [path for path in targets if path.exists()]
    if existing and not force:
        raise FileExistsError("Refusing to overwrite existing result(s): {0}. Pass --force to replace them.".format(", ".join(str(path) for path in existing)))
    written = []
    for case, target in zip(cases, targets):
        started, start_clock = datetime.now(timezone.utc), time.monotonic()
        try:
            completed = subprocess.run(list(command), input=case.prompt, text=True, capture_output=True, check=False, timeout=timeout)
            returncode, stdout, stderr, timed_out = completed.returncode, completed.stdout, completed.stderr, False
        except subprocess.TimeoutExpired as error:
            returncode, stdout, stderr, timed_out = 124, error.stdout or "", error.stderr or "", True
            if isinstance(stdout, bytes): stdout = stdout.decode(errors="replace")
            if isinstance(stderr, bytes): stderr = stderr.decode(errors="replace")
            stderr = (stderr + "\nRuntime command timed out.").lstrip()
        output_path = output_dir / (case.case_id + ".output.md")
        execution_path = output_dir / (case.case_id + ".execution.json")
        output_path.write_text(stdout, encoding="utf-8")
        execution_path.write_text(json.dumps({"command": list(command), "started_at": started.isoformat(), "duration_seconds": round(time.monotonic() - start_clock, 3), "returncode": returncode, "timed_out": timed_out, "stderr": stderr}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        payload = {
            "schema_version": "1.0", "eval_id": case.case_id, "eval_type": "functional",
            "run": {"id": "{0}-{1}".format(started.strftime("%Y%m%dT%H%M%SZ"), case.case_id), "started_at": started.isoformat(), "runtime": runtime, "model": model, "skill_version": skill_version, "condition": condition},
            "input": {"prompt": case.prompt, "source": "canonical", "reference_uris": []},
            "artifacts": [{"kind": "design_record", "uri": output_path.name, "label": "Untouched runtime output"}],
            "rubric": {"before_critique": _empty_rubric(), "after_critique": _empty_rubric()},
            "checks": {"case_specific_pass": False, "critical_failure": False, "useful_without_unnecessary_clarification": False, "alternatives_warranted": False, "alternatives_behaviorally_distinct": None},
            "critique": {"screens_removed": 0, "important_states_initially_missed": 0, "changes": []},
            "review": {"task_success": None, "preference": "not_compared", "corrections": []},
            "failure_categories": ["execution/tool failure"] if returncode != 0 else [],
            "notes": "Pending human review. Must: {0} Fail if: {1}".format(case.must, case.fail_if),
        }
        target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        written.append(target)
    return written


def load_results(results_dir: Path) -> List[Dict[str, Any]]:
    paths = sorted(path for path in results_dir.glob("eval-*.json") if re.fullmatch(r"eval-\d+\.json", path.name))
    if not paths: raise ValueError("No eval result files found in {0}".format(results_dir))
    results = []
    for path in paths:
        try: payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error: raise ValueError("Could not read {0}: {1}".format(path, error)) from error
        if not isinstance(payload, dict) or not all(key in payload for key in ("eval_id", "rubric", "checks", "review")):
            raise ValueError("{0} is not a Wireframer eval result".format(path))
        results.append(payload)
    return results


def _rate(numerator: int, denominator: int) -> Optional[float]:
    return round(numerator / denominator, 4) if denominator else None


def build_report(results: Sequence[Dict[str, Any]], expected_case_count: int) -> Dict[str, Any]:
    case_ids = [result.get("eval_id") for result in results]
    duplicates = [case_id for case_id, count in Counter(case_ids).items() if count > 1]
    if duplicates: raise ValueError("Duplicate result IDs: {0}".format(", ".join(str(item) for item in duplicates)))
    execution_failures = sum("execution/tool failure" in result.get("failure_categories", []) for result in results)
    scored = [result for result in results if result["review"].get("task_success") is not None]
    pre_scores = [float(result["rubric"]["before_critique"]["total"]) for result in scored]
    post_scores = [float(result["rubric"]["after_critique"]["total"]) for result in scored]
    critical_failures = sum(bool(result["checks"]["critical_failure"]) for result in scored)
    useful_count = sum(bool(result["checks"]["useful_without_unnecessary_clarification"]) for result in scored)
    alternatives = [result for result in scored if result["checks"]["alternatives_warranted"]]
    distinct_count = sum(bool(result["checks"].get("alternatives_behaviorally_distinct")) for result in alternatives)
    correction_counts = Counter(correction["category"] for result in scored for correction in result["review"].get("corrections", []))
    mean_pre, mean_post = (round(mean(pre_scores), 2) if pre_scores else None), (round(mean(post_scores), 2) if post_scores else None)
    useful_rate, distinct_rate = _rate(useful_count, len(scored)), _rate(distinct_count, len(alternatives))
    all_scored = len(scored) == expected_case_count and len(results) == expected_case_count
    gates = {"all_cases_scored": all_scored, "mean_score": mean_post is not None and mean_post >= 85, "no_critical_failures": bool(scored) and critical_failures == 0, "useful_without_clarification": useful_rate is not None and useful_rate >= 0.9, "distinct_alternatives": distinct_rate is not None and distinct_rate >= 0.8, "self_critique_improved": mean_pre is not None and mean_post is not None and mean_post > mean_pre}
    summary = {"expected": expected_case_count, "result_files": len(results), "completed": len(scored), "unscored": len(results) - len(scored), "execution_failures": execution_failures, "mean_pre_critique_score": mean_pre, "mean_post_critique_score": mean_post, "critical_failures": critical_failures, "useful_without_clarification_rate": useful_rate, "alternatives_warranted": len(alternatives), "distinct_alternative_rate": distinct_rate, "corrections_by_category": dict(sorted(correction_counts.items()))}
    cases = [{"id": result["eval_id"], "status": "scored" if result["review"].get("task_success") is not None else "pending", "pre_critique_score": result["rubric"]["before_critique"]["total"] if result["review"].get("task_success") is not None else None, "post_critique_score": result["rubric"]["after_critique"]["total"] if result["review"].get("task_success") is not None else None, "critical_failure": result["checks"]["critical_failure"] if result["review"].get("task_success") is not None else None} for result in results]
    return {"schema_version": 1, "generated_at": datetime.now(timezone.utc).isoformat(), "summary": summary, "gates": gates, "overall_pass": all(gates.values()), "cases": cases}


def _display(value: Any) -> str:
    if value is None: return "n/a"
    if isinstance(value, float) and 0 <= value <= 1: return "{0:.1%}".format(value)
    return str(value)


def render_markdown(report: Dict[str, Any]) -> str:
    summary = report["summary"]
    lines = ["# Wireframer eval report", "", "Overall: **{0}**".format("PASS" if report["overall_pass"] else "NOT READY"), "", "## Summary", "", "- Completed: {0}/{1}".format(summary["completed"], summary["expected"]), "- Execution failures: {0}".format(summary["execution_failures"]), "- Mean score before critique: {0}".format(_display(summary["mean_pre_critique_score"])), "- Mean score after critique: {0}".format(_display(summary["mean_post_critique_score"])), "- Critical failures: {0}".format(summary["critical_failures"]), "- Useful without unnecessary clarification: {0}".format(_display(summary["useful_without_clarification_rate"])), "- Behaviorally distinct alternatives: {0}".format(_display(summary["distinct_alternative_rate"])), "", "## Launch gates", ""]
    labels = {"all_cases_scored": "All canonical cases scored", "mean_score": "Mean score ≥85", "no_critical_failures": "No critical failures", "useful_without_clarification": "Useful without unnecessary clarification ≥90%", "distinct_alternatives": "Distinct alternatives ≥80% where warranted", "self_critique_improved": "Self-critique improves mean score"}
    lines.extend("- [{0}] {1}".format("x" if passed else " ", labels[key]) for key, passed in report["gates"].items())
    lines.extend(["", "## Cases", "", "| Case | Status | Pre | Post | Critical failure |", "|---|---|---:|---:|---|"])
    lines.extend("| {id} | {status} | {pre} | {post} | {critical} |".format(id=case["id"], status=case["status"], pre=_display(case["pre_critique_score"]), post=_display(case["post_critique_score"]), critical=_display(case["critical_failure"])) for case in report["cases"])
    if summary["corrections_by_category"]:
        lines.extend(["", "## Corrections by category", ""])
        lines.extend("- {0}: {1}".format(category, count) for category, count in summary["corrections_by_category"].items())
    return "\n".join(lines) + "\n"


def write_report(report: Dict[str, Any], markdown_path: Path, json_path: Path) -> None:
    markdown_path.parent.mkdir(parents=True, exist_ok=True); json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--evals", type=Path, default=DEFAULT_EVALS_PATH)
    subparsers = parser.add_subparsers(dest="action", required=True); subparsers.add_parser("list")
    run = subparsers.add_parser("run"); run.add_argument("--command", required=True); run.add_argument("--runtime", required=True); run.add_argument("--model", required=True); run.add_argument("--skill-version", required=True); run.add_argument("--condition", choices=("wireframer", "unskilled_baseline", "native_generator", "ablation"), default="wireframer"); run.add_argument("--output-dir", type=Path, default=DEFAULT_RESULTS_DIR); run.add_argument("--case", action="append", dest="case_ids"); run.add_argument("--timeout", type=float); run.add_argument("--force", action="store_true")
    report = subparsers.add_parser("report"); report.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS_DIR); report.add_argument("--markdown", type=Path, default=DEFAULT_RESULTS_DIR / "report.md"); report.add_argument("--json", type=Path, default=DEFAULT_RESULTS_DIR / "report.json")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        cases = load_eval_cases(args.evals)
        if args.action == "list":
            for case in cases: print("{0}\t{1}".format(case.case_id, case.title))
            return 0
        if args.action == "run":
            selected = cases
            if args.case_ids:
                wanted = set(args.case_ids); selected = [case for case in cases if case.case_id in wanted]; missing = wanted.difference(case.case_id for case in selected)
                if missing: raise ValueError("Unknown case ID(s): {0}".format(", ".join(sorted(missing))))
            paths = run_cases(selected, shlex.split(args.command), args.output_dir, runtime=args.runtime, model=args.model, skill_version=args.skill_version, condition=args.condition, force=args.force, timeout=args.timeout)
            for path in paths: print(path)
            return 0 if all(json.loads(path.with_name(path.stem + ".execution.json").read_text())["returncode"] == 0 for path in paths) else 1
        report = build_report(load_results(args.results_dir), len(cases)); write_report(report, args.markdown, args.json); print(args.markdown); print(args.json)
        return 0 if report["overall_pass"] else 1
    except (OSError, ValueError, FileExistsError) as error:
        print("error: {0}".format(error), file=sys.stderr); return 2

if __name__ == "__main__": sys.exit(main())
