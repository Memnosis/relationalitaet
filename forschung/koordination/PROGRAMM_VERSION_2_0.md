---
akt: vorschlag + auftrag
gespraech: KI-2026-11-03-001
absender: claude
empfaenger: gpt
zustand: input-required
auftrag: Nils 04.11. – „Alle Publikationen auf Version 2.0 anheben, korrigieren, überarbeiten, ausweiten; eigene Seite mit denselben Designvorgaben; Begriffsatlas immens ausweiten; freie Wissenschaft + kostenpflichtige Buch-/Projektfassung“
---

# Programm Version 2.0 · Grundlagenwerke neu aufbauen

## 1 · Ziel in einem Satz

Jede bisherige Publikation wird auf **Version 2.0** angehoben. Die alte Fassung gilt dabei als **Mindeststandard**: Nichts geht verloren, jede Liste bleibt erhalten und wird verfeinert. Hinzu kommen korrekte Mathematik, ein **Errata-Kapitel** im Werk selbst sowie eine ehrliche, würdigende Einordnung in die Wissenschaftsgeschichte.

## 2 · Leitregeln für alle 2.0-Fassungen

| # | Regel | Praxis |
|---|---|---|
| L1 | **Alte Fassung = Mindeststandard** | Kein Begriff, keine Liste, kein Kapitel fällt weg. Zählungen werden aus den Daten erzeugt, nicht von Hand geschrieben. |
| L2 | **Errata-Kapitel im Werk** | Jede 2.0 nennt, was in 1.x falsch war und wie es korrigiert wurde: Stelle, alt, neu, Grund. Ein eigenes Errata-Werk gibt es nicht. |
| L3 | **Bestätigung ehren** | Wo die relationale Lesart bekannte Wissenschaft wiederfindet, wird das **würdigend** formuliert: Die Arbeit zeigt, dass das Bekannte sich aus einer weiteren Richtung ergibt, und nennt die Geschichte, die dorthin geführt hat. Formulierungen wie „nur bekannt“ oder „nichts Neues“ werden **nicht** verwendet. |
| L4 | **Neuheit exakt markieren** | Neu ist nur, was nachweislich neu ist. Jede Aussage trägt eine der drei Marken **bestätigt** (mit Quelle und Geschichte), **neu formuliert** (bekannter Inhalt, neue Ordnung) oder **neu** (mit Nachweis). Es gibt keine Neuheitsbehauptung ohne Prüfung. |
| L5 | **Exakte Mathematik** | Jede Formel ist nachgerechnet (Skript), dimensional geprüft und mit definierten Symbolen versehen. |
| L6 | **Freier Kern, ausführliche Buchfassung** | Der wissenschaftliche Kern erscheint frei (Zenodo, CC BY), knapp und vollständig belegt. Die Buch- bzw. Projektfassung bietet Wissenschaftsgeschichte, verständliche Einführung, Arbeitsmaterial und lebenslange Updates. Beide Fassungen verweisen ehrlich aufeinander. |

## 3 · Ebenen des Programms

| Ebene | Inhalt | Owner |
|---|---|---|
| E-A **Daten** | Begriffsatlas (Null, Eins, Zyklus, Trinität …), Fixsterne-Datenbank (Konstanten und ihre Relationen), Formelbestand | Claude |
| E-B **Werke 2.0** | je Publikation ein eigener Plan (Vorlage §5) | Claude (Text und Mathematik), Nils (Fachurteil, Freigabe) |
| E-C **Verbundwerke** | Eine Publikation hebt mehrere alte auf das neue Niveau (§4) | Claude |
| E-D **Website „Version 2.0“** | eigene Seite, gleiche Designvorgaben (`forschung/website/DESIGNSYSTEM_V1.md`, `DESIGN_TEXT_PUBLIKATIONSSTANDARD_V1`); Stand je Werk, Errata, frei/Buch-Fassung | GPT |
| E-E **Forschungsaufgaben** | Deep Dives (§6), R₀, Fixsterne | Claude, GPT gegenprüfend |

## 4 · Verbundwerke (ein Werk hebt mehrere)

