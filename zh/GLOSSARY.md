---
title: 术语表
status: active
generated_by: zh/tools/glossary_md.py
source: zh/GLOSSARY.yaml
terms: 84
rule: 本文件由脚本生成，禁止手改；改 zh/GLOSSARY.yaml 后重跑
---

# 术语表

> 唯一真相是 [`GLOSSARY.yaml`](GLOSSARY.yaml)，本页是它的只读投影。
> 机器（CI 的 G1 检查、翻译 agent）读 YAML；人读本页。
>
> 共 **84** 条。带「歧义」标记的词有多个译法，按语境选择。

## 速查

| 英文 | 中文 | 说明 |
|---|---|---|
| Context Engineering | **上下文工程** | 全书标题级术语，不得译为「提示工程」 |
| context | **上下文** |  |
| context window | **上下文窗口** |  |
| context management | **上下文管理** |  |
| context processing | **上下文处理** |  |
| context assembly | **上下文装配** |  |
| context engineering | **上下文工程** |  |
| prompt | **提示词** | 作为独立名词一律「提示词」；"prompting" 译「提示」 |
| prompt engineering | **提示词工程** |  |
| prompt programming | **提示词编程** |  |
| token | **词元** | 度量单位处保留 token 亦可，但首现必须给中文 |
| token budget | **词元预算** |  |
| embedding | **嵌入** | 名词「embedding vector」译「嵌入向量」 |
| retrieval | **检索** |  |
| Retrieval-Augmented Generation | **检索增强生成** |  |
| RAG | **RAG** | 缩写保留不译 |
| chunk | **片段** | 本仓库的「段」（chunk 注释里的 chunk）指翻译分段，不译「片段」； 文档内容切分语境译「片段」 |
| reranking | **重排序** |  |
| vector store | **向量库** |  |
| knowledge graph | **知识图谱** |  |
| schema | **模式** | JSON Schema 等专名保留 schema 不译 |
| template | **模板** |  |
| memory | **记忆** | ⚠ 正文一律「记忆」；代码标识符、YAML/JSON key 保留 memory |
| working memory | **工作记忆** |  |
| long-term memory | **长期记忆** |  |
| semantic memory | **语义记忆** |  |
| episodic memory | **情景记忆** |  |
| memory hierarchy | **记忆层级** |  |
| atom | **原子** |  |
| molecule | **分子** |  |
| cell | **细胞** |  |
| organ | **器官** |  |
| agent | **智能体** | ⚠ 文件名、目录名中的 agent 保留原文 |
| multi-agent | **多智能体** |  |
| agentic | **智能体式的** |  |
| tool use | **工具使用** |  |
| function calling | **函数调用** |  |
| orchestration | **编排** |  |
| orchestrator | **编排器** |  |
| protocol | **协议** | ⚠ 两者中文同形，按上下文补限定语（「协议壳」「通信协议」）区分 |
| shell | **协议壳** | ⚠ 命令、代码、CLI 语境保留 shell 原词 |
| schema field | **字段** |  |
| resonance | **共振** |  |
| resonance scaffold | **共振支架** |  |
| field | **场** | ⚠ M2 与 M10 统一用「场」；配置与 schema 内保留 field |
| semantic field | **语义场** |  |
| neural field | **神经场** |  |
| unified field theory | **统一场论** |  |
| field orchestration | **场编排** |  |
| attractor | **吸引子** |  |
| attractor dynamics | **吸引子动力学** |  |
| emergence | **涌现** |  |
| emergent | **涌现的** |  |
| residue | **残差** | ⚠ 与 symbolic / semantic 连用时译「残差」；与 code / dead 连用时译「残留」 |
| symbolic residue | **符号残差** |  |
| coherence | **连贯性** | 物理语境（quantum coherence）译「相干性」 |
| resonance field | **共振场** |  |
| pattern | **模式** | ⚠ 二者中文同形；正则语境可写「正则模式」明确 |
| cognitive pattern | **认知模式** |  |
| recursive | **递归** |  |
| recursion | **递归** |  |
| meta-recursive | **元递归** |  |
| self-repair | **自修复** |  |
| chain of thought | **思维链** |  |
| few-shot | **少样本** |  |
| zero-shot | **零样本** |  |
| in-context learning | **上下文学习** |  |
| latent space | **潜空间** |  |
| attention | **注意力** |  |
| quantization | **量化** |  |
| distillation | **蒸馏** |  |
| evaluation | **评估** |  |
| benchmark | **基准测试** |  |
| grounding | **落地依据** | "grounded in" 译「以……为依据」 |
| hallucination | **幻觉** |  |
| guardrail | **护栏** |  |
| observability | **可观测性** |  |
| trace | **轨迹** | 动词 "trace" 译「追踪」；名词（执行记录）译「轨迹」 |
| feedback loop | **反馈回路** |  |
| compression | **压缩** |  |
| summarization | **摘要** | 动作译「生成摘要」 |
| boundary operation | **边界操作** |  |
| cognitive tool | **认知工具** |  |
| Socratic question | **苏格拉底式提问** |  |

