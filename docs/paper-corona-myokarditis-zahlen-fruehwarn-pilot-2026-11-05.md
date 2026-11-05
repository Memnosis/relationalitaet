# Myokarditis-Zahlen: erster reproduzierbarer Vergleichs- und Frühwarnpilot
**COR-MYO-01 · 05.11.2026 · Zahlenquelle verifiziert, aber keine vollständige kausale Nutzen-Schaden-Bilanz**

## Forschungsfrage
Dürfen eine PEI-Spontanmelderate und die risikoadjustierten Zusatzfälle einer nordischen Kohortenstudie direkt als dieselbe Risikozahl präsentiert werden? **Nein**: Messobjekt, Altersgruppe, Design und teilweise Zeitfenster unterscheiden sich.

## Drei tatsächlich publizierte Größen
| ID | Quelle und Wissensstand | Bevölkerung / Präparat | Messobjekt | Zahl | Vergleich |
|---|---|---|---|---|---|
| MYO-NUM-01 | PEI-Bericht bis 30.09.2021 | Jungen 12–17, zweite Comirnaty-Dosis | Verdachtsmeldungen Myo-/Perikarditis pro zweite Impfdosis | 1 je 13.812 Dosen ≈ **7,24 pro 100.000** | **C** gegen klinische Register |
| MYO-NUM-02 | Nordic JAMA Cardiology 2022 | Männer 16–24, zweite BNT162b2-Dosis | adjustierte **zusätzliche** Myokarditisdiagnosen im 28-Tage-Fenster | **5,55 pro 100.000** (95%-KI 3,70–7,39) | **C** gegen Spontanmeldungen |
| MYO-NUM-03 | dieselbe nordische Kohorte | Männer 16–24, zweite mRNA-1273-Dosis | adjustierte **zusätzliche** Myokarditisdiagnosen im 28-Tage-Fenster | **18,39 pro 100.000** (95%-KI 9,05–27,72) | **B** innerhalb derselben Kohorte |

### Originalquellen
- [Paul-Ehrlich-Institut Sicherheitsbericht bis Ende September 2021](https://www.pei.de/SharedDocs/Downloads/EN/newsroom-en/dossiers/safety-reports/safety-report-27-december-2020-30-september-2021.pdf?__blob=publicationFile&v=9).
- [Nordische Bevölkerungs-Kohorte mit 23,1 Millionen Menschen](https://jamanetwork.com/journals/jamacardiology/fullarticle/2791253).
- [STIKO Pressemitteilung vom 10.11.2021](https://www.rki.de/DE/Themen/Infektionskrankheiten/Impfen/Staendige-Impfkommission/Empfehlungen-der-STIKO/PM/PM_2021-11-10.html): bei unter 30-Jährigen vorzugsweise Comirnaty.
- [RKI Epidemiologisches Bulletin 46/2021](https://www.rki.de/DE/Aktuelles/Publikationen/Epidemiologisches-Bulletin/2021/46_21.pdf?__blob=publicationFile&v=1): israelische Hinweise Februar bis April 2021, US-Meldedaten Juni 2021.

## Was ist damit tatsächlich belegt?
1. Ein Risiko-/Sicherheitssignal war spätestens 2021 erkannt und im späteren öffentlich datierten Risikomanagement berücksichtigt. Eine pauschale Behauptung, Myokarditis sei erst 2022 oder 2023 bekannt geworden, wäre falsch.
2. Das Risiko hängt nach den Studien ausgeprägt von Alter, Geschlecht, Dosis und Impfpräparat ab. Die Gesamtmelderate ist für männliche Jugendliche kein angemessener alleiniger Prüfmaßstab.
3. **Nicht belegt:** Die numerischen PEI- und Nordic-Raten seien direkt vergleichbar, oder das Risiko einer Impfung überwiege für alle Kinder/Jugendlichen ihren individuellen Nutzen.
4. Die Entscheidung, *wann* Behörden zusätzliche Warnhinweise, Empfehlungen oder Nachuntersuchungen hätten einsetzen müssen, braucht die zu jedem Stichtag verfügbare Evidenz, Dokumente und rechtlichen Zuständigkeiten.

## Fehler- und Sensitivitätsanalyse
- PEI: Spontanmelderate ist nicht automatisch bestätigte Inzidenz; möglich sind Unter-/Übermeldung und Mehrfachberichte.
- Nordische Kohorte: Beobachtungsdaten haben andere Kodierung, Kontrollperioden und Residualkonfundierung; 28-Tage-Intervall ausdrücklich.
- Unterschiedliche Altersbereiche 12–17 und 16–24 sowie unterschiedlicher Endpunkt Myo-/Perikarditis vs. Myokarditis.
- Die innerhalb derselben Nordic-Studie verglichenen Produktgruppen sind wesentlich näher vergleichbar, bleiben wegen möglicher Auswahl- und Restkonfundierung bedingt.
- **GRADE**: Qualität eines vollständigen Evidenzkörpers pro Aussage noch nicht formal bestimmt; kein „hoch/moderat/niedrig“ erfunden.

## Zeitachse Frühwarnqualität
Frühe israelische Signale **Februar–April 2021** → öffentlich dokumentierte US-Pharmakovigilanz **Juni 2021** → PEI-Bericht mit Stichtag **September 2021** → STIKO-Kommunikation **10.11.2021** → bestätigende größere Registeranalysen **2022**. **Das ist keine vollständig berechnete Entscheidungsverzögerung**, weil Erhebungs-, Verfügbarkeits-, Freigabe- und Publikationszeitpunkte differieren.

## Technische Reproduktion
[JSON-Datensatz mit drei unterschiedlich definierten Outcomes](./data/bki-corona-myokarditis-zahlenvergleich-pilot-v0-1.json). Der Crosswalk sperrt eine automatische gemeinsame Metaanalyse und dokumentiert Messobjekte, Einheiten, Populationen, Zeitfenster und Unsicherheit. Die Umrechnung `100000/13812 ≈ 7,24` ist rein arithmetisch und ändert die Bedeutung der Verdachtsmeldung nicht.

[Corona-Messkarten](./buerger-ki-corona-messkarten.html) · [Myokarditis-Quellen 11–20](./data/bki-myokarditis-quellenserie-011-020-v0-1.json).
