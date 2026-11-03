#!/usr/bin/env python3
"""Project-wide Git checkout audit: ALL file paths, SHA256, local webpage links and sources.
Usage: python forschung/website/AUDIT_ALLE_DATEIEN.py --root . --out full_source_inventory.json
Requires complete git checkout; not a verified full historical local_only archive.
"""
from pathlib import Path
from urllib.parse import urlparse,unquote
from html.parser import HTMLParser
from collections import Counter
import argparse,hashlib,json,os,re
SKIP={'.git','.venv','node_modules','__pycache__','.pytest_cache'}
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if d.get('id'):self.ids.add(d['id'])
  for k in ('href','src','poster','data-src'):
   if d.get(k):self.refs.append(d[k])
def scan(root):
 root=root.resolve();paths=[]
 for d,dirs,files in os.walk(root):
  dirs[:]=sorted(x for x in dirs if x not in SKIP)
  paths.extend(Path(d)/n for n in sorted(files) if (Path(d)/n).is_file())
 names={p.relative_to(root).as_posix() for p in paths};pages={};files=[];refs=[];source_urls=set()
 for p in paths:
  rel=p.relative_to(root).as_posix();size=p.stat().st_size
  h=hashlib.sha256()
  with p.open('rb') as f:
   for buf in iter(lambda:f.read(1048576),b''):h.update(buf)
  files.append({'path':rel,'bytes':size,'sha256':h.hexdigest(),'extension':p.suffix.lower()})
  if p.suffix.lower() in ('.html','.htm'):
   a=Parser();a.feed(p.read_text(encoding='utf8',errors='replace'));pages[rel]=a
 for p in paths:
  if p.suffix.lower() not in ('.html','.htm','.md','.txt','.json','.svg','.css','.js','.py','.yaml','.yml','.xml'):continue
  rel=p.relative_to(root).as_posix();text=p.read_text(encoding='utf8',errors='replace')
  urls=[]
  if rel in pages:urls+=pages[rel].refs
  if p.suffix.lower() in ('.md','.txt'):
   urls += re.findall(r'\\[[^\\]]+\\]\\(([^)]+)\\)',text)
  urls += re.findall(r'https?://[^\\s\"\\'<>),]+',text)
  for url in dict.fromkeys(urls):
   u=urlparse(url);fragment=unquote(u.fragment)
   if u.scheme in ('http','https'):
    source_urls.add(url)
    if u.netloc!='memnosis.github.io' or not u.path.startswith('/relationalitaet/'):continue
    target='docs/'+u.path.split('/relationalitaet/',1)[1]
   elif u.scheme or url.startswith(('mailto:','tel:','javascript:','data:')):continue
   elif url.startswith('#'):target=rel
   elif u.path.startswith('/relationalitaet/'):target='docs/'+u.path[len('/relationalitaet/'):]
   elif u.path.startswith('/'):continue
   else:target=(p.parent/u.path).resolve().relative_to(root).as_posix()
   if target.endswith('/'):target+='index.html'
   if target in names:
    status='exists'
    if fragment and target in pages and fragment not in pages[target].ids:status='anchor_requires_dynamic_review'
   else:status='missing_file'
   refs.append({'source':rel,'target':target,'fragment':fragment,'status':status})
 counts=Counter(f['extension'] for f in files)
 return {'schema':'ki-tensor.project-sources.full-checkout.v1','scope':'full checkout only; local_only archives not included',
         'files_total':len(files),'extensions':dict(counts),'files':files,'local_references':refs,
         'source_urls':sorted(source_urls),
         'missing_local_links':[r for r in refs if r['status']=='missing_file'],
         'uncertain_dynamic_anchors':[r for r in refs if r['status']=='anchor_requires_dynamic_review'],
         'notes':['URL collection does not assert a link is reachable','Generated task anchors may exist only after JavaScript','Scientific source claim review requires original documents','Historical project inventory may reference local_only records']}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path('.'));a.add_argument('--out',type=Path,default=Path('full_source_inventory.json'));args=a.parse_args()
 result=scan(args.root);args.out.parent.mkdir(parents=True,exist_ok=True)
 args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\\n',encoding='utf8')
 print('Files:',result['files_total'],'Links missing:',len(result['missing_local_links']),'Dynamic anchors:',len(result['uncertain_dynamic_anchors']))
