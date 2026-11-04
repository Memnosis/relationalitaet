/* Forschungsplattform · einzige aktive Navigation + Themenwegweiser · v3.1
   Historische Detail-URLs bleiben erhalten. Keine zweite Navigationsinstanz. */
(()=>{"use strict";
const items=[["Start","index.html","project"],["KI","ki-systeme.html","ki"],["Tensor","tensor-einfuehrung.html","tensor"],["Projekte","projektstand.html","project"],["Harvesting","harvesting.html","harvest"],["Publikationen","publikationen.html","book"],["Mitmachen","mitmachen.html","colleagues"],["SOULution","soulution.html","colleagues"]];
const parents={
"ki-geschichte.html":"ki-systeme.html","ki-kernforschung.html":"ki-systeme.html","vernetzung-ki.html":"ki-systeme.html",
"minimal-ki.html":"projektstand.html","geoki.html":"projektstand.html","geoki-systeme.html":"projektstand.html","komprimierung.html":"projektstand.html","visuelle-engine.html":"projektstand.html",
"tensoralgebra.html":"tensor-einfuehrung.html","tensor-paper.html":"tensor-einfuehrung.html",
"bibliothek.html":"publikationen.html","inkubator.html":"publikationen.html","soulution-schroedingers-inkubator.html":"publikationen.html","soulution-inkubator-quellen.html":"publikationen.html","medien.html":"publikationen.html","projektmanagement.html":"projektstand.html","projektportfolio.html":"projektstand.html","thesen.html":"publikationen.html","codebuch.html":"publikationen.html","glossar.html":"publikationen.html","forschungsdaten.html":"publikationen.html","interoperabilitaet.html":"publikationen.html",
"taskkarten.html":"mitmachen.html","mitmachen-rueckgabe.html":"mitmachen.html","quellen-und-uebergabe.html":"publikationen.html","soulution-ki-kreativrechte.html":"soulution.html","soulution-weltwissen-dividende.html":"soulution.html","wissen-macht-wirklichkeit.html":"soulution.html"
};
const palettes={ki:["var(--ux-ki)","ki"],tensor:["var(--ux-tensor)","tensor"],mini:["var(--ux-mini)","mini"],geo:["var(--ux-geo)","earth"],kompr:["var(--ux-kompr)","compress"],visual:["var(--ux-visual)","eye"],projekte:["var(--ux-projekte)","project"],pub:["var(--ux-pub)","book"],ink:["var(--ux-ink)","inkubator"],harv:["var(--ux-harv)","harvest"],soul:["var(--ux-soul)","colleagues"]};
const roles={
"ki-systeme.html":"ki","ki-geschichte.html":"ki","ki-kernforschung.html":"ki","vernetzung-ki.html":"ki",
"minimal-ki.html":"mini","komprimierung.html":"kompr","visuelle-engine.html":"visual","geoki.html":"geo","geoki-systeme.html":"geo",
"tensor-einfuehrung.html":"tensor","tensoralgebra.html":"tensor","tensor-paper.html":"tensor",
"harvesting.html":"harv","projektstand.html":"projekte","projektportfolio.html":"projekte","projektmanagement.html":"projekte",
"inkubator.html":"ink","soulution-schroedingers-inkubator.html":"ink","soulution-inkubator-quellen.html":"ink",
"bibliothek.html":"pub","codebuch.html":"pub","glossar.html":"pub","thesen.html":"pub","medien.html":"pub","publikationen.html":"pub","forschungsdaten.html":"pub","interoperabilitaet.html":"pub","quellen-und-uebergabe.html":"pub",
"soulution.html":"soul","soulution-ki-kreativrechte.html":"soul","soulution-weltwissen-dividende.html":"soul","wissen-macht-wirklichkeit.html":"soul",
"mitmachen.html":"projekte","mitmachen-rueckgabe.html":"projekte","taskkarten.html":"projekte"
};
const iconMap={"ki-ansaetze":"ki","ki-geschichte":"history","ki-kernforschung":"workflow","ki-kollegen":"colleagues","ki-publikationen":"book","vier-kernprojekte":"project","vier-projekte":"project","projektportfolio":"project","tensor-algebra-block":"algebra","inkubator-uebersicht":"inkubator","inkubator-deep-dive":"book","inkubator-quellen":"database","daten-explorer":"database","status-grenzen":"tensor","daten-originale":"book"};
const key=location.pathname.split("/").pop()||"index.html";const active=parents[key]||key;const labelFor=Object.fromEntries(items.map(x=>[x[1],x[0]]));
function svgSymbol(name,size){const ns="http://www.w3.org/2000/svg",svg=document.createElementNS(ns,"svg"),use=document.createElementNS(ns,"use");svg.setAttribute("viewBox","0 0 24 24");svg.setAttribute("width",String(size));svg.setAttribute("height",String(size));svg.setAttribute("aria-hidden","true");use.setAttribute("href","./assets/tensor-icons.svg#"+name);svg.append(use);return svg;}
function init(){
 document.body.classList.add("ux-site-v3");document.body.classList.remove("ux-site-v2");
 const role=roles[key]||"tensor",theme=palettes[role]||palettes.tensor;
 document.body.style.setProperty("--ux-page-accent",theme[0]);
 document.body.style.setProperty("--ux-page-icon",'"'+theme[1]+'"');
 const header=document.querySelector("header.tensor-global-nav"),old=header?.querySelector("nav");
 if(header&&old){
  const nav=document.createElement("nav");nav.className="ux-site-nav";nav.setAttribute("aria-label","Hauptnavigation");
  for(const [name,href,icon] of items){
   const a=document.createElement("a");a.href="./"+href;a.append(svgSymbol(icon,16),document.createTextNode(name));
   if(href===active)a.setAttribute("aria-current",key===href?"page":"location");
   if(name==="Mitmachen")a.classList.add("tensor-nav-join");
   if(name==="SOULution")a.classList.add("tensor-nav-soulution");
   nav.append(a);
  }
  old.replaceWith(nav); /* ersetzt auch die vom alten Hierarchie-Skript erzeugte Navigation */
 }
 document.querySelectorAll(".ux-topic").forEach(section=>{
  const icon=section.querySelector(".ux-topic-head > .ux-topic-icon");if(!icon)return;
  const tone=section.dataset.tone||role;
  icon.replaceChildren(svgSymbol(iconMap[section.id]||palettes[tone]?.[1]||"tensor",27));
 });
 const main=document.querySelector("main");
 if(main){
   for(const section of main.querySelectorAll(":scope > section:not(.ux-topic)")){
    const heading=section.querySelector(":scope > h2");
    if(!heading||heading.querySelector(".ux-legacy-heading-icon"))continue;
    const mark=svgSymbol(theme[1],23);mark.classList.add("ux-legacy-heading-icon");heading.prepend(mark);
   }
 }
 if(main && key!=="index.html"){
  const crumbs=document.createElement("nav");crumbs.className="ux-breadcrumb";crumbs.setAttribute("aria-label","Brotkrumennavigation");
  const home=document.createElement("a");home.href="./index.html";home.textContent="Start";crumbs.append(home);
  if(active!==key){const parent=document.createElement("a");parent.href="./"+active;parent.textContent=labelFor[active]||"Übersicht";crumbs.append(parent);}
  const now=document.createElement("span");now.setAttribute("aria-current","page");const h=main.querySelector("h1");now.textContent=key===active?(labelFor[active]||"Thema"):(h?.textContent?.trim().slice(0,65)||"Vertiefung");crumbs.append(now);
  main.insertBefore(crumbs,main.firstChild);
  // Nur einen Inhaltswegweiser: vorhandene Fach- und Lerngliederung hat Vorrang.
  const hasLocal=main.querySelector("nav.ux-inline-nav,nav.geo-chapters,nav.tns-lead-nav,nav.join-six");
  if(!hasLocal){
   const sections=[...main.querySelectorAll(":scope > section")].filter(s=>s.querySelector("h2"));
   const used=new Set([...main.querySelectorAll("[id]")].map(e=>e.id));
   let entries=[];
   for(const [i,s] of sections.entries()){
    const h=s.querySelector("h2");if(!h)continue;
    if(!s.id){let id="thema-"+h.textContent.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"").slice(0,40);
      let base=id,n=2;while(used.has(id))id=base+"-"+n++;s.id=id;used.add(id);}
    const label=h.textContent.trim().replace(/\s+/g," ").slice(0,50);if(label)entries.push([label,s.id]);
   }
   if(entries.length>=2){
    const nav=document.createElement("nav");nav.className="ux-context-nav";nav.setAttribute("aria-label","Abschnitte dieser Seite");
    const title=document.createElement("span");title.className="ux-context-title";title.textContent="Auf dieser Seite";nav.append(title);
    const holder=document.createElement("div");holder.className="ux-context-links";
    for(const [label,id] of entries.slice(0,8)){const a=document.createElement("a");a.href="#"+id;a.textContent=label;holder.append(a);}
    if(entries.length>8){const d=document.createElement("details"),summary=document.createElement("summary");summary.textContent="Alle "+entries.length+" Themen";d.append(summary);for(const [label,id] of entries.slice(8)){const a=document.createElement("a");a.href="#"+id;a.textContent=label;d.append(a);}holder.append(d);}
    nav.append(holder);const hero=main.querySelector(":scope > .ux-hero,:scope > .geo-hero");if(hero)hero.after(nav);else crumbs.after(nav);
   }
  }
 }
 const footer=document.querySelector("body > footer");
 if(footer){let pm=footer.querySelector('a[href$="projektmanagement.html"]');if(!pm){pm=document.createElement("a");pm.href="./projektmanagement.html";pm.textContent="Projektmanagement";footer.append(" · ",pm);}pm.classList.add("ux-stealth-pm");pm.setAttribute("aria-label","Projektmanagement und Aufgabenstand");}
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init,{once:true});else init();
})();