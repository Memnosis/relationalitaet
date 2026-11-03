/* Thematic thesis evidence cards: curated preview, not the canonical original-thesis register. */
(()=>{"use strict";
const $=id=>document.getElementById(id);
const names={"E0":"These formuliert","E1":"Modell beschrieben","E2":"Einzelfall geprüft","E3":"Unabhängig geprüft","E4":"Im behaupteten Bereich bestätigt"};
const source="./data/thesen-uebersicht-v1.json";
function el(t,txt,cls){const n=document.createElement(t);if(txt!==undefined&&txt!==null)n.textContent=txt;if(cls)n.className=cls;return n}
function card(t,central){
 const a=el("article",null,"th-evidence-card");a.id=central?"these-"+t.id:"these-kontext-"+t.id;
 const head=el("div",null,"th-evidence-heading");const svg=document.createElementNS("http://www.w3.org/2000/svg","svg");svg.classList.add("th-evidence-icon");svg.setAttribute("aria-hidden","true");
 const use=document.createElementNS("http://www.w3.org/2000/svg","use");use.setAttribute("href","./assets/media/research-icons.svg#"+t.icon);svg.append(use);head.append(svg);
 const title=el("h3",t.title);head.append(title);a.append(head);
 const meta=el("div",null,"th-evidence-meta");meta.append(el("span",t.id+" · "+t.field,"th-evidence-id"));
 const level=el("span",t.evidence+" · "+(names[t.evidence]||"offen"),"th-evidence-level");meta.append(level);a.append(meta);
 a.append(el("p",t.question));
 const caveat=el("p","Stand der Nachweise: "+t.evidence_note,"th-evidence-caveat");a.append(caveat);
 const details=el("details");details.append(el("summary","Gegenprüfung und offene Nachweise"));
 details.append(el("p","Was der derzeitige Stand trägt: "+t.evidence_for));
 details.append(el("p","Nächster fachlicher Test: "+t.test));
 details.append(el("p","Quelle der Zuordnung: thematische Website-Prüfung durch GPT. Claudes Originalthesen- und Quellenprüfung steht aus."));
 const refs=el("p");
 const page=el("a","Zum Fachkapitel");page.href="./"+t.page+(t.anchor?"#"+t.anchor:"");refs.append(page);
 if(!central){refs.append(document.createTextNode(" · "));const at=el("a","Thesenübersicht");at.href="./thesen.html#these-"+t.id;refs.append(at)}
 details.append(refs);a.append(details);return a
}
async function run(){
 const targets=[...document.querySelectorAll("[data-thesis-ref]")];if(!targets.length)return;
 try{
 const res=await fetch(source,{cache:"no-store"});if(!res.ok)throw Error("HTTP "+res.status);
 const data=await res.json();
 if(data.schema_version!=="thesis-public-thematic/0.1"||!Array.isArray(data.theses))throw Error("Schema");
 for(const root of targets){
 const requested=root.getAttribute("data-thesis-ref");
 const items=requested==="all"?data.theses:data.theses.filter(t=>t.id===requested);
 if(!items.length){root.textContent="Zu diesem Thema gibt es noch keine freigegebene öffentliche Thesenkarte.";continue}
 root.replaceChildren();
 const grid=el("div",null,"th-evidence-grid");
 for(const t of items)grid.append(card(t,requested==="all"));
 root.append(grid);
 }
 }catch(err){for(const root of targets){const p=el("p","Der aktuelle Evidenzstand konnte nicht geladen werden.");root.replaceChildren(p);const a=el("a","Themen und Prüfgrenzen im Thesenatlas");a.href="./thesen.html";root.append(a)}}
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",run,{once:true});else run();
})();