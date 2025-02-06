from pathlib import Path
import json
from typing import Dict, Any, Optional

from PyQt6.QtWidgets import QFileDialog

from .constants import SETTINGS_FILE, DEFAULT_SETTINGS, WATERMARK_SIZE, WATERMARK_TRANSPARENCY, HORIZONTAL_OFFSET, \
    VERTICAL_OFFSET
from ui import popup


class SettingsManager:
    def __init__(self) -> None:
        self.file_path: Path = Path(SETTINGS_FILE)
        self.default_settings: Dict[str, Any] = DEFAULT_SETTINGS

    def save(self, settings: Dict[str, Any], file_path: Path = Path(SETTINGS_FILE)) -> None:
        try:
            with file_path.open("w", encoding="utf-8") as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
        except Exception as e:
            popup("Error", f"Error saving settings: {e}", "Critical")

    def load(self) -> Dict[str, Any]:
        try:
            if self.file_path.exists():
                with self.file_path.open("r", encoding="utf-8") as f:
                    settings: Dict[str, Any] = json.load(f)
                    return self._validate_settings(settings)
            else:
                self.save(self.default_settings)
                return self.default_settings
        except json.JSONDecodeError:
            self.save(self.default_settings)
            return self.default_settings

    def load_from_file(self) -> Optional[Dict[str, Any]]:
        file_path, _ = QFileDialog.getOpenFileName(None, "Choose Settings File", "", "JSON Files (*.json)")

        if not file_path:
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                settings: Dict[str, Any] = json.load(f)

            return self._validate_settings(settings, Path(file_path))
        except json.JSONDecodeError:
            popup("Error", "Invalid JSON format!", "Critical")
        except Exception as e:
            popup("Error", f"Error loading settings: {e}", "Critical")

        return None

    def _validate_settings(self, settings: Dict[str, Any], file_path: Path = None) -> Dict[str, Any]:
        updated: bool = False

        def check_value(key: str, value: float, limits: Dict[str, float]) -> float:
            nonlocal updated
            if not (limits["MIN"] <= value <= limits["MAX"]):
                popup("Warning", f"Invalid value for {key} = {value}.\n\n"
                                 f"Resetting to default = {limits['DEFAULT']}\n\n"
                                 f"Valid values:\nMin = {limits['MIN']}\nMax = {limits['MAX']}", "Warning")
                updated = True
                return limits["DEFAULT"]
            return value

        settings["size"] = check_value("size", settings.get("size", WATERMARK_SIZE["DEFAULT"]), WATERMARK_SIZE)
        settings["transparency"] = check_value("transparency",
                                               settings.get("transparency", WATERMARK_TRANSPARENCY["DEFAULT"]),
                                               WATERMARK_TRANSPARENCY)
        settings["horizontal_offset"] = check_value("horizontal_offset",
                                                    settings.get("horizontal_offset", HORIZONTAL_OFFSET["DEFAULT"]),
                                                    HORIZONTAL_OFFSET)
        settings["vertical_offset"] = check_value("vertical_offset",
                                                  settings.get("vertical_offset", VERTICAL_OFFSET["DEFAULT"]),
                                                  VERTICAL_OFFSET)

        if updated and file_path is None:
            self.save(settings)

        if updated and file_path is not None:
            self.save(settings, file_path)

        return settings
