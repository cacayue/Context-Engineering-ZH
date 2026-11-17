---
title: 最小上下文（Context）模板
source: 20_templates/PROMPTS/minimal_context.md
module: M6
task: M6-01
chunks: 1
chunks_done: [1]
status: published
source_sha256: c882cd2a15a41a23033029b8650ddda2e0988480a13afb85a8998ac0e5529cd0
---

> 原文：[20_templates/PROMPTS/minimal_context.md](../../../20_templates/PROMPTS/minimal_context.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 最小上下文（Context）模板

## 摘要
用于为 AI 系统创建精简但有效的上下文的模板，重点关注清晰度与必要信息。
## 上下文与应用
当你需要为 AI 系统提供恰好足够的上下文，使其有效执行任务而不受多余信息干扰时，使用此模板。它以结构化格式确立清晰的边界、预期和必要信息。

此模板非常适合：
- 与 AI 系统的首次交互
- 交付物明确、定义清晰的任务
- 需要尽量缩短提示词（Prompt）的情况
- 为更复杂的提示词建立基线

## 模板结构

```
# Task: {{specific_task}}

## Context
- {{key_background_point_1}}
- {{key_background_point_2}}
- {{additional_context_if_needed}}

## Constraints
- {{constraint_1}}
- {{constraint_2}}

## Expected Output
- Format: {{output_format}}
- Length: {{approximate_length}}
- Style: {{style_guidelines}}

## Examples
{{optional_example}}
```

## 参数

- `{{specific_task}}`：清楚描述希望 AI 执行的操作（例如「撰写产品描述」或「分析以下数据」）
- `{{key_background_point_X}}`：正确完成任务所需的必要信息（限制为 2-4 点）
- `{{constraint_X}}`：必须遵守的限制或要求（例如「不要包含价格信息」）
- `{{output_format}}`：输出的结构、格式或文件类型（例如「项目符号列表」或「JSON 对象」）
- `{{approximate_length}}`：输出篇幅的指导（例如「300-400 词」或「5 个要点」）
- `{{style_guidelines}}`：语气、表达方式和风格预期（例如「专业且正式」或「口语化且引人入胜」）
- `{{optional_example}}`：预期输出的样例（首次执行任务时强烈建议提供）

## 示例

### 示例 1：数据分析报告

```
# Task: Analyze the provided sales data and create a summary report

## Context
- Data represents quarterly sales figures for 2022
- Company has 3 product lines: Basic, Premium, and Enterprise
- Previous year showed seasonal trends with Q4 strongest

## Constraints
- Focus on significant changes year-over-year
- Do not speculate beyond what the data shows
- Include at least one actionable recommendation

## Expected Output
- Format: Executive summary followed by bullet points
- Length: Approximately 300-400 words
- Style: Professional, data-focused, actionable

## Examples
Executive Summary:
Q2 2022 shows a 15% increase in overall sales compared to Q2 2021, with the Premium product line showing the strongest growth at 23%. This continues the upward trend observed in Q1...
```

### 示例 2：创意内容创作

```
# Task: Write a product description for our new wireless headphones

## Context
- Target audience: tech-savvy professionals ages 25-40
- Key features: noise cancellation, 30-hour battery life, voice assistant integration
- Main selling points: comfort for all-day wear, premium sound quality

## Constraints
- Keep technical specifications to a minimum
- Don't mention competitors by name
- Focus on benefits, not just features

## Expected Output
- Format: Two paragraphs of flowing text
- Length: 150-200 words
- Style: Modern, enthusiastic but not overly promotional

## Examples
Experience music as it was meant to be heard with our new XDR Wireless Headphones. Designed for professionals who demand the best, these headphones deliver crystal-clear sound while intelligent noise cancellation technology creates your own personal sanctuary of sound—whether you're in a busy office or on a crowded commute...
```

## 变体

### 技术规格模板
用于需要精确指令的技术任务：

```
# Task: {{specific_technical_task}}

## Context
- {{technical_background_point_1}}
- {{technical_background_point_2}}
- {{system_dependencies}}

## Requirements
- {{functional_requirement_1}}
- {{functional_requirement_2}}
- {{performance_requirement}}

## Technical Constraints
- {{technical_limitation_1}}
- {{compatibility_requirement}}

## Expected Output
- Format: {{technical_format}}
- Testing Criteria: {{validation_method}}
- Documentation: {{documentation_requirements}}

## Examples
{{technical_example}}
```

### 创意简报模板
用于写作或设计等创意任务：

```
# Task: {{creative_task}}

## Context
- Audience: {{target_audience}}
- Purpose: {{communication_goal}}
- Brand Voice: {{brand_personality}}

## Creative Direction
- {{inspiration_point_1}}
- {{inspiration_point_2}}
- {{emotional_response_desired}}

## Constraints
- {{brand_guideline_1}}
- {{content_restriction}}
- {{technical_limitation}}

## Expected Output
- Format: {{creative_format}}
- Length/Size: {{dimension_guidelines}}
- Style: {{stylistic_direction}}

## Examples
{{creative_example}}
```

## 最佳实践

- **明确任务**——避免「写点关于耳机的内容」这类模糊指令，改用「为面向年轻专业人士的无线耳机撰写产品描述」
- **只提供必要上下文**——过多信息会分散注意力，使输出相关性降低
- **使用项目符号提高可读性**——将信息拆成要点，比密集段落更易处理
- 尽可能**至少包含一个示例**——示例能显著改善对预期的理解
- **明确列出约束**，而非将其埋在段落中——使约束更难被遗漏
- **对于复杂任务，拆成清晰步骤**或组件——有助于保持重点和结构
- **让上下文匹配输出预期**——确保提供的上下文支持预期的输出格式和风格

## 相关模板

- **少样本（Few-Shot）学习模板**：用于需要通过多个示例教导 AI 的情况
- **思维链（Chain of Thought）模板**：用于需要逐步推理的任务
- **基于角色的上下文模板**：用于采用特定角色或视角可以改善结果的情况
