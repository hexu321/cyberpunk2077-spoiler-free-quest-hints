# Spoiler-Free Quest Hints v0.1.0-beta.1

First public beta release.

## Highlights

- Adds spoiler-free quest impact summaries to the native Journal quest list.
- Adds objective-level importance hints to Journal details.
- Mirrors the same quest and objective hints in the normal gameplay HUD quest tracker.
- Uses stable Journal paths instead of localized quest titles for rule matching.
- Ships only the six runtime redscript files in the installable package.
- Keeps story research, candidate data, validation tools, and third-party reference material out of the player-facing ZIP.

## Requirements

- Cyberpunk 2077 for PC.
- Tested baseline: Cyberpunk 2077 2.31 / 2.31a.
- redscript 0.5.31 or compatible.

## Install

Download `SpoilerFreeQuestHints-v0.1.0-beta.1.zip` from this release and either install the ZIP through Vortex or extract it directly into the Cyberpunk 2077 game root.

The archive starts with `r6/`, so the scripts land at:

`Cyberpunk 2077/r6/scripts/SpoilerFreeQuestHints/`

Do not use GitHub's auto-generated `Source code.zip` as the mod installer.

## Beta limitations

- The verified quest-rule database is still expanding.
- Some objective-specific rules still need additional save-state and branch verification.
- Current in-game hint labels are Chinese-only.
- Large Journal/HUD UI overhauls that modify the same controllers may require compatibility work.

This mod deliberately avoids telling the player what to choose or revealing outcomes. The hints describe importance only.
