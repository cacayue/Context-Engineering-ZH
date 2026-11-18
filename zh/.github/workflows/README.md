---
title: 工作流（CI Workflows）
source: .github/workflows/README.md
module: M10
task: M10-04
chunks: 0
chunks_done: []
status: authored
source_sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b
---

> 原文：[.github/workflows/README.md](../../../.github/workflows/README.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)

# 工作流（CI Workflows）

本目录收录仓库的持续集成工作流定义。这些工作流在每次推送时自动运行，检查译文的结构完整性、术语一致性、代码围栏与双语锚点是否达标，是保证整部中译本质量的自动化护栏。

**章节导览**

- **`ci.yml`** — 主持续集成流水线。
- **`eval.yml`** — 评估相关检查。
- **`protocol_tests.yml`** — 协议壳定义的结构测试。
- **`zh_checks.yml`** — 中译本专项校验（九项门禁 G1–G9）。

**阅读建议**

工作流文件是 YAML 配置，键名与结构原样保留，其中自然语言注释按全书术语对照译为中文。建议配合仓库根目录的质量工具链（`zh/tools/`）一起阅读，理解每一项门禁对应的检查逻辑。
