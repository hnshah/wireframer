#!/usr/bin/env python3
"""Build a deterministic, evidence-based Wireframer launch readiness report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional


VALID_STATUSES = ("passed", "failed", "unverified", "external_manual")


def _gate(
    gate_id: str,
    name: str,
    status: str,
    evidence: Iterable[str],
    detail: str,
) -> Dict[str, Any]:
    if status not in VALID_STATUSES:
        raise ValueError(f"invalid gate status: {status}")
    return {
        "id": gate_id,
        "name": name,
        "status": status,
        "evidence": list(evidence),
        "detail": detail,
    }


def _read_json(path: Path) -> Mapping[str, Any]:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"eval evidence must be a JSON object: {path}")
    return payload


def _metric(payload: Mapping[str, Any], *names: str) -> Any:
    containers = [payload]
    for key in ("summary", "metrics", "launch_metrics"):
        value = payload.get(key)
        if isinstance(value, dict):
            containers.append(value)
    for container in containers:
        for name in names:
            if name in container:
                return container[name]
    return None


def _functional_eval_gate(eval_evidence: Optional[Mapping[str, Any]], source: str) -> Dict[str, Any]:
    if eval_evidence is None:
        return _gate(
            "functional_eval_evidence",
            "Canonical functional eval evidence",
            "unverified",
            ["evals/EVALS.md defines cases, but no result report was supplied"],
            "Run the canonical eval suite and pass its machine-readable result report with --eval-report.",
        )

    mean_score = _metric(
        eval_evidence,
        "mean_post_critique_score",
        "mean_rubric_score",
        "rubric_mean",
        "mean_score",
    )
    critical_failures = _metric(eval_evidence, "critical_failures", "critical_failure_count")
    clarification_rate = _metric(eval_evidence, "clarification_rate")
    useful_rate = _metric(eval_evidence, "useful_without_clarification_rate")
    if clarification_rate is None and useful_rate is not None:
        clarification_rate = 1 - float(useful_rate)
    distinct_rate = _metric(
        eval_evidence,
        "distinct_alternative_rate",
        "behaviorally_distinct_alternative_rate",
    )
    metrics = {
        "mean_rubric_score": mean_score,
        "critical_failures": critical_failures,
        "clarification_rate": clarification_rate,
        "distinct_alternative_rate": distinct_rate,
    }
    missing = [name for name, value in metrics.items() if value is None]
    if missing:
        return _gate(
            "functional_eval_evidence",
            "Canonical functional eval evidence",
            "unverified",
            [source, f"missing metrics: {', '.join(missing)}"],
            "The supplied report is incomplete and cannot prove the functional launch gate.",
        )

    mean_value = float(metrics["mean_rubric_score"])
    critical_value = int(metrics["critical_failures"])
    clarification_value = float(metrics["clarification_rate"])
    distinct_value = float(metrics["distinct_alternative_rate"])
    passed = (
        mean_value >= 85
        and critical_value == 0
        and clarification_value <= 0.10
        and distinct_value >= 0.80
    )
    return _gate(
        "functional_eval_evidence",
        "Canonical functional eval evidence",
        "passed" if passed else "failed",
        [
            source,
            f"mean rubric score: {mean_score} (required >=85)",
            f"critical failures: {critical_failures} (required 0)",
            f"clarification rate: {clarification_rate} (required <=0.10)",
            f"distinct alternative rate: {distinct_rate} (required >=0.80)",
        ],
        "All numeric functional thresholds pass." if passed else "One or more functional thresholds fail.",
    )


def _benchmark_gate(eval_evidence: Optional[Mapping[str, Any]], source: str) -> Dict[str, Any]:
    benchmark: Any = eval_evidence.get("benchmark") if eval_evidence else None
    if not isinstance(benchmark, dict):
        benchmark = None
        for key in ("summary", "metrics", "launch_metrics"):
            container = eval_evidence.get(key) if eval_evidence else None
            if isinstance(container, dict) and isinstance(container.get("benchmark"), dict):
                benchmark = container["benchmark"]
                break
    if benchmark is None:
        return _gate(
            "benchmark_evidence",
            "30-task blind benchmark evidence",
            "unverified",
            ["evals/BENCHMARK.md defines the protocol; no benchmark result was supplied"],
            "Supply 30 task-level results with at least 21 Wireframer wins.",
        )

    wins = benchmark.get("wins")
    tasks = benchmark.get("tasks", benchmark.get("task_count"))
    if wins is None or tasks is None:
        return _gate(
            "benchmark_evidence",
            "30-task blind benchmark evidence",
            "unverified",
            [source, "benchmark wins or task count is missing"],
            "The benchmark result is incomplete.",
        )
    passed = int(tasks) >= 30 and int(wins) >= 21
    return _gate(
        "benchmark_evidence",
        "30-task blind benchmark evidence",
        "passed" if passed else "failed",
        [source, f"Wireframer wins: {wins}/{tasks} (required >=21/30)"],
        "Benchmark threshold passes." if passed else "Benchmark threshold does not pass.",
    )


def _link_gate(readme: str, gate_id: str, name: str, label: str) -> Dict[str, Any]:
    matching_lines = [line.strip() for line in readme.splitlines() if label.lower() in line.lower()]
    has_placeholder = any("COMING_SOON" in line for line in matching_lines)
    has_url = any(re.search(r"https?://", line) for line in matching_lines)
    passed = has_url and not has_placeholder
    return _gate(
        gate_id,
        name,
        "passed" if passed else "failed",
        matching_lines or [f"README.md has no {label} line"],
        "Public URL is present." if passed else "A real public URL must replace COMING_SOON before launch.",
    )


def _checklist_summary(checklist: str) -> Dict[str, Any]:
    completed = len(re.findall(r"^- \[[xX]\] ", checklist, flags=re.MULTILINE))
    pending = len(re.findall(r"^- \[ \] ", checklist, flags=re.MULTILINE))
    return {
        "source": "LAUNCH_CHECKLIST.md",
        "completed": completed,
        "pending": pending,
        "total": completed + pending,
    }


def build_readiness(repo_root: Path, eval_report: Optional[Path] = None) -> Dict[str, Any]:
    """Aggregate repository, checklist, eval, and external launch evidence."""
    repo_root = Path(repo_root).resolve()
    skill_path = repo_root / "SKILL.md"
    readme_path = repo_root / "README.md"
    checklist_path = repo_root / "LAUNCH_CHECKLIST.md"
    readme = readme_path.read_text(encoding="utf-8")
    checklist = checklist_path.read_text(encoding="utf-8")
    skill = skill_path.read_text(encoding="utf-8")

    eval_evidence = _read_json(eval_report) if eval_report else None
    eval_source = str(eval_report) if eval_report else "not supplied"
    version_match = re.search(r'^\s*version:\s*["\']?([^"\'\n]+)', skill, flags=re.MULTILINE)
    canonical_passed = skill_path.exists() and version_match is not None

    gates: List[Dict[str, Any]] = [
        _gate(
            "canonical_skill",
            "Canonical versioned skill",
            "passed" if canonical_passed else "failed",
            [
                "SKILL.md exists" if skill_path.exists() else "SKILL.md is missing",
                f"version: {version_match.group(1).strip()}" if version_match else "version metadata is missing",
            ],
            "The canonical skill is present and versioned." if canonical_passed else "Canonical skill requirements fail.",
        ),
        _functional_eval_gate(eval_evidence, eval_source),
        _benchmark_gate(eval_evidence, eval_source),
        _link_gate(readme, "public_grok_bot_link", "Public Grok Bot link", "Public Grok Bot"),
        _link_gate(readme, "figma_community_link", "Figma Community link", "Figma Community skill"),
        _gate(
            "runtime_smoke_tests",
            "Fresh-session Grok and Figma smoke tests",
            "external_manual",
            ["GROK_BOT_SETUP.md", "FIGMA_SKILL_SETUP.md"],
            "Run the documented smoke prompts in both hosted runtimes and preserve untouched outputs.",
        ),
        _gate(
            "public_release_operations",
            "Public sharing, tag, demo, and launch operations",
            "external_manual",
            ["LAUNCH_CHECKLIST.md sections G-J"],
            "Verify sharing from clean accounts, publish the links, create the release tag, and capture the demo.",
        ),
    ]

    summary = {status: 0 for status in VALID_STATUSES}
    for gate in gates:
        summary[gate["status"]] += 1
    overall_status = "ready" if all(gate["status"] == "passed" for gate in gates) else "blocked"
    return {
        "schema_version": 1,
        "product": "Wireframer",
        "overall_status": overall_status,
        "summary": summary,
        "checklist": _checklist_summary(checklist),
        "inputs": {
            "skill": "SKILL.md",
            "readme": "README.md",
            "launch_checklist": "LAUNCH_CHECKLIST.md",
            "eval_report": eval_source,
        },
        "gates": gates,
    }


def render_markdown(report: Mapping[str, Any]) -> str:
    summary = report["summary"]
    checklist = report["checklist"]
    lines = [
        "# Wireframer launch readiness",
        "",
        f"**Overall status:** {str(report['overall_status']).upper()}",
        "",
        (
            "This report is evidence-based. Unverified claims and hosted-runtime operations "
            "remain blocking until their evidence is captured."
        ),
        "",
        "## Summary",
        "",
        f"- Passed: {summary['passed']}",
        f"- Failed: {summary['failed']}",
        f"- Unverified: {summary['unverified']}",
        f"- External/manual: {summary['external_manual']}",
        f"- Launch checklist: {checklist['completed']}/{checklist['total']} checked",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
    ]
    for gate in report["gates"]:
        lines.append(f"| {gate['name']} | {gate['status']} | {gate['detail']} |")

    lines.extend(["", "## Evidence", ""])
    for gate in report["gates"]:
        lines.append(f"### {gate['name']}")
        lines.extend(f"- {item}" for item in gate["evidence"])
        lines.append("")

    lines.extend(["## Remaining external/manual steps", ""])
    external = [gate for gate in report["gates"] if gate["status"] == "external_manual"]
    if external:
        lines.extend(f"- {gate['name']}: {gate['detail']}" for gate in external)
    else:
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--eval-report", type=Path)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = build_readiness(args.repo_root, args.eval_report)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"launch readiness error: {exc}", file=sys.stderr)
        return 2

    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(render_markdown(report), encoding="utf-8")
    print(f"overall_status={report['overall_status']}", file=sys.stderr)
    print(f"json_report={args.json_output}", file=sys.stderr)
    print(f"markdown_report={args.markdown_output}", file=sys.stderr)
    return 0 if report["overall_status"] == "ready" else 1


if __name__ == "__main__":
    raise SystemExit(main())
