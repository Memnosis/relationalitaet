#!/usr/bin/env python3
"""No-dependency No-Loss audit for docs/*.html: links, anchors, assets, navigation and ids.

Run from repository root: python scripts/audit_website.py
Exit nonzero for missing internal links, anchors, assets or inconsistent main navigation.
Does not render a browser or validate externally hosted content.
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
import urllib.parse
from collections import Counter
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = "memnosis.github.io"
PROJECT = "/relationalitaet/"
NAV = ("Start", "KI", "Tensor", "Projekte", "Harvesting", "Publikationen", "Mitmachen", "SOULution")

class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []
        self.h1 = 0
        self.nav_main = 0
        self.in_main_nav = False
        self.nav_titles = []
        self._nav_depth = 0
        self._in_nav_link = False
        self._nav_words = []
        self.legacy = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.append(d["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "nav" and d.get("aria-label") == "Hauptnavigation":
            self.nav_main += 1
            self.in_main_nav = True
            self._nav_depth = 1
        elif tag == "nav" and self.in_main_nav:
            self._nav_depth += 1
        if self.in_main_nav and tag == "a":
            self._in_nav_link = True
            self._nav_words = []
        if tag in ("a", "use", "script", "img", "link", "source"):
            for attr in ("href", "src", "srcset"):
                if d.get(attr):
                    self.refs.append((tag, attr, d[attr]))
        if tag == "script" and "tensor-hierarchy.js" in d.get("src", ""):
            self.legacy = True

    def handle_data(self, data):
        if self._in_nav_link:
            self._nav_words.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._in_nav_link:
            name = "".join(self._nav_words).strip()
            if name:
                self.nav_titles.append(name)
            self._in_nav_link = False
        if tag == "nav" and self.in_main_nav:
            self._nav_depth -= 1
            if self._nav_depth == 0:
                self.in_main_nav = False

def main() -> int:
    pages = {p.resolve(): p for p in DOCS.rglob("*.html")}
    scans = {}
    errors, warnings = [], []

    for path in pages:
        try:
            text = path.read_text(encoding="utf-8")
            o = Scan()
            o.feed(text)
            scans[path] = o
            duplicates = [name for name, n in Counter(o.ids).items() if n > 1]
            if duplicates:
                errors.append((path, "duplicate ids: " + ", ".join(duplicates)))
            if o.nav_main != 1:
                errors.append((path, f"expected one Hauptnavigation, got {o.nav_main}"))
            elif tuple(o.nav_titles) != NAV:
                errors.append((path, "navigation differs: " + repr(o.nav_titles)))
            if o.legacy:
                errors.append((path, "obsolete tensor-hierarchy.js is active"))
            if o.h1 != 1:
                warnings.append((path, f"expected one h1, got {o.h1}"))
            if "repeat(4," in text or "repeat( 4," in text:
                warnings.append((path, "possible 4-column CSS requires inspection"))
        except Exception as e:
            errors.append((path, "parse error: " + str(e)))

    # Some valid anchors are generated from the public task register on page load.
    dynamic = {}
    public_tasks = DOCS / "data" / "mitmach-public-v2.json"
    if public_tasks.exists():
        try:
            dynamic[(DOCS / "mitmachen.html").resolve()] = {
                t["id"] for t in json.loads(public_tasks.read_text(encoding="utf-8"))["tasks"]
            }
        except (OSError, KeyError, ValueError) as e:
            errors.append((public_tasks, "unreadable dynamic task IDs: " + str(e)))

    for source, o in scans.items():
        for tag, attr, raw in o.refs:
            if raw.startswith(("mailto:", "tel:", "data:", "blob:")):
                continue
            if raw.startswith("javascript:"):
                errors.append((source, "javascript: URL not permitted"))
                continue
            if attr == "srcset":
                # future enhancement: srcset size-descriptor parser
                continue
            url = urllib.parse.urlparse(raw)
            if url.scheme in ("http", "https"):
                if url.netloc.lower() != SITE:
                    continue  # external resources are outside the static audit
                if not url.path.startswith(PROJECT):
                    continue
                rel = url.path[len(PROJECT):]
                target = (DOCS / rel).resolve()
            elif url.scheme:
                continue
            elif raw.startswith("#"):
                target = source
            elif raw.startswith("/"):
                warnings.append((source, "root-relative URL needs manual check: " + raw))
                continue
            else:
                target = (source.parent / urllib.parse.unquote(url.path)).resolve()

            if not target.is_relative_to(DOCS.resolve()):
                errors.append((source, "path outside docs: " + raw))
                continue
            if not target.is_file():
                errors.append((source, "missing local file: " + raw))
                continue
            if url.fragment:
                frag = urllib.parse.unquote(url.fragment)
                if frag and target.suffix.lower() == ".html":
                    dest = scans.get(target)
                    if dest and frag not in dest.ids and frag not in dynamic.get(target, set()):
                        errors.append((source, "missing target anchor: " + raw))
                elif target.suffix.lower() == ".svg":
                    # SVG sprite fragment must be an existing symbol, not just an existing file.
                    svg = target.read_text(encoding="utf-8")
                    if not re.search(r'<(?:symbol|g)\\b[^>]*\\bid=["\\\']' + re.escape(frag) + r'["\\\']', svg):
                        errors.append((source, "missing SVG sprite symbol: " + raw))

    inventory = DOCS / "data" / "tensor-inventar-v10_7.json"
    if inventory.exists():
        try:
            data = json.loads(inventory.read_text(encoding="utf-8"))
            records = data["tensors"]
            if len(records) != 103 or sum(len(t["axes"]) for t in records) != 309:
                errors.append((inventory, "historical tensor and triad totals differ from 103/309"))
        except Exception as e:
            errors.append((inventory, "JSON invalid: " + str(e)))

    print(f"Audited {len(scans)} HTML pages; errors={len(errors)} warnings={len(warnings)}")
    for path, msg in errors:
        print("ERROR", str(path.relative_to(ROOT)), msg)
    for path, msg in warnings:
        print("WARN ", str(path.relative_to(ROOT)), msg)
    print("External links, JavaScript interactions, CSS render output and mobile screenshots require separate browser tests.")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
