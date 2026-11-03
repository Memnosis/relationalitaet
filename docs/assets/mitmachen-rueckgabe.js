/* Zero-network client-side export. No submitted/persisted data or assumed approval. */
(()=>{"use strict";
const form=document.getElementById("contribution");
if(!form)return;
const status=document.getElementById("status");
const fields=["task","question","method","result","source","negative","teststatus"];
function record(){
 if(!form.reportValidity())throw Error("Bitte alle Pflichtfelder ausfüllen.");
 const v=Object.fromEntries(fields.map(id=>[id,document.getElementById(id).value.trim()]));
 if(!/^[A-Za-z0-9][A-Za-z0-9._-]{1,69}$/.test(v.task))throw Error("Die Aufgaben-ID enthält ungültige Zeichen.");
 return {schema_version:"mitmach-ergebnis/0.1",task_id:v.task,question:v.question,method_and_inputs:v.method,observation:v.result,public_source_and_pinpoint:v.source,negative_findings:v.negative,test_status:v.teststatus,independent_review:"pending",publication_approved:false,created_at:new Date().toISOString(),submission_status:"not_submitted"};
}
function payload(){return JSON.stringify(record(),null,2)+"\n"}
document.getElementById("copy-result").addEventListener("click",async()=>{
 try{const text=payload();if(!navigator.clipboard?.writeText)throw Error("Zwischenablage nicht verfügbar. Bitte die JSON-Datei erstellen.");await navigator.clipboard.writeText(text);status.textContent="JSON in die Zwischenablage kopiert – noch nicht eingereicht."}
 catch(e){status.textContent=e.message}
});
document.getElementById("download-result").addEventListener("click",()=>{
 try{
 const text=payload(),name=record().task_id;
 const blob=new Blob([text],{type:"application/json;charset=utf-8"});
 const url=URL.createObjectURL(blob),a=document.createElement("a");
 a.href=url;a.download="forschungsbeitrag-"+name+".json";document.body.append(a);a.click();a.remove();
 setTimeout(()=>URL.revokeObjectURL(url),1500);
 status.textContent="JSON-Datei erstellt – noch nicht eingereicht. Vor der Weitergabe sensible Angaben überprüfen.";
 }catch(e){status.textContent=e.message}
});
form.addEventListener("reset",()=>{status.textContent=""});
})();