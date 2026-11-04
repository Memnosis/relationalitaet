/* Site information architecture v2: present one shared navigation, retain old detail URLs as deep links. */
(function(){
"use strict";
const items=[["Start","index.html"],["KI","ki-systeme.html"],["Tensor","tensor-einfuehrung.html"],["Projekte","projektstand.html"],["Harvesting","harvesting.html"],["Publikationen","publikationen.html"],["Inkubator","inkubator.html"],["Mitmachen","mitmachen.html"],["SOULution","soulution.html"]];
function ready(){
const nav=document.querySelector(".tensor-global-nav nav,header nav[aria-label='Hauptnavigation']");
if(nav){
  nav.classList.add("ux-site-nav");nav.setAttribute("aria-label","Hauptnavigation");
  const here=location.pathname.split("/").pop()||"index.html";
  const sections={"ki-geschichte.html":"ki-systeme.html","ki-kernforschung.html":"ki-systeme.html","minimal-ki.html":"projektstand.html","geoki.html":"projektstand.html","komprimierung.html":"projektstand.html","visuelle-engine.html":"projektstand.html","tensoralgebra.html":"tensor-einfuehrung.html","bibliothek.html":"publikationen.html","medien.html":"publikationen.html","projektmanagement.html":"projektstand.html","thesen.html":"publikationen.html","codebuch.html":"publikationen.html"};
  const current=sections[here]||here;
  nav.replaceChildren(...items.map(([label,href])=>{let a=document.createElement("a");a.href="./"+href;a.textContent=label;if(href===current)a.setAttribute("aria-current","page");if(label==="SOULution")a.style.color="var(--ux-soul,#49a477)";return a;}));
}
let foot=document.querySelector("body > footer");
if(foot){
let link=foot.querySelector('a[href$="projektmanagement.html"]');
if(!link){link=document.createElement("a");link.href="./projektmanagement.html";link.textContent="Projektmanagement";link.setAttribute("aria-label","Projektmanagement und Aufgabenstand");link.className="ux-stealth-pm";foot.append(" · ",link);}
else link.classList.add("ux-stealth-pm");
function hide(){const c=getComputedStyle(foot).backgroundColor;const b=getComputedStyle(document.body).backgroundColor;link.style.color=(!c||c==="rgba(0, 0, 0, 0)"||c==="transparent")?b:c;}
hide();link.addEventListener("blur",hide);link.addEventListener("focus",()=>{link.style.color=getComputedStyle(foot).color;});link.addEventListener("mouseenter",()=>{link.style.color=getComputedStyle(foot).color;});link.addEventListener("mouseleave",hide);
}
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",ready);else ready();
})();