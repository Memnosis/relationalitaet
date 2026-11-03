# Promptbibliothek v1 · Prüfung und Auswirkung auf GitHub-Publikation

Stand 2026-11-03. Ergebnis im Integrationsbranch, noch nicht auf GitHub Pages main veröffentlicht.

## Bestand und Prüftiefe
47 Promptobjekte mit Kennung, Eingabe, Ausgabe, Quelle und Status: 5 Leser, 15 Vorpublikation, 13 Mitmachen, 7 Geo/Format und 7 Meta. 47/47 Registerverträge bestehen strukturelle Anforderungen, jedoch **kein** eigenständiger KI-Antwortbenchmark. Die erste Quellenprüfung an zwei Nutzer-Originalbüchern ergab 12/12 nachvollziehbare Fundstellen. Sie belegt die Herkunft der Fragestellungen, nicht die Qualität von Modellantworten. Sieben Mitmach- und Geo-Meilenstein-Objekte besitzen Teiltestnachweise, keine vollständigen Aufgabenabschlüsse. In 20 historischen Aufträgen stehen weiterhin Prompt-first-Anweisungen; sie werden ohne Informationsverlust archiviert, aber nicht als aktiver Arbeitsstandard behandelt.

## Originalwerke
Die kompletten Originale *Öffentliches Potenzial* (171 PDF-Seiten) und *Mediale Potenziale* (33 PDF-Seiten) liegen im Gespräch als hochgeladene Bücher und Originalcover vor. Die Werksanzeige für Mafia-Spiele ist in Mediale Potenziale auf PDF-Seite 23 nachweisbar. Originalcover nicht erfinden. Die binären PDFs/Bilder sind in diesem Branch noch nicht als Seitenassets hochgeladen. Historische SOULution-Neunfelderliste aus dem Mediale-Buch nicht ohne Versions-Crosswalk mit der gegenwärtigen Site gleichsetzen.

## Seitenarchitektur
- `docs/promptbibliothek.html` zeigt die fünf Familien mit Volltext, Kopieren, Such- und Statusfilter und konsistenten gerahmten Meta-Elementen. Register: `docs/data/promptbibliothek-v1.json`.
- Der Einstieg wird von `docs/bibliothek.html`, `docs/mitmachen.html`, `docs/wissen-macht-wirklichkeit.html`, `docs/soulution.html`, `docs/ki-systeme.html`, `docs/projektstand.html` verlinkt.
- Die Publikation sollte vier bestehende Werke wiederkehrend mit echten Originalcover-Miniaturen, Fachbezug und Links zeigen, nicht vier isolierte Werk-Kapitel bauen.
- Die Bürgerfrage bleibt die Rechenschaft über Entscheidungen, Mittel, Wirkungen, Dokumentation und Konsequenz. Der persönliche Prompt-Prompt ist eine optionale Methode.
- Die Mini-KI, Geo-KI und KI-Tensor sind verschiedene Forschungsansätze; eine Promptbeschreibung ist kein ausführbarer Skill. Tensor-Nutzen wird über zusätzliche **gesicherte Ableitungen** verglichen, nicht über bloße Knotenanzahl.
- Glossar-/Harvesting-/Datenobjekte bleiben in ihrem Fachregister. Ein Prompt verlinkt sie, statt sie zu duplizieren.

## Ergebnisse und nächste echte Tests
1. H1–H5 unverändert und optimiert an denselben Originaldokumenten ausführen, die vollständigen Modellantworten und Quellenstände speichern und unabhängig prüfen.
2. Struktur-, Synthese-, Meta-, Skill- und Agentenprompts an reproduzierbaren Fallkarten mit Negativtests vergleichen.
3. SVIK-Rechenschaft mit eigenen amtlichen Primärdaten, Fristen- und Datenstatus durchführen; die derzeitigen Bücher enthalten keine auszahlungsgenauen SVIK-Zahlen.
4. Die 20 Altaufträge mit Prompt-first-Schritt als historische meta_prompt archivieren, aktuelles Feld next_executable_test priorisieren.
5. Die vier Originalcover als echte Repository-Assets übernehmen und mit den Book-IDs verbinden.
6. Browser-/Mobil-/Screenreader-Smoke und Pages-Publikation nach Review/Merge prüfen.

**No-loss-Regel:** Quellenfall ≠ KI-Lauf ≠ unabhängig bestätigter Fachbefund; fachliche Dreiteilung ≠ validierte Trinität ≠ vollständiger Tensor.
