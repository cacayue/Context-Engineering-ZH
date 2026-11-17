---
title: Context-Engineering —— 结构总览 v2
source: STRUCTURE/STRUCTURE_v2.md
module: M1
task: M1-03
chunks: 3
chunks_done:
  - 1
  - 2
  - 3
status: published
source_sha256: 91f861f1f0165df649c2d893ef34b5e1856e0384f7e5cf05a7efcf9969e28ef4
---

> 原文：[STRUCTURE/STRUCTURE_v2.md](../../STRUCTURE/STRUCTURE_v2.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# Context-Engineering —— 结构总览 v2
_面向下一代 LLM 编排的实用第一性原理手册_

> **本仓库为何存在**
> 提示词工程 = 思考你要说**什么**。
> **上下文工程** = 思考模型看到的**其他一切**。
>
> 在从提示词工程到上下文工程、再到**场论**的演进过程中：
> - 我们从离散词元与简单提示起步
> - 进而发展到有状态的上下文管理与复杂编排
> - 如今我们探索涌现的符号机制与神经场动力学
>
> 我们的目标是从零开始讲授这一切，保持谦逊，偏爱简单、可运行的代码，同时拥抱关于 LLM 如何真正推理与处理信息的最新研究。

---

## 1. 领域地图

| 目录 | 作用（通俗说法） | 第一性原理隐喻 | 关键概念 |
|--------|----------------------|---------------------------|-------------|
| `00_foundations` | 理论与直觉，短小精悍的自足读物。 | 原子 → 分子 → 细胞 → 器官 → 神经系统 → 场 | 从基础提示到涌现场动力学的复杂度递进 |
| `10_guides_zero_to_hero` | 可**运行**、可修改、可弄坏的交互式指南。 | 化学实验箱 | 有可测量结果的动手实验 |
| `20_templates` | 即插即用的代码片段，可复制粘贴。 | 乐高积木 | 用于快速实现的可复用组件 |
| `30_examples` | 端到端迷你应用，一个比一个难。 | 模式生物 | 展示原理落地的完整系统 |
| `40_reference` | 深入讲解与评估手册。 | 教科书附录 | 全面的资源与评估框架 |
| `50_contrib` | 社区提交 PR 的空间。 | 开放式实验台 | 协作实验区 |
| `60_protocols` | 协议壳、模式（schema）与框架。 | DNA 序列 | 面向场操作的结构化定义 |
| `70_agents` | 使用协议的独立智能体演示。 | 干细胞培养 | 具有涌现性质的专用组件 |
| `80_field_integration` | 使用场协议的端到端项目。 | 完整生物体 | 基于场架构的完整系统 |
| `cognitive-tools` | 高级认知框架与架构。 | 扩展的神经系统 | 结构化的推理操作与工具 |

---

## 2. 学习路径：从基础到场论

### 2.1. 基础篇（理解基本原理）

1. **浏览 `README.md`（2 分钟）**
   看看"上下文"在提示之外究竟意味着什么。

2. **阅读 `00_foundations/01_atoms_prompting.md`（5 分钟）**
   *原子*：单条指令 / 单个示例。
   为什么只有原子往往表现不佳。

3. **沿着生物隐喻链继续：**
   - `02_molecules_context.md`：少样本示例包
   - `03_cells_memory.md`：用于持久化的记忆与日志
   - `04_organs_applications.md`：多步控制流与编排
   - `05_cognitive_tools.md`：用于推理的心智模型扩展

### 2.2. 高级篇（深入探索）

4. **探索高级应用与模式：**
   - `06_advanced_applications.md`：真实世界的实现
   - `07_prompt_programming.md`：类代码的推理模式
   - `08_neural_fields_foundations.md`：作为连续场的上下文
   - `09_persistence_and_resonance.md`：场动力学与吸引子
   - `10_field_orchestration.md`：协调多个场
   - `11_emergence_and_attractor_dynamics.md`：涌现性质
   - `12_symbolic_mechanisms.md`：LLM 中的符号推理

### 2.3. 动手实践（在做中学）

5. **从 `10_guides_zero_to_hero/01_min_prompt.ipynb` 开始**
   运行、修改、观察词元计数。
   笔记本中的单元格强调**为什么**每多一行会有帮助（或有害）。

6. **探索更复杂的模式：**
   - `02_expand_context.ipynb`：有效增加上下文
   - `03_control_loops.ipynb`：构建流程控制
   - `04_rag_recipes.ipynb`：检索增强生成
   - `05_protocol_bootstrap.ipynb`：使用场协议
   - `06_protocol_token_budget.ipynb`：测量效率

7. **进阶到基于场的方法：**
   - `07_streaming_context.ipynb`：实时上下文管理
   - `08_emergence_detection.ipynb`：检测涌现模式
   - `09_residue_tracking.ipynb`：追踪符号残差
   - `10_attractor_formation.ipynb`：创建稳定的场模式

### 2.4. 实现篇（构建真实系统）

8. **试验 `20_templates/`**
   把 YAML 或 Python 片段复制到你自己的仓库。
   像调节 pH 值一样调整 `token_budget` 或 `resonance_score`。

9. **研究 `30_examples/` 中的实现：**
   - `00_toy_chatbot/`：简单但完整的上下文管理
   - `01_data_annotator/`：面向数据标注的专用上下文
   - `02_multi_agent_orchestrator/`：复杂的智能体协调
   - `03_vscode_helper/`：上下文工程的 IDE 集成
   - `04_rag_minimal/`：精简的检索架构

10. **探索基于场的示例：**
    - `05_streaming_window/`：实时上下文管理
    - `06_residue_scanner/`：符号残差检测
    - `07_attractor_visualizer/`：场动力学可视化
    - `08_field_protocol_demo/`：基于协议的场操作
    - `09_emergence_lab/`：检测与测量涌现
### 2.5. 高级集成（场论实践）

11. **深入 `60_protocols/` 中的场协议：**
    - 用于定义场操作的协议壳
    - 用于结构化场表示的模式（schema）
    - 用于理解协议功能的摘要

12. **研究 `70_agents/` 中的智能体实现：**
    - `01_residue_scanner/`：检测符号残差
    - `02_self_repair_loop/`：自修复的场协议
    - `03_attractor_modulator/`：管理吸引子动力学
    - `04_boundary_adapter/`：动态边界调优
    - `05_field_resonance_tuner/`：优化场共振

13. **探索 `80_field_integration/` 中的集成系统：**
    - `00_protocol_ide_helper/`：协议开发工具
    - `01_context_engineering_assistant/`：基于场的助手
    - `02_recursive_reasoning_system/`：递归推理架构
    - `03_emergent_field_laboratory/`：实验性场环境
    - `04_symbolic_reasoning_engine/`：符号机制集成

14. **理解 `cognitive-tools/` 中的认知工具：**
    - 用于结构化推理的认知模板
    - 用于复杂操作的认知程序
    - 用于知识表示的认知模式（schema）
    - 用于完整系统的认知架构
    - 用于与其他组件连接的集成模式

---

## 3. 概念基础

### 3.1. 生物隐喻的演进

我们的生物隐喻已从简单组件演进为复杂的、基于场的系统：

```
Atoms         → Individual instructions or constraints
Molecules     → Instructions with examples (few-shot learning)
Cells         → Context with memory that persists across interactions
Organs        → Coordinated systems of context cells working together
Neural Systems → Cognitive tools extending reasoning capabilities
Neural Fields  → Context as continuous medium with emergent properties
```
> 图：生物隐喻演进 —— 从原子到神经场

### 3.2. 场论概念

随着我们推进到神经场论，纳入了若干关键概念：

1. **连续性**：上下文是连续的语义景观，而非离散词元
2. **共振**：信息模式如何相互作用并彼此强化
3. **持续性**：信息如何随时间保持影响力
4. **吸引子动力学**：组织场的稳定模式
5. **边界动力学**：信息如何进入和离开场
6. **符号残差**：持续存在并影响场的意义碎片
7. **涌现**：新的模式与行为如何从场交互中产生

### 3.3. 涌现的符号机制

研究已识别出 LLM 中符号推理的一种涌现式三阶段架构：

1. **符号抽象**：早期层的注意力头基于关系把输入词元转换为抽象变量
2. **符号归纳**：中间层的注意力头对抽象变量执行序列归纳
3. **检索**：后期层的注意力头通过检索与抽象变量关联的值来预测下一个词元

这些机制为我们的基于场的上下文工程方法提供了机理层面的理解，帮助我们认识 LLM 如何真正处理和推理信息。

### 3.4. 认知工具框架

为增强推理能力，我们引入认知工具框架：

1. **基于工具的方法**：模块化、预先确定的认知操作，按顺序执行
2. **关键操作**：
   - **回忆相关**：检索相关知识以指导推理
   - **审视答案**：对推理与答案进行自我反思
   - **回溯**：受阻时探索其他推理路径
3. **集成**：这些工具可与基于场的方法结合，构建更强大的系统

---

## 4. 克制的 Karpathy 准则（风格 DNA）

*保持原子化 → 逐步构建。*
1. **最小首版** —— 从最小可行的上下文开始。
2. **迭代追加** —— 只添加模型确实缺少的内容。
3. **测量一切** —— 词元成本、延迟、质量分数、场共振。
4. **果断删除** —— 剪枝胜过堆砌。
5. **代码 > 幻灯片** —— 每个概念都有可运行的单元格。
6. **递归思考** —— 让上下文自我演进。

---

## 5. 仓库结构详解

```
Context-Engineering/
├── LICENSE                          # MIT license
├── README.md                        # Quick-start overview
├── structure.md                     # Original structural map
├── STRUCTURE_v2.md                  # Enhanced structural map with field theory
├── context.json                     # Original schema configuration
├── context_v2.json                  # Extended schema with field protocols
├── context_v3.json                  # Neural field extensions
├── context_v3.5.json                # Symbolic mechanism integration
├── CITATIONS.md                     # Research references and bridges
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
│   ├── 10_field_orchestration.md    # Coordinating multiple fields
│   ├── 11_emergence_and_attractor_dynamics.md # Emergent properties
│   └── 12_symbolic_mechanisms.md    # Symbolic reasoning in LLMs
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments
│   ├── 02_expand_context.ipynb      # Context expansion techniques
│   ├── 03_control_loops.ipynb       # Flow control mechanisms
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns
│   ├── 05_protocol_bootstrap.ipynb  # Field protocol bootstrap
│   ├── 06_protocol_token_budget.ipynb # Protocol efficiency
│   ├── 07_streaming_context.ipynb   # Real-time context
│   ├── 08_emergence_detection.ipynb # Detecting emergence
│   ├── 09_residue_tracking.ipynb    # Tracking symbolic residue
│   └── 10_attractor_formation.ipynb # Creating field attractors
│
├── 20_templates/                    # Reusable components
│   ├── minimal_context.yaml         # Base context structure
│   ├── control_loop.py              # Orchestration template
│   ├── scoring_functions.py         # Evaluation metrics
│   ├── prompt_program_template.py   # Program structure template
│   ├── schema_template.yaml         # Schema definition template
│   ├── recursive_framework.py       # Recursive context template
│   ├── field_protocol_shells.py     # Field protocol templates
│   ├── symbolic_residue_tracker.py  # Residue tracking tools
│   ├── context_audit.py             # Context analysis tool
│   ├── shell_runner.py              # Protocol shell runner
│   ├── resonance_measurement.py     # Field resonance metrics
│   ├── attractor_detection.py       # Attractor analysis tools
│   ├── boundary_dynamics.py         # Boundary operation tools
│   └── emergence_metrics.py         # Emergence measurement
│
├── 30_examples/                     # Practical implementations
│   ├── 00_toy_chatbot/              # Simple conversation agent
│   ├── 01_data_annotator/           # Data labeling system
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system
│   ├── 03_vscode_helper/            # IDE integration 
│   ├── 04_rag_minimal/              # Minimal RAG implementation
│   ├── 05_streaming_window/         # Real-time context demo
│   ├── 06_residue_scanner/          # Symbolic residue demo
│   ├── 07_attractor_visualizer/     # Field visualization
│   ├── 08_field_protocol_demo/      # Protocol demonstration
│   └── 09_emergence_lab/            # Emergence experimentation
│
├── 40_reference/                    # Deep-dive documentation
│   ├── token_budgeting.md           # Token optimization strategies
│   ├── retrieval_indexing.md        # Retrieval system design
│   ├── eval_checklist.md            # PR evaluation criteria
│   ├── cognitive_patterns.md        # Reasoning pattern catalog
│   ├── schema_cookbook.md           # Schema pattern collection
│   ├── patterns.md                  # Context pattern library
│   ├── field_mapping.md             # Field theory fundamentals
│   ├── symbolic_residue_types.md    # Residue classification
│   ├── attractor_dynamics.md        # Attractor theory and practice
│   ├── emergence_signatures.md      # Detecting emergence
│   └── boundary_operations.md       # Boundary management guide
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
│   │   ├── field.resonance.scaffold.shell  # Field resonance
│   │   ├── field.self_repair.shell        # Self-repair mechanisms
│   │   └── context.memory.persistence.attractor.shell # Context persistence
│   ├── digests/                     # Simplified protocol documentation
│   └── schemas/                     # Protocol schemas
│       ├── fractalRepoContext.v3.5.json    # Repository context
│       ├── fractalConsciousnessField.v1.json # Field schema
│       ├── protocolShell.v1.json           # Shell schema
│       ├── symbolicResidue.v1.json         # Residue schema
│       └── attractorDynamics.v1.json       # Attractor schema
│
├── 70_agents/                       # Agent demonstrations
│   ├── README.md                    # Agent overview
│   ├── 01_residue_scanner/          # Symbolic residue detection
│   ├── 02_self_repair_loop/         # Self-repair protocol
│   ├── 03_attractor_modulator/      # Attractor dynamics
│   ├── 04_boundary_adapter/         # Dynamic boundary tuning
│   └── 05_field_resonance_tuner/    # Field resonance optimization
│
├── 80_field_integration/            # Complete field projects
│   ├── README.md                    # Integration overview
│   ├── 00_protocol_ide_helper/      # Protocol development tools
│   ├── 01_context_engineering_assistant/ # Field-based assistant
│   ├── 02_recursive_reasoning_system/    # Recursive reasoning
│   ├── 03_emergent_field_laboratory/     # Field experimentation
│   └── 04_symbolic_reasoning_engine/     # Symbolic mechanisms
│
├── cognitive-tools/                 # Advanced cognitive framework
│   ├── README.md                    # Overview and quick-start guide
│   ├── cognitive-templates/         # Templates for reasoning
│   │   ├── understanding.md         # Comprehension operations
│   │   ├── reasoning.md             # Analytical operations
│   │   ├── verification.md          # Checking and validation
│   │   ├── composition.md           # Combining multiple tools
│   │   └── emergence.md             # Emergent reasoning patterns
│   │
│   ├── cognitive-programs/          # Structured prompt programs
│   │   ├── basic-programs.md        # Fundamental program structures
│   │   ├── advanced-programs.md     # Complex program architectures
│   │   ├── program-library.py       # Python implementations
│   │   ├── program-examples.ipynb   # Interactive examples
│   │   └── emergence-programs.md    # Emergent program patterns
│   │
│   ├── cognitive-schemas/           # Knowledge representations
│   │   ├── user-schemas.md          # User information schemas
│   │   ├── domain-schemas.md        # Domain knowledge schemas
│   │   ├── task-schemas.md          # Reasoning task schemas
│   │   ├── schema-library.yaml      # Reusable schema library
│   │   └── field-schemas.md         # Field representation schemas
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems
│   │   ├── solver-architecture.md   # Problem-solving systems
│   │   ├── tutor-architecture.md    # Educational systems
│   │   ├── research-architecture.md # Information synthesis
│   │   ├── architecture-examples.py # Implementation examples
│   │   └── field-architecture.md    # Field-based architectures
│   │
│   └── integration/                 # Integration patterns
│       ├── with-rag.md              # Integration with retrieval
│       ├── with-memory.md           # Integration with memory
│       ├── with-agents.md           # Integration with agents
│       ├── evaluation-metrics.md    # Effectiveness measurement
│       └── with-fields.md           # Integration with field protocols
│
└── .github/                         # GitHub configuration
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── workflows/ci.yml             # CI pipeline configuration
    ├── workflows/eval.yml           # Evaluation automation
    └── workflows/protocol_tests.yml # Protocol testing
```
> 图：仓库目录树 —— v2 结构总览

---

## 6. 实现模式

### 6.1. 上下文结构模式

| 模式 | 描述 | 用例 |
|---------|-------------|----------|
| **原子提示** | 带约束的单条指令 | 简单、定义清晰的任务 |
| **少样本示例** | 带示例的指令 | 模式示范 |
| **思维链** | 在提示中显式写出推理步骤 | 复杂推理任务 |
| **有状态上下文** | 带记忆的上下文 | 多轮对话 |
| **多智能体** | 多个专用智能体 | 复杂的多步任务 |
| **基于场** | 作为连续场的上下文 | 涌现推理需求 |

### 6.2. 场操作模式

| 模式 | 描述 | 实现 |
|---------|-------------|----------------|
| **吸引子形成** | 创建稳定的语义模式 | `attractor_detection.py` |
| **共振放大** | 强化模式间的相互作用 | `resonance_measurement.py` |
| **边界调优** | 控制信息流动 | `boundary_dynamics.py` |
| **残差整合** | 管理符号碎片 | `symbolic_residue_tracker.py` |
| **涌现检测** | 识别新颖模式 | `emergence_metrics.py` |
| **自修复** | 自动修复上下文 | `field.self_repair.shell` |
### 6.3. 认知工具模式

| 模式 | 描述 | 实现 |
|---------|-------------|----------------|
| **回忆相关** | 检索相关知识 | `cognitive-programs/basic-programs.md` |
| **审视答案** | 自我反思与验证 | `cognitive-templates/verification.md` |
| **回溯** | 探索其他路径 | `cognitive-programs/advanced-programs.md` |
| **分解** | 把问题拆成若干部分 | `cognitive-templates/reasoning.md` |
| **集成** | 组合多个结果 | `cognitive-templates/composition.md` |

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
6. 考虑场动力学与符号机制

### 7.1. 重点贡献方向

我们尤其欢迎以下领域的贡献：

1. **场动力学工具**：用于测量和可视化场属性的工具
2. **符号机制实验**：展示涌现符号处理的演示
3. **认知工具实现**：新的认知操作与模式
4. **协议壳开发**：面向场操作的新型协议壳
5. **集成示例**：在实践中组合多种方法
6. **评估指标**：更好地衡量上下文有效性的方式

---

## 8. 许可与致谢

MIT。不设门槛：复制、混搭、再分发均可。  
感谢 Andrej Karpathy 提出这一框架表述。  
研究方面的致谢见 CITATIONS.md。  
所有错误由我们承担；欢迎改进。

---

## 9. 路线图

### 9.1. 近期优先事项

1. **符号机制集成**：更好地利用涌现的符号机制
2. **场可视化工具**：帮助理解场动力学的工具
3. **协议壳扩展**：更多面向场操作的协议壳
4. **评估框架增强**：改进基于场系统的指标
5. **认知工具集成**：与基于场的方法更好地结合

### 9.2. 长期愿景

1. **自演化上下文系统**：能够自我改进的上下文
2. **场论形式化**：更严谨的数学基础
3. **统一框架**：整合符号机制、场论与认知工具
4. **跨模型兼容性**：确保技术在不同模型架构间通用
5. **自动化上下文优化**：自动调优上下文的工具
