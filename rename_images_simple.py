#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple command-line entry point for batch file renaming."""

from __future__ import annotations

import argparse
from pathlib import Path

from i18n import DEFAULT_LANGUAGE, LANGUAGES, t
from rename_core import (
    RenameExecutionError,
    SUPPORTED_FORMATS,
    build_rename_plan,
    execute_rename_plan,
    list_supported_files,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch rename image and video files.")
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder to process. Defaults to the current folder.",
    )
    parser.add_argument(
        "--template",
        default="{n}",
        help="Name template. Use {n} for the number. Default: {n}",
    )
    parser.add_argument(
        "--start",
        default="1",
        help="Start number. Leading zeroes are preserved, e.g. 001.",
    )
    parser.add_argument(
        "--language",
        "--lang",
        choices=sorted(LANGUAGES),
        default=DEFAULT_LANGUAGE,
        help="Console language code. Default: en.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Rename without asking for confirmation.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    language = args.language
    folder = Path(args.folder)

    print("=" * 60)
    print(t(language, "cli_intro"))
    print("=" * 60)
    print(t(language, "cli_scan", folder=folder.absolute()))

    if not folder.exists() or not folder.is_dir():
        print(t(language, "folder_missing"))
        input(t(language, "cli_exit"))
        return 1

    files = list_supported_files(folder)
    print(t(language, "cli_found", count=len(files)))
    print(t(language, "supported_formats", formats=", ".join(sorted(SUPPORTED_FORMATS))))

    if not files:
        print(t(language, "no_supported_files"))
        input(t(language, "cli_exit"))
        return 0

    try:
        plan = build_rename_plan(files, args.template, args.start)
    except Exception as exc:
        print(t(language, "rename_error_log", error=exc))
        input(t(language, "cli_exit"))
        return 1

    print("-" * 60)
    for operation in plan[:10]:
        print(f"{operation.original.name} -> {operation.final.name}")
    if len(plan) > 10:
        print(t(language, "preview_more", count=len(plan) - 10))
    print("-" * 60)

    if not args.yes:
        answer = input(t(language, "cli_confirm")).strip().lower()
        if answer != "y":
            print(t(language, "cli_cancelled"))
            input(t(language, "cli_exit"))
            return 0

    def progress(phase, operation) -> None:
        if phase == "final":
            print(f"{operation.original.name} -> {operation.final.name}")

    try:
        count = execute_rename_plan(plan, progress=progress)
    except RenameExecutionError as exc:
        print(t(language, "rename_error_log", error=exc))
        if exc.rollback_errors:
            print(t(language, "rollback_errors_log", errors="; ".join(exc.rollback_errors)))
        input(t(language, "cli_exit"))
        return 1

    print(t(language, "cli_done", count=count))
    input(t(language, "cli_exit"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
