from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from settings import DEFAULT_SETTINGS, WATERMARK_SIZE, WATERMARK_TRANSPARENCY
from ui.builders import create_slider, create_slider_layout


class WatermarkFrame(QFrame):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)

        self.default_size = DEFAULT_SETTINGS.get("size")
        self.default_transparency = DEFAULT_SETTINGS.get("transparency")

        self._init_ui()
        self._connect_signals()

    def get_size(self):
        return self.size_slider.value()

    def set_size(self, value):
        self.size_slider.setValue(value)
        self.size_input.setText(str(value))

    def get_transparency(self):
        return self.transparency_slider.value()

    def set_transparency(self, value):
        self.transparency_slider.setValue(value)
        self.transparency_input.setText(str(value))

    def _init_ui(self):
        self.layout = QVBoxLayout(self)

        self._init_size_slider()
        self._init_transparency_slider()

    def _init_size_slider(self):
        self.size_slider, self.size_input, self.size_percent = create_slider(
            WATERMARK_SIZE['MIN'], WATERMARK_SIZE['MAX'], self.settings, "size", self.default_size
        )
        size_layout = create_slider_layout(self.size_slider, self.size_input, self.size_percent)

        self.layout.addWidget(QLabel("⏹️ Size"), 1)
        self.layout.addLayout(size_layout, 2)

    def _init_transparency_slider(self):
        self.transparency_slider, self.transparency_input, self.transparency_percent = create_slider(
            WATERMARK_TRANSPARENCY['MIN'], WATERMARK_TRANSPARENCY['MAX'], self.settings, "transparency",
            self.default_transparency
        )
        transparency_layout = create_slider_layout(self.transparency_slider, self.transparency_input,
                                                   self.transparency_percent)

        self.layout.addWidget(QLabel("⏺️ Transparency"), 1)
        self.layout.addLayout(transparency_layout, 2)

    def _connect_signals(self):
        self.size_slider.valueChanged.connect(self._update_size_input)
        self.transparency_slider.valueChanged.connect(self._update_transparency_input)

        self.size_input.editingFinished.connect(self._update_size_slider)
        self.transparency_input.editingFinished.connect(self._update_transparency_slider)

    def _update_size_input(self):
        self.size_input.setText(str(self.size_slider.value()))

    def _update_transparency_input(self):
        self.transparency_input.setText(str(self.transparency_slider.value()))

    def _update_size_slider(self):
        value = self._validate_size_input(self.size_input.text())
        self.size_slider.setValue(value)
        self.size_input.setText(str(value))

    def _update_transparency_slider(self):
        value = self._validate_transparency_input(self.transparency_input.text())
        self.transparency_slider.setValue(value)
        self.transparency_input.setText(str(value))

    def _validate_size_input(self, text):
        try:
            value = round(float(text))
            return max(WATERMARK_SIZE['MIN'], min(WATERMARK_SIZE['MAX'], value))
        except ValueError:
            return WATERMARK_SIZE['MIN']

    def _validate_transparency_input(self, text):
        try:
            value = round(float(text))
            return max(WATERMARK_TRANSPARENCY['MIN'], min(WATERMARK_TRANSPARENCY['MAX'], value))
        except ValueError:
            return WATERMARK_TRANSPARENCY['MIN']
