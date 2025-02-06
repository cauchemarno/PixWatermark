SETTINGS_FILE = "settings.json"
OUTPUT_FOLDER_NAME = "output"

WATERMARK_SIZE = {
    "MAX": 100,
    "MIN": 5,
    "DEFAULT": 25
}

WATERMARK_TRANSPARENCY = {
    "MAX": 100,
    "MIN": 10,
    "DEFAULT": 80
}

HORIZONTAL_OFFSET = {
    "MAX": 100,
    "MIN": 0,
    "DEFAULT": 100
}

VERTICAL_OFFSET = {
    "MAX": 100,
    "MIN": 0,
    "DEFAULT": 75
}

DEFAULT_SETTINGS = {
    "target_folder": "",
    "watermark_file": "",
    "size": WATERMARK_SIZE['DEFAULT'],
    "transparency": WATERMARK_TRANSPARENCY['DEFAULT'],
    "horizontal_offset": HORIZONTAL_OFFSET['DEFAULT'],
    "vertical_offset": VERTICAL_OFFSET['DEFAULT']
}
