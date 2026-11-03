(()=>{"use strict";
const host=document.getElementById("portfolio-cards"),summary=document.getElementById("portfolio-summary"),sort=document.getElementById("port-sort"),filter=document.getElementById("port-focus");if(!host)return;
const elem=(tag,content,cls)=>{const e=document.createElement(tag);if(content!=null)e.textContent=content;if(cls)e.className=cls;return e};
let items=[];
function score(item){return item.dependency_leverage*2+item.impact_risk}
function redraw(){let list=items.filter(x=>filter.value==="all"||x.priority===filter.value);
if(sort.value==="priority")list.sort((a,b)=>(b.priority==="P0")-(a.priority==="P0")||score(b)-score(a)||a.id.localeCompare(b.id));
if(sort.value==="leverage")list.sort((a,b)=>b.dependency_leverage-a.dependency_leverage||a.id.localeCompare(b.id));
if(sort.value==="risk")list.sort((a,b)=>b.impact_risk-a.impact_risk||a.id.localeCompare(b.id));
if(sort.value==="name")list.sort((a,b)=>a.name.localeCompare(b.name,"de"));
summary.textContent=list.length+" von "+items.length+" öffentlich belegten Projektfeldern · Rangwerte sind redaktionelle Schätzungen, keine Messwerte.";
host.replaceChildren();
for(const [i,x] of list.entries()){const c=elem("article",null,"portfolio-card");c.dataset.priority=x.priority;c.id="portfolio-"+x.id;
c.append(elem("p","Rang "+(i+1)+" · "+x.priority+" · "+(x.owner==="both"?"gemeinsame Arbeit":x.owner==="gpt"?"GPT Website":"Claude Forschung"),"p-meta"),elem("h3",x.name),elem("p",x.scope));
c.append(elem("p","Planungswert "+score(x)+" (Hebel "+x.dependency_leverage+"/5 × 2 + Risiko "+x.impact_risk+"/5)","p-score"));
c.append(elem("p","Nächste überprüfbare Arbeit: "+x.next));
const a=elem("a","Fachseite und bisherige Ergebnisse ansehen");a.href="./"+x.page.replace(/^docs\//,"");c.append(a);
c.append(elem("p","Fachliche Gesamtfreigabe: nicht anhand dieser Portfolioansicht nachgewiesen.","p-meta"));host.append(c)}
}
Promise.resolve(fetch("./data/projektportfolio-v1.json",{cache:"no-store"})).then(r=>{if(!r.ok)throw Error("HTTP "+r.status);return r.json()}).then(d=>{if(d.schema_version!=="public-portfolio/0.1"||!Array.isArray(d.items))throw Error("Schema");items=d.items;redraw()}).catch(()=>{host.replaceChildren(elem("p","Die öffentliche Projektübersicht konnte nicht geladen werden."));summary.textContent="Lesesicht derzeit nicht verfügbar."});
sort.addEventListener("change",redraw);filter.addEventListener("change",redraw);
})();