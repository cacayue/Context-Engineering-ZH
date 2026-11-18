---
title: 智能体库（Agents）
source: 70_agents/README.md
module: M11
task: M11-01
chunks: 0
chunks_done: []
status: authored
source_sha256: 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b
---

> 原文：[70_agents/README.md](../../70_agents/README.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)

# 智能体库（Agents）

本目录用于收纳可复用的智能体（agent）定义与配置。上游仓库此目录暂无正文，中文镜像保留位置，供后续补充按领域划分的智能体提示词、工具权限与编排约定。

**本目录应包含什么**

- **智能体定义** — 每个智能体的系统提示词、可用工具与输入输出约定。
- **协作编排** — 多智能体之间的通信协议、任务分解与冲突消解策略。
- **评估与护栏** — 每个智能体的验收判据、失败模式与人工介入点。
- **与模板库的关系** — `20_templates/PROMPTS/` 下的 `.agent.md` 是可直接使用的成品，本目录收纳的是它们的组织方式与组合方案。

**阅读建议**

先读 `20_templates/PROMPTS/README.md` 了解既有成品，再读 `00_COURSE/07_multi_agent_systems/` 理解多智能体协作的原理，最后回到本目录思考如何按自己的领域组织智能体库。术语沿用全书：agent=智能体、orchestration=编排、protocol=协议、guardrail=护栏。
