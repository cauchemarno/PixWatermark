from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QProgressBar

from models import process_images
from ui import popup


class ProcessLayout(QVBoxLayout):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self._init_ui()

    def _init_ui(self):
        self._init_components()
        self._init_layout()
        self._connect_signals()

    def _init_components(self):
        self.run_button = QPushButton("❇️ Mark it!")
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)

    def _init_layout(self):
        self.addWidget(self.run_button)
        self.addWidget(self.progress_bar)

    def _connect_signals(self):
        self.run_button.clicked.connect(self._run_process)

    def _run_process(self):
        input_folder = self.main_window.target_folder.get_folder()
        watermark_path = self.main_window.watermark_file.get_file()

        if not input_folder:
            popup("Warning", "Target folder is not selected. Please choose a folder.", "Warning")
            return

        if not watermark_path:
            popup("Warning", "Watermark file is not selected. Please choose a file.", "Warning")
            return

        self._start_progress_bar()

        process_images(
            input_folder,
            watermark_path,
            self.main_window.watermark_frame.get_transparency() / 100,
            self.main_window.offsets_frame.get_vertical() / 100,
            self.main_window.offsets_frame.get_horizontal() / 100,
            self.main_window.watermark_frame.get_size() / 100,
            self._update_progress_bar
        )

        self._stop_progress_bar()

    def _start_progress_bar(self):
        self.progress_bar.setVisible(True)
        self.main_window.show_progress_bar(True)
        self.progress_bar.setValue(0)

    def _update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def _stop_progress_bar(self):
        self.progress_bar.setVisible(False)
        self.main_window.show_progress_bar(False)
