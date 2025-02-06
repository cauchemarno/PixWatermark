import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import Callable

from PIL import Image, UnidentifiedImageError

from .watermark import _add_watermark
from settings import OUTPUT_FOLDER_NAME
from ui import popup


def process_images(input_folder: str,
                   watermark_path: str,
                   transparency: float,
                   vertical_offset: float,
                   horizontal_offset: float,
                   watermark_size: float,
                   update_progress: Callable[[int], None]) -> None:
    try:
        input_folder = Path(input_folder)
        watermark_path = Path(watermark_path)

        if not input_folder.exists():
            popup("Error", "Input folder does not exist!", "Warning")
            return

        if not watermark_path.is_file():
            popup("Error", "Watermark file not found!", "Warning")
            return

        try:
            Image.open(watermark_path).verify()
        except (UnidentifiedImageError, OSError):
            popup("Error", "The watermark file is not a valid image!", "Critical")
            return

        output_folder = input_folder / OUTPUT_FOLDER_NAME
        os.makedirs(output_folder, exist_ok=True)

        image_files = [f for f in input_folder.iterdir() if f.suffix.lower() in (".png", ".jpg", ".jpeg")]

        if not image_files:
            popup("Error", "No valid image files found in the input folder.", "Warning")
            return

        stats = {"success": 0, "errors": []}
        total_files = len(image_files)

        def process_file(file_path: Path):
            _add_watermark(
                str(file_path),
                str(watermark_path),
                str(output_folder / file_path.name),
                transparency,
                vertical_offset,
                horizontal_offset,
                watermark_size,
                stats,
            )

            if update_progress:
                update_progress(int((stats["success"] + len(stats["errors"])) / total_files * 100))

        with ThreadPoolExecutor() as executor:
            list(executor.map(process_file, image_files))

        failed = len(stats["errors"])
        message = f"Files processed: {total_files}\n✅ Successful: {stats['success']}\n❌ Errors: {failed}"

        if failed:
            message += "\n\nErrors:\n" + "\n".join(stats["errors"])

        popup("Processing Result", message, "Information" if failed == 0 else "Warning")

    except Exception as e:
        popup("Error", f"Error processing images: {e}", "Critical")