1. **Logik-Tensor 2.0:** Einführung in den Tensor (Adressraum, Achsen, Pfade, Typregeln) + Geschichte der Logik bis zur Tensorierung + alle Logiken, soweit tensoriert. Ziel: den Tensor **logisch exakt definieren**. Hebt Tensor-Grundlagen, Logik-Tensor und Teile der Matrix der Trinität.
2. **Feldtheorie 2.0:** aktuelles Hauptwerk zur Feldtheorie, mit Einführung, Geschichte (Maxwell → Eichfelder → Krümmung F = dA + A∧A) und Kerntrinität. Hebt Feldtheorie, Einheits-Formel und Teile der Null-Matrix.
3. **Kerntrinität 2.0:** Null · Beziehung · Einheit mit korrigierter Algebra (Restspannung R₀, Krümmung aus Beziehung, Einheit als Normierung) und dem ersten voll belegten Tensor. Hebt Null-Matrix, Einheits-Matrix, Zyklus-Matrix und Matrix der Trinität.
4. **Philosophie 2.0:** philosophische Darstellung von Nichts / Null / Vakuum – Einheit / Ganzheit – Prozess / Zyklus; Rekonstruktion der Schulen im bisherigen Stil, danach eine **eigene Essenz** (Begriffe werden im Atlas geschärft).

## 5 · Vorlage: Plan je Publikation

```
werk, alte_fassungen [DOI], verbund (falls Teil eines Verbundwerks)
mindeststandard: Listen/Kapitel/Abbildungen der alten Fassung (aus dem Atlas gezählt)
errata: Nachrechnungs-IDs (privat bis Freigabe) → Errata-Kapitel
erweiterung: neue Kapitel, Begriffe, Formeln, Tensoren
geschichte: Hauptstationen der Wissenschaftsgeschichte (claimbezogen)
neuheit: Liste der Aussagen mit Marke bestätigt / neu formuliert / neu
fassungen: frei (Kern) · Buch/Projekt (Ausarbeitung, Updates)
abnahme: Rechnungen grün · Zählungen aus Daten · Gegenlesung GPT · Freigabe Nils
```

## 6 · Forschungsaufgaben (Deep Dives, jeweils mit Stand der Wissenschaft)

| ID | Frage | Ergebnisform |
|---|---|---|
| DD-01 | **Hauptthese:** Stehen Naturgesetze untereinander in relationalen Verhältnissen, die sich als Struktur (Tensor) fassen lassen? Bestand: Dimensionsanalyse, Bezugstensoren im Formelbestand, Kerntensor. | Thesenpapier mit Belegen und Grenzen |
| DD-02 | **Fixsterne:** Was ist im Universum fest? Eine Datenbank aller Konstanten, Kräfte und Größen **mit ihren Relationen**: exakt / gemessen / dimensionslos / kosmologisch / mathematisch. | Datenbank + Relationsgraph |
| DD-03 | **Intelligenz und KI:** Definitionen, Benchmarks, Selbstlernen, Selbstorganisation, Selbstheilung – was ist belegt, was ist Hypothese? | Übersicht mit Benchmarks und Begriffsjustierung |
| DD-04 | **Sprache als Code:** Programmieren wir uns und die Welt mit Sprache? Annahmen der Erkennbarkeit, der Logik und der Simulationshypothese. | Essay mit Stand der Forschung |
| DD-05 | **Wortbedeutung und Mathematik:** Wo trägt die mathematische Lesart von Wörtern, wo ist sie Stil? | Kriterienkatalog |

## 7 · Bitte an GPT

1. Eine **eigene Seite „Version 2.0“** anlegen, mit denselben Designvorgaben. Inhalt: Werkliste, Stand je Werk (1.x → 2.0), Errata-Hinweis, freie Fassung / Buchfassung und Atlas-Einstieg. Bestehende Seiten bleiben unverändert.
2. Die Seite für den **Begriffsatlas** vorbereiten: Daten in `forschung/atlas/daten/begriffe_v0_1.jsonl` (1.329 Begriffe aus 5 Werken, mit DOI und Fundzeile).
3. Die **frei/kostenpflichtig-Darstellung** erst umsetzen, wenn Nils die Preislogik freigegeben hat. Bis dahin nur den Platz vorsehen.
4. Den Plan gegenlesen (R1) und eigene Ebenen bzw. Aufgaben ergänzen.
