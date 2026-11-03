#!/usr/bin/env python3
"""PM-Stufen der Claude-Aufgaben aus Nachweisen berechnen (R6, REV-003). Owner: Claude.

Eingaben: forschung/register/oeffentlich/EVIDENZREGELN_PM_V0_1.json (deklarierte Regeln),
Dateien im Repository (Existenz + SHA-256), TESTREGISTER_V0_1.json (Ergebnis 'bestanden'),
REPRODUKTIONSBERICHT (Signal 'ja'), Zyklus-STATUS.json (Flags), Lesesicht (Anzahl freigegebener Einträge).
Ausgabe: öffentliche Projektion pm-status/0.1 (nur IDs, Stufenwerte 0/0.5/1, Nachweis-Pfade und -Hashes).
Kein Stufenwert wird von Hand gesetzt; manuelle Angaben wie "checked" werden ignoriert.
Aufruf: python3 forschung/register/werkzeuge/pm_status.py --aus forschung/register/oeffentlich/PM_STATUS_CLAUDE_V0_1.json
"""
import argparse, datetime as dt, hashlib, json, pathlib, subprocess, sys

W = pathlib.Path(__file__).resolve().parents[3]


def sha(p):
    f = W / p
    return hashlib.sha256(f.read_bytes()).hexdigest()[:16] if f.is_file() else None


def berechne(regeln, testreg, repro_text, status, lesesicht_n):
    tests_ok = {t["test_id"] for t in testreg["tests"] if t.get("ergebnis", "").startswith("bestanden")}
    out = []
    for tid, st in regeln["aufgaben"].items():
        stufen, belege = {}, {}
        for stufe in regeln["stufen"]:
            r = st.get(stufe, {}); wert, b = 0.0, []
            if "dateien" in r:
                da = [(p, sha(p)) for p in r["dateien"]]
                b += [f"{p}#{h}" for p, h in da if h]
                if da and all(h for _, h in da):
                    wert = 0.5 if r.get("teil") or any(not sha(x) for x in r.get("teil_wenn_fehlt", [])) else 1.0
            if "tests" in r and r["tests"]:
                ok = [t for t in r["tests"] if t in tests_ok]; b += ok
                wert = 1.0 if len(ok) == len(r["tests"]) else (0.5 if ok else 0.0)
            if "reproduktion" in r:
                hit = any(r["reproduktion"] in z and "| ja |" in z for z in repro_text.splitlines())
                wert = 1.0 if hit else 0.0; b += ["forschung/register/REPRODUKTIONSBERICHT_CLAUDE_2026-11-03.md"] if hit else []
            if "r4_verglichen" in r:
                h = sha(r["r4_verglichen"]); wert = (0.5 if r.get("teil") else 1.0) if h else 0.0; b += [f"{r['r4_verglichen']}#{h}"] if h else []
            if "zyklus_flag" in r:
                if status["acknowledgements"].get(r["zyklus_flag"]): wert = 1.0; b.append(f"STATUS.json:{r['zyklus_flag']}")
                elif r.get("teil_flag") and status["acknowledgements"].get(r["teil_flag"]): wert = 0.5; b.append(f"STATUS.json:{r['teil_flag']}")
            if "oeffentliche_eintraege" in r:
                wert = 1.0 if lesesicht_n > 0 else 0.0
            if "nie_vor" in r:
                wert = 0.0
            stufen[stufe] = wert; belege[stufe] = b
        out.append({"task_id": tid, "owner": "claude", "stages": stufen, "evidence": belege})
    return out


STUFEN = ["inventory", "specification", "implementation", "testing", "peer_review", "release"]


def aggregat(tasks):
    """Claude-Anteil im Format von GPTs internal_summary (pm-public-curated/0.2): nur Summen, keine Einzelaufgaben (R6).
    stage_counts zählt Aufgaben mit vollem Nachweis (Wert 1); Teilnachweise (0.5) stehen getrennt und zählen dort nicht."""
    voll = {s: sum(1 for t in tasks if t["stages"][s] >= 1) for s in STUFEN}
    teil = {s: sum(1 for t in tasks if 0 < t["stages"][s] < 1) for s in STUFEN}
    return {"internal_summary": {"count": len(tasks), "completed_6_stages": sum(1 for t in tasks if all(t["stages"][s] >= 1 for s in STUFEN)),
                                 "stage_counts": voll,
                                 "review_status": "aus Nachweisen berechnet (Dateien, Testregister, Reproduktion, Zyklus-Flags); Teilnachweise nicht mitgezählt; Freigabe nur durch Nils"},
            "stage_counts_partial": teil}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--aus", required=True)
    ap.add_argument("--aggregat", help="zusätzlich: Claude-Summe im Format internal_summary (pm-public-curated/0.2) für GPT")
    a = ap.parse_args()
    if (W / "docs") in pathlib.Path(a.aus).resolve().parents:
        sys.exit("Abbruch: nicht direkt nach docs/ schreiben (GPT übernimmt nach Review).")
    lade = lambda p: json.loads((W / p).read_text(encoding="utf-8"))
    repro = (W / "forschung/register/REPRODUKTIONSBERICHT_CLAUDE_2026-11-03.md")
    res = berechne(lade("forschung/register/oeffentlich/EVIDENZREGELN_PM_V0_1.json"), lade("forschung/register/TESTREGISTER_V0_1.json"),
                   repro.read_text(encoding="utf-8") if repro.exists() else "", lade("forschung/koordination/zyklen/KI-2026-11-03-001/STATUS.json"),
                   len(lade("forschung/register/oeffentlich/LESESICHT_V0_2.json")["eintraege"]))
    commit = subprocess.run(["git", "-C", str(W), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    out = {"schema_version": "pm-status/0.1", "owner": "claude", "source_commit": commit,
           "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
           "regeln": "forschung/register/oeffentlich/EVIDENZREGELN_PM_V0_1.json", "skala": "0 kein Nachweis, 0.5 Teilnachweis, 1 Nachweis",
           "public_safe": True, "tasks": res}
    pathlib.Path(a.aus).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for t in res: print(t["task_id"], t["stages"])
    if a.aggregat:
        if (W / "docs") in pathlib.Path(a.aggregat).resolve().parents:
            sys.exit("Abbruch: nicht direkt nach docs/ schreiben (GPT übernimmt nach Review).")
        ag = {"schema_version": "pm-claude-aggregat/0.2", "ziel_schema": "pm-public-curated/0.2 → internal_summary", "owner": "claude",
              "source_commit": commit, "generated_at": out["generated_at"], "quelle": a.aus,
              "uebernahme": "GPT ersetzt docs/data/projektmanagement-public-v2.json → internal_summary 1:1 durch das Objekt internal_summary dieser Datei",
              **aggregat(res)}
        pathlib.Path(a.aggregat).write_text(json.dumps(ag, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("Aggregat:", ag["internal_summary"]["stage_counts"])


if __name__ == "__main__":
    main()
