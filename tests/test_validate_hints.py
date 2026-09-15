from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_hints import validate_document


class ValidateHintsTests(unittest.TestCase):
    def write_payload(self, payload: dict) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "hints.json"
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        return path

    def valid_payload(self) -> dict:
        return {
            "schemaVersion": 2,
            "questImpacts": [
                {
                    "id": "test.impact",
                    "questPath": "quests/example",
                    "impacts": ["relationship", "followup"],
                    "source": "test provenance",
                }
            ],
            "stageHints": [
                {
                    "id": "test.notice",
                    "questPath": "quests/example",
                    "objectivePath": "quests/example/phase/objective",
                    "level": "notice",
                    "label": "值得留意",
                    "source": "test provenance",
                }
            ],
        }

    def test_valid_document_passes(self) -> None:
        path = self.write_payload(self.valid_payload())
        self.assertEqual(validate_document(path), [])

    def test_spoiler_prone_key_is_rejected(self) -> None:
        payload = self.valid_payload()
        payload["stageHints"][0]["endingName"] = "do not ship this"
        path = self.write_payload(payload)
        errors = validate_document(path)
        self.assertTrue(any("forbidden" in error or "unsupported" in error for error in errors))

    def test_duplicate_id_across_sections_is_rejected(self) -> None:
        payload = self.valid_payload()
        payload["stageHints"][0]["id"] = payload["questImpacts"][0]["id"]
        path = self.write_payload(payload)
        errors = validate_document(path)
        self.assertTrue(any("duplicates" in error for error in errors))

    def test_invalid_impact_is_rejected(self) -> None:
        payload = self.valid_payload()
        payload["questImpacts"][0]["impacts"] = ["relationship", "reward"]
        path = self.write_payload(payload)
        errors = validate_document(path)
        self.assertTrue(any("unsupported values" in error for error in errors))

    def test_objective_path_must_belong_to_quest(self) -> None:
        payload = self.valid_payload()
        payload["stageHints"][0]["objectivePath"] = "quests/other/phase/objective"
        path = self.write_payload(payload)
        errors = validate_document(path)
        self.assertTrue(any("inside its questPath" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
