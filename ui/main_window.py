from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QApplication
from PyQt6.QtCore import Qt

from settings import SettingsManager
from .components import TargetFolderWidget, TargetWatermarkWidget, WatermarkFrame, OffsetsFrame, \
    SettingsButtonsLayout, ProcessLayout

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 320
WINDOW_HEIGHT_PROGRESS = 350


class MainWindow(QMainWindow):
    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.settings_manager = settings_manager
        self.settings = self.settings_manager.load()

        self._init_window()
        self._init_components()
        self._init_layout()

    def _init_window(self):
        self.setWindowTitle("Pix Watermark")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self._center_on_screen()

    def _init_components(self):
        self.target_folder = TargetFolderWidget(self.settings)
        self.watermark_file = TargetWatermarkWidget(self.settings)
        self.watermark_frame = WatermarkFrame(self.settings)
        self.offsets_frame = OffsetsFrame(self.settings)
        self.settings_buttons = SettingsButtonsLayout(self, self.settings_manager)
        self.process_layout = ProcessLayout(self)

    def _init_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        layout.addLayout(self._create_browse_layout())
        layout.addLayout(self._create_frame_layout())
        layout.addLayout(self.settings_buttons)
        layout.addLayout(self.process_layout)

    def _create_browse_layout(self):
        browse_layout = QVBoxLayout()
        browse_layout.addWidget(self.target_folder)
        browse_layout.addWidget(self.watermark_file)
        return browse_layout

    def _create_frame_layout(self):
        frame_layout = QHBoxLayout()
        frame_layout.addWidget(self.watermark_frame)
        frame_layout.addWidget(self.offsets_frame)
        return frame_layout

    def _center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def show_progress_bar(self, show):
        if show:
            self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT_PROGRESS)
        else:
            self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)