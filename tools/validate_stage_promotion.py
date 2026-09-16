from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from tools.validate_hints import EXPECTED_LABELS
except ModuleNotFoundError:
    from validate_hints import EXPECTED_LABELS

PROMOTED_STATUSES = {
    "journal-located",
    "logic-verified",
    "in-game-verified",
    "ready",
    "shipped",
}


def load_stage_candidates(path: Path) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.strip():
            item = json.loads(raw_line)
            if isinstance(item, dict):
                candidates.append(item)
    return candidates


def validate_stage_promotion(stage_candidates_path: Path, hints_path: Path) -> list[str]:
    errors: list[str] = []

    if not stage_candidates_path.exists():
        return [f"file not found: {stage_candidates_path}"]
    if not hints_path.exists():
        return [f"file not found: {hints_path}"]

    try:
        candidates = load_stage_candidates(stage_candidates_path)
        hints_payload = json.loads(hints_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]

    stage_hints = hints_payload.get("stageHints")
    if not isinstance(stage_hints, list):
        return ["hints document must contain a stageHints array"]

    production_by_objective: dict[str, dict[str, object]] = {}
    for index, item in enumerate(stage_hints):
        if not isinstance(item, dict):
            continue
        objective_path = item.get("objectivePath")
        if not isinstance(objective_path, str) or not objective_path:
            continue
        production_by_objective[objective_path] = item

    eligible = [item for item in candidates if item.get("status") in PROMOTED_STATUSES]

    for item in eligible:
        candidate_id = str(item.get("id", ""))
        quest_path = str(item.get("questPath", ""))
        objective_path = str(item.get("objectivePath", ""))
        level = str(item.get("suspectedLevel", ""))
        expected_label = EXPECTED_LABELS.get(level)
        expected_runtime_id = f"research.{candidate_id}"

        runtime = production_by_objective.get(objective_path)
        if runtime is None:
            errors.append(
                f"{candidate_id}: eligible stage is not promoted to data/hints.json: {objective_path}"
            )
            continue

        if runtime.get("questPath") != quest_path:
            errors.append(
                f"{candidate_id}: questPath mismatch: research={quest_path!r}, runtime={runtime.get('questPath')!r}"
            )
        if runtime.get("level") != level:
            errors.append(
                f"{candidate_id}: level mismatch: research={level!r}, runtime={runtime.get('level')!r}"
            )
        if expected_label is None:
            errors.append(f"{candidate_id}: unsupported suspectedLevel: {level!r}")
        elif runtime.get("label") != expected_label:
            errors.append(
                f"{candidate_id}: label mismatch: expected={expected_label!r}, runtime={runtime.get('label')!r}"
            )
        if runtime.get("id") != expected_runtime_id:
            errors.append(
                f"{candidate_id}: runtime id should be {expected_runtime_id!r} for one-to-one traceability, got {runtime.get('id')!r}"
            )
        if runtime.get("source") != "research/stage-candidates.jsonl":
            errors.append(
                f"{candidate_id}: runtime source must point back to research/stage-candidates.jsonl"
            )

    eligible_objectives = {str(item.get("objectivePath", "")) for item in eligible}
    for runtime in stage_hints:
        if not isinstance(runtime, dict):
            continue
        if runtime.get("source") != "research/stage-candidates.jsonl":
            continue
        objective_path = runtime.get("objectivePath")
        if isinstance(objective_path, str) and objective_path not in eligible_objectives:
            errors.append(
                f"runtime stage has no eligible research candidate: {objective_path}"
            )

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(
            "Usage: python tools/validate_stage_promotion.py "
            "<stage-candidates.jsonl> <hints.json>"
        )
        return 2

    stage_candidates_path = Path(argv[1])
    hints_path = Path(argv[2])
    errors = validate_stage_promotion(stage_candidates_path, hints_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    candidates = load_stage_candidates(stage_candidates_path)
    eligible_count = sum(item.get("status") in PROMOTED_STATUSES for item in candidates)
    print(
        f"OK: {eligible_count}/{eligible_count} eligible stage candidates are promoted "
        "with exact objective mounts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
