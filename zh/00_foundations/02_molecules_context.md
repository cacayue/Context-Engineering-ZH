---
title: 分子：将提示词与示例结合
source: 00_foundations/02_molecules_context.md
module: M2
task: M2-01
chunks: 1
chunks_done:
  - 1
status: published
source_sha256: dc5e6c881b6e63ea8dbbaf44dadd18d7233d9a37b3bdc2e5acb6e0a180b85ab7
---

> 原文：[00_foundations/02_molecules_context.md](../../00_foundations/02_molecules_context.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# 分子：将提示词与示例结合

> 「整体大于部分之和。」——亚里士多德

## 从原子到分子

上一节，我们探讨了**原子（atom）提示词**——构成 LLM 交互基本单元的单一指令。现在，我们将把这些原子组合成**分子（molecule）**：包含示例与模式、供模型遵循的结构化上下文（context）。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

> 图：分子提示词的组成 —— MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]

这种分子式方法利用了 LLM 的一项强大能力：**少样本（few-shot）学习**。

## 少样本学习：通过示例来教

少样本学习是指我们提供期望的输入—输出模式示例，让模型识别并延续该模式。

```
┌───────────────────────────────────────────────────────────────────────┐
│ Input: "Paris"                                                        │
│ Output: "Paris is the capital of France."                             │
│                                                                       │
│ Input: "Tokyo"                                                        │
│ Output: "Tokyo is the capital of Japan."                              │
│                                                                       │
│ Input: "Ottawa"                                                       │
│ Output: ?                                                             │
└───────────────────────────────────────────────────────────────────────┘
```

> 图：少样本输入—输出示例 —— Input / Output

模型识别出模式后将其补全：「Ottawa is the capital of Canada.」

## 分子式优势：可衡量的改进

让我们比较同一任务下的原子式方法与分子式方法：

```
┌───────────────────────────────────────┬──────────────────────────────────────┐
│ ATOMIC APPROACH                       │ MOLECULAR APPROACH                   │
├───────────────────────────────────────┼──────────────────────────────────────┤
│ "Classify this review as positive     │ "Classify the sentiment of reviews.  │
│  or negative:                         │                                      │
│                                       │ Review: 'The food was amazing!'      │
│  'The service was terrible and        │ Sentiment: Positive                  │
│   the food was cold.'"                │                                      │
│                                       │ Review: 'Waited 30 minutes and       │
│                                       │  the food was cold.'                 │
│                                       │ Sentiment: Negative                  │
│                                       │                                      │
│                                       │ Review: 'The service was terrible    │
│                                       │  and the food was cold.'"            │
│                                       │ Sentiment:                           │
└───────────────────────────────────────┴──────────────────────────────────────┘
```

> 图：原子式方法与分子式方法对比 —— ATOMIC APPROACH / MOLECULAR APPROACH

分子式方法通常能实现：
- 更高的准确率（许多任务上提升 10-30%）
- 更强的一致性（输出方差更低）
- 更好的格式遵循度
- 更清晰地处理边界情况

## 设计有效的分子模板

分子上下文的结构非常重要。以下是一些常见模式：

```
┌─────────────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│ PREFIX-SUFFIX           │  │ INPUT-OUTPUT PAIRS│  │ CHAIN-OF-THOUGHT  │
├─────────────────────────┤  ├───────────────────┤  ├───────────────────┤
│ <instruction>           │  │ <instruction>     │  │ <instruction>     │
│                         │  │                   │  │                   │
│ <example1> → <result1>  │  │ Input: <example1> │  │ Input: <example1> │
│                         │  │ Output: <result1> │  │ Thinking: <step1> │
│ <example2> → <result2>  │  │                   │  │           <step2> │
│                         │  │ Input: <example2> │  │ Output: <result1> │
│ <new_input> →           │  │ Output: <result2> │  │                   │
└─────────────────────────┘  │                   │  │ Input: <example2> │
                             │ Input: <new_input>│  │ Thinking: <step1> │
                             │ Output:           │  │           <step2> │
                             └───────────────────┘  │ Output: <result2> │
                                                    │                   │
                                                    │ Input: <new_input>│
                                                    │ Thinking:         │
                                                    └───────────────────┘
```

> 图：常见分子模板模式 —— PREFIX-SUFFIX / INPUT-OUTPUT PAIRS / CHAIN-OF-THOUGHT

每种模板在不同任务上各有优势：
- **前缀—后缀**：最简单，适合直接了当的任务
- **输入—输出对**：界限清晰，适合结构化数据
- **思维链（chain of thought）**：暴露推理步骤，最适合复杂任务

## 示例选择的科学

并非所有示例都生而平等。为分子上下文挑选示例时：

```
┌──────────────────────────────────────────────────────────────┐
│ EXAMPLE SELECTION STRATEGIES                                 │
├──────────────────────────────────────────────────────────────┤
│ ✓ Cover diverse cases to show range                          │
│ ✓ Include edge cases that clarify boundaries                 │
│ ✓ Order from simple to complex when possible                 │
│ ✓ Use recent or common examples (recency and frequency bias) │
│ ✓ Include near-misses to establish precise boundaries        │
└──────────────────────────────────────────────────────────────┘
```

> 图：示例选择策略 —— EXAMPLE SELECTION STRATEGIES

## 衡量分子效率

随着上下文规模增长，词元数量也随之增长。让我们从经验上衡量这一权衡：

