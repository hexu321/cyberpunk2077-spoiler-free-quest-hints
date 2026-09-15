from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from tools.validate_hints import validate_document
except ModuleNotFoundError:
    from validate_hints import validate_document

HEADER = """module SpoilerFreeQuestHints

// Generated from data/hints.json. Do not edit by hand.
"""

IMPACT_LABELS = {
    "relationship": "人物关系",
    "followup": "后续任务",
    "ending": "结局条件",
}


def reds_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def impact_label(impacts: list[str]) -> str:
    return " / ".join(IMPACT_LABELS[impact] for impact in impacts)


def generate(input_path: Path) -> str:
    errors = validate_document(input_path)
    if errors:
        raise ValueError("\n".join(errors))

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    quest_impacts: list[dict[str, object]] = []
    exact_stage_hints: list[dict[str, object]] = []
    fallback_stage_hints: list[dict[str, object]] = []

    for rule in payload["questImpacts"]:
        if rule.get("enabled", True):
            quest_impacts.append(rule)

    for rule in payload["stageHints"]:
        if not rule.get("enabled", True) or rule["level"] == "none":
            continue
        if "objectivePath" in rule:
            exact_stage_hints.append(rule)
        else:
            fallback_stage_hints.append(rule)

    lines = [HEADER.rstrip(), ""]

    lines.append("public func QOHResolveQuestImpactLabel(questPath: String) -> String {")
    for rule in quest_impacts:
        label = impact_label([str(value) for value in rule["impacts"]])
        lines.append(f'  if QOHPathMatches(questPath, "{reds_string(str(rule["questPath"]))}") {{')
        lines.append(f'    return "{reds_string(label)}";')
        lines.append("  };")
    lines.append('  return "";')
    lines.append("}")
    lines.append("")

    lines.append("public func QOHResolveExactObjectiveLabel(objectivePath: String) -> String {")
    for rule in exact_stage_hints:
        lines.append(
            f'  if QOHPathMatches(objectivePath, "{reds_string(str(rule["objectivePath"]))}") {{'
        )
        lines.append(f'    return "{reds_string(str(rule["label"]))}";')
        lines.append("  };")
    lines.append('  return "";')
    lines.append("}")
    lines.append("")

    lines.append("public func QOHResolveQuestFallbackLabel(questPath: String) -> String {")
    for rule in fallback_stage_hints:
        lines.append(f'  if QOHPathMatches(questPath, "{reds_string(str(rule["questPath"]))}") {{')
        lines.append(f'    return "{reds_string(str(rule["label"]))}";')
        lines.append("  };")
    lines.append('  return "";')
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print("Usage: python tools/generate_runtime_rules.py <hints.json> [output.reds]")
        return 2

    input_path = Path(argv[1])
    try:
        generated = generate(input_path)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    if len(argv) == 3:
        output_path = Path(argv[2])
        output_path.write_text(generated, encoding="utf-8", newline="\n")
        print(f"OK: wrote {output_path}")
    else:
        print(generated, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
