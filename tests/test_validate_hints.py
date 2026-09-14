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

    def test_valid_rule_passes(self) -> None:
        path = self.write_payload(
            {
                "schemaVersion": 1,
                "rules": [
                    {
                        "id": "test.notice",
                        "questPath": "quests/example",
                        "objectivePath": "quests/example/objective",
                        "level": "notice",
                        "label": "值得留意",
                        "source": "test provenance",
                        "enabled": True,
                    }
                ],
            }
        )
        self.assertEqual(validate_document(path), [])

    def test_spoiler_prone_key_is_rejected(self) -> None:
        path = self.write_payload(
            {
                "schemaVersion": 1,
                "rules": [
                    {
                        "id": "test.bad",
                        "questPath": "quests/example",
                        "level": "critical",
                        "label": "关键节点 · 建议存档",
                        "source": "test provenance",
                        "endingName": "do not ship this",
                    }
                ],
            }
        )
        errors = validate_document(path)
        self.assertTrue(any("forbidden" in error or "unsupported" in error for error in errors))

    def test_duplicate_rule_id_is_rejected(self) -> None:
        rule = {
            "id": "test.duplicate",
            "questPath": "quests/example",
            "level": "important",
            "label": "重要阶段",
            "source": "test provenance",
        }
        path = self.write_payload({"schemaVersion": 1, "rules": [rule, dict(rule)]})
        errors = validate_document(path)
        self.assertTrue(any("duplicates" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
