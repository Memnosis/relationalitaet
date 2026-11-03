#!/usr/bin/env python3
"""Non-destructive P0 website integrity and navigation preflight.
Reports actual HTML files; does not merge, rewrite, or publish website pages.
Run: python forschung/website/website_p0_preflight.py
     python forschung/website/website_p0_preflight.py --strict
"""
from __future__ import annotations
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
PROTECTED = {
    "index.html": ["forschungswege"],
    "mitmachen.html": ["prompt-freigabe"],
    "tensoralgebra.html": ["prompt-ebenen", "algebra-weiterentwickeln"],
}
NAV_SCRIPTS = {"tensor-hierarchy.js", "site-nav.js"}

class Scanner(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []
        self.ids = []
        self.scripts = []
        self.nav_count = 0
        self.mains = 0
        self.h1 = 0
        self.images_without_alt = 0
        self.header_nav = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "name" in a:
            self.ids.append(a["name"])
        if tag == "nav":
            self.nav_count += 1
        if tag == "main":
            self.mains += 1
        if tag == "h1":
            self.h1 += 1
        if tag == "img" and "alt" not in a:
            self.images_without_alt += 1
        for att in ("href", "src"):
            if a.get(att):
                self.refs.append(a[att])
        if tag == "script" and a.get("src"):
            self.scripts.append(a["src"])

def audit():
    pages = sorted(DOCS.glob("*.html"))
    scans = {}
    findings = []
    for p in pages:
        s = Scanner()
        try:
            s.feed(p.read_text(encoding="utf-8"))
            scans[p.name] = s
        except (OSError, UnicodeError, ValueError) as e:
            findings.append({"severity":"error","page":p.name,"kind":"parse","detail":str(e)})
            continue
        scripts = [Path(urlsplit(x).path).name for x in s.scripts]
        active = sorted(NAV_SCRIPTS.intersection(scripts))
        if len(active) > 1:
            findings.append({"severity":"error","page":p.name,"kind":"two_navigation_engines","detail":active})
        elif len(active) == 0:
            findings.append({"severity":"review","page":p.name,"kind":"no_global_nav_script","detail":"Check fallback and intended exception"})
        if s.nav_count == 0:
            findings.append({"severity":"review","page":p.name,"kind":"no_nav_fallback","detail":"No static nav element"})
        if s.mains != 1:
            findings.append({"severity":"review","page":p.name,"kind":"main_count","detail":s.mains})
        if s.h1 != 1:
            findings.append({"severity":"review","page":p.name,"kind":"h1_count","detail":s.h1})
        if s.images_without_alt:
            findings.append({"severity":"review","page":p.name,"kind":"image_without_alt","detail":s.images_without_alt})
        ids = Counter(s.ids)
        for key, n in ids.items():
            if n > 1:
                findings.append({"severity":"error","page":p.name,"kind":"duplicate_id","detail":key})
        for key in PROTECTED.get(p.name, []):
            if ids[key] != 1:
                findings.append({"severity":"error","page":p.name,"kind":"protected_anchor","detail":{"id":key,"count":ids[key]}})
    for p in pages:
        s = scans.get(p.name)
        if not s:
            continue
        for raw in s.refs:
            if raw.startswith(("mailto:", "tel:", "javascript:", "data:")) or raw.startswith("//"):
                continue
            u = urlsplit(raw)
            if u.scheme or u.netloc:
                continue
            target = (p.parent / unquote(u.path)).resolve() if u.path else p
            try:
                target.relative_to(DOCS.resolve())
            except ValueError:
                continue  # external asset above docs belongs to another scan scope
            if not target.exists():
                findings.append({"severity":"error","page":p.name,"kind":"missing_local_target","detail":raw})
            elif u.fragment and target.suffix.lower() == ".html":
                dest = scans.get(target.name)
                if dest and unquote(u.fragment) not in dest.ids:
                    findings.append({"severity":"error","page":p.name,"kind":"missing_anchor","detail":raw})
    return {"schema":"website-preflight/0.1","pages":len(pages),
            "protected_anchors":PROTECTED,
            "counts":dict(Counter(x["severity"] for x in findings)),
            "findings":findings,
            "important":"Static-only audit; no browser, touch, keyboard or screenreader test is implied."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail if any static error is found")
    args = parser.parse_args()
    report = audit()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.strict and report["counts"].get("error",0):
        raise SystemExit(1)
