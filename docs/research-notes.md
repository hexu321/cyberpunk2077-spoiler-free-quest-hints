# Research Notes

## Verified direction

### Journal state is the right source of truth

Current Cyberpunk 2077 quest-authoring documentation distinguishes Journal definition, lifecycle state, visited state, and tracked state. Objective activation/success is save-backed runtime state rather than a property that should be inferred from localized text.

That supports the project's core rule:

> resolve the hint from stable Journal quest/objective identity plus current runtime state, not from the text currently displayed on screen.

### Objective granularity is necessary

The game represents quest phases and objectives as distinct Journal entries. A single quest can activate and succeed multiple objectives over time while the quest itself remains the same. Therefore a permanent quest-level badge is insufficient for the desired UX.

### Native UI is feasible

Community redscript documentation supports hooking game UI controllers and traversing ink widget trees. `QuestTrackerGameController` is a documented hook point, but this project specifically wants the Journal menu rather than the HUD tracker, so the exact Journal controller/widget path still needs runtime inspection before implementation.

## 2026 reference baseline

Useful community baselines found during project setup:

- Cyberpunk 2077 2.31 / 2.31a
- RED4ext 1.30.0
- redscript 0.5.31
- WolvenKit 8.19.0 for resource-oriented quest work

These are research references, not a promise of compatibility with every later build.

## References

- Cyberpunk Modding Docs / REDscript UI scripting:
  https://github.com/CDPR-Modding-Documentation/Redscript-Wiki/tree/main/references-and-examples/ui-scripting
- REDscript hook examples:
  https://github.com/CDPR-Modding-Documentation/Redscript-Wiki/blob/main/getting-started/how-to-create-a-hook/things-to-hook.md
- Journal state and tracking research:
  https://hlky.github.io/cyberpunk-quest-authoring/journal/quest-state.html
- Journal / localization overview:
  https://hlky.github.io/cyberpunk-quest-authoring/journal/

## QuestGuide boundary

QuestGuide's public description is useful evidence that a native-style quest interface with live quest/objective state and controller support is practical. Its packaged code/assets are not a source for this repository.

Project rule: inspect behavior and public documentation for interoperability research; do not copy QuestGuide source/assets/package contents into this project.

## Next technical investigation

Before adding a production `.reds` UI hook:

1. Identify the Journal menu game controller used by the user's current installed game.
2. Inspect the widget tree while a quest detail page is open.
3. Identify the currently selected quest entry and active objective access path.
4. Prove a read-only test label can be inserted and removed without breaking controller navigation.
5. Prove the label refreshes when the objective changes inside the same quest.
6. Only then move the tested hook into `src/r6/scripts/SpoilerFreeQuestHints/`.

## Acceptance test for the first runtime build

Use one non-spoiler test rule on a disposable save:

- opening the target quest shows the label;
- advancing from objective A to B removes or changes it immediately;
- reopening Journal preserves correct state;
- changing language does not break matching;
- mouse and controller navigation remain unchanged;
- no label appears for unreached objectives.
