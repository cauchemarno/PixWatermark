from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QFileDialog, QLabel

from settings import DEFAULT_SETTINGS


class TargetWatermarkWidget(QWidget):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings

        self.default_value = DEFAULT_SETTINGS.get("target_folder")

        self._init_ui()

    def get_file(self):
        return self.file_line_edit.text()

    def set_file(self, file_path):
        self.file_line_edit.setText(file_path)

    def _init_ui(self):
        self._init_components()
        self._init_layout()
        self._connect_signals()

    def _init_components(self):
        self.ui_label = QLabel("🌠 Watermark ")
        self.file_line_edit = QLineEdit(self.settings.get("watermark_file", self.default_value))
        self.select_button = QPushButton("🔍 Browse")

    def _init_layout(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.ui_label, 3)
        layout.addWidget(self.file_line_edit, 7)
        layout.addWidget(self.select_button, 1)

    def _connect_signals(self):
        self.select_button.clicked.connect(self._select_file)

    def _select_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Watermark",
            filter="Images (*.png *.jpg *.jpeg)"
        )
        if file:
            self.file_line_edit.setText(file)
