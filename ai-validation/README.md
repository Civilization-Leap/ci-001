# CI-001 AI-first validation / AI优先验证

This layer lets AI do the work it can verify while preventing simulated material from being described as external evidence. It does not modify the CI-001 criterion and does not make a human trial a release gate.

本层让AI承担能够复算的工作，同时阻止把模拟材料写成外部证据。它不修改CI-001判据，也不把真人测试设为发布门槛。

## What it validates / 核验内容

- the cited source file exists;
- the named Markdown section exists;
- the quotation occurs inside that section after whitespace normalization;
- an AI or hybrid record does not claim independent external validation;
- hypothetical and textual tests do not claim empirical observation;
- an observed reproducible claim supplies a system version and evidence references;
- local evidence files exist and match their declared SHA-256.

对应检查：来源文件、章节和引文真实存在；AI记录不冒充外部独立验证；假设推演不冒充实测；实测主张必须给出系统版本与证据；本地证据文件必须与声明哈希一致。

Passing this intake means only that the record is correctly attributed and minimally evidenced. It does not mean that its reasoning is correct, that CI-001 is valid, or that an audit has passed.

通过入口校验只表示引用归属与最低证据条件成立，不证明推理正确、判据有效或治理审计通过。

## Record classes / 记录类型

| `scenario_kind` | Meaning / 含义 |
| --- | --- |
| `textual` | Logic or wording analysis based only on supplied text / 仅基于原文的逻辑或措辞分析 |
| `hypothetical` | Declared synthetic stress case; no empirical claim / 明示假设压力场景，不声称实测 |
| `observed_reproducible` | A real observation with system version and evidence references / 带系统版本与证据引用的现实观察 |

All AI results use `internal_ai_test` or `internal_hybrid_test`. Human responses, if they arise, remain useful but are not required by this suite.

所有AI结果标为`internal_ai_test`或`internal_hybrid_test`。真人反馈若自然出现仍可使用，但本套件不以其为前提。

## Run / 运行

```bash
python3 ai-validation/validator.py ai-validation/record-template.json --repo-root .
python3 ai-validation/run_suite.py --repo-root .
```

The unedited template deliberately fails because its placeholder quotation is not source text. Copy a real quotation before use. The regression suite contains one valid record and three negative controls: fabricated quotation, false independence, and empirical claim without evidence.

未编辑模板会因占位引文并非原文而失败，使用前须复制真实原文。回归套件包含一个有效记录和三个反向控制：伪引文、虚假独立性、无证据实测主张。

## Scope boundary / 能力边界

The validator can establish textual attribution and specified evidence-file integrity. It cannot determine whether a hypothetical architecture exists, whether a URL proves a claim, whether an assessor reasoned correctly, or whether a real party retains C/E/R. Those remain explicit unknowns until supported by evidence.

校验器能够确认文本归属及指定证据文件的完整性，不能证明假设架构真实存在、链接足以支持主张、推理必然正确或现实主体确实保有C/E/R；证据不足时继续保留未知。
