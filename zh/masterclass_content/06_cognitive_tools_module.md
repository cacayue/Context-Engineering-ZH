---
title: 第 6 模块：认知工具——工程化设计 AI 的思考过程
source: masterclass_content/06_cognitive_tools_module.md
module: M1
task: M1-04
chunks: 1
chunks_done:
  - 1
status: published
source_sha256: ac641f52907b9fb35248e739dd551a4421cf2988792fb77c5ff66147d5a360ba
---

> 原文：[masterclass_content/06_cognitive_tools_module.md](../../masterclass_content/06_cognitive_tools_module.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)

# 第 6 模块：认知工具——工程化设计 AI 的思考过程

### 模块摘要

本模块标志着我们方法的重大转变。我们超越了单纯提供上下文，转向主动工程化设计 AI 本身的推理过程。「认知工具（Cognitive Tools）」是先进的、结构化的方法，它们模仿人类的心智捷径（启发式），使 AI 的思考更稳健、更可复用且更透明。

我们将探索三项核心工具。首先是**提示词程序（Prompt Programs）**（或协议壳），它们将我们的提示词从一次性命令转变为可复用、可编程的模板。其次是**上下文模式（Context Schemas）**，它们规范我们向 AI 提供的信息结构，就像数据库模式组织数据一样。最后是**递归提示（Recursive Prompting）**，这是一种强大的技术，它创建反馈回路，迫使 AI 反思并改进自身的工作。通过精通这些工具，你将从一名提示词撰写者演变成为一名真正的「认知架构师」，设计 AI 用以思考的系统本身。

### 关键要点

*   **为你的提示词编程：** 「提示词程序」是一个具有明确参数、清晰过程和指定输出格式的可复用提示词模板。它将提示从一门艺术转变为一门工程学科。
*   **结构不可或缺：** 「上下文模式」（例如使用 JSON 或 YAML）定义了上下文的形态，使其可预测且更易于 AI 理解。这减少了歧义并提高了可靠性。
*   **强制自我纠错：** 「递归提示」是一个循环，在此过程中你要求 AI 批判自己先前的答案。这种简单的反馈机制可以显著提高复杂输出的质量和准确性。
*   **协议壳带来清晰：** 「协议壳（Protocol Shell）」是一种在无需代码的情况下实现提示词程序的简单文本化方法，它使用清晰的 `/protocol.name{}` 语法来定义意图、输入、过程和输出。
*   **成为认知架构师：** 这些工具的目标是将你的工作从编写单独的提示词提升为 AI 设计可扩展、可复用且透明的推理系统。

> **专家提示：** 回顾你最复杂、最成功的一个提示词——那个你最引以为傲的提示词。分析它并尝试将其逆向工程为一个「提示词程序」。形式化核心 `task`，识别你引导 AI 经历的隐式 `process` 步骤，并定义你期望的 `output format`。这种解构自身直觉成功的行为，是让你的提示技能更系统化、更具可扩展性的一大步。

### 动手练习：小挑战

你的目标是将「提示词程序」的概念应用于标准的临时提示词中，使其更具结构且更易复用。

**任务：**
你拥有以下简单的「原子」提示词：
*「用两段话向一个 10 岁的孩子解释光合作用的概念。」*（`"Explain the concept of photosynthesis to a 10-year-old in two paragraphs."`）

**你的挑战：**
使用下面的模板将这个临时提示词重写为结构化的**提示词程序**。你的程序应该具有针对 `concept`、`target_audience` 和 `length` 的清晰参数。

**要填写的模板：**
```
program ExplainConcept(concept, target_audience, length) {
  // Define the task
  task = `...`;

  // Define the process
  process = ```
    1. ...
    2. ...
    3. ...
  ```;

  // Define the output format
  format = `...`;

  // Construct the complete prompt
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\nConcept to explain: ${concept}`;
}
```
这个练习将让你获得切身实践，把提示词不看作单一命令，而是看作可复用、结构化的组件。
