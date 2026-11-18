---
title: 上下文工程（Context Engineering）的认知工具（cognitive tool）
source: cognitive-tools/README.md
module: M9
task: M9-01
chunks: 1
chunks_done: [1]
status: published
source_sha256: 8a3aec44cdd989648ba8f61c28a71f377d23340bc6411e628e44d054e3c3290e
---

> 原文：[cognitive-tools/README.md](../../cognitive-tools/README.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# 上下文工程（Context Engineering）的认知工具（cognitive tool）

> 「给我一根足够长的杠杆和一个支点，我就能撬动世界。」—— 阿基米德

## 什么是认知工具？
> "Providing our “cognitive tools” to GPT-4.1
increases its pass@1 performance on AIME2024 from 26.7% to 43.3%, bringing it very close to the performance of o1-preview." — [IBM June 2025](https://www.arxiv.org/pdf/2506.12115)

<div align="center">
    
![image](https://github.com/user-attachments/assets/a6402827-8bc0-40b5-93d8-46a07154fa4e)

"The tool breaks down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that might be helpful in solving the problem." — [Eliciting Reasoning in Language Models with Cognitive Tools — IBM June 2025](https://www.arxiv.org/pdf/2506.12115)


</div>

认知工具是结构化提示词模式，引导语言模型执行特定推理操作。正如人类解决问题时使用类比、心智模型和启发式等思维工具，这些工具为模型的复杂推理任务提供支架。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  CONTEXT ENGINEERING PROGRESSION                             │
│                                                              │
│  Atoms       → Molecules   → Cells       → Organs      → Cognitive Tools  │
│  (Prompts)     (Few-shot)    (Memory)      (Multi-agent)  (Reasoning Patterns) │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```
> 图：上下文工程结构与流程 —— CONTEXT ENGINEERING PROGRESSION

## 结构
```
cognitive-tools/
├── README.md                       # Overview and quick-start guide
├── cognitive-templates/            # Templates for cognitive processes
│   ├── understanding.md            # Comprehension templates
│   ├── reasoning.md                # Reasoning templates
│   ├── verification.md             # Verification templates
│   ├── composition.md              # Composition templates
│   ├── emergence.md                # Emergence templates
│   ├── quantum_interpretation.md   # Quantum semantics templates
│   ├── unified_field_reasoning.md  # Unified field templates
│   ├── meta_recursive_reasoning.md # Self-improvement templates
│   ├── interpretability_scaffolding.md # Transparency templates
│   ├── collaborative_co_evolution.md # Human-AI templates
│   └── cross_modal_integration.md  # Multi-modal templates
├── cognitive-programs/             # Executable cognitive processes
│   ├── basic-programs.md           # Fundamental programs
│   ├── advanced-programs.md        # Complex programs
│   ├── program-library.py          # Program collection
│   ├── program-examples.ipynb      # Program demonstrations
│   ├── emergence-programs.md       # Emergence programs
│   ├── quantum_semantic_programs.md # Quantum semantics programs
│   ├── unified_field_programs.md   # Unified field programs
│   ├── meta_recursive_programs.md  # Self-improvement programs
│   ├── interpretability_programs.md # Transparency programs
│   ├── collaborative_evolution_programs.md # Human-AI programs
│   └── cross_modal_programs.md     # Multi-modal programs
├── cognitive-schemas/              # Knowledge representation structures
│   ├── user-schemas.md             # User modeling schemas
│   ├── domain-schemas.md           # Domain knowledge schemas
│   ├── task-schemas.md             # Task representation schemas
│   ├── schema-library.yaml         # Schema collection
│   ├── field-schemas.md            # Field theory schemas
│   ├── quantum_schemas.md          # Quantum semantics schemas
│   ├── unified_schemas.md          # Unified field schemas
│   ├── meta_recursive_schemas.md   # Self-improvement schemas
│   ├── interpretability_schemas.md # Transparency schemas
│   ├── collaborative_schemas.md    # Human-AI schemas
│   └── cross_modal_schemas.md      # Multi-modal schemas
├── cognitive-architectures/        # System-level frameworks
│   ├── solver-architecture.md      # Problem-solving architecture
│   ├── tutor-architecture.md       # Educational architecture
│   ├── research-architecture.md    # Research assistant architecture
│   ├── architecture-examples.py    # Architecture demonstrations
│   ├── field-architecture.md       # Field theory architecture
│   ├── quantum_architecture.md     # Quantum semantics architecture
│   ├── unified_architecture.md     # Unified field architecture
│   ├── meta_recursive_architecture.md # Self-improvement architecture
│   ├── interpretability_architecture.md # Transparency architecture
│   ├── collaborative_architecture.md # Human-AI architecture
│   └── cross_modal_architecture.md # Multi-modal architecture
├── integration/                    # Integration with other systems
│   ├── with-rag.md                 # Retrieval integration
│   ├── with-memory.md              # Memory system integration
│   ├── with-agents.md              # Agent system integration
│   ├── evaluation-metrics.md       # Evaluation methods
│   ├── with-fields.md              # Field theory integration
│   ├── with-quantum.md             # Quantum semantics integration
│   ├── with-unified.md             # Unified field integration
│   ├── with-meta-recursion.md      # Self-improvement integration
│   ├── with-interpretability.md    # Transparency integration
│   ├── with-collaboration.md       # Human-AI integration
│   └── with-cross-modal.md         # Multi-modal integration
└── meta-cognition/                 # Meta-cognitive capabilities
    ├── self-reflection.md          # Self-analysis systems
    ├── recursive-improvement.md    # Self-enhancement methods
    ├── meta-awareness.md           # System self-awareness
    ├── attribution-engines.md      # Causal attribution systems
    ├── symbolic-echo-processing.md # Symbolic pattern processing
    ├── meta-interpretability.md    # Meta-level transparency
    ├── meta-collaboration.md       # Meta-level human-AI partnership
    └── meta-modal-integration.md   # Meta-level modal integration
```
> 图：上下文工程结构与流程 —— cognitive-tools/
## 认知工具为何重要

研究表明，用认知工具组织推理能够显著提升模型性能：

- **性能**：在数学推理基准测试中提升高达 16.6%
- **可靠性**：显著减少推理错误与幻觉
- **效率**：用更少的总词元获得更佳的结果
- **灵活性**：适用于从数学到创意写作的各个领域

## 快速入门

要使用认知工具，请从 `cognitive-templates/` 中选择与任务匹配的模板：

```python
# Example: Using the "understand_question" cognitive tool
from cognitive_tools.templates import understand_question

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
understanding = llm.generate(understand_question(problem))
print(understanding)
```

对于更复杂的推理，请使用 `cognitive-programs/` 中的结构化提示词程序：

```python
# Example: Using a multi-step reasoning program
from cognitive_tools.programs import solve_math_problem

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
solution = solve_math_problem(problem, llm=my_llm_interface)
print(solution.steps)  # View step-by-step reasoning
print(solution.answer)  # View final answer
```

## 目录结构

- `cognitive-templates/`：用于不同推理操作的可复用模板
- `cognitive-programs/`：具有类代码模式的结构化提示词程序
- `cognitive-schemas/`：面向不同领域的知识表示格式
- `cognitive-architectures/`：结合多种工具的完整推理系统
- `integration/`：与其他组件（RAG、记忆等）集成的指南

## 学习路径

1. **从模板开始**：学习基础认知操作
2. **探索程序**：了解如何将操作组合为推理流程
3. **研究模式（Schemas）**：理解如何有效组织知识结构
4. **掌握架构**：构建完整的推理系统
5. **集成组件**：与 RAG、记忆及其他上下文工程组件结合

## 衡量效果

始终衡量认知工具对具体任务的影响：

```python
# Example: Measuring performance improvement
from cognitive_tools.evaluation import measure_reasoning_quality

baseline_score = measure_reasoning_quality(problem, baseline_prompt)
tool_score = measure_reasoning_quality(problem, cognitive_tool_prompt)

improvement = (tool_score / baseline_score - 1) * 100
print(f"Cognitive tool improved performance by {improvement:.1f}%")
```

## 研究基础

这些工具基于以下研究：

- Brown et al. (2025): "Eliciting Reasoning in Language Models with Cognitive Tools"
- Wei et al. (2023): "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Huang et al. (2022): "Inner Monologue: Embodying Knowledge and Reasoning in Language Models"

## 参与贡献

有新的有效认知工具模式？请参阅 [CONTRIBUTING.md](../../.github/CONTRIBUTING.md)，了解提交模板、程序或架构的指南。（上游链接已失效。）

## 下一步

- 查看 [understanding.md](./cognitive-templates/understanding.md) 了解基础理解工具
- 尝试 [basic-programs.md](./cognitive-programs/basic-programs.md) 了解基础程序结构
- 探索 [solver-architecture.md](./cognitive-architectures/solver-architecture.md) 了解完整的解题系统
