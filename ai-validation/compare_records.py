#!/usr/bin/env python3
import argparse,json
from collections import Counter
from pathlib import Path
from validator import validate
ap=argparse.ArgumentParser();ap.add_argument('records',nargs='+');ap.add_argument('--repo-root',default='.');ap.add_argument('--output');a=ap.parse_args();root=Path(a.repo_root).resolve();items=[];errors=[]
for name in a.records:
 r=json.loads(Path(name).read_text());v=validate(r,root)
 if v['status']!='PASS_INTERNAL_AI_RECORD':errors.append({'file':name,'validation_errors':v['errors']});continue
 unit=r.get('assessment_unit',{}).get('unit_id');cer=r.get('cer',{})
 if not unit or any(str(cer.get(k)) not in {'0','1','?'} for k in ('C','E','R')):errors.append({'file':name,'validation_errors':[{'code':'MISSING_COMPARISON_UNIT_OR_CER'}]});continue
 items.append({'file':name,'record_id':r['record_id'],'unit_id':unit,'C':str(cer['C']),'E':str(cer['E']),'R':str(cer['R']),'rebuilding':cer.get('rebuilding')})
units=sorted({x['unit_id'] for x in items})
if len(units)>1:errors.append({'code':'ASSESSMENT_UNIT_MISMATCH','units':units})
fields={}
for k in ('C','E','R','rebuilding'):
 vals=[x[k] for x in items];counts=dict(Counter(vals));fields[k]={'counts':counts,'agreement':len(counts)<=1,'values':vals}
result={'comparator':'CI-001 AI record comparison 1.0','status':'PASS_COMPARISON' if len(items)>=2 and not errors else 'REJECTED','external_validation':False,'records':items,'field_comparison':fields,'disagreement_fields':[k for k,v in fields.items() if not v['agreement']],'errors':errors}
payload=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
if a.output:Path(a.output).write_text(payload)
print(payload,end='');raise SystemExit(result['status']!='PASS_COMPARISON')
