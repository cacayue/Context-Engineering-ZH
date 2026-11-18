---
title: 推理模板
source: cognitive-tools/cognitive-templates/reasoning.md
module: M9
task: M9-02
chunks: 1
chunks_done: [1]
status: published
source_sha256: 387b32aa01bb1380965b9a293b3241e5b52a6635bbeec4ea9900d6503a7b1494
---

> 原文：[cognitive-tools/cognitive-templates/reasoning.md](../../../cognitive-tools/cognitive-templates/reasoning.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 推理模板

> 「逻辑是思想的解剖学。」—— 约翰·洛克

## 概述

推理模板引导语言模型通过结构化思考过程解决问题、产生洞见或作出决策。这些模板以理解模板为基础，为处理信息和得出结论提供系统化方法。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  REASONING PROCESS                                           │
│                                                              │
│  Input → Structure → Apply Logic → Step-by-Step → Conclusion │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

## 基础模板

### 1. 逐步推理

将复杂推理拆解为可管理步骤的基础模板。

```markdown
# Step-by-Step Reasoning Template

Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {{problem}}

Please follow this process:
1. **Understand**: Restate the problem and identify what you need to find.
2. **Plan**: Outline your approach to solving the problem.
3. **Execute**: Work through each step of your plan in detail.
   - Step 1: [Description of the first step]
   - Step 2: [Description of the second step]
   - Step 3: [Continue with additional steps as needed]
4. **Verify**: Check your solution against the original problem.
5. **Conclude**: State your final answer or conclusion clearly.

Show all your work and explain your reasoning at each step.
```

**词元（token）数**：约 130 token（仅模板）

**使用示例**：
- 用于数学问题求解
- 用于梳理复杂逻辑论证
- 用于任何需要透明推理的任务

### 2. 比较与对照

用于评估相似点与差异的分析性推理。

```markdown
# Compare and Contrast Template

Task: Analyze the similarities and differences between the following items.

Items to Compare: {{item_a}} and {{item_b}}

Please follow this structured approach:
1. **Background**: Briefly introduce both items and their context.
2. **Criteria Selection**: Identify the key dimensions for comparison.
3. **Systematic Comparison**:
   - Dimension 1: [Explain how both items relate to this dimension]
   - Dimension 2: [Explain how both items relate to this dimension]
   - Dimension 3: [Continue with additional dimensions as needed]
4. **Key Similarities**: Explicitly list the most important similarities.
5. **Key Differences**: Explicitly list the most important differences.
6. **Synthesis**: Explain what these similarities and differences reveal.
7. **Conclusion**: Summarize the most significant insights from this comparison.
```

**词元数**：约 140 token（仅模板）

**使用示例**：
- 用于比较理论、产品或方法
- 用于分析相互竞争的解决方案
- 用于评估其他解释

### 3. 因果分析

用于推理因果关系。

```markdown
# Causal Analysis Template

Task: Analyze the causes and effects related to the following situation or phenomenon.

Situation: {{situation}}

Please follow this structured approach:
1. **Describe the Phenomenon**: Clearly state what needs to be explained.
2. **Identify Potential Causes**:
   - Immediate Causes: [Direct factors that led to the situation]
   - Underlying Causes: [Deeper factors that created conditions for the situation]
   - Contributory Factors: [Elements that amplified or enabled the causes]
3. **Evaluate Each Cause**:
   - Evidence: [What evidence supports this as a cause?]
   - Significance: [How important was this cause?]
   - Mechanism: [How did this cause lead to the effect?]
4. **Analyze Effects**:
   - Immediate Effects: [Direct consequences]
   - Long-term Effects: [Ongoing or future consequences]
   - Secondary Effects: [Indirect consequences]
5. **Examine Interactions**: How do these causes and effects interact with each other?
6. **Conclusion**: Summarize the most significant causal relationships.
```

**词元数**：约 160 token（仅模板）

**使用示例**：
- 用于历史分析
- 用于研究复杂系统
- 用于理解社会或经济现象

## 高级模板

### 4. 假设检验

用于依据证据系统地评估假设。

```markdown
# Hypothesis Testing Template

Task: Systematically evaluate the following hypothesis based on available evidence.

Hypothesis: {{hypothesis}}

Evidence: {{evidence}}

Please follow this structured approach:
1. **Clarify the Hypothesis**: Restate the hypothesis in precise terms.
2. **Identify Testable Predictions**: What should be true if the hypothesis is correct?
3. **Evaluate Evidence**:
   - Supporting Evidence: [Evidence that confirms predictions]
     - Strength: [How strongly does this evidence support the hypothesis?]
     - Reliability: [How reliable is this evidence?]
   - Contradictory Evidence: [Evidence that contradicts predictions]
     - Strength: [How strongly does this evidence oppose the hypothesis?]
     - Reliability: [How reliable is this evidence?]
   - Missing Evidence: [Evidence that should exist but isn't present]
4. **Consider Alternative Hypotheses**: What other explanations could account for the evidence?
5. **Weigh Comparative Explanatory Power**: How well does the hypothesis explain the evidence compared to alternatives?
6. **Conclusion**: Assess the overall credibility of the hypothesis.
7. **Confidence Level**: Indicate your level of confidence in this assessment.
```

**词元数**：约 180 token（仅模板）

**使用示例**：
- 用于科学推理
- 用于评估理论或主张
- 用于循证决策

### 5. 决策矩阵

用于基于多个标准的结构化决策。

```markdown
# Decision Matrix Template

Task: Evaluate options against criteria to make a structured decision.

Decision Context: {{decision_context}}
Options: {{options}}
Criteria: {{criteria}}

Please follow this structured approach:
1. **Define the Decision**: Clearly state what decision needs to be made.
2. **Establish Criteria Weights**:
   - Criterion 1: [Importance weight (1-10)]
   - Criterion 2: [Importance weight (1-10)]
   - [Continue for all criteria]
3. **Evaluate Each Option**:
   Create a matrix with options as rows and criteria as columns.
   
   | Option | Criterion 1 | Criterion 2 | ... | Total |
   |--------|-------------|-------------|-----|-------|
   | Option A | [Score] | [Score] | ... | [Sum] |
   | Option B | [Score] | [Score] | ... | [Sum] |
   
   For each cell, provide:
   - Score: [Rating (1-10)]
   - Justification: [Brief explanation]
   
4. **Calculate Weighted Scores**: Multiply each score by the criterion weight.
5. **Rank Options**: Order options based on their total weighted scores.
6. **Sensitivity Analysis**: How would the ranking change if weights were adjusted?
7. **Recommendation**: State the recommended option with justification.
```

**词元数**：约 180 token（仅模板）

**使用示例**：
- 用于在备选方案之间作出选择
- 用于权衡多个因素
- 用于透明的决策过程

### 6. 论证构建

用于构建结构清晰的论证。

```markdown
# Argument Construction Template

Task: Construct a well-reasoned argument for the following position.

Position: {{position}}

Please follow this structured approach:
1. **Thesis Statement**: Clearly articulate the main claim or position.
2. **Define Key Terms**: Clarify any ambiguous or technical terms.
3. **Establish Premises**:
   - Premise 1: [State first supporting claim]
     - Evidence: [Support for this premise]
     - Reasoning: [How this evidence supports the premise]
   - Premise 2: [State second supporting claim]
     - Evidence: [Support for this premise]
     - Reasoning: [How this evidence supports the premise]
   - [Continue with additional premises as needed]
4. **Logical Structure**: Explain how these premises lead to the conclusion.
5. **Address Counterarguments**:
   - Counterargument 1: [Potential objection]
     - Response: [Rebuttal or accommodation]
   - Counterargument 2: [Potential objection]
     - Response: [Rebuttal or accommodation]
6. **Conclusion**: Restate the thesis and summarize the supporting arguments.
```

**词元数**：约 170 token（仅模板）

**使用示例**：
- 用于说服性写作
- 用于撰写立场文件
- 用于构建逻辑论证

## 实现模式

下面是实现逐步推理模板的简单 Python 函数：

```python
def step_by_step_reasoning(problem, steps=None):
    """
    Create a prompt that guides through step-by-step reasoning.
    
    Args:
        problem (str): The problem to solve
        steps (list, optional): Custom steps for the reasoning process
        
    Returns:
        str: A formatted prompt for step-by-step reasoning
    """
    if steps is None:
        steps = [
            "Understand: Restate the problem and identify what you need to find.",
            "Plan: Outline your approach to solving the problem.",
            "Execute: Work through each step of your plan in detail.",
            "Verify: Check your solution against the original problem.",
            "Conclude: State your final answer or conclusion clearly."
        ]
    
    steps_text = "\n".join([f"{i+1}. **{step.split(':', 1)[0]}**:{step.split(':', 1)[1]}" 
                           for i, step in enumerate(steps)])
    
    return f"""
Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {problem}

Please follow this process:
{steps_text}

Show all your work and explain your reasoning at each step.
"""
```

## 衡量与优化

使用推理模板时，可通过以下指标衡量效果：

1. **逻辑有效性**：前提是否充分支持结论？
2. **完整性**：推理是否涉及问题的所有方面？
3. **透明度**：每一步是否得到清晰解释和论证？
4. **效率**：推理是否沿直接路径抵达解答？
5. **正确性**：推理是否得出了正确答案或结论？

可通过以下方式优化模板：
- 根据问题复杂度调整细节层次
- 为专业领域添加领域特定的推理步骤
- 为特定类型的问题定制评估标准

## 与其他工具结合

推理模板作为完整认知工作流的一部分时效果最佳：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

例如，先用理解模板分析问题，再用推理模板求解，最后用验证模板检查解答。

## 高级推理模式

对于复杂问题，可考虑以下高级模式：

### 分而治之

将问题拆分为独立子问题，分别求解，再合并结果。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Main Problem                                                 │
│       │                                                       │
│       ├────────────────┬────────────────┬────────────────┐    │
│       │                │                │                │    │
│       ▼                ▼                ▼                ▼    │
│  Sub-Problem 1    Sub-Problem 2    Sub-Problem 3    Sub-Problem 4 │
│       │                │                │                │    │
│       ├────────────────┼────────────────┼────────────────┘    │
│       │                │                │                     │
│       ▼                ▼                ▼                     │
│  Combine Solutions and Integrate Results                      │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

### 迭代改进

从简单解答开始，再通过迭代加以改进。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Initial Solution                                             │
│       │                                                       │
│       ▼                                                       │
│  Identify Weaknesses                                          │
│       │                                                       │
│       ▼                                                       │
│  Improve Solution           ◄─────────────┐                   │
│       │                                    │                   │
│       ▼                                    │                   │
│  Evaluate Improvement                      │                   │
│       │                                    │                   │
│       └────────────────────────────────────┘                   │
│       │                                                        │
│       ▼                                                        │
│  Final Solution (when satisfactory)                            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

### 类比推理

将已知领域的推理模式应用于新问题。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Target Problem                                               │
│       │                                                       │
│       ▼                                                       │
│  Identify Similar Solved Problem                              │
│       │                                                       │
│       ▼                                                       │
│  Map Elements from Solved Problem to Target Problem           │
│       │                                                       │
│       ▼                                                       │
│  Apply Similar Solution Strategy                              │
│       │                                                       │
│       ▼                                                       │
│  Adapt as Needed for Target Problem                           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

## 后续步骤

- 探索 [verification.md](./verification.md)，了解检查推理的模板
- 参阅 [composition.md](./composition.md)，了解组合多个模板的方法
- 查看 [../cognitive-programs/advanced-programs.md](../cognitive-programs/advanced-programs.md)，了解利用这些推理模式的程序化方法
