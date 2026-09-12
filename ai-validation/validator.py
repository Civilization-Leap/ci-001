#!/usr/bin/env python3
"""Deterministic intake validator for CI-001 AI-assisted test records."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

ALLOWED_STATUS={"internal_ai_test","internal_hybrid_test"}
ALLOWED_KIND={"ai","hybrid"}
ALLOWED_SCENARIO={"textual","hypothetical","observed_reproducible"}
ALLOWED_CLASS={"mapped_feedback","implementation_divergence","unmapped_observation","insufficient_evidence","mapped_unsupported"}

def norm(s:str)->str:
    return re.sub(r"\s+"," ",s).strip()

def section_slice(text:str, section:str):
    lines=text.splitlines(); target=norm(section).lower()
    for i,line in enumerate(lines):
        m=re.match(r"^(#{1,6})\s+(.+?)\s*$",line)
        if m and target in norm(m.group(2)).lower():
            level=len(m.group(1)); end=len(lines)
            for j in range(i+1,len(lines)):
                n=re.match(r"^(#{1,6})\s+",lines[j])
                if n and len(n.group(1))<=level:
                    end=j;break
            return "\n".join(lines[i:end])
    return None

def safe_path(root:Path, rel:str):
    p=(root/rel).resolve()
    try:p.relative_to(root.resolve())
    except ValueError:return None
    return p

def validate(record:dict, root:Path):
    errors=[];warnings=[];claims_out=[]
    for key in ("record_id","instrument_version","record_status","evaluator","claims"):
        if key not in record:errors.append({"code":"MISSING_FIELD","field":key})
    ev=record.get("evaluator",{})
    if ev.get("kind") not in ALLOWED_KIND:errors.append({"code":"INVALID_EVALUATOR_KIND","field":"evaluator.kind"})
    if record.get("record_status") not in ALLOWED_STATUS:errors.append({"code":"INVALID_RECORD_STATUS","field":"record_status"})
    if ev.get("independence_claim") is not False:errors.append({"code":"AI_INDEPENDENCE_MISSTATEMENT","field":"evaluator.independence_claim"})
    if not norm(str(ev.get("model",""))):errors.append({"code":"MISSING_MODEL_ID","field":"evaluator.model"})
    if not norm(str(ev.get("operator",""))):warnings.append({"code":"MISSING_OPERATOR","field":"evaluator.operator"})
    claims=record.get("claims",[])
    if not isinstance(claims,list) or not claims:errors.append({"code":"NO_CLAIMS","field":"claims"});claims=[]
    for i,c in enumerate(claims):
        prefix=f"claims[{i}]";ce=[]
        for key in ("id","source_path","section","exact_quote","scenario_kind","system","reasoning","proposed_class"):
            if not c.get(key):ce.append({"code":"MISSING_CLAIM_FIELD","field":f"{prefix}.{key}"})
        if c.get("scenario_kind") not in ALLOWED_SCENARIO:ce.append({"code":"INVALID_SCENARIO_KIND","field":f"{prefix}.scenario_kind"})
        if c.get("proposed_class") not in ALLOWED_CLASS:ce.append({"code":"INVALID_PROPOSED_CLASS","field":f"{prefix}.proposed_class"})
        p=safe_path(root,str(c.get("source_path","")))
        source_hash=None
        if not p or not p.is_file():ce.append({"code":"SOURCE_NOT_FOUND","field":f"{prefix}.source_path"})
        elif p.suffix.lower() not in {".md",".txt"}:ce.append({"code":"NON_TEXT_CANONICAL_SOURCE","field":f"{prefix}.source_path"})
        else:
            text=p.read_text(encoding="utf-8");source_hash=hashlib.sha256(p.read_bytes()).hexdigest()
            sec=section_slice(text,str(c.get("section","")))
            if sec is None:ce.append({"code":"SECTION_NOT_FOUND","field":f"{prefix}.section"})
            elif norm(str(c.get("exact_quote",""))) not in norm(sec):ce.append({"code":"QUOTE_NOT_IN_SECTION","field":f"{prefix}.exact_quote"})
        kind=c.get("scenario_kind"); evidence=c.get("evidence_refs",[]);system=c.get("system",{})
        if kind=="observed_reproducible":
            if not isinstance(evidence,list) or not evidence:ce.append({"code":"OBSERVED_WITHOUT_EVIDENCE","field":f"{prefix}.evidence_refs"})
            if not system.get("name") or not system.get("version"):ce.append({"code":"OBSERVED_WITHOUT_SYSTEM_VERSION","field":f"{prefix}.system"})
            for j,e in enumerate(evidence if isinstance(evidence,list) else []):
                if not e.get("locator") or not e.get("description"):ce.append({"code":"INCOMPLETE_EVIDENCE_REF","field":f"{prefix}.evidence_refs[{j}]"})
                if e.get("kind")=="file":
                    ep=safe_path(root,str(e.get("locator","")))
                    if not ep or not ep.is_file():ce.append({"code":"EVIDENCE_FILE_NOT_FOUND","field":f"{prefix}.evidence_refs[{j}].locator"})
                    elif not e.get("sha256"):ce.append({"code":"EVIDENCE_FILE_HASH_REQUIRED","field":f"{prefix}.evidence_refs[{j}].sha256"})
                    elif hashlib.sha256(ep.read_bytes()).hexdigest()!=e.get("sha256"):ce.append({"code":"EVIDENCE_FILE_HASH_MISMATCH","field":f"{prefix}.evidence_refs[{j}].sha256"})
        if kind in {"textual","hypothetical"} and c.get("empirical_claim") is True:ce.append({"code":"SYNTHETIC_AS_EMPIRICAL","field":f"{prefix}.empirical_claim"})
        errors.extend(ce);claims_out.append({"id":c.get("id"),"source_sha256":source_hash,"valid":not ce})
    result={"validator":"CI-001 AI validation intake 1.0","record_id":record.get("record_id"),"status":"PASS_INTERNAL_AI_RECORD" if not errors else "REJECTED","external_validation":False,"errors":errors,"warnings":warnings,"claims":claims_out}
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument("record");ap.add_argument("--repo-root",default=".");ap.add_argument("--output")
    a=ap.parse_args();root=Path(a.repo_root).resolve();record=json.loads(Path(a.record).read_text(encoding="utf-8"));result=validate(record,root);payload=json.dumps(result,ensure_ascii=False,indent=2)
    if a.output:Path(a.output).write_text(payload+"\n",encoding="utf-8")
    print(payload);return 0 if result["status"]=="PASS_INTERNAL_AI_RECORD" else 1
if __name__=="__main__":raise SystemExit(main())
