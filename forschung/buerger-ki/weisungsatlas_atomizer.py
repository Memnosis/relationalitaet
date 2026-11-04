#!/usr/bin/env python3
"""Bürger-KI Weisungsatlas: Quellenstruktur -> eigene MD-Rekonstruktionsvorlage.

Projektregel: Originaltexte aus Behördenunterlagen werden NICHT als Markdown,
JSON, Textauszug oder Regelatom in den Forschungsbestand exportiert.
Eingabedateien werden nur temporär ausgelesen, Struktur und SHA registriert.
Fachliche Paraphrase und atomare Regelauslegung erfolgen anschließend gesondert
mit konkretem Norm-/Seitenbezug und Freigabe. Keine OCR, keine Rechtsauskunft.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

VERSION = "0.2.0"
MAX_BYTES = 25_000_000


class StructuralHTML(HTMLParser):
    """Erfasst nur Struktur- und Absatzgrenzen; Text wird nicht ausgegeben."""
    def __init__(self):
        super().__init__()
        self.paragraphs = 0
        self.headings = 0
        self.skip = 0
        self.in_paragraph = False
        self.has_paragraph_text = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer"):
            self.skip += 1
        if self.skip:
            return
        if tag in ("p", "li"):
            self.in_paragraph = True
            self.has_paragraph_text = False
        if re.fullmatch(r"h[1-6]", tag):
            self.headings += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer"):
            self.skip = max(0, self.skip - 1)
            return
        if tag in ("p", "li") and self.in_paragraph:
            if self.has_paragraph_text:
                self.paragraphs += 1
            self.in_paragraph = False

    def handle_data(self, data):
        if self.in_paragraph and not self.skip and data.strip():
            self.has_paragraph_text = True


def extract_structure(path: Path):
    raw = path.read_bytes()
    if len(raw) > MAX_BYTES:
        raise ValueError("Quelle > 25 MB")
    suffix = path.suffix.lower()
    if suffix in (".txt", ".md"):
        txt = raw.decode("utf-8-sig")
        parts = [p for p in re.split(r"\n\s*\n", txt) if p.strip()]
        pages = [{"page": 1, "paragraph_count": len(parts),
                  "text_present": bool(txt.strip())}]
    elif suffix in (".html", ".htm"):
        doc = StructuralHTML()
        doc.feed(raw.decode("utf-8-sig"))
        pages = [{"page": 1, "paragraph_count": doc.paragraphs,
                  "heading_count": doc.headings, "text_present": bool(raw.strip())}]
    elif suffix == ".pdf":
        try:
            import fitz
        except ImportError as exc:
            raise ValueError("PyMuPDF erforderlich für PDF") from exc
        pdf = fitz.open(stream=raw, filetype="pdf")
        pages = []
        for idx, page in enumerate(pdf, 1):
            txt = page.get_text(sort=True)
            parts = [p for p in re.split(r"\n\s*\n", txt) if p.strip()]
            pages.append({"page": idx, "paragraph_count": len(parts),
                          "text_present": bool(txt.strip())})
        pdf.close()
    else:
        raise ValueError("Nicht unterstütztes Format: " + suffix)
    if not pages or not any(p["text_present"] for p in pages):
        raise ValueError("Keine verwertbare Textstruktur; manuelle Prüfung nötig")
    return pages, hashlib.sha256(raw).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--id", required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--issuer", required=True)
    p.add_argument("--retrieved-at", required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    if not a.id or not re.fullmatch(r"[A-Za-z0-9._-]{3,100}", a.id):
        p.error("Quellen-ID muss stabil und sicher sein")
    if not a.url.startswith("https://"):
        p.error("HTTPS-Quellen-URL erforderlich")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.retrieved_at):
        p.error("Abrufdatum YYYY-MM-DD erforderlich")
    pages, digest = extract_structure(a.input)
    a.out.mkdir(parents=True, exist_ok=True)
    original_metadata = {
        "schema": "bki-weisungs-rekonstruktion/0.2",
        "source_id": a.id,
        "source_url": a.url,
        "issuer": a.issuer,
        "retrieved_at": a.retrieved_at,
        "source_sha256": digest,
        "format": a.input.suffix.lower().lstrip("."),
        "extractor_version": VERSION,
        "structure": pages,
        "original_text_exported": False,
        "atom_candidates": [],
        "review_status": "awaiting_manual_paraphrase"
    }
    (a.out / (a.id + ".source.json")).write_text(
        json.dumps(original_metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Eigene Rekonstruktion – " + a.id, "",
        "**Status:** Bearbeitungsvorlage; keine fachlich geprüften Regeln.", "",
        "- Herausgeber: " + a.issuer,
        "- Fundstelle: " + a.url,
        "- Abrufdatum: " + a.retrieved_at,
        "- SHA-256 der lokalen Ursprungsdatei: `" + digest + "`",
        "- Originaltext: **nicht übernommen**", "",
        "## Rechtsgebiet und Anwendungsbereich", "",
        "_In eigenen Worten ausarbeiten. Noch nicht geprüft._", "",
        "## Gesetzeübergreifende Beziehungen", "",
        "_Norm- und Paragraphenreferenzen zuordnen; keine automatische Gleichsetzung._", "",
        "## Eigene atomare Handlungsmodelle", "",
        "_Je Regel: Akteur, Handlung, Bedingung, Ausnahme, Zuständigkeit, Zeitraum,",
        "präzise Originalfundstelle, Quellen-ID, Geltungs- und Prüfstatus._", "",
        "## Gegenproben und offene Fragen", "",
        "_Positiv-, Grenz-, Negativfall und Rechtsgrundlagenprüfung nachtragen._", "",
        "## Fundstellen-Struktur (ohne Originaltexte)", ""
    ]
    lines.extend("- Seite/Abschnitt %s: Strukturpositionen %s" % (p["page"], p["paragraph_count"])
                 for p in pages)
    (a.out / (a.id + ".md")).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Rekonstruktionsvorlage angelegt:", a.id, "; Seiten:", len(pages),
          "; Regeln freigegeben: 0; Originaltexte exportiert: nein")
    return 0


if __name__ == "__main__":
    sys.exit(main())
