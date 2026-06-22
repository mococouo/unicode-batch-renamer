#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Multilingual GUI for batch-renaming image and video files."""

from __future__ import annotations

from pathlib import Path
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import font as tkfont

from i18n import DEFAULT_LANGUAGE, LANGUAGES, t
from rename_core import (
    RenameExecutionError,
    SUPPORTED_FORMATS,
    build_rename_plan,
    execute_rename_plan,
    list_supported_files,
    parse_start_number,
    validate_template,
)


class BatchRenameGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.language = DEFAULT_LANGUAGE
        self.localized_widgets: list[tuple[tk.Widget, str, str]] = []

        self.folder_path = tk.StringVar()
        self.name_template = tk.StringVar(value="{n}")
        self.start_number = tk.StringVar(value="1")
        self.language_name = tk.StringVar(value=LANGUAGES[self.language])

        self.all_files: list[Path] = []
        self.filtered_files: list[Path] = []

        self.create_widgets()
        self.apply_language()

    def tr(self, key: str, **kwargs) -> str:
        return t(self.language, key, **kwargs)

    def create_widgets(self) -> None:
        self.root.geometry("780x650")
        self.root.minsize(720, 560)
        self.root.resizable(True, True)

        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        heading_font = default_font.copy()
        heading_font.configure(size=18, weight="bold")

        top_frame = ttk.Frame(self.root, padding=(20, 16, 20, 8))
        top_frame.pack(fill="x")

        self.title_label = ttk.Label(top_frame, font=heading_font)
        self.title_label.pack(side="left", anchor="w")
        self.bind_text(self.title_label, "main_title")

        language_frame = ttk.Frame(top_frame)
        language_frame.pack(side="right", anchor="e")
        self.language_label = ttk.Label(language_frame)
        self.language_label.pack(side="left", padx=(0, 8))
        self.bind_text(self.language_label, "language_label")

        self.language_combo = ttk.Combobox(
            language_frame,
            textvariable=self.language_name,
            values=list(LANGUAGES.values()),
            state="readonly",
            width=14,
        )
        self.language_combo.pack(side="left")
        self.language_combo.bind("<<ComboboxSelected>>", self.change_language)

        self.folder_frame = ttk.LabelFrame(self.root, padding=12)
        self.folder_frame.pack(pady=8, padx=20, fill="x")
        self.bind_text(self.folder_frame, "folder_frame")

        self.folder_help_label = ttk.Label(self.folder_frame)
        self.folder_help_label.pack(anchor="w")
        self.bind_text(self.folder_help_label, "folder_help")

        path_frame = ttk.Frame(self.folder_frame)
        path_frame.pack(fill="x", pady=(6, 0))
        self.path_entry = ttk.Entry(path_frame, textvariable=self.folder_path)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.browse_button = ttk.Button(path_frame, command=self.browse_folder, width=12)
        self.browse_button.pack(side="right")
        self.bind_text(self.browse_button, "browse")

        self.template_frame = ttk.LabelFrame(self.root, padding=12)
        self.template_frame.pack(pady=8, padx=20, fill="x")
        self.bind_text(self.template_frame, "template_frame")

        input_frame = ttk.Frame(self.template_frame)
        input_frame.pack(fill="x")

        self.template_label = ttk.Label(input_frame)
        self.template_label.pack(side="left")
        self.bind_text(self.template_label, "template_label")

        self.template_entry = ttk.Entry(input_frame, textvariable=self.name_template, width=34)
        self.template_entry.pack(side="left", padx=(8, 18))

        self.start_label = ttk.Label(input_frame)
        self.start_label.pack(side="left")
        self.bind_text(self.start_label, "start_label")

        self.number_entry = ttk.Entry(input_frame, textvariable=self.start_number, width=8)
        self.number_entry.pack(side="left", padx=(8, 18))

        self.preview_button = ttk.Button(input_frame, command=self.preview_rename, width=12)
        self.preview_button.pack(side="left")
        self.bind_text(self.preview_button, "preview")

        self.examples_label = ttk.Label(self.template_frame, justify="left", wraplength=700)
        self.examples_label.pack(anchor="w", pady=(10, 0))
        self.bind_text(self.examples_label, "examples_text")

        self.preview_frame = ttk.LabelFrame(self.root, padding=10)
        self.preview_frame.pack(pady=8, padx=20, fill="both", expand=True)
        self.bind_text(self.preview_frame, "preview_frame")

        text_frame = ttk.Frame(self.preview_frame)
        text_frame.pack(fill="both", expand=True)
        text_font = tkfont.nametofont("TkFixedFont").copy()
        text_font.configure(size=9)
        self.preview_text = tk.Text(text_frame, height=12, wrap="word", font=text_font)
        self.preview_text.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(text_frame, command=self.preview_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.preview_text.config(yscrollcommand=scrollbar.set)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=(8, 14))
        self.scan_button = ttk.Button(button_frame, command=self.scan_files, width=16)
        self.scan_button.pack(side="left", padx=6)
        self.bind_text(self.scan_button, "scan")

        self.rename_button = ttk.Button(
            button_frame,
            command=self.start_rename,
            width=16,
            state="disabled",
        )
        self.rename_button.pack(side="left", padx=6)
        self.bind_text(self.rename_button, "rename")

        self.progress = ttk.Progressbar(self.root, mode="indeterminate")

        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x")

    def bind_text(self, widget: tk.Widget, key: str, option: str = "text") -> None:
        self.localized_widgets.append((widget, option, key))

    def apply_language(self) -> None:
        self.root.title(self.tr("app_title"))
        for widget, option, key in self.localized_widgets:
            widget.configure(**{option: self.tr(key)})

        if self.filtered_files:
            self.status_var.set(self.tr("status_found", count=len(self.filtered_files)))
            self.render_preview()
        else:
            self.status_var.set(self.tr("status_ready"))

    def change_language(self, _event=None) -> None:
        selected = self.language_name.get()
        for code, label in LANGUAGES.items():
            if label == selected:
                self.language = code
                break
        self.apply_language()

    def browse_folder(self) -> None:
        folder = filedialog.askdirectory(title=self.tr("select_folder_dialog"))
        if folder:
            self.folder_path.set(folder)
            self.scan_files()

    def log(self, message: str = "") -> None:
        self.preview_text.insert("end", message + "\n")
        self.preview_text.see("end")

    def clear_log(self) -> None:
        self.preview_text.delete("1.0", "end")

    def warn(self, key: str) -> None:
        messagebox.showwarning(self.tr("warning_title"), self.tr(key))

    def scan_files(self) -> None:
        folder = self.folder_path.get().strip()
        if not folder:
            self.warn("no_folder")
            return

        folder_path = Path(folder)
        if not folder_path.exists() or not folder_path.is_dir():
            messagebox.showerror(self.tr("error_title"), self.tr("folder_missing"))
            return

        self.all_files = [file_path for file_path in folder_path.iterdir() if file_path.is_file()]
        self.all_files.sort(key=lambda item: item.name.casefold())
        self.filtered_files = list_supported_files(folder_path)

        self.render_preview()
        self.rename_button.config(state="normal" if self.filtered_files else "disabled")
        self.status_var.set(self.tr("status_found", count=len(self.filtered_files)))

        if self.filtered_files:
            messagebox.showinfo(
                self.tr("scan_done_title"),
                self.tr("scan_done_message", count=len(self.filtered_files)),
            )

    def validate_inputs(self, show_dialog: bool = True) -> tuple[str, str] | None:
        template = self.name_template.get().strip()
        if not template:
            if show_dialog:
                self.warn("empty_template")
            return None

        try:
            validate_template(template)
        except ValueError:
            if show_dialog:
                self.warn("invalid_template")
            return None

        start = self.start_number.get().strip()
        try:
            parse_start_number(start)
        except ValueError:
            if show_dialog:
                self.warn("invalid_start_number")
            return None

        return template, start

    def render_preview(self) -> None:
        self.clear_log()
        folder = self.folder_path.get().strip()
        if not folder:
            return

        self.log(self.tr("scanned_folder", folder=Path(folder).absolute()))
        self.log(self.tr("total_files", count=len(self.all_files)))
        self.log(self.tr("supported_count", count=len(self.filtered_files)))

        skipped = len(self.all_files) - len(self.filtered_files)
        if skipped:
            self.log(self.tr("unsupported_count", count=skipped))
        self.log(self.tr("supported_formats", formats=", ".join(sorted(SUPPORTED_FORMATS))))
        self.log("-" * 72)

        if not self.filtered_files:
            self.log(self.tr("no_supported_files"))
            return

        shown_files = min(10, len(self.filtered_files))
        self.log(self.tr("first_files", count=shown_files))
        for index, file_path in enumerate(self.filtered_files[:shown_files], 1):
            self.log(f"  {index}. {file_path.name}")
        if len(self.filtered_files) > shown_files:
            self.log(self.tr("more_files", count=len(self.filtered_files) - shown_files))

        inputs = self.validate_inputs(show_dialog=False)
        if inputs is None:
            self.rename_button.config(state="disabled")
            return

        template, start = inputs
        try:
            plan = build_rename_plan(self.filtered_files, template, start)
        except Exception as exc:
            self.log("")
            self.log(self.tr("rename_error_log", error=exc))
            self.rename_button.config(state="disabled")
            return

        self.rename_button.config(state="normal")
        self.log("")
        self.log("=" * 72)
        self.log(self.tr("preview_heading"))
        self.log(self.tr("template_line", template=template, start=start))
        self.log(self.tr("preview_first", count=min(10, len(plan))))

        for operation in plan[:10]:
            self.log(f"  {operation.original.name}")
            self.log(f"    -> {operation.final.name}")
        if len(plan) > 10:
            self.log(self.tr("preview_more", count=len(plan) - 10))

        self.status_var.set(self.tr("status_preview_ready"))

    def preview_rename(self) -> None:
        if not self.filtered_files:
            self.scan_files()
            return
        if self.validate_inputs(show_dialog=True) is None:
            return
        self.render_preview()

    def start_rename(self) -> None:
        if not self.filtered_files:
            self.warn("no_supported_files")
            return

        inputs = self.validate_inputs()
        if inputs is None:
            return

        template, start = inputs
        try:
            plan = build_rename_plan(self.filtered_files, template, start)
        except Exception as exc:
            messagebox.showerror(self.tr("error_title"), str(exc))
            return

        confirmed = messagebox.askyesno(
            self.tr("confirm_title"),
            self.tr(
                "confirm_message",
                count=len(plan),
                template=template,
                start=start,
            ),
        )
        if not confirmed:
            return

        self.set_busy(True)
        self.clear_log()
        self.log(self.tr("rename_started"))
        self.log(self.tr("temp_step"))
        threading.Thread(target=self.rename_worker, args=(plan,), daemon=True).start()

    def set_busy(self, busy: bool) -> None:
        state = "disabled" if busy else "normal"
        readonly_state = "disabled" if busy else "readonly"
        self.scan_button.config(state=state)
        self.rename_button.config(state="disabled" if busy else "normal")
        self.browse_button.config(state=state)
        self.template_entry.config(state=state)
        self.number_entry.config(state=state)
        self.path_entry.config(state=state)
        self.preview_button.config(state=state)
        self.language_combo.config(state=readonly_state)

        if busy:
            self.progress.pack(pady=(0, 10), padx=20, fill="x")
            self.progress.start()
        else:
            self.progress.stop()
            self.progress.pack_forget()

    def rename_worker(self, plan) -> None:
        def progress(phase, operation) -> None:
            if phase == "final":
                self.root.after(0, self.log, f"  {operation.original.name} -> {operation.final.name}")
            elif phase == "temp" and operation == plan[-1]:
                self.root.after(0, self.log, self.tr("final_step"))

        try:
            count = execute_rename_plan(plan, progress=progress)
        except RenameExecutionError as exc:
            self.root.after(0, self.rename_failed, exc)
            return
        except Exception as exc:  # pragma: no cover - defensive UI boundary
            self.root.after(0, self.rename_failed, exc)
            return

        self.root.after(0, self.rename_succeeded, count)

    def rename_succeeded(self, count: int) -> None:
        self.log("")
        self.log("=" * 72)
        self.log(self.tr("rename_complete_log", count=count))
        self.status_var.set(self.tr("status_done"))
        self.filtered_files = []
        self.set_busy(False)
        self.rename_button.config(state="disabled")
        messagebox.showinfo(self.tr("complete_title"), self.tr("rename_complete_message", count=count))

    def rename_failed(self, error: Exception) -> None:
        self.log("")
        self.log(self.tr("rename_error_log", error=error))
        rollback_errors = getattr(error, "rollback_errors", None)
        if rollback_errors:
            self.log(self.tr("rollback_errors_log", errors="; ".join(rollback_errors)))
        self.status_var.set(self.tr("status_failed"))
        self.set_busy(False)
        messagebox.showerror(self.tr("error_title"), self.tr("rename_error_log", error=error))


def main() -> None:
    root = tk.Tk()
    style = ttk.Style(root)
    for theme in ("vista", "clam"):
        try:
            style.theme_use(theme)
            break
        except tk.TclError:
            continue

    BatchRenameGUI(root)
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.mainloop()


if __name__ == "__main__":
    main()
