---
title: 认知工具：扩展上下文工程框架
source: 00_foundations/05_cognitive_tools.md
module: M2
task: M2-03
chunks: 2
chunks_done:
  - 1
  - 2
status: published
source_sha256: 9447185ed630033a6e6ba1631b3b268da4e81a090b4d77c72946c075a5a22abf
---

> 原文：[00_foundations/05_cognitive_tools.md](../../00_foundations/05_cognitive_tools.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# 认知工具：扩展上下文工程框架

> 「心灵不是需要填满的容器，而是需要点燃的火焰。」—— 普鲁塔克

## 从生物到认知

我们的上下文工程（context engineering）之旅一直遵循一条生物隐喻：

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Atoms   │────►│ Molecules│────►│  Cells   │────►│  Organs  │
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
    │                │                │                │
    ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Prompts │     │ Few-shot │     │  Memory  │     │  Multi   │
│          │     │          │     │          │     │  -agent  │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```
> 图：从原子到器官的认知隐喻 —— Atoms → Molecules → Cells → Organs

现在，我们将通过与人类认知建立类比来扩展这一框架。正如人类心智使用认知工具（cognitive tools）高效处理信息一样，我们可以为 LLM 构建类似的结构：

```
┌─────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE TOOLS EXTENSION                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Heuristics        │ Mental shortcuts that simplify       │
│ COGNITION│                   │ complex problems                     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Prompt Programs   │ Structured prompt patterns that      │
│ PARALLEL │                   │ guide model reasoning                │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Schemas           │ Organized knowledge structures       │
│ COGNITION│                   │ that help categorize information     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Context Schemas   │ Standardized formats that            │
│ PARALLEL │                   │ structure information for models     │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Priming           │ Activation of certain associations   │
│ COGNITION│                   │ that influence subsequent thinking   │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Recursive         │ Self-referential prompting that      │
│ PARALLEL │ Prompting         │ shapes model behavior patterns       │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘
```
> 图：认知工具扩展中的人类认知与 LLM 对应 —— COGNITIVE TOOLS EXTENSION / HUMAN COGNITION / LLM PARALLEL


## 认知工具？

### **[用认知工具激发语言模型中的推理—— IBM Zurich，2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)**

### 作为推理工具调用的提示词与提示词程序
> 「认知工具」将推理操作封装在 LLM 自身内部 —— [IBM Zurich](https://www.arxiv.org/pdf/2506.12115)



![图片](https://github.com/user-attachments/assets/cd06c3f5-5a0b-4ee7-bbba-2f9f243f70ae)

> **这些认知工具（作为工具调用的结构化提示词模板）通过识别当前的主要问题概念、提取问题中的相关信息，并突出可能有助于解题的有意义属性、定理和技巧来分解问题。**

![图片](https://github.com/user-attachments/assets/f7ce8605-6fa3-494f-94cd-94e6b23032b6)


> **这些模板为推理层搭建支架，类似认知心理捷径，也就是常说的「启发式」（heuristics）。**

## 提示词程序：面向 LLM 的算法思维（推理工具调用）

提示词程序是一种结构化、可复用的提示词模式（prompt patterns），旨在引导 LLM 的推理过程 —— 类似于启发式引导人类思考的方式。

### 从临时提示词到程序化模式

让我们比较一个临时提示词与一个简单的提示词程序（推理工具调用）：

```
┌───────────────────────────────────────────────────────────────┐
│ AD-HOC PROMPT                                                 │
├───────────────────────────────────────────────────────────────┤
│ "Summarize this article about climate change in 3 paragraphs. │
│  Make it easy to understand."                                 │
└───────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│ PROMPT PROGRAM                                                │
├───────────────────────────────────────────────────────────────┤
│ program Summarize(text, paragraphs=3, complexity="simple") {  │
│   // Define the task                                          │
│   task = `Summarize the following text in ${paragraphs}       │
│           paragraphs. Use ${complexity} language.`;           │
│                                                               │
│   // Define the process                                       │
│   process = ```                                               │
│     1. Identify the main topic and key points                 │
│     2. Organize points by importance                          │
│     3. Create a coherent summary with:                        │
│        - First paragraph: Main topic and context              │
│        - Middle paragraph(s): Key supporting details          │
│        - Final paragraph: Conclusions or implications         │
│   ```;                                                        │
│                                                               │
│   // Define the output format                                 │
│   format = "A ${paragraphs}-paragraph summary using           │
│             ${complexity} language.";                         │
│                                                               │
│   // Construct the complete prompt                            │
│   return `${task}\n\nProcess:\n${process}\n\n                 │
│           Format:\n${format}\n\nText to summarize:\n${text}`; │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```
> 图：临时提示词与提示词程序的对比 —— AD-HOC PROMPT / PROMPT PROGRAM

提示词程序方法有以下几个优势：
1. **可复用性**：同一模式可用于不同文本
2. **参数化**：轻松定制长度、复杂度等
3. **透明性**：清晰的结构使提示词的意图一目了然
4. **一致性**：在不同运行中产生更可预测的结果

### 简易提示词程序模板

下面是创建自己的提示词程序的基本模板：

```
program [Name]( [parameters]) {
  // Define the task
  task = `[Clear instruction using parameters]`;
  
  // Define the process
  process = ```
    1. [First step]
    2. [Second step]
    3. [Additional steps as needed]
  ```;
  
  // Define the output format
  format = "[Expected response structure]";
  
  // Construct the complete prompt
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\n[Input]`;
}
```

在实践中，这个模板可以通过多种方式实现：
- 在文档中作为伪代码或协议壳
- 作为生成提示词的实际 JavaScript/Python 函数
- 作为带变量替换的 YAML 模板
- 作为用于标准化提示词构建的 JSON 模式（schema）

## 推理提示词模板（工具调用）

### 1. 逐步推理

这是把复杂推理拆解为可管理步骤的基本模板。

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

**词元数量（token count）**：约 130 个词元（仅模板）

## 什么是协议壳？（推理工具调用）

协议壳（protocol shells）是结构化的无代码模板，用于把与 AI 系统的交流组织成清晰、一致的模式。可以把它们看作对话蓝图，用来确立：

1. **意图**：你想要完成什么
2. **输入**：你提供什么信息
3. **过程**：应如何处理这些信息
4. **输出**：你期望得到什么结果

### 协议壳的基本结构

```
/protocol.name{
    intent="Clear statement of purpose",
    input={
        param1="value1",
        param2="value2"
    },
    process=[
        /step1{action="do something"},
        /step2{action="do something else"}
    ],
    output={
        result1="expected output 1",
        result2="expected output 2"
    }
}
```

这种结构创建了一个清晰且节省词元的框架，你与 AI 都能遵循。

**反思练习**：回顾你最近的 AI 对话。你能否发现一直在使用的隐含结构（例如情绪上下文、潜在意图、长期目标、相互矛盾的输入等）？把这些结构正式化为协议壳、让数据更明确，会如何改善你的交互？

## 协议壳剖析

让我们剖析协议壳的每个组成部分，理解它的用途与力量：

```
┌─────────────────────────────────────────────────────────┐
│                    PROTOCOL ANATOMY                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  /protocol.name{                                        │
│    │       │                                            │
│    │       └── Subtype or specific variant              │
│    │                                                    │
│    └── Core protocol type                               │
│                                                         │
│    intent="Clear statement of purpose",                 │
│    │       │                                            │
│    │       └── Guides AI understanding of goals         │
│    │                                                    │
│    └── Declares objective                               │
│                                                         │
│    input={                                              │
│        param1="value1",   ◄── Structured input data     │
│        param2="value2"                                  │
│    },                                                   │
│                                                         │
│    process=[                                            │
│        /step1{action="do something"},     ◄── Ordered   │
│        /step2{action="do something else"} ◄── steps     │
│    ],                                                   │
│                                                         │
│    output={                                             │
│        result1="expected output 1",   ◄── Output        │
│        result2="expected output 2"    ◄── specification │
│    }                                                    │
│  }                                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
> 图：协议壳剖析 —— PROTOCOL ANATOMY / /protocol.name{


## 上下文模式：结构化信息模式


正如人类心智用模式组织知识一样，我们可以为 LLM 创建上下文模式（context schemas）—— 用标准化的信息结构来提升模型理解。

### 基本模式结构

```
┌───────────────────────────────────────────────────────────────┐
│ CONTEXT SCHEMA                                                │
├───────────────────────────────────────────────────────────────┤
│ {                                                             │
│   "$schema": "context-engineering/schemas/v1.json",           │
│   "title": "Analysis Request Schema",                         │
│   "description": "Standard format for requesting analysis",   │
│   "type": "object",                                           │
│   "properties": {                                             │
│     "task": {                                                 │
│       "type": "string",                                       │
│       "description": "The analysis task to perform"           │
│     },                                                        │
│     "context": {                                              │
│       "type": "object",                                       │
│       "properties": {                                         │
│         "background": { "type": "string" },                   │
│         "constraints": { "type": "array" },                   │
│         "examples": { "type": "array" }                       │
│       }                                                       │
│     },                                                        │
│     "data": {                                                 │
│       "type": "string",                                       │
│       "description": "The information to analyze"             │
│     },                                                        │
│     "output_format": {                                        │
│       "type": "string",                                       │
│       "enum": ["bullet_points", "paragraphs", "table"]        │
│     }                                                         │
│   },                                                          │
│   "required": ["task", "data"]                                │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```
> 图：上下文模式结构 —— CONTEXT SCHEMA / "$schema": "context-engineering/schemas/v1.json"


### **[MEM1：学习协同记忆（memory）与推理，以实现高效长时程智能体（agents）—— 新加坡 - MIT，2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)**

> 「我们的结果表明，推理驱动的记忆巩固很有前景，可作为训练长时程交互式智能体的现有方案的可扩展替代方案，同时兼顾效率与性能。」—— [Singapore-MIT](https://arxiv.org/pdf/2506.15841)

![图片](https://github.com/user-attachments/assets/16e3f241-5f44-4ed5-9622-f0b4acbb67b0)


### 从模式到提示词

通过填写结构化模板，可以把模式转换为实际提示词：

```
# Analysis Request

## Task
Identify the main themes and supporting evidence in the provided text.

## Context
### Background
This is a speech given at a climate conference in 2023.

### Constraints
- Focus on scientific claims
- Ignore political statements
- Maintain neutrality

### Examples
- Theme: Rising Sea Levels
  Evidence: "Measurements show a 3.4mm annual rise since 2010"

## Data
[The full text of the speech would go here]

## Output Format
bullet_points
```

这种结构化方法有助于模型准确理解提供了哪些信息，以及期望它返回什么。

## 递归提示：自我参照式改进

递归提示（recursive prompting）类似于认知启动（cognitive priming）—— 它会建立影响后续模型行为的模式。关键在于让模型反思并改进自身输出。

### 基本递归模式

```
┌───────────────────────────────────────────────────────────────┐
│ RECURSIVE PROMPTING FLOW                                      │
│                                                               │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐    │
│  │             │      │             │      │             │    │
│  │  Initial    │─────►│  Self-      │─────►│  Improved   │    │
│  │  Response   │      │  Reflection │      │  Response   │    │
│  │             │      │             │      │             │    │
│  └─────────────┘      └─────────────┘      └─────────────┘    │
│        ▲                                          │           │
│        └──────────────────────────────────────────┘           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```
> 图：递归提示流程 —— RECURSIVE PROMPTING FLOW / Initial Response → Self-Reflection → Improved Response

### 简单实现

```python
def recursive_prompt(question, model, iterations=2):
    """Apply recursive prompting to improve responses."""
    
    # Initial response
    response = model.generate(f"Question: {question}\nAnswer:")
    
    for i in range(iterations):
        # Self-reflection prompt
        reflection_prompt = f"""
        Question: {question}
        
        Your previous answer: 
        {response}
        
        Please reflect on your answer:
        1. What information might be missing?
        2. Are there any assumptions that should be questioned?
        3. How could the explanation be clearer or more accurate?
        
        Now, provide an improved answer:
        """
        
        # Generate improved response
        response = model.generate(reflection_prompt)
    
    return response
```

这一简单的递归模式通过鼓励模型批判并精炼自身思考，可以显著提升回答质量。
## 整合一切：认知架构

这些认知工具可以组合成一个完整的架构，映射人类思维过程：

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE ARCHITECTURE                               │
│                                                                           │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Input Parser   │  Understands user intent using schema recognition    │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Prompt Program │  Selects and applies appropriate reasoning pattern   │
│  │  Selector       │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Working Memory │  Maintains state and context across steps            │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Recursive      │  Applies self-improvement through reflection         │
│  │  Processor      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Output         │  Formats final response according to schema          │
│  │  Formatter      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```
> 图：认知架构 —— COGNITIVE ARCHITECTURE / Input Parser → Prompt Program Selector → Working Memory → Recursive Processor → Output Formatter

利用我们讨论过的工具与模式，这一架构可以实现为一个完整的系统。

## 关键要点

1. **提示词程序 / 协议**像人类启发式一样组织推理
2. **上下文模式**像心智知识结构一样组织信息
3. **递归提示**创建类似认知反思的自我改进回路
4. **认知架构**把这些工具组合成完整系统

这些认知扩展让我们能够在上下文工程框架内，创建更复杂但仍易于理解的使用 LLM 的方法。

## 练习

1. 把你常用的一个提示词转换成提示词程序
2. 为你用 LLM 执行的一项常见任务创建一个简单模式
3. 实现基本递归提示，以提升回答质量
4. 把这些方法组合成一个迷你认知架构

## 下一步

在接下来的章节中，我们将探索这些认知工具的实际实现：
- 展示提示词程序实际运行的 Jupyter notebooks
- 用于创建自己的模式的模板
- 完整认知架构的示例

[继续阅读下一节 →](06_advanced_applications.md)

---

## 深入探究：从我们的研究到你的应用

上文描述的认知工具是更高级研究概念的简化表示。如果你想进一步探索：

- **提示词程序**是研究者所称「程序化提示」或「结构化提示框架」的实际实现
- **上下文模式**是知识表示系统与本体论框架的简化版本
- **递归提示**与 AI 系统中的自我反思、元认知和递归自我改进有关

这些简化的框架让高级概念更易理解，同时保留其实际效用。
