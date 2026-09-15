from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_STATUSES = {
    "candidate",
    "journal-located",
    "logic-verified",
    "in-game-verified",
    "ready",
    "shipped",
    "rejected",
}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}
ALLOWED_IMPACTS = {"relationship", "followup", "ending"}
ALLOWED_LEVELS = {"notice", "important", "critical"}
REQUIRED_KEYS = {
    "id",
    "questId",
    "questPath",
    "objectivePath",
    "objectiveDescription",
    "suspectedLevel",
    "suspectedImpacts",
    "status",
    "confidence",
    "journalVerified",
    "gameLogicVerified",
    "externalCorroborated",
    "inGameVerified",
    "notes",
}


def validate_stage_candidates(path: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_objectives: set[str] = set()

    if not path.exists():
        return [f"file not found: {path}"]

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip():
            continue
        prefix = f"line {line_number}"
        try:
            item = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"{prefix}: invalid JSON: {exc.msg}")
            continue

        if not isinstance(item, dict):
            errors.append(f"{prefix}: entry must be an object")
            continue

        missing = REQUIRED_KEYS - set(item)
        extra = set(item) - REQUIRED_KEYS
        if missing:
            errors.append(f"{prefix}: missing keys: {sorted(missing)}")
        if extra:
            errors.append(f"{prefix}: unsupported keys: {sorted(extra)}")

        candidate_id = item.get("id")
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            errors.append(f"{prefix}: id must be a non-empty string")
        elif candidate_id in seen_ids:
            errors.append(f"{prefix}: duplicate id: {candidate_id}")
        else:
            seen_ids.add(candidate_id)

        quest_id = item.get("questId")
        quest_path = item.get("questPath")
        objective_path = item.get("objectivePath")
        for key, value in (
            ("questId", quest_id),
            ("questPath", quest_path),
            ("objectivePath", objective_path),
            ("objectiveDescription", item.get("objectiveDescription")),
            ("notes", item.get("notes")),
        ):
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}: {key} must be a non-empty string")

        if isinstance(quest_path, str) and isinstance(objective_path, str):
            if not objective_path.startswith(quest_path + "/"):
                errors.append(f"{prefix}: objectivePath must belong to questPath")
            if objective_path in seen_objectives:
                errors.append(f"{prefix}: duplicate objectivePath: {objective_path}")
            else:
                seen_objectives.add(objective_path)

        impacts = item.get("suspectedImpacts")
        if not isinstance(impacts, list) or not impacts:
            errors.append(f"{prefix}: suspectedImpacts must be a non-empty array")
        elif any(impact not in ALLOWED_IMPACTS for impact in impacts):
            errors.append(f"{prefix}: suspectedImpacts must use only {sorted(ALLOWED_IMPACTS)}")
        elif len(set(impacts)) != len(impacts):
            errors.append(f"{prefix}: suspectedImpacts contains duplicates")

        if item.get("suspectedLevel") not in ALLOWED_LEVELS:
            errors.append(f"{prefix}: invalid suspectedLevel: {item.get('suspectedLevel')!r}")
        if item.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{prefix}: invalid status: {item.get('status')!r}")
        if item.get("confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"{prefix}: invalid confidence: {item.get('confidence')!r}")

        for key in (
            "journalVerified",
            "gameLogicVerified",
            "externalCorroborated",
            "inGameVerified",
        ):
            if not isinstance(item.get(key), bool):
                errors.append(f"{prefix}: {key} must be boolean")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python tools/validate_stage_candidates.py <stage-candidates.jsonl>")
        return 2

    path = Path(argv[1])
    errors = validate_stage_candidates(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {path} passed stage candidate validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
