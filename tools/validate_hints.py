from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_LEVELS = {"none", "notice", "important", "critical"}
EXPECTED_LABELS = {
    "none": "",
    "notice": "值得留意",
    "important": "重要阶段",
    "critical": "关键节点 · 建议存档",
}
ALLOWED_IMPACTS = {"relationship", "followup", "ending"}
FORBIDDEN_KEYS = {
    "choice",
    "choiceText",
    "recommendedChoice",
    "recommendedOption",
    "ending",
    "endingName",
    "outcome",
    "result",
    "reward",
    "romanceResult",
    "characterFate",
}
REQUIRED_IMPACT_KEYS = {"id", "questPath", "impacts", "source"}
ALLOWED_IMPACT_KEYS = REQUIRED_IMPACT_KEYS | {"enabled"}
REQUIRED_STAGE_KEYS = {"id", "questPath", "level", "label", "source"}
ALLOWED_STAGE_KEYS = REQUIRED_STAGE_KEYS | {"objectivePath", "enabled"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def validate_id(
    item: dict[str, object], prefix: str, seen_ids: set[str], errors: list[str]
) -> None:
    item_id = item.get("id")
    if not isinstance(item_id, str) or not item_id.strip():
        errors.append(f"{prefix}.id must be a non-empty string")
    elif item_id in seen_ids:
        errors.append(f"{prefix}.id duplicates an earlier id: {item_id}")
    else:
        seen_ids.add(item_id)


def validate_common(
    item: dict[str, object], prefix: str, seen_ids: set[str], errors: list[str]
) -> str | None:
    validate_id(item, prefix, seen_ids, errors)

    quest_path = item.get("questPath")
    if not isinstance(quest_path, str) or not quest_path.strip():
        errors.append(f"{prefix}.questPath must be a non-empty string")
        quest_path = None

    source = item.get("source")
    if not isinstance(source, str) or not source.strip():
        errors.append(f"{prefix}.source must be a non-empty maintainer provenance string")

    enabled = item.get("enabled", True)
    if not isinstance(enabled, bool):
        errors.append(f"{prefix}.enabled must be boolean when present")

    return quest_path


def validate_quest_impact(
    item: object,
    index: int,
    seen_ids: set[str],
    seen_quest_paths: set[str],
) -> list[str]:
    prefix = f"questImpacts[{index}]"
    if not isinstance(item, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    keys = set(item)
    missing = REQUIRED_IMPACT_KEYS - keys
    extra = keys - ALLOWED_IMPACT_KEYS
    forbidden = keys & FORBIDDEN_KEYS
    if missing:
        errors.append(f"{prefix} missing required keys: {sorted(missing)}")
    if extra:
        errors.append(f"{prefix} has unsupported keys: {sorted(extra)}")
    if forbidden:
        errors.append(f"{prefix} contains spoiler-prone forbidden keys: {sorted(forbidden)}")

    quest_path = validate_common(item, prefix, seen_ids, errors)
    if quest_path is not None:
        if quest_path in seen_quest_paths:
            errors.append(f"{prefix}.questPath duplicates an earlier quest impact: {quest_path}")
        else:
            seen_quest_paths.add(quest_path)

    impacts = item.get("impacts")
    if not isinstance(impacts, list) or not impacts:
        errors.append(f"{prefix}.impacts must be a non-empty array")
    else:
        invalid = [impact for impact in impacts if impact not in ALLOWED_IMPACTS]
        if invalid:
            errors.append(
                f"{prefix}.impacts contains unsupported values: {sorted(set(map(str, invalid)))}"
            )
        if len(impacts) != len(set(map(str, impacts))):
            errors.append(f"{prefix}.impacts must not contain duplicates")

    return errors


def validate_stage_hint(
    item: object,
    index: int,
    seen_ids: set[str],
    seen_objective_paths: set[str],
) -> list[str]:
    prefix = f"stageHints[{index}]"
    if not isinstance(item, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    keys = set(item)
    missing = REQUIRED_STAGE_KEYS - keys
    extra = keys - ALLOWED_STAGE_KEYS
    forbidden = keys & FORBIDDEN_KEYS
    if missing:
        errors.append(f"{prefix} missing required keys: {sorted(missing)}")
    if extra:
        errors.append(f"{prefix} has unsupported keys: {sorted(extra)}")
    if forbidden:
        errors.append(f"{prefix} contains spoiler-prone forbidden keys: {sorted(forbidden)}")

    quest_path = validate_common(item, prefix, seen_ids, errors)

    objective_path = item.get("objectivePath")
    if objective_path is not None:
        if not isinstance(objective_path, str) or not objective_path.strip():
            errors.append(f"{prefix}.objectivePath must be a non-empty string when present")
        else:
            if quest_path is not None and not objective_path.startswith(quest_path + "/"):
                errors.append(f"{prefix}.objectivePath must be inside its questPath")
            if objective_path in seen_objective_paths:
                errors.append(
                    f"{prefix}.objectivePath duplicates an earlier exact stage hint: {objective_path}"
                )
            else:
                seen_objective_paths.add(objective_path)

    level = item.get("level")
    if level not in ALLOWED_LEVELS:
        errors.append(f"{prefix}.level must be one of {sorted(ALLOWED_LEVELS)}")
    else:
        expected_label = EXPECTED_LABELS[str(level)]
        if item.get("label") != expected_label:
            errors.append(
                f"{prefix}.label must be {expected_label!r} when level is {level!r}"
            )

    return errors


def validate_document(path: Path) -> list[str]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"file not found: {path}"]
    except json.JSONDecodeError as exc:
        return [f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"]

    if not isinstance(payload, dict):
        return ["top-level value must be an object"]

    errors: list[str] = []
    allowed_top_level = {"schemaVersion", "questImpacts", "stageHints"}
    extra_top_level = set(payload) - allowed_top_level
    if extra_top_level:
        errors.append(f"unsupported top-level keys: {sorted(extra_top_level)}")

    if payload.get("schemaVersion") != 2:
        errors.append("schemaVersion must be 2")

    quest_impacts = payload.get("questImpacts")
    stage_hints = payload.get("stageHints")
    if not isinstance(quest_impacts, list):
        errors.append("questImpacts must be an array")
    if not isinstance(stage_hints, list):
        errors.append("stageHints must be an array")
    if errors and (not isinstance(quest_impacts, list) or not isinstance(stage_hints, list)):
        return errors

    seen_ids: set[str] = set()
    seen_quest_paths: set[str] = set()
    seen_objective_paths: set[str] = set()

    for index, item in enumerate(quest_impacts):
        errors.extend(validate_quest_impact(item, index, seen_ids, seen_quest_paths))
    for index, item in enumerate(stage_hints):
        errors.extend(validate_stage_hint(item, index, seen_ids, seen_objective_paths))

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python tools/validate_hints.py <hints.json>")
        return 2

    path = Path(argv[1])
    errors = validate_document(path)
    if errors:
        for error in errors:
            fail(error)
        return 1

    print(f"OK: {path} passed spoiler-free hint validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
