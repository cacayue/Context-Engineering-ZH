---
title: 理解模板
source: cognitive-tools/cognitive-templates/understanding.md
module: M9
task: M9-02
chunks: 1
chunks_done: [1]
status: published
source_sha256: 196ebdd3ae38f1ec96885127c2bbce86d5ebdbbf78988776bbdefc3c1b1418fc
---

> 原文：[cognitive-tools/cognitive-templates/understanding.md](../../../cognitive-tools/cognitive-templates/understanding.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 理解模板

> 「智慧始于对术语的定义。」—— 苏格拉底

## 概述

理解模板帮助语言模型在尝试解决问题或生成内容之前理解和分析信息。这些模板确保模型正确解读任务、上下文（context）和要求，从而为有效推理奠定基础。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  UNDERSTANDING PROCESS                                       │
│                                                              │
│  Input → Analyze → Structure → Clarify → Ready for Reasoning │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

## 基础模板

### 1. 问题分析

最基础的理解模板，帮助将问题拆解为核心组成部分。

```markdown
# Question Analysis Template

Task: Analyze and break down the following question before attempting to answer it.

Question: {{question}}

Please provide:
1. **Question Type**: What kind of question is this? (e.g., factual, conceptual, analytical)
2. **Core Task**: What specific action or thinking is required?
3. **Key Components**: What are the main elements that need to be addressed?
4. **Implicit Assumptions**: What unstated assumptions might be relevant?
5. **Knowledge Domains**: What fields of knowledge are relevant?
6. **Constraints**: Are there any explicit or implicit constraints?
7. **Restatement**: Restate the question in your own words for clarity.

Once you've completed this analysis, you'll be better prepared to address the question effectively.
```

**词元（token）数**：约 120 token（仅模板）

**使用示例**：
- 用于理解要求至关重要的复杂问题
- 用于需要精确解读的情况
- 用于处理多步骤问题之前

### 2. 信息提取

用于从文本中提取结构化信息。

```markdown
# Information Extraction Template

Task: Extract and organize the key information from the following text.

Text: {{text}}

Please extract:
1. **Main Topic**: What is the central subject?
2. **Key Facts**: List the most important factual statements.
3. **Entities**: Identify people, organizations, locations, dates, etc.
4. **Relationships**: How are these entities related to each other?
5. **Numerical Data**: Extract any numbers, statistics, or measurements.
6. **Claims**: What assertions or arguments are made?
7. **Evidence**: What support is provided for these claims?

Organize this information in a clear, structured format.
```

**词元数**：约 110 token（仅模板）

**使用示例**：
- 用于处理研究论文或文章
- 用于总结复杂文档
- 用于综合多个来源的信息之前

### 3. 问题分解

用于将复杂问题拆分为可解决的部分。

```markdown
# Problem Decomposition Template

Task: Decompose the following problem into smaller, manageable components.

Problem: {{problem}}

Please provide:
1. **Problem Type**: What category of problem is this?
2. **Goal State**: What does a successful solution look like?
3. **Given Information**: What information is explicitly provided?
4. **Unknown Variables**: What needs to be determined?
5. **Constraints**: What limitations or conditions must be satisfied?
6. **Sub-Problems**: Break down the main problem into smaller parts.
7. **Dependencies**: How do these sub-problems relate to each other?
8. **Solution Approach**: Suggest a high-level strategy for solving the problem.

This decomposition will provide a structured approach to solving the problem.
```

**词元数**：约 120 token（仅模板）

**使用示例**：
- 用于数学或逻辑问题
- 用于面对多步骤推理任务时
- 用于开展复杂分析之前

## 高级模板

### 4. 概念映射

用于理解某个领域内概念之间的关系。

```markdown
# Conceptual Mapping Template

Task: Create a conceptual map of the ideas and relationships in the following text.

Text: {{text}}

Please provide:
1. **Core Concepts**: Identify the central ideas or concepts.
2. **Concept Definitions**: Briefly define each concept.
3. **Hierarchical Relationships**: Which concepts are subcategories of others?
4. **Causal Relationships**: Which concepts influence or cause others?
5. **Contrasting Concepts**: Which concepts stand in opposition to each other?
6. **Complementary Concepts**: Which concepts support or enhance each other?
7. **Missing Concepts**: Are there any implied but unstated concepts?

Represent these relationships in a structured format that shows how the concepts interconnect.
```

**词元数**：约 120 token（仅模板）

**使用示例**：
- 用于理论性或抽象内容
- 用于分析复杂系统
- 用于综合不同信息之前

### 5. 多视角分析

用于理解关于某个主题的不同观点。

```markdown
# Multi-Perspective Analysis Template

Task: Analyze the following topic from multiple perspectives.

Topic: {{topic}}

Please provide:
1. **Perspective Identification**: What major viewpoints exist on this topic?
2. **Core Arguments**: What are the main arguments from each perspective?
3. **Evidence Base**: What evidence supports each perspective?
4. **Underlying Values**: What values or assumptions underlie each perspective?
5. **Areas of Agreement**: Where do the perspectives converge?
6. **Key Disagreements**: What are the fundamental points of contention?
7. **Synthesis Possibilities**: How might these perspectives be integrated?

This analysis will provide a balanced understanding of the different ways to view this topic.
```

**词元数**：约 120 token（仅模板）

**使用示例**：
- 用于有争议或复杂的主题
- 用于需要均衡理解的情况
- 用于形成细致立场之前

### 6. 需求分析

用于清晰理解任务要求。

```markdown
# Requirement Analysis Template

Task: Analyze the requirements for the following task or project.

Task Description: {{task_description}}

Please provide:
1. **Primary Objective**: What is the main goal?
2. **Deliverables**: What specific outputs are required?
3. **Quality Criteria**: How will success be measured?
4. **Constraints**: What limitations must be worked within?
5. **Dependencies**: What external factors impact this task?
6. **Stakeholders**: Who is involved or affected?
7. **Priorities**: Which aspects are most important?
8. **Ambiguities**: What aspects need clarification?

This analysis will ensure all requirements are properly understood before proceeding.
```

**词元数**：约 120 token（仅模板）

**使用示例**：
- 用于项目规划
- 用于需要创建特定输出的任务
- 用于开始任何复杂任务之前

## 实现模式

下面是实现问题分析模板的简单 Python 函数：

```python
def understand_question(question):
    """
    Create a prompt that analyzes and breaks down a question.
    
    Args:
        question (str): The question to analyze
        
    Returns:
        str: A formatted prompt for question analysis
    """
    return f"""
Task: Analyze and break down the following question before attempting to answer it.

Question: {question}

Please provide:
1. **Question Type**: What kind of question is this? (e.g., factual, conceptual, analytical)
2. **Core Task**: What specific action or thinking is required?
3. **Key Components**: What are the main elements that need to be addressed?
4. **Implicit Assumptions**: What unstated assumptions might be relevant?
5. **Knowledge Domains**: What fields of knowledge are relevant?
6. **Constraints**: Are there any explicit or implicit constraints?
7. **Restatement**: Restate the question in your own words for clarity.

Once you've completed this analysis, you'll be better prepared to address the question effectively.
"""
```

## 衡量与优化

使用理解模板时，可通过以下指标衡量效果：

1. **准确性**：理解结果是否正确识别了所有关键要素？
2. **全面性**：是否覆盖了输入的所有重要方面？
3. **清晰度**：结构化理解是否清晰、无歧义？
4. **实用性**：理解结果是否改善了后续推理？

可通过以下方式优化模板：
- 删除不能改善理解的不必要部分
- 添加特定领域所需的具体组成部分
- 根据输入的复杂程度调整细节层次

## 与其他工具结合

理解模板与其他认知工具（cognitive tool）结合使用时效果最佳：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

例如，先使用问题分析模板，再将结构化理解传给问题求解模板，最后用验证模板核验解答。

## 后续步骤

- 探索 [reasoning.md](./reasoning.md)，了解在理解基础上进行推理的模板
- 参阅 [composition.md](./composition.md)，了解组合多个模板的方法
- 查看 [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md)，了解使用这些模板的程序化方法
