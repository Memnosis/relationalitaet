/* Desktop smoke test for public GitHub Pages source, executed locally in GitHub Actions.
 * Checks rendered browser behavior. It does not validate scientific assertions.
 */
import { chromium } from 'playwright';

const root=process.env.TEST_SITE_URL || 'http://127.0.0.1:8765';
const browser=await chromium.launch({headless:true});
const errors=[];
let verified=0;
async function visit(path,check){
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 const jsErrors=[];
 page.on('pageerror',err=>jsErrors.push(err.message));
 try{
  const res=await page.goto(root+'/'+path,{waitUntil:'networkidle',timeout:25000});
  if(!res?.ok())throw Error('HTTP '+res?.status());
  await page.locator('nav.tensor-hierarchical-nav').waitFor({timeout:10000});
  if(await page.locator('nav.tensor-hierarchical-nav details').count()!==5)throw Error('Expected five dropdown groups plus two direct links');
  if(check)await check(page);
  if(jsErrors.length)throw Error('JavaScript errors: '+jsErrors.join(' | '));
  verified++;
  console.log('PASS',path);
 }catch(e){errors.push(path+': '+e.message);console.error('FAIL',path,e.message)}
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
await visit('thesen.html',async p=>{
 await p.locator('[data-thesis-ref="all"] .th-evidence-card').first().waitFor({timeout:12000});
 if(await p.locator('[data-thesis-ref="all"] .th-evidence-card').count()!==6)throw Error('Expected six scoped theme cards');
});
await visit('ki-systeme.html');
await visit('ki-kernforschung.html');
await visit('codebuch.html');
await visit('soulution-schroedingers-inkubator.html');
await visit('soulution-inkubator-quellen.html');
await visit('mitmachen.html');
await visit('geoki.html',async p=>{
 const points=p.locator('#matrix rect');
 if(await points.count()!==27)throw Error('Tensor schematic must have exactly 27 selectable addresses');
 await points.first().click();
 const chosen=await p.locator('#selected').innerText();
 if(!chosen.includes('T1.E1.R1'))throw Error('Incorrect first address, expected T1.E1.R1; got '+chosen);
});
await visit('glossar.html');
await visit('interoperabilitaet.html');
await browser.close();
console.log('BROWSER REPORT:',verified,'pages checked,',errors.length,'issues');
if(errors.length){errors.forEach(x=>console.error(x));process.exitCode=1}
