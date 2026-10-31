# KI-Tensor · Crosswalk v4.3 (2026-10-31)

Automatischer Abgleich der aktiven lokalen konsolidierten Datenbanken und DLMF-Tripel.

| Quelle | Zeilen |
|---|---:|
| Historisch v10.7 | 309 |
| Chemie v9.6 | 12 |
| CORE v10.5 | 9 |
| P112 | 12 |
| DLMF-Rohtripel | 675 |
| **Gesamt** | **1.017** |

- 1.007 unterschiedliche normalisierte Elementtripel (sowohl geordnet als auch ungeordnet).
- 10 exakte Übereinstimmungspaare, neun davon CORE105 gegenüber historischen CORE-T-Achsen, eine innerhalb FACH-F054.
- 111 vollständige strukturelle Tensorgruppen aus den Beständen mit expliziten Tensor-IDs, nicht automatisch 111 unterschiedliche wissenschaftlich gültige Tensoren.
- Kein exakter Texttreffer zwischen 675 englischen DLMF-Rohtripeln und historischen Achsen.
- Wortbasierter Mehrfachtrefferfilter: 0 vorgeschlagene Cross-Domain-Verbindungen; dieser Negativbefund ist keine Widerlegung von Relationen.

## Nachweise und Grenzen
Die Relationen zwischen den drei Elementen sind noch nicht durch Quellen- und Formelprüfung nachgewiesen. Der Crosswalk inventarisiert Namen, Herkunft, Position und mögliche Identität. Das zugehörige No-Loss-ZIP `KI_Tensor_Crosswalk_v4_3_NoLoss.zip` mit SQLite, CSV und ausführbarem Buildskript liegt aktuell als Chat-Datei vor und ist noch nicht als GitHub-Release gesichert.

## Nächster Prüfschritt
Bilinguale Begriffsnormalisierung und Formelsemantik an die historische Registerstruktur anbinden; positive und negative Relationen nach Bedingung, Gegenprobe und Quelle vergleichen; neue Tensoren nur bei genau 3 quellengebundenen Trinitäten und 27 durchgeprüften Feldpositionen bestätigen.