```
                   [Accuracy]
                       ▲
                       │                                    ● 4-shot
                       │                           ● 3-shot
                       │                              
                       │                   ● 2-shot 
                       │              
                       │           
                       │           ● 1-shot 
                       │      
                       │
                       │  
                       │   ● 0-shot
                       └─────────────────────────────────────────────────►
                                [Tokens]
```

> 图：示例数量、词元数与准确率的关系 —— Accuracy / Tokens / 0-shot / 4-shot

关键洞见：**收益递减**。每增加一个示例都要花费词元，但带来的改进却比上一个示例更少。

## 找到分子的甜点区

对多数任务而言，存在一个最佳示例数量，能在质量与词元效率之间取得平衡：

```
┌─────────────────────────────────────────────────────────────────┐
│ EXAMPLE COUNT HEURISTICS BY TASK TYPE                           │
├───────────────────────────┬─────────────────────────────────────┤
│ Classification            │ 1-3 examples per class              │
├───────────────────────────┼─────────────────────────────────────┤
│ Generation                │ 2-5 examples                        │
├───────────────────────────┼─────────────────────────────────────┤
│ Structured Extraction     │ 2-4 examples covering all fields    │
├───────────────────────────┼─────────────────────────────────────┤
│ Reasoning                 │ 2-3 examples with thinking steps    │
├───────────────────────────┼─────────────────────────────────────┤
│ Translation               │ 3-5 examples with varying complexity│
└───────────────────────────┴─────────────────────────────────────┘
```

> 图：按任务类型划分的示例数量经验法则 —— EXAMPLE COUNT HEURISTICS BY TASK TYPE

## 动态分子构造

高级上下文工程包括为每次输入动态选择最相关的示例：

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   User Query                                                      │
│       │                                                           │
│       ▼                                                           │
│  ┌─────────────┐      ┌─────────────────┐                         │
│  │ Query       │      │                 │                         │
│  │ Analysis    │─────▶│ Example         │                         │
│  │             │      │ Database        │                         │
│  └─────────────┘      │                 │                         │
│                       └─────────────────┘                         │
│                              │                                    │
│                              │ Retrieve most                      │
│                              │ similar examples                   │
│                              ▼                                    │
│                       ┌─────────────────┐                         │
│                       │ Dynamic         │                         │
│                       │ Molecular       │                         │
│                       │ Context         │                         │
│                       └─────────────────┘                         │
│                              │                                    │
│                              │                                    │
│                              ▼                                    │
│                       ┌─────────────────┐                         │
│                       │                 │                         │
│                       │ LLM             │                         │
│                       │                 │                         │
│                       └─────────────────┘                         │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

> 图：动态分子上下文构造流程 —— User Query / Query Analysis / Example Database / Dynamic Molecular Context

这种方法：
1. 分析用户查询
2. 检索最相关的示例
3. 构造量身定制的分子上下文
4. 将优化后的上下文发送给 LLM

## 付诸实践：一个简单实现

下面是一个从示例构造分子上下文的 Python 函数：

```python
def create_molecular_context(instruction, examples, new_input, 
                            format_type="input-output"):
    """
    Construct a molecular context from examples.
    
    Args:
        instruction (str): The task instruction
        examples (List[Dict]): List of example input/output pairs
        new_input (str): The new input to process
        format_type (str): Template type (input-output, chain-of-thought)
    
    Returns:
        str: The complete molecular context
    """
    context = f"{instruction}\n\n"
    
    # Add examples based on format type
    if format_type == "input-output":
        for example in examples:
            context += f"Input: {example['input']}\n"
            context += f"Output: {example['output']}\n\n"
    elif format_type == "chain-of-thought":
        for example in examples:
            context += f"Input: {example['input']}\n"
            context += f"Thinking: {example['thinking']}\n"
            context += f"Output: {example['output']}\n\n"
    
    # Add the new input
    context += f"Input: {new_input}\nOutput:"
    
    return context
```


## 关键要点

1. **分子上下文**把指令与示例结合起来，以提升 LLM 性能
2. **少样本学习**让模型能够识别并延续模式
3. **模板结构**很重要；不同格式更适合不同任务
4. **示例选择**是一门科学；多样性、边界情况与顺序都很重要
5. **收益递减**确实存在；每增加一个示例都要花费词元，而收益递减
6. **动态构造**可以针对每个具体输入优化上下文

## 练习

1. 选一个简单的分类任务，分别用 0、1、3、5 个示例衡量性能
2. 在同一任务上比较不同的模板结构
3. 基于与新输入的相似度实现动态示例选择
4. 为你关心的任务找到「最小可行分子」

## 下一步

下一节，我们将探讨**细胞（cell）**——能在多次交互中维持记忆与状态的上下文结构。

[继续阅读 03_cells_memory.md →](03_cells_memory.md)

---

## 深入探究：提示词工程与上下文工程

提示词工程（prompt engineering）专注于打磨出完美的指令。上下文工程（Context Engineering）则涵盖于此，且不止于此：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT ENGINEERING LAYERS                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────┐                                               │
│   │ State & Memory  │  Conversation history, persistent variables   │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Retrieved Data  │  RAG, tool outputs, external knowledge        │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Examples        │  Few-shot learning, demonstrations            │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Instructions    │  Prompts, system messages, constraints        │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Model Behavior  │  Training data, alignments, capabilities      │
│   └─────────────────┘                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

> 图：上下文工程的层次 —— CONTEXT ENGINEERING LAYERS

上下文工程让你能够控制其中更多层次，从而构建更强大的应用。
