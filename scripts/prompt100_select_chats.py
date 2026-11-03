#!/usr/bin/env python3
"""Private local catalog to select eligible project chat IDs for 100-message review."""
import argparse,json,re
from pathlib import Path
from prompt100_reconcile import load_export
p=argparse.ArgumentParser()
p.add_argument("--export",required=True)
p.add_argument("--out",required=True)
p.add_argument("--pattern",default="tensor|soulution|geo.ki|mini.ki|logik|soziation")
a=p.parse_args()
pattern=re.compile(a.pattern,re.I)
items=[]
for chat in load_export(a.export):
    cid=chat.get("id")
    if not cid:continue
    title=str(chat.get("title") or "")
    n=sum(1 for node in (chat.get("mapping") or {}).values() if ((node or {}).get("message") or {}).get("author",{}).get("role")=="user")
    items.append({"conversation_id":cid,"title":title,"user_messages":n,"candidate_by_title":bool(pattern.search(title)),"selected":False})
Path(a.out).write_text(json.dumps(items,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Private catalog:",len(items),"conversations; manual project-chat selection required.")
