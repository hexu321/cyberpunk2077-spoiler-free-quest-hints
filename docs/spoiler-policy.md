# Spoiler Policy

## Purpose

The project is allowed to reveal **importance**, not **outcome**.

A player should learn only whether the current stage deserves extra attention. They should not be able to infer the correct option, the ending branch, a character's fate, or the reward from the hint itself.

## Allowed labels

Preferred labels are deliberately generic:

- `值得留意`
- `重要阶段`
- `关键节点 · 建议存档`

Equivalent translations may be added later, but they must preserve the same low-information character.

## Forbidden player-facing content

Do not include any of the following in a displayed hint:

- ending names;
- names of future quests that have not appeared yet;
- who lives, dies, leaves, stays, romances, betrays, or becomes unavailable;
- specific rewards, weapons, vehicles, achievements, or unlocks;
- the exact dialogue line to choose;
- `choose A`, `refuse B`, `call C`, `wait five minutes`, or similar prescriptive instructions;
- faction / relationship result descriptions;
- explicit statements such as `this changes the ending` when a lower-information label can communicate importance.

## Internal source notes

Maintainer-only provenance may contain enough detail to verify a rule, but it must not be compiled into the player-facing payload.

Where possible, keep verification references separate from the shipped runtime data.

## Classification rules

### none

Use when there is no evidence that the current stage needs special attention.

### notice

Use when a stage may have durable side effects or optional follow-up relevance, but interrupting the player's flow would be excessive.

### important

Use when the player should reasonably pay attention because the stage can materially affect later content, access, relationships, or branching.

### critical

Reserve for a narrow set of stages with strong evidence of substantial long-term branching. The UI should still say only `关键节点 · 建议存档`.

## Anti-overwarning rule

If too many objectives are marked important, the system becomes a spoiler by implication and the labels lose meaning. Prefer false negatives over speculative warnings.

## Future-content rule

Never resolve or display rules for objectives the player has not reached. The resolver may know the database, but the UI receives only the current selected/active objective result.

## Recommendation neutrality

The project never defines a `best`, `good`, `bad`, or `canon` option. Its job is to protect player agency, not replace it.
