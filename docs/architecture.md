# Architecture

## 1. Product behavior

The runtime answers two spoiler-safe questions:

1. For the current quest, what broad impact categories are known (`人物关系 / 后续任务 / 结局条件`)?
2. For the current active objective, should the UI show an importance hint?

It must not answer what the concrete consequence is or which choice is preferred.

## 2. Runtime data flow

```text
Game Journal runtime state
        |
        v
Current quest + current active objective
        |
        +--> Quest impact resolver --> 人物关系 / 后续任务 / 结局条件
        |
        +--> Stage hint resolver
               exact objective rule
                    |
                    +--> optional quest-level fallback
                    |
                    v
               none / notice / important / critical
        |
        v
Native Journal + HUD adapters
```

The resolver and the UI adapter are intentionally separate. A future game patch may rename or restructure UI controllers without invalidating the rules database.

## 3. Rule identity

A rule should prefer stable Journal identity rather than localized display strings.

The source data is split into two rule families.

Quest-level impact example:

```json
{
  "id": "unique-impact-id",
  "questPath": "stable journal quest path",
  "impacts": ["relationship", "followup"],
  "source": "human-reviewed provenance note"
}
```

Objective-level stage hint example:

```json
{
  "id": "unique-stage-id",
  "questPath": "stable journal quest path",
  "objectivePath": "stable journal objective path",
  "level": "important",
  "label": "重要阶段",
  "source": "human-reviewed provenance note"
}
```

`objectivePath` may be omitted only for an explicitly documented stage fallback. Exact objective matches always win over fallback stage rules. A quest impact rule never automatically makes every objective important.

Do not key rules by the Chinese or English quest title: localization and display text are presentation, not identity.

## 4. Objective-aware behavior

A large job can transition through many objectives while remaining the same quest. Therefore the UI adapter must refresh when at least one of these changes:

- selected Journal quest;
- active/tracked objective state;
- objective lifecycle state;
- Journal menu selection / detail panel refresh.

The core requirement is that a hint for objective A must disappear when the player advances to objective B unless B has its own rule or an allowed quest fallback.

## 5. UI target

Verified targets:

```text
JOURNAL LIST
  Quest title  影响：人物关系 / 后续任务
  Original gray objective summary

JOURNAL DETAILS
  Current objective  [重要阶段]

GAMEPLAY HUD
  Quest title  影响：人物关系 / 后续任务
  Current objective  [重要阶段]
```

Presentation requirements:

- one short line;
- visually secondary to the quest title;
- controller requires no extra focus target;
- no popup on objective change;
- no audio cue;
- no future objective list;
- hide completely for `none`.

If direct Journal injection proves unstable, the fallback is a small read-only line in the quest detail area, not a separate CET overlay.

## 6. Dependencies

Preferred minimal runtime dependency:

- redscript;
- dependencies already transitively required by a verified native UI implementation only when necessary.

Do not introduce CET solely for configuration or JSON loading if a small redscript-native implementation can satisfy the feature.

## 7. Data strategy

The first production ruleset should be curated offline and compiled/shipped with the mod. Runtime AI inference is explicitly out of scope because it can hallucinate importance, leak spoilers, and behave inconsistently across languages.

The source rules live under `data/` and are validated before they are transformed into runtime data.

## 8. Validation gates

A rule can ship only when all are true:

1. Journal identity is verified against the target game version.
2. A quest impact uses only the approved broad categories and does not reveal the concrete outcome.
3. A stage hint is tied to the narrowest useful objective/phase whenever possible.
4. The displayed label contains no consequence information.
5. The source note is sufficient for a maintainer to re-check the classification.
6. A save-state test confirms exact stage badges appear only while the intended objective is current.

A `critical` stage rule additionally requires manual review by a second pass before release.

## 9. Compatibility strategy

The UI integration should be isolated in one adapter module. No rule file should depend on concrete widget names or controller fields.

When a game patch breaks the Journal UI, compatibility work should normally touch only:

```text
Journal adapter -> widget lookup / refresh hook
```

not:

```text
rule semantics -> spoiler policy -> curated classifications
```

## 10. QuestGuide boundary

QuestGuide demonstrates that a native-UI quest tool can expose live quest/objective state and controller-friendly interaction. This project does not copy QuestGuide source, assets, labels, or packaged files. It independently implements a narrower spoiler-free hint use case.
