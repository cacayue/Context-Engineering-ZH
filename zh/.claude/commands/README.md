---
title: 上下文工程 AgenticOS 命令集
source: .claude/commands/README.md
module: M6
task: M6-05
chunks: 2
chunks_done: [1, 2]
status: published
source_sha256: e2bf151fff6c1a7194c2997ff4757e24fd1454f994b8d16cadfc0768633b5982
---

> 原文：[.claude/commands/README.md](../../../.claude/commands/README.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 上下文工程（Context Engineering）AgenticOS

> 「我们塑造工具，此后工具又塑造我们。」—— [马歇尔·麦克卢汉](https://www.goodreads.com/quotes/350791-we-become-what-we-behold-we-shape-our-tools-and)


## [Anthropic 斜杠命令](https://docs.anthropic.com/en/docs/claude-code/slash-commands) | [子智能体](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
## 概述

本目录收录了一个持续扩充的智能体（agent）与执行框架库。这些组件以斜杠命令的形式嵌入，具备模块化、可定制和可扩展的特性，共同构成智能体操作系统（AgenticOS），旨在增强 [Claude Code](https://www.anthropic.com/claude-code) 以及其他前沿系统的能力，例如 [OpenCode](https://opencode.ai/)、[Amp](https://sourcegraph.com/amp)、[Kiro](https://kiro.dev/)、[Codex](https://openai.com/codex/)、[Gemini CLI](https://github.com/google-gemini/gemini-cli) 等。每个智能体都采用结构一致的标准化工作流，支持在不同领域开展复杂的上下文工程。

该操作系统提供了一系列智能体，作为上下文驱动的 AI 工作流的支架，利用认知工具（cognitive tool）、神经场理论、符号机制和量子语义学的最新研究，构建能力更强、可解释性更高、行为更可预测的 AI 交互。

```
/command Q="query" param="value" context=@file.md ...
      │
      ▼
[context]→[specialized_phase_1]→[specialized_phase_2]→...→[synthesis]→[audit/log]
        ↑___________________feedback/CI___________________|
```
> 图：命令工作流及反馈路径 —— context → synthesis → audit/log

## AgenticOS 库（建设中）

| 命令 | 用途 | 用法示例 |
|---------|---------|---------------|
| [`alignment.agent.md`](./alignment.agent.md) | AI 安全与对齐评估 | `/alignment Q="prompt injection" model="claude-3"` |
| [`cli.agent.md`](./cli.agent.md) | 终端工作流自动化 | `/cli "find all .log files" alias=logscan` |
| [`comms.agent.md`](./comms.agent.md) | 利益相关方沟通 | `/comms Q="major outage" audience="internal" type="crisis"` |
| [`data.agent.md`](./data.agent.md) | 数据转换与验证 | `/data input="data.csv" op="validate" schema=@schema.json` |
| [`deploy.agent.md`](./deploy.agent.md) | 部署自动化 | `/deploy target="app" env="staging" version="1.2.0"` |
| [`diligence.agent.md`](./diligence.agent.md) | 尽职调查工作流 | `/diligence target="acquisition" scope="tech" depth="full"` |
| [`doc.agent.md`](./doc.agent.md) | 文档生成 | `/doc target="api" format="markdown" scope="public"` |
| [`legal.agent.md`](./legal.agent.md) | 法律研究与分析 | `/legal Q="contract review" jurisdiction="US" type="SaaS"` |
| [`lit.agent.md`](./lit.agent.md) | 文献综述与写作 | `/literature Q="PEMF effect" type="review" years=3` |
| [`marketing.agent.md`](./marketing.agent.md) | 营销策略与活动 | `/marketing goal="lead gen" channel="email" vertical="SaaS"` |
| [`meta.agent.md`](./meta.agent.md) | 元层级智能体协调 | `/meta agents="research,data" task="market analysis"` |
| [`monitor.agent.md`](./monitor.agent.md) | 系统与服务监控 | `/monitor service="api" period="24h" alert=true` |
| [`optimize.agent.md`](./optimize.agent.md) | 代码与流程优化 | `/optimize target="foo.py" area="speed" mode="aggressive"` |
| [`research.agent.md`](./research.agent.md) | 研究工作流 | `/research topic="quantum computing" depth="technical"` |
| [`security.agent.md`](./security.agent.md) | 安全分析 | `/security target="app" scope="full" report="detailed"` |
| [`test.agent.md`](./test.agent.md) | 测试生成与执行 | `/test suite="integration" mutate=true report=summary"` |

## 命令结构

每个命令智能体都遵循标准化的系统提示词（prompt）格式，包含以下关键组件：

```
/command.agent.md
├── [meta]            # Protocol version, runtime, namespaces
├── [instructions]    # Agent rules, invocation, argument mapping
├── [ascii_diagrams]  # File tree, workflow, phase flow
├── [context_schema]  # JSON/YAML: domain-specific fields
├── [workflow]        # YAML: specialized workflow phases
├── [tools]           # YAML: tool registry & control
├── [recursion]       # Python: feedback/revision loop
└── [examples]        # Markdown: sample runs, logs, usage
```
> 图：命令智能体文件的组成 —— /command.agent.md

### 元信息部分

元信息部分定义协议兼容性和运行时参数：

```json
{
  "agent_protocol_version": "2.0.0",
  "prompt_style": "multimodal-markdown",
  "intended_runtime": ["Anthropic Claude", "OpenAI GPT-4o", "Agentic System"],
  "schema_compatibility": ["json", "yaml", "markdown", "python", "shell"],
  "namespaces": ["project", "user", "team", "field"],
  "audit_log": true,
  "last_updated": "2025-07-10",
  "prompt_goal": "Purpose statement for the command harness"
}
```

### 工作流阶段

每个命令都实现了领域特定的工作流阶段，以系统化地处理输入并生成输出：

```yaml
phases:
  - context_mapping:
      description: |
        Parse input arguments, clarify goals, establish context.
      output: Context table, argument log, clarifications.
  
  - domain_specific_phase_1:
      description: |
        Specialized processing for the domain.
      output: Domain-specific artifacts and logs.
  
  - domain_specific_phase_2:
      description: |
        Additional domain processing.
      output: Secondary artifacts and analysis.
  
  - synthesis_phase:
      description: |
        Integrate findings and generate recommendations.
      output: Synthesis report, action items, open questions.
  
  - audit_logging:
      description: |
        Document process, decisions, and version history.
      output: Audit log, version history, unresolved issues.
```

### 工具注册表

命令为每个阶段显式声明工具访问权限：

```yaml
tools:
  - id: domain_specific_tool
    type: internal
    description: Tool purpose and functionality.
    input_schema: { param1: string, param2: string }
    output_schema: { result: list, metadata: dict }
    call: { protocol: /tool.function{ param1=<param1>, param2=<param2> } }
    phases: [domain_specific_phase_1, domain_specific_phase_2]
    examples: [{ input: {...}, output: {...} }]
  - id: github_issue
    type: external
    description: Create or update issues in a GitHub repo for agent workflow failures or meta-level tracking.
    input_schema: { repo: string, title: string, body: string }
    output_schema: { issue_url: string, status: string }
    endpoint: "https://api.github.com/repos/{repo}/issues"
    auth: "api_token"
    call: { protocol: /call_api{ endpoint=<endpoint>, params={repo, title, body} } }
    phases: [error_feedback_handling, audit_meta_logging]
    examples:
      - input: { repo: "team/agent-infra", title: "Meta-agent error", body: "Dependency loop detected" }
        output: { issue_url: "https://github.com/team/agent-infra/issues/45", status: "created" }
```

### 递归回路

命令通过反馈回路（feedback loop）实现递归自我改进：

```python
def agent_cycle(context, state=None, audit_log=None, depth=0, max_depth=4):
    # Execute each phase sequentially
    for phase in workflow_phases:
        state[phase] = run_phase(phase, context, state)
    
    # Check if revision is needed and recurse if appropriate
    if depth < max_depth and needs_revision(state):
        revised_context, reason = query_for_revision(context, state)
        audit_log.append({'revision': phase, 'reason': reason, 'timestamp': get_time()})
        return agent_cycle(revised_context, state, audit_log, depth + 1, max_depth)
    else:
        state['audit_log'] = audit_log
        return state
```

## 使用模式

### 基本调用

命令采用带命名参数的斜杠命令模式：

```bash
/command Q="main question" param1="value1" param2="value2"
```

### 文件引用

使用 `@` 前缀将文件内容纳入命令：

```bash
/legal Q="contract review" context=@agreement.md
```

### Bash 命令集成

使用 `!` 前缀执行 Bash 命令，并纳入其输出：

```
/cli "commit changes" context="!git status"
```

## 理论基础

AgenticOS 将上下文工程框架中的若干关键概念付诸实践：

### 渐进复杂度范式

```
atoms → molecules → cells → organs → neural systems → neural fields
  │        │         │        │             │              │
single    few-     memory/   multi-    cognitive tools   fields +
prompt    shot     agents    agents    prompt programs   persistence
```
> 图：从原子到神经场的渐进复杂度层级 —— atoms → molecules → cells → organs → neural systems → neural fields

### 涌现符号机制（普林斯顿大学，ICML，2025）

三阶段符号处理架构：

1. **符号抽象头（早期层）** - 将词元（token）转换为抽象变量
2. **符号归纳头（中间层）** - 对抽象变量进行序列归纳
3. **检索头（后期层）** - 检索与抽象变量关联的值，预测下一个词元

### 认知工具架构（IBM 苏黎世，2025）

封装推理操作的结构化提示词模板：

```python
def cognitive_tool_template():
    """IBM Zurich cognitive tool structure"""
    return {
        "understand": "Identify main concepts and requirements",
        "extract": "Extract relevant information from context", 
        "highlight": "Identify key properties and relationships",
        "apply": "Apply appropriate reasoning techniques",
        "validate": "Verify reasoning steps and conclusions"
    }
```

### 量子语义框架（印第安纳大学，2025）

一种依赖观察者的意义实现框架，其中语义解释通过表达与解释性上下文之间的动态交互而涌现。

## 与 Claude Code CLI 集成

这些命令遵循 Anthropic 的[斜杠命令文档](https://docs.anthropic.com/en/docs/claude-code/slash-commands)，可与 Claude Code CLI 无缝协作。

主要特性：
- 通过标准化接口**执行自定义命令**
- 通过子目录实现**命名空间划分**（例如 `/domain:command`）
- 通过 `$ARGUMENTS` 占位符传递**参数**
- 使用 `!` 前缀实现 **Bash 集成**
- 使用 `@` 前缀实现**文件引用**

## 创建自定义命令

创建自己的命令智能体：

1. 从本目录中**复制现有模板**
2. 根据使用场景**修改领域特定部分**
3. **定义专门的工作流阶段**，使其适合所处领域
4. 为每个阶段**注册适当的工具**
5. **提供实用示例**并加入审计日志

遵循以下命名约定：
- 项目专用命令：`.claude/commands/your-command.agent.md`
- 个人命令：`~/.claude/commands/your-command.agent.md`

## 实施策略

这些命令遵循以下关键原则：

1. **分层方法** - 从基础构建逐步走向高级集成
2. **注重实践** - 确保理论得到实际实现
3. **模块化设计** - 创建可组合、可重组的组件
4. **渐进复杂度** - 从简单入手，逐步增加复杂性
5. **强调集成** - 关注组件之间的交互
6. **自我改进** - 构建能够提升自身能力的系统
7. **透明性** - 尽管系统复杂，仍保持可理解性
8. **协作** - 为高效的人类与 AI 合作而设计
9. **模态灵活性** - 支持跨模态的统一理解

## 高级模式

### 场论动力学

命令可以实现吸引子动力学（attractor dynamics）与场共振（field resonance）：

```python
def attractor_field_dynamics():
    """Shanghai AI Lab field theory framework"""
    return {
        "attractor_detection": {
            "identify_basins": "Map stable behavioral patterns",
            "measure_depth": "Quantify attractor strength",
            "track_evolution": "Monitor attractor development"
        },
        "field_resonance": {
            "resonance_patterns": "Identify coherent field oscillations",
            "coupling_strength": "Measure component interactions",
            "phase_relationships": "Track synchronization patterns"
        },
        "symbolic_residue": {
            "residue_tracking": "Monitor persistent information",
            "decay_analysis": "Study information degradation",
            "transfer_mechanisms": "Understand residue propagation"
        }
    }
```

### 记忆与推理协同

命令可以将记忆（memory）巩固与推理相结合：

```python
def mem1_consolidation():
    """Singapore-MIT MEM1 memory-reasoning synergy"""
    return {
        "analysis_stage": {
            "interaction_patterns": "Analyze memory-reasoning interactions",
            "efficiency_metrics": "Measure memory utilization",
            "bottleneck_identification": "Find performance constraints"
        },
        "consolidation_stage": {
            "selective_compression": "Compress low-value information",
            "insight_extraction": "Extract high-value patterns",
            "relationship_mapping": "Map memory element relationships"
        },
        "optimization_stage": {
            "memory_pruning": "Remove redundant information",
            "reasoning_acceleration": "Optimize for reasoning speed",
            "synergy_enhancement": "Improve memory-reasoning integration"
        }
    }
```

## 贡献指南

创建新的命令智能体时：

1. 遵循既定的结构模式
2. 提供全面的文档和示例
3. 实现适当的审计日志与版本管理
4. 在不同运行时环境中进行测试
5. 考虑与现有命令的集成

## 未来方向

本目录将扩展，纳入以下内容：
- 更多领域特定的命令智能体
- 与外部工具和 API 更深入的集成
- 更完善的反馈与递归改进机制
- 跨命令协调框架
- 更先进的场论与量子语义实现
- 支持系统级涌现的元递归框架

---

*有关上下文工程概念与实现的更多信息，请参阅[上下文工程主仓库](https://github.com/davidkimai/Context-Engineering)。*
