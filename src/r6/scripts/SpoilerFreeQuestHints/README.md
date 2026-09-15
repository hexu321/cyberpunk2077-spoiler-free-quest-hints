# Runtime implementation boundary

This directory contains the tested redscript runtime implementation.

Runtime responsibilities are intentionally split:

1. `JournalPath.reds`
   - builds stable Journal paths from live entries;
   - walks parents to find the owning `JournalQuest`.

2. `GeneratedRules.reds`
   - generated from `data/hints.json`;
   - contains no widget/controller knowledge;
   - resolves quest impact labels and stage labels by stable Journal path.

3. `HintResolver.reds`
   - resolves broad quest impacts separately from stage importance;
   - exact objective match first;
   - optional stage fallback second;
   - ignores non-active objectives.

4. `QuestListImpactAdapter.reds`
   - wraps the native Journal quest list item;
   - appends `影响：...` only when a quest impact rule exists;
   - leaves the original gray objective summary untouched.

5. `JournalHintAdapter.reds`
   - wraps the native Journal details objective controller;
   - appends a stage label only when the current active objective matches a rule.

6. `HudQuestTrackerAdapter.reds`
   - mirrors the same quest-impact and stage-hint behavior in the normal gameplay quest tracker.

The UI adapters must not contain story classifications. The rules database must not contain widget/controller knowledge.

QuestGuide source may be inspected locally as an API/architecture reference, but its source and assets are not copied into this project.
