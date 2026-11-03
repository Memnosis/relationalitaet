/* Project management v1.0: read-only public summary; no internal prompts or APIs. */
(()=>{"use strict";
const dataUrl="./data/projektmanagement-v1.json";
const $=id=>document.getElementById(id);
const ownerLabels={gpt:"GPT · Website",claude:"Claude · Daten/Forschung",both:"GPT + Claude"};
const weights={
 gpt:{urgency:4,architecture:3,leverage:3,unblocks:3,risk:3,readiness:2,effort:-1},
 claude:{urgency:4,architecture:4,leverage:3,unblocks:3,risk:4,readiness:2,effort:-1}
};
const sortDescriptions={
 gpt:"GPT-Reihenfolge: öffentliche Wirkung, technische Risiken, Architektur und notwendige Eingangsdaten werden kombiniert. Dies ist eine transparente Planungsannahme.",
 claude:"Claude-Reihenfolge: Provenienz- und Fehlerrisiken, Architektur, Quellensicherheit sowie die Zahl abhängiger Arbeiten erhalten zusätzliches Gewicht.",
 urgency:"Dringlichkeit: P0 wird vor P1 gereiht; gleichrangige Aufgaben nach aktuellen Risiken.",
 architecture:"Architekturwirkung: Welche Aufgabe die gemeinsamen Strukturen und Schnittstellen beeinflusst.",
 leverage:"Schlüsselwirkung: Wie viele weitere Anwendungsbereiche voraussichtlich profitieren.",
 unblocks:"Freigeschaltete Folgeaufgaben: Nur ausdrücklich dokumentierte direkte Abhängigkeiten werden gezählt.",
 risk:"Risiko: Verhindert Quellenfehler, irreführende Freigaben oder Daten- und Websiteverlust.",
 readiness:"Machbarkeit: Welche Aufgabe mit den gegenwärtig vorhandenen Eingaben begonnen werden kann."
};
let snapshot=null;
function el(tag,text,cls){const o=document.createElement(tag);if(text!==undefined&&text!==null)o.textContent=text;if(cls)o.className=cls;return o}
function priorityNum(p){return p==="P0"?3:p==="P1"?2:1}
function score(t,mode){
 if(!weights[mode])return 0;
 const w=weights[mode],s=t.scores||{};
 let sum=priorityNum(t.priority)*4;
 for(const [key,val] of Object.entries(w))sum+=Number(s[key]||0)*val;
 return sum;
}
function rank(t,mode){
 if(weights[mode])return score(t,mode);
 if(mode==="urgency")return priorityNum(t.priority)*100+Number(t.scores.risk||0);
 if(mode==="unblocks")return (t.enables||[]).length*100+Number(t.scores.leverage||0);
 return Number(t.scores[mode]||0)*100+priorityNum(t.priority);
}
function percent(t,stages){const total=stages.length,passed=stages.reduce((n,s)=>n+(t.stage?.[s.key]===1?1:0),0);return Math.round(100*passed/total)}
function makeBadge(label){return el("span",label,"pm-badge")}
function evidenceLink(t){
 const a=el("a","Nachweisdatei");a.href="https://github.com/Memnosis/relationalitaet/blob/main/"+t.evidence;
 a.target="_blank";a.rel="noopener noreferrer";return a;
}
function taskCard(t,stages,mode){
 const box=el("article",null,"pm-task");box.dataset.owner=t.owner;box.id="task-"+t.id;
 const top=el("div",null,"pm-top");const left=el("span",t.id+" · "+(ownerLabels[t.owner]||t.owner),"pm-meta");
 const badges=el("div");badges.append(makeBadge(t.priority));top.append(left,badges);box.append(top);
 box.append(el("h3",t.title,"pm-title"));
 const pct=percent(t,stages);
 const meter=el("div",null,"pm-progress");meter.setAttribute("role","progressbar");meter.setAttribute("aria-label","Dokumentierte Bearbeitungsstufen für "+t.title);meter.setAttribute("aria-valuemin","0");meter.setAttribute("aria-valuemax","100");meter.setAttribute("aria-valuenow",String(pct));
 const fill=el("div",null,"pm-progress-fill");fill.style.width=pct+"%";meter.append(fill);box.append(meter);
 box.append(el("p",pct+" % der dokumentierten Bearbeitungsstufen · "+stages.filter(s=>t.stage?.[s.key]===1).length+" von "+stages.length,"pm-meta"));
 const marks=el("div",null,"pm-stages");for(const st of stages){const ok=t.stage?.[st.key]===1;const span=el("span",(ok?"✓ ":"○ ")+st.label,"pm-stage");span.dataset.done=ok?"yes":"no";marks.append(span)}box.append(marks);
 const impacts=el("p","Wirkt auf: "+(t.domains||[]).join(" · "),"pm-meta");box.append(impacts);
 const direct=(t.enables||[]).filter(id=>snapshot.tasks.some(x=>x.id===id));
 box.append(el("p","Nächster Schritt: "+t.next,"pm-meta"));
 const verification=t.owner_verification||{};const primaryLabel=verification.primary_status==="partial_evidence_only"?"Eigennachweise vorhanden – Abschluss noch offen":verification.primary_status==="not_independently_verified_by_gpt"?"Claude-Eigenprüfung getrennt nachzuweisen":verification.primary_status==="joint_signoff_pending"?"Beide KIs müssen gesondert bestätigen":"Eigennachweise noch offen";
 box.append(el("p","Aufgabenverifikation: "+primaryLabel+" · Gegenevaluation: "+(verification.independent_peer_status==="pending"?"ausstehend":"siehe Prüfakte"),"pm-meta"));
 const details=el("details");const sum=el("summary","Abhängigkeiten, Schlüsselwirkung und Nachweise");details.append(sum);
 const req=el("p","Benötigt: "+(t.requires?.length?t.requires.join(", "):"keine als Pflicht eingetragene Voraufgabe"));details.append(req);
 details.append(el("p","Ermöglicht unmittelbar: "+(direct.length?direct.join(", "):"keine dokumentierte Folgeaufgabe")));
 const w=el("p","Planungswerte (0–3): Dringlichkeit "+t.scores.urgency+", Architektur "+t.scores.architecture+", Hebel "+t.scores.leverage+", Risiko "+t.scores.risk+", Bereitschaft "+t.scores.readiness+".");details.append(w);
 if(weights[mode])details.append(el("p","Gewichteter Prioritätswert: "+score(t,mode)+". Der Wert bewertet Aufgabenplanung, keinen Fortschritt oder wissenschaftlichen Beweis."));
 const trace=el("div");trace.append(el("p","Nachweise je erreichte Stufe (Datei/Version):","pm-meta"));
 const list=el("ul",null,"pm-list");
 for(const st of stages){const ev=t.stage_evidence?.[st.key];if(t.stage?.[st.key]===1&&ev?.path){
 const li=el("li");li.append(el("strong",st.label+" · "));
 const a=el("a",ev.path.split("/").pop());a.href="https://github.com/Memnosis/relationalitaet/blob/main/"+ev.path;a.target="_blank";a.rel="noopener noreferrer";li.append(a);list.append(li);
 }}
 if(list.children.length){trace.append(list);details.append(trace)}
 if(t.last_activity){details.append(el("p","Letzter dokumentierter Änderungsschritt: "+t.last_activity.date+" · "+t.last_activity.summary));const a=el("a","Commit und Änderung öffnen");a.href="https://github.com/Memnosis/relationalitaet/commit/"+t.last_activity.commit;details.append(a)}
 details.append(evidenceLink(t));box.append(details);
 return box;
}
function redraw(){
 if(!snapshot)return;
 const own=$("pm-owner").value,order=$("pm-order").value,pri=$("pm-priority").value;
 $("pm-sort-explain").textContent=sortDescriptions[order];
 const tasks=snapshot.tasks.filter(t=>(own==="all"||t.owner===own||(own==="gpt"&&t.owner==="both")||(own==="claude"&&t.owner==="both"))&&(pri==="all"||t.priority===pri));
 tasks.sort((a,b)=>rank(b,order)-rank(a,order)||a.id.localeCompare(b.id));
 const host=$("pm-task-list");host.replaceChildren();
 if(!tasks.length){host.append(el("p","Für diese Auswahl sind noch keine Aufgaben in der öffentlichen Lesesicht vorhanden.","pm-empty"));return}
 for(const t of tasks)host.append(taskCard(t,snapshot.stages,order));
}
function initStats(){
 const tasks=snapshot.tasks,allDone=tasks.filter(t=>snapshot.stages.every(s=>t.stage?.[s.key]===1));
 const values=[[tasks.length,"Aufgaben in dieser öffentlichen Auswahl"],[tasks.filter(t=>t.owner==="gpt").length,"GPT-Aufgaben"],[tasks.filter(t=>t.owner==="claude").length,"Claude-Aufgaben"],[allDone.length,"In allen sechs Stufen bestätigt"]];
 $("pm-stats").replaceChildren();
 for(const [n,label] of values){const box=el("div",null,"pm-stat");box.append(el("strong",String(n)),el("small",label));$("pm-stats").append(box)}
 $("pm-snapshot").textContent="Datenstand: "+snapshot.snapshot_date+" · "+snapshot.notes;
}
function initImpact(){
 const tasks=snapshot.tasks;
 const sorted=[...tasks].sort((a,b)=>(b.enables?.length||0)-(a.enables?.length||0)||b.domains.length-a.domains.length);
 $("pm-impact-top").replaceChildren();
 for(const t of sorted.slice(0,7)){
 const li=el("li");const a=el("a",t.id+" · "+t.title);a.href="#task-"+t.id;
 a.addEventListener("click",()=>{if($("pm-owner").value!=="all"||$("pm-priority").value!=="all"){$("pm-owner").value="all";$("pm-priority").value="all";redraw()}});
 li.append(a,el("span"," · "+(t.enables?.length||0)+" direkte Folgeaufgaben · "+t.domains.length+" Forschungsfelder","pm-meta"));$("pm-impact-top").append(li)
 }
 const domains=new Map();
 for(const t of tasks)for(const d of t.domains)domains.set(d,(domains.get(d)||0)+1);
 $("pm-domains").replaceChildren();
 for(const [name,count] of [...domains].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]))){
 const tr=el("tr");tr.append(el("td",name),el("td",String(count)));$("pm-domains").append(tr)
 }
}
async function load(){
 try{
 const response=await fetch(dataUrl,{cache:"no-store"});if(!response.ok)throw new Error("HTTP "+response.status);
 const data=await response.json();
 if(data.schema_version!=="pm-public-curated/0.1"||!Array.isArray(data.tasks)||!Array.isArray(data.stages))throw new Error("Unbekanntes Datenformat");
 const ids=data.tasks.map(t=>t.id);
 if(new Set(ids).size!==ids.length)throw new Error("Doppelte Aufgaben-IDs");
 snapshot=data;initStats();initImpact();redraw();
 }catch(err){
 $("pm-snapshot").textContent="Der öffentliche Aufgabenstand konnte nicht geladen werden ("+err.message+").";
 const h=$("pm-task-list");h.replaceChildren();const p=el("p","Die Datenansicht ist derzeit nicht verfügbar. Das Register bleibt auf GitHub einsehbar.");h.append(p);
 const a=el("a","Öffentliches Aufgabenregister öffnen");a.href="https://github.com/Memnosis/relationalitaet/blob/main/docs/data/projektmanagement-v1.json";h.append(a);
 }
}
for(const id of ["pm-owner","pm-order","pm-priority"])$(id)?.addEventListener("change",redraw);
load();
})();