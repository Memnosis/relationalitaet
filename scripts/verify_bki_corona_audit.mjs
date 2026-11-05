import fs from 'node:fs';
const file='docs/data/bki-corona-messvergleich-medienpilot-v0-3.json';
const data=JSON.parse(fs.readFileSync(file,'utf8'));
const errors=[];const ids=new Set();const classCounts={A:0,B:0,C:0,D:0};
if(data.schema!=='bki-corona-benchmark-audit/0.3')errors.push('bad schema');
if(data.measurement_cards.length!==15)errors.push('Expected 15 measurement cards');
for(const x of data.measurement_cards){
 if(ids.has(x.id))errors.push('duplicate '+x.id);ids.add(x.id);
 for(const k of ['id','title','source','comparison','assessment','status'])if(!(k in x))errors.push(x.id+' missing '+k);
 if(!['A','B','C','D'].includes(x.comparison?.class))errors.push(x.id+' invalid comparison class');else classCounts[x.comparison.class]++;
 if(x.comparison?.proven_comparable!==false)errors.push(x.id+' improperly marked comparable');
 if(x.assessment?.research_quality?.status!=='not_formally_assessed')errors.push(x.id+' invents formal review');
 if(x.assessment?.subject_result?.status!=='methodological_finding_only')errors.push(x.id+' invents causal finding');
 if(x.assessment?.evidence_level?.status!=='GRADE_not_assessed')errors.push(x.id+' invents GRADE result');
 if(!Array.isArray(x.assessment?.missing_data)||!x.assessment.missing_data.length)errors.push(x.id+' missing gap');
}
console.log(JSON.stringify({schema:data.schema,count:ids.size,classes:classCounts,formal_medical_grade:0,proven_directly_comparable:0,errors},null,2));
if(errors.length)process.exitCode=1;
