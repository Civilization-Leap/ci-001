#!/usr/bin/env python3
import argparse,hashlib,json,re
from pathlib import Path

def sections(text):
 lines=text.splitlines();out=[]
 for i,line in enumerate(lines):
  m=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
  if not m:continue
  level=len(m.group(1));end=len(lines)
  for j in range(i+1,len(lines)):
   n=re.match(r'^(#{1,6})\s+',lines[j])
   if n and len(n.group(1))<=level:end=j;break
  out.append({'heading':m.group(2),'level':level,'text':'\n'.join(lines[i:end])})
 return out
ap=argparse.ArgumentParser();ap.add_argument('--repo-root',default='.');ap.add_argument('--output');a=ap.parse_args();root=Path(a.repo_root).resolve()
paths=['review/v1.5-rc2/docs/zh/criterion.md','review/v1.5-rc2/docs/en/criterion.md']
result={'corpus':'CI-001 V1.5-RC2 canonical Markdown','documents':[]}
for rel in paths:
 p=root/rel;b=p.read_bytes();result['documents'].append({'path':rel,'sha256':hashlib.sha256(b).hexdigest(),'sections':sections(b.decode())})
payload=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
if a.output:Path(a.output).write_text(payload)
else:print(payload,end='')
