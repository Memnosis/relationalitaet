#!/usr/bin/env python3
"""Weisungsatlas – Quelltext nach Markdown und atomaren Prüf-KANDIDATEN.

Input ist eine zuvor rechtmäßig beschaffte lokale HTML/TXT/PDF-Datei.
Der Export bewahrt Herkunfts-Metadaten. Keine OCR und keine automatische
Behauptung, dass eine extrahierte Aussage rechtlich gültig sei.
PDF-Unterstützung erfordert PyMuPDF (fitz). Regeln werden nur als
Kandidaten markiert, bis eine Fachprüfung erfolgt.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

LIMIT = 25_000_000
VERSION = "0.1.0"

class TextHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fragments = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer"):
            self.skip += 1
        if not self.skip and tag in ("p", "h1", "h2", "h3", "h4", "li", "br", "tr"):
            self.fragments.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer"):
            self.skip = max(0, self.skip - 1)
        elif not self.skip and tag in ("p", "h1", "h2", "h3", "h4", "li", "tr"):
            self.fragments.append("\n")
    def handle_data(self, data):
        if not self.skip:
            self.fragments.append(data)

def normalize(text):
    text = text.replace("\r\n", "\n").replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()

def extract_file(path):
    raw = path.read_bytes()
    if len(raw) > LIMIT:
        raise ValueError("Eingabedatei größer als 25 MB")
    ext = path.suffix.lower()
    if ext in (".txt", ".md"):
        pages = [normalize(raw.decode("utf-8-sig"))]
    elif ext in (".htm", ".html"):
        parser = TextHTML()
        parser.feed(raw.decode("utf-8-sig"))
        pages = [normalize(html.unescape("".join(parser.fragments)))]
    elif ext == ".pdf":
        try:
            import fitz
        except ImportError as exc:
            raise ValueError("PyMuPDF für PDF-Extraktion installieren") from exc
        doc = fitz.open(stream=raw, filetype="pdf")
        pages = [normalize(page.get_text(sort=True)) for page in doc]
    else:
        raise ValueError("Format nicht unterstützt: " + ext)
    if not any(pages):
        raise ValueError("Kein Text extrahiert; manuelle Prüfung nötig, keine automatische OCR")
    return pages, hashlib.sha256(raw).hexdigest()

def candidates(pages, document_id):
    result = []
    # Verfahrens- und Pflichtausdrücke sind zunächst nur Hinweise.
    keywords = re.compile(r"\b(muss|müssen|soll|sollen|darf|dürfen|ist verpflichtet|sind verpflichtet|hat zu|haben zu|innerhalb von|sofern|wenn|es sei denn)\b", re.I)
    for page_no, text in enumerate(pages, 1):
        parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ§])", text)
        for part in parts:
            part = " ".join(part.split())
            if 30 <= len(part) <= 900 and keywords.search(part):
                candidate_id = f"{document_id}-C{len(result)+1:05d}"
                result.append({"candidate_id": candidate_id,
                               "locator": {"page": page_no, "text_prefix": part[:100]},
                               "text": part,
                               "text_sha256": hashlib.sha256(part.encode()).hexdigest(),
                               "modality_hint": keywords.search(part).group(0).lower(),
                               "actor": None, "action": None, "condition": None,
                               "exception": None, "legal_basis": None,
                               "valid_from": None, "valid_until": None,
                               "review_status": "unreviewed_candidate"})
    return result

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--id", required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--issuer", required=True)
    p.add_argument("--retrieved-at", required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    if not a.url.startswith("https://"):
        p.error("HTTPS-Quellen-URL erforderlich")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.retrieved_at):
        p.error("Abrufdatum muss YYYY-MM-DD sein")
    pages, digest = extract_file(a.input)
    atoms = candidates(pages, a.id)
    a.out.mkdir(parents=True, exist_ok=True)
    md = [
        "# "+a.id+" – automatisierte Quellentranskription",
        "",
        "> Nicht fachlich verifiziert. Keine Aussage über aktuelle Geltung, Veröffentlichungslizenz oder vollständige PDF-Texterkennung.",
        "",
        f"- Originalquelle: {a.url}",
        f"- Herausgeber: {a.issuer}",
        f"- Abrufdatum: {a.retrieved_at}",
        f"- Original-SHA256: `{digest}`",
        f"- Seiten/Abschnitte: {len(pages)}", "",
    ]
    for idx, text in enumerate(pages, 1):
        md.extend([f"## Seite/Abschnitt {idx}", "", text, ""])
    (a.out / (a.id+".md")).write_text("\n".join(md), encoding="utf-8")
    record = {"schema": "bki-weisungsatome/0.1", "document_id": a.id,
              "original_url": a.url, "issuer": a.issuer, "retrieved_at": a.retrieved_at,
              "original_sha256": digest, "parser_version": VERSION,
              "source_publication_permission": "not_assessed",
              "text_extraction_status": "unreviewed",
              "atoms": atoms}
    (a.out / (a.id+".atoms.json")).write_text(json.dumps(record, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"{a.id}: {len(pages)} Seiten/Abschnitte; {len(atoms)} ungeprüfte Atom-Kandidaten")
    return 0

if __name__ == "__main__":
    sys.exit(main())
