#!/usr/bin/env python3
"""Validate the BFF'26 source page, built route, and legacy asset references."""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


FRONT_MATTER_BLOCK = re.compile(
    r"\A---[ \t]*\r?\n(?P<contents>.*?)(?:^---[ \t]*(?:\r?\n|\Z))",
    re.MULTILINE | re.DOTALL,
)
FRONT_MATTER_ASSIGNMENT = re.compile(
    r"^(?P<indent>[ \t]*)(?P<key>[A-Za-z0-9_-]+)[ \t]*:[ \t]*(?P<raw>.*)$"
)
CSS_URL_START = re.compile(r"url\s*\(", re.IGNORECASE)
ASSET_ROOT_MARKER = "/26/26-assets/"
HTML_ASSET_ATTRIBUTES = frozenset(
    {
        "src",
        "href",
        "poster",
        "data-src",
        "data-lazy-src",
        "data-original",
        "data-background-image",
        "srcset",
        "imagesrcset",
        "data-srcset",
    }
)
SHELL_TAGS = frozenset({"html", "head", "body"})
EXPECTED_DOCUMENT_SEQUENCE = (
    "doctype",
    "start:html",
    "start:head",
    "end:head",
    "start:body",
    "end:body",
    "end:html",
)
VOID_HTML_TAGS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)


