/* Desktop smoke test for public GitHub Pages source, executed locally in GitHub Actions.
 * Checks rendered browser behavior. It does not validate scientific assertions.
 */
import { chromium } from 'playwright';
import fs from 'node:fs';

const root=process.env.TEST_SITE_URL || 'http://127.0.0.1:8765';
const browser=await chromium.launch({headless:true});
const errors=[];
let verified=0;
const checks=[];
async function visit(path,check){
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 const jsErrors=[];
 page.on('pageerror',err=>jsErrors.push(err.message));
 try{
  const res=await page.goto(root+'/'+path,{waitUntil:'networkidle',timeout:25000});
  if(!res?.ok())throw Error('HTTP '+res?.status());
  await page.locator('header.tensor-global-nav nav.ux-site-nav').waitFor({timeout:10000});
  const links=page.locator('header.tensor-global-nav nav.ux-site-nav > a');
  if(await links.count()!==8)throw Error('Expected eight current primary navigation links');
  if(check)await check(page);
  if(jsErrors.length)throw Error('JavaScript errors: '+jsErrors.join(' | '));
  verified++;
  checks.push({page:path,status:'passed'});
  console.log('PASS',path);
 }catch(e){errors.push(path+': '+e.message);checks.push({page:path,status:'failed',reason:e.message});console.error('FAIL',path,e.message)}
 finally{await page.close()}
}
await visit('index.html',async p=>{
 await p.getByRole('link',{name:'KI-Systeme vergleichen'}).first().waitFor();
 await p.getByRole('link',{name:'Codebuch-Webindex'}).first().waitFor();
});
await visit('projektmanagement.html',async p=>{
 await p.locator('#pm-task-list .pm-task').first().waitFor({timeout:12000});
 await p.locator('#workflow-status-content .pm-stats').waitFor({timeout:12000});
 await p.locator('#anforderungsabdeckung table tbody tr').first().waitFor({timeout:12000});
 const total=await p.locator('#pm-task-list .pm-task').count();
 if(total!==7)throw Error('Expected 7 visible public and shared task cards, got '+total);
 const info=await p.locator('#workflow-status-content').innerText();
 if(!info.includes('82')||!info.includes('102'))throw Error('Prompt inventory numbers not rendered');
 const owner=p.locator('#pm-owner');await owner.selectOption('claude');
 if(await p.locator('#pm-task-list .pm-task[data-owner="claude"]').count()>0)throw Error('Internal Claude task leaked');
 await owner.selectOption('gpt');await p.locator('#pm-task-list .pm-task').first().waitFor();
 await p.locator('#pm-priority').selectOption('P0');
 await p.locator('#pm-order').selectOption('risk');
});
await visit('tensor-einfuehrung.html',async p=>{
 const detail=p.locator('details').filter({has:p.getByText('Alle 27 Adressen als beschriftete Struktur ansehen')});
 await detail.locator('summary').click();
 const figure=detail.locator('img[src$="tensor_27_structure_only.svg"]');
 await figure.waitFor();
 if(!(await figure.evaluate(img=>img.complete && img.naturalWidth>0)))throw Error('27-address diagram missing or unreadable');
});
await visit('thesen.html',async p=>{
 await p.locator('[data-thesis-ref="all"] .th-evidence-card').first().waitFor({timeout:12000});
 if(await p.locator('[data-thesis-ref="all"] .th-evidence-card').count()!==6)throw Error('Expected six scoped theme cards');
});
await visit('ki-systeme.html');
await visit('ki-kernforschung.html');
await visit('codebuch.html');
await visit('soulution-schroedingers-inkubator.html');
await visit('soulution-inkubator-quellen.html');
await visit('mitmachen.html',async p=>{
 await p.locator('#tasks .tensor-join-card').first().waitFor({timeout:12000});
 const count=await p.locator('#tasks .tensor-join-card').count();
 if(count!==13)throw Error('Expected 13 public task IDs, got '+count);
 if(await p.locator('#tasks pre').count()>0)throw Error('Unexpected raw or approved prompt text in the unapproved public catalog');
 const link=await p.locator('#tasks .tensor-join-card').first().locator('a[href*="mitmachen-rueckgabe.html"]').getAttribute('href');
 if(!link?.includes('?task='))throw Error('Result form link missing public task ID');
});
await visit('geoki.html',async p=>{
 const points=p.locator('#matrix rect');
 if(await points.count()!==27)throw Error('Tensor schematic must have exactly 27 selectable addresses');
 await points.first().click();
 const chosen=await p.locator('#selected').innerText();
 if(!chosen.includes('T1.E1.R1'))throw Error('Incorrect first address, expected T1.E1.R1; got '+chosen);
 await points.last().click();
 const last=await p.locator('#selected').innerText();
 if(!last.includes('T3.E3.R3'))throw Error('Incorrect final address, expected T3.E3.R3; got '+last);
});
await visit('mitmachen-rueckgabe.html',async p=>{
 const form=p.locator('#contribution');
 await form.locator('#task').fill('GEO-OPS-01');
 await form.locator('#question').fill('Kann die Rotation eine Fläche erhalten?');
 await form.locator('#method').fill('Synthetische Geometrie-Eingaben und dokumentierte Schritte');
 await form.locator('#result').fill('Simulierter Testfall: positives Resultat nur im beschriebenen Scope');
 await form.locator('#source').fill('https://example.org/public-example');
 await form.locator('#negative').fill('Grenzfälle wurden noch nicht geprüft');
 await form.locator('#teststatus').selectOption('run_by_contributor');
 const download=p.waitForEvent('download');
 await p.locator('#download-result').click();
 const file=await download;
 if(file.suggestedFilename()!=='forschungsbeitrag-GEO-OPS-01.json')throw Error('Wrong export filename');
 const local=await file.path();
 const content=JSON.parse(fs.readFileSync(local,'utf8'));
 if(content.task_id!=='GEO-OPS-01'||content.submission_status!=='not_submitted'||content.publication_approved!==false)throw Error('Unsafe or incorrect result contract');
 if(!(await p.locator('#status').innerText()).includes('noch nicht eingereicht'))throw Error('Missing no-submission disclaimer');
});
await visit('glossar.html');
await visit('interoperabilitaet.html');
// Bürger-KI standalone questionnaire smoke test; intentionally does not require global tensor nav.
{
 const page=await browser.newPage({viewport:{width:1280,height:850},acceptDownloads:true});
 const name='buerger-ki-kaffeekraenzchen-fragen.html';
 try{
  const response=await page.goto(root+'/'+name,{waitUntil:'networkidle',timeout:25000});
  if(!response?.ok())throw Error('HTTP '+response?.status());
  await page.locator('#bki-form').waitFor();
  await page.locator('#content').fill('Welche Arbeit würdest du bei gleichem Einkommen wirklich gerne machen?');
  await page.locator('#check').check();
  const wait=page.waitForEvent('download');
  await page.locator('#download').click();
  const file=await wait;
  const data=JSON.parse(fs.readFileSync(await file.path(),'utf8'));
  if(data.schema!=='bki-coffee-proposal/0.1'||data.status!=='draft_not_submitted')throw Error('Invalid export contract');
  await page.evaluate(()=>{window.__issueUrl='';window.open=(url)=>{window.__issueUrl=url;return null}});
  await page.locator('#bki-form button[type="submit"]').click();
  const issue=await page.evaluate(()=>window.__issueUrl);
  if(!issue.includes('github.com/Memn')||!issue.includes('/issues/new?title='))throw Error('Actual GitHub issue destination missing');
  await page.locator('#content').fill('zu kurz');
  await page.locator('#download').click();
  const feedback=await page.locator('#feedback').innerText();
  if(!feedback.includes('mindestens 15 Zeichen'))throw Error('Invalid short input accepted');
  verified++;checks.push({page:name,status:'passed',tests:['load','local-json-download','github-issue-handoff','invalid-short-input']});
  console.log('PASS',name);
 }catch(err){errors.push(name+': '+err.message);checks.push({page:name,status:'failed',reason:err.message});console.error('FAIL',name,err.message)}
 finally{await page.close()}
}
await browser.close();
const output={schema_version:'website-browser-smoke/1.0',checked_at:new Date().toISOString(),source_sha:process.env.GITHUB_SHA||'local',browser:'chromium',viewport:{width:1440,height:900},pages_checked:checks.length,pages_passed:verified,pages_failed:errors.length,checks};
fs.mkdirSync('reports',{recursive:true});
fs.writeFileSync('reports/website-browser-smoke.json',JSON.stringify(output,null,2)+'\n');
if(process.env.GITHUB_STEP_SUMMARY){fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY,'## Website Desktop Chromium Regression\n\nSource: `'+output.source_sha+'`\n\n'+verified+'/'+checks.length+' Seiten bestanden, '+errors.length+' fehlgeschlagen.\n\n');}
console.log('BROWSER REPORT:',verified,'pages passed,',errors.length,'issues');
if(errors.length){errors.forEach(x=>console.error(x));process.exitCode=1}
