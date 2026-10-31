# KI-Tensor v5.8 – typisierte Teil-ASTs für DLMF-Funktionen

Identische 300-Formel-Kohorte gegenüber v5.7.

**Tatsächlich ausgeführt:**
- 117 typisierte Funktions-Unterausdrücke in 81 der 300 Formeln extrahiert (Makroname, Typ, geklammerte Argumente, Zeichenoffsets).
- Familien: Gamma 41, Digamma 1, Fehlerfunktion 1, elementare trigonometrische Funktionen 27, Logarithmus 19, Exponentialfunktion 16, Big-O 9, Little-o 3.
- Vier unabhängige algebraische Spezialfunktions-Regressionen mit Symbol-Residual null; Big-O gesondert als asymptotische Aussage.
- **0 zusätzliche vollständige Gleichungsparses; 0 neu fachlich verifizierte Quellenbedingungen; 0 neue Inversenbeweise; 0 neue vollständig geprüfte Trinitäten/Tensoren.**
- Im Codebuch neue Tabellen v58_typed_macro_ast, v58_full_eq_benchmark und v58_type_regression. Historischer Datenbestand erhalten.

**Grenze:** Typisierung eines Teilbaums beweist weder seine komplette Argumentsemantik noch die Original-DLMF-Relation. Nächste Stufe ist die Komposition vollständiger typisierter Ausdrücke mit Quellbedingungen und sicheren spezialfunktionsspezifischen Regeln.

Vollständiges SQLite- und Skriptpaket im Chat: KI_Tensor_DLMF_TypedAST_v5_8_NoLoss.zip.
