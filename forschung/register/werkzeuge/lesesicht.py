#!/usr/bin/env python3
"""Öffentliche Lesesicht (web-lesesicht/0.2) aus Claims, Seitenzuordnung und Referenzset erzeugen. Owner: Claude.

Aufnahmeregeln (alle müssen gelten), abgestimmt mit GPT (GPT_DISKUSSION_02_ZENODO §3–§5):
  1. public_release == true (Freigabe durch Nils)   2. vertraulichkeit == "oeffentlich"
  3. source_id im öffentlichen Referenzset           4. Seitenzuordnung mit Rolle traegt_abschnitt/historischer_kontext
Ausgabe nur außerhalb von docs/ (GPT übernimmt nach Prüfsummen-Review).
Aufruf: python3 forschung/register/werkzeuge/lesesicht.py --aus forschung/register/oeffentlich/LESESICHT_V0_2.json [CLAIMDATEI ...]
"""
import argparse, datetime as dt, json, pathlib, subprocess, sys

W = pathlib.Path(__file__).resolve().parents[3]
STANDARD = ["forschung/tensor/logik-claude/LOGIK_CLAIMREGISTER_V0_1.json", "forschung/register/beispiele/CLAIMS_BEISPIELE_V0_1.json"]


def lade(p):
    return json.loads((W / p if not pathlib.Path(p).is_absolute() else pathlib.Path(p)).read_text(encoding="utf-8"))


def erzeuge(claim_dateien, zuordnung, referenzset, commit):
    ref = {w["source_id"]: w for w in referenzset["werke"]}
    eintraege = []
    for datei in claim_dateien:
        for c in lade(datei)["claims"]:
            if c.get("public_release") is not True or c.get("vertraulichkeit") != "oeffentlich" or c.get("source_id") not in ref:
                continue
            w = ref[c["source_id"]]
            v = next((x for x in w["versionen"] if x["doi"] == c.get("werk_version", {}).get("doi")), w["versionen"][0])
            fs = c.get("fundstelle", {})
            pin = ", ".join(x for x in [f"S. {fs['seite']}" if fs.get("seite") else "", f"Z. {fs['zeile']}" if fs.get("zeile") else "", fs.get("abschnitt", "")] if x)
            for r in zuordnung["regeln"]:
                if c["claim_id"].startswith(r["claim_praefix"]):
                    eintraege.append({"claim_id": c["claim_id"], "page_id": r["page_id"], "section_id": r["section_id"],
                                      "short_claim": c["aussage"][:300], "source_id": c["source_id"], "title": w["titel"],
                                      "version_doi": v["doi"], "pinpoint": pin, "source_access": c["quellenstatus"]["status"],
                                      "evidence_level": c["evidenz"]["stufe"], "review_state": c.get("review_state", "owner_checked"),
                                      "public_release": True, "license": v.get("lizenz") or "", "source_commit": commit, "rolle": r["rolle"]})
    eintraege.sort(key=lambda e: (e["page_id"], e["section_id"], e["claim_id"]))
    return {"schema_version": "web-lesesicht/0.2", "source_commit": commit,
            "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(), "public_release": True,
            "seiten": sorted({e["page_id"] for e in eintraege}), "eintraege": eintraege}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--aus", required=True); ap.add_argument("claims", nargs="*")
    a = ap.parse_args()
    ziel = pathlib.Path(a.aus).resolve()
    if (W / "docs") in ziel.parents:
        sys.exit("Abbruch: nicht direkt nach docs/ schreiben; GPT übernimmt nach Review.")
    commit = subprocess.run(["git", "-C", str(W), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    out = erzeuge(a.claims or STANDARD, lade("forschung/register/oeffentlich/SEITENZUORDNUNG_V0_1.json"),
                  lade("forschung/register/QUELLEN_REFERENZSET_V0_1.json"), commit)
    ziel.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"eintraege": len(out["eintraege"]), "seiten": out["seiten"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
