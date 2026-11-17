---
title: 吸引子（Attractor）设计模板
source: 20_templates/PROMPTS/attractor_design.md
module: M6
task: M6-01
chunks: 2
chunks_done: [1, 2]
status: published
source_sha256: ce929f04a17c6857084ebae55a53135b2ec5d79b84804eca65823946299e650a
---

> 原文：[20_templates/PROMPTS/attractor_design.md](../../../20_templates/PROMPTS/attractor_design.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 吸引子（Attractor）设计模板

## 摘要
用于创建语义吸引子的模板，无需明确指令即可引导 AI 推理朝向特定概念框架、方法或结果。

## 上下文（Context）与应用
当你希望在语义空间中创建「吸引子」，巧妙引导 AI 推理生成特定类型的响应时，使用此模板。这些概念引力井会自然地将思考拉向特定方向。不同于直接指令，吸引子通过建立 AI 会自然延续或补全的模式（Pattern）发挥作用。

此模板非常适合：
- 鼓励特定思维风格或框架，而不明确要求采用它们
- 创建自然、不生硬的微妙引导
- 建立推理围绕运转的「引力中心」
- 在引导推理的同时保留灵活性与创造力
- 施加影响，但不规定具体结果

## 模板结构

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following concepts may be relevant to consider:*

{{primary_attractor_concept_1}}:
- {{supporting_element_1a}}
- {{supporting_element_1b}}
- {{supporting_element_1c}}

{{primary_attractor_concept_2}}:
- {{supporting_element_2a}}
- {{supporting_element_2b}}
- {{supporting_element_2c}}

{{resonant_concept}}:
- {{resonant_element_a}}
- {{resonant_element_b}}

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
{{output_specifications}}
```

## 参数

- `{{task_description}}`：不明确提及吸引子概念的任务描述
- `{{neutral_context}}`：用于建立上下文、但不偏向吸引子的背景信息
- `{{primary_attractor_concept_X}}`：希望充当语义吸引子的主要概念
- `{{supporting_element_X}}`：强化并界定吸引子概念的要素
- `{{resonant_concept}}`：与主要吸引子产生共振（Resonance）并将其放大的概念
- `{{output_specifications}}`：输出的格式与结构规格

## 示例

### 示例 1：系统思维吸引子

```
# Task: Analyze the challenges facing urban transportation in growing cities

## Context
Urban areas worldwide are experiencing population growth, putting pressure on existing transportation infrastructure. Many cities are seeking solutions to mobility challenges.

## Conceptual Framework
*The following concepts may be relevant to consider:*

Interconnectedness:
- Relationship between transportation and land use
- Impact of transportation choices on environmental systems
- Connection between mobility and economic opportunity

Feedback Loops:
- How infrastructure investments shape development patterns
- Relationship between congestion and behavior adaptation
- Environmental impacts that affect future transportation choices

Emergence:
- Patterns that arise from individual transportation decisions
- Unexpected consequences of transportation policies
- Self-organizing aspects of urban mobility

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
A comprehensive analysis of urban transportation challenges that identifies key issues, explores underlying dynamics, and suggests potential approaches. Include both short-term and long-term perspectives.
```

### 示例 2：创意创新吸引子

```
# Task: Suggest product improvement ideas for a smart home thermostat

## Context
Smart thermostats have become increasingly common in homes, allowing temperature programming, remote control, and some learning capabilities. The company is looking to develop their next generation product.

## Conceptual Framework
*The following concepts may be relevant to consider:*

Boundary Breaking:
- Extending functionality beyond traditional temperature control
- Integration with unexpected systems or services
- Challenging assumptions about what a thermostat should be

Recombination:
- Merging features from different product categories
- Novel combinations of existing technologies
- Unexpected applications of familiar capabilities

User-Centered Surprise:
- Features that anticipate needs users didn't know they had
- Delightful interactions that exceed expectations
- Transformative experiences rather than incremental improvements

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
A list of 5-7 innovative product improvement ideas, each with a brief description, potential user benefit, and implementation considerations. Focus on distinctive ideas rather than obvious incremental improvements.
```

## 变体

### 多吸引子场（Field）
用于创建多个强度不同的吸引子：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following concepts may be relevant to consider (in no particular order):*

{{primary_attractor}} [strength: high]:
- {{supporting_elements}}

{{secondary_attractor}} [strength: medium]:
- {{supporting_elements}}

{{tertiary_attractor}} [strength: low]:
- {{supporting_elements}}

## Approach
Consider these concepts in your response, giving each appropriate consideration.

## Expected Output
{{output_specifications}}
```

### 吸引子与排斥子动力学
用于同时创建吸引和排斥的概念力量：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*Consider the following as you develop your response:*

Relevant Approaches:
- {{attractor_concept_1}}
- {{attractor_concept_2}}
- {{attractor_concept_3}}

Approaches to Avoid:
- {{repeller_concept_1}}
- {{repeller_concept_2}}

## Approach
Develop your response drawing from the relevant approaches while avoiding the limitations of approaches to avoid.

## Expected Output
{{output_specifications}}
```

### 共振场吸引子
用于创建相互强化、彼此放大的概念：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following interconnected concepts may be relevant:*

{{concept_1}} ↔ {{concept_2}}:
- How {{concept_1}} influences {{concept_2}}
- How {{concept_2}} reinforces {{concept_1}}

{{concept_2}} ↔ {{concept_3}}:
- Ways {{concept_2}} shapes {{concept_3}}
- Ways {{concept_3}} enhances {{concept_2}}

{{concept_3}} ↔ {{concept_1}}:
- The relationship between {{concept_3}} and {{concept_1}}
- Mutual amplification effects

## Approach
Consider these resonant relationships in your analysis.

## Expected Output
{{output_specifications}}
```

## 最佳实践

- **巧妙引导，而非强行要求**——吸引子像自然的考虑因素而非强制要求时，效果最好
- **创建连贯的吸引子场**——使用自然互补的概念
- **平衡具体性与开放性**——太模糊无法产生足够牵引，太具体则变成规定
- **用支撑要素清楚界定吸引子**——帮助明确吸引子概念涵盖的内容
- **将吸引子定位为「可考虑的概念」而非要求**——在产生微妙引力的同时保留灵活性
- **用熟悉概念搭桥，引向陌生概念**——帮助开辟通向新思维的路径
- **对于复杂任务，使用多个共振吸引子**——创建丰富的概念场
- **测试吸引子强度**——太弱则增强支撑要素，太强势则降低具体程度
- **让吸引子与真实目标对齐**——牵引应指向真正有用的方法
- **让吸引子有利于发现**——它们应给人洞见而非指令的感觉

## 相关模板

- **场边界建立模板**：用于创建概念边界，与吸引子相互补充
- **共振提示模板**：用于在概念之间创建共振效应
- **角色吸引子模板**：用于将角色用作语义吸引子
- **涌现（Emergence）工程模板**：用于通过吸引子场培育涌现性质
