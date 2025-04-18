from pathlib import Path
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QFileDialog
from ui import popup
from ui.components.info_text import info_text


class SettingsButtonsLayout(QHBoxLayout):
    def __init__(self, main_window, settings_manager):
        super().__init__()
        self.main_window = main_window
        self.settings_manager = settings_manager
        self._init_ui()

    def _init_ui(self):
        self._init_components()
        self._init_layout()
        self._connect_signals()

    def _init_components(self):
        self.load_button = QPushButton("📂 Load Preset")
        self.info_button = QPushButton("ℹ️")
        self.info_button.setFixedSize(24, 24)
        self.save_button = QPushButton("💾 Save Preset")

    def _init_layout(self):
        self.addWidget(self.load_button)
        self.addWidget(self.info_button)
        self.addWidget(self.save_button)

    def _connect_signals(self):
        self.save_button.clicked.connect(self._save_preset)
        self.load_button.clicked.connect(self._load_preset)
        self.info_button.clicked.connect(lambda: popup("Information", info_text, "Question"))

    def _save_preset(self):
        settings = self._get_current_settings()
        file_path, _ = QFileDialog.getSaveFileName(
            self.main_window,
            "Save Preset As",
            "my_preset.json",
            "JSON Files (*.json)"
        )
        if file_path:
            self.settings_manager.save_preset(settings, Path(file_path))
            popup("Success", "Preset saved!")

    def _load_preset(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Load Preset",
            "",
            "JSON Files (*.json)"
        )
        if not file_path:
            return

        settings = self.settings_manager.load_preset(Path(file_path))
        if settings:
            self._apply_settings(settings)
            popup("Success", "Preset loaded!")

    def _get_current_settings(self):
        return {
            "target_folder": self.main_window.target_folder.get_folder(),
            "watermark_file": self.main_window.watermark_file.get_file(),
            "size": self.main_window.watermark_frame.get_size(),
            "transparency": self.main_window.watermark_frame.get_transparency(),
            "horizontal_offset": self.main_window.offsets_frame.get_horizontal(),
            "vertical_offset": self.main_window.offsets_frame.get_vertical(),
        }

    def _apply_settings(self, settings=None):
        if settings is None:
            settings = self.settings_manager.load_persistent()

        self.main_window.target_folder.set_folder(settings["target_folder"])
        self.main_window.watermark_file.set_file(settings["watermark_file"])
        self.main_window.watermark_frame.set_size(settings["size"])
        self.main_window.watermark_frame.set_transparency(settings["transparency"])
        self.main_window.offsets_frame.set_horizontal(settings["horizontal_offset"])
        self.main_window.offsets_frame.set_vertical(settings["vertical_offset"])
