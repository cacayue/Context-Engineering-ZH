---
title: 第 8 模块：提示词编程——用文字编写代码
source: masterclass_content/08_prompt_programming_module.md
module: M1
task: M1-04
chunks: 1
chunks_done:
  - 1
status: published
source_sha256: c0bc6f110460e664e375a16492807b8405cb8b5ca96b599c46c0e1e43c045452
---

> 原文：[masterclass_content/08_prompt_programming_module.md](../../masterclass_content/08_prompt_programming_module.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)

# 第 8 模块：提示词编程——用文字编写代码

### 模块摘要

提示词编程（prompt programming）代表了上下文工程的巅峰，在这里自然语言与计算机代码之间的界限变得模糊。这一学科涉及将软件开发的结构化、逻辑范式——如函数式、过程式和面向对象编程——应用于提示词设计这一工艺中。你不再编写独立的提示词，而是开始设计可复用的「认知函数」，将它们组合成复杂的工作流，并使用逻辑来引导 AI 的推理过程。

在本模块中，你将学会把提示词不仅视为简单的指令，而是视为用英语编写的程序。我们将探索如何创建模块化、可复用的提示词函数，将它们串联在一起以解决多步骤问题，甚至使用条件逻辑来构建能够调整自身策略的提示词。精通提示词编程是从提示词使用者转变为资深 AI 系统架构师的最后一步。

### 关键要点

*   **像对待函数一样对待提示词：** 核心理念是将认知任务定义为一个具有清晰输入和可预测输出的函数（例如 `function summarize(text, style, length)`）。这使你的提示词模块化且可复用。
*   **组合，而非堆砌：** 通过组合简单函数来解决复杂问题。`research(topic)` 函数的输出可以直接管道传输到 `analyze(research_results)` 函数中，后者进而供给 `synthesize(analysis)` 函数。
*   **编写过程式脚本：** 对于任何非同寻常的任务，明确定义 AI 应遵循的 `steps` 序列。这是实现供 AI 运行的「程序」的最直接方式。
*   **以对象思维思考：** 当你的提示词始终围绕单个实体（如分析文档）展开时，像「对象」一样构建你的思维。定义其 `properties`（例如文本、作者）以及你可以在其上调用的 `methods`（例如 `.summarize()`、`.extract_entities()`）。
*   **使用条件逻辑：** 通过包含 `if/then` 逻辑来构建更智能的提示词。例如：「如果用户的问题具有技术性，采用专家人设。如果问题很简单，采用适合初学者的语调。」

> **专家提示：** 创建一个**「工具构建器」元提示词**。这是一个唯一职责是为你生成*其他*高质量专门提示词的提示词。例如，你可以问它：`"You are an expert prompt engineer. Create a detailed prompt template for a 'Fact-Checking' agent. The template should include steps for identifying claims, finding primary sources, and flagging contradictions."` 通过这样做，你可以利用 AI 构建属于自己的强大、可复用的认知工具库，大幅加快你的工作流程。

### 动手练习：小挑战

你的目标是通过创建一个将两个认知任务串联在一起的提示词，来实践「函数组合」。

**任务：**
你有一段文本，需要首先提取关键要点，然后将这些要点格式化为一封专业邮件。

**你的「认知函数」库：**
1.  **`extract_key_points(text)`：** 接收文本并输出最重要的要点列表的提示词。
2.  **`format_as_email(subject, recipient, points)`：** 接收主题、收件人和要点列表，并将其格式化为整洁邮件的提示词。

**你的挑战：**
给定以下文本：
`"The quarterly meeting is confirmed for next Tuesday at 10 AM in Conference Room 3. All department heads are required to attend. Please prepare a 5-minute summary of your team's progress. The main agenda items will be the Q3 budget review and the Q4 product roadmap. A follow-up email with the full agenda will be sent by EOD Friday."`

编写一个单独的「组合」提示词，指示 AI 首先执行 `extract_key_points` 任务，然后立即使用该输出执行 `format_as_email` 任务，将摘要发送至 'all-heads@company.com'，主题为 "Key Info for Upcoming Quarterly Meeting"。
