#!/usr/bin/env python3
"""Find script files in server paths and save one random script."""

from __future__ import annotations

import argparse
import random
import shutil
from pathlib import Path

SCRIPT_EXTENSIONS = {".py", ".sh", ".bash", ".zsh", ".ps1", ".rb", ".pl"}


def find_scripts(server_paths: list[Path]) -> list[Path]:
    matches: list[Path] = []
    for server_path in server_paths:
        if not server_path.exists() or not server_path.is_dir():
            continue
        for path in server_path.rglob("*"):
            if path.is_file() and path.suffix.lower() in SCRIPT_EXTENSIONS:
                matches.append(path)
    return matches


def save_random_script(scripts: list[Path], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    selected = random.choice(scripts)
    destination = output_dir / selected.name
    counter = 1
    while destination.exists():
        destination = output_dir / f"{selected.stem}_{counter}{selected.suffix}"
        counter += 1
    shutil.copy2(selected, destination)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find script files in server directories and save one random script."
    )
    parser.add_argument(
        "--servers",
        nargs="+",
        required=True,
        help="One or more server directory paths to search.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where the random script will be copied.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    server_paths = [Path(path).expanduser() for path in args.servers]
    scripts = find_scripts(server_paths)
    if not scripts:
        print("No script files were found in the provided server paths.")
        return 1
    saved_path = save_random_script(scripts, Path(args.output_dir).expanduser())
    print(f"Saved random script to: {saved_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
