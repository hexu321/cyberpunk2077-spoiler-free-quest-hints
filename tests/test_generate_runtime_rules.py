from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.generate_runtime_rules import generate


class GenerateRuntimeRulesTests(unittest.TestCase):
    def write_payload(
        self,
        quest_impacts: list[dict],
        stage_hints: list[dict],
    ) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "hints.json"
        path.write_text(
            json.dumps(
                {
                    "schemaVersion": 2,
                    "questImpacts": quest_impacts,
                    "stageHints": stage_hints,
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        return path

    def test_quest_impacts_render_as_spoiler_free_labels(self) -> None:
        path = self.write_payload(
            [
                {
                    "id": "test.impact",
                    "questPath": "quests/example",
                    "impacts": ["relationship", "followup", "ending"],
                    "source": "test provenance",
                }
            ],
            [],
        )

        output = generate(path)
        self.assertIn('QOHPathMatches(questPath, "quests/example")', output)
        self.assertIn('return "人物关系 / 后续任务 / 结局条件";', output)

    def test_exact_stage_and_fallback_have_separate_lookup_functions(self) -> None:
        path = self.write_payload(
            [],
            [
                {
                    "id": "test.fallback",
                    "questPath": "quests/example",
                    "level": "important",
                    "label": "重要阶段",
                    "source": "test provenance",
                },
                {
                    "id": "test.exact",
                    "questPath": "quests/example",
                    "objectivePath": "quests/example/phase/objective",
                    "level": "critical",
                    "label": "关键节点 · 建议存档",
                    "source": "test provenance",
                },
            ],
        )

        output = generate(path)
        exact_position = output.index('QOHPathMatches(objectivePath, "quests/example/phase/objective")')
        fallback_function = output.index("public func QOHResolveQuestFallbackLabel")
        self.assertLess(exact_position, fallback_function)
        self.assertIn('return "关键节点 · 建议存档";', output)
        self.assertIn('return "重要阶段";', output)

    def test_disabled_and_none_entries_are_not_emitted(self) -> None:
        path = self.write_payload(
            [
                {
                    "id": "test.disabled-impact",
                    "questPath": "quests/disabled-impact",
                    "impacts": ["ending"],
                    "source": "test provenance",
                    "enabled": False,
                }
            ],
            [
                {
                    "id": "test.disabled-stage",
                    "questPath": "quests/disabled-stage",
                    "objectivePath": "quests/disabled-stage/phase/objective",
                    "level": "notice",
                    "label": "值得留意",
                    "source": "test provenance",
                    "enabled": False,
                },
                {
                    "id": "test.none",
                    "questPath": "quests/none",
                    "level": "none",
                    "label": "",
                    "source": "test provenance",
                },
            ],
        )

        output = generate(path)
        self.assertNotIn("quests/disabled-impact", output)
        self.assertNotIn("quests/disabled-stage", output)
        self.assertNotIn("quests/none", output)


if __name__ == "__main__":
    unittest.main()
