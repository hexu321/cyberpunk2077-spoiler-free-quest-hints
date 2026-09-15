from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_stage_candidates import validate_stage_candidates


class ValidateStageCandidatesTests(unittest.TestCase):
    def write_lines(self, items: list[dict[str, object]]) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "stage-candidates.jsonl"
        path.write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in items) + "\n",
            encoding="utf-8",
        )
        return path

    def valid_item(self) -> dict[str, object]:
        return {
            "id": "stage.test",
            "questId": "sq_test",
            "questPath": "quests/side_quest/sq_test",
            "objectivePath": "quests/side_quest/sq_test/phase/objective",
            "objectiveDescription": "Talk to someone.",
            "suspectedLevel": "important",
            "suspectedImpacts": ["relationship"],
            "status": "journal-located",
            "confidence": "high",
            "journalVerified": True,
            "gameLogicVerified": False,
            "externalCorroborated": True,
            "inGameVerified": False,
            "notes": "test provenance",
        }

    def test_valid_stage_candidate_passes(self) -> None:
        self.assertEqual(validate_stage_candidates(self.write_lines([self.valid_item()])), [])

    def test_duplicate_objective_path_is_rejected(self) -> None:
        first = self.valid_item()
        second = self.valid_item() | {"id": "stage.test.2"}
        errors = validate_stage_candidates(self.write_lines([first, second]))
        self.assertTrue(any("duplicate objectivePath" in error for error in errors))

    def test_objective_must_belong_to_quest(self) -> None:
        item = self.valid_item() | {"objectivePath": "quests/side_quest/other/phase/objective"}
        errors = validate_stage_candidates(self.write_lines([item]))
        self.assertTrue(any("objectivePath must belong to questPath" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
