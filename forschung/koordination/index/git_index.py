#!/usr/bin/env python3
"""Index des Git-Repositoriums: Bereiche, Umfang, Aktivität, Verantwortliche (KI-Trailer), Schlüsseldateien.
Aufruf: python3 forschung/koordination/index/git_index.py   → GIT_INDEX_V0_1.json und .md im selben Ordner"""
import collections, json, pathlib, subprocess, datetime
R = pathlib.Path(__file__).resolve().parents[3]; H = pathlib.Path(__file__).resolve().parent
git = lambda *a: subprocess.run(["git", "-C", str(R), *a], capture_output=True, text=True).stdout
BEREICH = {  # Feld/Zweck je Ordner (aus Inhalt und Ownerregel)
 "docs": "Website (GitHub Pages) – Owner GPT", "scripts": "Website-Skripte und Validatoren – Owner GPT", "dashboard": "Dashboard-Prototyp",
 "forschung/atlas": "Begriffsatlas Null · Eins · Zyklus · Trinität – Owner Claude", "forschung/register": "Register, Gegenrechnungen, Reproduktion – Owner Claude",
 "forschung/tensor": "Tensor: Algebra, Logik, Formeln, Datensätze – Owner Claude (+ GPT-Grafik)", "forschung/tensor-grafik": "Tensor-Grafik – Owner GPT",
 "forschung/koordination": "Zusammenarbeit der KIs: Regeln, Zyklen, Berichte, Skills – gemeinsam", "forschung/website": "Website-Planung und Designsystem – Owner GPT",
 "forschung/soulution": "SOULution: Inkubator, Register, Designvorgaben", "forschung/buerger-ki": "Bürger-KI: Rechte, Lernpfade, Weisungsatlas",
 "forschung/geoki": "Geo-KI: Geometrie-Modelle", "forschung/minimal-ki": "Minimal-KI: Beobachter-Modelle", "forschung/interop": "Interoperabilität und Formate",
 "forschung/g30": "g30: Feldkarten, Index-Algebra, Forschungswarteschlange", ".": "Wurzel: Originaldateien des Autors (Markdown, PDF, CSV)"}
def bereich(p):
    t = p.split("/")
    if len(t) == 1: return "."
    if t[0] == "forschung" and len(t) > 2: return "/".join(t[:2])
    return t[0]
dateien = [p for p in git("ls-files").splitlines() if p]
stat = collections.defaultdict(lambda: {"dateien": 0, "bytes": 0, "typen": collections.Counter()})
for p in dateien:
    b = bereich(p); f = R / p
    stat[b]["dateien"] += 1; stat[b]["bytes"] += f.stat().st_size if f.exists() else 0
    stat[b]["typen"][(pathlib.Path(p).suffix or "ohne").lower()] += 1
# Aktivität und Trailer je Bereich aus dem Log
log = git("log", "--name-only", "--format=@@%h|%ad|%(trailers:key=KI,valueonly,separator=%x2C)", "--date=short")
akt = collections.defaultdict(lambda: {"commits": set(), "zuletzt": "", "ki": collections.Counter()})
cur = None
for z in log.splitlines():
    if z.startswith("@@"):
        h, d, ki = (z[2:].split("|") + [""])[:3]; cur = (h, d, (ki.strip() or "ohne Trailer"))
    elif z.strip() and cur:
        a = akt[bereich(z.strip())]
        if cur[0] not in a["commits"]:
            a["commits"].add(cur[0]); a["ki"][cur[2]] += 1; a["zuletzt"] = max(a["zuletzt"], cur[1])
schluessel = collections.defaultdict(list)
for p in dateien:
    n = pathlib.Path(p).name.upper()
    if any(k in n for k in ("README", "KONZEPT", "PLAN", "PROGRAMM", "REGELN", "PAPER_", "DATENBLATT", "SKILLSAMMLUNG", "LANDKARTE", "INDEX")) and not n.endswith((".PNG", ".SVG")):
        schluessel[bereich(p)].append(p)
rows = []
for b in sorted(stat):
    s, a = stat[b], akt[b]
    rows.append({"bereich": b, "zweck": BEREICH.get(b, "–"), "dateien": s["dateien"], "groesse_kb": round(s["bytes"] / 1024),
                 "haeufigste_typen": ", ".join(f"{t} {n}" for t, n in s["typen"].most_common(4)), "commits": len(a["commits"]), "zuletzt": a["zuletzt"],
                 "commits_nach_ki": dict(a["ki"]), "schluesseldateien": sorted(schluessel[b])[:12]})
html = sorted(p for p in dateien if p.startswith("docs/") and p.endswith(".html"))
out = {"schema_version": "git-index/0.1", "erzeugt": datetime.date.today().isoformat(), "commit": git("rev-parse", "--short", "HEAD").strip(),
       "dateien_gesamt": len(dateien), "commits_gesamt": int(git("rev-list", "--count", "HEAD").strip()), "bereiche": rows, "website_seiten": html}
(H / "GIT_INDEX_V0_1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
L = [f"# Index des Repositoriums · Stand {out['erzeugt']} (Commit {out['commit']})", "",
     f"{out['dateien_gesamt']} Dateien, {out['commits_gesamt']} Commits. Erzeugt mit `python3 forschung/koordination/index/git_index.py`.", "",
     "| Bereich | Zweck | Dateien | KB | Commits | zuletzt | Commits nach KI-Trailer |", "|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| `{r['bereich']}` | {r['zweck']} | {r['dateien']} | {r['groesse_kb']} | {r['commits']} | {r['zuletzt']} | {', '.join(f'{k} {v}' for k, v in r['commits_nach_ki'].items())} |")
L += ["", "## Schlüsseldateien je Bereich", ""]
for r in rows:
    if r["schluesseldateien"]:
        L.append(f"**{r['bereich']}**: " + " · ".join(f"`{p}`" for p in r["schluesseldateien"]))
        L.append("")
L += [f"## Website-Seiten ({len(html)})", "", " · ".join(f"`{p[5:]}`" for p in html)]
(H / "GIT_INDEX_V0_1.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(out["dateien_gesamt"], out["commits_gesamt"]); [print(r["bereich"], r["dateien"], r["commits"], r["commits_nach_ki"]) for r in rows]
