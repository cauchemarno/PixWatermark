from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel

from settings import DEFAULT_SETTINGS, HORIZONTAL_OFFSET, VERTICAL_OFFSET
from ui.builders import create_slider, create_slider_layout


class OffsetsFrame(QFrame):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)

        self.default_horizontal = DEFAULT_SETTINGS.get("horizontal_offset")
        self.default_vertical = DEFAULT_SETTINGS.get("vertical_offset")

        self._init_ui()
        self._connect_signals()

    def get_horizontal(self):
        return self.horizontal_slider.value()

    def set_horizontal(self, value):
        self.horizontal_slider.setValue(value)
        self.horizontal_input.setText(str(value))

    def get_vertical(self):
        return self.vertical_slider.value()

    def set_vertical(self, value):
        self.vertical_slider.setValue(value)
        self.vertical_input.setText(str(value))

    def _init_ui(self):
        self.layout = QVBoxLayout(self)

        self._init_horizontal_slider()
        self._init_vertical_slider()

    def _init_horizontal_slider(self):
        self.horizontal_slider, self.horizontal_input, self.horizontal_percent = create_slider(
            HORIZONTAL_OFFSET['MIN'], HORIZONTAL_OFFSET['MAX'], self.settings, "horizontal_offset",
            self.default_horizontal
        )
        horizontal_layout = create_slider_layout(self.horizontal_slider, self.horizontal_input, self.horizontal_percent)

        self.layout.addWidget(QLabel("↔️ Horizontal Offset"), 1)
        self.layout.addLayout(horizontal_layout, 2)

    def _init_vertical_slider(self):
        self.vertical_slider, self.vertical_input, self.vertical_percent = create_slider(
            VERTICAL_OFFSET['MIN'], VERTICAL_OFFSET['MAX'], self.settings, "vertical_offset", self.default_vertical
        )
        vertical_layout = create_slider_layout(self.vertical_slider, self.vertical_input, self.vertical_percent)

        self.layout.addWidget(QLabel("↕️ Vertical Offset"), 1)
        self.layout.addLayout(vertical_layout, 2)

    def _connect_signals(self):
        self.horizontal_slider.valueChanged.connect(self._update_horizontal_input)
        self.vertical_slider.valueChanged.connect(self._update_vertical_input)

        self.horizontal_input.editingFinished.connect(self._update_horizontal_slider)
        self.vertical_input.editingFinished.connect(self._update_vertical_slider)

    def _update_horizontal_input(self):
        self.horizontal_input.setText(str(self.horizontal_slider.value()))

    def _update_vertical_input(self):
        self.vertical_input.setText(str(self.vertical_slider.value()))

    def _update_horizontal_slider(self):
        value = self._validate_horizontal_input(self.horizontal_input.text())
        self.horizontal_slider.setValue(value)
        self.horizontal_input.setText(str(value))

    def _update_vertical_slider(self):
        value = self._validate_vertical_input(self.vertical_input.text())
        self.vertical_slider.setValue(value)
        self.vertical_input.setText(str(value))

    def _validate_horizontal_input(self, text):
        try:
            value = round(float(text))
            return max(HORIZONTAL_OFFSET['MIN'], min(HORIZONTAL_OFFSET['MAX'], value))
        except ValueError:
            return HORIZONTAL_OFFSET['MIN']

    def _validate_vertical_input(self, text):
        try:
            value = round(float(text))
            return max(VERTICAL_OFFSET['MIN'], min(VERTICAL_OFFSET['MAX'], value))
        except ValueError:
            return VERTICAL_OFFSET['MIN']
