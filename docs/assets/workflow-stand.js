/* Public, redacted evidence-based status for workflow project. */
(()=>{"use strict";
const host=document.getElementById("workflow-status-content");
if(!host)return;
const node=(tag,text,cls)=>{const x=document.createElement(tag);if(text!=null)x.textContent=text;if(cls)x.className=cls;return x};
(async()=>{
try{
const r=await fetch("./data/workflow-stand-v1.json",{cache:"no-store"});if(!r.ok)throw Error("HTTP "+r.status);
const data=await r.json();
if(data.schema_version!=="public-workflow/1.0"||!data.prompt_overview?.labels)throw Error("unknown version");
host.replaceChildren();
const p=data.prompt_overview;
const nums=node("div",null,"pm-stats");
for(const [value,label] of [[p.objects,"Objektvorkommen"],[p.groups,"Bestandsgruppen"],[p.overlapping_occurrences,"Überschneidungen"],[p.mutually_tested,"Gegenseitig geprüfte Prompts"]]){const c=node("div",null,"pm-stat");c.append(node("strong",String(value)),node("small",label));nums.append(c)}host.append(nums);
const hint=node("p","Die 82 Vorkommen sind wegen Überschneidungen nicht 82 eindeutige Prompts. Gemeldet ist ein Modell-Probelauf; die vollständige gegenseitige Gegenprüfung steht aus.","pm-control-help");host.append(hint);
const table=node("table",null,"pm-table");const thead=node("thead");const tr=node("tr");for(const s of ["Promptbereich","Erfasste Vorkommen"]){tr.append(node("th",s))}thead.append(tr);table.append(thead);const body=node("tbody");
for(const item of p.labels){const row=node("tr");row.append(node("td",item.name),node("td",String(item.count)));body.append(row)}table.append(body);host.append(table);
host.append(node("p","Quellenstand: "+data.as_of+" · Die Zahlen werden erst nach fachlicher Freigabe und Versionierung aus den gemeinsamen Datenregistern aktualisiert.","pm-control-help"));
}catch(e){host.replaceChildren(node("p","Die aktuelle Programmübersicht ist noch nicht verfügbar. Bitte das Projektmanagement-Register auf GitHub verwenden.","pm-empty"))}
})();
})();