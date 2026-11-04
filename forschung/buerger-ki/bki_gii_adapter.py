#!/usr/bin/env python3
"""Bürger-KI: XML-Rechtsquellenadapter (Forschungsprototyp).

Importiert lokal gespeicherte Gesetzestexte im XML-Format, extrahiert
Paragraphen samt Provenienz und lehnt unklare Zuordnungen ausdrücklich ab.
Kein Online-Abruf, keine Rechtsauskunft, keine Ortszuständigkeitsbestimmung.
"""
from __future__ import annotations

import argparse
import io
import zipfile
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ADAPTER_VERSION = "0.2.0"
MAX_BYTES = 20_000_000
ALLOWED_LAWS = {"bmg", "gewo"}


class ImportErrorWithContext(ValueError):
    pass


def _text(element):
    if element is None:
        return ""
    return " ".join(" ".join(element.itertext()).split())


def _find_text(root, tag):
    el = root.find(".//" + tag)
    return _text(el)


def _strip_external_dtd(raw):
    # Die GII-Dateien können auf eine externe DTD verweisen.
    # Externe DTD wird nicht geladen. Interne DTD/Entities werden
    # aus Sicherheits- und Reproduzierbarkeitsgründen abgelehnt.
    s = raw.decode("utf-8-sig")
    if re.search(r"<!DOCTYPE\s+[^>]*\[", s, re.I):
        raise ImportErrorWithContext("Interne DTD nicht unterstützt")
    s = re.sub(r"<!DOCTYPE\s+[^>]+>", "", s, count=1, flags=re.I)
    if "<!ENTITY" in s.upper():
        raise ImportErrorWithContext("Entity-Deklarationen abgelehnt")
    return s


def _unpack_gii(raw: bytes):
    """Amtliches GII-Angebot: XML liegt üblicherweise in xml.zip."""
    if not raw.startswith(b"PK\\x03\\x04"):
        return raw, None
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            entries = [z for z in archive.infolist()
                       if not z.is_dir() and z.filename.lower().endswith(".xml")]
            if len(entries) != 1:
                raise ImportErrorWithContext("ZIP muss genau eine XML-Datei enthalten")
            member = entries[0]
            if (member.file_size > MAX_BYTES or member.compress_size > MAX_BYTES
                    or ".." in member.filename or member.filename.startswith("/")):
                raise ImportErrorWithContext("Unsicheres oder zu großes ZIP-Mitglied")
            with archive.open(member) as stream:
                xml_raw = stream.read(MAX_BYTES + 1)
            if len(xml_raw) > MAX_BYTES:
                raise ImportErrorWithContext("Entpackte XML-Datei zu groß")
            return xml_raw, member.filename
    except (zipfile.BadZipFile, RuntimeError, OSError) as exc:
        raise ImportErrorWithContext("ZIP nicht lesbar: " + str(exc)) from exc


def extract(raw: bytes, law: str, source_url: str, retrieved_at: str):
    law = law.lower().strip()
    if law not in ALLOWED_LAWS:
        raise ImportErrorWithContext("Gesetz nicht auf Positivliste: " + law)
    if not source_url.startswith("https://www.gesetze-im-internet.de/"):
        raise ImportErrorWithContext("Nur überprüfbare GII-Original-URLs als Quelle")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", retrieved_at):
        raise ImportErrorWithContext("Abrufdatum YYYY-MM-DD erforderlich")
    if len(raw) > MAX_BYTES:
        raise ImportErrorWithContext("Quelldatei zu groß")
    xml_raw, archive_member = _unpack_gii(raw)
    try:
        root = ET.fromstring(_strip_external_dtd(xml_raw))
    except (ET.ParseError, UnicodeDecodeError) as exc:
        raise ImportErrorWithContext("XML nicht lesbar: " + str(exc)) from exc

    norm_list = [root] if root.tag == "norm" else root.findall(".//norm")
    if not norm_list:
        raise ImportErrorWithContext("Keine norm-Elemente gefunden")
    provisions = []
    for norm in norm_list:
        name = _find_text(norm, "enbez")
        if not re.fullmatch(r"§\s*\d+[a-zA-Z]?", name):
            continue
        metadata = norm.find("metadaten")
        token = _text(metadata.find("jurabk")) if metadata is not None else ""
        if token and token.lower() != law:
            continue
        body = norm.find("textdaten")
        content = _text(body)
        if not content:
            continue
        provisions.append({"provision_id": law.upper() + "-" + re.sub(r"\s+", "", name),
                           "heading": _find_text(norm, "titel"),
                           "citation": law.upper() + " " + name,
                           "text": content,
                           "text_hash_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest()})
    if not provisions:
        raise ImportErrorWithContext("Keine verwertbaren Paragraphen gefunden")
    ids = [p["provision_id"] for p in provisions]
    if len(set(ids)) != len(ids):
        raise ImportErrorWithContext("Doppelte Paragraphen-IDs")
    return {"schema": "bki-gii-xml-import/0.1", "adapter_version": ADAPTER_VERSION,
            "law": law.upper(), "source_url": source_url, "retrieved_at": retrieved_at,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "xml_sha256": hashlib.sha256(xml_raw).hexdigest(),
            "archive_member": archive_member,
            "official_promulgation": False, "legal_validity_checked": False,
            "local_authority_checked": False, "provisions": provisions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml", type=Path)
    parser.add_argument("--law", required=True, choices=sorted(ALLOWED_LAWS))
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--retrieved-at", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = extract(args.xml.read_bytes(), args.law, args.source_url, args.retrieved_at)
    except (OSError, ImportErrorWithContext) as exc:
        print("Import nicht abgenommen: " + str(exc), file=sys.stderr)
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Extrahiert:", len(result["provisions"]), "Paragraphen;", result["law"],
          "; SHA-256", result["source_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
