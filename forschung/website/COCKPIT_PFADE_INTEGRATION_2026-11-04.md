# Cockpit-Architektur: Fragen, Pfade, Forschung, Mitmachen
Stand: 2026-11-04 · Status: Entwurf, nicht freigegeben.

## Bestandsprüfung (Dateien aus main)
- `docs/index.html`: öffentliche Forschungsstartseite, Kernthema Mini-KI und wissenschaftliche Beziehungen, Projektkarten und Verbindungen.
- `docs/projektstand.html`: Projektmanagement, Bestandszahlen, Phasen, Meilensteine; organisatorische Ansicht.
- `dashboard/index.html`: weitere, ältere Start-/Dashboardstruktur mit sechs Kernbereichen, nicht als öffentliche Kanonseite ausweisen.
- `docs/erkenntnispfade.html` (Forschungsbranch): Frage-first-Prototyp mit sechs Fragen und neun Etappen zum Intelligenzpfad; auf main nicht veröffentlicht.
- `docs/publikationen.html`, `docs/mitmachen.html`, `docs/ki-kernforschung.html`: vorhandene Fach-/Beteiligungsbereiche.
Der Live-Deployment-Zustand konnte hier nicht über die externe Website verifiziert werden. Dateibefunde sind aus GitHub.

## Ziel: Ein Cockpit, drei Aufgaben
1. Einstieg: „Sind wir überhaupt intelligent?“ als Leitpfad; weitere offene, nicht suggestive Fragen.
2. Orientierung: Wo befinde ich mich zwischen Frage, Definition, Messung, Test, Ergebnis und weiterführendem Material?
3. Handeln: Lesen, wissenschaftlichen Gegenbefund prüfen, eigene KI verwenden, einen moderierten Thread eröffnen, Buch/Paper lesen.

## Nicht-destruktive Änderungen
- `docs/index.html`: Hero-Frage plus drei Einstiegskarten vor bisherigem Projekt-Hero; Bestandsinformation und Navigation vollständig erhalten.
- `docs/erkenntnispfade.html`: zentrale Pfadübersicht; aus statischem JSON-Overlay generieren, Quelle und Status pro Etappe; keine erfundene Nutzerfortschrittsanzeige.
- Alle Fachseiten: kleiner „Dein Pfad“-Bereich (vorherige/nächste Etappe, relevante Definition, Test und Originalquelle), nicht als globales Menüduplikat.
- `docs/projektstand.html`: reines internes/öffentlich kuratiertes Forschungs-/Portfolio-Cockpit; kein reißerischer Publikumseinstieg und keine voreiligen Erfolgsscores.
- `dashboard/index.html`: vor Umbau klären, ob noch genutzt; keine parallele zweite Startseite.
- `docs/mitmachen.html`: drei Wege Leser/IT/eigene KI; gemeinsamer Thread nur mit Authentifizierung, Moderation, Nutzerzustimmung, KI-Kennzeichnung und nachvollziehbarer Datenweitergabe.
- `docs/publikationen.html`: Pfadbezug zu bestehenden Büchern/Originalcovers, Paper und Shop-Angeboten; URLs und Freigabestatus vor Veröffentlichung prüfen.

## Cockpit-Layout
A. Stabile globale Navigation (Forschung, KI, Tensor, Projekte, Publikationen, Mitmachen, SOULution).
B. Fragespezifischer Hero + direkte Aktion „Pfad beginnen“.
C. Drei Nutzungsmodi: Entdecken, Forschen, Mitmachen.
D. Pfad-Leiste: Frage → Definition → Messung → Quellen → Test → Gegenprüfung → Paper → neue Frage.
E. Themen- und Forschungsübersicht mit Herkunft und Status statt vermischter Zahlen.
F. Zugehörige Papers, Skills, ausführbare Aufgaben, Originalbücher, Leser-/KI-Diskussion.
G. Status und Datengrundlage jeder Zahl sowie separater Projektstand.

## Pfaddatenvertrag
`path_id, path_version, audience, question, steps[{node_id,type,title,canonical_ref,origin,evidence_status,learning_goal,practice_prompt,tests}], relations, visibility, editorial_review`.
Keine Speicherung von Nutzerdaten ohne gesonderte Einwilligung; Pfadfortschritt nur wenn tatsächlich implementiert.

## Rollout und Tests
P0: bestehende Links und Originalstände inventarisieren, Metadaten-/Quellensynchronisierung.
P1: Desktop/Mobil-Wireframe und sechs Nutzungstests (Leser, Fachperson, Entwickler).
P1: drei Pfad-Piloten (Sind wir intelligent? Selbstlernen? Tensoren?); Linkprüfung und Zugänglichkeit.
P2: Cockpit als optionale neue Startansicht, bisherige Seiten erhalten.
P2: Diskussionstests mit Autor/Leser/markiertem KI-Beitrag.
P3: nach redaktioneller Freigabe Navigation, Bibliotheks-/Shopwege und Messdaten synchronisieren.

## Nicht behaupten
Kein Live-Chat implementiert, kein Benutzerfortschritt gespeichert, keine fachliche Gesamtvalidierung von Tensoren, keine vollständige 100%-Aufzeichnung aller Chattexte oder öffentliche Freigabe.
