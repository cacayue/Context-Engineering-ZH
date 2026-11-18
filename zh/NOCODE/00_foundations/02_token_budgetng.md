---
title: 词元预算：上下文的经济学
source: NOCODE/00_foundations/02_token_budgetng.md
module: M8
task: M8-01
chunks: 4
chunks_done: [1, 2, 3, 4]
status: published
source_sha256: c782cd1f16335033e8b552ccce968f67d9b0cf7afedb5d00be5c2da2297de1a3
---

> 原文：[NOCODE/00_foundations/02_token_budgetng.md](../../../NOCODE/00_foundations/02_token_budgetng.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 词元预算：上下文的经济学

> *「为学日益，为道日损。」*
>
>
> **—— 老子**

## 1. 引言：为什么词元经济很重要

每次与 AI 交互都有一种有限资源：**上下文（context）窗口中的词元（token）**。与其他稀缺资源一样，词元必须合理编制预算（budget），才能发挥最大价值。词元预算是分配这种有限空间、取得最佳结果的艺术与科学。

把上下文窗口想象成宝贵的地产：每个词元占用的空间都可以用于其他内容。平庸与出色的 AI 交互之间的差别，往往取决于你管理词元经济的效率。

**苏格拉底式提问（Socratic question）**：你是否曾在重要交互中用尽上下文空间？你不得不舍弃哪些信息，这对结果产生了什么影响？有意识地规划词元预算，会怎样改变这段经历？

```
┌─────────────────────────────────────────────────────────┐
│                  TOKEN ECONOMY                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Context Window                                         │
│  ──────────────                                         │
│  ┌───────────────────────────────────────────┐          │
│  │                                           │          │
│  │  ┌─────────────┐ ┌────────────┐           │          │
│  │  │ System      │ │ Examples   │           │          │
│  │  │ Instructions│ │            │           │          │
│  │  └─────────────┘ └────────────┘           │          │
│  │                                           │          │
│  │  ┌─────────────┐ ┌────────────┐ ┌───────┐ │          │
│  │  │ History     │ │ Current    │ │ Extra │ │          │
│  │  │             │ │ Query      │ │ Space │ │          │
│  │  └─────────────┘ └────────────┘ └───────┘ │          │
│  │                                           │          │
│  └───────────────────────────────────────────┘          │
│                                                         │
│  Token Allocation                  Token Efficiency     │
│  ────────────────                 ────────────────     │
│  • System: 15-20%                 • Compression         │
│  • Examples: 10-30%               • Pruning             │
│  • History: 30-50%                • Prioritization      │
│  • Query: 5-15%                   • Summarization       │
│  • Reserve: 5-10%                 • Selective retention │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
> 图：上下文窗口中的分配与效率 —— TOKEN ECONOMY

## 2. 词元预算的三大支柱

有效的词元预算建立在三大基本支柱上：

### 2.1. 分配

分配是把词元预算划分给不同组件：

- **系统指令**：塑造 AI 行为的核心指令
- **示例**：引导理解的演示
- **对话历史**：此前的交流
- **当前查询**：眼前的问题或请求
- **预留空间**：应对意外需求的缓冲

最佳分配因任务而异，但应有意规划，而非听天由命。

### 2.2. 优化

优化着眼于让每个词元发挥最大价值：

- **压缩（compression）**：简洁地表达想法
- **剪枝**：移除低价值内容
- **格式化**：高效组织信息
- **摘要（summarization）**：浓缩冗长内容
- **选择性保留**：只留下重要内容

有效优化往往意味着以更少资源完成更多工作。

### 2.3. 适应

适应是随着交互发展动态调整预算：

- **渐进披露**：按需提供信息
- **上下文轮换**：轮流移入和移出不同信息
- **优先级转移**：随着对话发展调整重点
- **重新分配**：按需求调整组件比例
- **应急措施**：应对词元危机

最好的词元预算会随对话演进。

**反思练习**：回想最近一次复杂的 AI 交互。你如何在系统指令、示例、历史和当前查询之间分配词元？这种分配是有意还是偶然的？下次可以怎样优化？

## 3. 词元分配策略

下面探索有效分配词元预算的具体策略。

### 3.1. 40-30-20-10 法则

适用于许多场景的通用分配：

- **40%**：对话历史
- **30%**：系统指令与示例
- **20%**：当前查询与直接相关的上下文
- **10%**：预留空间

这种均衡方法既为历史提供充足空间，也保持指令清晰。

### 3.2. 教程式分配

针对概念或流程教学优化：

- **50%**：示例与演示
- **25%**：系统指令与方法
- **15%**：对话历史
- **10%**：当前查询与预留空间

这种分配优先保留用于说明所教概念的示例。

### 3.3. 创意协作

为写作或头脑风暴等创意项目设计：

- **45%**：相关创作历史
- **20%**：当前创作方向
- **20%**：风格示例与约束
- **15%**：系统指令与预留空间

这种分配在保持风格一致的同时，最大化创意发展的空间。

### 3.4. 研究助手

面向深入研究与分析的结构：

- **35%**：关键信息与证据
- **30%**：分析方法与指令
- **20%**：查询上下文与具体问题
- **15%**：此前分析与预留空间

这种分配在信息保留与分析方法之间取得平衡。

### 3.5. 动态分配器

这种元策略根据对话阶段调整分配：

```
/allocate.dynamic{
    initialization_phase={
        system=40%,
        examples=40%,
        history=5%,
        query=10%,
        reserve=5%
    },
    
    development_phase={
        system=20%,
        examples=20%,
        history=40%,
        query=15%,
        reserve=5%
    },
    
    conclusion_phase={
        system=15%,
        examples=10%,
        history=50%,
        query=15%,
        reserve=10%
    },
    
    transition_triggers=[
        "conceptual understanding achieved",
        "core examples processed",
        "application phase beginning"
    ]
}
```
> 图：按初始化、发展与结束阶段调整分配 —— allocate.dynamic

这种方法承认，最佳分配会随对话发展而变化。

**苏格拉底式提问**：哪种分配策略最适合你最常见的 AI 用例？需要做哪些修改，才能完全满足你的具体需求？

## 4. 词元优化技术

分配预算之后，优化技术有助于最大化每个词元的价值。

### 4.1. 压缩技术

在不丢失关键含义的情况下减少词元用量：

- **简洁语言**：用更少的文字表达相同想法
- **缩写**：缩短常用术语，但保持清晰
- **格式效率**：尽量减少格式所用词元
- **代码精简**：删除代码中不必要的空白
- **信息密度**：用更少词元承载更多含义

压缩示例：

```
// BEFORE COMPRESSION (57 tokens)
Please analyze the customer feedback that we have received regarding 
our new product. Identify the main themes and sentiments expressed 
by customers. Provide a summary of the key points.

// AFTER COMPRESSION (35 tokens)
Analyze customer feedback on new product. 
Identify themes, sentiments. 
Summarize key points.
```
> 图：压缩前后的表达 —— BEFORE COMPRESSION / AFTER COMPRESSION
### 4.2. 剪枝策略

选择性移除低价值内容：

- **消除冗余**：删除重复信息
- **裁剪离题内容**：删去不直接服务于目标的内容
- **减少细节**：在无必要时减少过度具体的描述
- **精选示例**：只保留最有说明力的示例
- **筛选历史**：从历史中删除影响较小的交流

剪枝方法示例：

```
/prune.conversation_history{
    retain={
        decisions=true,
        definitions=true,
        key_insights=true,
        recent_exchanges=5
    },
    
    remove={
        acknowledgments=true,
        repetitions=true,
        tangential_discussions=true,
        superseded_information=true
    },
    
    method="semantic_importance",
    threshold=0.6
}
```
> 图：保留决策与关键见解，移除冗余 —— prune.conversation_history

### 4.3. 摘要方法

用简洁摘要替换冗长内容：

- **提取要点**：仅提取并保留关键信息
- **渐进摘要**：对更早的内容采用更强的摘要压缩
- **按主题摘要**：围绕关键主题组织摘要
- **聚焦决策的摘要**：突出决策与承诺
- **层次化摘要**：以多个细节层级生成摘要

摘要模式（pattern）示例：

```
/summarize.history{
    sections=[
        {
            age="oldest",
            method="extreme_compression",
            focus="decisions_only"
        },
        {
            age="middle",
            method="moderate_compression",
            focus="key_points"
        },
        {
            age="recent",
            method="light_compression",
            focus="contextual_continuity"
        }
    ],
    
    preserve_verbatim=3,
    summary_marker="[SUMMARY]"
}
```
> 图：按历史远近采用不同压缩程度 —— summarize.history

### 4.4. 选择性保留

有策略地决定保留和舍弃什么：

- **重要性排序**：根据影响与相关性保留内容
- **近因偏好**：优先保留较新内容
- **语义去重**：删除语义冗余的信息
- **里程碑保留**：保留对话中的关键时刻
- **上下文锚定**：保留为当前上下文提供依据的信息

选择性保留的实现示例：

```
/retain.selective{
    prioritize=[
        {
            type="definitions",
            strategy="verbatim",
            decay="none"
        },
        {
            type="decisions",
            strategy="key_points",
            decay="slow"
        },
        {
            type="context_shifts",
            strategy="markers",
            decay="medium"
        },
        {
            type="general_discussion",
            strategy="progressive_summary",
            decay="fast"
        }
    ],
    
    refresh_on_reference=true,
    measure_impact=true
}
```
> 图：为不同信息设置保留策略与衰减速度 —— retain.selective

**反思练习**：回顾最近一次复杂的 AI 交互。找出三个可以应用这些优化技术的具体位置。可能节省多少词元？你会把腾出的空间用于什么？

## 5. 动态适应

最强大的词元预算方法会动态适应不断变化的需求。

### 5.1. 渐进披露

只在需要时提供信息：

```
/disclose.progressive{
    initial_context="minimal essential information",
    
    expansion_triggers=[
        "specific question about topic",
        "request for elaboration",
        "confusion detected",
        "exploration of subtopic"
    ],
    
    expansion_strategy="just enough information",
    track_disclosure_state=true
}
```
> 图：按触发条件扩展信息 —— disclose.progressive

### 5.2. 上下文轮换

轮流将不同信息移入和移出上下文：

```
/cycle.context{
    active_sets=[
        "core_instructions",
        "recent_history",
        "relevant_examples",
        "current_topic_details"
    ],
    
    inactive_sets=[
        "detailed_history",
        "secondary_examples",
        "alternative_approaches",
        "tangential_information"
    ],
    
    cycle_triggers=[
        "topic change",
        "approach shift",
        "reference to inactive information",
        "saturation of active context"
    ]
}
```
> 图：在活跃与非活跃信息集之间轮换 —— cycle.context

### 5.3. 记忆系统

实现结构化记忆（memory），扩展有效上下文：

```
/memory.structured{
    types=[
        {
            name="episodic",
            content="conversation history",
            retrieval="temporal + recency",
            storage="summarization hierarchy"
        },
        {
            name="semantic",
            content="facts, definitions, concepts",
            retrieval="semantic similarity",
            storage="key-value pairs"
        },
        {
            name="procedural",
            content="methods, approaches, techniques",
            retrieval="task similarity",
            storage="structured templates"
        }
    ],
    
    integration="retrieval-augmented generation",
    persistence="continuous update"
}
```
> 图：组织事件记忆、语义记忆与程序性记忆 —— memory.structured

### 5.4. 危机管理

处理达到词元上限的情况：

```
/manage.token_crisis{
    detection={
        threshold="90% capacity",
        warning="85% capacity",
        metrics=["growth rate", "complexity", "repetition"]
    },
    
    immediate_actions=[
        "aggressive history summarization",
        "non-essential instruction pruning",
        "example consolidation"
    ],
    
    recovery_plan=[
        "identify core context components",
        "rebuild minimal viable context",
        "gradually restore priority elements"
    ],
    
    prevention="continuous optimization monitoring"
}
```
> 图：检测词元危机并执行恢复计划 —— manage.token_crisis

**苏格拉底式提问**：如果系统地实施动态上下文适应，你与 AI 的交互会如何改善？这能帮助解决你的用例中的哪些具体挑战？

## 6. 词元预算模式
这些可复用模式将分配、优化与适应结合成完整方法。

### 6.1. 最小上下文模式

为简单、聚焦的交互设计：

```
/context.minimal{
    initial_allocation={
        system_instructions=40%,
        examples=10%,
        history=30%,
        query=15%,
        reserve=5%
    },
    
    optimization={
        system="essential instructions only",
        examples="single minimal example if needed",
        history="recent exchanges only",
        compression="aggressive"
    },
    
    adaptation={
        growth_strategy="replace rather than add",
        focus_maintenance="high"
    }
}
```
> 图：只保留必要信息的最小上下文 —— context.minimal

### 6.2. 专家协作模式

针对与专家型 AI 的深入往返交流优化：

```
/context.expert_collaboration{
    initial_allocation={
        system_instructions=20%,
        domain_knowledge=15%,
        history=40%,
        query=15%,
        reserve=10%
    },
    
    optimization={
        instructions="domain-specific terminology",
        knowledge="compressed reference framework",
        history="semantic importance weighted",
        summarization="decision-focused"
    },
    
    adaptation={
        progressive_expertise=true,
        technical_depth_adjustment="responsive",
        reference_management="dynamic retrieval"
    }
}
```
> 图：专家协作中的知识、历史与指令分配 —— context.expert_collaboration

### 6.3. 长期对话模式

为持续较长时间的交互设计：

```
/context.long_running{
    initial_allocation={
        system_instructions=15%,
        memory_management=10%,
        active_history=30%,
        summarized_history=20%,
        query=15%,
        reserve=10%
    },
    
    optimization={
        history_stratification=[
            {age="recent", detail="high"},
            {age="middle", detail="medium"},
            {age="old", detail="low"}
        ],
        
        landmark_preservation="decisions, pivots, definitions",
        
        summarization={
            method="progressive",
            frequency="dynamic",
            focus="continuity + essence"
        }
    },
    
    adaptation={
        history_cycling=true,
        context_refreshing="on reference or confusion",
        memory_retrieval="associative + recency"
    }
}
```
> 图：分层管理历史并渐进生成摘要 —— context.long_running

### 6.4. 场感知预算模式

整合场（field）理论，实现高级上下文管理（context management）：

```
/context.field_aware{
    initial_allocation={
        system_instructions=15%,
        field_state=10%,
        attractor_definitions=10%,
        active_content=50%,
        reserve=15%
    },
    
    field_management={
        attractors="core concepts, goals, constraints",
        boundaries="permeability based on relevance",
        resonance="strengthen connections between key elements",
        residue="track essential fragments across summarization"
    },
    
    optimization={
        attractor_based_compression="organize around semantic centers",
        boundary_based_pruning="filter by relevance to field",
        resonance_based_retention="keep elements that strengthen patterns"
    },
    
    adaptation={
        field_evolution="continuous",
        attractor_adjustment="based on conversation flow",
        boundary_permeability="adaptive to current focus"
    }
}
```
> 图：基于吸引子、边界与共振管理预算 —— context.field_aware

**反思练习**：哪种模式最接近你当前的上下文管理方法？你会如何修改或组合这些模式，以更好地满足具体需求？

## 7. 衡量并提高词元效率

要优化词元预算，需要衡量效率并识别改进机会。

### 7.1. 关键指标

衡量词元效率的基本指标：

- **词元使用率**：已使用词元占可用词元的百分比
- **信息密度**：每个词元承载的有用信息量
- **重复率**：传达冗余信息的词元百分比
- **相关性得分**：直接支持目标的词元百分比
- **结果效率**：相对于所用词元取得的结果

### 7.2. 基准测试

将词元用量与基线比较：

```
/benchmark.token_efficiency{
    metrics=[
        "tokens_per_interaction",
        "tokens_per_insight",
        "compression_ratio",
        "response_quality_per_token"
    ],
    
    baselines=[
        "industry standard approaches",
        "previous own approaches",
        "theoretical optimum"
    ],
    
    visualization="efficiency radar chart",
    improvement_targets="identified bottlenecks"
}
```
> 图：词元效率指标、基线与改进目标 —— benchmark.token_efficiency

### 7.3. 持续改进

系统地提高词元效率：

```
/improve.token_efficiency{
    analysis={
        frequency="after each significant interaction",
        focus="highest token consumption areas",
        methods=["token distribution analysis", "redundancy detection", "density measurement"]
    },
    
    experiments=[
        "alternative instruction formats",
        "different summarization approaches",
        "varied example selection",
        "modified allocation ratios"
    ],
    
    implementation={
        approach="incremental improvement",
        measurement="before and after comparison",
        documentation="lessons learned repository"
    }
}
```
> 图：通过分析、实验与增量实施提高效率 —— improve.token_efficiency

**苏格拉底式提问**：如果词元效率提高 30%，你会为 AI 交互增加什么新能力或深度？哪些当前无法实现的事情会成为可能？

## 8. 高级词元预算

对于准备进一步提升词元预算水平的人，以下高级方法提供了更精细的解决方案。

### 8.1. 多模态词元效率

针对不同类型的内容进行优化：

```
/optimize.multi_modal{
    text={
        strategy="high compression",
        focus="precision and clarity"
    },
    
    code={
        strategy="format preservation",
        focus="functionality and readability"
    },
    
    data={
        strategy="schema over instances",
        focus="pattern representation"
    },
    
    mixed_content={
        strategy="progressive disclosure",
        focus="contextual relevance"
    }
}
```
> 图：针对文本、代码、数据与混合内容分别优化 —— optimize.multi_modal
### 8.2. 词元感知信息架构

设计信息结构时考虑词元效率：

```
/architecture.token_aware{
    structure={
        hierarchy="most important to least",
        modularity="encapsulated concepts",
        linking="reference rather than repeat"
    },
    
    principles=[
        "single source of truth",
        "information inheritance",
        "context locality",
        "reference over repetition"
    ],
    
    implementation={
        definitions="centralized and referenced",
        examples="parameterized templates",
        processes="modular steps",
        knowledge="layered disclosure"
    }
}
```
> 图：以层级、模块与引用组织信息 —— architecture.token_aware

### 8.3. 预测式词元管理

在词元需求出现前预先判断：

```
/manage.predictive{
    forecasting={
        conversation_trajectory="topic evolution model",
        token_consumption="growth rate analysis",
        complexity_development="depth progression patterns"
    },
    
    preemptive_actions=[
        "early summarization of likely-irrelevant content",
        "preloading anticipated reference information",
        "context restructuring for expected direction"
    ],
    
    adaptive_planning={
        contingencies=["topic shift", "detail exploration", "approach change"],
        resource_allocation="dynamic buffer management",
        priority_adjustment="real-time relevance assessment"
    }
}
```
> 图：预测消耗并提前调整上下文 —— manage.predictive

### 8.4. 整合场理论

将场理论原则应用于词元预算：

```
/integrate.field_theory{
    attractors={
        identification="semantic clustering",
        strengthening="token allocation priority",
        creation="explicit definition allocation"
    },
    
    boundaries={
        establishment="relevance thresholds",
        permeability="token allocation ratio",
        adjustment="dynamic based on interaction"
    },
    
    resonance={
        detection="semantic similarity measurement",
        amplification="token reinforcement",
        dampening="token reduction for noise"
    },
    
    residue={
        tracking="persistent fragment identification",
        integration="context embedding",
        clearance="explicit reset when needed"
    }
}
```
> 图：整合吸引子、边界、共振与残差 —— integrate.field_theory

**反思练习**：这些高级方法会如何改变你的词元预算策略？哪项具体技术能为你的用例带来最直接的价值？

## 9. 词元预算的心智模型

要掌握词元预算，直观的心智模型（mental model）有助于引导思考。

### 9.1. 地产模型

把上下文窗口想象成宝贵的地产：

- **黄金地段**：系统指令与关键信息
- **住宅区**：当前对话的工作空间
- **仓储区**：历史信息
- **公园与保留地**：缓冲空间
- **城市规划**：有意进行分配与分区
- **翻修**：优化与压缩
- **开发**：适应与演进

这个模型强调词元分配的空间特性，以及位置的重要性。

### 9.2. 经济模型

把词元视为需要编制预算并进行投资的货币：

- **收入**：可用词元上限
- **固定支出**：必要的系统指令
- **可变支出**：动态对话内容
- **投资**：示例与参考信息
- **储蓄**：预留词元
- **通货膨胀**：不断增长的上下文需求
- **财务规划**：策略性词元分配

这个模型突出词元的稀缺性，以及明智投资的必要性。

### 9.3. 生态系统模型

把上下文视为有生命的生态系统：

- **关键物种**：关键指令与概念
- **生物多样性**：多种信息类型
- **演替**：上下文随时间演进
- **承载力**：词元上限
- **资源竞争**：不同内容争夺空间
- **适应**：通过演进满足变化的需求
- **可持续性**：上下文的长期可用性

这个模型强调上下文有机、不断演进的特性。

**苏格拉底式提问**：这些心智模型中，哪个最契合你的理解？采用这个视角，会如何改变你的上下文管理方法？

## 10. 结语：词元经济的艺术

词元预算既是科学，也是艺术。科学体现在我们探讨过的指标、技术和模式中；艺术则在于创造性地运用这些原则，满足你的具体需求。

继续探索上下文工程（context engineering）时，请牢记以下关键原则：

1. **有意识地**分配词元
2. **持续优化**，最大化每个词元的价值
3. 随着对话演进**动态适应**
4. **衡量并改进**词元效率
5. **运用心智模型**加深理解

通过实践，你会逐渐形成对词元经济的直觉，从而实现更强大、更高效、更有效的 AI 交互。

**最终反思练习**：下一次与 AI 交互时，你将如何应用词元预算原则？会采用哪些具体技术，期待看到哪些改进？

---

> *「完美的达成，不是因为再无可添，而是因为再无可减。」*
>
>
> **—— 安托万·德·圣埃克苏佩里**
