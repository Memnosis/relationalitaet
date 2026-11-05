# Bürger-KI · Corporate Design, Mitmach-Anwendungen, Forschungsdaten und Publikationen
**Release-Zusammenfassung · 05.11.2026 · Versionsstand Forschungsedition**

## Öffentliche Module
- [Bürger-KI](./buerger-ki.html): Identität, Leitfrage und Lernnavigation; neuer Branding-Hinweis.
- [Designlegende](./buerger-ki-legende.html): Farben, Icons, redaktionelle Stufen, Spezialperspektiven.
- [Skills & Werkzeuge](./buerger-ki-skillzentrum.html): eigenständiger, sichtbarer Navigationsbereich; nachweisbare Funktionen getrennt von Ideen.
- [Kaffeekränzchen](./buerger-ki-kaffeekraenzchen.html): freiwilliges soziales und didaktisches Methodenprogramm.
- [Kaffeekränzchen-Frage / Antwort](./buerger-ki-kaffeekraenzchen-fragen.html): eigenständiges Formular; JSON-Entwurf lokal speichern oder GitHub-Issue für bewusste öffentliche Einreichung öffnen.
- [Publikationen](./publikationen.html): neue Papers, Test- und Methodenlinks.
- [Sitemap](./sitemap.html): 63 HTML-Hauptseiten mit Kurzbeschreibung; [XML-Sitemap](./sitemap.xml).
- [Mermaid 1](./paper-mermaid-seitengrammatik-teil-1-2026-11-05.md), [2](./paper-mermaid-seitengrammatik-teil-2-2026-11-05.md), [3](./paper-mermaid-seitengrammatik-teil-3-2026-11-05.md), [4](./paper-mermaid-seitengrammatik-teil-4-2026-11-05.md): für 62 Hauptseiten jeweils zwei diagrammfähige Strukturvorschläge (124); die danach neu angelegte Legenden-Seite ist noch nicht als eigenes Diagramm erfasst.

## Einzelpaper und Prüfungen
- [Interaktions- und Betreiber-Audit](./paper-interaktionsaudit-betreiberpflicht-und-seo-2026-11-05.md): Funktion, vorhandener Code, dokumentierte Reaktion, ungetestete Schritte.
- [Kaffeekränzchen-Gesamtausarbeitung](./paper-kaffeekraenzchen-gesamtserie-claims-2026-11-05.md): zwei vorhandene Konzept-Paper, sieben Bild-/Claim-Motive, Gegenproben.
- [Offener Standard Arbeitsvermittlung](./paper-offener-standard-arbeitsvermittlung-2026-11-05.md): ESCO, KldB, ISCO, O*NET, HR Open Standards, JobPosting, API-Grenzen und Rechte.
- [Politik-100-Finalisierung](./paper-entscheidungsmonitor-100-finalisierungsgates-2026-11-05.md): fünf Qualitätstore; weiterhin keine behaupteten 100 vollständigen Wirkungsstudien.
- [Ko-fi-Publikationsfamilie](./paper-publikationsfamilie-kofi-potenziale-2026-11-05.md): Originalwerke, Links und Cover-/Promo-Provenienz.
- [Benchmark v0.3](./data/bki-benchmark-normalisiert-v0-3.json): zehn Datensätze mit korrigierten Feldnamen; Unbekanntes null. [JSON-Schema](./data/bki-benchmark-v0-3.schema.json) und [GitHub-Actions-Validierung](https://github.com/Memnosis/relationalitaet/blob/main/.github/workflows/bki-benchmark-contract.yml).
- [Corporate Design](./paper-buerger-ki-corporate-design-legende-2026-11-05.md), [Logozeichen](./assets/media/buerger-ki-zeichen.svg) und [CSS-Grundstil](./assets/buerger-ki-ci.css).
- [Potenziale](./paper-potenziale-arbeitslosigkeit-unbezahlte-arbeit-innovation-2026-11-05.md) und [Corona-Forschungsstatus](./paper-corona-gesamtaudit-evidenzluecken-trinitaere-pruefung-2026-11-05.md) sind ausdrücklich getrennte Fachbereiche.

## Tests und Grenzen
- Interne Lesbarkeit der Repository-Dateien und Referenzen nach Schreibvorgang; kein vollständiger Live-Website-Check.
- Neue Browser-Smoketests für das Kaffeekränzchen sind in `scripts/verify_website_browser.mjs` integriert: Seite, Export, Übergabe-URL, Negativfall. Ein erfolgreicher GitHub-Actions-Lauf ist noch nicht bestätigt.
- Der Benchmark-Registertest bestätigt zehn eindeutige IDs, vorhandene Pflichtschlüssel und **null** zum numerischen Vergleich freigegebene Datensätze. Inhaltliche Harmonisierung offen.
- Neue Forschungs-MD-Dateien haben einheitlich Logo, Beschreibung, Keywords, Datum, Kontakt und Rücknavigation bekommen; ursprüngliche No-Loss-Artefakte bleiben unverändert.
- Ein neuer Bürger-KI-DOCX-/PDF-Publikationsentwurf wurde separat mit Logo und Kontakt erstellt. Die Volltexte der Original-Ko-fi-Werke wurden nicht vollständig kollationiert.
- Es gibt keine bestätigte automatisierte Moderation oder öffentliche Nutzerstatistik. Reale GitHub-Issue-Abgabe ist eine bewusste, separate Nutzeraktion.

## Nächste Schritte
1. CI-Ergebnisse und Browser-Interaktionen real prüfen; Fehlermeldungen und Barrierefreiheit testen.
2. Benchmark-Semantik, Population, Messmethoden, Unsicherheit und Quellenzeitpunkte nachtragen; Freigabesperren nicht umgehen.
3. Alle Hauptseiten auf Navigation, JSON/Links, Layout und saubere SEO-Metadaten prüfen.
4. Operator-Antwortprozess, Zuständigkeit und Freigaberahmen für Vorschläge definieren; keine stillschweigenden Reaktionsversprechen.
5. Originalcover und Quellenstände der externen Publikationen gezielt gegen die Originale prüfen.
6. Politik-100-Kohorte anhand Primärakten, Verfahrensständen und Evaluierbarkeit qualifizieren.