## 核心概念

上下文工程的基本词汇。出现在几乎每一篇里，最先要稳定下来。

### Context Engineering → 上下文工程

- **首次出现写法**：`上下文工程（Context Engineering）`
- **禁用译法**：`语境工程`、`情景工程`
- **说明**：全书标题级术语，不得译为「提示工程」

### context → 上下文

- **禁用译法**：`语境`、`情景`、`脉络`、`上下文环境`

### context window → 上下文窗口

- **禁用译法**：`上下文视窗`、`语境窗口`

### context management → 上下文管理


### context processing → 上下文处理


### context assembly → 上下文装配

- **禁用译法**：`上下文组装`、`上下文拼装`

### context engineering → 上下文工程


### prompt → 提示词

- **禁用译法**：`提示语`、`提示信息`
- **说明**：作为独立名词一律「提示词」；"prompting" 译「提示」

### prompt engineering → 提示词工程

- **禁用译法**：`提示工程`、`提示词设计工程`

### prompt programming → 提示词编程

- **首次出现写法**：`提示词编程（prompt programming）`
- **禁用译法**：`提示编程`

### token → 词元

- **首次出现写法**：`词元（token）`
- **禁用译法**：`令牌`
- **说明**：度量单位处保留 token 亦可，但首现必须给中文

### token budget → 词元预算

- **禁用译法**：`令牌预算`、`token 预算`

### embedding → 嵌入

- **禁用译法**：`向量嵌入`
- **说明**：名词「embedding vector」译「嵌入向量」

### retrieval → 检索

- **禁用译法**：`召回`

### Retrieval-Augmented Generation → 检索增强生成

- **首次出现写法**：`检索增强生成（RAG）`
- **禁用译法**：`检索增强式生成`、`检索辅助生成`

### RAG → RAG

- **说明**：缩写保留不译

### chunk → 片段

- **禁用译法**：`分块`、`切片`
- **说明**：本仓库的「段」（chunk 注释里的 chunk）指翻译分段，不译「片段」； 文档内容切分语境译「片段」

### reranking → 重排序

- **禁用译法**：`再排序`

### vector store → 向量库

- **禁用译法**：`向量存储`、`矢量库`

### knowledge graph → 知识图谱


### schema → 模式

- **禁用译法**：`结构体`、`架构图`
- **说明**：JSON Schema 等专名保留 schema 不译

### template → 模板

- **禁用译法**：`范本`、`样板`

## 记忆与认知层级

Atoms → Molecules → Cells → Organs 的层级隐喻，以及记忆系统的各个部件。

### memory → 记忆

- **禁用译法**：`内存`
- **说明**：正文一律「记忆」；代码标识符、YAML/JSON key 保留 memory
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 记忆系统 / 记忆机制（正文） | `记忆` |
  | 程序变量或代码中的 memory | `memory` |


### working memory → 工作记忆


### long-term memory → 长期记忆


### semantic memory → 语义记忆


### episodic memory → 情景记忆


### memory hierarchy → 记忆层级

- **禁用译法**：`记忆层次`

### atom → 原子

- **首次出现写法**：`原子（atom）`

### molecule → 分子

- **首次出现写法**：`分子（molecule）`

### cell → 细胞

- **首次出现写法**：`细胞（cell）`

### organ → 器官

- **首次出现写法**：`器官（organ）`

## 智能体与工具

智能体、工具调用、协议壳与编排。

### agent → 智能体

- **禁用译法**：`代理`、`代理人`、`经纪`
- **说明**：文件名、目录名中的 agent 保留原文
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 智能体（通用角色） | `智能体` |
  | .agent.md 提示词文件名 | `.agent.md（保留文件名不译）` |


### multi-agent → 多智能体

- **禁用译法**：`多代理`、`多主体`

### agentic → 智能体式的

- **禁用译法**：`代理式`

### tool use → 工具使用


### function calling → 函数调用


### orchestration → 编排

- **禁用译法**：`协奏`、`管弦`

### orchestrator → 编排器


### protocol → 协议

