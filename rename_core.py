#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Core rename logic shared by the GUI and command-line entry points."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable
import uuid


IMAGE_FORMATS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
    ".svg",
    ".ico",
}

VIDEO_FORMATS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".wmv",
    ".flv",
    ".m4v",
    ".mpg",
    ".mpeg",
    ".3gp",
    ".webm",
}

SUPPORTED_FORMATS = IMAGE_FORMATS | VIDEO_FORMATS
INVALID_FILENAME_CHARS = set('<>:"/\\|?*\0')


@dataclass(frozen=True)
class RenameOperation:
    original: Path
    temp: Path
    final: Path


class RenameExecutionError(RuntimeError):
    """Raised when execution fails after attempting rollback."""

    def __init__(self, message: str, rollback_errors: list[str] | None = None):
        super().__init__(message)
        self.rollback_errors = rollback_errors or []


def path_key(path: Path) -> str:
    """Use a case-folded absolute key to avoid Windows/macOS collisions."""
    return str(path.absolute()).casefold()


def list_supported_files(folder: Path) -> list[Path]:
    files = [
        file_path
        for file_path in folder.iterdir()
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_FORMATS
    ]
    return sorted(files, key=lambda item: item.name.casefold())


def parse_start_number(value: str) -> tuple[int, int]:
    stripped = value.strip()
    if not stripped.isdigit():
        raise ValueError("Start number must be a non-negative integer.")

    start_number = int(stripped)
    width = len(stripped) if len(stripped) > 1 and stripped.startswith("0") else 0
    return start_number, width


def validate_template(template: str) -> str:
    cleaned = template.strip()
    if not cleaned:
        raise ValueError("Template cannot be empty.")

    bad_chars = sorted(char for char in INVALID_FILENAME_CHARS if char in cleaned)
    if bad_chars:
        visible = ", ".join(repr(char) for char in bad_chars)
        raise ValueError(f"Template contains characters that are unsafe in file names: {visible}")

    return cleaned


def format_index(index: int, width: int) -> str:
    return str(index).zfill(width) if width else str(index)


def generate_new_name(template: str, index: int, suffix: str, width: int = 0) -> str:
    number = format_index(index, width)
    stem = template.replace("{n}", number) if "{n}" in template else f"{template}{number}"
    return f"{stem}{suffix}"


def build_rename_plan(
    files: Iterable[Path],
    template: str = "{n}",
    start_number: str = "1",
) -> list[RenameOperation]:
    file_list = list(files)
    template = validate_template(template)
    start_index, width = parse_start_number(start_number)

    selected_paths = {path_key(path) for path in file_list}
    planned_targets: set[str] = set()
    temp_prefix = f".__batch_rename_{uuid.uuid4().hex}_"
    operations: list[RenameOperation] = []

    for offset, original in enumerate(file_list):
        final_name = generate_new_name(template, start_index + offset, original.suffix, width)
        final_path = original.parent / final_name
        final_key = path_key(final_path)

        if final_key in planned_targets:
            raise ValueError(f"Multiple files would be renamed to the same target: {final_name}")

        if final_path.exists() and final_key not in selected_paths:
            raise FileExistsError(f"Target already exists and is not part of this batch: {final_name}")

        temp_path = original.parent / f"{temp_prefix}{offset + 1:06d}{original.suffix}"
        while temp_path.exists():
            temp_prefix = f".__batch_rename_{uuid.uuid4().hex}_"
            temp_path = original.parent / f"{temp_prefix}{offset + 1:06d}{original.suffix}"

        planned_targets.add(final_key)
        operations.append(RenameOperation(original=original, temp=temp_path, final=final_path))

    return operations


def rollback_operations(operations: Iterable[RenameOperation]) -> list[str]:
    errors: list[str] = []
    operation_list = list(operations)

    for operation in reversed(operation_list):
        try:
            if operation.final.exists() and not operation.temp.exists():
                operation.final.rename(operation.temp)
        except Exception as exc:  # pragma: no cover - depends on filesystem state
            errors.append(f"{operation.final.name} -> {operation.temp.name}: {exc}")

    for operation in reversed(operation_list):
        try:
            if operation.temp.exists():
                if operation.original.exists():
                    errors.append(f"Cannot restore {operation.original.name}: target already exists")
                    continue
                operation.temp.rename(operation.original)
        except Exception as exc:  # pragma: no cover - depends on filesystem state
            errors.append(f"{operation.temp.name} -> {operation.original.name}: {exc}")

    return errors


def execute_rename_plan(
    operations: list[RenameOperation],
    progress: Callable[[str, RenameOperation], None] | None = None,
) -> int:
    temp_moved: list[RenameOperation] = []

    try:
        for operation in operations:
            operation.original.rename(operation.temp)
            temp_moved.append(operation)
            if progress:
                progress("temp", operation)

        for operation in operations:
            operation.temp.rename(operation.final)
            if progress:
                progress("final", operation)

    except Exception as exc:
        rollback_errors = rollback_operations(temp_moved)
        raise RenameExecutionError(str(exc), rollback_errors) from exc

    return len(operations)
