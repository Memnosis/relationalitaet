import fs from 'node:fs';
const j=JSON.parse(fs.readFileSync('docs/data/bki-benchmark-normalisiert-v0-3.json','utf8'));
const s=JSON.parse(fs.readFileSync('docs/data/bki-benchmark-v0-3.schema.json','utf8'));
const required=s.properties.records.items.required;
const errors=[], ids=new Set();
if(j.schema!=='bki-benchmark/0.3')errors.push('Incorrect schema version');
for(const [i,r] of j.records.entries()){
 for(const key of required)if(!(key in r))errors.push('record '+i+' lacks '+key);
 if(ids.has(r.benchmark_id))errors.push('duplicate '+r.benchmark_id);ids.add(r.benchmark_id);
 if(typeof r.benchmark_id!=='string'||r.benchmark_id.length<3)errors.push('invalid ID at '+i);
 for(const k of ['name','unit','place','observed_period','source','version'])if(typeof r[k]!=='string'||!r[k])errors.push('invalid '+k+' '+i);
 if(r.comparability_status==='authorized_after_validation'&&[r.population,r.measurement_method,r.uncertainty,r.source_date].some(x=>x===null))errors.push('unauthorized semantic comparison '+r.benchmark_id);
 if(r.comparability_status!=='not_authorized'&&r.review_status!=='reviewed')errors.push('unreviewed comparison '+r.benchmark_id);
}
console.log(JSON.stringify({records:j.records.length,unique_ids:ids.size,missing_required_keys:errors.length,semantically_comparable:j.records.filter(r=>r.comparability_status==='authorized_after_validation').length},null,2));
if(errors.length){console.error(errors.join('\n'));process.exitCode=1}
