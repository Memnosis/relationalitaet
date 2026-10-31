#!/usr/bin/env python3
"""Execute schema checks on codebuch_v64.sqlite without changing historical data."""
import sqlite3,sys
db=sys.argv[1] if len(sys.argv)>1 else "codebuch_v64.sqlite"
c=sqlite3.connect(db)
assert c.execute("SELECT count(*) FROM v64_pipeline").fetchone()[0]==21
assert c.execute("SELECT count(*) FROM v64_pipeline_edges").fetchone()[0]==20
assert c.execute("SELECT count(*) FROM v64_algebra_axioms").fetchone()[0]==15
assert c.execute("SELECT count(*) FROM v63_algebra_register").fetchone()[0]==20
axes=c.execute("SELECT tensor_id,count(*) FROM v62_axis_inventory WHERE source_family='HISTORIC' GROUP BY tensor_id").fetchall()
assert len(axes)==103 and all(n==3 for _,n in axes)
assert c.execute("SELECT count(*) FROM v44_tensor_feldpruefung").fetchone()[0]==2889
print("PASS: 103 historic 3-axis tensors, 21 stages, 20 edges, 15 axiom candidates")
