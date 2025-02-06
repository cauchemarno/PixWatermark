from PyQt6.QtWidgets import QMessageBox


def popup(title: str, message: str, icon_type: str = "Information") -> None:
    msg_box = QMessageBox()
    icon = _get_icon(icon_type)
    msg_box.setIcon(icon)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg_box.exec()

def _get_icon(icon_type: str) -> QMessageBox.Icon:
    match icon_type:
        case "Critical":
            return QMessageBox.Icon.Critical
        case "Warning":
            return QMessageBox.Icon.Warning
        case "Question":
            return QMessageBox.Icon.Question
        case "Information":
            return QMessageBox.Icon.Information
        case _:
            return QMessageBox.Icon.Information
