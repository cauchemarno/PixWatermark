from typing import Dict, Any

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QLineEdit, QLabel, QHBoxLayout


def create_slider(min_value: int, max_value: int, settings: Dict[str, Any], key: str, default_value: int):
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setRange(min_value, max_value)
    slider.setValue(settings.get(key, default_value))

    input_field = QLineEdit(str(slider.value()))
    input_field.setFixedWidth(40)

    percent_label = QLabel("%")

    return slider, input_field, percent_label


def create_slider_layout(slider: QSlider, input_field: QLineEdit, percent_label: QLabel) -> QHBoxLayout:
    layout = QHBoxLayout()

    layout.addWidget(slider, 5)
    layout.addWidget(input_field, 0)
    layout.addWidget(percent_label, 0)

    return layout
