#!/usr/bin/env python3
"""Validate the local-only BFF'25 page, its built route, and asset bundle."""
from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REQUIRED_FRONT_MATTER = {
    "layout": "default",
    "permalink": "/25/",
    "screen": "blue",
}
REQUIRED_MARKERS = (
    "BFF’25",
    "Beyond the Frame",
    "22–25 May 2025",
    "Kinoteka",
    "European Bitcoin Pizza Day",
    "Roger9000",
    "MadMunky",
    "Community Stage",
    "Pitching Rabbits",
    "€3,000",
    "Barbazaar afterparty",
    "Vistula afterparty",
    "Entrepreneurs Breakfast",
    "Golden Rabbits",
    "PoWies",
    "Full release",
    "Works in progress",
    "Trailers and others",
    "UNBANKABLE",
    "REVOLUCIÓN BITCOIN",
    "HOTEL BITCOIN",
    "NO MORE INFLATION",
    "SATOSHI: THE CREATION OF BITCOIN",
    "BITCOIN IS THE MYCELIUM OF MONEY",
    "STRANGE CURRENCIES",
    "Archive-only ticket tiers",
    "Why Bitcoin FilmFest?",
    "Why Warsaw?",
    "Travel &amp; Commute",
    "Bitcoin in Warsaw",
    "Why sponsor?",
    "How to submit my film?",
    "Best Movie",
    "Best Story",
    "Best Short",
    "Audience Choice",
    "Bitcoin Cinema Digest",
    "bff25-photo-rail",
)
FORBIDDEN_SOURCE_TAGS = re.compile(
    r"<(?:html|head|body|nav|footer|script|style)\b|cinema-seats",
    re.IGNORECASE,
)
LOCAL_REF = re.compile(
    r"\{\{\s*['\"]?/25/25-assets/([^'\"]+)['\"]?\s*\|\s*relative_url\s*\}\}"
)


class BuiltPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self.asset_urls: list[str] = []
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag.lower())
        for name, value in attrs:
            if name.lower() in {"src", "href", "poster"} and value:
                self.asset_urls.append(value)

    def handle_data(self, data: str) -> None:
        self.text.append(data)


def front_matter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", text, re.DOTALL)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if item:
            values[item.group(1)] = item.group(2).strip().strip('"\'')
    return values


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skip-built", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    source_path = root / "site" / "bff25.md"
    built_path = root / "site" / "_site" / "25" / "index.html"
    asset_dir = root / "site" / "25" / "25-assets"
    failures: list[str] = []

    if not source_path.is_file():
        fail(failures, f"missing source page: {source_path}")
        source = ""
    else:
        source = source_path.read_text(encoding="utf-8")

    metadata = front_matter(source)
    for key, expected in REQUIRED_FRONT_MATTER.items():
        if metadata.get(key) != expected:
            fail(failures, f"front matter {key} must be {expected!r}; found {metadata.get(key)!r}")
    if FORBIDDEN_SOURCE_TAGS.search(source):
        fail(failures, "source contains standalone shell markup or a forbidden script/style tag")
    for marker in REQUIRED_MARKERS:
        if marker not in source:
            fail(failures, f"source missing marker: {marker}")
    if "https://bitcoinfilmfest.com/wp-content/uploads/" in source:
        fail(failures, "source still depends on WordPress uploads")

    asset_files = sorted(p for p in asset_dir.rglob("*") if p.is_file()) if asset_dir.is_dir() else []
    asset_names = {p.name for p in asset_files}
    if not asset_files:
        fail(failures, f"missing asset bundle: {asset_dir}")
    local_refs = LOCAL_REF.findall(source)
    for name in local_refs:
        if name not in asset_names:
            fail(failures, f"missing local asset referenced by source: {name}")
    if len(local_refs) < 15:
        fail(failures, f"expected a substantial local asset bundle; found only {len(local_refs)} references")

    legacy_path = root / "site" / "bff25-legacy.md"
    if not legacy_path.is_file():
        fail(failures, f"missing compatibility page: {legacy_path}")
    else:
        legacy = legacy_path.read_text(encoding="utf-8")
        legacy_metadata = front_matter(legacy)
        if legacy_metadata.get("permalink") != "/bff25/" or legacy_metadata.get("redirect_to") != "/25/":
            fail(failures, "compatibility route must redirect /bff25/ to /25/")

    if not args.skip_built:
        if not built_path.is_file():
            fail(failures, f"missing built route: {built_path}")
        else:
            built = built_path.read_text(encoding="utf-8")
            built_parser = BuiltPageParser()
            built_parser.feed(built)
            built_parser.close()
            built_text = "".join(built_parser.text)
            if "BFF’25" not in built_text or "Beyond the Frame" not in built_text:
                fail(failures, "built route is missing BFF’25 page text")
            if "https://bitcoinfilmfest.com/wp-content/uploads/" in built:
                fail(failures, "built route still contains WordPress upload references")
            for url in built_parser.asset_urls:
                if url.startswith("/25/25-assets/"):
                    name = url.rsplit("/", 1)[-1]
                    if name not in asset_names:
                        fail(failures, f"built route references missing asset: {name}")
            if built_parser.tags.count("nav") != 1:
                fail(failures, f"built route expected shared nav only; found {built_parser.tags.count('nav')} nav tags")
            if built_parser.tags.count("footer") != 1:
                fail(failures, f"built route expected shared footer only; found {built_parser.tags.count('footer')} footer tags")

    byte_count = sum(p.stat().st_size for p in asset_files)
    print(f"asset_count={len(asset_files)} asset_bytes={byte_count} local_refs={len(local_refs)}")
    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1
    print("BFF25 validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
