from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).parents[1]
JPG_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".jfif", ".tif", ".tiff"}
JOBS = (
    (
        "bff23",
        Path(r"C:/Users/Lenovo/OneDrive/Bitcoin FilmFest/BFF23/WK23 zdjęcia od fotografa/Weekend Kapitalizmu 2023 - zdjęcia"),
        ROOT / "site/23/23-assets/gallery",
        "bff23-warsaw",
        "BFF’23 · Warsaw photo archive",
    ),
    (
        "bff23-zlota44",
        Path(r"C:/Users/Lenovo/OneDrive/Bitcoin FilmFest/BFF23/WK23 zdjęcia od fotografa/BFF x WK23 - Złota 44 VIP koktajl - zdjęcia"),
        ROOT / "site/23/23-assets/gallery",
        "bff23-zlota44",
        "BFF’23 · Złota 44 photo archive",
    ),
    (
        "bff25",
        Path(r"C:/Users/Lenovo/OneDrive/Bitcoin FilmFest/BFF25/BFF 25 fotki/BFF25"),
        ROOT / "site/25/25-assets/gallery",
        "bff25",
        "BFF’25 · event photo archive",
    ),
)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> None:
    all_manifests: dict[str, list[dict[str, str]]] = {}
    for key, source_root, destination, prefix, caption in JOBS:
        if not source_root.is_dir():
            raise SystemExit(f"missing source root: {source_root}")
        destination.mkdir(parents=True, exist_ok=True)
        source_files = sorted(
            p for p in source_root.iterdir() if p.is_file() and p.suffix.lower() in JPG_EXTS
        )
        entries: list[dict[str, str]] = []
        input_bytes = 0
        output_bytes = 0
        for index, source in enumerate(source_files, start=1):
            input_bytes += source.stat().st_size
            output_name = f"{prefix}-{index:04d}.jpg"
            output = destination / output_name
            with Image.open(source) as image:
                image = ImageOps.exif_transpose(image)
                if image.mode in {"RGBA", "LA"} or (image.mode == "P" and "transparency" in image.info):
                    rgba = image.convert("RGBA")
                    background = Image.new("RGB", rgba.size, "#111111")
                    background.paste(rgba, mask=rgba.getchannel("A"))
                    image = background
                else:
                    image = image.convert("RGB")
                image.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                image.save(output, "JPEG", quality=82, optimize=True, progressive=True)
            output_bytes += output.stat().st_size
            entries.append(
                {
                    "path": f"/{'23' if key.startswith('bff23') else '25'}/{'23-assets' if key.startswith('bff23') else '25-assets'}/gallery/{output_name}",
                    "alt": f"{caption} photograph {index}",
                    "caption": caption,
                    "source": f"{key}/{source.name}",
                }
            )
        all_manifests[key] = entries
        print(f"{key}: {len(entries)} files; input={input_bytes}; output={output_bytes}")

    data_root = ROOT / "site/_data"
    data_root.mkdir(parents=True, exist_ok=True)
    for key, entries in all_manifests.items():
        if key.startswith("bff23"):
            output = data_root / "bff23_gallery.yml"
        else:
            output = data_root / "bff25_gallery.yml"
        mode = "a" if output.exists() and key == "bff23-zlota44" else "w"
        with output.open(mode, encoding="utf-8", newline="\n") as handle:
            for entry in entries:
                handle.write("- path: " + yaml_string(entry["path"]) + "\n")
                handle.write("  alt: " + yaml_string(entry["alt"]) + "\n")
                handle.write("  caption: " + yaml_string(entry["caption"]) + "\n")
                handle.write("  source: " + yaml_string(entry["source"]) + "\n")

    manifest_path = ROOT / "docs/context/PHOTO-DERIVATIVE-MANIFEST.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(all_manifests, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
