/* Forschungsdaten-Explorer v1: originalgetreue Entwurfsachsen und Skills, keine fingierten Beweise */
(()=>{"use strict";
const $=id=>document.getElementById(id),els=(tag,cls,txt)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(txt!==undefined)e.textContent=txt;return e;};
const state={tensors:[],skills:[],families:[],mode:"tensor",visible:12,query:"",filter:"all",selected:null};
const msg=$("data-feedback"),list=$("data-results"),info=$("data-result-count"),detail=$("data-detail");
const base="./data/";
function txt(node,text){node.textContent=text;}
function link(label,url){const a=els("a","",label);a.href=url;a.target="_blank";a.rel="noopener noreferrer";return a;}
function reset(){state.visible=12;state.selected=null;detail.hidden=true;refresh();}
function matches(t){const q=state.query.trim().toLocaleLowerCase("de");return !q||JSON.stringify(t).toLocaleLowerCase("de").includes(q);}
function renderCard(o){
  const card=els("article","data-card"),title=els("h3","",o.name||o.id);
  const status=o.axes?"Historisches Tensorgerüst":o.type==="python_function"?"Implementierte Funktion":"Format-/Skillkandidat";
  card.append(els("span","data-tag",status),title);
  if(o.axes){card.append(els("p","","Kennung: "+o.id),els("p","","Achsen: "+o.axes.map(a=>a.elements.join(" – ")).join(" | ")),els("p","","Modell: "+(o.model||"historischer CORE-Entwurf")));}
  else if(o.signature){card.append(els("p","",o.signature),els("p","","Geo-KI v0.4 · implementiert; Fachfreigabe separat"));}
  else card.append(els("p","","Formate: "+(o.formats||[]).join(", ")),els("p","","Prüfung offen"));
  const b=els("button","","Details ansehen");b.type="button";b.addEventListener("click",()=>showDetail(o));card.append(b);return card;
}
function showDetail(o){
 detail.replaceChildren();detail.hidden=false;
 const head=els("h3","",o.name||o.id);detail.append(head,els("span","data-tag",o.axes?"Strukturentwurf · nicht fachvalidiert":o.signature?"Geo-KI · implementiert":"Interoperabilität · Kandidat"));
 if(o.axes){
   detail.append(els("p","","ID: "+o.id+" · 3 Trinitäten × 3 Rollen = 27 Feldadressen"));
   const grid=els("div","data-axis-grid");
   o.axes.forEach((a,i)=>{const box=els("article","data-axis");box.append(els("h4","","Trinität "+(i+1)),els("small","",a.status));const ol=els("ol");a.elements.forEach(x=>ol.append(els("li","",x)));box.append(ol);grid.append(box);});
   detail.append(grid);
   if(o.model)detail.append(els("p","","Ausgangsmodell: "+o.model));
   if(o.formula_anchor)detail.append(els("p","","Historischer Formelprüfanker: "+o.formula_anchor));
   if(o.measure)detail.append(els("p","","Messgrößen: "+o.measure));
   detail.append(els("h4","","27 Kombinationen als Untersuchungsadressen"));
   const cells=els("div","data-cells"),readout=els("p","data-status-help","Eine Position auswählen. Die genaue Relation und ihr Beleg wurden historisch noch nicht feldweise validiert.");
   for(let i=0;i<27;i++){
     const a=Math.floor(i/9),b=Math.floor(i%9/3),c=i%3;const btn=els("button","",""+(i+1));btn.type="button";
     const id=o.id+"@v10.7#"+(a+1)+"-"+(b+1)+"-"+(c+1);btn.setAttribute("aria-label","Position "+id);
     btn.addEventListener("click",()=>{cells.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===btn)));txt(readout,id+" · "+o.axes[0].elements[a]+" / "+o.axes[1].elements[b]+" / "+o.axes[2].elements[c]+". Status: adressiert, relationale Belegung und Nachweis offen.");});
     btn.setAttribute("aria-pressed","false");cells.append(btn);
   }
   detail.append(cells,readout,els("p","data-ref","Quelle: KI-Tensor v10.7 Gesamtinventar, überlieferter Strukturentwurf. Keine 27 Einzelbeweise."));
 } else if(o.signature){
   detail.append(els("p","","Funktionssignatur: "+o.signature),els("p","","Prüfstand: im öffentlichen Python-Quellcode implementiert. Der Testbericht nennt 14 bestandene Tests für die Gesamt-Suite; keine individuelle wissenschaftliche Abnahme."));
   detail.append(link("Python-Quellcode ansehen",o.source),els("span",""," · "),link("Testbericht ansehen",o.test_report));
 } else {
   detail.append(els("p","","Formate: "+(o.formats||[]).join(", ")),els("p","","Werkzeugkandidaten: "+(o.tools||[]).join(", ")),els("p","","Risiken und Prüfbedarf: "+(o.risks||"nicht angegeben")),els("p","","Status: Kandidateninventar, keine nachgewiesene Integration."));
   detail.append(link("Originalregister ansehen",o.source));
 }
 const issueTitle="Forschungsfrage zu "+o.id;
 const issueBody="Referenzobjekt: "+o.id+"\nDatenstand: "+(o.axes?"Tensorgrundgeruest v10.7":"Skill-/Formatregister v1")+"\n\nFrage oder Anmerkung:\n\nOriginalquelle und ggf. Gegenprobe:\n\n";
 const feedback=els("p","data-ref");
 feedback.append(link("Öffentliche Frage oder Anmerkung zu "+o.id+" einreichen","https://github.com/Memnosis/relationalitaet/issues/new?title="+encodeURIComponent(issueTitle)+"&body="+encodeURIComponent(issueBody)));
 detail.append(feedback);
 detail.scrollIntoView({behavior:"smooth",block:"start"});
}
function refresh(){
 const arr=state.mode==="tensor"?state.tensors:state.mode==="functions"?state.skills:state.families;
 const visible=arr.filter(matches).filter(x=>state.filter==="all"||(state.filter==="core"?x.id.startsWith("CORE-"):state.filter==="fach"?x.id.startsWith("FACH-"):state.filter==="locked"?x.status==="historisch_gesperrt":true));
 const count=visible.length;txt(info,count+" Einträge · "+state.mode+(state.query?" · gefiltert":""));
 list.replaceChildren();
 visible.slice(0,state.visible).forEach(x=>list.append(renderCard(x)));
 if(!count)list.append(els("p","data-empty","Für diesen Suchbegriff gibt es in diesem veröffentlichten Teilbestand keinen Eintrag."));
 $("data-more").hidden=count<=state.visible;
}
function selectMode(v){state.mode=v;state.filter="all";state.query="";$("data-search").value="";$("data-filter").hidden=v!=="tensor";$("data-filter").value="all";$("data-more").hidden=false;reset();document.querySelectorAll("[data-mode]").forEach(x=>x.setAttribute("aria-pressed",String(x.dataset.mode===v)));}
$("data-search").addEventListener("input",e=>{state.query=e.target.value;reset();});
$("data-filter").addEventListener("change",e=>{state.filter=e.target.value;reset();});
$("data-more").addEventListener("click",()=>{state.visible+=12;refresh();});
document.querySelectorAll("[data-mode]").forEach(b=>b.addEventListener("click",()=>selectMode(b.dataset.mode)));
Promise.all([fetch(base+"tensor-inventar-v10_7.json").then(r=>{if(!r.ok)throw Error("Tensorliste nicht erreichbar");return r.json()}),fetch(base+"skills-oeffentlich-v1.json").then(r=>{if(!r.ok)throw Error("Skillliste nicht erreichbar");return r.json()})])
.then(([t,s])=>{if(t.tensors.length!==103||t.tensors.some(x=>x.axes.length!==3))throw Error("Unvollständiges Tensorinventar");state.tensors=t.tensors;state.skills=s.implemented_geoki_functions;state.families=s.interop_format_families;txt(msg,"103 historische Tensorgerüste, "+state.skills.length+" implementierte Funktionen und "+state.families.length+" Formatfamilien aus belegten Forschungsdateien. Forschungsstände, keine pauschalen Fachfreigaben.");selectMode("tensor");})
.catch(err=>{txt(msg,"Datenabruf fehlgeschlagen: "+err.message+". Bitte die unveränderten JSON-Dateien über die folgenden Datenlinks öffnen.");});
})();