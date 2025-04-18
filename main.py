import sys
import ctypes
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from settings import SettingsManager
from ui.main_window import MainWindow
from resources import resources_rc


def main():
    app = QApplication(sys.argv)

    if sys.platform.startswith("win"):
        icon = QIcon(":/resources/icons/icon.ico")
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('PixWatermark')
    elif sys.platform.startswith("darwin"):
        icon = QIcon(":/resources/icons/icon.icns")
    else:
        icon = QIcon(":/resources/icons/icon.png")

    app.setWindowIcon(icon)

    settings_manager = SettingsManager()
    main_window = MainWindow(settings_manager)

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
