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
for(const [value,label] of [[p.unique_ids,"Eindeutige Prompt-IDs"],[p.objects,"Erfasste Vorkommen"],[p.overlapping_occurrences,"Identische Überschneidungen"],[p.mutually_tested,"Vollständig wechselseitig getestet"]]){const c=node("div",null,"pm-stat");c.append(node("strong",String(value)),node("small",label));nums.append(c)}host.append(nums);
const hint=node("p","Claudes Crosswalk verzeichnet 82 eindeutige IDs aus 102 Fundvorkommen; 20 Überschneidungen sind anhand von Hashes identisch. Ein begrenzter Paarvergleich für LOGIK-PROMPT-02 liegt vor, aber kein vollständig abgenommener R4-Prompt-Test.","pm-control-help");host.append(hint);
const table=node("table",null,"pm-table");const thead=node("thead");const tr=node("tr");for(const s of ["Promptbereich","Eindeutige Prompt-IDs"]){tr.append(node("th",s))}thead.append(tr);table.append(thead);const body=node("tbody");
for(const item of p.labels){const row=node("tr");row.append(node("td",item.name),node("td",String(item.count)));body.append(row)}table.append(body);host.append(table);
host.append(node("p","Quellenstand: "+data.as_of+" · Die Zahlen werden erst nach fachlicher Freigabe und Versionierung aus den gemeinsamen Datenregistern aktualisiert.","pm-control-help"));
}catch(e){host.replaceChildren(node("p","Die aktuelle Programmübersicht ist noch nicht verfügbar. Bitte das Projektmanagement-Register auf GitHub verwenden.","pm-empty"))}
})();
})();