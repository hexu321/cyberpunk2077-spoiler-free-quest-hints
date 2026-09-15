from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_research_candidates import validate_candidates


class ValidateResearchCandidatesTests(unittest.TestCase):
    def write_lines(self, entries: list[dict]) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "candidates.jsonl"
        path.write_text(
            "\n".join(json.dumps(entry, ensure_ascii=False) for entry in entries) + "\n",
            encoding="utf-8",
        )
        return path

    def valid_entry(self) -> dict:
        return {
            "id": "test.quest",
            "questId": "sq_test",
            "questPath": "quests/side_quest/sq_test",
            "title": "Test Quest",
            "suspectedImpacts": ["relationship", "ending"],
            "status": "candidate",
            "confidence": "seed",
            "seedSource": "test source",
            "sourceRef": "test ref",
            "needsObjectiveResearch": True,
            "journalVerified": True,
            "gameLogicVerified": False,
            "externalCorroborated": False,
            "inGameVerified": False,
            "lastVerifiedGameVersion": None,
            "notes": "test note",
        }

    def test_valid_candidate_passes(self) -> None:
        self.assertEqual(validate_candidates(self.write_lines([self.valid_entry()])), [])

    def test_duplicate_quest_id_is_rejected(self) -> None:
        first = self.valid_entry()
        second = self.valid_entry()
        second["id"] = "test.quest.two"
        errors = validate_candidates(self.write_lines([first, second]))
        self.assertTrue(any("duplicate questId" in error for error in errors))

    def test_invalid_status_is_rejected(self) -> None:
        entry = self.valid_entry()
        entry["status"] = "unknown"
        errors = validate_candidates(self.write_lines([entry]))
        self.assertTrue(any("invalid status" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
