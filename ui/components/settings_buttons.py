from PyQt6.QtWidgets import QHBoxLayout, QPushButton
from ui import popup
from settings import SettingsManager
from .info_text import info_text
from settings import WATERMARK_SIZE, WATERMARK_TRANSPARENCY, HORIZONTAL_OFFSET, VERTICAL_OFFSET

class SettingsButtonsLayout(QHBoxLayout):
    def __init__(self, main_window, settings_manager: SettingsManager):
        super().__init__()
        self.main_window = main_window

        self.settings_manager = settings_manager

        self._init_ui()

    def _init_ui(self):
        self._init_components()
        self._init_layout()
        self._connect_signals()

    def _init_components(self):
        self.load_button = QPushButton("📂 Load Settings")
        self.info_button = QPushButton("ℹ️")
        self.info_button.setFixedSize(24, 24)
        self.save_button = QPushButton("📝 Save Settings")

    def _init_layout(self):
        self.addWidget(self.load_button)
        self.addWidget(self.info_button)
        self.addWidget(self.save_button)

    def _connect_signals(self):
        self.save_button.clicked.connect(self._save_settings)
        self.load_button.clicked.connect(self._load_settings)
        self.info_button.clicked.connect(lambda: popup("Information", info_text, "Question"))

    def _save_settings(self):
        settings = self._get_current_settings()
        self.settings_manager.save(settings)
        popup("Success", "Settings saved!")

    def _load_settings(self):
        settings = self.settings_manager.load_from_file()
        if settings:
            self._apply_settings(settings)
            popup("Success", "Settings loaded successfully!")

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
            settings = self.settings_manager.load()

        self.main_window.target_folder.set_folder(settings.get("target_folder", ""))
        self.main_window.watermark_file.set_file(settings.get("watermark_file", ""))
        self.main_window.watermark_frame.set_size(settings.get("size", WATERMARK_SIZE['DEFAULT']))
        self.main_window.watermark_frame.set_transparency(settings.get("transparency", WATERMARK_TRANSPARENCY['DEFAULT']))
        self.main_window.offsets_frame.set_horizontal(settings.get("horizontal_offset", HORIZONTAL_OFFSET['DEFAULT']))
        self.main_window.offsets_frame.set_vertical(settings.get("vertical_offset", VERTICAL_OFFSET['DEFAULT']))