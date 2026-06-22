#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small translation table for the batch rename GUI."""

from __future__ import annotations


DEFAULT_LANGUAGE = "en"

LANGUAGES = {
    "en": "English",
    "zh": "中文",
    "fr": "Français",
    "de": "Deutsch",
    "ja": "日本語",
}


TRANSLATIONS = {
    "en": {
        "app_title": "Unicode Batch Renamer",
        "main_title": "Unicode Batch Renamer",
        "language_label": "Language:",
        "folder_frame": "Step 1: Choose a folder",
        "folder_help": "Folder to process:",
        "browse": "Browse...",
        "template_frame": "Step 2: Set the naming template",
        "template_label": "Template:",
        "start_label": "Start number:",
        "examples_text": (
            "Examples:\n"
            "  {n} -> 1.jpg, 2.png, 3.mp4\n"
            "  photo_ -> photo_1.jpg, photo_2.jpg\n"
            "  trip_{n}_final -> trip_1_final.jpg"
        ),
        "preview": "Preview",
        "preview_frame": "Preview and log",
        "scan": "Scan Files",
        "rename": "Start Rename",
        "status_ready": "Ready - choose a folder and naming template",
        "select_folder_dialog": "Choose a folder to process",
        "warning_title": "Warning",
        "error_title": "Error",
        "info_title": "Info",
        "confirm_title": "Confirm Rename",
        "complete_title": "Complete",
        "scan_done_title": "Scan Complete",
        "no_folder": "Choose a folder first.",
        "folder_missing": "The selected folder does not exist.",
        "empty_template": "Enter a naming template.",
        "invalid_start_number": "Start number must be a non-negative integer.",
        "invalid_template": "The template contains characters that are unsafe in file names.",
        "scan_done_message": "Found {count} supported files. Review the preview before renaming.",
        "scanned_folder": "Folder: {folder}",
        "total_files": "Files found: {count}",
        "supported_count": "Supported files: {count}",
        "unsupported_count": "Unsupported files skipped: {count}",
        "supported_formats": "Supported formats: {formats}",
        "no_supported_files": "No supported image or video files were found.",
        "first_files": "First {count} files:",
        "more_files": "... and {count} more files",
        "preview_heading": "Rename preview:",
        "template_line": "Template: '{template}' | Start number: {start}",
        "preview_first": "First {count} generated names:",
        "preview_more": "... and {count} more rename operations",
        "status_found": "Found {count} supported files",
        "status_preview_ready": "Preview ready",
        "confirm_message": (
            "Rename {count} files?\n\n"
            "Template: '{template}'\n"
            "Start number: {start}\n\n"
            "This cannot be undone automatically. Make sure important files are backed up."
        ),
        "rename_started": "Starting rename...",
        "temp_step": "Step 1: moving files to temporary names...",
        "final_step": "Step 2: applying final names...",
        "rename_complete_log": "Done. Renamed {count} files.",
        "rename_complete_message": "Renamed {count} files.",
        "rename_error_log": "Rename failed: {error}",
        "rollback_errors_log": "Rollback also reported: {errors}",
        "status_done": "Rename complete",
        "status_failed": "Rename failed",
        "cli_intro": "Batch File Renamer",
        "cli_scan": "Scanning: {folder}",
        "cli_found": "Found {count} supported files.",
        "cli_confirm": "Type y and press Enter to rename these files: ",
        "cli_cancelled": "Cancelled.",
        "cli_done": "Done. Renamed {count} files.",
        "cli_exit": "Press Enter to exit...",
    },
    "zh": {
        "app_title": "Unicode 文件批量重命名工具",
        "main_title": "Unicode 文件批量重命名工具",
        "language_label": "语言:",
        "folder_frame": "步骤 1：选择文件夹",
        "folder_help": "要处理的文件夹:",
        "browse": "浏览...",
        "template_frame": "步骤 2：设置命名模板",
        "template_label": "模板:",
        "start_label": "起始编号:",
        "examples_text": (
            "示例:\n"
            "  {n} -> 1.jpg, 2.png, 3.mp4\n"
            "  photo_ -> photo_1.jpg, photo_2.jpg\n"
            "  trip_{n}_final -> trip_1_final.jpg"
        ),
        "preview": "预览",
        "preview_frame": "预览和日志",
        "scan": "扫描文件",
        "rename": "开始重命名",
        "status_ready": "就绪 - 请选择文件夹并设置命名模板",
        "select_folder_dialog": "选择要处理的文件夹",
        "warning_title": "警告",
        "error_title": "错误",
        "info_title": "提示",
        "confirm_title": "确认重命名",
        "complete_title": "完成",
        "scan_done_title": "扫描完成",
        "no_folder": "请先选择文件夹。",
        "folder_missing": "选择的文件夹不存在。",
        "empty_template": "请输入命名模板。",
        "invalid_start_number": "起始编号必须是非负整数。",
        "invalid_template": "模板包含不适合文件名的字符。",
        "scan_done_message": "找到 {count} 个支持的文件。重命名前请检查预览。",
        "scanned_folder": "文件夹: {folder}",
        "total_files": "发现文件: {count}",
        "supported_count": "支持的文件: {count}",
        "unsupported_count": "跳过的不支持文件: {count}",
        "supported_formats": "支持格式: {formats}",
        "no_supported_files": "未找到支持的图片或视频文件。",
        "first_files": "前 {count} 个文件:",
        "more_files": "... 还有 {count} 个文件",
        "preview_heading": "重命名预览:",
        "template_line": "模板: '{template}' | 起始编号: {start}",
        "preview_first": "前 {count} 个新文件名:",
        "preview_more": "... 还有 {count} 个重命名操作",
        "status_found": "找到 {count} 个支持的文件",
        "status_preview_ready": "预览已生成",
        "confirm_message": (
            "确认重命名 {count} 个文件？\n\n"
            "模板: '{template}'\n"
            "起始编号: {start}\n\n"
            "该操作不能自动撤销。请确认重要文件已备份。"
        ),
        "rename_started": "开始重命名...",
        "temp_step": "步骤 1：移动到临时文件名...",
        "final_step": "步骤 2：应用最终文件名...",
        "rename_complete_log": "完成，已重命名 {count} 个文件。",
        "rename_complete_message": "已重命名 {count} 个文件。",
        "rename_error_log": "重命名失败: {error}",
        "rollback_errors_log": "回滚也出现问题: {errors}",
        "status_done": "重命名完成",
        "status_failed": "重命名失败",
        "cli_intro": "文件批量重命名工具",
        "cli_scan": "正在扫描: {folder}",
        "cli_found": "找到 {count} 个支持的文件。",
        "cli_confirm": "输入 y 并按回车开始重命名: ",
        "cli_cancelled": "已取消。",
        "cli_done": "完成，已重命名 {count} 个文件。",
        "cli_exit": "按回车键退出...",
    },
    "fr": {
        "app_title": "Renommeur Unicode par lot",
        "main_title": "Renommeur Unicode par lot",
        "language_label": "Langue :",
        "folder_frame": "Étape 1 : choisir un dossier",
        "folder_help": "Dossier à traiter :",
        "browse": "Parcourir...",
        "template_frame": "Étape 2 : définir le modèle de nom",
        "template_label": "Modèle :",
        "start_label": "Numéro initial :",
        "examples_text": (
            "Exemples :\n"
            "  {n} -> 1.jpg, 2.png, 3.mp4\n"
            "  photo_ -> photo_1.jpg, photo_2.jpg\n"
            "  voyage_{n}_final -> voyage_1_final.jpg"
        ),
        "preview": "Aperçu",
        "preview_frame": "Aperçu et journal",
        "scan": "Analyser",
        "rename": "Renommer",
        "status_ready": "Prêt - choisissez un dossier et un modèle",
        "select_folder_dialog": "Choisir un dossier à traiter",
        "warning_title": "Avertissement",
        "error_title": "Erreur",
        "info_title": "Info",
        "confirm_title": "Confirmer le renommage",
        "complete_title": "Terminé",
        "scan_done_title": "Analyse terminée",
        "no_folder": "Choisissez d'abord un dossier.",
        "folder_missing": "Le dossier sélectionné n'existe pas.",
        "empty_template": "Saisissez un modèle de nom.",
        "invalid_start_number": "Le numéro initial doit être un entier positif ou nul.",
        "invalid_template": "Le modèle contient des caractères non sûrs pour les noms de fichiers.",
        "scan_done_message": "{count} fichiers pris en charge trouvés. Vérifiez l'aperçu avant de renommer.",
        "scanned_folder": "Dossier : {folder}",
        "total_files": "Fichiers trouvés : {count}",
        "supported_count": "Fichiers pris en charge : {count}",
        "unsupported_count": "Fichiers ignorés : {count}",
        "supported_formats": "Formats pris en charge : {formats}",
        "no_supported_files": "Aucune image ni vidéo prise en charge n'a été trouvée.",
        "first_files": "{count} premiers fichiers :",
        "more_files": "... et {count} fichiers de plus",
        "preview_heading": "Aperçu du renommage :",
        "template_line": "Modèle : '{template}' | Numéro initial : {start}",
        "preview_first": "{count} premiers noms générés :",
        "preview_more": "... et {count} renommages de plus",
        "status_found": "{count} fichiers pris en charge trouvés",
        "status_preview_ready": "Aperçu prêt",
        "confirm_message": (
            "Renommer {count} fichiers ?\n\n"
            "Modèle : '{template}'\n"
            "Numéro initial : {start}\n\n"
            "Cette action ne peut pas être annulée automatiquement. Sauvegardez les fichiers importants."
        ),
        "rename_started": "Renommage en cours...",
        "temp_step": "Étape 1 : déplacement vers des noms temporaires...",
        "final_step": "Étape 2 : application des noms finaux...",
        "rename_complete_log": "Terminé. {count} fichiers renommés.",
        "rename_complete_message": "{count} fichiers renommés.",
        "rename_error_log": "Échec du renommage : {error}",
        "rollback_errors_log": "La restauration a aussi signalé : {errors}",
        "status_done": "Renommage terminé",
        "status_failed": "Échec du renommage",
    },
    "de": {
        "app_title": "Unicode Batch Renamer",
        "main_title": "Unicode Batch Renamer",
        "language_label": "Sprache:",
        "folder_frame": "Schritt 1: Ordner wählen",
        "folder_help": "Zu verarbeitender Ordner:",
        "browse": "Durchsuchen...",
        "template_frame": "Schritt 2: Namensvorlage festlegen",
        "template_label": "Vorlage:",
        "start_label": "Startnummer:",
        "examples_text": (
            "Beispiele:\n"
            "  {n} -> 1.jpg, 2.png, 3.mp4\n"
            "  foto_ -> foto_1.jpg, foto_2.jpg\n"
            "  reise_{n}_final -> reise_1_final.jpg"
        ),
        "preview": "Vorschau",
        "preview_frame": "Vorschau und Protokoll",
        "scan": "Dateien suchen",
        "rename": "Umbenennen",
        "status_ready": "Bereit - Ordner und Vorlage wählen",
        "select_folder_dialog": "Ordner zur Verarbeitung wählen",
        "warning_title": "Warnung",
        "error_title": "Fehler",
        "info_title": "Info",
        "confirm_title": "Umbenennen bestätigen",
        "complete_title": "Fertig",
        "scan_done_title": "Suche abgeschlossen",
        "no_folder": "Wählen Sie zuerst einen Ordner.",
        "folder_missing": "Der ausgewählte Ordner existiert nicht.",
        "empty_template": "Geben Sie eine Namensvorlage ein.",
        "invalid_start_number": "Die Startnummer muss eine nicht negative ganze Zahl sein.",
        "invalid_template": "Die Vorlage enthält für Dateinamen unsichere Zeichen.",
        "scan_done_message": "{count} unterstützte Dateien gefunden. Prüfen Sie die Vorschau vor dem Umbenennen.",
        "scanned_folder": "Ordner: {folder}",
        "total_files": "Gefundene Dateien: {count}",
        "supported_count": "Unterstützte Dateien: {count}",
        "unsupported_count": "Übersprungene Dateien: {count}",
        "supported_formats": "Unterstützte Formate: {formats}",
        "no_supported_files": "Keine unterstützten Bild- oder Videodateien gefunden.",
        "first_files": "Erste {count} Dateien:",
        "more_files": "... und {count} weitere Dateien",
        "preview_heading": "Umbenennungs-Vorschau:",
        "template_line": "Vorlage: '{template}' | Startnummer: {start}",
        "preview_first": "Erste {count} generierte Namen:",
        "preview_more": "... und {count} weitere Umbenennungen",
        "status_found": "{count} unterstützte Dateien gefunden",
        "status_preview_ready": "Vorschau bereit",
        "confirm_message": (
            "{count} Dateien umbenennen?\n\n"
            "Vorlage: '{template}'\n"
            "Startnummer: {start}\n\n"
            "Diese Aktion kann nicht automatisch rückgängig gemacht werden. Sichern Sie wichtige Dateien."
        ),
        "rename_started": "Umbenennung wird gestartet...",
        "temp_step": "Schritt 1: Dateien auf temporäre Namen verschieben...",
        "final_step": "Schritt 2: endgültige Namen anwenden...",
        "rename_complete_log": "Fertig. {count} Dateien umbenannt.",
        "rename_complete_message": "{count} Dateien umbenannt.",
        "rename_error_log": "Umbenennen fehlgeschlagen: {error}",
        "rollback_errors_log": "Auch das Zurücksetzen meldete: {errors}",
        "status_done": "Umbenennung abgeschlossen",
        "status_failed": "Umbenennung fehlgeschlagen",
    },
    "ja": {
        "app_title": "Unicode 一括リネーム",
        "main_title": "Unicode 一括リネーム",
        "language_label": "言語:",
        "folder_frame": "ステップ 1: フォルダーを選択",
        "folder_help": "処理するフォルダー:",
        "browse": "参照...",
        "template_frame": "ステップ 2: 名前テンプレート",
        "template_label": "テンプレート:",
        "start_label": "開始番号:",
        "examples_text": (
            "例:\n"
            "  {n} -> 1.jpg, 2.png, 3.mp4\n"
            "  photo_ -> photo_1.jpg, photo_2.jpg\n"
            "  trip_{n}_final -> trip_1_final.jpg"
        ),
        "preview": "プレビュー",
        "preview_frame": "プレビューとログ",
        "scan": "ファイルを検索",
        "rename": "リネーム開始",
        "status_ready": "準備完了 - フォルダーとテンプレートを選択してください",
        "select_folder_dialog": "処理するフォルダーを選択",
        "warning_title": "警告",
        "error_title": "エラー",
        "info_title": "情報",
        "confirm_title": "リネーム確認",
        "complete_title": "完了",
        "scan_done_title": "検索完了",
        "no_folder": "先にフォルダーを選択してください。",
        "folder_missing": "選択したフォルダーが存在しません。",
        "empty_template": "名前テンプレートを入力してください。",
        "invalid_start_number": "開始番号は 0 以上の整数にしてください。",
        "invalid_template": "テンプレートにファイル名として安全でない文字が含まれています。",
        "scan_done_message": "{count} 個の対応ファイルを見つけました。リネーム前にプレビューを確認してください。",
        "scanned_folder": "フォルダー: {folder}",
        "total_files": "検出ファイル: {count}",
        "supported_count": "対応ファイル: {count}",
        "unsupported_count": "スキップした非対応ファイル: {count}",
        "supported_formats": "対応形式: {formats}",
        "no_supported_files": "対応する画像または動画ファイルが見つかりません。",
        "first_files": "最初の {count} 件:",
        "more_files": "... ほか {count} 件",
        "preview_heading": "リネームプレビュー:",
        "template_line": "テンプレート: '{template}' | 開始番号: {start}",
        "preview_first": "生成される最初の {count} 件:",
        "preview_more": "... ほか {count} 件のリネーム",
        "status_found": "{count} 個の対応ファイルを検出",
        "status_preview_ready": "プレビュー準備完了",
        "confirm_message": (
            "{count} 個のファイルをリネームしますか？\n\n"
            "テンプレート: '{template}'\n"
            "開始番号: {start}\n\n"
            "この操作は自動では元に戻せません。重要なファイルはバックアップしてください。"
        ),
        "rename_started": "リネームを開始しています...",
        "temp_step": "ステップ 1: 一時ファイル名へ移動...",
        "final_step": "ステップ 2: 最終ファイル名を適用...",
        "rename_complete_log": "完了。{count} 個のファイルをリネームしました。",
        "rename_complete_message": "{count} 個のファイルをリネームしました。",
        "rename_error_log": "リネームに失敗しました: {error}",
        "rollback_errors_log": "ロールバックでも問題が発生しました: {errors}",
        "status_done": "リネーム完了",
        "status_failed": "リネーム失敗",
    },
}


def t(language: str, key: str, **kwargs) -> str:
    text = TRANSLATIONS.get(language, TRANSLATIONS[DEFAULT_LANGUAGE]).get(key)
    if text is None:
        text = TRANSLATIONS[DEFAULT_LANGUAGE].get(key, key)
    return text.format(**kwargs) if kwargs else text
