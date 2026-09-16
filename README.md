# Cyberpunk 2077 Spoiler-Free Quest Hints

A lightweight redscript mod that adds **spoiler-free importance hints** to Cyberpunk 2077's native Journal and quest tracker.

Instead of telling you what to choose or what will happen, the mod only tells you when a quest or objective is worth paying closer attention to.

Current in-game hints include:

- Quest-level impact summaries such as `影响：人物关系 / 后续任务 / 结局条件`.
- Objective-level labels such as `值得留意`, `重要阶段`, and `关键节点 · 建议存档`.
- Matching hints in both the native Journal UI and the normal gameplay HUD quest tracker.
- Stable Journal-path matching instead of relying on localized quest titles.

The goal is simple: **warn without spoiling, and leave every decision to the player.**

## Screenshots

A clean public-facing screenshot is not committed yet. The current build has already been verified in-game, but this first beta is intentionally being published without fabricated or third-party screenshots. A real gameplay screenshot will be added here after capture from the verified build.

## Requirements

- Cyberpunk 2077 for PC.
- Tested development baseline: Cyberpunk 2077 `2.31 / 2.31a`.
- `redscript` `0.5.31` or a compatible version, together with the dependencies required by your redscript installation.

The mod has no direct dependency on CET, Codeware, ArchiveXL, or TweakXL.

## Installation

Download the installable ZIP from the GitHub **Releases** page:

`SpoilerFreeQuestHints-v0.1.0-beta.1.zip`

Do **not** use GitHub's automatically generated `Source code.zip` as the mod installer.

The release package is laid out from the Cyberpunk 2077 game root:

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

## Vortex Installation

1. Download `SpoilerFreeQuestHints-v0.1.0-beta.1.zip` from GitHub Releases.
2. Open Cyberpunk 2077 in Vortex.
3. Add the downloaded ZIP to the Mods page, then install it.
4. Enable/deploy the mod if Vortex asks you to do so.
5. Launch the game normally.

Do not unpack the ZIP into an extra top-level folder before giving it to Vortex. The archive must start with `r6/`.

## Manual Installation

1. Download `SpoilerFreeQuestHints-v0.1.0-beta.1.zip`.
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

## Known Limitations

This is a beta release.

- The verified rule database is still expanding; not every consequential quest or objective is covered yet.
- Not every exact objective rule has been replayed against every possible save-state or quest branch.
- The current hint labels are Chinese-only. Localization is planned separately.
- UI overhauls that modify the same Journal or HUD quest-tracker controllers may require compatibility work.
- The mod deliberately avoids guessing when evidence for a quest consequence is weak, so some important moments may remain unlabelled until verified.

## Hint Levels

| Level | Display | Meaning |
| --- | --- | --- |
| `none` | No hint | Ordinary progression; no extra warning. |
| `notice` | `值得留意` | This stage may have later consequences. |
| `important` | `重要阶段` | Pay attention to the current story/objective. |
| `critical` | `关键节点 · 建议存档` | Strong evidence of long-term impact, without revealing the outcome. |

These labels describe **importance**, not the "correct" choice.

## Spoiler Policy

The project intentionally does not display:

- ending names;
- who lives or dies;
- character outcomes;
- rewards;
- faction outcomes;
- recommended dialogue choices;
- "best" or "correct" options.

The UI only exposes the importance level for story content the player has already reached.

## Development Status

`v0.1.0-beta.1` is the first public beta candidate.

Already verified in the real game environment:

- Journal quest-list impact summaries.
- Journal objective importance labels.
- HUD quest-title impact summaries.
- HUD objective importance labels.
- Stable Journal-path matching.
- Offline rule validation and generated runtime rules.

Ongoing work focuses on expanding and manually reviewing the real quest-rule database.

## Repository Structure

```text
data/
  hints.json                       # Manually reviewed production rules
  hints.schema.json                # Rule constraints
  hints.example.json               # Spoiler-free example data

docs/
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

## Development Principles

1. Verify the game API before adding hooks.
2. Every `critical` rule should have a source and human review record.
3. Production data must not contain recommended choices, ending names, or direct outcome spoilers.
4. UI hints only describe the current quest/objective the player has reached.
5. Future locked story content must not be scanned and exposed to the player.
6. QuestGuide may be studied as an API/interaction reference, but its source, assets, and package files are not copied into this project.

## Building the Release ZIP

From the repository root:

```bash
python tools/build_release.py
```

The installable archive is written to:

```text
dist/SpoilerFreeQuestHints-v0.1.0-beta.1.zip
```

`dist/` is intentionally ignored by Git.
