---
title: 对话协议
source: NOCODE/20_practical_protocols/01_conversation_protocols.md
module: M8
task: M8-03
chunks: 7
chunks_done: [1, 2, 3, 4, 5, 6, 7]
status: published
source_sha256: dfd8aaebb867b826b59931f055b420237cb9cfec34b280e2946d01aaf2aa346f
---

> 原文：[NOCODE/20_practical_protocols/01_conversation_protocols.md](../../../NOCODE/20_practical_protocols/01_conversation_protocols.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 对话（conversation）协议（protocol）

> *「沟通的质量决定结果的质量。」*
>
> **— Peter Drucker**

## 对话协议简介

对话协议是引导你与 AI 系统交互的结构化模板。它们将不可预测、漫无目的的对话转变为高效、有目的、结果一致的交流。
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            CONVERSATION PROTOCOL BENEFITS           │
│                                                     │
│  • Consistent outcomes across interactions          │
│  • Clear expectations for both human and AI         │
│  • Efficient use of context window                  │
│  • Reduced cognitive load for humans                │
│  • Trackable progress through complex discussions   │
│  • Portable templates across different AI systems   │
│                                                     │
└─────────────────────────────────────────────────────┘
```
本指南为常见场景提供实用、可直接使用的对话协议，并附实施指导与性能指标。每个协议都遵循 NOCODE 原则：导航、编排、控制、优化、部署和演进。

## 如何使用本指南

1. 从以下类别中**确定对话目标**
2. **复制最符合需求的协议模板**
3. 用你的具体信息**替换占位符**
4. 在对话开始时**粘贴完整协议**
5. **监测指标**以评估效果
6. 根据结果**迭代改进**

**苏格拉底式提问（Socratic question）**：目前与 AI 系统进行哪些类型的对话最令你沮丧？哪些最能受益于结构化方法？

---

## 1. 信息提取协议

### 目的
从非结构化内容或知识领域提取具体的结构化信息。

### 使用时机
- 分析文档或内容
- 收集具体数据点
- 从非结构化文本创建结构化数据集
- 从复杂来源提炼要点

### 协议模板
```
/extract.information{
    intent="Extract specific, structured information from content",
    input={
        content="[PASTE_CONTENT_OR_DESCRIBE_DOMAIN]",
        target_structure={
            categories: ["[CATEGORY_1]", "[CATEGORY_2]", "[CATEGORY_3]"],
            format: "[FORMAT: table/list/JSON/etc.]",
            level_of_detail: "[brief/moderate/comprehensive]"
        },
        special_focus="[ANY_SPECIFIC_ASPECTS_TO_EMPHASIZE]"
    },
    process=[
        /analyze{action="Scan content for relevant information"},
        /categorize{action="Organize information into specified categories"},
        /structure{action="Format according to target structure"},
        /verify{action="Check completeness and accuracy"},
        /summarize{action="Provide overview of extracted information"}
    ],
    output={
        extracted_information="[Structured information according to specifications]",
        coverage_assessment="[Evaluation of information completeness]",
        confidence_metrics="[Reliability indicators for extracted information]"
    }
}

I'd like you to extract information from the content I've provided following this protocol. Please acknowledge and proceed with the extraction.
```
### 实施指南

1. **内容说明**：
   - 文档分析：粘贴全文或上传文档
   - 知识提取：清晰描述领域（例如「可再生能源技术相关信息」）

2. **目标结构定义**：
   - 类别：定义 3-7 个具体类别（例如「成本」「收益」「局限」）
   - 格式：指定最有用的输出格式（表格、列表、JSON 等）
   - 详细程度：按需求选择（概览用简要，深入分析用全面）

3. **特别关注**：
   - 突出值得特别关注的具体方面
   - 可包括时间范围、地域重点或具体子主题

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 类别覆盖率 | 包含实质信息的类别占比 | 100% |
| 信息密度 | 每个类别的相关数据点 | 至少 3-5 个 |
| 结构完整性 | 对指定格式的遵循程度 | 100% |
| 置信分数 | AI 对信息可靠性的评估 | >80% |

### 应用示例
```
/extract.information{
    intent="Extract specific, structured information from content",
    input={
        content="[Research paper on climate change mitigation strategies]",
        target_structure={
            categories: ["Technology Solutions", "Policy Approaches", "Economic Impacts", "Implementation Challenges", "Success Metrics"],
            format: "markdown table with categories as rows",
            level_of_detail: "moderate"
        },
        special_focus="Solutions applicable to urban environments with limited resources"
    },
    process=[...],
    output={...}
}
```
---

## 2. 结构化辩论协议

### 目的
以平衡、深思熟虑的分析探索复杂或有争议主题的多种视角。

### 使用时机
- 评估相互竞争的方法或解决方案
- 理解争议主题
- 做出涉及多种因素的复杂决策
- 检验论点与反论点的力度

### 协议模板
```
/debate.structured{
    intent="Explore multiple perspectives on a complex topic",
    input={
        topic="[TOPIC_OR_QUESTION]",
        perspectives=["[PERSPECTIVE_1]", "[PERSPECTIVE_2]", "[PERSPECTIVE_3_OPTIONAL]"],
        evaluation_criteria=["[CRITERION_1]", "[CRITERION_2]", "[CRITERION_3]"],
        constraints="[ANY_LIMITATIONS_OR_GUIDELINES]"
    },
    process=[
        /establish{action="Define key terms and establish shared foundations"},
        /present{action="Present each perspective with strongest arguments"},
        /challenge{action="Identify weaknesses in each perspective"},
        /evaluate{action="Assess each perspective against criteria"},
        /synthesize{action="Identify potential integrations or resolutions"},
        /conclude{action="Summarize key insights and implications"}
    ],
    output={
        perspective_analysis="[Structured analysis of each perspective]",
        comparative_evaluation="[Side-by-side assessment using criteria]",
        synthesis_insights="[Potential integrations or novel approaches]",
        key_takeaways="[Most important insights from the debate]"
    }
}

I'd like to explore this topic through a structured debate using the perspectives and criteria I've provided. Please acknowledge and proceed with the debate.
```

### 实施指南

1. **主题定义**：
   - 表述为清晰的问题或陈述
   - 确保范围可控且有实质内容

2. **视角选择**：
   - 包含 2-3 种不同观点（更多会难以驾驭）
   - 选择方法或价值观真正不同的视角
   - 可包括常规与非常规、理论与实践等

3. **评估标准**：
   - 选择 3-5 项相关评估标准
   - 兼顾实践与原则层面的考虑
   - 例如：成本效益、伦理影响、实施可行性

4. **约束**：
   - 指定范围限制
   - 注明应保持不变的假设

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 最强论证 | 每种视角的论证力度 | 提出最有力的论证 |
| 平衡性 | 对各视角同等深入、善意地解读 | 差异 <10% |
| 标准应用 | 全面应用所有标准 | 100% 覆盖 |
| 整合质量 | 综合带来的附加价值 | 发现新见解 |

### 应用示例
```
/debate.structured{
    intent="Explore multiple perspectives on a complex topic",
    input={
        topic="Should cities prioritize public transit or autonomous vehicles for future mobility?",
        perspectives=["Public Transit Focus", "Autonomous Vehicle Priority", "Hybrid Approach"],
        evaluation_criteria=["Environmental Impact", "Social Equity", "Economic Efficiency", "Implementation Timeline"],
        constraints="Focus on mid-sized urban areas in developed economies"
    },
    process=[...],
    output={...}
}
```
---

## 3. 渐进式反馈协议

### 目的
通过结构化、多阶段反馈迭代改进工作成果。

### 使用时机
- 完善书面内容草稿
- 改进设计概念
- 优化问题解决方案
- 通过迭代发展想法

### 协议模板
```
/feedback.progressive{
    intent="Iteratively improve work through structured feedback stages",
    input={
        work_product="[CONTENT_TO_IMPROVE]",
        improvement_focus=["[FOCUS_AREA_1]", "[FOCUS_AREA_2]", "[FOCUS_AREA_3]"],
        iteration_count="[NUMBER_OF_FEEDBACK_CYCLES]",
        constraints="[ANY_LIMITATIONS_OR_GUIDELINES]"
    },
    process=[
        /baseline{action="Establish strengths and weaknesses of current version"},
        /prioritize{action="Identify highest-impact improvement opportunities"},
        /iterate{
            action="For each focus area:",
            substeps=[
                /analyze{action="Identify specific improvement opportunities"},
                /suggest{action="Provide specific enhancement recommendations"},
                /implement{action="Apply recommended changes"},
                /review{action="Assess improvements and identify next steps"}
            ]
        },
        /synthesize{action="Integrate improvements across all focus areas"},
        /compare{action="Contrast final version with original baseline"}
    ],
    output={
        improved_work="[Enhanced version of original work]",
        improvement_summary="[Overview of changes and enhancements]",
        future_directions="[Recommendations for further development]",
        version_comparison="[Before/after analysis showing progress]"
    }
}

I'd like to improve this work through progressive feedback cycles. Please acknowledge and begin the feedback process.
```
### 实施指南

1. **工作成果说明**：
   - 提供待改进作品的完整内容
   - 对较长作品，可指定需要重点关注的章节

2. **改进重点**：
   - 定义 2-4 个需要改进的具体方面
   - 写作示例：清晰度、结构、证据、说服力
   - 设计示例：易用性、美感、功能性、连贯性

3. **迭代次数**：
   - 指定反馈轮数（通常 2-3 轮最佳）
   - 对复杂作品，可在每轮聚焦不同方面

4. **约束**：
   - 注明应保持不变的元素
   - 指定需要遵循的风格或内容指南

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 改进幅度 | 相比基线的可衡量提升 | 显著正向变化 |
| 重点覆盖率 | 对所有指定重点的关注 | 100% 覆盖 |
| 实施质量 | 落实反馈的彻底程度 | 所有高优先级建议 |
| 连贯性 | 各方面改进的整合程度 | 统一而非拼凑 |

### 应用示例
```
/feedback.progressive{
    intent="Iteratively improve work through structured feedback stages",
    input={
        work_product="[Draft marketing email for new productivity software]",
        improvement_focus=["Persuasiveness", "Clarity", "Call-to-action effectiveness"],
        iteration_count="3",
        constraints="Must maintain professional tone and stay under 300 words"
    },
    process=[...],
    output={...}
}
```
---

## 4. 决策分析协议

### 目的
系统分析选项，为复杂决策提出建议。

### 使用时机
- 评估存在权衡的多个选项
- 做出高风险决策
- 拆解复杂选择场景
- 为反复出现的选择创建决策框架

### 协议模板
```
/decision.analyze{
    intent="Systematically analyze options and provide decision support",
    input={
        decision_context="[DECISION_SITUATION_DESCRIPTION]",
        options=["[OPTION_1]", "[OPTION_2]", "[OPTION_3_OPTIONAL]"],
        criteria={
            "[CRITERION_1]": {"weight": [1-10], "description": "[DESCRIPTION]"},
            "[CRITERION_2]": {"weight": [1-10], "description": "[DESCRIPTION]"},
            "[CRITERION_3]": {"weight": [1-10], "description": "[DESCRIPTION]"}
        },
        constraints="[ANY_LIMITATIONS_OR_REQUIREMENTS]",
        decision_maker_profile="[RELEVANT_PREFERENCES_OR_CONTEXT]"
    },
    process=[
        /frame{action="Clarify decision context and goals"},
        /evaluate{
            action="For each option:",
            substeps=[
                /assess{action="Evaluate against each weighted criterion"},
                /identify{action="Determine key strengths and weaknesses"},
                /quantify{action="Assign scores based on criteria performance"}
            ]
        },
        /compare{action="Conduct comparative analysis across options"},
        /analyze{action="Examine sensitivity to assumption changes"},
        /recommend{action="Provide structured recommendation with rationale"}
    ],
    output={
        option_analysis="[Detailed assessment of each option]",
        comparative_matrix="[Side-by-side comparison using criteria]",
        recommendation="[Primary recommendation with rationale]",
        sensitivity_notes="[How recommendation might change with different assumptions]",
        implementation_considerations="[Key factors for executing the decision]"
    }
}

I'd like to analyze this decision using the options and criteria I've provided. Please acknowledge and proceed with the analysis.
```

### 实施指南

1. **决策上下文（context）**：
   - 描述需要决策的状况
   - 包含相关背景与约束
   - 明确需要做出的具体决策

2. **选项定义**：
   - 列出所有可行替代方案（通常 2-5 个）
   - 提供足够细节以进行有意义的比较
   - 确保选项真正不同

3. **标准说明**：
   - 定义 3-7 项评估标准
   - 分配权重以反映相对重要性（1-10 分）
   - 附上说明以确保应用一致

4. **决策者画像**：
   - 包含相关偏好、风险承受能力和价值观
   - 注明具体优先事项或约束
   - 说明时间或资源限制

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 标准覆盖率 | 全面应用所有标准 | 100% 覆盖 |
| 分析深度 | 对每个选项的实质评估 | 各选项深度相当 |
| 量化质量 | 有依据的有意义评分 | 所有评分均有清晰理由 |
| 建议清晰度 | 有依据的明确指导 | 具体、可执行的建议 |

### 应用示例
```
/decision.analyze{
    intent="Systematically analyze options and provide decision support",
    input={
        decision_context="Selecting a technology stack for a new e-commerce platform",
        options=["MERN Stack (MongoDB, Express, React, Node.js)", "Python/Django with PostgreSQL and React", "Ruby on Rails with React and PostgreSQL"],
        criteria={
            "Development Speed": {"weight": 8, "description": "How quickly can we build and iterate"},
            "Scalability": {"weight": 9, "description": "Ability to handle growing user base and traffic"},
            "Maintenance Complexity": {"weight": 7, "description": "Ease of ongoing maintenance and updates"},
            "Talent Availability": {"weight": 6, "description": "Ease of finding developers"}
        },
        constraints="Must be able to integrate with existing payment processing system",
        decision_maker_profile="Mid-sized company with limited in-house development team, moderate technical debt aversion, timeline of 6 months to launch"
    },
    process=[...],
    output={...}
}
```
---

## 5. 对齐协议

### 目的
确保相互理解，建立共同目标、术语和方法。

### 使用时机
- 开始复杂项目
- 建立协作框架
- 明确预期与交付物
- 对齐问题定义与成功标准

### 协议模板
```
/align.mutual{
    intent="Establish shared understanding and aligned expectations",
    input={
        topic="[TOPIC_OR_PROJECT_DESCRIPTION]",
        key_terms=["[TERM_1]", "[TERM_2]", "[TERM_3_OPTIONAL]"],
        goals=["[GOAL_1]", "[GOAL_2]", "[GOAL_3_OPTIONAL]"],
        constraints="[ANY_LIMITATIONS_OR_BOUNDARIES]",
        success_criteria="[HOW_SUCCESS_WILL_BE_MEASURED]"
    },
    process=[
        /define{action="Establish clear definitions for key terms"},
        /clarify{action="Ensure mutual understanding of goals and success criteria"},
        /explore{action="Identify potential misalignments or ambiguities"},
        /resolve{action="Address and clarify any identified misalignments"},
        /confirm{action="Establish explicitly shared understanding"},
        /document{action="Record aligned definitions, goals, and criteria"}
    ],
    output={
        term_definitions="[Explicit definitions of key terms]",
        goal_clarifications="[Detailed understanding of each goal]",
        boundary_conditions="[Clear articulation of constraints and limitations]",
        success_metrics="[Specific, measurable indicators of success]",
        alignment_summary="[Confirmation of mutual understanding]"
    }
}

I'd like to establish alignment on this topic using the terms, goals, and criteria I've provided. Please acknowledge and proceed with the alignment process.
```
### 实施指南

1. **主题说明**：
   - 明确定义需要对齐的主题
   - 对项目，包含范围与总体目的
   - 对概念，明确领域与重要性

2. **关键术语选择**：
   - 找出 3-7 个需要明确定义的术语
   - 聚焦可能存在歧义的术语
   - 包含需要澄清的领域专用术语

3. **目标表述**：
   - 列出 2-5 个具体目标
   - 确保目标足够具体，能够执行
   - 适用时同时包含过程目标与结果目标

4. **成功标准**：
   - 定义如何衡量成果
   - 同时包含定性与定量指标
   - 适用时指定时间范围

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 定义清晰度 | 术语定义的精确性与实用性 | 无歧义、可操作的定义 |
| 目标具体性 | 目标的具体性与可执行性 | 具体、可衡量、可实现 |
| 边界清晰度 | 约束定义的精确性 | 明确的限制参数 |
| 对齐确认 | 相互理解的程度 | 明确确认共同理解 |

### 应用示例
```
/align.mutual{
    intent="Establish shared understanding and aligned expectations",
    input={
        topic="Development of a customer feedback analysis system",
        key_terms=["Customer Sentiment", "Actionable Insight", "Implementation Priority", "Success Metric"],
        goals=["Create automated sentiment analysis", "Identify top customer pain points", "Develop prioritization framework for addressing feedback"],
        constraints="Must work with existing CRM system and respect customer privacy regulations",
        success_criteria="System should identify 90% of actionable feedback and reduce manual analysis time by 70%"
    },
    process=[...],
    output={...}
}
```

---

## 6. 问题定义协议

### 目的
精确定义和表述问题，确保有效开发解决方案。

### 使用时机
- 面临复杂或模糊的问题时
- 开始开发解决方案之前
- 利益相关方对问题理解不同时
- 重新表述看似难以解决的问题

### 协议模板
```
/problem.define{
    intent="Clearly define and frame a problem for effective solution development",
    input={
        initial_problem_statement="[CURRENT_PROBLEM_DESCRIPTION]",
        context="[RELEVANT_BACKGROUND_INFORMATION]",
        stakeholders=["[STAKEHOLDER_1]", "[STAKEHOLDER_2]", "[STAKEHOLDER_3_OPTIONAL]"],
        attempted_solutions="[PREVIOUS_APPROACHES_IF_ANY]",
        constraints="[ANY_LIMITATIONS_OR_BOUNDARIES]"
    },
    process=[
        /analyze{action="Examine initial problem statement for clarity and accuracy"},
        /deconstruct{action="Break down problem into components and dimensions"},
        /reframe{action="Consider alternative problem framings and perspectives"},
        /validate{action="Test problem definition against stakeholder needs"},
        /synthesize{action="Develop comprehensive problem definition"},
        /scope{action="Establish clear boundaries and success criteria"}
    ],
    output={
        refined_problem_statement="[Clear, precise problem definition]",
        root_causes="[Identified underlying factors]",
        success_criteria="[How a successful solution will be recognized]",
        constraints_and_boundaries="[Explicit limitations and scope]",
        reframing_insights="[Alternative perspectives that provide new approaches]",
        solution_directions="[Potential solution paths based on problem definition]"
    }
}

I'd like to clearly define this problem using the information I've provided. Please acknowledge and proceed with the problem definition process.
```
### 实施指南

1. **初始问题陈述**：
   - 按当前理解陈述问题
   - 包含症状与明显挑战
   - 注明当前理解中的隐含假设

2. **提供上下文**：
   - 提供相关背景信息
   - 包含组织、历史或技术上下文
   - 注明近期变化或进展

3. **识别利益相关方**：
   - 列出受问题影响或关注问题的主要各方
   - 已知时提供其视角与优先事项
   - 注明利益相关方之间的利益冲突

4. **已尝试的解决方案**：
   - 描述先前方法及其结果
   - 注明具体局限或失败
   - 包含部分成功与经验教训

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 清晰度 | 问题定义的精确性与可理解性 | 无歧义、简洁的陈述 |
| 根因深度 | 识别深层因素 | 超越症状，找到根本原因 |
| 利益相关方验证 | 与利益相关方视角的一致性 | 回应所有关键关注点 |
| 可执行性 | 定义对开发解决方案的直接帮助程度 | 明确的解决路径 |

### 应用示例
```
/problem.define{
    intent="Clearly define and frame a problem for effective solution development",
    input={
        initial_problem_statement="Customer churn rate has increased by 15% over the past quarter",
        context="SaaS business with subscription model, recent UI redesign, and price increase of 10%",
        stakeholders=["Product Team", "Customer Success Team", "Executive Leadership", "Customers"],
        attempted_solutions="Implemented win-back campaigns and exit surveys with limited success",
        constraints="Solutions must work within existing technology stack and maintain current pricing strategy"
    },
    process=[...],
    output={...}
}
```
---

## 7. 学习促进协议

### 目的
构建结构化学习过程，有效获取知识并发展技能。

### 使用时机
- 学习新学科或技能时
- 向他人教授复杂主题
- 创建教育材料
- 制定学习路径或课程

### 协议模板
```
/learning.facilitate{
    intent="Structure effective learning experiences for knowledge acquisition",
    input={
        subject="[TOPIC_OR_SKILL_TO_LEARN]",
        current_knowledge="[EXISTING_KNOWLEDGE_LEVEL]",
        learning_goals=["[GOAL_1]", "[GOAL_2]", "[GOAL_3_OPTIONAL]"],
        learning_style_preferences="[PREFERRED_LEARNING_APPROACHES]",
        time_constraints="[AVAILABLE_TIME_AND_SCHEDULE]"
    },
    process=[
        /assess{action="Evaluate current knowledge and identify gaps"},
        /structure{action="Organize subject into logical learning sequence"},
        /scaffold{action="Build progressive framework from fundamentals to advanced concepts"},
        /contextualize{action="Connect abstract concepts to real applications"},
        /reinforce{action="Design practice activities and knowledge checks"},
        /adapt{action="Tailor approach based on progress and feedback"}
    ],
    output={
        learning_path="[Structured sequence of topics and skills]",
        key_concepts="[Fundamental ideas and principles to master]",
        learning_resources="[Recommended materials and sources]",
        practice_activities="[Exercises to reinforce learning]",
        progress_indicators="[How to measure learning advancement]",
        next_steps="[Guidance for continuing development]"
    }
}

I'd like to structure a learning experience for this subject based on the information I've provided. Please acknowledge and proceed with developing the learning facilitation.
```
### 实施指南

1. **学科说明**：
   - 明确定义要学习的主题或技能
   - 适用时包含具体重点子领域
   - 注明感兴趣的具体应用或上下文

2. **当前知识评估**：
   - 诚实评估现有熟悉程度与能力
   - 注明具体强项与弱项
   - 找出需要纠正的误解

3. **学习目标定义**：
   - 指定 2-5 项具体学习成果
   - 同时包含知识与应用目标
   - 根据可用时间设定适当的目标高度

4. **学习风格偏好**：
   - 注明偏好方法（视觉、动手实践、理论等）
   - 说明过去特别有效的学习经历
   - 指出需要避免的方法

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 顺序逻辑 | 概念的适当递进 | 遵循明确的依赖关系 |
| 参与程度 | 与学习偏好的一致性 | 包含多种模态 |
| 练习质量 | 巩固活动的有效性 | 提供主动学习机会 |
| 目标对齐 | 活动与既定目标的联系 | 直达目标的路径 |

### 应用示例
```
/learning.facilitate{
    intent="Structure effective learning experiences for knowledge acquisition",
    input={
        subject="Data visualization with Python (matplotlib and seaborn)",
        current_knowledge="Intermediate Python programming, basic statistics, no visualization experience",
        learning_goals=["Create publication-quality visualizations", "Develop interactive dashboards", "Implement automated visualization pipelines"],
        learning_style_preferences="Hands-on projects with practical applications, visual examples, iterative building",
        time_constraints="10 hours per week for 4 weeks"
    },
    process=[...],
    output={...}
}
```
---

## 8. 场景规划协议

### 目的
探索可能的未来，为不确定环境制定稳健策略。

### 使用时机
- 不确定环境中的战略规划
- 风险评估与应急规划
- 创新与面向未来的准备
- 具有长期影响的决策

### 协议模板
```
/scenario.plan{
    intent="Explore possible futures and develop robust strategies",
    input={
        focal_question="[CENTRAL_STRATEGIC_QUESTION]",
        time_horizon="[PLANNING_TIMEFRAME]",
        key_uncertainties=["[UNCERTAINTY_1]", "[UNCERTAINTY_2]", "[UNCERTAINTY_3_OPTIONAL]"],
        driving_forces=["[FORCE_1]", "[FORCE_2]", "[FORCE_3_OPTIONAL]"],
        current_situation="[RELEVANT_CONTEXT_AND_STARTING_POINT]"
    },
    process=[
        /identify{action="Define key factors and driving forces"},
        /analyze{action="Assess impact and uncertainty of factors"},
        /construct{
            action="Develop 3-4 distinct, plausible scenarios",
            substeps=[
                /name{action="Create memorable scenario title"},
                /narrate{action="Describe scenario evolution and key events"},
                /detail{action="Explore implications for stakeholders"}
            ]
        },
        /identify{action="Extract strategic insights across scenarios"},
        /develop{action="Create robust strategies and early indicators"}
    ],
    output={
        scenarios=[
            {name="[SCENARIO_1_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"},
            {name="[SCENARIO_2_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"},
            {name="[SCENARIO_3_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"}
        ],
        robust_strategies="[APPROACHES_EFFECTIVE_ACROSS_SCENARIOS]",
        early_indicators="[SIGNS_INDICATING_SCENARIO_EMERGENCE]",
        key_uncertainties="[CRITICAL_FACTORS_TO_MONITOR]",
        strategic_recommendations="[IMMEDIATE_AND_LONG-TERM_ACTIONS]"
    }
}

I'd like to develop scenario plans around this focal question using the information I've provided. Please acknowledge and proceed with the scenario planning process.
```
### 实施指南

1. **核心问题定义**：
   - 清晰表述核心战略问题
   - 确保范围与相关性适当
   - 聚焦决策需求

2. **时间跨度选择**：
   - 选择适当时间范围（通常 3-10 年）
   - 平衡可预见未来与有意义的变化
   - 考虑行业特有的时间因素

3. **关键不确定性识别**：
   - 选择 2-4 项影响重大的关键不确定性
   - 聚焦真正不确定的因素（而非既定因素）
   - 包含不同类型（技术、社会、经济等）

4. **驱动力分析**：
   - 识别塑造环境的主要趋势与因素
   - 同时包含外部与内部驱动力
   - 考虑 STEEP 因素（社会、技术、经济、环境、政治）

### 性能指标

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 场景合理性 | 逻辑连贯性与可信度 | 无空想或矛盾 |
| 场景差异性 | 场景之间的实质差异 | 清晰、对照鲜明的未来 |
| 战略实用性 | 从场景得出的可执行见解 | 对决策有具体启示 |
| 指标质量 | 早期预警信号的实用性 | 可观察的先行指标 |

### 应用示例
```
/scenario.plan{
    intent="Explore possible futures and develop robust strategies",
    input={
        focal_question="How should our retail business adapt to changing consumer behavior and technology over the next decade?",
        time_horizon="10 years (2025-2035)",
        key_uncertainties=["Pace and nature of AI/automation adoption", "Consumer preferences for physical vs. digital experiences", "Regulatory environment for data and privacy"],
        driving_forces=["Aging demographics in core markets", "Climate change impacts on supply chains", "Increasing economic inequality", "Metaverse and virtual reality development"],
        current_situation="Mid-sized retail chain with 60% revenue from physical stores, growing e-commerce presence, limited data analytics capabilities"
    },
    process=[...],
    output={...}
}
```

---

## 高级协议整合

### 组合协议以处理复杂交互

面对复杂需求时，协议可以顺序组合，也可以嵌套使用：

```
/sequence{
    steps=[
        /problem.define{...},
        /debate.structured{...},
        /decision.analyze{...}
    ]
}
```

### 协议调整指南

1. **增加专门的流程步骤**：
   ```
   /extract.information{
       ...
       process=[
           ...,
           /specialize{action="Domain-specific analysis step"}
       ]
   }
   ```

2. **扩展输入参数**：
   ```
   /learning.facilitate{
       ...
       input={
           ...,
           accessibility_needs="[SPECIFIC_ACCESSIBILITY_REQUIREMENTS]"
       }
   }
   ```

3. **增强输出规格**：
   ```
   /scenario.plan{
       ...
       output={
           ...,
           visual_timeline="[GRAPHICAL_REPRESENTATION_OF_SCENARIOS]"
       }
   }
   ```

## 性能优化技巧

### 词元效率

1. **优先处理输入要素**：
   - 只包含必要的上下文
   - 列表用项目符号，不用叙述性长句
   - 尽可能引用外部信息

2. **流程精简**：
   - 对较简单的任务减少流程步骤
   - 适当合并相关步骤
   - 删除不产生价值的子步骤

3. **输出聚焦**：
   - 只指定需要的输出要素
   - 要求合适的详细程度
   - 用结构化格式提升效率

### 协议选择的心智模型

1. **花园模型**：
   - 哪种协议最能培育我需要的思想？
   - 需要怎样的照料与修剪？
   - 如何确保可持续的生长？

2. **河流模型**：
   - 信息流的源头在哪里？
   - 我希望对话流向何处？
   - 哪些障碍可能使水流改道？

3. **预算模型**：
   - 这次交互的词元预算是多少？
   - 哪些投入回报最高？
   - 如何把浪费降到最低？

## 持续改进

### 协议精炼流程

1. **记录结果**：
   - 记录协议产出
   - 标注任何偏差或困难
   - 全程跟踪 AI 行为

2. **评估表现**：
   - 与既定指标对比
   - 识别优点与弱点
   - 记录意外收益或局限

3. **精炼要素**：
   - 调整输入参数，提升清晰度与完整性
   - 依据实际效果修改流程步骤
   - 更新输出规格，使其更贴合需求

4. **迭代测试**：
   - 把精炼后的协议应用到相似场景
   - 比较各次迭代的表现
   - 记录渐进式改进

### 协议版本系统

要跟踪协议的演进，可使用简单的版本号记法：

```
/protocol.name.v1.2{...}
```

其中：
- 第一个数字（1）：主版本号（结构性变更）
- 第二个数字（2）：次版本号（参数或流程的精炼）

为每个版本附上变更说明：

```
/extract.information.v1.2{
    meta={
        version_history=[
            {version="1.0", date="2025-02-10", changes="Initial release"},
            {version="1.1", date="2025-03-15", changes="Added confidence metrics to output"},
            {version="1.2", date="2025-04-22", changes="Enhanced special_focus parameter"}
        ]
    },
    ...
}
```

## 对话协议中的场动力学

> *「你的场的品质，决定了其中会涌现出什么。」*

对话协议会创造语义场，以微妙而强大的方式塑造交互。理解场动力学，有助于设计更有效的协议。

### 场动力学的核心概念

1. **吸引子**：对话自然趋向的稳定模式
   - 每个协议都会创造特定的吸引域
   - 设计良好的协议能维持期望的吸引子

2. **边界**：界定对话空间的限定
   - 清晰的边界防止漂移、保持专注
   - 可渗透的边界允许有益的探索

3. **共振**：对某些主题或模式的放大
   - 协议可以创造共振场，强化某些特质
   - 有意的共振可提升连贯性与深度

4. **残差**：向前传递的持久影响
   - 有效的协议留下有生产性的残差
   - 符号残差为后续交互奠定基础

### 应用场动力学

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            FIELD DYNAMICS ENHANCEMENT               │
│                                                     │
│  Add to any protocol:                               │
│                                                     │
│  field_dynamics={                                   │
│    attractors: ["[PRIMARY_ATTRACTOR]", "[SECONDARY]"],│
│    boundaries: {                                    │
│      firm: ["[FIRM_BOUNDARY]"],                     │
│      permeable: ["[PERMEABLE_BOUNDARY]"]            │
│    },                                               │
│    resonance: ["[RESONANCE_PATTERN]"],              │
│    residue: {                                       │
│      target: "[DESIRED_SYMBOLIC_RESIDUE]",          │
│      persistence: "[HIGH|MEDIUM|LOW]"               │
│    }                                                │
│  }                                                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**示例应用**：

```
/debate.structured{
    ...
    field_dynamics={
        attractors: ["evidence-based reasoning", "charitable interpretation"],
        boundaries: {
            firm: ["personal attacks", "logical fallacies"],
            permeable: ["creative analogies", "interdisciplinary connections"]
        },
        resonance: ["intellectual curiosity", "nuanced understanding"],
        residue: {
            target: "multiple valid perspectives can coexist",
            persistence: "HIGH"
        }
    },
    ...
}
```

## 协议库管理

随着你积累的协议越来越多，把它们组织好对于复用和改进至关重要。

### 个人协议库模板

创建一个个人协议库的 Markdown 文件：

```markdown
# Personal Protocol Library

## Conversation Protocols

### Daily Use
- [Extract Information v1.2](#extract-information)
- [Structured Debate v2.0](#structured-debate)

### Special Purpose
- [Scenario Planning v1.0](#scenario-planning)
- [Problem Definition v1.3](#problem-definition)

## Protocol Definitions

### Extract Information
```
/extract.information.v1.2{
    // Full protocol definition
}
```

### Structured Debate
```
/debate.structured.v2.0{
    // Full protocol definition
}
```
```

### 与笔记系统整合

协议可以与常用笔记及知识管理系统整合：

1. **Obsidian**：
   - 创建专用协议文件夹
   - 使用模板插件快速插入
   - 将协议链接到相关笔记

2. **Notion**：
   - 创建协议数据库
   - 包含用例、效果评分等元数据
   - 使用模板快速添加到页面

3. **Roam Research**：
   - 创建带块引用的协议块
   - 按不同用例为协议添加标签
   - 构建包含协议的工作流模板

## 协议开发流程

创建自己的协议遵循结构化路径：
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            PROTOCOL DEVELOPMENT CYCLE               │
│                                                     │
│  1. IDENTIFY NEED                                   │
│     • Recognize recurring conversation pattern      │
│     • Identify frustrations or inefficiencies       │
│     • Define desired outcomes                       │
│                                                     │
│  2. DESIGN STRUCTURE                                │
│     • Define core components (input, process, output)│
│     • Outline key process steps                     │
│     • Determine required parameters                 │
│                                                     │
│  3. PROTOTYPE & TEST                                │
│     • Create minimal viable protocol                │
│     • Test with various AI systems                  │
│     • Document performance                          │
│                                                     │
│  4. REFINE & OPTIMIZE                               │
│     • Enhance based on test results                 │
│     • Optimize for token efficiency                 │
│     • Improve clarity and usability                 │
│                                                     │
│  5. DOCUMENT & SHARE                                │
│     • Create usage guidelines                       │
│     • Define performance metrics                    │
│     • Share with community                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```
### 协议设计工作表

使用此工作表开发新协议：
```
## Protocol Design Worksheet

### 1. Basic Information
- Protocol Name: _______________
- Purpose: _______________
- Use Cases: _______________

### 2. Core Components
- Input Parameters:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- Process Steps:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- Output Elements:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________

### 3. Field Dynamics
- Primary Attractors: _______________
- Firm Boundaries: _______________
- Desired Resonance: _______________
- Target Residue: _______________

### 4. Implementation Notes
- Token Efficiency Considerations: _______________
- Integration With Other Protocols: _______________
- Version History Plan: _______________

### 5. Evaluation Plan
- Success Metrics: _______________
- Testing Approach: _______________
- Refinement Criteria: _______________
```
## 结论：对话协议的未来

对话协议代表人机交互的根本转变。通过明确协议构建对话，我们从不可预测、临时拼凑的交流转向一致、高效、有目的的协作。

构建协议库时，请记住以下原则：

1. **从简单开始**：先用基础协议满足常见需求
2. **持续迭代**：根据实际使用情况完善
3. **分享与协作**：与他人交换协议
4. **以场思考**：考虑你正在创建的对话场
5. **优先保证清晰**：清晰结构带来清晰结果

借助这些原则与本指南中的协议模板，你已做好准备，将不可预测的 AI 对话转变为可靠、高效的协作。

**反思问题**：这些协议除了改变你与 AI 的交互，还可能如何改变你对有效沟通的整体理解？

---

> *「好的对话与卓越对话之间的差别，不在运气，而在架构。」*

---

## 附录：速查

### 协议基本结构
```
/protocol.name{
    intent="Clear statement of purpose",
    input={...},
    process=[...],
    output={...}
}
```
### 常用处理动作

- `/analyze`：系统地检查信息
- `/synthesize`：将元素组合成连贯整体
- `/evaluate`：对照标准评估
- `/prioritize`：确定相对重要性
- `/structure`：按逻辑组织信息
- `/verify`：确认准确性或有效性
- `/explore`：探索可能性
- `/refine`：通过迭代改进

### 场动力学快速配置
```
field_dynamics={
    attractors: ["focus", "clarity"],
    boundaries: {
        firm: ["off-topic", "vagueness"],
        permeable: ["relevant examples", "useful analogies"]
    },
    resonance: ["understanding", "insight"],
    residue: {
        target: "actionable knowledge",
        persistence: "MEDIUM"
    }
}
```
### 协议选择指南

| 需求 | 推荐协议 |
|------|----------------------|
| 提取具体信息 | `/extract.information` |
| 探索多种视角 | `/debate.structured` |
| 通过反馈改进工作 | `/feedback.progressive` |
| 做出复杂决策 | `/decision.analyze` |
| 建立共同理解 | `/align.mutual` |
| 清晰定义问题 | `/problem.define` |
| 构建结构化学习体验 | `/learning.facilitate` |
| 探索可能的未来 | `/scenario.plan` |
