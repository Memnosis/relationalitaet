# KI-Tensor v5.5 – Parser taxonomy, proof regressions and no-loss

Same 300 sample IDs as v5.3; **no new parser executions** and no demonstrated parser hit-rate improvement. Classification:
- 192 Lark unexpected-token grammar
- 38 elliptic expressions
- 33 special function/macros
- 30 other/parsed
- 4 math environments
- 3 other parser errors.

Six source-linked equation records revisited, five with symbolic or finite regression checks and one open. Source constraints still lack independent complete verification. One conditional inverse-reconstruction formula analysed (geometric series, x != 1 and x^N != 1 for reconstruction of a); non-identifiability at roots of unity. Two boundary counterexamples to *unconditional extrapolations*, not to DLMF source models.

**New fully verified scientific trinitäten: 0. New fully verified tensors: 0.**

Files provided as chat artifact: KI_Tensor_DLMF_Regression_v5_5_NoLoss.zip. Source scripts, test CSVs, SQLite and SHA256 manifest are in that archive. Next: discriminate the 192 unsupported tokens by exact failing grammar, parse original DLMF constraints, and rerun same cohort to measure improvements before full 7,622 corpus.
