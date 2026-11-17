---
title: 思维链（Chain of Thought）模板
source: 20_templates/PROMPTS/chain_of_thought.md
module: M6
task: M6-01
chunks: 1
chunks_done: [1]
status: published
source_sha256: ba06173f85977d5690fbfbab5d642c67cf1cbf0c04079d46f27dea2d78bdb8e2
---

> 原文：[20_templates/PROMPTS/chain_of_thought.md](../../../20_templates/PROMPTS/chain_of_thought.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 思维链（Chain of Thought）模板

## 摘要
用于引导 AI 系统进行明确的逐步推理，提高复杂任务的准确性与透明度的模板。

## 上下文（Context）与应用
当任务需要仔细推理，或得出结论的过程与结论本身同样重要时，使用此模板。思维链提示将复杂思考分解为明确步骤，从而提高准确性、支持验证，并使推理过程透明。

此模板非常适合：
- 复杂的问题求解任务
- 需要逻辑推理的情况
- 多步计算或分析
- 重视解释「为什么」的任务
- 减少难题中的错误

## 模板结构

```
# Task: {{task_description}}

## Approach
Think through this step-by-step:

1. {{first_reasoning_step}}
2. {{second_reasoning_step}}
3. {{additional_steps_as_needed}}
4. Formulate your conclusion based on this reasoning.

## Expected Output
Provide your complete reasoning process and then your final answer.
```

## 参数

- `{{task_description}}`：清楚描述要解决的问题或要回答的疑问
- `{{first_reasoning_step}}`：推理过程的初始步骤（例如「识别关键变量」）
- `{{second_reasoning_step}}`：接下来的逻辑步骤（例如「确定变量之间的关系」）
- `{{additional_steps_as_needed}}`：引导完整推理的后续步骤

## 示例

### 示例 1：数学问题求解

```
# Task: Solve the following word problem

A store sells notebooks for $4 each and pens for $2 each. Emma bought some notebooks and twice as many pens. If she spent $24 in total, how many notebooks did she buy?

## Approach
Think through this step-by-step:

1. Define variables for what we're looking for
2. Set up equations based on the given information
3. Solve the equations to find the unknown values
4. Verify your answer makes sense with the original conditions

## Expected Output
Provide your complete reasoning process and then your final answer.
```

### 示例 2：伦理决策分析

```
# Task: Analyze the ethical implications of the following scenario

A pharmaceutical company has developed a drug that shows promise for treating a rare disease. The clinical trials indicate 70% efficacy but also reveal potentially serious side effects in 15% of patients. The company needs to decide whether to bring this drug to market.

## Approach
Think through this step-by-step:

1. Identify the key stakeholders in this scenario
2. Analyze the potential benefits of making the drug available
3. Consider the potential harms and risks involved
4. Evaluate alternative options that might be available
5. Balance competing ethical principles (beneficence, non-maleficence, autonomy, justice)
6. Formulate a nuanced recommendation with potential safeguards or conditions

## Expected Output
Provide your complete reasoning process and then your final recommendation.
```

## 变体

### 自提示思维链
用于鼓励 AI 自行制定推理步骤：

```
# Task: {{task_description}}

## Approach
- First, break this problem down into logical steps
- Work through each step systematically
- Show your complete reasoning process
- Only then provide your final answer

## Expected Output
Step-by-step reasoning followed by conclusion.
```

### 引导式问题分解
用于需要更结构化指导的高度复杂问题：

```
# Task: {{task_description}}

## Problem Decomposition
1. Sub-problem 1: {{sub_problem_description}}
   - Consider: {{relevant_factor_1}}
   - Consider: {{relevant_factor_2}}

2. Sub-problem 2: {{sub_problem_description}}
   - Consider: {{relevant_factor_1}}
   - Consider: {{relevant_factor_2}}

3. Integration: Combine your analyses from the sub-problems

## Expected Output
Analysis of each sub-problem, integration of insights, and final conclusion.
```

### 场景分析思维链
用于需要考虑多种场景的决策：

```
# Task: {{decision_task}}

## Approach
Think through this step-by-step:

1. Scenario A: If {{condition_A}} happens
   - Probable outcomes:
   - Benefits:
   - Risks:

2. Scenario B: If {{condition_B}} happens
   - Probable outcomes:
   - Benefits:
   - Risks:

3. Compare scenarios and determine the most robust approach

## Expected Output
Analysis of each scenario and reasoned recommendation.
```

## 最佳实践

- **让推理步骤匹配问题类型**——不同问题需要不同的推理方法
- **明确推理过程**——清楚说明每一步应进行什么思考
- **加入验证步骤**——增加检查工作或验证结论的步骤
- **对于数学问题**，加入检查单位和数量级的步骤
- **对于伦理或主观分析**，加入考虑多种视角的步骤
- **不要跳步**——将推理拆成更小的步骤可提高准确性
- 大多数问题**使用 3-7 个步骤**——太少缺乏引导，太多则令人不堪重负
- **鼓励元认知**——加入促使反思推理过程本身的步骤
- **对于复杂问题**，考虑先分解为子问题，再整合

## 相关模板

- **验证回路模板**：通过明确的验证步骤扩展思维链
- **少样本（Few-Shot）学习模板**：可结合使用，展示思维链推理示例
- **元认知反思模板**：用于深入思考推理过程本身
