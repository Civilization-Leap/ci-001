#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path
from validator import section_slice
ap=argparse.ArgumentParser();ap.add_argument('scenario');ap.add_argument('--repo-root',default='.');ap.add_argument('--output',required=True);a=ap.parse_args();root=Path(a.repo_root).resolve();s=json.loads(Path(a.scenario).read_text())
excerpts=[]
for req in s['required_sections']:
 p=(root/req['source_path']).resolve();text=p.read_text();section=section_slice(text,req['section'])
 if section is None:raise SystemExit('section not found: '+req['section'])
 excerpts.append({'source_path':req['source_path'],'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'section':req['section'],'exact_section_text':section})
task={'task_format':'CI-001 AI task 1.0','record_status_required':'internal_ai_test','external_validation':False,'instructions':['Use only supplied scenario facts and exact source text.','Do not invent system behavior, logs, identities, permissions or evidence.','Record C, E and R as 1, 0 or ?. Assess rebuilding separately.','Every textual claim must copy an exact quotation and name its source section.','Return JSON shaped like ai-validation/record-template.json.'],'scenario':s,'source_excerpts':excerpts}
Path(a.output).write_text(json.dumps(task,ensure_ascii=False,indent=2)+'\n')
print(a.output)
