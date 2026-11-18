---
title: 协议设计（Protocol Design）
source: NOCODE/40_protocol_design/README.md
module: M8
task: M8-04
chunks: 0
chunks_done: []
status: authored
source_sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b
---

> 原文：[NOCODE/40_protocol_design/README.md](../../../NOCODE/40_protocol_design/README.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)

# 协议设计（Protocol Design）

本目录用于收纳自行设计协议的方法论。上游仓库此目录暂无正文，中文镜像保留位置，供后续补充如何从零写出一个可复用的协议壳：明确输入、定义阶段、规定产出、留出校验点。

**本目录应包含什么**

- **协议解剖** — 一个协议由哪些部分组成：意图、输入、阶段、产出、护栏。
- **设计流程** — 从真实任务反推协议的结构，而不是先想结构再找任务。
- **可复用性** — 哪些部分应当参数化，哪些应当固定。
- **校验设计** — 如何为协议设定可检查的完成判据，而不是靠感觉。
- **与成品的对照** — `60_protocols/shells/` 是既有成品，`20_templates/PROMPTS/` 是成品提示词，本目录讲的是它们怎么被造出来的。

**阅读建议**

先精读 `60_protocols/shells/` 里的一两个协议壳，把结构拆开看；再读 `NOCODE/20_practical_protocols/` 感受九类协议的差别；最后回到本目录，试着为你手上的一个真实任务写一份协议。术语沿用全书：protocol=协议、shell=协议壳、guardrail=护栏、schema=模式。
