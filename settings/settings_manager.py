from pathlib import Path
import json
from typing import Dict, Any, Optional

from PyQt6.QtCore import QSettings
from ui import popup
from settings.constants import DEFAULT_SETTINGS, WATERMARK_SIZE, WATERMARK_TRANSPARENCY, HORIZONTAL_OFFSET, VERTICAL_OFFSET


class SettingsManager:
    def __init__(self) -> None:
        self.settings = QSettings("cauchemarno", "PixWatermark")
        self.default_settings: Dict[str, Any] = DEFAULT_SETTINGS

    def load_persistent(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for key, default in self.default_settings.items():
            result[key] = self.settings.value(key, default, type=type(default))
        return result

    def save_persistent(self, settings: Dict[str, Any]) -> None:
        for key, value in settings.items():
            self.settings.setValue(key, value)
        self.settings.sync()

    def save_preset(self, settings: Dict[str, Any], file_path: Path) -> None:
        try:
            with file_path.open("w", encoding="utf-8") as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
        except Exception as e:
            popup("Error", f"Error saving preset: {e}", "Critical")

    def load_preset(self, file_path: Path) -> Optional[Dict[str, Any]]:
        try:
            with file_path.open("r", encoding="utf-8") as f:
                data: Dict[str, Any] = json.load(f)
            settings = {**self.default_settings, **data}
            return self._validate_settings(settings)
        except json.JSONDecodeError:
            popup("Error", "Invalid JSON format!", "Critical")
        except Exception as e:
            popup("Error", f"Error loading preset: {e}", "Critical")
        return None

    def _validate_settings(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        updated = False

        def check(key: str, value: Any, limits: Dict[str, Any]) -> Any:
            nonlocal updated
            try:
                v = float(value)
            except (TypeError, ValueError):
                updated = True
                return limits["DEFAULT"]

            if not (limits["MIN"] <= v <= limits["MAX"]):
                popup(
                    "Warning",
                    f"Invalid value for {key} = {value}. Reset to default = {limits['DEFAULT']}",
                    "Warning"
                )
                updated = True
                return limits["DEFAULT"]
            return type(limits["DEFAULT"])(v)

        settings["size"] = check("size", settings.get("size"), WATERMARK_SIZE)
        settings["transparency"] = check("transparency", settings.get("transparency"), WATERMARK_TRANSPARENCY)
        settings["horizontal_offset"] = check(
            "horizontal_offset", settings.get("horizontal_offset"), HORIZONTAL_OFFSET
        )
        settings["vertical_offset"] = check(
            "vertical_offset", settings.get("vertical_offset"), VERTICAL_OFFSET
        )

        settings["target_folder"] = settings.get("target_folder") or self.default_settings["target_folder"]
        settings["watermark_file"] = settings.get("watermark_file") or self.default_settings["watermark_file"]

        return settings
