/* Public-safe Mitmachen task cards. Only data from the redacted web projection. */
(()=>{"use strict";
const root=document.getElementById("tasks"),filters=document.getElementById("filter");
if(!root||!filters)return;
const make=(tag,text,cls)=>{const e=document.createElement(tag);if(text!==undefined&&text!==null)e.textContent=text;if(cls)e.className=cls;return e};
let current="Alle",tasks=[];
function redraw(){
 root.replaceChildren();
 const shown=tasks.filter(t=>current==="Alle"||t.area===current);
 for(const t of shown){
  const card=make("article",null,"tensor-join-card");card.id=t.id;
  card.append(make("span",t.area+" · "+t.id+" · "+t.status,"small"),make("h3",t.title),make("p",t.public_summary||"Öffentliche Forschungsidee in Vorbereitung.","meta"));
  const approved=t.public_release==="approved"&&t.prompt_execution_status==="passed"&&typeof t.direct_prompt==="string";
  if(approved){
   const d=make("details");d.append(make("summary","Geprüften direkten Arbeits-Prompt ansehen"),make("pre",t.direct_prompt));card.append(d);
   const b=make("button","Geprüften Prompt kopieren");b.type="button";b.addEventListener("click",async()=>{
    try{await navigator.clipboard.writeText(t.direct_prompt);b.textContent="Prompt kopiert"}
    catch(e){d.open=true;b.textContent="Prompt manuell kopieren"}
   });card.append(b);
  }else card.append(make("p","Noch nicht freigegeben: keine Meta-Prompt-Rohtexte und keine behaupteten Ausführungstests.","small"));
  const links=make("p");const issue=make("a","Forschungsfrage als Issue ansprechen");
  issue.href="https://github.com/Memnosis/relationalitaet/issues/new?title="+encodeURIComponent("Mitmachen: "+t.id);
  const result=make("a","Ergebnisdatei vorbereiten");result.href="./mitmachen-rueckgabe.html?task="+encodeURIComponent(t.id);
  links.append(issue,document.createTextNode(" · "),result);card.append(links);root.append(card);
 }
 if(!shown.length)root.append(make("p","Zu diesem Bereich liegen noch keine öffentlichen Taskkarten vor."));
}
fetch("./data/mitmach-public-v2.json",{cache:"no-store"}).then(r=>{if(!r.ok)throw Error("HTTP "+r.status);return r.json()}).then(data=>{
 if(data.schema_version!=="mitmach-public/0.2"||!Array.isArray(data.tasks))throw Error("Schema");
 tasks=data.tasks;
 const areas=["Alle",...new Set(tasks.map(t=>t.area))];
 for(const area of areas){
  const b=make("button",area);b.type="button";b.setAttribute("aria-pressed",String(area===current));
  b.addEventListener("click",()=>{current=area;for(const n of filters.children)n.setAttribute("aria-pressed",String(n===b));redraw()});filters.append(b);
 }
 redraw();
 const hash=decodeURIComponent(location.hash.slice(1));if(hash&&document.getElementById(hash))document.getElementById(hash).scrollIntoView({block:"start"});
}).catch(()=>{
 root.replaceChildren(make("p","Die öffentliche Aufgabenübersicht ist momentan nicht verfügbar."));
 const a=make("a","Freigegebene Aufgabenübersicht als JSON ansehen");a.href="./data/mitmach-public-v2.json";root.append(a);
});
})();