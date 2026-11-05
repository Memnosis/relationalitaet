# Benchmark-Datenqualitätsaudit

Stand 2026-11-05. Bei 10 Datensätzen des Beispieldatenbestands v0.2 fehlen Pflichtfelder. Die Kennung `id` entspricht nicht `benchmark_id`; `population`, `observed_period`, `measurement_method`, `uncertainty`, `version`, `review_status` sind in allen zehn Datensätzen nicht als benannte Pflichtfelder vorhanden. `source_date` fehlt in acht Fällen. **Keine formelle Interoperabilitätsfreigabe.**

Nächster Schritt: bestehende Datensätze unverändert belassen; neue v0.3 mit vollständigem Vertrag, ehrlich mit null markierten Unbekannten und Validierung anlegen. Erst danach Referenzversionen, semantische Equivalenz, Einheiten, räumliche/zeitliche Auflösung und Rücktransformationen prüfen.
