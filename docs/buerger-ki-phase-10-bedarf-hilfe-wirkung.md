# Bürger-KI Phase 10 – Vom sichtbaren Bedarf zur überprüfbaren Hilfe

**ID:** BKI-PH10-001 · **Stand:** 2026-11-05 · **Status:** Forschungsdesign; keine ausgeführten Anbieter- oder Wirkungs-Audits.
**Kernreferenz:** [Bedarfslandkartenpaper](./paper-buerger-ki-bedarfslandkarte-rechtsstatus-und-blindstellen-v0-1.md)
**Register:** [Bedarfs- und Blindstellen-JSON](./data/bki-bedarf-versorgungsblindstellen-v0-1.json); [Hilfeportal-Crosswalk](./data/bki-hilfeportale-handlungsatlas-v0-1.json)

## Arbeitsziel
Die neue Phase verknüpft aggregierte Problemanzeigen aus Hilfetelefonen, Ombuds- und Widerspruchsstatistiken mit vorhandenen Hilfsangeboten, Zielklassen und Bürger-KI-Skills. Keine Verarbeitung individueller Beratungsfälle und keine automatische Gleichsetzung von Beratungen und betroffenen Personen.

## Fünf Prüfmodule
**P10-A – Bedarfsontologie:** Themenklassifikationen von Nummer gegen Kummer, Hilfetelefon Gewalt gegen Frauen, UPD und BA-Widerspruchsstatistik getrennt normalisieren. Identitäten und Nichtentsprechungen dokumentieren. Abnahme: 4 Quellensysteme mit differenzierten Zähleinheiten.

**P10-B – Organisationen-/Angebots-Crosswalk:** 20 tatsächlich veröffentlichte Organisations-/Dienstprofile prüfen: Registeridentität, Tätigkeitsart, Zielgruppe, Region, Gebühren, Kontaktweg, Stand. Abnahme: 20 einzeln geprüfte Treffer; Registereintrag allein genügt nicht.

**P10-C – Blindstellenanalyse:** Zu zehn typischen Unsichtbarkeiten (keine Kontaktaufnahme, Warteliste, Unkenntnis, Doppelkontakt, verwaltungsinterner Fehler etc.) identifizieren, ob eine sekundäre öffentliche Datenquelle existiert. Abnahme: 10 Negativ- oder Prüfergebnisse.

**P10-D – Skill-Abdeckung:** 15 synthetische Bürgerziele auf vorhandene Skill-IDs und kompetente Hilfswege abbilden. Abnahme: Ergebnisse differenziert nach Wissen/Verfahren/erreichbarer Hilfe/effektiver Zielerreichung.

**P10-E – Öffentliche Wissensrechte:** 20 konkrete Dokumente aus Bund, Ländern, Schulplanung, Fernsehinhalten und Fachportalen klassifizieren: amtliches Werk nach § 5 UrhG, DNG-Status, Dritt-/Lizenzrechte, Zugang und technische Wiederverwendung. Abnahme: 20 überprüfte Werk- und Nutzungsstatus; nicht aus „öffentlich finanziert“ automatisch Gemeinfreiheit ableiten.

## Ergebnisvertrag
`need_signal → need_class → goal → legal/professional source → provider → service_offer → eligibility/access → skill → test → evidence → missing_or_verified_outcome`

Jede Relation benötigt `source_id`, `year`, `region`, `unit`, `scope`, `review_status`. Keine automatische Erhebung personenbezogener Daten. Nicht vorhandene Statistiken erhalten `unknown`, niemals `zero`.

## Fortschritt
Gesamter Bürger-KI-Programmzähler weiterhin **3/10 bisherige Abnahme-Gates**; das Phase-10-Design stellt zusätzliche Forschungsarbeit dar, keine empirisch abgeschlossene Versorgungskartierung. Die nächste messbare Abnahme ist die sachgerechte Verknüpfung von mindestens zwei verschiedenartigen öffentlichen Aggregatquellen mit einem nachgewiesenen Beratungs-/Organisationsangebot unter Beibehaltung unterschiedlicher Zähleinheiten.
