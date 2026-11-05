#!/usr/bin/env python3
"""No-loss website smoke test for the 34 documented pages.

Validates existing pages, common navigation, local assets/links,
known source JSON files, and the 72 traceable requirement IDs.
It does not certify live GitHub Pages, browser behavior or science.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = ROOT / "forschung/website/seiten/README.md"
errors = []
warnings = []


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.add(d["id"])
        for attr in ("href", "src"):
            if d.get(attr):
                self.urls.append((attr, d[attr]))


text = INDEX.read_text(encoding="utf-8")
slugs = list(dict.fromkeys(re.findall(r"\./([a-z0-9-]+)_AUDIT_PLAN_2026-11-03\.md", text)))
if len(slugs) != 34:
    errors.append("expected 34 independently documented pages, got " + str(len(slugs)))
scans = {}
all_links = 0

for slug in slugs:
    name = slug + ".html"
    page = DOCS / name
    if not page.is_file():
        errors.append("missing audited page: " + name)
        continue
    html = page.read_text(encoding="utf-8")
    parser = Scan()
    parser.feed(html)
    scans[name] = parser
    if "website-unified.js" not in html or "ux-site-nav" not in html:
        errors.append(name + ": missing current unified navigation (website-unified.js + ux-site-nav)")
    if "site-nav.js" in html:
        errors.append(name + ": conflicting integration-branch navigation")
    if "<html" not in html.lower() or "</html>" not in html.lower():
        errors.append(name + ": incomplete HTML structure")
    if slug in ("ki-systeme", "ki-kernforschung", "soulution-ki-kreativrechte") and re.search(r'href=["\']\./promptbibliothek\.html', html):
        errors.append(name + ": points to unapproved prompt library")
    for attr, raw in parser.urls:
        all_links += 1
        u = urlsplit(raw)
        if u.scheme or u.netloc or raw.startswith(("mailto:", "tel:", "data:", "#", "javascript:")):
            if raw.startswith("#") and unquote(u.fragment) not in parser.ids:
                warnings.append(name + ": anchor may be generated dynamically: " + raw)
            continue
        if not u.path:
            continue
        target = (page.parent / unquote(u.path)).resolve()
        try:
            target.relative_to(DOCS)
        except ValueError:
            errors.append(name + ": link outside docs: " + raw)
            continue
        if not target.exists():
            errors.append(name + ": missing local link/asset " + raw)
        elif u.fragment and target.suffix == ".html" and target.name in scans:
            if unquote(u.fragment) not in scans[target.name].ids:
                warnings.append(name + ": target anchor may be dynamic: " + raw)

for name in ("codebuch-web-index.json", "inkubator-quellenregister.json",
             "projektmanagement-public-v2.json", "workflow-stand-v1.json",
             "thesen-uebersicht-v1.json", "mitmach-public-v2.json", "mitmachen-ergebnis-schema-v1.json"):
    file = DOCS / "data" / name
    if not file.is_file():
        errors.append("missing public JSON " + name)
    else:
        json.loads(file.read_text(encoding="utf-8"))

p = ROOT / "forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json"
data = json.loads(p.read_text(encoding="utf-8"))
ids = [x["id"] for x in data["requirements"]]
if data.get("verified_exact_100_message_sequence") is not False:
    errors.append("incorrect claim of literal last-100-message provenance")
if len(ids) != 72 or len(set(ids)) != len(ids):
    errors.append("72 requirement IDs missing or duplicated")
for item in data["requirements"]:
    if not (ROOT / item["evidence"]).is_file():
        errors.append(item["id"] + ": linked Git evidence file missing")
    if item.get("original_text_verified"):
        errors.append(item["id"] + ": original user wording improperly declared proven")

public = DOCS / "data/anforderungsabdeckung-v1.json"
if public.is_file():
    summary = json.loads(public.read_text(encoding="utf-8"))
    if summary.get("schema_version") != "user-requirement-coverage-public/0.1":
        errors.append("unsupported public requirement summary")
    if summary.get("atomic_requirements") != len(ids):
        errors.append("public task count differs from source requirements")
    if sum(x["items"] for x in summary.get("groups", [])) != len(ids):
        errors.append("public task group count mismatch")
    if summary.get("exact_last_100_original_messages_verified") is not False:
        errors.append("unsupported claim that all 100 original user prompts were verified")
    if summary.get("source_file_refs_present") != len(ids):
        errors.append("public source file presence claim disagrees with full ledger")
else:
    errors.append("public requirement summary missing")

print("Audited site pages:", len(slugs), "HTML href/src references:", all_links,
      "traceable atomic tasks:", len(ids))
for warning in warnings[:30]:
    print("WARNING:", warning)
if len(warnings) > 30:
    print("... more warning cases:", len(warnings) - 30)
for err in errors:
    print("ERROR:", err)
if errors:
    sys.exit(1)
print("PASS: static site/page/asset/task path checks only; live deployment remains untested")
