/* Anonymised, source-limited project-request coverage – no raw user prompts. */
(()=>{"use strict";
const root=document.getElementById("anforderungsabdeckung");
if(!root)return;
const elt=(tag,text)=>{const e=document.createElement(tag);if(text!==undefined)e.textContent=text;return e};
(async()=>{
try{
const response=await fetch("./data/anforderungsabdeckung-v2.json",{cache:"no-store"});
if(!response.ok)throw Error("HTTP "+response.status);
const d=await response.json();
if(d.schema_version!=="user-requirement-coverage-public/0.2"||!Array.isArray(d.groups))throw Error("Schema");
root.replaceChildren();
const summary=elt("p",d.atomic_requirements+" konkretisierte Anforderungen in "+d.groups.length+" Themenfeldern. Für "+d.source_file_refs_present+" Positionen wurde die Existenz der jeweils zugeordneten Git-Datei geprüft. Die exakten letzten 100 Originalnachrichten sind noch nicht vollständig rekonstruiert.");
root.append(summary);
const table=elt("table");table.className="pm-table";
const head=elt("thead"),hdr=elt("tr");
for(const s of ["Forschungs-/Aufgabenfeld","Atomisierte Anforderungen","Zuständigkeit"]){const t=elt("th",s);t.scope="col";hdr.append(t)}head.append(hdr);table.append(head);
const body=elt("tbody");
for(const g of d.groups){const tr=elt("tr");tr.append(elt("td",g.field),elt("td",String(g.items)),elt("td",g.assigned_owner==="both"?"GPT und Claude":g.assigned_owner==="gpt"?"GPT Website":"Claude Daten"));body.append(tr)}table.append(body);root.append(table);root.append(elt('p','Prüfstatus (vorläufig): '+Object.entries(d.status_classes||{}).map(([k,v])=>k+': '+v).join(' · ')));
const p=elt("p","Eine vorhandene Datei belegt noch keinen abgeschlossenen Test oder eine fachlich freigegebene Aussage.");p.className="pm-control-help";root.append(p);
}catch(e){root.replaceChildren(elt("p","Die aktuelle Übersicht ist nicht abrufbar. Das belegte Anforderungsregister bleibt im Git-Archiv verfügbar."))}
})();
})();