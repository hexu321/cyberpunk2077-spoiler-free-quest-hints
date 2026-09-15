from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_STATUSES = {
    "candidate",
    "source-verified",
    "journal-located",
    "logic-verified",
    "in-game-verified",
    "ready",
    "shipped",
    "rejected",
}
ALLOWED_CONFIDENCE = {"seed", "low", "medium", "high"}
ALLOWED_IMPACTS = {"relationship", "followup", "ending"}
REQUIRED_KEYS = {
    "id",
    "questId",
    "questPath",
    "title",
    "suspectedImpacts",
    "status",
    "confidence",
    "seedSource",
    "sourceRef",
    "needsObjectiveResearch",
    "journalVerified",
    "gameLogicVerified",
    "externalCorroborated",
    "inGameVerified",
    "lastVerifiedGameVersion",
    "notes",
}


def validate_candidates(path: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_quests: set[str] = set()

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
        if not isinstance(quest_id, str) or not quest_id.strip():
            errors.append(f"{prefix}: questId must be a non-empty string")
        elif quest_id in seen_quests:
            errors.append(f"{prefix}: duplicate questId: {quest_id}")
        else:
            seen_quests.add(quest_id)

        quest_path = item.get("questPath")
        if quest_path is not None and (not isinstance(quest_path, str) or not quest_path.strip()):
            errors.append(f"{prefix}: questPath must be null or a non-empty string")

        title = item.get("title")
        if title is not None and (not isinstance(title, str) or not title.strip()):
            errors.append(f"{prefix}: title must be null or a non-empty string")

        impacts = item.get("suspectedImpacts")
        if not isinstance(impacts, list) or not impacts:
            errors.append(f"{prefix}: suspectedImpacts must be a non-empty array")
        elif any(impact not in ALLOWED_IMPACTS for impact in impacts):
            errors.append(
                f"{prefix}: suspectedImpacts must use only {sorted(ALLOWED_IMPACTS)}"
            )
        elif len(set(impacts)) != len(impacts):
            errors.append(f"{prefix}: suspectedImpacts contains duplicates")

        if item.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{prefix}: invalid status: {item.get('status')!r}")
        if item.get("confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"{prefix}: invalid confidence: {item.get('confidence')!r}")

        for key in (
            "needsObjectiveResearch",
            "journalVerified",
            "gameLogicVerified",
            "externalCorroborated",
            "inGameVerified",
        ):
            if not isinstance(item.get(key), bool):
                errors.append(f"{prefix}: {key} must be boolean")

        for key in ("seedSource", "sourceRef", "notes"):
            if not isinstance(item.get(key), str) or not item.get(key, "").strip():
                errors.append(f"{prefix}: {key} must be a non-empty string")

        version = item.get("lastVerifiedGameVersion")
        if version is not None and (not isinstance(version, str) or not version.strip()):
            errors.append(
                f"{prefix}: lastVerifiedGameVersion must be null or a non-empty string"
            )

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python tools/validate_research_candidates.py <candidates.jsonl>")
        return 2

    path = Path(argv[1])
    errors = validate_candidates(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {path} passed research candidate validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
