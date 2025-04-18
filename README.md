# 🎑 Pix Watermark

**PixWatermark** is a simple tool for batch watermarking images. It applies a selected watermark to all images in a chosen folder with adjustable settings such as size, transparency, and positioning. Ideal for protecting visual content or adding branding to images.

---

## 🚀 Installation

### ✅ A ready-to-use installer for Windows:
👉 [Download PixWatermark Installer](https://github.com/cauchemarno/PixWatermark/releases)

---

## ✨ Features

- 📂 **Batch processing** – Apply the watermark to all images in a selected folder.
- 🎨 **Customizable watermark**:
    - Resize the watermark relative to the smallest dimension of each image.
    - Adjust transparency level.
    - Set horizontal and vertical offsets.
- 💾 **Save and load presets** – Quickly reapply preferred configurations.
- 🌠 **Supported image formats** – PNG, JPG, and JPEG.

---

## 🖥 Screenshots

![App Screenshot](https://i.imgur.com/qEi4LXg.png)

![Usage Example](https://i.imgur.com/MM7xKay.png)

---

## 🧪 Run from Source
To run PixWatermark from source, follow these steps:

1. Clone the repository:

```bash
  git clone https://github.com/cauchemarno/PixWatermark.git
  cd PixWatermark
```
2. Install the required dependencies:

```bash
  pip install -r requirements.txt
```

3. Run the app::
```bash
  python main.py
```
---

## 🛠 Build Your Own Executable
You can build PixWatermark using PyInstaller.
```bash
pip install pyinstaller
```

### 📦 One-folder build (recommended)
```bash
pyinstaller main.py --name PixWatermark --noconsole --icon=resources/icons/icon.ico
```

🧍 Optional: One-file build
```bash
pyinstaller main.py --name PixWatermark --onefile --noconsole --icon=resources/icons/icon.ico
```
---

## 📝 ToDo

- Add watermark rotation
- Add option to tile watermark across the entire image
- Add GIF support

---

## 💬 Feedback & Contributions
Feel free to report issues or suggest features on GitHub.

Happy merging! 🚀

---

## 📜 License

This project is licensed under the [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html) License.

The logo/icon uses an emoji from [Twemoji](https://github.com/twitter/twemoji) (CC BY 4.0).