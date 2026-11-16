#!/usr/bin/env python3
"""Write Markdown copies of built pages for AI agents and crawlers.

Runs after `jekyll build` (see .github/workflows/deploy-pages.yml). The shared
Jekyll head (site/_includes/head-meta.html) emits this tag on indexable pages:

    <link rel="alternate" type="text/markdown" href="/about/index.md">

For every built HTML file that carries the tag, this script writes a Markdown
copy to the address in href, inside the built site. The link and the file come
from the same build, so they cannot disagree.

Exit 1 when: a copy is shorter than 300 characters, a link points outside the
site (or is not a .md path), a linked page is noindex, a linked page has no
canonical URL, or no page carries the link at all.

html_to_md is vendored from ai-doors/ai_doors.py (2026-10-26), including the
live-widget and JS-placeholder stripping. Needs beautifulsoup4, lxml, markdownify.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse as up
from pathlib import Path

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify

MIN_CHARS = 300


# ---------------------------------------------------------------- html -> md
# Vendored from ai_doors.py. Keep the two in step when either changes.

def meta(soup, *names):
    for n in names:
        t = soup.find("meta", attrs={"property": n}) or soup.find("meta", attrs={"name": n})
        if t and t.get("content"):
            return t["content"].strip()
    return None


def jsonld_dates(soup):
    pub = mod = None
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
        except Exception:
            continue
        stack = [data]
        while stack:
            d = stack.pop()
            if isinstance(d, list):
                stack.extend(d)
            elif isinstance(d, dict):
                pub = pub or d.get("datePublished")
                mod = mod or d.get("dateModified")
                stack.extend(v for v in d.values() if isinstance(v, (dict, list)))
    return pub, mod


def html_to_md(html, url):
    soup = BeautifulSoup(html, "lxml")
    title = (meta(soup, "og:title") or (soup.title.string if soup.title else "") or url).strip()
    desc = meta(soup, "description", "og:description")
    pub, mod = jsonld_dates(soup)
    pub = pub or meta(soup, "article:published_time")
    mod = mod or meta(soup, "article:modified_time")
    noindex = "noindex" in (meta(soup, "robots") or "").lower()

    container = (soup.find("main") or soup.find("article")
                 or soup.find(attrs={"role": "main"}) or soup.body or soup)
    for c in container.find_all(string=lambda x: isinstance(x, Comment)):
        c.extract()
    kill = ["script", "style", "noscript", "svg", "iframe", "form", "nav", "footer",
            "aside", "button", "template", "dialog", "canvas", "video", "audio"]
    if container.name == "body":
        kill.append("header")
    for t in container.find_all(kill):
        t.decompose()
    for t in container.find_all(attrs={"hidden": True}):
        t.decompose()
    for t in container.find_all(attrs={"aria-hidden": "true"}):
        t.decompose()
    # live widgets (clocks, tickers, timers) are noise in a static copy
    for t in container.find_all(attrs={"aria-live": True}):
        t.decompose()
    for t in container.find_all(attrs={"role": ["timer", "marquee", "status"]}):
        t.decompose()
    widget = re.compile(r"(^|[-_ ])(clock|ticker|countdown|timer)([-_ ]|$)", re.I)
    for t in container.find_all(class_=widget) + container.find_all(id=widget):
        if t.parent is not None:
            # drop the whole small wrapper (e.g. "<span>[icon] <b id=clock>--:--</b> local</span>")
            wrap = t.parent if t.parent is not container and len(t.parent.get_text(strip=True)) < 60 else t
            wrap.decompose()
    # JS placeholders that only make sense before a script fills them in
    placeholder = re.compile(
        r"^(loading\b.*|[-–—]{1,3}\s*(°\s*[CF]|%|km/h|kts?|mph|m|cm)?|…|\.\.\.|feels like\s*…?|"
        r"[-–—]{1,2}:[-–—]{1,2}(:[-–—]{1,2})?)$", re.I)
    for t in list(container.find_all(True)):
        if t.parent is None or t.find(["img", "a", "h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]):
            continue
        txt = t.get_text(" ", strip=True)
        if txt and len(txt) < 80 and placeholder.match(txt):
            t.decompose()
    # badges glued to heading text ("...exist nowReal"): separate inline children with a space
    for h in container.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        for el in h.find_all(["span", "small", "em", "b", "strong", "mark", "abbr"]):
            prev = el.previous_sibling
            if prev is not None and isinstance(prev, str) and prev and not prev[-1].isspace():
                el.insert_before(" ")
    for a in container.find_all("a", href=True):
        a["href"] = up.urljoin(url, a["href"])
    for img in container.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if src:
            img["src"] = up.urljoin(url, src)
        else:
            img.decompose()

    body = markdownify(str(container), heading_style="ATX", bullets="-",
                       strip=["picture", "source"])
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    head = []
    if not re.match(r"^# ", body):
        head.append(f"# {title}\n")
    head.append(f"Source: {url}  ")
    if pub:
        head.append(f"Published: {pub[:10]}  ")
    if mod:
        head.append(f"Updated: {mod[:10]}  ")
    if desc:
        head.append(f"\n> {desc}")
    return "\n".join(head).rstrip() + "\n\n" + body + "\n", title, desc, noindex


# ---------------------------------------------------------------- build step

def link_target(href, site, baseurl=""):
    """File inside site for a link href, or None if the link points outside the site.

    baseurl is the Jekyll baseurl the page was built with (e.g. /bitcoinfilmfest-com
    for the github-pages config). It is not a folder in _site, so it is stripped.
    """
    if not href or "\\" in href:
        return None
    parts = up.urlsplit(href)
    if parts.scheme or parts.netloc or not parts.path.startswith("/") or parts.path.startswith("//"):
        return None
    path = up.unquote(parts.path)
    if baseurl:
        if not path.startswith(baseurl + "/"):
            return None
        path = path[len(baseurl):]
    if not path.endswith(".md"):
        return None
    dest = (site / path.lstrip("/")).resolve()
    try:
        dest.relative_to(site)
    except ValueError:
        return None
    return dest


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="site/_site", help="built site (Jekyll destination)")
    ap.add_argument("--baseurl", default="", help="Jekyll baseurl used for the build ('' for production)")
    a = ap.parse_args()
    site = Path(a.site).resolve()
    if not site.is_dir():
        sys.exit(f"ERROR site folder not found: {site}")

    html_files = sorted(site.rglob("*.html"))
    errors, copies, linked_pages = [], [], 0
    for f in html_files:
        text = f.read_text(encoding="utf-8")
        if 'type="text/markdown"' not in text:
            continue
        soup = BeautifulSoup(text, "lxml")
        hrefs = [t.get("href") for t in soup.find_all("link", attrs={"rel": "alternate", "type": "text/markdown"})]
        if not hrefs:
            continue
        rel = f.relative_to(site).as_posix()
        linked_pages += 1
        canon = soup.find("link", attrs={"rel": "canonical"})
        if canon is None or not canon.get("href"):
            errors.append(f"{rel}: no canonical URL, cannot resolve the copy")
            continue
        md, _title, _desc, noindex = html_to_md(text, canon["href"])
        if noindex:
            errors.append(f"{rel}: has a Markdown link but is noindex")
            continue
        for href in hrefs:
            dest = link_target(href, site, a.baseurl)
            if dest is None:
                errors.append(f"{rel}: link points outside the site or is not a .md path: {href!r}")
                continue
            if len(md) < MIN_CHARS:
                errors.append(f"{rel}: copy for {href} is {len(md)} chars (< {MIN_CHARS})")
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(md, encoding="utf-8", newline="\n")
            copies.append(href)

    sitemap = site / "sitemap.xml"
    loc_count = sitemap.read_text(encoding="utf-8").count("<loc>") if sitemap.exists() else 0
    if linked_pages == 0:
        errors.append("no built page carries the Markdown link: is _includes/head-meta.html in the build?")

    for e in errors:
        print("ERROR", e)
    print(f"built HTML files: {len(html_files)}")
    print(f"pages with a Markdown link: {linked_pages}")
    print(f"Markdown copies written: {len(copies)}")
    print(f"sitemap.xml <loc> entries: {loc_count}")
    if errors:
        print(f"FAILED: {len(errors)} error(s); see above")
        sys.exit(1)
    print("OK: every link has a copy of at least", MIN_CHARS, "characters")


if __name__ == "__main__":
    main()
