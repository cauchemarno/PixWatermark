from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QFileDialog, QLabel

from settings import DEFAULT_SETTINGS


class TargetFolderWidget(QWidget):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings

        self.default_value = DEFAULT_SETTINGS.get("target_folder")

        self._init_ui()

    def get_folder(self):
        return self.folder_line_edit.text()

    def set_folder(self, folder):
        self.folder_line_edit.setText(folder)

    def _init_ui(self):
        self._init_components()
        self._init_layout()
        self._connect_signals()

    def _init_components(self):
        self.ui_label = QLabel("🗂 Target Folder ")
        self.folder_line_edit = QLineEdit(self.settings.get("target_folder", self.default_value))
        self.select_button = QPushButton("🔍 Browse")

    def _init_layout(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.ui_label, 3)
        layout.addWidget(self.folder_line_edit, 7)
        layout.addWidget(self.select_button, 1)

    def _connect_signals(self):
        self.select_button.clicked.connect(self._select_folder)

    def _select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Target Folder")
        if folder:
            self.folder_line_edit.setText(folder)
