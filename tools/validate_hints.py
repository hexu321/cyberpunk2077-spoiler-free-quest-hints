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
REQUIRED_RULE_KEYS = {"id", "questPath", "level", "label", "source"}
ALLOWED_RULE_KEYS = REQUIRED_RULE_KEYS | {"objectivePath", "enabled"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def validate_rule(rule: object, index: int, seen_ids: set[str]) -> list[str]:
    errors: list[str] = []
    prefix = f"rules[{index}]"

    if not isinstance(rule, dict):
        return [f"{prefix} must be an object"]

    keys = set(rule)
    missing = REQUIRED_RULE_KEYS - keys
    extra = keys - ALLOWED_RULE_KEYS
    forbidden = keys & FORBIDDEN_KEYS

    if missing:
        errors.append(f"{prefix} missing required keys: {sorted(missing)}")
    if extra:
        errors.append(f"{prefix} has unsupported keys: {sorted(extra)}")
    if forbidden:
        errors.append(f"{prefix} contains spoiler-prone forbidden keys: {sorted(forbidden)}")

    rule_id = rule.get("id")
    if not isinstance(rule_id, str) or not rule_id.strip():
        errors.append(f"{prefix}.id must be a non-empty string")
    elif rule_id in seen_ids:
        errors.append(f"{prefix}.id duplicates an earlier id: {rule_id}")
    else:
        seen_ids.add(rule_id)

    quest_path = rule.get("questPath")
    if not isinstance(quest_path, str) or not quest_path.strip():
        errors.append(f"{prefix}.questPath must be a non-empty string")

    if "objectivePath" in rule:
        objective_path = rule.get("objectivePath")
        if not isinstance(objective_path, str) or not objective_path.strip():
            errors.append(f"{prefix}.objectivePath must be a non-empty string when present")

    level = rule.get("level")
    if level not in ALLOWED_LEVELS:
        errors.append(f"{prefix}.level must be one of {sorted(ALLOWED_LEVELS)}")
    else:
        expected_label = EXPECTED_LABELS[level]
        if rule.get("label") != expected_label:
            errors.append(
                f"{prefix}.label must be {expected_label!r} when level is {level!r}"
            )

    source = rule.get("source")
    if not isinstance(source, str) or not source.strip():
        errors.append(f"{prefix}.source must be a non-empty maintainer provenance string")

    enabled = rule.get("enabled", True)
    if not isinstance(enabled, bool):
        errors.append(f"{prefix}.enabled must be boolean when present")

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
    if set(payload) - {"schemaVersion", "rules"}:
        errors.append(f"unsupported top-level keys: {sorted(set(payload) - {'schemaVersion', 'rules'})}")

    if payload.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")

    rules = payload.get("rules")
    if not isinstance(rules, list):
        errors.append("rules must be an array")
        return errors

    seen_ids: set[str] = set()
    for index, rule in enumerate(rules):
        errors.extend(validate_rule(rule, index, seen_ids))

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
