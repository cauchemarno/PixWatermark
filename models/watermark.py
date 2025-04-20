from typing import Dict
from PIL import Image, ImageEnhance, UnidentifiedImageError


def _add_watermark(input_image_path: str,
                   watermark_image_path: str,
                   output_image_path: str,
                   transparency: float,
                   vertical_offset: float,
                   horizontal_offset: float,
                   watermark_size: float,
                   stats: Dict[str, int | list[str]]) -> None:
    try:
        img = Image.open(input_image_path).convert("RGBA")
        watermark = Image.open(watermark_image_path).convert("RGBA")

        img_width, img_height = img.size
        smaller_side = min(img_width, img_height)

        new_width = int(smaller_side * watermark_size)
        aspect_ratio = watermark.width / watermark.height
        new_height = int(new_width / aspect_ratio)
        watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)

        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(transparency)
        watermark.putalpha(alpha)

        position_x = int((img_width - watermark.width) * horizontal_offset)
        position_y = int((img_height - watermark.height) * vertical_offset)

        transparent = Image.new("RGBA", img.size, (0, 0, 0, 0))
        transparent.paste(watermark, (position_x, position_y), watermark)
        combined = Image.alpha_composite(img, transparent)

        input_format = input_image_path.lower().split('.')[-1]
        if input_format in ['jpg', 'jpeg']:
            combined = combined.convert("RGB")
            combined.save(output_image_path, format="JPEG", quality=95, optimize=True, subsampling="4:4:4")
        else:
            combined.save(output_image_path, format="PNG", compress_level=1)

        stats["success"] += 1

    except UnidentifiedImageError:
        stats["errors"].append(f"'{input_image_path}' is not a valid image.")
    except Exception as e:
        stats["errors"].append(f"Error with file '{input_image_path}': {e}")
