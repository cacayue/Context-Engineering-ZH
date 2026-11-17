---
title: 第 3 模块：上下文的分子——用示例教学
source: masterclass_content/03_molecules_of_context_module.md
module: M1
task: M1-04
chunks: 1
chunks_done:
  - 1
status: published
source_sha256: 58843efe1beee72cc747fbfff3adec7da043374c45080628207871010e58e857
---

> 原文：[masterclass_content/03_molecules_of_context_module.md](../../masterclass_content/03_molecules_of_context_module.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)

# 第 3 模块：上下文的分子——用示例教学

### 模块摘要

如果说「原子」提示词是单条命令，那么「分子」提示词就是完整的配方。一个分子将核心**指令（Instruction）**与高质量的**示例（Examples）**相结合，教导 AI 如何执行任务，而不仅仅是指示它去做。这种方法被称为**少样本学习（few-shot learning）**，是在无需复杂编程的情况下提高 AI 准确性与可靠性的最有效方法之一。

通过向 AI 提供一些所需输入输出模式的示例，你实际上给了它一个遵循的蓝图。这极大地减少了歧义和不一致，特别是对于分类、结构化数据提取或遵循特定格式等任务。成功的关键不仅在于提供示例，还在于挑选*合适*的示例并对其进行有效构建。从原子走向分子，是你从单纯*使用* AI 到*工程化设计*其上下文的第一个重大飞跃。

### 关键要点

*   **超越单纯指令：** 分子提示词不仅是一条命令，更是一堂课。基本公式为 `INSTRUCTION + EXAMPLES + NEW INPUT`。
*   **结构决定一切：** 你如何编排示例格式至关重要。简单的 `Input: / Output:` 对在许多任务中表现良好，但在示例中使用 `Chain-of-Thought` 结构可以教导模型更复杂的推理。
*   **明智精选示例：** 示例的质量至关重要。包含多样化的案例，特别是棘手的边界案例，为 AI 明确界定任务的边界。
*   **警惕收益递减：** 最大的性能跃升往往来自第一个示例。每一个额外的示例带来的收益越来越少，但仍会消耗词元（token）。对于大多数任务，找到 2-5 个示例的「平衡点」。
*   **动态选择是高级实践：** 最复杂的系统不会使用固定的示例集。它们会根据用户的具体查询，从大型数据库中动态检索最相关的示例。

> **专家提示：** 你可以通过使用「思维链（Chain of Thought）」示例来大幅增强简单提示词的效果，即使你不需要最终输出展示其推理过程。通过向 AI 展示包含逐步推理的示例，你可以「引导」它在处理新输入时进行更具逻辑性和更细致的思考。这可以在不让最终响应杂乱无章的情况下，显著提高棘手任务的准确性。

### 动手练习：小挑战

你的目标是直接衡量少样本学习对情感分类任务的影响。

**任务：**
你需要将客户评论的情感分类为「Positive」、「Negative」或「Neutral」。以下是需要分类的新评论：
*「结账过程很顺畅，但物品晚到了一周。」*（`"The checkout process was smooth, but the item arrived a week late."`）

**你的挑战：**
创建三个不同的提示词来分类这条评论，从零样本开始，逐步增加更多示例。

1.  **提示词 A（零样本）：** 使用仅包含指令的简单「原子」提示词。
2.  **提示词 B（单样本）：** 在提示词中添加一个「Positive」评论的清晰示例。
3.  **提示词 C（少样本）：** 在要求 AI 分类新评论之前，向提示词添加三个不同类别的示例（一个 Positive、一个 Negative、一个 Neutral）。

**提示词 C 的示例结构：**
```
Classify the sentiment of the following reviews as Positive, Negative, or Neutral.

Review: 'The product is fantastic, I love it!'
Sentiment: Positive

Review: 'The item broke after one use.'
Sentiment: Negative

Review: 'The packaging was standard.'
Sentiment: Neutral

Review: 'The checkout process was smooth, but the item arrived a week late.'
Sentiment:
```

观察随着你在提示词 C 中提供更多上下文，AI 的回答如何从「Negative」（在提示词 A 中）转变为更细腻且正确的「Neutral」。这展示了分子提示的力量。