- **禁用译法**：`协议规范`
- **说明**：两者中文同形，按上下文补限定语（「协议壳」「通信协议」）区分
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 协议壳规范（.shell.md 中的行为约定） | `协议` |
  | 通信协议 / 网络协议 | `协议` |


### shell → 协议壳

- **禁用译法**：`外壳`、`壳层`
- **说明**：命令、代码、CLI 语境保留 shell 原词
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 协议壳（.shell.md 的可复用行为模板） | `协议壳` |
  | bash / 命令行 shell | `shell（保留）` |


### schema field → 字段


### resonance → 共振

- **禁用译法**：`共鸣`、`谐振`

### resonance scaffold → 共振支架

- **禁用译法**：`共振脚手架`

## 场论与涌现

本书最具理论色彩的部分。多数词在中文语境里没有既有译法，本表的译法即规范。

### field → 场

- **禁用译法**：`字段域`
- **说明**：M2 与 M10 统一用「场」；配置与 schema 内保留 field
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 神经场 / 语义场 / 场论（正文） | `场` |
  | 数据字段（YAML / JSON key） | `field（保留）` |


### semantic field → 语义场


### neural field → 神经场


### unified field theory → 统一场论


### field orchestration → 场编排


### attractor → 吸引子

- **禁用译法**：`吸引点`、`吸引力点`

### attractor dynamics → 吸引子动力学


### emergence → 涌现

- **禁用译法**：`突现`

### emergent → 涌现的

- **禁用译法**：`突现的`

### residue → 残差

- **禁用译法**：`残余`、`残留物`
- **说明**：与 symbolic / semantic 连用时译「残差」；与 code / dead 连用时译「残留」
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 符号残差（符号机制遗留的语义痕迹） | `残差` |
  | 代码残留 / 未清理的死代码 | `残留` |


### symbolic residue → 符号残差


### coherence → 连贯性

- **禁用译法**：`连贯度`
- **说明**：物理语境（quantum coherence）译「相干性」

### resonance field → 共振场


## 模式与递归

可复用的结构、递归、元层操作。

### pattern → 模式

- **禁用译法**：`样式`、`图案`
- **说明**：二者中文同形；正则语境可写「正则模式」明确
- **一词多义**：

  | 语境 | 译法 |
  |---|---|
  | 设计模式 / 行为模式（正文） | `模式` |
  | 正则模式 / 匹配模式（regex） | `模式` |


### cognitive pattern → 认知模式


### recursive → 递归

- **禁用译法**：`递归式`

### recursion → 递归


### meta-recursive → 元递归

- **禁用译法**：`超递归`、`元递归式`

### self-repair → 自修复

- **禁用译法**：`自我修复`、`自愈合`

## 学习范式

提示词工程的演进路径与教学用语。

### chain of thought → 思维链

- **首次出现写法**：`思维链（chain of thought）`
- **禁用译法**：`思考链`、`思维链条`、`思路链`

### few-shot → 少样本

- **禁用译法**：`少量样本`、`小样本`、`few shot`

### zero-shot → 零样本

- **禁用译法**：`无样本`、`零示例`

### in-context learning → 上下文学习

- **禁用译法**：`语境学习`、`情境学习`

### latent space → 潜空间

- **禁用译法**：`隐空间`、`潜在空间`

### attention → 注意力

- **禁用译法**：`关注度`、`注意机制`

### quantization → 量化


### distillation → 蒸馏


## 质量与运维

评估、预算、可观测性。

### evaluation → 评估

- **禁用译法**：`评测`、`评价`

### benchmark → 基准测试

- **禁用译法**：`跑分`

### grounding → 落地依据

- **禁用译法**：`接地`、`基础化`、`扎根`
- **说明**："grounded in" 译「以……为依据」

### hallucination → 幻觉

- **禁用译法**：`臆造`、`幻象`

### guardrail → 护栏

- **禁用译法**：`防护栏`、`护栏机制`

### observability → 可观测性

- **禁用译法**：`可观察性`

### trace → 轨迹

- **禁用译法**：`跟踪记录`
- **说明**：动词 "trace" 译「追踪」；名词（执行记录）译「轨迹」

### feedback loop → 反馈回路

- **禁用译法**：`反馈环`、`反馈循环`

### compression → 压缩


### summarization → 摘要

- **禁用译法**：`概括`
- **说明**：动作译「生成摘要」

### boundary operation → 边界操作

- **禁用译法**：`边界运算`

### cognitive tool → 认知工具


### Socratic question → 苏格拉底式提问

- **禁用译法**：`苏格拉底问题`
