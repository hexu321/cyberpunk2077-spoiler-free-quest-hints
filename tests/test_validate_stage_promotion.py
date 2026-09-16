from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_stage_promotion import validate_stage_promotion


class ValidateStagePromotionTests(unittest.TestCase):
    def write_inputs(
        self,
        candidate: dict[str, object],
        stage_hint: dict[str, object] | None,
    ) -> tuple[Path, Path]:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        root = Path(tmpdir.name)
        candidates_path = root / "stage-candidates.jsonl"
        hints_path = root / "hints.json"
        candidates_path.write_text(
            json.dumps(candidate, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        hints_path.write_text(
            json.dumps(
                {
                    "schemaVersion": 2,
                    "questImpacts": [],
                    "stageHints": [] if stage_hint is None else [stage_hint],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        return candidates_path, hints_path

    def candidate(self, status: str = "journal-located") -> dict[str, object]:
        return {
            "id": "stage.test.choice",
            "questId": "sq_test",
            "questPath": "quests/side_quest/sq_test",
            "objectivePath": "quests/side_quest/sq_test/phase/choice",
            "objectiveDescription": "Talk to someone.",
            "suspectedLevel": "important",
            "suspectedImpacts": ["relationship"],
            "status": status,
            "confidence": "high",
            "journalVerified": True,
            "gameLogicVerified": False,
            "externalCorroborated": True,
            "inGameVerified": False,
            "notes": "test provenance",
        }

    def stage_hint(self) -> dict[str, object]:
        return {
            "id": "research.stage.test.choice",
            "questPath": "quests/side_quest/sq_test",
            "objectivePath": "quests/side_quest/sq_test/phase/choice",
            "level": "important",
            "label": "重要阶段",
            "source": "research/stage-candidates.jsonl",
        }

    def test_exact_promoted_stage_passes(self) -> None:
        paths = self.write_inputs(self.candidate(), self.stage_hint())
        self.assertEqual(validate_stage_promotion(*paths), [])

    def test_missing_eligible_stage_is_rejected(self) -> None:
        paths = self.write_inputs(self.candidate(), None)
        errors = validate_stage_promotion(*paths)
        self.assertTrue(any("not promoted" in error for error in errors))

    def test_wrong_objective_mount_is_rejected(self) -> None:
        stage_hint = self.stage_hint() | {
            "objectivePath": "quests/side_quest/sq_test/phase/other"
        }
        paths = self.write_inputs(self.candidate(), stage_hint)
        errors = validate_stage_promotion(*paths)
        self.assertTrue(any("not promoted" in error for error in errors))

    def test_runtime_id_must_trace_back_to_research_id(self) -> None:
        stage_hint = self.stage_hint() | {"id": "legacy.stage.name"}
        paths = self.write_inputs(self.candidate(), stage_hint)
        errors = validate_stage_promotion(*paths)
        self.assertTrue(any("one-to-one traceability" in error for error in errors))

    def test_unlocated_candidate_does_not_require_promotion(self) -> None:
        paths = self.write_inputs(self.candidate(status="source-verified"), None)
        self.assertEqual(validate_stage_promotion(*paths), [])


if __name__ == "__main__":
    unittest.main()
