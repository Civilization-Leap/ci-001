#!/usr/bin/env python3
import argparse,json,subprocess,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--repo-root',default='.')
a=ap.parse_args();root=Path(a.repo_root).resolve();cases=Path(__file__).resolve().parent/'cases';fail=[]
for p in sorted(cases.glob('*.json')):
 data=json.loads(p.read_text());expected=data.pop('_expected_status')
 tmp=cases/(p.stem+'.input.tmp.json');tmp.write_text(json.dumps(data,ensure_ascii=False))
 try:
  q=subprocess.run([sys.executable,str(Path(__file__).with_name('validator.py')),str(tmp),'--repo-root',str(root)],capture_output=True,text=True)
  got=json.loads(q.stdout)['status']
 finally:
  tmp.unlink(missing_ok=True)
 print(f'{p.name}: {got} (expected {expected})')
 if got!=expected:fail.append(p.name)
print('PASS: AI validation regression suite' if not fail else 'FAIL: '+', '.join(fail))
raise SystemExit(bool(fail))
