#!/usr/bin/env python3
"""Reproduzierbares KI-Tensor-No-Loss-Audit: ZIP-Inventar plus getrennte Tabellenkopien.
Usage: python consolidate.py /pfad/zu/archiven /pfad/zu/kernatlas.sqlite /pfad/zu/codebuch_v38.sqlite /pfad/zur/ausgabe
"""
import csv,hashlib,json,sqlite3,sys,zipfile
from pathlib import Path
def main():
 root,old,new,out=map(Path,sys.argv[1:5]);out.mkdir(parents=True,exist_ok=True)
 archives=[];members=[]
 for p in sorted(root.glob("*.zip")):
  with zipfile.ZipFile(p) as z:
   items=[i for i in z.infolist() if not i.is_dir()]
   archives.append(dict(archive=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,files=len(items)))
   for i in items:members.append(dict(archive=p.name,path=i.filename,bytes=i.file_size,crc=hex(i.CRC)))
 for name,data in [("archives.csv",archives),("members.csv",members)]:
  with (out/name).open("w",encoding="utf-8",newline="") as f:
   w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 target=out/"codebuch_vereint.sqlite"
 target.write_bytes(new.read_bytes())
 c=sqlite3.connect(target);c.execute("ATTACH DATABASE ? AS historic",(str(old),))
 names=[r[0] for r in c.execute("SELECT name FROM historic.sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
 for table in names:
  if '"' in table:raise ValueError("unsafe table name")
  c.execute(f'CREATE TABLE IF NOT EXISTS historisch_{table} AS SELECT * FROM historic."{table}"')
 c.execute("DETACH DATABASE historic")
 c.execute("CREATE TABLE IF NOT EXISTS source_gaps (source_id TEXT PRIMARY KEY,expected_count INTEGER,status TEXT)")
 c.executemany("INSERT OR REPLACE INTO source_gaps VALUES(?,?,?)",[("GLOSSAR",1072,"SOURCE_MISSING"),("FELDAKTEN",27,"NOT_RECONCILED"),("RELATION_IDS",12,"NOT_RECONCILED")])
 c.commit();c.close()
 print(json.dumps({"archives":len(archives),"members":len(members),"historic_tables":len(names)},ensure_ascii=False))
if __name__=="__main__":main()
