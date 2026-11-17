---
title: 协议模式（Protocol Schemas）
source: 60_protocols/schemas/README.md
module: M6
task: M6-02
chunks: 0
chunks_done: []
status: authored
source_sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b
---

> 原文：[60_protocols/schemas/README.md](../../../60_protocols/schemas/README.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)

# 协议模式（Protocol Schemas）

本目录收录用于校验的协议模式（schema），是 `60_protocols` 工程资产中「结构定义」的一环。模式把语义场、协议壳、符号残差等抽象概念固化为可机器校验的数据结构，让递归场涌现与吸引子动力学的定义能够被工具链检查与复用。

**目录内容**

- `protocolShell.v1.json` — 协议壳 v1 模式，定义协议壳的结构约束。
- `symbolicResidue.v1.json` — 符号残差 v1 模式，定义符号残差的结构约束。

**阅读建议**

模式文件是 JSON，键名与结构原样保留，其中的自然语言描述按全书术语对照译为中文。建议配合 `shells/` 下的协议壳定义与 `digests/` 下的简化说明一起阅读，先理解协议语义，再查模式的结构约束。
