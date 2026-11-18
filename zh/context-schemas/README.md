---
title: 上下文模式集（Context Schemas）
source: context-schemas/README.md
module: M11
task: M11-01
chunks: 0
chunks_done: []
status: authored
source_sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b
---

> 原文：[context-schemas/README.md](../../context-schemas/README.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)

# 上下文模式集（Context Schemas）

本目录收录上下文工程模式集的历代版本（JSON Schema 形式），记录这一领域从简单结构到复杂场表示的演化轨迹。每份 `context_vX.0.json` 是同一套核心概念在某一阶段的定形，彼此可对照阅读。

**版本谱系**

- `context.json` — 最早的基础模式。
- `context_v2.0.json` 至 `context_v7.0.json` — 逐代扩展：新增字段、细化约束、引入场与吸引子等抽象。
- 上游目录暂无正文说明，中文镜像保留位置，版本对比的解读按需补充。

**阅读建议**

模式文件是 JSON Schema，键名与结构原样保留，其中 `description` 等自然语言字段按全书术语对照译为中文。建议按版本顺序对读，观察每一代新增了什么、舍弃了什么——这本身就是一部微缩的上下文工程思想史。术语沿用全书：context=上下文、schema=模式、field=场、attractor=吸引子、embedding=嵌入。
