#!/usr/bin/env python3
"""Validate BFF23/BFF24 archive pages and their generated local routes."""
from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

CASES = {
    "23": ("site/23.md", "/23/", "edition-page--bff23"),
    "24": ("site/24.md", "/24/", "edition-page--bff24"),
}
FORBIDDEN_SOURCE = re.compile(r"<(?:html|head|body|nav|footer|script|style)\b", re.I)
LOCAL_REF = re.compile(r"/(23|24)/(23|24)-assets/([^'\"\s}]+)")


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.urls: list[str] = []
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag.lower())
        for name, value in attrs:
            if name.lower() in {"src", "href", "poster"} and value:
                self.urls.append(value)

    def handle_data(self, data):
        self.text.append(data)


def metadata(source: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", source, re.S)
    if not match:
        return {}
    out = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([\w-]+):\s*(.*)$", line)
        if item:
            out[item.group(1)] = item.group(2).strip().strip("\"'")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("edition", choices=sorted(CASES), nargs="+")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--skip-built", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    failures: list[str] = []
    total_files = total_bytes = 0
    for edition in args.edition:
        page_rel, route, class_name = CASES[edition]
        source_path = root / page_rel
        asset_dir = root / "site" / edition / f"{edition}-assets"
        source = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
        if not source:
            failures.append(f"{edition}: missing source page {source_path}")
            continue
        meta = metadata(source)
        for key, expected in {"layout": "default", "permalink": route}.items():
            if meta.get(key) != expected:
                failures.append(f"{edition}: front matter {key} expected {expected!r}, got {meta.get(key)!r}")
        if class_name not in source:
            failures.append(f"{edition}: missing edition class {class_name}")
        if FORBIDDEN_SOURCE.search(source):
            failures.append(f"{edition}: standalone shell/script/style markup in source")
        if "wp-content/uploads" in source:
            failures.append(f"{edition}: WordPress asset dependency remains")
        assets = sorted(p for p in asset_dir.rglob("*") if p.is_file()) if asset_dir.is_dir() else []
        names = {p.name for p in assets}
        refs = LOCAL_REF.findall(source)
        if not assets:
            failures.append(f"{edition}: missing asset bundle")
        if len(refs) < 4:
            failures.append(f"{edition}: too few local asset references ({len(refs)})")
        for ref_edition, asset_edition, name in refs:
            if ref_edition != edition or asset_edition != edition or name not in names:
                failures.append(f"{edition}: missing referenced asset {name}")
        total_files += len(assets)
        total_bytes += sum(p.stat().st_size for p in assets)
        if not args.skip_built:
            built_path = root / "site" / "_site" / edition / "index.html"
            if not built_path.is_file():
                failures.append(f"{edition}: missing built route {built_path}")
            else:
                built = built_path.read_text(encoding="utf-8")
                parsed = Parser(); parsed.feed(built); parsed.close()
                if parsed.tags.count("nav") != 1 or parsed.tags.count("footer") != 1:
                    failures.append(f"{edition}: expected one shared nav/footer, got {parsed.tags.count('nav')}/{parsed.tags.count('footer')}")
                if class_name not in built or f"BFF’{edition}" not in "".join(parsed.text):
                    failures.append(f"{edition}: built route missing archive content")
                if "wp-content/uploads" in built:
                    failures.append(f"{edition}: built route contains WordPress asset dependency")
                for url in parsed.urls:
                    if url.startswith(f"/{edition}/{edition}-assets/") and url.rsplit("/", 1)[-1] not in names:
                        failures.append(f"{edition}: built route missing asset {url}")
    print(f"asset_count={total_files} asset_bytes={total_bytes}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print("archive validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
