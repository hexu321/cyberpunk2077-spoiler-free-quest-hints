# Cyberpunk 2077 Spoiler-Free Quest Hints

[English](README.md) | [简体中文](README.zh-CN.md)

A lightweight redscript mod that adds **spoiler-free quest importance hints** to Cyberpunk 2077's native Journal and gameplay quest tracker.

Instead of telling you what to choose or revealing what will happen, the mod only warns you when the current quest or objective is worth paying closer attention to.

> **Warn without spoiling. Leave every decision to the player.**

Current release: **`v0.1.0-beta.2`**

[Download the latest release](https://github.com/hexu321/cyberpunk2077-spoiler-free-quest-hints/releases/tag/v0.1.0-beta.2)

## Screenshots

### Native Journal quest impact

The quest list can show a compact, spoiler-free impact summary such as relationship, follow-up quest, or ending relevance.

![Quest impact summary in the native Journal](docs/images/journal-quest-impact.png)

### Gameplay HUD quest impact and stage hint

The normal gameplay tracker can show both a quest-level impact summary and an objective-level importance hint without opening a separate guide window.

![Quest impact and objective hint in the gameplay HUD](docs/images/hud-quest-impact-and-stage-hint.png)

> The screenshots use the current Simplified Chinese in-game labels. The rule matching itself does not depend on the language of quest titles.

## Features

- **Native Journal integration** — quest impact summaries appear directly in the existing quest list.
- **Objective-level hints** — active objectives can be marked as `值得留意`, `重要阶段`, or `关键节点 · 建议存档`.
- **Gameplay HUD integration** — the same information can appear in the normal quest tracker while playing.
- **Spoiler-free by design** — no ending names, character outcomes, rewards, recommended dialogue choices, or "best" answers.
- **Stable Journal-path matching** — rules do not rely on localized quest-title text.
- **Conservative rules** — when the evidence is weak, the mod prefers showing nothing rather than guessing.
- **Controller-friendly** — no extra keyboard-only interaction is required.

## What the hints mean

| Level | In-game label | Meaning |
| --- | --- | --- |
| `none` | No hint | Ordinary progression; no extra warning. |
| `notice` | `值得留意` | This stage may have later consequences. |
| `important` | `重要阶段` | Pay closer attention to the current story/objective. |
| `critical` | `关键节点 · 建议存档` | Strong evidence of long-term impact, without revealing the outcome. |

Quest-level impact summaries can currently describe broad categories such as:

- `人物关系` — relationship impact;
- `后续任务` — follow-up quest impact;
- `结局条件` — ending-condition relevance.

These labels describe **importance**, not the "correct" choice.

## Requirements

- Cyberpunk 2077 for PC.
- Tested development baseline: Cyberpunk 2077 `2.31 / 2.31a`.
- `redscript` `0.5.31` or a compatible version, together with the dependencies required by your redscript installation.

The mod has no direct dependency on CET, Codeware, ArchiveXL, or TweakXL.

## Installation

Download the installable ZIP from the GitHub **Releases** page:

`SpoilerFreeQuestHints-v0.1.0-beta.2.zip`

Do **not** use GitHub's automatically generated `Source code.zip` as the mod installer.

The release archive is laid out from the Cyberpunk 2077 game root:

```text
r6/
└── scripts/
    └── SpoilerFreeQuestHints/
        ├── GeneratedRules.reds
        ├── HintResolver.reds
        ├── JournalPath.reds
        ├── JournalHintAdapter.reds
        ├── QuestListImpactAdapter.reds
        └── HudQuestTrackerAdapter.reds
```

### Vortex

1. Download `SpoilerFreeQuestHints-v0.1.0-beta.2.zip` from GitHub Releases.
2. Open Cyberpunk 2077 in Vortex.
3. Add the ZIP to the Mods page and install it.
4. Enable/deploy the mod if Vortex asks you to do so.
5. Launch the game normally.

Do not unpack the ZIP into an extra top-level folder before giving it to Vortex. The archive must start with `r6/`.

### Manual installation

1. Download `SpoilerFreeQuestHints-v0.1.0-beta.2.zip`.
2. Extract the archive directly into your Cyberpunk 2077 installation folder.
3. Confirm that the files end up here:

```text
Cyberpunk 2077/r6/scripts/SpoilerFreeQuestHints/
```

4. Launch the game normally. redscript will compile the scripts during startup.

## Uninstallation

Remove this directory from the game installation:

```text
Cyberpunk 2077/r6/scripts/SpoilerFreeQuestHints/
```

If you installed through Vortex, remove or disable the mod through Vortex and deploy the changes.

The mod does not intentionally write save-game data, so removing it should only remove the UI hints.

## Compatibility

The mod wraps native Journal and quest-tracker controllers rather than replacing the whole UI.

It should coexist with ordinary redscript mods, but another mod that heavily replaces or rewrites the same Journal / Quest Tracker controller behavior may conflict with it. If a UI overhaul changes those native controllers, compatibility should be tested separately.

Because matching uses stable Journal paths, the rules do not depend on whether the player's quest titles are displayed in Chinese or English.

## Known limitations

This is a beta release.

- The verified rule database is still expanding; not every consequential quest or objective is covered yet.
- Not every exact objective rule has been replayed against every possible save-state or quest branch.
- The current in-game hint labels are Simplified Chinese only. Additional localization is planned separately.
- UI overhauls that modify the same Journal or HUD quest-tracker controllers may require compatibility work.
- The mod deliberately avoids guessing when evidence for a quest consequence is weak, so some important moments may remain unlabelled until verified.

## Spoiler policy

The project intentionally does **not** display:

- ending names;
- who lives or dies;
- character outcomes;
- rewards;
- faction outcomes;
- recommended dialogue choices;
- "best" or "correct" options.

The UI only exposes the importance level for story content the player has already reached.

See [`docs/spoiler-policy.md`](docs/spoiler-policy.md) for the project policy.

For adding or modifying quest-level and objective-level rules, see [`docs/quest-rule-maintenance.zh-CN.md`](docs/quest-rule-maintenance.zh-CN.md) (Chinese maintainer guide).

## Development status

`v0.1.0-beta.2` expands reviewed runtime rule coverage and fixes research-to-UI promotion gaps found after the first public beta.

Already verified in the real game environment:

- Journal quest-list impact summaries;
- Journal objective importance labels;
- HUD quest-title impact summaries;
- HUD objective importance labels;
- stable Journal-path matching;
- offline rule validation and generated runtime rules.

Ongoing work focuses on expanding and manually reviewing the real quest-rule database.

## Repository structure

```text
data/
  hints.json                       # Manually reviewed production rules
  hints.schema.json                # Rule constraints
  hints.example.json               # Spoiler-free example data

docs/
  images/                          # In-game screenshots used by the README
  architecture.md                  # Runtime architecture
  spoiler-policy.md                # Content/spoiler policy
  research-notes.md                # Verified research notes

research/
  candidates.jsonl                 # Candidate consequence research queue
  cases/                           # Per-quest investigation records
  sources/                         # Normalized research sources

tools/
  validate_hints.py                # Production-rule validation
  generate_runtime_rules.py        # JSON -> GeneratedRules.reds
  validate_research_candidates.py  # Research-candidate validation
  validate_stage_candidates.py     # Stage-candidate validation
  build_release.py                 # Builds the installable release ZIP

src/
  r6/scripts/SpoilerFreeQuestHints/
    GeneratedRules.reds
    HintResolver.reds
    JournalHintAdapter.reds
    QuestListImpactAdapter.reds
    HudQuestTrackerAdapter.reds
    JournalPath.reds
```

## Development principles

1. Verify the game API before adding hooks.
2. Every `critical` rule should have a source and human review record.
3. Production data must not contain recommended choices, ending names, or direct outcome spoilers.
4. UI hints only describe the current quest/objective the player has reached.
5. Future locked story content must not be scanned and exposed to the player.
6. QuestGuide may be studied as an API/interaction reference, but its source, assets, and package files are not copied into this project.

## Building the release ZIP

From the repository root:

```bash
python tools/build_release.py
```

The installable archive is written to:

```text
dist/SpoilerFreeQuestHints-v0.1.0-beta.2.zip
```

`dist/` is intentionally ignored by Git.
