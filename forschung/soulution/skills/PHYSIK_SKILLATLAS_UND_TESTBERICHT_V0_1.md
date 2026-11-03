# Physik-Skillatlas · reale Skilltests und redaktionelle Übergaben

Stand: 2026-11-03. Reproduktionspaket im Gesprächsanhang **SOULution_Physik_Skillbibliothek_Pilot_v01.zip**. Die ZIP-Datei ist kein GitHub-Anhang und muss separat übernommen werden.

## Tatsächlicher Test
SymPy 1.14.0, SciPy 1.17.0, NumPy 2.3.5 und NetworkX 3.6.1 sind in der lokalen Testumgebung vorhanden. Das Modell eines idealen ungedämpften harmonischen Oszillators mit m=2 kg, k=8 N/m, x0=1.5 m wurde symbolisch und numerisch geprüft. 9/9 automatische Assertions erfolgreich. Maximaler Positionsfehler 9.892442420778025e-11 m, maximaler relativer Energiefehler 1.3189923227704034e-10. Rückrechnung der Federkonstante bestanden. Gedämpfte Dynamik und grobes Euler-Verfahren als Verletzung der Energieinvarianz erkannt. Dimensionsfehler abgewiesen.

## Externe Bibliotheken
- SymPy — https://docs.sympy.org/latest/guides/physics/index.html (lokal installiert, getestet)
- SciPy — https://docs.scipy.org/doc/scipy/ (lokal installiert, getestet)
- NumPy — https://numpy.org/doc/ (lokal installiert, getestet)
- NetworkX — https://networkx.org/ (lokal installiert, getestet)
- QuTiP — https://qutip.org/ (extern dokumentiert, lokal nicht installiert)
- Scikit-HEP — https://scikit-hep.org/ (extern dokumentiert, lokal nicht installiert)

Versuch, SymPy 1.14.0 per pip neu herunterzuladen: DNS-Fehler. **Kein erfolgreicher externer Paketdownload**. Vorhandene lokale Bibliotheken wurden ausgeführt; deren vollständiger Quellcode wurde nicht neu verteilt.

## Die sechs verdichteten Kernskills
| Skill | Funktion | Bibliothek | Stand |
|---|---|---|---|
| PHYS-S01 | Modell und Parameter definieren | SymPy | teilweise getestet |
| PHYS-S02 | Formel herleiten/prüfen | SymPy | ausgeführt |
| PHYS-S03 | Differentialgleichung simulieren | SciPy, NumPy | ausgeführt |
| PHYS-S04 | Invarianten und Gegenbeispiele prüfen | SymPy, SciPy | ausgeführt |
| PHYS-S05 | Rückrechnung und Dimensionen | SymPy, NumPy | ausgeführt |
| PHYS-S06 | Skillabhängigkeiten gliedern | NetworkX | ausgeführt |

Dreierbeziehungen sind **didaktische Relationskandidaten** und keine tensorvalidierten Strukturen. Der 3×3×3-Vollnachweis ist offen.

## Verknüpfung mit vorhandenen Forschungs-Prompts
H1 / P01: Quelle–Behauptung–Nachweis; vorhandene Skillkandidaten SK-PDF-EXTRACT, SK-EVIDENCE.
H2 / P02: Geldfluss, Summenprüfung, Rückrechnung; SK-FIN-FLOW, SK-VIZ, PHYS-S05 (Methodenübertrag, **nicht** Finanzdaten-Test).
H3 / P03: wissenschaftliche Evidenz, Modelle, Gegenprobe; SK-EVIDENCE, PHYS-S04 (Methodenübertrag).
H4 / P07: Rechtsgrundlage und Kontrollkette; SK-LEGAL-TRACE, SK-EVIDENCE (**nicht ausgeführt**).
H5 / P05: Lösungen finden und vergleichen; SK-EVIDENCE, SK-VIZ (**nicht ausgeführt**).
P04: Ziele, Maßnahme, Wirkung; SK-EVIDENCE, PHYS-S05 (Methodenübertrag).
P06: Bibliotheks-/Skillfinder und Datenzugang; SK-PDF-EXTRACT, PHYS-S06 (nur Bibliotheksinventar/Graph getestet).
P08: Relations-/Tensorübergabe; SK-REL, PHYS-S06 (Graphstruktur getestet, Tensor offen).

## Nichtsprachliche Strukturen mit Testnachweis
1. Physikalische Modell- und Invariantenstruktur — ausgeführt, 9 Checks.
2. Skill-Abhängigkeitsgraph — drei Modellrouten als gerichtete Graphen, 3/3 azyklisch; nur Struktur, keine selbständigen Agenten.
3. 3×3×3-Vorab-Gate — drei synthetische Strukturfälle, rein numerische Vorprüfung; kein Tensorbeweis.

## Interkapitelstruktur
Der Übergang von einem Buchkapitel zum nächsten verbindet (a) die fachliche Frage, (b) den zugehörigen Kernskill, (c) seine Grenzen und (d) eine neue weiterführende Forschungsfrage. Am Kapitelübergang kann eine 0.5–1-seitige verdichtete Skillkarte stehen. Ein ausführlicher Prompt, Agenten-Bündel oder Meta-Thema erscheint nur, wenn es auf diesem Übergang neue Relationen eröffnet.

## Redaktionelle Grenze
Kapitelumfang aus didaktischem Erklärungsbedarf ableiten. Mini-Prompts sind Satzimpulse, Hauptprompts können ganze Gliederungen und Forschungsbereiche erschließen, Meta-Prompts optimieren Prompts, Agentenrollen orchestrieren Skills, und der Tensor prüft tieferliegende Relationen. Nur empirisch geprüfte Skillketten als ausgeführt bezeichnen.
