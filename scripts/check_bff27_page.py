from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_MARKERS = (
    "layout: default",
    "permalink: /27/",
    "BFF’27",
    "24–27 June 2027",
    "Early-bird page",
    "BFF27%20film%20submission",
    "BFF27%20collaboration",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).parents[1])
    parser.add_argument("--built", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    source = root / "site" / "27.md"
    built = args.built or (root / "site" / "_site" / "27" / "index.html")
    failures: list[str] = []

    if not source.is_file():
        failures.append(f"missing source: {source}")
        source_text = ""
    else:
        source_text = source.read_text(encoding="utf-8")

    for marker in REQUIRED_MARKERS:
        if marker not in source_text:
            failures.append(f"source missing {marker}")
    if re.search(r"<(?:html|head|body|nav|footer)\b", source_text):
        failures.append("source contains a standalone shell element")
    if "<script" in source_text or "<style" in source_text:
        failures.append("source contains inline script/style")

    if not built.is_file():
        failures.append(f"missing built route: {built}")
    else:
        built_text = built.read_text(encoding="utf-8")
        if built_text.count('class="topnav"') != 1:
            failures.append("built route must contain exactly one shared nav")
        if built_text.count('class="site-footer"') != 1:
            failures.append("built route must contain exactly one shared footer")
        for asset in ("/26/26-assets/rabbit.png", "/26/26-assets/photos/e25-04.jpg"):
            if asset not in built_text:
                failures.append(f"built route missing local asset reference: {asset}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    print("BFF27 validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
