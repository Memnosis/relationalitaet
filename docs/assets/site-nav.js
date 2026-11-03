/* Site-wide, accessible navigation. Previous static links remain as fallback if JS fails. */
(()=>{'use strict';
const items=[
 {type:'link',label:'Start',href:'index.html'},
 {type:'group',label:'KI & Forschung',members:[
  ['Orientierung · KI-Systeme','ki-systeme.html'],['Kann aus Skills KI entstehen?','ki-kernforschung.html'],
  ['Mini-KI · Kernfunktionen','minimal-ki.html'],['Geo-KI · Formengenerierung','geoki.html'],
  ['KI-Tensor · 3×3×3','tensor-einfuehrung.html'],['Tensoralgebra','tensoralgebra.html'],
  ['Vernetzung & Schwellen','vernetzung-ki.html'],['Kompression','komprimierung.html'],
  ['Harvesting','harvesting.html'],['Visuelle Engine','visuelle-engine.html'],['Tensor-Paper','tensor-paper.html']]},
 {type:'group',label:'Wissen & Werkzeuge',members:[
  ['Bibliothek und Quellen','bibliothek.html'],['Promptbibliothek','promptbibliothek.html'],
  ['Glossar','glossar.html'],['Codebuch','codebuch.html'],
  ['Interoperabilität','interoperabilitaet.html'],['Quellenübergabe','quellen-und-uebergabe.html'],
  ['Aufgabenkarten','taskkarten.html'],['Medien & Grafik','medien.html'],
  ['Projektstand','projektstand.html']]},
 {type:'group',label:'SOULution & Publikationen',members:[
  ['SOULution · neun Bereiche','soulution.html'],['Wissen, Macht und Wirklichkeit','wissen-macht-wirklichkeit.html'],
  ['KI, Stimmen und Musikrechte','soulution-ki-kreativrechte.html'],
  ['Weltwissen und KI-Kritik','ki-kernforschung.html#urheberrecht'],
  ['Bürgerforschung & Rechenschaft','soulution.html#ki-forschungsfrage']]},
 {type:'link',label:'Mitmachen',href:'mitmachen.html'}
];
const current=decodeURIComponent(location.pathname.split('/').pop()||'index.html')||'index.html';
const header=document.querySelector('header.tensor-global-nav')||document.querySelector('header:not(.hero) nav')?.closest('header');
let target=header?.querySelector('nav');
let host=header;
if(!host){host=document.createElement('header');host.className='tensor-global-nav site-injected-header';const inner=document.createElement('div');inner.className='tensor-nav-inner';const logo=document.createElement('a');logo.href='./index.html';logo.className='tensor-brand';logo.textContent='Tensor';inner.append(logo);host.append(inner);document.querySelector('main,body>*')?.before(host);}
if(!target)target=host.querySelector('.tensor-nav-inner')||host;
const nav=document.createElement('nav');nav.className='site-navigation';nav.setAttribute('aria-label','Projektweite Hauptnavigation');nav.setAttribute('data-version','v2');
function a(label,href){const el=document.createElement('a');el.href='./'+href;el.textContent=label;const path=href.split('#')[0];if(path===current)el.setAttribute('aria-current','page');return el;}
for(const item of items){if(item.type==='link'){const link=a(item.label,item.href);link.classList.add('site-nav-mainlink');if(item.label==='Mitmachen')link.classList.add('site-nav-action');nav.append(link);continue;}
 const group=document.createElement('details');group.className='site-nav-group';const summary=document.createElement('summary');summary.textContent=item.label;const panel=document.createElement('div');panel.className='site-menu-panel';panel.setAttribute('role','group');panel.setAttribute('aria-label',item.label);
 for(const [label,href] of item.members)panel.append(a(label,href));
 group.append(summary,panel);if(item.members.some(([,href])=>href.split('#')[0]===current))group.classList.add('site-nav-active-group');
 group.addEventListener('toggle',()=>{if(group.open)nav.querySelectorAll('details.site-nav-group').forEach(other=>{if(other!==group)other.open=false;});});nav.append(group);}
if(target.tagName==='NAV')target.replaceWith(nav);else target.append(nav);
document.querySelectorAll('.ki-fachnavigation').forEach(el=>el.hidden=true);
document.addEventListener('keydown',e=>{if(e.key==='Escape')nav.querySelectorAll('details[open]').forEach(d=>d.open=false);});
document.addEventListener('click',e=>{if(!nav.contains(e.target))nav.querySelectorAll('details[open]').forEach(d=>d.open=false);});
const link=document.createElement('link');link.rel='stylesheet';link.href='./assets/site-nav.css';document.head.append(link);
})();