import ctypes
import os
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from settings import SettingsManager
from ui.main_window import MainWindow


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def main():
    app = QApplication(sys.argv)
    icon_path = resource_path("icon.ico")
    app.setWindowIcon(QIcon(icon_path))
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('pix_watermark')
    settings_manager = SettingsManager()
    main_window = MainWindow(settings_manager)
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
