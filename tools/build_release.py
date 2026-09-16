from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path


VERSION = "v0.1.0-beta.2"
PACKAGE_NAME = f"SpoilerFreeQuestHints-{VERSION}.zip"
RUNTIME_FILES = (
    "GeneratedRules.reds",
    "HintResolver.reds",
    "JournalPath.reds",
    "JournalHintAdapter.reds",
    "QuestListImpactAdapter.reds",
    "HudQuestTrackerAdapter.reds",
)


def build_release(repo_root: Path, output_dir: Path) -> Path:
    source_dir = repo_root / "src" / "r6" / "scripts" / "SpoilerFreeQuestHints"
    missing = [name for name in RUNTIME_FILES if not (source_dir / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing runtime files: {', '.join(missing)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / PACKAGE_NAME

    with tempfile.TemporaryDirectory(prefix="spoiler-free-quest-hints-") as temp_dir:
        package_root = Path(temp_dir)
        runtime_dir = package_root / "r6" / "scripts" / "SpoilerFreeQuestHints"
        runtime_dir.mkdir(parents=True)

        for name in RUNTIME_FILES:
            shutil.copy2(source_dir / name, runtime_dir / name)

        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package_root.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(package_root))

    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the installable Cyberpunk 2077 mod ZIP.")
    parser.add_argument("--output-dir", default="dist", help="Directory for the release ZIP.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    output_path = build_release(repo_root, repo_root / args.output_dir)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
