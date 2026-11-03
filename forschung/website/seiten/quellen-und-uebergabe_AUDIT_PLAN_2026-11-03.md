# Seitenanalyse und Upgrade: Quellen und Übergabe

**Seite:** [`docs/quellen-und-uebergabe.html`](../../../docs/quellen-und-uebergabe.html) · **Priorität P0** · Auditdatum 2026-11-03 · **Prüfer:** GPT für Website, Claude für fachlich zugelieferte Daten; beiderseitige Endabnahme offen.

## Was wirklich vorhanden ist
Übergabeschritte, Quellenfamilien und Aufgabenanschluss für externe Mitarbeit. Ein eingebauter Abschnitt ist nicht mit einem bestandenen Browser-/Wissenschaftstest gleichzusetzen.

## Diagnose: Lücke und Wirkung
Öffentlich sichtbare Aufgaben-URLs und vertrauliche interne Quellarchitektur sind nicht sauber getrennt; Export-/Rückgabe-Endtest fehlt.

**Didaktische Sollstruktur:** E1 allgemeinverständliche Begriffs- und Nutzenklärung, E2 historische Ausdifferenzierung, Varianten und Gegenargumente, E3 Fachwissen/Quellen/Operatoren/Tests. Die Länge richtet sich nach dem Verständnisbedarf; separat Prompt-, Agenten- und Meta-Funktion. Serifenlos, bestehende Fachfarbe, klare gerahmte Blöcke und sachlich erklärende Icons.

## Reihenfolge / überprüfbarer Plan
1. Original-Git-Blob, Text/Anker/Medien/Quellen schützen und Nachher-Diff führen.
2. **Inhalt:** Claude liefert public-safe Claims, GPT erstellt extern nutzbaren Rückgabeweg; Git-Schreibberechtigung darf nicht Pflicht sein.
3. GPT-Eigenprüfung: die Seite mit verifizierten Task-IDs und Quellen-/Testschnittstellen verbinden, HTML/Links/JS/Desktop tatsächlich ausführen und Commit dokumentieren.
4. Claude-Eigenprüfung: relevante Claims und fachliche Daten gegen Originalquellen/Tests prüfen; reproduzierbare negative Befunde getrennt führen.
5. Cross-KI-Abnahme und ggf. Nils' Publikationsfreigabe; vor deren Nachweis kein Status „erledigt“.

**Taskfamilien:** PM-DATA-01, PM-PROMPT-01. **Historische Prompt-Herkunft:** einzelne der letzten 100+ Nutzerbefehle noch nicht lückenlos nummeriert – nicht mit diesem Themen-Audit verwechseln. [Abgleich und Planänderungen](../PLAN_UPDATE_PROMPT100_UND_LUECKENAUDIT_2026-11-03.md).

**Verweis:** [Gesamtseiten-Audit](../SEITENAUDIT_GESAMT_LERNWEGE_THESEN_GEOKI_2026-11-03.md) · [Git-Changelog](../CHANGELOG_PM_KI_HISTORY_GEO_THESES_2026-11-03.md). **Status:** teils dokumentiert/implementiert; Endfreigabe nicht nachgewiesen.