class DocumentParser(HTMLParser):
    """Collect ordered, nested HTML tokens without treating comments as content."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.shell_events: list[str] = []
        self.doctypes: list[str] = []
        self.document_text: list[str] = []
        self.body_text: list[str] = []
        self.html_asset_urls: list[str] = []
        self.css_text: list[str] = []
        self.start_tag_classes: list[tuple[str, set[str]]] = []
        self.shared_nav_count = 0
        self.shared_footer_count = 0
        self.out_of_body_nav_count = 0
        self.out_of_body_footer_count = 0
        self.nesting_errors: list[str] = []
        self._tag_stack: list[str] = []
        self._raw_tag: str | None = None

    @staticmethod
    def _class_tokens(attrs: list[tuple[str, str | None]]) -> set[str]:
        for name, value in attrs:
            if name.lower() == "class" and value:
                return set(value.split())
        return set()

    def _record_start(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
        self_closing: bool = False,
    ) -> None:
        tag = tag.lower()
        if tag in SHELL_TAGS:
            self.shell_events.append(f"start:{tag}")
        classes = self._class_tokens(attrs)
        self.start_tag_classes.append((tag, classes))
        in_body = "body" in self._tag_stack
        if tag == "nav" and "topnav" in classes:
            if in_body:
                self.shared_nav_count += 1
            else:
                self.out_of_body_nav_count += 1
        if tag == "footer" and "site-footer" in classes:
            if in_body:
                self.shared_footer_count += 1
            else:
                self.out_of_body_footer_count += 1

        for name, value in attrs:
            name = name.lower()
            if value is None:
                continue
            if name in HTML_ASSET_ATTRIBUTES:
                if name in {"srcset", "imagesrcset", "data-srcset"}:
                    self.html_asset_urls.extend(
                        candidate.strip().split()[0]
                        for candidate in value.split(",")
                        if candidate.strip()
                    )
                else:
                    self.html_asset_urls.append(value)
            if name == "style":
                self.css_text.append(value)

        if tag in {"script", "style"} and not self_closing:
            self._raw_tag = tag
        if self_closing and tag in SHELL_TAGS:
            self.shell_events.append(f"end:{tag}")
        if not self_closing and tag not in VOID_HTML_TAGS:
            self._tag_stack.append(tag)

    def handle_decl(self, decl: str) -> None:
        if re.match(r"doctype\b", decl, re.IGNORECASE):
            self.doctypes.append(decl)
            self.shell_events.append("doctype")

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self._record_start(tag, attrs)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self._record_start(tag, attrs, self_closing=True)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in SHELL_TAGS:
            self.shell_events.append(f"end:{tag}")
        if self._raw_tag == tag:
            self._raw_tag = None
        if tag in VOID_HTML_TAGS:
            return
        if not self._tag_stack:
            self.nesting_errors.append(f"unexpected closing </{tag}>")
            return
        if self._tag_stack[-1] != tag:
            self.nesting_errors.append(
                f"mismatched closing </{tag}> (open <{self._tag_stack[-1]}>)"
            )
            if tag in self._tag_stack:
                del self._tag_stack[self._tag_stack.index(tag) :]
            return
        self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._raw_tag is not None:
            if self._raw_tag == "style":
                self.css_text.append(data)
            return
        self.document_text.append(data)
        if "body" in self._tag_stack:
            self.body_text.append(data)


def read_text(path: Path, label: str, failures: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        failures.append(f"{label}: invalid UTF-8 in {path} ({exc})")
    except OSError as exc:
        failures.append(f"{label}: cannot read {path} ({exc})")
    return None


def front_matter_value(raw: str) -> str | None:
    """Return one simple YAML scalar, rejecting unterminated/mixed quotes."""
    raw = raw.strip()
    if not raw:
        return None

    if raw[0] in {'"', "'"}:
        quote = raw[0]
        escaped = False
        for index in range(1, len(raw)):
            char = raw[index]
            if quote == '"' and char == "\\" and not escaped:
                escaped = True
                continue
            if char == quote and not escaped:
                suffix = raw[index + 1 :].strip()
                if suffix and not suffix.startswith("#"):
                    return None
                return raw[1:index]
            escaped = False
        return None

    comment = re.search(r"[ \t]#", raw)
    value = raw[: comment.start()] if comment else raw
    value = value.strip()
    if not value or any(quote in value for quote in {'"', "'"}):
        return None
    return value


def front_matter_assignments(
    text: str, failures: list[str] | None = None
) -> dict[str, str]:
    front_matter = FRONT_MATTER_BLOCK.match(text)
    if front_matter is None:
        if failures is not None:
            failures.append("source: missing initial YAML front matter")
        return {}

    assignments: dict[str, str] = {}
    seen: set[str] = set()
    target_keys = {"layout", "permalink"}
    for line in front_matter.group("contents").splitlines():
        assignment = FRONT_MATTER_ASSIGNMENT.match(line)
        if assignment is None:
            continue
        key = assignment.group("key")
        indent = assignment.group("indent")
        if indent and key in target_keys:
            if failures is not None:
                failures.append(
                    f"source: {key} assignment must be top-level (column 0)"
                )
            continue
        if not indent and key in seen:
            if failures is not None:
                failures.append(f"source: duplicate top-level {key} assignment")
            continue
        if indent:
            continue
        seen.add(key)
        value = front_matter_value(assignment.group("raw"))
        if value is None:
            if failures is not None and key in target_keys:
                failures.append(f"source: malformed {key} assignment quotes")
            continue
        assignments[key] = value
    return assignments


def front_matter_has(text: str, key: str, value: str) -> bool:
    return front_matter_assignments(text).get(key) == value


def parse_html(text: str, label: str, failures: list[str]) -> DocumentParser | None:
    parser = DocumentParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # HTMLParser should be permissive, but never traceback.
        failures.append(f"{label}: malformed HTML ({exc})")
        return None
    if parser.nesting_errors or parser._tag_stack:
        details = parser.nesting_errors[:]
        if parser._tag_stack:
            details.append(
                "unclosed " + ", ".join(f"<{tag}>" for tag in parser._tag_stack)
            )
        failures.append(f"{label}: malformed HTML nesting ({'; '.join(details)})")
    return parser


def validate_source(text: str, failures: list[str]) -> None:
    assignments = front_matter_assignments(text, failures)
    if assignments.get("layout") != "default":
        failures.append("source: missing layout: default")
    if assignments.get("permalink") != "/26/":
        failures.append("source: missing permalink: /26/")

    parser = parse_html(text, "source", failures)
    if parser is None:
        return

    if "start:html" in parser.shell_events:
        failures.append("source: document shell marker <html")
    if "start:head" in parser.shell_events:
        failures.append("source: document shell marker <head")
    if "start:body" in parser.shell_events:
        failures.append("source: document shell marker <body")
    if parser.shared_nav_count or parser.out_of_body_nav_count:
        failures.append("source: document shell marker <nav class=\"topnav")
    if any(tag == "footer" for tag, _classes in parser.start_tag_classes):
        failures.append("source: document shell marker <footer")
    if any(
        tag == "img" and "cinema-seats" in classes
        for tag, classes in parser.start_tag_classes
    ):
        failures.append("source: document shell marker <img class=\"cinema-seats")


def validate_built(text: str, assets: Path, failures: list[str]) -> None:
    parser = parse_html(text, "built", failures)
    if parser is None:
        return

    if len(parser.doctypes) != 1:
        failures.append(
            "built: expected exactly one doctype declaration "
            f"(found {len(parser.doctypes)})"
        )
    html_doctypes = [
        decl
        for decl in parser.doctypes
        if re.match(r"doctype\s+html\b", decl, re.IGNORECASE)
    ]
    if len(html_doctypes) != 1:
        failures.append("built: doctype declaration is not HTML")

    if tuple(parser.shell_events) != EXPECTED_DOCUMENT_SEQUENCE:
        found = ", ".join(parser.shell_events) or "none"
        expected = ", ".join(EXPECTED_DOCUMENT_SEQUENCE)
        failures.append(
            f"built: invalid HTML document sequence/order "
            f"(expected {expected}; found {found})"
        )

    if parser.out_of_body_nav_count:
        failures.append("built: shared nav marker outside <body>")
    if parser.out_of_body_footer_count:
        failures.append("built: shared footer marker outside <body>")

    visible_text = "".join(parser.body_text)
    marker_checks = (
        ("<!DOCTYPE html>", len(html_doctypes) == 1),
        (
            'shared nav marker <nav class="topnav',
            parser.shared_nav_count > 0,
        ),
        (
            'shared footer marker <footer class="site-footer',
            parser.shared_footer_count > 0,
        ),
        ("BFF’26", "BFF’26" in visible_text),
        ("Golden Rabbits", "Golden Rabbits" in visible_text),
        ("AI Contest", "AI Contest" in visible_text),
        ("MoneroKon", "MoneroKon" in visible_text),
        ("Warsaw", "Warsaw" in visible_text),
        ("BFF’27", "BFF’27" in visible_text),
    )
    for name, present in marker_checks:
        if not present:
            failures.append(f"built: missing {name}")

    if parser.shared_nav_count > 1:
        failures.append('built: duplicate shared nav marker <nav class="topnav')
    if parser.shared_footer_count > 1:
        failures.append(
            'built: duplicate shared footer marker <footer class="site-footer'
        )

    check_assets(
        text,
        assets,
        failures,
        parser.html_asset_urls,
        parser.css_text,
    )


def css_url_references(
    css_blocks: list[str], failures: list[str]
) -> list[str]:
    """Extract CSS url() values and name malformed/unclosed constructs."""
    references: list[str] = []
    for css in css_blocks:
        without_comments: list[str] = []
        index = 0
        while index < len(css):
            if css.startswith("/*", index):
                end = css.find("*/", index + 2)
                if end < 0:
                    break
                index = end + 2
                continue
            without_comments.append(css[index])
            index += 1
        cleaned = "".join(without_comments)

        index = 0
        while True:
            match = CSS_URL_START.search(cleaned, index)
            if match is None:
                break
            cursor = match.end()
            while cursor < len(cleaned) and cleaned[cursor].isspace():
                cursor += 1
            if cursor >= len(cleaned):
                failures.append("assets: unclosed CSS url()")
                break

            quote = cleaned[cursor] if cleaned[cursor] in {'"', "'"} else None
            if quote is not None:
                value_start = cursor + 1
                cursor = value_start
                escaped = False
                while cursor < len(cleaned):
                    char = cleaned[cursor]
                    if char == quote and not escaped:
                        break
                    if char == "\\" and not escaped:
                        escaped = True
                    else:
                        escaped = False
                    cursor += 1
                if cursor >= len(cleaned):
                    failures.append("assets: malformed CSS url()")
                    break
                value = cleaned[value_start:cursor]
                cursor += 1
                while cursor < len(cleaned) and cleaned[cursor].isspace():
                    cursor += 1
                if cursor >= len(cleaned) or cleaned[cursor] != ")":
                    failures.append("assets: malformed CSS url()")
                    index = cursor
                    continue
            else:
                value_start = cursor
                while cursor < len(cleaned) and cleaned[cursor] != ")":
                    if cleaned[cursor] in {'"', "'"}:
                        failures.append("assets: malformed CSS url()")
                        break
                    cursor += 1
                if cursor >= len(cleaned):
                    failures.append("assets: unclosed CSS url()")
                    break
                if cleaned[cursor] != ")":
                    index = cursor + 1
                    continue
                value = cleaned[value_start:cursor]

            if value.strip():
                references.append(value)
            index = cursor + 1
    return references


def check_assets(
    text: str,
    assets: Path,
    failures: list[str],
    html_asset_urls: list[str] | None = None,
    css_blocks: list[str] | None = None,
) -> None:
    try:
        asset_root = assets.resolve()
    except (OSError, RuntimeError) as exc:
        failures.append(f"assets: cannot resolve --assets {assets} ({exc})")
        return

    if not asset_root.is_dir():
        failures.append(f"assets: directory not found {assets}")
        return

    seen: set[str] = set()
    references = list(html_asset_urls) if html_asset_urls is not None else []
    css_sources = css_blocks if css_blocks is not None else [text]
    references.extend(css_url_references(css_sources, failures))
    for raw_reference in references:
        raw_url = raw_reference.strip()
        if (
            not raw_url
            or "\x00" in raw_url
            or any(ord(char) < 0x20 for char in raw_url)
            or re.search(r"%(?![0-9A-Fa-f]{2})", raw_url)
        ):
            failures.append(f"assets: malformed URL {raw_url!r}")
            continue
        try:
            parsed = urlsplit(raw_url)
            # Access these properties too: urlsplit defers invalid-host/port checks
            # until the parsed result is inspected.
            _ = parsed.hostname
            _ = parsed.port
        except ValueError:
            failures.append(f"assets: malformed URL {raw_url!r}")
            continue

        if parsed.scheme or parsed.netloc:
            continue

        path = unquote(parsed.path).replace("\\", "/")
        marker_index = path.find(ASSET_ROOT_MARKER)
        if marker_index < 0:
            continue
        relative = path[marker_index + len(ASSET_ROOT_MARKER) :]
        normalized_relative = posixpath.normpath(relative)
        if normalized_relative in seen:
            continue
        seen.add(normalized_relative)

        try:
            candidate = (
                asset_root / Path(*normalized_relative.split("/"))
            ).resolve()
        except (OSError, RuntimeError, ValueError) as exc:
            failures.append(
                f"assets: cannot resolve reference {normalized_relative} ({exc})"
            )
            continue

        try:
            candidate.relative_to(asset_root)
        except ValueError:
            failures.append(
                f"assets: reference escapes --assets {normalized_relative}"
            )
            continue
        if not candidate.is_file():
            failures.append(f"assets: missing {normalized_relative}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="Jekyll source page")
    parser.add_argument("--built", required=True, type=Path, help="built HTML route")
    parser.add_argument("--assets", required=True, type=Path, help="legacy 26-assets directory")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    failures: list[str] = []

    source_text = read_text(args.source, "source", failures)
    built_text = read_text(args.built, "built", failures)

    if source_text is not None:
        validate_source(source_text, failures)
    if built_text is not None:
        validate_built(built_text, args.assets, failures)

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("PASS BFF’26 page validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
