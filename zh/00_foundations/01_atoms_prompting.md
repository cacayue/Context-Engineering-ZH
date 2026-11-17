---
title: 原子：提示的基本单元
source: 00_foundations/01_atoms_prompting.md
module: M2
task: M2-01
chunks: 1
chunks_done:
  - 1
status: published
source_sha256: d8d05ceaf3efc8b7de28f2ee88deab8bdd28f3357b69745669483c6eb7e2d82b
---

> 原文：[00_foundations/01_atoms_prompting.md](../../00_foundations/01_atoms_prompting.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# 原子：提示的基本单元

> 「如果你想从头做一个苹果派，你必须先发明宇宙。」——卡尔·萨根

## 原子：一条指令

在我们的上下文工程（Context Engineering）之旅中，我们从最基本的单元开始：**原子（atom）**——给 LLM 的一条独立指令。

```
┌───────────────────────────────────────────────┐
│                                               │
│  "Write a poem about the ocean in 4 lines."   │
│                                               │
└───────────────────────────────────────────────┘
```

> 图：单条指令示例 —— "Write a poem about the ocean in 4 lines."

这是最纯粹形式的提示词工程（prompt engineering）：一个人、一条指令、一次模型响应。简单、直接、原子化。

## 原子提示词剖析

让我们拆解一下有效原子提示词（atomic prompt）的构成：

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ATOMIC PROMPT = [TASK] + [CONSTRAINTS] + [OUTPUT FORMAT]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

> 图：原子提示词的组成 —— ATOMIC PROMPT = [TASK] + [CONSTRAINTS] + [OUTPUT FORMAT]

例如：

```
┌─────────────────────┬────────────────────────┬────────────────────┐
│        TASK         │      CONSTRAINTS       │   OUTPUT FORMAT    │
├─────────────────────┼────────────────────────┼────────────────────┤
│ "Write a poem       │ "about the ocean       │ "in 4 lines."      │
│  about space."      │  using only words      │                    │
│                     │  with 5 letters        │                    │
│                     │  or less."             │                    │
└─────────────────────┴────────────────────────┴────────────────────┘
```

> 图：原子提示词的组成拆解 —— TASK / CONSTRAINTS / OUTPUT FORMAT

## 原子的局限

虽然原子提示词是 LLM 交互的基石，但它们很快暴露出根本局限：

```
┌──────────────────────────────────────┐
│ LIMITATIONS OF ATOMIC PROMPTS        │
├──────────────────────────────────────┤
│ ✗ No memory across interactions      │
│ ✗ Limited demonstration capability   │
│ ✗ No complex reasoning scaffolds     │
│ ✗ Prone to ambiguity                 │
│ ✗ High variance in outputs           │
└──────────────────────────────────────┘
```

> 图：原子提示词的局限 —— LIMITATIONS OF ATOMIC PROMPTS

让我们用一个简单实验从经验上衡量这一点：

```python
# A basic atomic prompt
atomic_prompt = "List 5 symptoms of diabetes."

# Send to LLM multiple times
responses = [llm.generate(atomic_prompt) for _ in range(5)]

# Measure variability
unique_symptoms = set()
for response in responses:
    symptoms = extract_symptoms(response)
    unique_symptoms.update(symptoms)

print(f"Found {len(unique_symptoms)} unique symptoms across 5 identical prompts")
# Typically outputs far more than just 5 unique symptoms
```


问题在于：当给出的上下文（context）极少时，模型难以保持一致。

## 单原子基线：有用但有限

尽管有局限，原子提示词仍确立了我们的基线。它们帮助我们：

1. 衡量词元（token）效率（开销极小）
2. 对响应质量进行基准测试
3. 为实验建立对照组

```
                     [Response Quality]
                            ▲
                            │
                            │               ⭐ Context
                            │                 Engineering
                            │               
                            │           
                            │       ⭐ Advanced
                            │         Prompting
                            │
                            │   ⭐ Basic Prompting
                            │
                            │
                            └────────────────────────►
                                  [Complexity]
```

> 图：响应质量与复杂度的关系 —— Response Quality / Complexity

## 未言明的上下文：模型已经「知道」什么

即便使用原子提示词，LLM 也会利用其训练中大量隐式的上下文：

```
┌───────────────────────────────────────────────────────────────┐
│ IMPLICIT CONTEXT IN MODELS                                    │
├───────────────────────────────────────────────────────────────┤
│ ✓ Language rules and grammar                                  │
│ ✓ Common knowledge facts                                      │
│ ✓ Format conventions (lists, paragraphs, etc.)                │
│ ✓ Domain-specific knowledge (varies by model)                 │
│ ✓ Learned interaction patterns                                │
└───────────────────────────────────────────────────────────────┘
```

> 图：模型中隐式的上下文 —— IMPLICIT CONTEXT IN MODELS

这种隐式知识为我们提供了基础，但它并不可靠，且会因模型和版本而异。

## 幂律：词元—质量曲线

对许多任务而言，我们观察到上下文词元与输出质量之间存在幂律关系：

```
Quality
      ▲
      │                        •
      │                    •       •
      │                •               •
      │            •                       •
      │        •                               •
      │    •
      │•
      └───────────────────────────────────────────► Tokens
          [Poor Start]  [Maximum ROI]  [Diminishing Returns]
```

> 图：词元数量与输出质量的幂律曲线 —— Quality / Tokens / Maximum ROI

关键洞见：存在一个「最大 ROI 区间」——只需再增加少量词元，就能带来显著的质量提升；同时也存在「收益递减」——继续增加词元反而会降低性能。

## [深入了解上下文退化](https://research.trychroma.com/context-rot)

## 从原子到分子：对更多上下文的需求

原子的局限自然引导我们走向下一步：**分子（molecule）**——把指令与示例、附加上下文和结构化格式结合起来的多部分提示词。

下面是这一根本转变：

```
┌──────────────────────────┐         ┌──────────────────────────┐
│                          │         │ "Here's an example:      │
│ "Write a limerick about  │    →    │  There once was a...     │
│  a programmer."          │         │                          │
│                          │         │  Now write a limerick    │
└──────────────────────────┘         │  about a programmer."    │
                                     └──────────────────────────┘
    [Atomic Prompt]                       [Molecular Prompt]
```

> 图：从原子提示词到分子提示词 —— Atomic Prompt / Molecular Prompt

通过添加示例与结构，我们开始有意塑造上下文窗口（context window）——这是迈向上下文工程的第一步。

## 衡量原子效率：你的第一个任务

在继续之前，试试这个简单练习：

1. 选一个你会交给 LLM 的基本任务
2. 创建三个不同的原子提示词版本
3. 衡量所用词元数与主观质量
4. 绘制效率前沿

```
┌─────────────────────────────────────────────────────────────┐
│ Task: Summarize a news article                              │
├─────────┬───────────────────────────────┬────────┬──────────┤
│ Version │ Prompt                        │ Tokens │ Quality  │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ A       │ "Summarize this article."     │ 4      │ 2/10     │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ B       │ "Provide a concise summary    │ 14     │ 6/10     │
│         │  of this article in 3         │        │          │
│         │  sentences."                  │        │          │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ C       │ "Write a summary of the key   │ 27     │ 8/10     │
│         │  points in this article,      │        │          │
│         │  highlighting the main        │        │          │
│         │  people and events."          │        │          │
└─────────┴───────────────────────────────┴────────┴──────────┘
```

> 图：原子提示词效率对比 —— Version / Prompt / Tokens / Quality

## 关键要点

1. **原子提示词**是 LLM 交互的基本单元
2. 它们遵循一个基本结构：任务 + 约束 + 输出格式
3. 它们有内在局限：没有记忆、示例或推理支架
4. 即使是简单的原子提示词，也会利用模型的隐式知识
5. 上下文词元与质量之间存在幂律关系
6. 超越原子是迈向上下文工程的第一步

## 下一步

下一节，我们将探讨如何把原子组合成**分子**——这种少样本（few-shot）学习模式能显著提升可靠性与控制力。

[继续阅读 02_molecules_context.md →](02_molecules_context.md)

---

## 深入探究：提示词模板

对于想用原子提示词做更多实验的读者，这里有几个可尝试的模板：

```
# Basic instruction
{task}

# Persona-based
As a {persona}, {task}

# Format-specific
{task}
Format: {format_specification}

# Constraint-based
{task}
Constraints:
- {constraint_1}
- {constraint_2}
- {constraint_3}

# Step-by-step guided
{task}
Please follow these steps:
1. {step_1}
2. {step_2}
3. {step_3}
```


试着对同一任务使用每个模板，衡量其词元数量与质量！
