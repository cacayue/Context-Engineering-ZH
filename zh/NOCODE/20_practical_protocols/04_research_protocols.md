---
title: 研究协议
source: NOCODE/20_practical_protocols/04_research_protocols.md
module: M8
task: M8-03
chunks: 9
chunks_done: [1, 2, 3, 4, 5, 6, 7, 8, 9]
status: published
source_sha256: 962747790d5fd2c03ebbb391ac76d78ef00d4cfe47acc1fd7f064347541c6333
---

> 原文：[NOCODE/20_practical_protocols/04_research_protocols.md](../../../NOCODE/20_practical_protocols/04_research_protocols.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 研究协议

> *「研究是形式化的好奇心，是有目的的探寻与追问。」*
>
> **— Zora Neale Hurston**

## 研究协议简介

研究（research）协议（protocol）将知识发现中常见的混乱、非线性过程转化为结构化、高效的工作流，持续产出可靠洞见。通过建立明确的调查与分析框架，这些协议帮助你清晰、有目的地探索复杂的信息领域。

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            RESEARCH PROTOCOL BENEFITS               │
│                                                     │
│  • Systematic knowledge discovery and validation    │
│  • Reduced cognitive bias in analysis               │
│  • Efficient exploration of complex topics          │
│  • Clear progression from questions to insights     │
│  • Traceable reasoning and evidence paths           │
│  • Repeatable processes for knowledge development   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

本指南提供适用于常见求知场景的即用型研究协议，以及实施指导和性能指标。每个协议都遵循 NOCODE 原则：导航、编排、控制、优化、部署与演进。

## 如何使用本指南

1. **选择协议**，使其与你的研究目标匹配
2. **复制协议模板**，包括提示词，并进行定制
3. **提供完整协议**，在交互开始时交给 AI 助手
4. **遵循结构化流程**，从初始问题走向经过验证的洞见
5. **监控指标**，评估有效性
6. **迭代与完善**协议，用于未来研究

**苏格拉底式提问**：目前哪些研究最让你感到困难或耗时？在知识发现过程中，你通常在哪里遇到瓶颈？

---

## 1. 文献综述协议

**何时使用此协议：**
需要全面理解某个主题的现有知识？此协议引导你系统探索可用信息，非常适合主题概览、前沿进展评估或知识综合。

```
Prompt: I need to conduct a comprehensive literature review on recent advances in quantum machine learning algorithms. I'm particularly interested in developments over the last three years, practical applications emerging in the field, and the most significant technical challenges still to be overcome. Please help me develop a systematic overview of the current state of knowledge in this area.

Protocol:
/research.literature{
    intent="Develop comprehensive understanding of existing knowledge on a topic",
    input={
        research_topic="Recent advances in quantum machine learning algorithms (last three years)",
        key_questions=[
            "What are the most significant theoretical advances in quantum machine learning algorithms?",
            "What practical applications are emerging from these advances?",
            "What technical challenges remain to be overcome in the field?"
        ],
        scope_boundaries={
            timeframe: "Last three years (2022-2025)",
            inclusion: "Peer-reviewed research, technical reports from major labs, significant preprints",
            exclusion: "Popular science coverage, introductory materials, pre-2022 foundations"
        },
        organization_approach="Thematic analysis with chronological progression within themes"
    },
    process=[
        /map{
            action="Create conceptual framework of the field",
            elements=[
                "key theoretical foundations",
                "major research streams",
                "significant applications",
                "evolving terminology and concepts"
            ]
        },
        /explore{
            action="Identify and analyze key contributions",
            for_each="research_stream",
            elements=[
                "seminal works and breakthroughs",
                "methodological innovations",
                "empirical findings and results",
                "limitations and controversies"
            ]
        },
        /synthesize{
            action="Develop integrated understanding",
            approaches=[
                "identify emerging patterns and trends",
                "map relationships between research streams",
                "contrast competing theories or approaches",
                "note consensus views and open questions"
            ]
        },
        /evaluate{
            action="Assess quality and significance of research",
            criteria=[
                "methodological rigor",
                "empirical support",
                "theoretical coherence",
                "practical implications"
            ]
        },
        /organize{
            action="Structure findings into coherent framework",
            elements=[
                "thematic organization",
                "chronological progression within themes",
                "highlight relationships and contrasts",
                "identify gaps and opportunities"
            ]
        }
    ],
    output={
        knowledge_synthesis="Comprehensive overview of current state of knowledge",
        key_findings="Summary of most significant insights and developments",
        research_map="Visual or structured representation of the field",
        gap_analysis="Identification of unanswered questions and opportunities"
    }
}
```

### 实施指南

1. **主题定义**：
   - 明确具体重点与范围
   - 提出关键问题，引导探索
   - 同时考虑广度与深度要求

2. **设定范围边界**：
   - 确定清晰的时间范围参数
   - 定义纳入与排除标准
   - 考虑资源限制与优先级

3. **选择组织方式**：
   - 根据研究目标选择框架
   - 可按主题、时间或方法组织
   - 对复杂主题考虑混合方式

4. **形成关键问题**：
   - 提出 3-5 个核心问题，引导综述
   - 确保问题具体而全面
   - 同时包含事实性与分析性问题

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 覆盖广度 | 主题领域覆盖的全面程度 | 包含所有重要子领域 |
| 来源质量 | 来源的可信度与相关性 | 高质量、有代表性的来源 |
| 综合深度 | 将信息整合为连贯整体 | 明确识别模式与关系 |
| 空白识别 | 认识知识的局限 | 明确梳理尚未回答的问题 |

## 2. 分析协议

**何时使用此协议：**
需要从复杂信息或数据中提取有意义的洞见？此协议引导你开展系统分析，非常适合趋势分析、比较评估、模式识别或批判性评估。
```
Prompt: I need to analyze the key factors driving the rapid growth of renewable energy adoption in different global markets. I have data on policy frameworks, technology costs, market structures, and investment trends across several regions. I want to understand which factors are most influential, how they interact, and how they vary across markets to develop strategic insights for our clean energy investment portfolio.

Protocol:
/research.analyze{
    intent="Extract meaningful insights through systematic analytical process",
    input={
        analysis_subject="Factors driving renewable energy adoption across global markets",
        analytical_framework={
            dimensions: ["Policy frameworks", "Technology costs", "Market structures", "Investment trends"],
            regions: ["North America", "Europe", "Asia-Pacific", "Emerging markets"],
            timeframe: "Last 5 years (2020-2025)"
        },
        key_questions=[
            "Which factors most strongly correlate with rapid renewable adoption?",
            "How do these factors interact and influence each other?",
            "How do influential factors vary across different market contexts?",
            "What patterns emerge in markets with highest adoption rates?"
        ],
        analysis_approach="Multi-dimensional comparative analysis with causal relationship mapping"
    },
    process=[
        /decompose{
            action="Break subject into analyzable components",
            elements=[
                "identify constituent factors and variables",
                "establish relevant metrics and indicators",
                "map relationships and dependencies",
                "define analytical boundaries and limitations"
            ]
        },
        /examine{
            action="Analyze each component systematically",
            for_each="dimension",
            approaches=[
                "comparative analysis across regions",
                "trend analysis over time",
                "pattern identification",
                "correlation and possible causation mapping"
            ]
        },
        /contextualize{
            action="Consider relevant context and influences",
            elements=[
                "historical development and precedents",
                "external factors and influences",
                "systemic constraints and enablers",
                "competing or alternative perspectives"
            ]
        },
        /integrate{
            action="Synthesize component analyses into holistic understanding",
            techniques=[
                "identify cross-component patterns",
                "map causal or influence networks",
                "develop explanatory frameworks",
                "test alternative interpretations"
            ]
        },
        /validate{
            action="Critically evaluate analytical conclusions",
            approaches=[
                "check against available evidence",
                "identify assumptions and limitations",
                "consider counter-arguments or exceptions",
                "assess confidence levels for findings"
            ]
        }
    ],
    output={
        key_insights="Primary analytical findings with supporting evidence",
        factor_analysis="Detailed examination of each key factor and its influence",
        relationship_map="Visual or structured representation of how factors interact",
        strategic_implications="Practical applications of analytical findings"
    }
}
```
### 实施指南

1. **定义对象**：
   - 清晰说明分析重点
   - 定义范围与边界
   - 确定需要考察的具体方面

2. **选择分析框架**：
   - 选择适当的分析维度
   - 定义用于比较的类别或区域
   - 确定相关时间范围

3. **形成关键问题**：
   - 提出具体问题，引导分析
   - 包含描述性、比较性与因果性问题
   - 聚焦具有战略或实践价值的问题

4. **选择分析方式**：
   - 选择适合对象与问题的方法
   - 考虑比较、时间、因果或系统分析方式
   - 定义适当的分析粒度

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 分析严谨性 | 系统、基于证据的考察 | 清晰的逻辑推进 |
| 洞见价值 | 发现的意义与实用性 | 非显而易见且可行动的洞见 |
| 关系映射 | 因素交互的清晰度 | 明确的因果或影响路径 |
| 验证质量 | 对结论进行批判性检验 | 多种验证方式 |

## 3. 战略前瞻协议

**何时使用此协议：**
需要预判未来发展，为新机遇或挑战做好准备？此协议引导你系统探索未来，非常适合趋势分析、场景构建、战略规划或创新预测。
```
Prompt: I need to develop a strategic foresight analysis for the healthcare technology sector over the next decade. Our organization needs to understand emerging technologies, shifting patient and provider needs, potential regulatory changes, and how these factors might reshape healthcare delivery models. We want to identify strategic opportunities and potential disruption risks to inform our long-term R&D investments.

Protocol:
/research.foresight{
    intent="Systematically explore future developments and strategic implications",
    input={
        domain="Healthcare technology sector",
        time_horizon="10 years (2025-2035)",
        focal_areas=[
            "Emerging technologies and their adoption trajectories",
            "Evolving patient and provider needs and expectations",
            "Regulatory environment and policy developments",
            "Healthcare delivery model transformation"
        ],
        key_uncertainties=[
            "Pace and direction of AI integration in clinical decision-making",
            "Patient data ownership and privacy regulation evolution",
            "Healthcare payment model transformation",
            "Public vs. private sector roles in healthcare innovation"
        ],
        strategic_context="Informing long-term R&D investment decisions for healthcare technology company"
    },
    process=[
        /scan{
            action="Identify and assess signals of change",
            elements=[
                "emerging trends and developments",
                "potential disruptive forces",
                "weak signals of systemic change",
                "stabilizing and constraining factors"
            ]
        },
        /analyze{
            action="Evaluate implications and interactions of trends",
            approaches=[
                "systems analysis of interrelated factors",
                "stakeholder impact assessment",
                "adoption and diffusion pattern analysis",
                "regulatory and policy evolution mapping"
            ]
        },
        /construct{
            action="Develop multiple plausible future scenarios",
            technique="Critical uncertainties matrix",
            elements=[
                "scenario narratives and evolution paths",
                "key milestones and indicators",
                "stakeholder positions and responses",
                "critical success factors in each scenario"
            ]
        },
        /assess{
            action="Evaluate strategic implications of scenarios",
            for_each="scenario",
            elements=[
                "opportunities and challenges",
                "required capabilities and resources",
                "competitive positioning",
                "risk factors and vulnerabilities"
            ]
        },
        /recommend{
            action="Develop strategic options and monitoring framework",
            elements=[
                "robust strategies across multiple futures",
                "hedging and option-creating approaches",
                "early indicator monitoring system",
                "adaptive strategy framework"
            ]
        }
    ],
    output={
        trend_analysis="Assessment of key trends and driving forces",
        scenario_portfolio="Set of distinct, plausible future scenarios",
        strategic_implications="Opportunities, challenges, and strategic options",
        monitoring_framework="Early indicators and adaptation triggers"
    }
}
```
### 实施指南

1. **定义领域**：
   - 明确重点领域与边界
   - 考虑相关的相邻领域
   - 定义适当的粒度

2. **设定时间跨度**：
   - 选择符合规划需求的时间范围
   - 适当时考虑多个时间跨度
   - 与组织规划周期保持一致

3. **选择重点领域**：
   - 确定关键探索领域
   - 同时包含内部与外部因素
   - 考虑技术、社会、经济与监管维度

4. **识别不确定性**：
   - 找出影响重大的关键不确定性
   - 聚焦真正不确定的要素，而非趋势
   - 考虑二阶不确定性与交互作用

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 场景合理性 | 逻辑连贯性与可信度 | 无幻想或矛盾 |
| 场景差异性 | 各种未来之间的有意义差别 | 清晰、对比鲜明的未来 |
| 战略相关性 | 对决策的可行动启示 | 与战略选择有明确联系 |
| 监测价值 | 预警框架的实用性 | 可观察的领先指标 |

## 4. 问题调查协议

**何时使用此协议：**
需要理解原因或维度不清晰的复杂问题？此协议引导你系统探索问题，适合根因分析、问题界定、问题诊断或挑战梳理。
```
Prompt: I need to investigate the underlying causes of our company's declining customer retention rates over the past 18 months. Despite several improvement initiatives, retention continues to drop across most customer segments. I want to develop a comprehensive understanding of the problem, including potential root causes, systemic factors, and relationship to other business metrics before we develop our next intervention strategy.

Protocol:
/research.problem{
    intent="Systematically investigate and understand complex problems",
    input={
        problem_statement="Declining customer retention rates over past 18 months despite improvement initiatives",
        problem_context="B2B SaaS company with enterprise customers across multiple industries",
        known_elements={
            symptoms: ["Increasing churn across most segments", "Declining product usage metrics", "Reduced expansion revenue"],
            attempted_solutions: ["Customer success team expansion", "User interface improvements", "New feature additions"],
            affected_stakeholders: ["Existing customers", "Account management team", "Product development", "Executive leadership"]
        },
        investigation_goals=["Identify root causes", "Map systemic factors", "Understand past solution failures", "Develop comprehensive problem frame"]
    },
    process=[
        /define{
            action="Clarify problem boundaries and manifestations",
            elements=[
                "precise problem definition and scope",
                "key metrics and indicators",
                "historical pattern and progression",
                "variation across contexts or segments"
            ]
        },
        /explore{
            action="Investigate potential causal factors",
            approaches=[
                "stakeholder perspective analysis",
                "comparative assessment across segments",
                "temporal correlation with external factors",
                "system relationship mapping"
            ]
        },
        /hypothesize{
            action="Develop potential explanations",
            techniques=[
                "multiple hypothesis formulation",
                "causal chain mapping",
                "system dynamics modeling",
                "contributing factor weighting"
            ]
        },
        /test{
            action="Evaluate hypotheses against available evidence",
            methods=[
                "evidence mapping to hypotheses",
                "identification of confirming/disconfirming data",
                "assessment of explanation power",
                "consideration of alternative interpretations"
            ]
        },
        /synthesize{
            action="Develop integrated problem understanding",
            elements=[
                "root cause identification",
                "systemic factor mapping",
                "interrelationship analysis",
                "comprehensive problem frame"
            ]
        }
    ],
    output={
        problem_analysis="Comprehensive assessment of the problem and its dimensions",
        causal_model="Map of root causes and contributing factors with relationships",
        evidence_assessment="Evaluation of supporting evidence for key findings",
        reframed_problem="Clarified problem statement with systemic context"
    }
}
```
### 实施指南

1. **形成问题陈述**：
   - 清晰说明观察到的问题
   - 聚焦症状而非假定原因
   - 包含范围与边界

2. **描述上下文**：
   - 提供相关组织与环境因素
   - 注明历史发展与变化
   - 包含利益相关方整体情况

3. **记录已知要素**：
   - 列出观察到的症状与表现
   - 记录此前的解决尝试与结果
   - 确定受影响的利益相关方及影响

4. **设定调查目标**：
   - 定义调查所需的具体成果
   - 同时包含分析与实践目标
   - 考虑决策的信息需求

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 因果深度 | 识别根本原因 | 超越症状，找到根本驱动因素 |
| 系统视角 | 考虑更广泛的上下文 | 梳理关系与交互作用 |
| 证据质量 | 对结论的支持 | 关键发现有多个证据来源 |
| 解决路径 | 从理解到行动的清晰路径 | 为干预提供可行动启示 |

## 5. 比较评估协议

**何时使用此协议：**
需要系统比较多个选项、方法或实体？此协议引导你开展结构化比较，适合方案评估、竞争分析、方法评估或决策支持。
```
Prompt: I need to conduct a comprehensive comparison of the three leading enterprise database technologies (Oracle, Microsoft SQL Server, and PostgreSQL) to determine the best fit for our organization's new data platform. We need to evaluate performance characteristics, cost structures, scalability, security features, ecosystem support, and future development roadmaps to make an informed technology selection decision.

Protocol:
/research.compare{
    intent="Systematically compare multiple options or entities with structured framework",
    input={
        comparison_subjects=["Oracle Database", "Microsoft SQL Server", "PostgreSQL"],
        evaluation_dimensions=[
            {name: "Performance", weight: 9, criteria: ["Query execution speed", "Indexing efficiency", "Concurrency handling"]},
            {name: "Cost structure", weight: 8, criteria: ["Licensing model", "Operational costs", "Scaling costs"]},
            {name: "Scalability", weight: 7, criteria: ["Vertical scaling capabilities", "Horizontal scaling options", "Performance at scale"]},
            {name: "Security", weight: 9, criteria: ["Access control granularity", "Encryption options", "Compliance capabilities"]},
            {name: "Ecosystem", weight: 6, criteria: ["Tool availability", "Talent pool", "Community support"]},
            {name: "Future roadmap", weight: 7, criteria: ["Innovation trajectory", "Vendor stability", "Feature development pace"]}
        ],
        comparison_context="Enterprise data platform selection for financial services organization",
        decision_criteria="Balance of performance, security, and total cost of ownership with consideration for future scalability needs"
    },
    process=[
        /establish{
            action="Create structured comparison framework",
            elements=[
                "comparison dimensions and criteria",
                "evaluation methodology",
                "scoring or assessment approach",
                "contextual considerations"
            ]
        },
        /analyze{
            action="Assess each subject across dimensions",
            for_each="comparison_subject",
            elements=[
                "detailed assessment against each criterion",
                "identification of strengths and weaknesses",
                "contextual performance factors",
                "distinctive characteristics or capabilities"
            ]
        },
        /compare{
            action="Conduct direct comparison across subjects",
            approaches=[
                "dimension-by-dimension comparative analysis",
                "relative strength assessment",
                "gap analysis",
                "trade-off identification"
            ]
        },
        /contextualize{
            action="Evaluate relevance to specific situation",
            elements=[
                "alignment with specific requirements",
                "implementation considerations",
                "organizational fit factors",
                "risk and opportunity assessment"
            ]
        },
        /synthesize{
            action="Develop integrated comparative assessment",
            elements=[
                "overall comparison summary",
                "key differentiating factors",
                "decision-relevant insights",
                "contextual recommendations"
            ]
        }
    ],
    output={
        comparison_matrix="Structured assessment across all dimensions and subjects",
        key_differentiators="Critical factors that distinguish the options",
        contextual_assessment="Evaluation of fit for specific situation",
        recommendation_framework="Decision support with conditional recommendations"
    }
}
```
### 实施指南

1. **选择对象**：
   - 确定适当的比较候选对象
   - 确保类别或分类相似
   - 考虑相关替代选项

2. **定义维度**：
   - 选择 4-8 个关键比较类别
   - 分配相对重要性权重
   - 定义每个维度的具体标准

3. **明确上下文**：
   - 描述相关情况或需求
   - 注明具体约束或偏好
   - 包含决策参数

4. **澄清决策标准**：
   - 说明比较如何为决策提供依据
   - 注明优先因素或需求
   - 包含所有不可妥协的要素

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 框架全面性 | 相关维度覆盖程度 | 包含所有决策关键因素 |
| 评估深度 | 对象评估的彻底程度 | 对每项标准进行实质分析 |
| 比较清晰度 | 选项间的清晰对照 | 在关键维度明确区分 |
| 上下文相关性 | 与具体情况的联系 | 明确应用于决策上下文 |

## 6. 研究综合协议

**何时使用此协议：**
需要将多样信息整合为连贯、有意义的框架？此协议引导你进行知识综合，适合跨学科整合、构建概念模型、创建框架或发展理论。
```
Prompt: I need to synthesize research findings from multiple disciplines (psychology, behavioral economics, neuroscience, and social media studies) to develop a comprehensive framework for understanding digital behavior change mechanisms. The goal is to create an integrated model that explains how different interventions influence online user behavior, particularly around sustainable consumption choices.

Protocol:
/research.synthesize{
    intent="Integrate diverse information into coherent frameworks or models",
    input={
        synthesis_goal="Develop comprehensive framework for digital behavior change mechanisms",
        knowledge_domains=[
            {domain: "Psychology", elements: ["Cognitive biases", "Motivation theory", "Habit formation"]},
            {domain: "Behavioral Economics", elements: ["Choice architecture", "Incentive structures", "Temporal discounting"]},
            {domain: "Neuroscience", elements: ["Reward pathways", "Attention mechanisms", "Decision processes"]},
            {domain: "Social Media Studies", elements: ["Engagement patterns", "Social influence", "Platform design effects"]}
        ],
        integration_level="Theoretical framework with practical application dimensions",
        application_context="Digital interventions for sustainable consumption choices"
    },
    process=[
        /map{
            action="Create knowledge landscape across domains",
            elements=[
                "key concepts and principles",
                "established relationships and mechanisms",
                "complementary and contradictory perspectives",
                "research quality and consensus levels"
            ]
        },
        /identify{
            action="Discover integration points and patterns",
            approaches=[
                "cross-domain concept mapping",
                "shared mechanism identification",
                "complementary explanation recognition",
                "gap and contradiction analysis"
            ]
        },
        /construct{
            action="Develop integrated framework or model",
            elements=[
                "organizing principles and structure",
                "key components and relationships",
                "causal or influence pathways",
                "boundary conditions and contexts"
            ]
        },
        /validate{
            action="Evaluate synthesis against evidence",
            methods=[
                "explanatory power assessment",
                "empirical support mapping",
                "logical consistency checking",
                "domain expert perspective consideration"
            ]
        },
        /refine{
            action="Enhance framework clarity and utility",
            approaches=[
                "conceptual clarity improvement",
                "practical application dimension development",
                "visual representation creation",
                "explanatory narrative construction"
            ]
        }
    ],
    output={
        integrated_framework="Comprehensive model synthesizing multi-domain insights",
        key_mechanisms="Core processes identified across domains",
        application_guidance="Practical implementation of theoretical framework",
        research_implications="Future research directions and open questions"
    }
}
```
### 实施指南

1. **定义综合目标**：
   - 清晰说明整合目的
   - 定义预期输出类型与层次
   - 明确预期应用

2. **梳理知识领域**：
   - 确定相关领域与学科
   - 从各领域选择关键要素
   - 注明相对发展程度与证据水平

3. **选择整合层次**：
   - 选择适当综合深度
   - 从概念映射到理论构建均可选择
   - 同时考虑理论与实践维度

4. **明确应用上下文**：
   - 定义预期用例或场景
   - 注明具体需求或约束
   - 考虑利益相关方需求与视角

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 整合质量 | 跨领域有意义的联系 | 连贯而非生硬拼凑的整合 |
| 框架实用性 | 综合的实践价值 | 可行动的启示与应用 |
| 解释力 | 解释多样现象的能力 | 全面解释关键机制 |
| 创新价值 | 整合产生的新洞见 | 单一领域看不到的新视角 |

## 7. 专家咨询协议

**何时使用此协议：**
需要从领域专家那里提取并组织专业知识？此协议引导你系统引出知识，适合专家访谈、专业知识记录、最佳实践收集或经验智慧采集。
### 实施指南

1. **明确领域**：
   - 清晰定义知识领域与边界
   - 聚焦具体方面，而非整个领域
   - 同时考虑广度与深度要求

2. **定义专业知识重点**：
   - 说明需要提取的具体知识
   - 优先关注价值最高或最紧迫的领域
   - 同时考虑显性与隐性知识

3. **记录专家背景**：
   - 注明相关背景与经验
   - 包含具体角色或职责
   - 考虑独特视角或专长

4. **设定知识目标**：
   - 定义期望的具体成果
   - 同时包含事实性与程序性知识
   - 考虑决策与上下文理解

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 知识深度 | 获取的专业知识层次 | 超越表面，深入专业经验 |
| 知识结构 | 组织性与可获取性 | 清晰、合乎逻辑的知识框架 |
| 隐性知识获取 | 提取隐含知识 | 不仅说明「是什么」，还说明「如何做」 |
| 上下文理解 | 因情况而异的应用因素 | 明确指导何时以及如何应用知识 |

## 8. 研究设计协议

**何时使用此协议：**
需要制定系统方法来回答研究问题？此协议引导你开发研究方法，适合研究设计、调查规划、方法选择或研究提案制定。
```
Prompt: I need to conduct an expert consultation to document best practices in cybersecurity incident response for financial institutions. I'm preparing for a structured interview with our organization's Chief Information Security Officer and want to ensure I capture their expertise comprehensively, especially regarding the initial detection and containment phases of incidents involving potential data breaches.

Protocol:
/research.expert{
    intent="Extract and structure specialized knowledge from domain expertise",
    input={
        domain="Cybersecurity incident response for financial institutions",
        expertise_focus="Best practices for detection and containment of potential data breaches",
        expert_context="Chief Information Security Officer with 15+ years experience",
        knowledge_goals=[
            "Critical first-response procedures and decision points",
            "Common pitfalls and their prevention",
            "Effective containment strategies and their situational application",
            "Communication protocols during breach investigation",
            "Evaluation frameworks for incident severity and scope"
        ],
        knowledge_structure="Procedural framework with decision criteria and contextual factors"
    },
    process=[
        /prepare{
            action="Develop knowledge extraction strategy",
            elements=[
                "domain map and terminology",
                "hierarchical question framework",
                "critical incident technique preparation",
                "knowledge validation approach"
            ]
        },
        /extract{
            action="Systematically elicit expert knowledge",
            techniques=[
                "scenario-based exploration",
                "process tracing and think-aloud protocols",
                "comparative case analysis",
                "tacit knowledge surfacing",
                "decision criteria elicitation"
            ]
        },
        /clarify{
            action="Ensure precise understanding of expert input",
            approaches=[
                "terminology and concept verification",
                "boundary condition exploration",
                "exception and edge case identification",
                "confidence level assessment"
            ]
        },
        /structure{
            action="Organize extracted knowledge into coherent framework",
            elements=[
                "procedural sequences and workflows",
                "decision frameworks and criteria",
                "contextual factors and considerations",
                "causal relationships and dependencies"
            ]
        },
        /validate{
            action="Verify knowledge accuracy and completeness",
            methods=[
                "expert review and correction",
                "scenario-based testing",
                "internal consistency checking",
                "comprehensiveness assessment"
            ]
        }
    ],
    output={
        knowledge_framework="Structured representation of expert knowledge",
        best_practices="Documented procedures and approaches",
        decision_guidance="Criteria and considerations for key decisions",
        application_contexts="Situational factors affecting implementation"
    }
}
```

```
Prompt: I'm planning a research study to understand how gamification elements impact user engagement and retention in health and wellness apps. I need to design a comprehensive methodology that will provide reliable insights into which game mechanics most effectively drive sustained engagement across different user demographics and health goals.

Protocol:
/research.design{
    intent="Develop systematic methodology to answer research questions",
    input={
        research_questions=[
            "Which gamification elements most effectively increase engagement in health apps?",
            "How do demographic factors moderate gamification effectiveness?",
            "What is the relationship between specific game mechanics and long-term retention?",
            "How do different health goals affect optimal gamification approaches?"
        ],
        research_context="Understanding engagement drivers in health and wellness mobile applications",
        methodological_constraints=[
            "Must be implementable within 4-month timeframe",
            "Access to existing app users for testing and data collection",
            "Mixed methods approach preferred",
            "Ethical considerations for health-related behavioral research"
        ],
        desired_outcomes="Actionable insights to guide gamification feature development priorities"
    },
    process=[
        /frame{
            action="Refine research questions and approach",
            elements=[
                "question specificity and testability",
                "conceptual framework development",
                "variable identification and operationalization",
                "hypothesis formulation"
            ]
        },
        /design{
            action="Develop research methodology",
            components=[
                "research approach selection (qualitative, quantitative, mixed)",
                "study design specification",
                "sampling strategy and participant selection",
                "data collection methods and instruments",
                "analytical approach planning"
            ]
        },
        /validate{
            action="Evaluate methodological quality and appropriateness",
            criteria=[
                "validity and reliability assessment",
                "bias identification and mitigation",
                "ethical consideration review",
                "feasibility and resource alignment",
                "limitations acknowledgment"
            ]
        },
        /plan{
            action="Create detailed implementation framework",
            elements=[
                "phased research timeline",
                "resource allocation and requirements",
                "research instruments and protocols",
                "data management and analysis plan",
                "contingency and adaptation strategies"
            ]
        },
        /communicate{
            action="Develop research documentation",
            components=[
                "methodology justification and rationale",
                "detailed procedure descriptions",
                "anticipated outcomes and applications",
                "limitations and constraints acknowledgment",
                "ethical and quality assurance measures"
            ]
        }
    ],
    output={
        research_design="Comprehensive methodology with rationale",
        implementation_plan="Detailed framework for execution",
        measurement_approach="Data collection and analysis methods",
        research_limitations="Acknowledged constraints and mitigations"
    }
}
```

### 实施指南

1. **形成研究问题**：
   - 提出清晰、具体、可回答的问题
   - 确保范围与重点适当
   - 同时考虑理论与实践维度

2. **描述研究上下文**：
   - 提供相关背景与环境
   - 注明现有知识与空白
   - 考虑利益相关方的兴趣与需求

3. **识别约束**：
   - 列出实际限制与边界
   - 包含时间范围、资源与访问条件
   - 注明伦理或监管方面的考虑

4. **定义成果**：
   - 澄清预期研究交付物
   - 定义结果的使用方式
   - 同时考虑学术与应用成果

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 方法契合度 | 问题与方法的匹配程度 | 从方法到答案有直接路径 |
| 设计严谨性 | 方法的科学质量 | 满足学科标准 |
| 可行性 | 实施的现实可操作性 | 可在约束内执行 |
| 预期效度 | 发现可能具有的可信度 | 较强的内部与外部效度 |

## 高级协议整合

### 为复杂项目组合研究协议

对于复杂研究需求，可以按顺序组合协议或将其嵌套：
```
Prompt: I'm leading a major research initiative to understand the future of remote work and its implications for organizational design, technology infrastructure, and employee well-being. We need to analyze current trends, anticipate future developments, synthesize cross-disciplinary insights, and develop strategic recommendations for organizations adapting to distributed work models.

Protocol:
/research.integrated{
    components=[
        /research.literature{
            intent="Establish current state of knowledge on remote work",
            input={
                research_topic="Remote work impacts across organizational, technological, and human dimensions",
                key_questions=[
                    "What are the established impacts of remote work on productivity, collaboration, and innovation?",
                    "How have organizations successfully adapted structures and processes for distributed work?",
                    "What technologies have proven most effective for supporting remote work?"
                ],
                scope_boundaries={
                    timeframe: "Focus on last 5 years with acceleration during pandemic",
                    inclusion: "Academic research, industry studies, organizational case studies",
                    exclusion: "Speculative or non-evidence-based commentary"
                }
            }
            // Process and output details
        },
        /research.foresight{
            intent="Anticipate future remote work developments",
            input={
                domain="Future of work with focus on remote/hybrid models",
                time_horizon="5-10 years (2025-2035)",
                focal_areas=[
                    "Technology evolution and adoption",
                    "Organizational structure and process transformation",
                    "Workforce expectations and needs",
                    "Regulatory and policy environment"
                ],
                key_uncertainties=[
                    "Extent of remote work normalization across industries",
                    "Impact of emerging technologies on virtual collaboration",
                    "Evolution of management and leadership approaches",
                    "Geographic redistribution of talent"
                ]
            }
            // Process and output details
        },
        /research.synthesize{
            intent="Integrate insights across disciplines",
            input={
                synthesis_goal="Develop comprehensive framework for remote work adaptation",
                knowledge_domains=[
                    {domain: "Organizational Psychology", elements: ["Team dynamics", "Culture formation", "Well-being factors"]},
                    {domain: "Management Science", elements: ["Coordination mechanisms", "Performance management", "Organizational design"]},
                    {domain: "Technology Studies", elements: ["Collaboration tools", "Digital infrastructure", "Human-computer interaction"]},
                    {domain: "Workplace Strategy", elements: ["Physical-digital integration", "Space utilization", "Experience design"]}
                ]
            }
            // Process and output details
        }
    ],
    integration_framework={
        sequence="Literature review → Foresight analysis → Cross-disciplinary synthesis",
        connection_points="Each phase builds on previous findings with explicit linkages",
        knowledge_building="Progressive development from current state to future possibilities to integrated framework"
    }
}
```
### 协议适配指南

1. **添加专门的流程步骤**：
   ```
   /research.analyze{
       ...
       process=[
           ...,
           /specialized{action="Industry-specific analytical techniques"}
       ]
   }
   ```
2. **扩展输入参数**：
   ```
   /research.literature{
       ...
       input={
           ...,
           methodological_filter="Focus on empirical studies with n>100"
       }
   }
   ```

3. **增强输出规范**：
   ```
   /research.expert{
       ...
       output={
           ...,
           training_framework="Knowledge structured for educational transfer"
       }
   }
   ```
## 研究协议中的场动力学

对于高级研究过程，可引入场动力学来塑造知识空间：
```
Prompt: I'm conducting research into emerging business models for decentralized autonomous organizations (DAOs) and want to ensure I explore both conventional and radical perspectives while maintaining analytical rigor. I'd like to use field dynamics to create a research space that balances established business theory with innovative concepts from the web3 ecosystem.

Protocol:
/research.literature{
    ...
    field_dynamics={
        attractors: [
            "business model innovation", 
            "governance mechanisms", 
            "value creation and capture"
        ],
        boundaries: {
            firm: ["unsubstantiated claims", "purely ideological arguments"],
            permeable: ["emerging concepts without extensive validation", "cross-disciplinary frameworks"]
        },
        resonance: ["organizational adaptation", "distributed decision-making"],
        residue: {
            target: "tension between centralized efficiency and decentralized resilience",
            persistence: "HIGH"
        }
    },
    ...
}
```
## 研究协议库管理

随着研究协议集合不断发展，组织管理对复用与完善变得至关重要。

### 组织框架

创建个人研究协议库：
```markdown
# Research Protocol Library

## By Research Phase
- [Literature Review v2.1](#literature-review)
- [Research Design v1.3](#research-design)
- [Expert Consultation v2.0](#expert-consultation)

## By Research Approach
- [Quantitative Research](#quantitative-research)
- [Qualitative Research](#qualitative-research)
- [Mixed Methods](#mixed-methods)

## Protocol Definitions

### Literature Review
```
## 研究协议开发流程

创建自己的研究协议可遵循以下开发路径：
```

### Research Design
```
## 平衡严谨性与创造力

研究协议提供结构，同时不妨碍发现。请考虑以下平衡原则：

1. **方法与开放并重**：建立方法上的严谨性，同时对意外发现保持开放
2. **结构与探索并重**：创建包含发散性调查的结构化流程
3. **精确与适应并重**：制定精确的方法，同时能适应新出现的洞见
4. **效率与全面并重**：构建高效工作流，同时保持全面覆盖

成功的研究协议建立起既确保质量、又促进发现的框架。

## 结论：知识发现的演进

研究协议将常常混乱的调查过程转变为结构化、可靠的洞见获取路径，同时保留发现与创造力的核心要素。通过为研究过程提供明确架构，它们支持更系统、高效、高质量的知识发展。

构建研究协议库时，请牢记以下原则：

1. **从关键问题出发**：聚焦最能从结构化中获益的研究挑战
2. **平衡严谨性与发现**：建立足够的方法结构，但不限制探索
3. **根据结果迭代**：依据研究成果完善协议
4. **适应上下文**：针对具体领域与问题修改协议
5. **内建质量保障**：在多个阶段加入验证与批判性评估

借助这些原则及本指南的研究协议，你便能够将不可预测的研究过程转化为可靠、严谨的调查，持续产出有价值的洞见。

**反思问题**：这些研究协议不仅会如何改变你的调查过程，还会如何改变你对知识发现质量标准的理解？

---

> *「研究不仅在于找到答案，更在于以更好的方式提出更好的问题。」*

---

## 附录：快速参考

### 协议基本结构
```
```
### 常见流程操作

- `/analyze`：系统考察信息
- `/synthesize`：将信息整合为连贯整体
- `/evaluate`：依据具体标准评估
- `/map`：创建领域的结构化表示
- `/explore`：调查可能性或因素
- `/validate`：验证质量、准确性或适当性
- `/contextualize`：考虑相关上下文或具体情况

### 场动力学快速设置
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│       RESEARCH PROTOCOL DEVELOPMENT CYCLE           │
│                                                     │
│  1. IDENTIFY NEED                                   │
│     • Recognize recurring research pattern          │
│     • Identify friction points in research process  │
│     • Define methodological requirements            │
│                                                     │
│  2. DESIGN STRUCTURE                                │
│     • Define research process components            │
│     • Outline key methodological stages             │
│     • Determine required input parameters           │
│                                                     │
│  3. PROTOTYPE & TEST                                │
│     • Create minimal viable protocol                │
│     • Test with realistic research questions        │
│     • Document effectiveness and limitations        │
│                                                     │
│  4. REFINE & OPTIMIZE                               │
│     • Enhance based on test results                 │
│     • Optimize for research quality and efficiency  │
│     • Improve adaptability across contexts          │
│                                                     │
│  5. SHARE & ITERATE                                 │
│     • Create usage guidelines                       │
│     • Define quality metrics                        │
│     • Evolve based on diverse applications          │
│                                                     │
└─────────────────────────────────────────────────────┘
```
### 研究协议选择指南

| 需求 | 推荐协议 |
|------|----------------------|
| 理解现有知识 | `/research.literature` |
| 从信息中提取洞见 | `/research.analyze` |
| 探索未来发展 | `/research.foresight` |
| 理解复杂问题 | `/research.problem` |
| 比较多个选项 | `/research.compare` |
| 整合多样知识 | `/research.synthesize` |
| 提取专家知识 | `/research.expert` |
| 开发研究方法 | `/research.design` |
```
/research.type{
    intent="Clear statement of purpose",
    input={...},
    process=[...],
    output={...}
}
```

### Common Process Actions

- `/analyze`: Examine information systematically
- `/synthesize`: Integrate information into coherent whole
- `/evaluate`: Assess against specific criteria
- `/map`: Create structured representation of domain
- `/explore`: Investigate possibilities or factors
- `/validate`: Verify quality, accuracy, or appropriateness
- `/contextualize`: Consider relevant context or situation

### Field Dynamics Quick Setup

```
field_dynamics={
    attractors: ["knowledge focus", "methodological approach"],
    boundaries: {
        firm: ["excluded approaches", "out-of-scope elements"],
        permeable: ["adjacent considerations", "emerging concepts"]
    },
    resonance: ["conceptual frameworks", "explanatory models"],
    residue: {
        target: "key tension or insight",
        persistence: "MEDIUM"
    }
}
```

### Research Protocol Selection Guide

| Need | Recommended Protocol |
|------|----------------------|
| Understand existing knowledge | `/research.literature` |
| Extract insights from information | `/research.analyze` |
| Explore future developments | `/research.foresight` |
| Understand complex problems | `/research.problem` |
| Compare multiple options | `/research.compare` |
| Integrate diverse knowledge | `/research.synthesize` |
| Extract expert knowledge | `/research.expert` |
| Develop research methodology | `/research.design` |
