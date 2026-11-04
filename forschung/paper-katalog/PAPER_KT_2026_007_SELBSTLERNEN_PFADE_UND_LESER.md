---
id: PAPER-KT-2026-007
title: Selbstlernen, Forschungs- und Leserpfade, KI-Mitwirkung
version: 0.1.0
date: 2026-11-04
status: research_draft_not_approved
source_policy: redacted_public_research_not_original_chat
---
# Selbstlernen, Forschungswege und Leserbeteiligung

## Forschungsbefund: Lernoperation statt universeller Intelligenzformel
Eine Lernoperation kann als Zustandsänderung modelliert werden: `S[t+1]=L(S[t],E[t],Z,F)`. Ein häufiges Beispiel ist `theta[t+1]=theta[t]-eta*grad(loss)`. Nicht jede Änderung ist Verbesserung, und Kontextanpassung beweist kein persistentes Lernen. Tests brauchen Vorher/Nachher-Leistung, Persistenz nach Neustart, unabhängigen Transfer, Negativfall, kontrollierte Bewertung.

## Pfad als eigenständiges Forschungsobjekt
Lernpfad, wissenschaftlicher Prüfpfad, Entwickler-Task, Leser-Mitmachpfad, Paper-Quellenpfad, Projektgeschichte und Buchpfad verbinden dieselben versionierten Knoten auf unterschiedliche Weise. Für jeden relevanten Begriff, jedes Paper, jeden Prompt, jeden Skill und jedes Produkt: verständlicher Einstieg, Lernziel, Vorkenntnis, Beispiel, Test/Mini-Aufgabe, Grenzen, Quellen und Verweis auf weiteren Weg. Der Pfad ersetzt nicht die vollständige Originalakte.

## No-Loss-Capture statt ID-Reduktion
Originaltext unverändert mit Herkunft, Zeit, Hash und Datenschutzklasse sichern; neues Paper als ableitende Version, Methoden/Fehler/Gegenbeispiele mitführen; strukturierte Extrakte erst zusätzlich. Rohchats dürfen nicht ohne private Speicherung, Rechteprüfung und Redaktion automatisch im öffentlichen Git erscheinen. Automatische Aufzeichnung zukünftiger Chat-Antworten ist im vorliegenden Repository **nicht** implementiert.

## Exemplarische Pfadklassen
- KI: Begriff -> historische Ansätze -> Lernoperation -> Prompt -> Skill -> Agent -> Mini-KI -> Mitmachen
- Tensor: Begriff -> 27er-Rollenstruktur -> Quellen-/Formelanker -> Rechenprobe -> Widerlegung -> Fachreview
- Prompt: Einzelfrage -> Kompetenzanalyse -> atomare Skills -> Komposition -> Verdichtungstest
- Buch: Themenfrage -> vorhandene originale Publikation/Cover -> Leseprobe -> Quellen -> Mitmachen -> freigegebenes Kauf-/Unterstützungsangebot
- Leser: Quellengestützte Fachfrage -> KI-Startprompt -> optional eigenes KI-Ergebnis -> moderierter Autor-/Community-Thread -> Review
- Historie: Originalstand -> Begründung/Änderung -> Gegenbefunde -> heutige Forschungsfrage
- Forschung: vollständige Analyse -> Methoden/Daten/Tests -> neues Paper -> unabhängige Prüfung -> Freigabe

## Wie Leser mit eigener KI und Autor sprechen
- Eigenen Chat starten: freigegebener Prompt/Quellenpaket; keine automatische gemeinsame Konversation.
- Öffentliche Diskussion: GitHub Discussions oder Discourse; Leser/Autor schreiben im selben Thread. Fremde KI-Ausgaben bleiben bezeichnete Leserbeiträge.
- Serverbasierter Mehrpersonen-/KI-Chat: möglich mit eigener Backend- und Accountinfrastruktur, etwa ChatKit, und Moderation/Consent; GitHub Pages allein genügt dafür nicht.
- Bring-your-own-agent: spätere A2A-basierte Integration, nur mit Identitäts-, Rollen-, Datenschutz- und Kostenkontrolle.
- ChatGPT-Gruppenchats seit 9.7.2026 nicht neu erstellbar; geteilte Einzelchats werden beim Fortsetzen private Kopien. Kein tragfähiger gemeinsamer Thread.

## Format und Freigabe
Je Pfad: `path_id,audience,goal,steps,prerequisites,source_refs,skill_refs,tests,release_gate`.
Je Paper: Volltext und Originalreferenz, RO-Crate/Provenienz/Versionen, Datentabellen und Skripte, Negativbefunde.
Je Diskussion: Thread-ID, Rollen, KI-Kennzeichnung, Consent/Moderation, Quellen, Review, Ergebnisstatus.
Alles zunächst Entwurf, keine öffentliche Ausschreibung, keine publizierte neue Buchausgabe.

## Quellen
- https://www.cs.cmu.edu/~tom/mlbook.html
- https://help.openai.com/de-de/articles/12703475-retiring-group-chats-in-chatgpt
- https://help-lb.openai.com/en/articles/7925741-chatgpt-shared-links-faq
- https://docs.github.com/en/discussions
- https://www.discourse.org/plugins/chat
- https://developers.openai.com/api/docs/guides/chatkit
- https://a2a-protocol.org/v1.0.0/

## Offene Tests
Originalantwort-Archiv nach Quelle/Hash inventarisieren; Pfad-Graph auf Zyklen, fehlende Voraussetzungen, unklare Freigaben prüfen; Lernoperation Vorher/Nachher/Transfer/Persistenz prüfen; mindestens zwei Mitmachpfade auf Verständlichkeit/Moderation testen; echte Buchlinks/Cover nach Freigabe prüfen; A2A-Interop und Sicherheitsmodell erst danach.
