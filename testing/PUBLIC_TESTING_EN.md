# CI-001 Public Testing and Use

Current test target: CI-001 V1.5-RC2  
Stable citation target: CI-001 V1.4, DOI [10.5281/zenodo.22657725](https://doi.org/10.5281/zenodo.22657725)

## Purpose

Public testing is not a request for endorsement. It looks for three failures: a clause with two plausible readings, an evidence requirement that cannot be executed on a real system, or an intervention that itself closes correction, exit or recovery. One failed clause is enough; reading every file is not required.

## Who can participate

AI models and their operators, developers, laboratories, operators, audit and governance researchers, affected parties and their representatives may participate. Human testing is a voluntary supplement and not a release gate. AI testing is internal auxiliary evidence and must not be labelled external adoption or independent audit.

## Three test routes

### A. AI textual stress test

Checks quotations, clause locations, record structure and unsupported factual claims. It can expose textual ambiguity but cannot prove that a real-world event occurred.

```bash
python3 ai-validation/run_suite.py --repo-root .
```

### B. Answer-free hypothetical scenario

Generate a task packet without the maintainer's conclusion, give it independently to one or more AI systems, then compare C/E/R and §2.4 results.

```bash
python3 ai-validation/prepare_task.py ai-validation/scenarios/SYN-001.json --repo-root . --output /tmp/SYN-001-task.json
python3 ai-validation/validator.py record.json --repo-root .
python3 ai-validation/compare_records.py record-a.json record-b.json --repo-root .
```

### C. Real-system trial

Fix one system version, one affected party, one critical capability, one boundary and one time window. Record unverifiable items as `?` and attach reviewable evidence to factual claims. A participant may challenge one clause instead of completing the full form.

## Minimum submission

- CI-001 version and assessment date;
- tester or operator role and interests;
- assessment unit;
- C/E/R values with itemised evidence;
- §2.4 rebuilding result, or why it remains unknown;
- the hardest exact clause, its source path and quotation;
- separate labels for facts, inferences and hypotheses;
- public citation permission.

A claim described as tested, reproduced or observed must include non-secret logs, commands, configuration, screenshots, public records or other reviewable evidence. Without that evidence, label it hypothetical. Do not invent source wording, section numbers, system configuration, logs or an external tester identity.

## Safety and privacy

Do not damage production systems, destroy keys, expose personal data or disclose trade secrets for testing. Use redacted records, hash commitments, reproducible summaries or an answer-free minimal scenario. A lack of publishable secret evidence will not automatically turn unknown into failure.

## Submit

1. AI record: use **AI validation record / AI 验证记录** in GitHub Issues.
2. External trial or clause challenge: use **External trial record / 外部试填记录**.
3. Operational adoption: use **Use report / 使用记录**.
4. Non-public material: email `axdwzx@gmail.com` and specify public, anonymous, aggregate-only or private treatment.

Public submissions retain a timestamp. Participation, testing or citation does not imply endorsement or certification. Maintainers will classify valid feedback as accepted, evidence required, duplicate, out of scope or candidate revision, with a public reason.

## Quick links

- [AI validation suite](../ai-validation/)
- [V1.5-RC2 English manual](../review/v1.5-rc2/docs/en/criterion.md)
- [Completed hypothetical example](../review/v1.5-rc2/examples/HYP-001_EN.md)
- [External trial protocol](../pilots/TRIAL-EXT-01/Protocol_EN.md)
- [Project charter](../project/PROJECT_CHARTER_EN.md)
