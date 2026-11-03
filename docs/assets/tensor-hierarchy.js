/* Progressive, hierarchical navigation. Existing navigation stays as fallback. */
(()=>{"use strict";
const groups=[
 {title:"Start",url:"index.html"},
 {title:"Forschung",items:[["Tensor verstehen","tensor-einfuehrung.html"],["KI-Geschichte & Ansätze","ki-geschichte.html"],["KI-Systeme im Vergleich","ki-systeme.html"],["KI-Kernforschung & Skills","ki-kernforschung.html"],["Forschungsthesen","thesen.html"],["Tensoralgebra","tensoralgebra.html"],["Forschungsbibliothek","bibliothek.html"],["Glossar & Codebuch","glossar.html"],["Codebuch-Webindex","codebuch.html"],["Formelernte","harvesting.html"]]},
 {title:"Projekte",items:[["Projektübersicht","projektstand.html"],["Projektmanagement","projektmanagement.html"],["Mini-KI","minimal-ki.html"],["Geo-KI","geoki.html"],["Geo-KI Werkzeuge","geoki-systeme.html"],["Komprimierung","komprimierung.html"],["Visuelle Engine","visuelle-engine.html"],["KI-Kollegen","vernetzung-ki.html"]]},
 {title:"Inkubator",items:[["Forschungsinkubator","inkubator.html"],["Schrödingers Inkubator","soulution-schroedingers-inkubator.html"],["Quellen und Projektvergleich","soulution-inkubator-quellen.html"]]},
 {title:"Publikationen",items:[["Medien & Publikationen","medien.html"],["Forschungsbibliothek","bibliothek.html"],["SOULution Publikationen","soulution.html#publikationen"],["Wissen Macht Wirklichkeit","wissen-macht-wirklichkeit.html"],["KI und kreative Rechte","soulution-ki-kreativrechte.html"],["Weltwissen und KI-Dividende","soulution-weltwissen-dividende.html"]]},
 {title:"Mitmachen",items:[["Mitmachprojekte","mitmachen.html"],["Forschungs-Taskkarten","taskkarten.html"],["Tensoralgebra weiterentwickeln","tensoralgebra.html#algebra-weiterentwickeln"]],special:"join"},
 {title:"SOULution",url:"soulution.html",special:"soulution"}
];
function init(){
 const header=document.querySelector("header.tensor-global-nav"),old=header?.querySelector("nav");if(!old)return;
 const current=location.pathname.split("/").pop()||"index.html";
 const nav=document.createElement("nav");nav.className="tensor-hierarchical-nav";nav.setAttribute("aria-label","Hauptnavigation");
 function link(label,url,cls){const a=document.createElement("a");a.href="./"+url;a.textContent=label;if(cls)a.className=cls;if(url.split("#")[0]===current)a.setAttribute("aria-current","page");return a}
 for(const g of groups){
   if(g.items){
     const d=document.createElement("details");d.className="tensor-nav-group"+(g.special?" tensor-nav-"+g.special:"");
     if(g.items.some(x=>x[1].split("#")[0]===current))d.classList.add("tensor-nav-active");
     const s=document.createElement("summary");s.textContent=g.title;d.append(s);
     const menu=document.createElement("div");menu.className="tensor-nav-menu";
     for(const [name,url] of g.items)menu.append(link(name,url));
     d.append(menu);nav.append(d);
   }else nav.append(link(g.title,g.url,g.special?"tensor-nav-"+g.special:""));
 }
 old.replaceWith(nav);
 const parents=[...nav.querySelectorAll("details")];
 document.addEventListener("click",e=>{for(const d of parents)if(!d.contains(e.target))d.open=false});
 document.addEventListener("keydown",e=>{if(e.key==="Escape"){for(const d of parents)d.open=false}});
 parents.forEach(d=>d.addEventListener("toggle",()=>{if(d.open)parents.filter(x=>x!==d).forEach(x=>x.open=false)}));
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init,{once:true});else init();
})();