---
title: Context-Engineering —— 结构总览
source: STRUCTURE/STRUCTURE.md
module: M1
task: M1-03
chunks: 2
chunks_done:
  - 1
  - 2
status: published
source_sha256: eeda905f8681e11b2feb1b34fd2958705a5e5a4ec369dd8752219628fe76553f
---

> 原文：[STRUCTURE/STRUCTURE.md](../../STRUCTURE/STRUCTURE.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# Context-Engineering —— 结构总览
_面向下一代 LLM 编排（orchestration）的实用第一性原理手册_

> **本仓库为何存在**
> 提示词工程（prompt engineering）= 思考你要说**什么**。
> **上下文工程（context engineering）** = 思考模型看到的**其他一切**。
> 我们的目标是从零开始讲清这个"其他一切"，保持谦逊，并倾向于简单、可运行的代码。
>
> 随着模型不断演进，我们的方法也在演进：从离散的词元（token）到连续的场，从静态提示到共振模式。

---

## 1. 领域地图

| 目录 | 作用（通俗说法） | 第一性原理隐喻 |
|--------|----------------------|---------------------------|
| `00_foundations` | 理论与直觉，短小精悍的自足读物。 | 原子 → 分子 → 细胞 → 器官 → 神经系统 → 场 |
| `10_guides_zero_to_hero` | 可**运行**、可修改、可弄坏的交互式指南。 | 化学实验箱 |
| `20_templates` | 即插即用的代码片段，可复制粘贴。 | 乐高积木 |
| `30_examples` | 端到端迷你应用，一个比一个难。 | 模式生物 |
| `40_reference` | 深入讲解与评估手册。 | 教科书附录 |
| `50_contrib` | 社区提交 PR 的空间。 | 开放式实验台 |
| `60_protocols` | 协议壳、模式（schema）与框架。 | DNA 序列 |
| `70_agents` | 使用协议的独立智能体演示。 | 干细胞培养 |
| `80_field_integration` | 使用场协议的端到端项目。 | 完整生物体 |
| `cognitive-tools` | 高级认知框架与架构。 | 扩展的神经系统 |

---

## 2. 学习路径（从零起步到精通）

### 基础篇（理解基本原理）

1. **浏览 `README.md`（2 分钟）**
   看看"上下文"在提示之外究竟意味着什么。

2. **阅读 `00_foundations/01_atoms_prompting.md`（5 分钟）**
   *原子*：单条指令 / 单个示例。
   为什么只有原子往往表现不佳。

3. **沿着生物隐喻链继续：**
   - `02_molecules_context.md`：少样本（few-shot）示例包
   - `03_cells_memory.md`：记忆与日志
   - `04_organs_applications.md`：多步控制流
   - `05_cognitive_tools.md`：心智模型扩展
   - `06_advanced_applications.md`：真实世界的实现
   - `07_prompt_programming.md`：类代码的推理模式
   - `08_neural_fields_foundations.md`：作为连续场的上下文
   - `09_persistence_and_resonance.md`：场动力学与吸引子
   - `10_field_orchestration.md`：多个场的协调

### 动手实践（在做中学）

4. **打开 `10_guides_zero_to_hero/01_min_prompt.ipynb`**
   运行、修改、观察词元计数。
   笔记本中的单元格强调**为什么**每多一行会有帮助（或有害）。

5. **通过渐进式笔记本实验：**
   - 基础上下文操作
   - 控制流与推理模式
   - 检索增强策略
   - 提示词编程技巧
   - 模式设计原则
   - 递归上下文模式
   - 神经场实现

### 应用技能（构建真实方案）

6. **从 `20_templates/` 复制一个模板**
   作为项目的起点：
   - `minimal_context.yaml` 适合基础项目
   - `control_loop.py` 适合交互式系统
   - `scoring_functions.py` 适合评估
   - `prompt_program_template.py` 适合推理任务
   - `schema_template.yaml` 适合结构化数据
   - `recursive_framework.py` 适合自我改进的系统
   - `neural_field_context.yaml` 适合基于场的方法

7. **研究 `30_examples/` 中的示例**
   查看复杂度逐级提升的完整实现：
   - 基础对话智能体
   - 数据标注系统
   - 多智能体编排
   - 认知助手
   - RAG 实现
   - 神经场编排器

### 高级主题（精益求精）

8. **探索认知工具与协议：**
   - `cognitive-tools/` 中的高级推理框架
   - `60_protocols/` 中的协议壳与模式（schema）
   - `70_agents/` 中的智能体演示
   - `80_field_integration/` 中的完整场集成项目

9. **回馈社区：**
   - 查看 `50_contrib/README.md` 中的贡献指南
   - 检查 `40_reference/eval_checklist.md` 中的评估标准
   - 用你的改进或扩展提交 PR

---

## 3. 生物隐喻的演进

本仓库围绕一个扩展的生物隐喻组织，它帮助把抽象概念具体化，并展示简单组件如何逐步构建为复杂系统：

```
                                   ┌───────────────────┐
                                   │  Neural Fields    │  08_neural_fields_foundations.md
                                   │  (Continuous      │  09_persistence_and_resonance.md
                                   │   Context Medium) │  10_field_orchestration.md
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                                   ┌───────┴───────────┐
                                   │ Neurobiological   │  05_cognitive_tools.md
                                   │ Systems           │  06_advanced_applications.md
                                   │ (Cognitive Tools) │  07_prompt_programming.md
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Organs            │  04_organs_applications.md
                             │  (Multi-Agent Systems)    │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Cells             │  03_cells_memory.md
                             │   (Memory Systems)        │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │       Molecules           │  02_molecules_context.md
                             │   (Few-Shot Examples)     │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Atoms             │  01_atoms_prompting.md
                             │    (Single Prompts)       │
                             └───────────────────────────┘
```
> 图：生物隐喻层级 —— 从原子到神经场

这一演进遵循生物系统中复杂度的自然递进，也映照出日益精密的上下文工程方法的发展过程。

---

## 4. 高级上下文框架

### 协议壳框架

协议提供结构化的壳（shell），用于编排复杂的上下文操作。相关定义位于 `60_protocols/` 目录：

```
/recursive.field{
    intent="Define field properties and operations",
    input={
        field_state=<current_state>,
        new_information=<incoming_data>
    },
    process=[
        /field.measure{resonance, coherence, entropy},
        /pattern.detect{across="field_state"},
        /attractor.form{where="pattern_strength > threshold"},
        /field.evolve{with="new_information"}
    ],
    output={
        updated_field=<new_state>,
        metrics={resonance_score, coherence_delta}
    }
}
```

这些协议壳实现了：
- 上下文操作的声明式定义
- 递归自我改进模式
- 基于场的上下文操作
- 通过显式过程步骤实现的可审计性

### 认知工具框架

认知工具提供可复用的推理模式，用以扩展模型能力。相关定义位于 `cognitive-tools/` 目录：

```
cognitive-tools/
├── cognitive-templates/     # Pattern templates for different reasoning modes
├── cognitive-programs/      # Structured prompt programs with code-like patterns
├── cognitive-schemas/       # Knowledge representation formats
├── cognitive-architectures/ # Complete reasoning systems
└── integration/            # Guides for integrating with other components
```
> 图：认知工具目录结构 —— 模板、程序、模式、架构与集成

该框架支持：
- 模块化的推理组件
- 特定领域的推理模式
- 与检索和记忆系统的集成
- 推理质量的评估指标
### 神经场框架

神经场（neural field）把上下文表示为连续介质，而非离散词元。相关实现分布在：

```
00_foundations/08_neural_fields_foundations.md  # Conceptual foundation
00_foundations/09_persistence_and_resonance.md  # Field dynamics
00_foundations/10_field_orchestration.md        # Multi-field coordination
20_templates/neural_field_context.yaml          # Implementation template
30_examples/05_neural_field_orchestrator/       # Complete example
```
> 图：神经场实现分布 —— 概念、动力学、协调、模板与示例

关键概念包括：
- 作为连续语义场的上下文
- 通过共振实现的信息持续性
- 吸引子的形成与动力学
- 面向复杂任务的场编排

---

## 5. 克制的 Karpathy 准则（风格 DNA）

*保持原子化 → 逐步构建。*
1. **最小首版** —— 从最小可行的上下文开始。
2. **迭代追加** —— 只添加模型确实缺少的内容。
3. **测量一切** —— 词元成本、延迟、质量分数、场共振。
4. **果断删除** —— 剪枝胜过堆砌。
5. **代码 > 幻灯片** —— 每个概念都有可运行的单元格。
6. **递归思考** —— 让上下文自我演进。

---

## 6. 仓库结构详解

```
Context-Engineering/
├── LICENSE                          # MIT license
├── README.md                        # Quick-start overview
├── structure.md                     # This structural map
├── context.json                     # Original schema configuration
├── context_v2.json                  # Extended schema with field protocols
│
├── 00_foundations/                  # First-principles theory
│   ├── 01_atoms_prompting.md        # Atomic instruction units
│   ├── 02_molecules_context.md      # Few-shot examples/context
│   ├── 03_cells_memory.md           # Stateful conversation layers
│   ├── 04_organs_applications.md    # Multi-step control flows
│   ├── 05_cognitive_tools.md        # Mental model extensions
│   ├── 06_advanced_applications.md  # Real-world implementations
│   ├── 07_prompt_programming.md     # Code-like reasoning patterns
│   ├── 08_neural_fields_foundations.md # Context as continuous fields
│   ├── 09_persistence_and_resonance.md # Field dynamics and attractors
│   └── 10_field_orchestration.md    # Coordinating multiple fields
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments
│   ├── 02_expand_context.ipynb      # Context expansion techniques
│   ├── 03_control_loops.ipynb       # Flow control mechanisms
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns
│   ├── 05_prompt_programs.ipynb     # Structured reasoning programs
│   ├── 06_schema_design.ipynb       # Schema creation patterns
│   ├── 07_recursive_patterns.ipynb  # Self-referential contexts
│   └── 08_neural_fields.ipynb       # Working with field-based contexts
│
├── 20_templates/                    # Reusable components
│   ├── minimal_context.yaml         # Base context structure
│   ├── control_loop.py              # Orchestration template
│   ├── scoring_functions.py         # Evaluation metrics
│   ├── prompt_program_template.py   # Program structure template
│   ├── schema_template.yaml         # Schema definition template
│   ├── recursive_framework.py       # Recursive context template
│   ├── neural_field_context.yaml    # Field-based context template
│   ├── field_resonance_measure.py   # Field property measurement
│   └── context_audit.py             # Context analysis tool
│
├── 30_examples/                     # Practical implementations
│   ├── 00_toy_chatbot/              # Simple conversation agent
│   ├── 01_data_annotator/           # Data labeling system
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system
│   ├── 03_cognitive_assistant/      # Advanced reasoning assistant
│   ├── 04_rag_minimal/              # Minimal RAG implementation
│   └── 05_neural_field_orchestrator/ # Field-based orchestration
│
├── 40_reference/                    # Deep-dive documentation
│   ├── token_budgeting.md           # Token optimization strategies
│   ├── retrieval_indexing.md        # Retrieval system design
│   ├── eval_checklist.md            # PR evaluation criteria
│   ├── cognitive_patterns.md        # Reasoning pattern catalog
│   ├── schema_cookbook.md           # Schema pattern collection
│   ├── neural_field_theory.md       # Comprehensive field theory
│   ├── symbolic_residue_guide.md    # Guide to residue tracking
│   └── protocol_reference.md        # Protocol shell reference
│
├── 50_contrib/                      # Community contributions
│   └── README.md                    # Contribution guidelines
│
├── 60_protocols/                    # Protocol shells and frameworks
│   ├── README.md                    # Protocol overview
│   ├── shells/                      # Protocol shell definitions
│   │   ├── attractor.co.emerge.shell      # Attractor co-emergence
│   │   ├── recursive.emergence.shell      # Recursive field emergence
│   │   ├── recursive.memory.attractor.shell # Memory persistence
│   │   └── field.resonance.scaffold.shell  # Field resonance
│   ├── digests/                     # Simplified protocol documentation
│   └── schemas/                     # Protocol schemas
│       ├── fractalRepoContext.v1.json     # Repository context
│       ├── fractalConsciousnessField.v1.json # Field schema
│       └── protocolShell.v1.json           # Shell schema
│
├── 70_agents/                       # Agent demonstrations
│   ├── README.md                    # Agent overview
│   ├── 01_residue_scanner/          # Symbolic residue detection
│   └── 02_self_repair_loop/         # Self-repair protocol
│
├── 80_field_integration/            # Complete field projects
│   ├── README.md                    # Integration overview
│   ├── 00_protocol_ide_helper/      # Protocol development tools
│   └── 01_context_engineering_assistant/ # Field-based assistant
│
├── cognitive-tools/                 # Advanced cognitive framework
│   ├── README.md                    # Overview and quick-start guide
│   ├── cognitive-templates/         # Templates for reasoning
│   │   ├── understanding.md         # Comprehension operations
│   │   ├── reasoning.md             # Analytical operations
│   │   ├── verification.md          # Checking and validation
│   │   └── composition.md           # Combining multiple tools
│   │
│   ├── cognitive-programs/          # Structured prompt programs
│   │   ├── basic-programs.md        # Fundamental program structures
│   │   ├── advanced-programs.md     # Complex program architectures
│   │   ├── program-library.py       # Python implementations
│   │   └── program-examples.ipynb   # Interactive examples
│   │
│   ├── cognitive-schemas/           # Knowledge representations
│   │   ├── user-schemas.md          # User information schemas
│   │   ├── domain-schemas.md        # Domain knowledge schemas
│   │   ├── task-schemas.md          # Reasoning task schemas
│   │   └── schema-library.yaml      # Reusable schema library
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems
│   │   ├── solver-architecture.md   # Problem-solving systems
│   │   ├── tutor-architecture.md    # Educational systems
│   │   ├── research-architecture.md # Information synthesis
│   │   └── architecture-examples.py # Implementation examples
│   │
│   └── integration/                 # Integration patterns
│       ├── with-rag.md              # Integration with retrieval
│       ├── with-memory.md           # Integration with memory
│       ├── with-agents.md           # Integration with agents
│       └── evaluation-metrics.md    # Effectiveness measurement
│
└── .github/                         # GitHub configuration
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── workflows/ci.yml             # CI pipeline configuration
    ├── workflows/eval.yml           # Evaluation automation
    └── workflows/protocol_tests.yml # Protocol testing
```
> 图：仓库目录树 —— 各模块及其职责说明

---

## 7. 如何贡献

在 `50_contrib/` 中提交 PR。  
清单在 `40_reference/eval_checklist.md`——提交前请跑一遍。

贡献时：
1. 遵循 Karpathy 风格准则
2. 附上可运行的代码示例
3. 测量词元用量与性能
4. 保持生物隐喻的一致性
5. 为任何新功能添加测试

---

## 8. 许可与致谢

MIT。不设门槛：复制、混搭、再分发均可。  
感谢 Andrej Karpathy 提出这一框架表述。  
研究方面的致谢见 CITATIONS.md。  
所有错误由我们承担；欢迎改进。
