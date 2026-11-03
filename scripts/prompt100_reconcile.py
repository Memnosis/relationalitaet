#!/usr/bin/env python3
"""Private-first original message crosswalk. Never commit input, private output,
or real user messages to the public repository. Candidate mappings need review.
"""
import argparse, json, re, sys, zipfile
from pathlib import Path
from datetime import datetime, timezone

STOP=set("der die das und von mit fuer für auf eine einer einem einen als oder ist sind wir ich du uns dem den des zu zur zum im in am an aus bei durch nach vor nicht noch schon jetzt auch aber".split())
def tokens(text):
    return set(w for w in re.findall(r"[^\\W\\d_][\\w-]{2,}",text.lower()) if w not in STOP)

def load_export(path):
    """Read a local ChatGPT JSON export, ZIP export or folder of numbered JSON files."""
    path=Path(path)
    if path.is_dir():
        candidates=sorted(path.glob("conversations*.json"))
        batches=[json.loads(x.read_text(encoding="utf-8")) for x in candidates]
    elif path.suffix.lower()==".zip":
        with zipfile.ZipFile(path) as archive:
            names=sorted(x for x in archive.namelist() if Path(x).name.startswith("conversations") and x.endswith(".json"))
            batches=[json.loads(archive.read(name)) for name in names]
    else:
        batches=[json.loads(path.read_text(encoding="utf-8"))]
    if not batches or any(not isinstance(batch,list) for batch in batches):
        raise ValueError("No valid conversation export found")
    return [convo for batch in batches for convo in batch]

def run(args):
    chats=load_export(args.export)
    allowed=set(json.loads(Path(args.allowlist).read_text(encoding="utf-8")))
    tasks=json.loads(Path(args.requirements).read_text(encoding="utf-8"))["requirements"]
    if not isinstance(chats,list) or not allowed:raise ValueError("Explicit non-empty project chat allowlist and conversation export required")
    msgs,issues=[],[]
    for chat in chats:
        cid=chat.get("id")
        if cid not in allowed:continue
        for mid,node in (chat.get("mapping") or {}).items():
            m=(node or {}).get("message") or {}
            if (m.get("author") or {}).get("role")!="user":continue
            when=m.get("create_time")
            if not isinstance(when,(int,float)):
                issues.append({"chat_id":cid,"message_id":mid,"problem":"missing_create_time"});continue
            c=m.get("content") or {}
            parts=c.get("parts") if c.get("content_type")=="text" else None
            message="\\n".join(x for x in (parts or []) if isinstance(x,str)).strip()
            if not message:
                issues.append({"chat_id":cid,"message_id":mid,"problem":"nontext_or_empty"});continue
            msgs.append({"chat_id":cid,"message_id":mid,"utc":when,"text":message})
    msgs=list({(m["chat_id"],m["message_id"]):m for m in msgs}.values())
    msgs.sort(key=lambda m:(m["utc"],str(m["chat_id"]),str(m["message_id"])))
    msgs=msgs[-args.limit:]
    vocab={t["id"]:tokens(t["summary"]) for t in tasks}
    private=[]
    for seq,m in enumerate(msgs,1):
        terms=tokens(m["text"])
        candidates=[]
        for t in tasks:
            overlap=terms & vocab[t["id"]]
            score=len(overlap)/max(1,len(vocab[t["id"]]))
            if score>=0.25 and len(overlap)>=2:
                candidates.append({"task_id":t["id"],"lexical_overlap":round(score,3),"terms":sorted(overlap)[:12],"review":"human_required"})
        candidates.sort(key=lambda x:(-x["lexical_overlap"],x["task_id"]))
        private.append({"sequence":seq,"chat_id":m["chat_id"],"message_id":m["message_id"],"timestamp_utc":datetime.fromtimestamp(m["utc"],timezone.utc).isoformat(),"original":m["text"],"candidates":candidates[:12],"decision":"requires_manual_review"})
    public={"schema_version":"prompt100-aggregate/0.1","selected_messages":len(private),"requested_messages":args.limit,"source_complete":len(private)==args.limit and not issues,"source_issues":len(issues),"atomic_requirements":len(tasks),"suggested_links":sum(len(r["candidates"]) for r in private),"human_reviewed_links":0,"verified_task_completions":None,"scope":"only explicitly allowed project conversations","note":"Lexical links are search hints, not verified semantic, revision or completion decisions. No raw user text is exported."}
    priv={"schema_version":"prompt100-private/0.1","records":private,"source_issues":issues,"edge_types":["creates","repeats","modifies","replaces","cancels","clarifies","not_related"],"review_required":True}
    Path(args.private_out).write_text(json.dumps(priv,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    Path(args.public_out).write_text(json.dumps(public,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    print(json.dumps(public,ensure_ascii=False))

if __name__=="__main__":
    p=argparse.ArgumentParser()
    for key in ("export","allowlist","requirements","private-out","public-out"):p.add_argument("--"+key,required=True)
    p.add_argument("--limit",type=int,default=100)
    a=p.parse_args()
    if a.limit<1 or Path(a.private_out).resolve()==Path(a.public_out).resolve():p.error("Invalid limit or overlapping private/public paths")
    try:run(a)
    except (ValueError,KeyError,TypeError) as e:print("BLOCKED:",e,file=sys.stderr);sys.exit(2)
