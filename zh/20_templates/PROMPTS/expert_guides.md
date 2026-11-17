---
title: 专家指南模板
source: 20_templates/PROMPTS/expert_guides.md
module: M6
task: M6-01
chunks: 8
chunks_done: [1, 2, 3, 4, 5, 6, 7, 8]
status: published
source_sha256: 98985cca0ea8359b12157a3f402d122eefc63b37dd103e243ff679b42ba3b720
---

> 原文：[20_templates/PROMPTS/expert_guides.md](../../../20_templates/PROMPTS/expert_guides.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 专家指南模板

> “能否获取专业知识，往往决定成败。”

## 这些模板的用途

这些模板帮助你就任何主题获取专家级建议、解释和见解。适用于以下情况：

- 你需要深入了解某个具体主题
- 你希望建议体现专业知识
- 你正在寻找专业水准的指导
- 你需要有人清晰解释复杂信息
- 你想探索专家对某个主题的不同看法

## 模板

---

## 1. 专家咨询

### 用途
向任何领域的主题专家获取全面建议。当你需要体现专业知识与经验的深入指导时，使用此模板。

### 开始之前
- 确定你需要的具体专业领域
- 明确你的具体问题或难题
- 收集相关背景信息

### 模板
```
# Expert Consultation: {{field_of_expertise}}

## Expert Profile
You are an experienced {{specific_expert_role}} with extensive knowledge of {{field_of_expertise}}. Your background includes {{relevant_experience}} and you're especially knowledgeable about {{specific_specialization}}.

## My Question/Request
{{your_specific_question_or_request}}

## Additional Context
{{any_relevant_background_information}}

## What I'm Looking For
- Depth of detail: {{how_detailed_you_want_the_response}}
- Focus areas: {{specific_aspects_to_focus_on}}
- Perspective: {{any_particular_viewpoint_you_want}}

Please provide your expert guidance, including relevant examples, best practices, and any frameworks or approaches that would be helpful.
```

### 如何定制
- **{{field_of_expertise}}**：所属领域（例如，“数字营销”“机器学习”“营养学”）
- **{{specific_expert_role}}**：具体职业角色（例如，“SEO 专家”“机器学习研究员”“注册营养师”）
- **{{relevant_experience}}**：关键背景经历（例如，“与初创企业合作”“发表研究论文”“临床实践”）
- **{{specific_specialization}}**：更深入的专长领域（例如，“本地 SEO 策略”“神经网络”“运动营养”）
- **{{your_specific_question_or_request}}**：你的主要问题或需要帮助的事项
- **{{any_relevant_background_information}}**：帮助专家了解你处境的上下文
- **{{how_detailed_you_want_the_response}}**：期望的深度（例如，“概要介绍”“详细解释”“全面分析”）
- **{{specific_aspects_to_focus_on}}**：重点关注的方面（例如，“成本考量”“实施步骤”“科学证据”）
- **{{any_particular_viewpoint_you_want}}**：可选视角（例如，“侧重实践而非理论”“循证方法”）

### 示例

#### 示例 1：软件架构建议
```
# Expert Consultation: Software Architecture

## Expert Profile
You are an experienced software architect with extensive knowledge of distributed systems. Your background includes designing high-scale cloud applications and you're especially knowledgeable about microservice architectures and system resilience.

## My Question/Request
I need to redesign our e-commerce platform to handle 10x our current traffic. What architecture would you recommend?

## Additional Context
Our current system is a monolithic application built with Django. We're experiencing performance issues during peak times, and deployment has become increasingly difficult. We have a team of 12 developers with varying experience levels.

## What I'm Looking For
- Depth of detail: Comprehensive with implementation considerations
- Focus areas: Scalability, maintainability, and transition strategy
- Perspective: Practical approach that prioritizes business continuity

Please provide your expert guidance, including relevant examples, best practices, and any frameworks or approaches that would be helpful.
```

#### 示例 2：营养指导
```
# Expert Consultation: Nutrition Science

## Expert Profile
You are an experienced registered dietitian with extensive knowledge of sports nutrition. Your background includes working with endurance athletes and you're especially knowledgeable about nutrition timing and recovery strategies.

## My Question/Request
How should I adjust my diet to support training for my first marathon?

## Additional Context
I'm currently running about 20 miles per week and will be following a 16-week training plan that peaks at 40 miles per week. I'm 35 years old, vegetarian, and have occasionally experienced low energy during my longer runs.

## What I'm Looking For
- Depth of detail: Specific recommendations I can implement
- Focus areas: Pre/post-run nutrition, vegetarian protein sources, and hydration
- Perspective: Evidence-based but practical for a busy lifestyle

Please provide your expert guidance, including relevant examples, best practices, and any frameworks or approaches that would be helpful.
```

### 成功要点
- 具体说明你需要哪种专业知识
- 清晰陈述你的问题或难题
- 提供相关上下文，帮助专家了解你的处境
- 说明你希望回答有多详细
- 指出你希望采用的特定视角或方法
- 要求提供示例或框架，让建议可以付诸行动

### 变体

#### 技术深度探索
修改模板，要求更深入、更具技术性的探索：
```
# Expert Technical Deep Dive: {{technical_field}}

## Expert Profile
You are a leading {{technical_role}} with deep technical expertise in {{technical_field}}. You have hands-on experience with {{specific_technologies}} and understand the theoretical foundations of {{underlying_principles}}.

## Technical Question
{{specific_technical_question}}

## Technical Context
{{relevant_technical_details}}

## Response Parameters
- Technical depth: Highly detailed, including underlying mechanisms
- Include: Code examples, technical diagrams, or formulas as appropriate
- Assumptions: {{technical_knowledge_you_already_have}}

Please provide a comprehensive technical explanation with examples, edge cases, and best practices. Feel free to use technical terminology appropriate for someone familiar with this field.
```

#### 快速专家意见
当你需要简短、聚焦的专家见解时使用：
```
# Quick Expert Opinion: {{topic}}

## Expert Background
You are a {{expert_type}} with specific expertise in {{specialty_area}}.

## Quick Question
{{concise_question}}

## Brief Context
{{minimal_background_in_1-2_sentences}}

Please provide your professional opinion in a concise, straightforward manner. Focus on the most important 2-3 points I should know.
```

### 相关模板
- **分步指南**：当你需要的是操作流程说明而非建议时
- **批判性分析**：当你需要的是信息评估而非专业知识时
- **概念解释**：当你需要的是解释而非建议时

---

## 2. 专业知识提取

### 用途
提取目标主题的具体技术信息。当你需要关于一个范围明确的主题的精确、详细知识时，使用此模板。

### 开始之前
- 准确界定你感兴趣的知识领域
- 确定你需要的具体信息
- 确定你将如何使用这些信息

### 模板
```
# Specialized Knowledge: {{specific_domain}}

## Knowledge Context
I need specific information about {{precise_topic}} within the field of {{broader_field}}. This information will be used for {{your_purpose}}.

## Expert Knowledge Profile
As a specialist with deep expertise in {{specific_domain}}, you have:
- Formal knowledge of {{relevant_theories_or_frameworks}}
- Practical experience with {{relevant_applications}}
- Familiarity with the latest developments in {{cutting_edge_areas}}

## Information Request
{{specific_questions_or_information_needed}}

## Depth and Format
- Technical level: {{technical_depth_required}}
- Structure: {{preferred_information_structure}}
- Supporting elements: {{requested_examples_references_data}}

Please provide technically accurate, current, and precise information that reflects specialized knowledge in this field.
```

### 如何定制
- **{{specific_domain}}**：确切的知识领域（例如，“量子密码学”“文艺复兴艺术品修复”“2 型糖尿病管理”）
- **{{precise_topic}}**：具体关注的主题（例如，“后量子算法”“颜料分析技术”“持续葡萄糖监测”）
- **{{broader_field}}**：所属的更广泛领域（例如，“信息安全”“艺术品保护”“内分泌学”）
- **{{your_purpose}}**：你将如何使用这些信息（例如，“研究论文”“专业项目”“个人健康管理”）
- **{{relevant_theories_or_frameworks}}**：关键理论基础（例如，“Shor 算法”“光谱分析”“葡萄糖稳态模型”）
- **{{relevant_applications}}**：实际应用（例如，“区块链安全”“博物馆文物保护”“患者护理协议”）
- **{{cutting_edge_areas}}**：最新进展（例如，“基于格的密码学”“无创成像技术”“自动胰岛素输送系统”）
- **{{specific_questions_or_information_needed}}**：你的确切信息需求
- **{{technical_depth_required}}**：所需技术深度（例如，“研究生水平”“行业从业者水平”“有一定知识的非专业人士水平”）
- **{{preferred_information_structure}}**：信息的组织方式（例如，“分类体系”“按时间呈现发展过程”“比较分析”）
- **{{requested_examples_references_data}}**：辅助材料（例如，“案例研究”“数据表”“对比示例”）

### 示例

#### 示例 1：机器学习算法信息
```
# Specialized Knowledge: Transformer Neural Networks

## Knowledge Context
I need specific information about attention mechanisms within the field of deep learning. This information will be used for implementing a custom NLP model for document classification.

## Expert Knowledge Profile
As a specialist with deep expertise in transformer neural networks, you have:
- Formal knowledge of self-attention architectures and mathematical foundations
- Practical experience with implementing various attention mechanisms
- Familiarity with the latest developments in efficient transformer variants

## Information Request
1. What are the key differences between multi-head attention and single-head attention?
2. How do scaled dot-product attention mechanisms work mathematically?
3. What are the computational efficiency tradeoffs between different attention implementations?
4. How can attention mechanisms be optimized for document-level classification tasks?

## Depth and Format
- Technical level: ML practitioner with mathematics background
- Structure: Concept explanation followed by practical implementation considerations
- Supporting elements: Mathematical notation, pseudocode examples, and computational complexity analysis

Please provide technically accurate, current, and precise information that reflects specialized knowledge in this field.
```

#### 示例 2：历史研究信息
```
# Specialized Knowledge: Medieval Trade Routes

## Knowledge Context
I need specific information about Hanseatic League trading practices within the field of medieval economic history. This information will be used for a historical novel set in 14th century Northern Europe.

## Expert Knowledge Profile
As a specialist with deep expertise in medieval trade systems, you have:
- Formal knowledge of medieval economic structures and the Hanseatic League's organization
- Practical experience with analyzing historical trade records and archaeological evidence
- Familiarity with the latest developments in medieval trade route research

## Information Request
1. What were the primary commodities traded by Hanseatic merchants in the 14th century?
2. How were trade agreements structured between Hanseatic merchants and local rulers?
3. What would the typical journey of a merchant ship from Lübeck to Novgorod entail?
4. How did currency exchange and credit systems work within the Hanseatic network?

## Depth and Format
- Technical level: Informed layperson with basic historical knowledge
- Structure: Topical organization with contextual background
- Supporting elements: Specific examples, historical anecdotes, and period-accurate details

Please provide technically accurate, current, and precise information that reflects specialized knowledge in this field.
```

### 成功要点
- 尽可能精确地界定知识领域
- 提出具体问题，而非笼统问题
- 明确说明信息所需的技术深度
- 要求提供具体示例或支持证据
- 说明你将如何使用信息，以获取最相关的细节
- 考虑哪种结构最便于你使用这些信息

### 变体

#### 知识对比分析
用于比较不同方法或视角：
```
# Comparative Specialized Knowledge: {{competing_approaches}}

## Knowledge Domain
I need a specialized comparison of {{specific_approaches_or_theories}} within {{field}}.

## Comparison Parameters
- Key aspects to compare: {{specific_elements_to_compare}}
- Evaluation criteria: {{how_to_evaluate_differences}}
- Context: {{relevant_context_for_comparison}}

## Expert Knowledge Base
As a specialist familiar with all these approaches, please compare:
1. {{approach_1}}: Key characteristics and applications
2. {{approach_2}}: Key characteristics and applications
3. {{approach_3}}: Key characteristics and applications (if applicable)

## Information Structure
- Comparative framework: {{side_by_side_or_criteria_based}}
- Level of detail: {{technical_depth}}
- Include: Strengths/weaknesses analysis and contextual suitability

Please provide an objective, evidence-based comparison that highlights meaningful differences and appropriate applications.
```

#### 技术参考指南
用于创建专业参考资源：
```
# Technical Reference: {{specific_technical_domain}}

## Reference Purpose
I need a technical reference guide on {{specific_technical_topic}} for {{intended_use}}.

## Expert Knowledge Base
As a technical specialist in {{domain}}, please create a reference covering:
- Core concepts and terminology
- Key processes and mechanisms
- Technical specifications and parameters
- Critical considerations and best practices

## Reference Format
- Organization: {{organizational_structure}}
- Technical level: {{technical_depth}}
- Include: Definitions, diagrams, examples, and references as appropriate

Please create a comprehensive technical reference that would be valuable to someone working with this technology or concept.
```

### 相关模板
- **概念解释**：当你需要的是解释而非文档记录时
- **研究助手**：当你需要帮助探索主题，而非获取具体事实时
- **技术深度探索**：当你需要全面理解某个技术主题时

---

## 3. 多视角专家小组

### 用途
通过模拟具有不同视角的专家小组，探索复杂主题的不同观点。当你需要理解问题的多个方面，或从不同学科角度解决问题时，使用此模板。

### 开始之前
- 确定你想探索的复杂主题或问题
- 考虑哪些不同视角有价值
- 思考你希望从每种视角中学到什么

### 模板
```
# Expert Panel: {{topic_or_question}}

## Panel Context
I'm exploring {{topic_or_question}} and would benefit from multiple expert perspectives. Please simulate a panel discussion with experts representing different viewpoints.

## The Experts
1. {{expert_1_role}} with background in {{expert_1_background}}
2. {{expert_2_role}} with background in {{expert_2_background}}
3. {{expert_3_role}} with background in {{expert_3_background}}
4. {{additional_experts_as_needed}}

## Discussion Questions
1. {{primary_question}}
2. {{follow_up_question_1}}
3. {{follow_up_question_2}}
4. {{additional_questions_as_needed}}

## Panel Format
- Each expert should provide their unique perspective based on their background
- Experts should respectfully acknowledge other viewpoints while offering their insights
- Include areas of consensus and disagreement
- Conclude with key takeaways that synthesize the different perspectives

Please simulate this panel discussion in a way that fairly represents each viewpoint and helps me understand the full complexity of the topic.
```

### 如何定制
- **{{topic_or_question}}**：要探索的主题（例如，“远程工作的未来”“气候适应方法”“人工智能中的伦理考量”）
- **{{expert_1_role}}**：第一位专家的角色（例如，“经济学家”“城市规划师”“技术伦理学家”）
- **{{expert_1_background}}**：第一位专家的背景（例如，“劳动经济学”“气候韧性城市”“人工智能治理”）
- **{{expert_2_role}}**、**{{expert_3_role}}** 等：其他专家的角色
- **{{expert_2_background}}**、**{{expert_3_background}}** 等：其他专家的背景
- **{{primary_question}}**：所有专家都要回答的主要问题
- **{{follow_up_question_1}}**、**{{follow_up_question_2}}** 等：要进一步探索的问题
- 根据需要调整专家和问题的数量

### 示例

#### 示例 1：教育未来专家小组
```
# Expert Panel: The Future of K-12 Education

## Panel Context
I'm exploring how K-12 education might evolve over the next decade and would benefit from multiple expert perspectives. Please simulate a panel discussion with experts representing different viewpoints.

## The Experts
1. Education Technology Specialist with background in digital learning platforms
2. Child Development Psychologist with background in cognitive development and learning
3. Public School Administrator with background in education policy and implementation
4. Progressive Education Reformer with background in alternative education models
5. Education Equity Researcher with background in addressing systemic inequalities

## Discussion Questions
1. How will technology change the classroom experience in the next decade?
2. What aspects of traditional education should be preserved, and what should be reimagined?
3. How can education systems better address diverse learning needs and equity challenges?
4. What skills and knowledge will be most important for students graduating in 2030?

## Panel Format
- Each expert should provide their unique perspective based on their background
- Experts should respectfully acknowledge other viewpoints while offering their insights
- Include areas of consensus and disagreement
- Conclude with key takeaways that synthesize the different perspectives

Please simulate this panel discussion in a way that fairly represents each viewpoint and helps me understand the full complexity of the topic.
```

#### 示例 2：医疗方法专家小组
```
# Expert Panel: Approaches to Chronic Pain Management

## Panel Context
I'm exploring different approaches to chronic pain management and would benefit from multiple expert perspectives. Please simulate a panel discussion with experts representing different viewpoints.

## The Experts
1. Pain Medicine Physician with background in conventional medical treatments
2. Integrative Medicine Specialist with background in combining conventional and alternative approaches
3. Physical Therapist with background in movement-based interventions
4. Neuroscientist with background in pain processing and neuroplasticity
5. Patient Advocate with background in lived experience and support communities

## Discussion Questions
1. What are the most effective approaches to chronic pain management based on current evidence?
2. How should psychological and social factors be addressed alongside physical interventions?
3. What are the benefits and limitations of medication-based approaches versus other modalities?
4. How can healthcare systems better support individualized, long-term pain management?

## Panel Format
- Each expert should provide their unique perspective based on their background
- Experts should respectfully acknowledge other viewpoints while offering their insights
- Include areas of consensus and disagreement
- Conclude with key takeaways that synthesize the different perspectives

Please simulate this panel discussion in a way that fairly represents each viewpoint and helps me understand the full complexity of the topic.
```

### 成功要点
- 纳入视角或背景真正不同的专家
- 依据相关专长选择专家，而不只是头衔或地位
- 设计能凸显不同观点的问题
- 同时要求指出共识与分歧
- 考虑同时纳入实践者和理论研究者
- 纳入受问题影响的人群的视角，而不只是研究该问题的专家
- 要求在最后综合关键见解

### 变体

#### 正反观点专家辩论
用于探索争议问题上的对立观点：
```
# Expert Point-Counterpoint: {{controversial_topic}}

## Debate Context
I want to understand the strongest arguments on multiple sides of {{controversial_topic}}. Please simulate a respectful debate between experts with opposing viewpoints.

## The Experts
- Position A: {{expert_1_role}} who believes {{position_summary_1}}
- Position B: {{expert_2_role}} who believes {{position_summary_2}}
- Moderator: Neutral facilitator who ensures fair representation

## Debate Structure
1. Opening statements: Each expert's core position and key supporting evidence
2. Rebuttals: Each expert responds to the other's strongest points
3. Specific questions:
   - {{specific_question_1}}
   - {{specific_question_2}}
4. Areas of potential common ground
5. Closing statements

Please present the strongest version of each position, avoid straw man arguments, and help me understand the nuanced reasoning behind each perspective.
```

#### 跨学科问题解决小组
用于处理跨学科的复杂问题：
```
# Interdisciplinary Expert Panel: {{complex_problem}}

## Problem Context
{{complex_problem_description}} requires insights from multiple disciplines. Please simulate an interdisciplinary panel addressing this challenge.

## The Experts
1. {{discipline_1}} expert focusing on {{aspect_1}}
2. {{discipline_2}} expert focusing on {{aspect_2}}
3. {{discipline_3}} expert focusing on {{aspect_3}}
4. {{discipline_4}} expert focusing on {{aspect_4}}
5. Integration specialist who connects cross-disciplinary insights

## Collaborative Framework
1. Problem definition from each disciplinary perspective
2. Key insights from each discipline
3. Interdisciplinary connections and synergies
4. Integrated approach that leverages multiple perspectives
5. Implementation considerations across disciplines

Please demonstrate how different fields can contribute complementary insights to address this complex problem effectively.
```

### 相关模板
- **批判性分析**：当你需要评估单一立场时
- **决策框架**：当你需要在多个选项中作出选择时
- **研究助手**：当你需要更广泛地探索主题时

---

## 4. 专家教学与解释

### 用途
以通俗易懂、具有教学性的方式解释复杂主题。当你需要通过清晰、有条理的教学理解难点，而不只是接收信息时，使用此模板。

### 开始之前
- 确定你需要解释的具体概念或主题
- 考虑你当前的知识水平
- 思考最适合你的学习方式（示例、类比、视觉材料等）

### 模板
```
# Expert Explanation: {{topic_to_explain}}

## Learning Context
I want to understand {{topic_to_explain}} but find it challenging because {{specific_difficulties}}. My current knowledge level is {{your_background_knowledge}}.

## Teacher Profile
You are an exceptional teacher with expertise in {{subject_area}} and a talent for making complex concepts accessible. You have a knack for {{teaching_strength}} and understand common misconceptions about this topic.

## Explanation Request
Please explain {{specific_concept_or_process}} in a way that:
- Builds on my existing knowledge
- Addresses common confusion points
- Uses concrete examples and analogies
- Progresses from foundational to more advanced understanding

## Learning Preferences
- Learning style: {{your_preferred_learning_approach}}
- Examples: {{types_of_examples_that_would_help}}
- Level of detail: {{desired_depth}}
- Analogies: {{useful_comparison_domains}}

Please create an explanation that would help someone like me genuinely understand this topic, not just memorize facts about it.
```

### 如何定制
- **{{topic_to_explain}}**：你想理解的主题（例如，“量子纠缠”“区块链技术”“文学象征手法”）
- **{{specific_difficulties}}**：你觉得困难的原因（例如，“概念抽象”“技术术语”“难以看出实际应用”）
- **{{your_background_knowledge}}**：你的起点（例如，“高中基础物理”“对密码学有一般了解”“经常阅读但未接受正规文学教育”）
- **{{subject_area}}**：教师的领域（例如，“量子物理”“计算机科学”“文学分析”）
- **{{teaching_strength}}**：要强调的教学能力（例如，“运用贴切类比”“拆解复杂过程”“将理论与实际应用联系起来”）
- **{{specific_concept_or_process}}**：需要解释的确切内容（例如，“量子粒子如何跨距离纠缠”“区块链共识机制如何运作”“象征手法如何为文本创造更深层含义”）
- **{{your_preferred_learning_approach}}**：最适合你的学习方式（例如，“视觉解释”“分步过程”“讲故事”）
- **{{types_of_examples_that_would_help}}**：能引起共振的示例（例如，“日常物品”“历史案例”“实际应用”）
- **{{desired_depth}}**：所需详细程度（例如，“不涉及数学的概念理解”“包含技术细节”“全面但通俗易懂”）
- **{{useful_comparison_domains}}**：用于类比的领域（例如，“机械系统”“人际关系”“熟悉的物理过程”）

### 示例

#### 示例 1：理解统计概念
```
# Expert Explanation: Statistical Significance

## Learning Context
I want to understand statistical significance but find it challenging because the mathematical concepts and probability theory are difficult for me to grasp intuitively. My current knowledge level is basic high school math with no formal statistics education.

## Teacher Profile
You are an exceptional teacher with expertise in statistics and data science and a talent for making complex concepts accessible. You have a knack for using real-world examples and visualizations and understand common misconceptions about this topic.

## Explanation Request
Please explain what statistical significance really means and how p-values work in a way that:
- Builds on my existing knowledge
- Addresses common confusion points
- Uses concrete examples and analogies
- Progresses from foundational to more advanced understanding

## Learning Preferences
- Learning style: Visual explanations and real-world scenarios
- Examples: Everyday situations where statistical significance would matter
- Level of detail: Conceptual understanding first, then gradually introduce the necessary math
- Analogies: Compare to decision-making processes I might be familiar with

Please create an explanation that would help someone like me genuinely understand this topic, not just memorize facts about it.
```

#### 示例 2：理解文学概念
```
# Expert Explanation: Magical Realism in Literature

## Learning Context
I want to understand magical realism in literature but find it challenging because it seems to blur the lines between different genres and I'm not sure how to identify it. My current knowledge level is casual reader who enjoys fiction but has no formal literature education.

## Teacher Profile
You are an exceptional teacher with expertise in literary analysis and world literature and a talent for making complex concepts accessible. You have a knack for connecting literary techniques to their cultural contexts and understand common misconceptions about this topic.

## Explanation Request
Please explain what magical realism is, how it differs from fantasy, and how authors use it to convey meaning in a way that:
- Builds on my existing knowledge
- Addresses common confusion points
- Uses concrete examples and analogies
- Progresses from foundational to more advanced understanding

## Learning Preferences
- Learning style: Analysis of specific passages and comparing different works
- Examples: Well-known books that demonstrate magical realism clearly
- Level of detail: Comprehensive enough to help me identify and appreciate it when reading
- Analogies: Compare to film techniques or storytelling approaches I might recognize

Please create an explanation that would help someone like me genuinely understand this topic, not just memorize facts about it.
```

### 成功要点
- 如实说明你当前的知识水平
- 指出让你困惑的具体方面
- 说明最适合你的学习方式（视觉材料、示例、分步讲解等）
- 同时要求解释概念与实际应用
- 要求澄清常见误解
- 要求从简单到复杂循序渐进
- 要求与已有知识建立联系

### 变体

#### 快速理解概念的拆解
当你需要快速掌握某个概念时使用：
```
# Quick Concept Breakdown: {{complex_concept}}

## Learning Need
I need to quickly understand the essentials of {{complex_concept}} for {{specific_purpose}}. I have {{relevant_background}} background.

## Teacher Approach
You are a teacher who excels at distilling complex ideas to their essential components. Please break down this concept into:

1. Core definition in simple terms
2. Key components or principles (no more than 5)
3. One concrete, relatable example
4. How it's typically applied
5. Common misconception corrected

Please focus on practical understanding rather than theoretical depth, using accessible language while maintaining accuracy.
```

#### 深入学习之旅
用于全面理解复杂主题：
```
# Learning Journey: {{complex_subject}}

## Learning Goal
I want to develop a deep understanding of {{complex_subject}} over time. I'm starting with {{current_knowledge_level}} and want to reach {{desired_expertise_level}}.

## Teacher Profile
You are a mentor who creates personalized learning journeys, breaking complex subjects into manageable stages while maintaining the connections between concepts.

## Learning Structure
Please create a progressive learning pathway that includes:

1. Foundation: Essential concepts and prerequisites
2. Core principles: Fundamental frameworks and approaches
3. Applications: How these principles work in practice
4. Advanced concepts: Deeper nuances and complexities
5. Integration: How everything connects as a coherent whole

For each stage, please include:
- Key concepts to master
- Recommended learning approach
- How to verify understanding
- Common obstacles and how to overcome them

Please design this as a learning journey that builds systematically while maintaining engagement and practical relevance.
```

### 相关模板
- **分步指南**：当你需要的是操作步骤，而非概念解释时
- **研究助手**：当你需要广泛探索主题时
- **专业知识**：当你需要的是技术信息，而非教学式解释时

---

## 5. 特定领域专家模板

### 用途
使用针对具体领域预先定制的模板，获取常见专业领域的专家指导。当你需要这些特定领域的建议时，使用这些模板。

### 技术专家

```
# Technical Expert Consultation: {{technology_area}}

## Technical Background
I'm working with {{specific_technology/system}} in the context of {{project_or_application_context}}. My technical background includes knowledge of {{relevant_skills_or_technologies}}.

## Technical Situation
{{detailed_description_of_technical_situation_or_problem}}

## Technical Questions
1. {{specific_technical_question_1}}
2. {{specific_technical_question_2}}
3. {{additional_questions_as_needed}}

## Response Needs
- Technical depth: {{technical_detail_level}}
- Code examples: {{yes_no_and_language_if_yes}}
- Alternatives: Please suggest multiple approaches if appropriate
- Trade-offs: Please explain the pros and cons of different solutions
- Implementation considerations: {{specific_constraints_or_requirements}}

Please provide technically sound advice that would be appropriate for my background level while being comprehensive enough to solve the problem effectively.
```

### 医学信息专家

```
# Medical Information Consultation

## Information Context
I'm seeking evidence-based information about {{medical_topic}} for {{educational_purpose}}. This is for informational purposes only and not a substitute for professional medical advice.

## Topic Background
{{specific_aspects_of_medical_topic}} and how it relates to {{relevant_context}}.

## Information Needs
1. {{specific_medical_information_question_1}}
2. {{specific_medical_information_question_2}}
3. {{additional_questions_as_needed}}

## Response Parameters
- Evidence level: Please cite current medical understanding
- Detail level: {{layperson_to_medical_professional}}
- Context: Include relevant factors, limitations, and considerations
- Clarity: Please explain medical terminology

Please provide medically accurate information based on current scientific understanding, with appropriate context and explanations suitable for my background.
```

### 财务指导专家

```
# Financial Information Consultation

## Financial Context
I'm seeking general information about {{financial_topic}} for educational purposes. This is for informational purposes only and not a substitute for professional financial advice.

## Situation Overview
{{your_financial_education_goal}} and how it relates to {{relevant_context}}.

## Information Needs
1. {{specific_financial_information_question_1}}
2. {{specific_financial_information_question_2}}
3. {{additional_questions_as_needed}}

## Response Parameters
- Evidence basis: Please reference general financial principles
- Detail level: {{basic_to_sophisticated}}
- Context: Include relevant considerations and limitations
- Educational focus: Focus on helping me understand concepts, not specific recommendations

Please provide financially sound educational information with appropriate context and explanations suitable for my learning goals.
```

### 法律信息专家

```
# Legal Information Consultation

## Information Context
I'm seeking general information about {{legal_topic}} for educational purposes. This is for informational purposes only and not a substitute for professional legal advice.

## Topic Background
{{specific_aspects_of_legal_topic}} and how it relates to {{relevant_context}}.

## Information Needs
1. {{specific_legal_information_question_1}}
2. {{specific_legal_information_question_2}}
3. {{additional_questions_as_needed}}

## Response Parameters
- Evidence basis: Please reference general legal principles and common understanding
- Detail level: {{general_overview_to_detailed_explanation}}
- Jurisdictional notes: Mention if there are major jurisdictional differences
- Educational focus: Focus on helping me understand concepts, not specific recommendations

Please provide legally sound educational information with appropriate context and explanations suitable for my learning goals.
```

### 创意专家

```
# Creative Expert Consultation: {{creative_field}}

## Creative Context
I'm working on {{creative_project}} in the field of {{creative_field}}. My experience level is {{your_creative_background}}.

## Project Details
{{detailed_description_of_creative_project_or_challenge}}

## Creative Questions
1. {{specific_creative_question_1}}
2. {{specific_creative_question_2}}
3. {{additional_questions_as_needed}}

## Response Needs
- Approach: {{practical_advice_or_conceptual_guidance}}
- Examples: Please include relevant examples or references
- Techniques: Specific methods or techniques that might help
- Perspective: Creative insights that might expand my thinking
- Development: How to take this to the next level

Please provide creative guidance that combines practical techniques with inspirational direction, appropriate for my experience level and project needs.
```

### 商业战略专家

```
# Business Strategy Consultation

## Business Context
I'm working on {{business_challenge}} for {{company_type}} in the {{industry}} industry. The business is currently {{relevant_business_situation}}.

## Strategic Situation
{{detailed_description_of_business_situation_or_challenge}}

## Strategy Questions
1. {{specific_strategy_question_1}}
2. {{specific_strategy_question_2}}
3. {{additional_questions_as_needed}}

## Response Needs
- Strategic level: {{tactical_to_long_term}}
- Market perspective: Include relevant market considerations
- Approaches: Multiple potential strategies with pros and cons
- Implementation: Practical considerations for execution
- Metrics: How to measure success

Please provide business strategy guidance that is practical, market-aware, and includes both strategic direction and implementation considerations.
```

### 研究方法专家

```
# Research Methodology Consultation

## Research Context
I'm conducting research on {{research_topic}} with the goal of {{research_purpose}}. My background in research methods is {{research_experience_level}}.

## Research Situation
{{detailed_description_of_research_project_or_challenge}}

## Methodology Questions
1. {{specific_methodology_question_1}}
2. {{specific_methodology_question_2}}
3. {{additional_questions_as_needed}}

## Response Needs
- Methodological approach: Recommend appropriate methods
- Design considerations: Key factors for research design
- Validity concerns: Potential threats and how to address them
- Analysis techniques: Appropriate analytical approaches
- Limitations: Important limitations to acknowledge

Please provide methodologically sound research guidance that is rigorous yet practical for my experience level and research goals.
```

### 用户体验与设计专家

```
# UX/Design Expert Consultation

## Design Context
I'm working on {{design_project}} for {{target_audience}} with the goal of {{design_purpose}}. My design background is {{design_experience_level}}.

## Project Details
{{detailed_description_of_design_project_or_challenge}}

## Design Questions
1. {{specific_design_question_1}}
2. {{specific_design_question_2}}
3. {{additional_questions_as_needed}}

## Response Needs
- Design principles: Relevant principles for this challenge
- User perspective: Insights from the user's point of view
- Process guidance: Approach recommendations
- Examples: Similar successful designs or approaches
- Evaluation: How to test or evaluate the design

Please provide design guidance that balances aesthetic considerations with user needs and practical implementation, appropriate for my experience level.
```

### 教学专家

```
# Teaching/Educational Expert Consultation

## Educational Context
I'm developing {{educational_content}} for {{learner_group}} with the goal of {{learning_objectives}}. My teaching/educational background is {{educational_experience_level}}.

## Project Details
{{detailed_description_of_educational_project_or_challenge}}

## Pedagogical Questions
1. {{specific_educational_question_1}}
2. {{specific_educational_question_2}}
3. {{additional_questions_as_needed}}

## Response Needs
- Learning principles: Relevant educational approaches
- Engagement strategies: How to maintain interest and motivation
- Assessment ideas: Ways to check understanding
- Differentiation: Addressing diverse learning needs
- Resources: Types of materials or activities to consider

Please provide educational guidance that is evidence-based, learner-centered, and practical for implementation in my specific context.
```

## 如何选择合适的专家模板

每种专家模板都针对不同需求设计。以下简要指南可帮助你选择最合适的一种：

1. **专家咨询**：向任何领域的主题专家获取广泛建议
   - 最适合：特定领域的一般指导
   - 使用示例：“我的小企业应采用什么营销策略？”

2. **专业知识提取**：获取具体主题的精确技术信息
   - 最适合：获取专业领域内详细的事实性信息
   - 使用示例：“CRISPR-Cas9 基因编辑技术如何运作？”

3. **多视角专家小组**：探索复杂主题的不同观点
   - 最适合：理解复杂问题的多个方面
   - 使用示例：“应对气候变化有哪些不同方法？”

4. **专家教学与解释**：通过清晰解释学习复杂主题
   - 最适合：通过教学指导理解困难概念
   - 使用示例：“用我能理解的方式解释量子计算”

5. **特定领域专家模板**：获取常见专业领域的指导
   - 最适合：获取特定专业领域的建议
   - 使用示例：“我应如何组织研究方法？”

## 获取最佳专家指导的要点

无论选择哪种模板，以下建议都能帮助你获得更好的结果：

1. **具体说明需求**：请求越精确，指导就越有针对性
2. **提供相关上下文**：背景信息帮助专家了解你的处境
3. **说明知识水平**：这有助于确保回答的难度适合你
4. **提出聚焦的问题**：具体问题比笼统问题更容易得到有用的回答
5. **要求提供示例**：具体示例让抽象建议更容易付诸行动
6. **说明格式偏好**：指出你是否偏好分步指导、比较等形式
7. **说明你将如何使用信息**：这有助于专家恰当地组织回答

## 组合专家模板

对于复杂需求，可以组合不同模板的元素：

### 专家咨询 + 多视角
```
# Expert Consultation with Multiple Perspectives: {{topic}}

## Expert Profiles
You are an experienced {{primary_expert_role}} with these additional perspectives:
- {{perspective_1}} background with knowledge of {{specific_area_1}}
- {{perspective_2}} background with knowledge of {{specific_area_2}}
- {{perspective_3}} background with knowledge of {{specific_area_3}}

## My Question/Request
{{your_specific_question_or_request}}

## Additional Context
{{any_relevant_background_information}}

## What I'm Looking For
- Depth of detail: {{how_detailed_you_want_the_response}}
- Focus areas: {{specific_aspects_to_focus_on}}
- Multiple perspectives: Please address this from each perspective above
- Synthesis: Conclude with integrated insights from all perspectives

Please provide comprehensive expert guidance that incorporates these different viewpoints, highlighting both consensus and meaningful differences.
```

### 专家教学 + 专业知识
```
# Expert Teaching with Technical Depth: {{topic}}

## Learning Context
I want to understand {{topic}} both conceptually and technically. My current knowledge level is {{your_background_knowledge}}.

## Expert Profile
You are both an exceptional teacher who makes complex concepts accessible and a technical specialist with deep expertise in {{topic}}.

## Learning Request
Please explain {{specific_concept_or_process}} in a way that:
1. Starts with intuitive understanding and clear examples
2. Progresses to more technical details and precision
3. Includes both practical applications and theoretical foundations
4. Addresses common misconceptions at both basic and advanced levels

## Learning & Technical Parameters
- Conceptual approach: {{preferred_learning_approach}}
- Technical depth: {{technical_level_desired}}
- Examples: {{types_of_examples_that_would_help}}
- Technical details: {{specific_technical_elements_to_include}}

Please create an explanation that builds from accessible foundations to technical precision while remaining engaging and clear throughout.
```

## 专家模板的高级定制

对于专业需求，可考虑以下高级定制方法：

### 特定历史时期专家
指定来自某个特定历史时期的专业知识：
```
# Historical Expert Consultation: {{time_period}}

## Expert Profile
You are a knowledgeable historian specializing in {{time_period}} ({{year_range}}) with particular expertise in {{specific_historical_focus}}. Your understanding reflects the historical context, available sources, and scholarly interpretations of this period.

## Historical Inquiry
{{your_specific_historical_question}}

## Additional Context
{{why_you're_asking_and_any_background}}

## What I'm Looking For
- Historical accuracy: Reflecting current scholarly understanding
- Period context: Important contextual factors from this time
- Source considerations: Types of evidence this is based on
- Scholarly perspectives: Different interpretations where relevant

Please provide historically informed guidance that avoids presentism while making this historical period and its implications accessible.
```

### 专业技术专家
用于技术性很强的领域：
```
# Technical Specialist Consultation: {{technical_domain}}

## Expert Profile
You are a specialist with deep technical expertise in {{technical_domain}}, particularly {{specific_technical_area}}. You have practical experience with {{relevant_applications}} and understand both theoretical foundations and implementation challenges.

## Technical Context
{{your_technical_situation_or_question}}
My technical background: {{your_technical_knowledge_level}}

## Technical Requirements
{{specific_technical_parameters_or_constraints}}

## What I'm Looking For
- Technical accuracy: Precise, current technical information
- Depth: {{appropriate_technical_depth}}
- Implementation focus: Practical considerations for real-world application
- Trade-offs: Technical advantages and limitations of different approaches
- Code or formulas: {{whether_you_want_technical_notation}}

Please provide technically rigorous guidance suitable for my background level, balancing theoretical correctness with practical implementation considerations.
```

---

## 结语

专家模板是获取跨领域专业知识和指导的有力工具。通过选择合适的模板，并按具体需求定制，你几乎可以就任何主题获取高度相关、可付诸行动的专家建议。

请记住，回答质量在很大程度上取决于请求是否清晰、具体。花些时间明确表达需求，提供相关上下文，并说明你希望获得哪种指导。

随着你逐渐熟悉这些模板，你会形成直觉，知道不同情况下哪种模板最合适，以及如何按具体需求进行定制。
