#!/usr/bin/env python3
"""No-loss static smoke test of the eight selectively imported web pages.

This covers local file links, scripts, asset paths, JSON syntax and navigation.
It is NOT a live browser, keyboard or screen-reader test.
"""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/"docs"
NAMES=[
    "ki-systeme.html","ki-kernforschung.html","codebuch.html",
    "soulution-schroedingers-inkubator.html","soulution-inkubator-quellen.html",
    "soulution-ki-kreativrechte.html","soulution-weltwissen-dividende.html",
    "wissen-macht-wirklichkeit.html"
]
errors=[]
class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls=[]
        self.ids=set()
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if d.get("id"):self.ids.add(d["id"])
        for k in ("href","src"):
            if d.get(k):self.urls.append((tag,k,d[k]))
for name in NAMES:
    page=DOCS/name
    if not page.is_file():
        errors.append("missing page "+name);continue
    html=page.read_text(encoding="utf-8")
    scan=Scan()
    scan.feed(html)
    if "tensor-hierarchy.js" not in html:
        errors.append(name+" missing approved navigation")
    if "site-nav.js" in html:
        errors.append(name+" has conflicting legacy navigation")
    if "<html" not in html or "</html>" not in html:
        errors.append(name+" invalid top-level HTML")
    for tag,attr,raw in scan.urls:
        u=urlsplit(raw)
        if u.scheme or u.netloc or raw.startswith(("mailto:","tel:","data:","#")):
            continue
        target=(page.parent / unquote(u.path)).resolve() if u.path else page.resolve()
        try:target.relative_to(DOCS)
        except ValueError:
            errors.append(name+" link escapes docs: "+raw);continue
        if not target.is_file() and not target.is_dir():
            errors.append(name+" broken relative link: "+raw)
for data in ("codebuch-web-index.json","inkubator-quellenregister.json"):
    p=DOCS/"data"/data
    if not p.is_file():errors.append("missing source JSON "+data)
    else:json.loads(p.read_text(encoding="utf-8"))
index=(ROOT/"forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json")
if not index.is_file():errors.append("missing recent-prompt coverage ledger")
else:
    d=json.loads(index.read_text(encoding="utf-8"))
    if d.get("verified_exact_100_message_sequence") is not False:
        errors.append("must not claim exact 100 prompt sequence")
    ids=[x["id"] for x in d["requirements"]]
    if len(ids)!=len(set(ids)):errors.append("duplicate requirement IDs")
    if d["requirements_count"]!=len(ids):errors.append("requirements count mismatch")
    for x in d["requirements"]:
        ev=ROOT/x["evidence"]
        if not ev.exists():errors.append(x["id"]+" missing linked evidence "+x["evidence"])
        if x.get("original_text_verified"):errors.append(x["id"]+" ungrounded original message claim")
print("Integration:",len(NAMES),"pages and",len(errors),"static findings")
for e in errors:print("ERROR:",e)
if errors:sys.exit(1)
print("PASS: file/link/JSON/no-loss static checks only")
