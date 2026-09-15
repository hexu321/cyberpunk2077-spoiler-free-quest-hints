from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.generate_runtime_rules import generate


class GenerateRuntimeRulesTests(unittest.TestCase):
    def write_payload(self, rules: list[dict]) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "hints.json"
        path.write_text(
            json.dumps({"schemaVersion": 1, "rules": rules}, ensure_ascii=False),
            encoding="utf-8",
        )
        return path

    def test_exact_rule_beats_fallback_by_separate_lookup(self) -> None:
        path = self.write_payload(
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
            ]
        )

        output = generate(path)
        exact_position = output.index('Equals(objectivePath, "quests/example/phase/objective")')
        fallback_position = output.index('Equals(questPath, "quests/example")')
        self.assertLess(exact_position, fallback_position)
        self.assertIn('return "关键节点 · 建议存档";', output)
        self.assertIn('return "重要阶段";', output)

    def test_disabled_and_none_rules_are_not_emitted(self) -> None:
        path = self.write_payload(
            [
                {
                    "id": "test.disabled",
                    "questPath": "quests/disabled",
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
            ]
        )

        output = generate(path)
        self.assertNotIn("quests/disabled", output)
        self.assertNotIn("quests/none", output)


if __name__ == "__main__":
    unittest.main()
