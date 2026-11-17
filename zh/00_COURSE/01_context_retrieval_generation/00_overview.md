---
title: 上下文检索与生成
source: 00_COURSE/01_context_retrieval_generation/00_overview.md
module: M3
task: M3-02
chunks: 3
chunks_done: [1, 2, 3]
status: published
source_sha256: a5b81f50d6a8d7186efb8af5a6d44ede051fb57790268dc110fd833ee0af6b1b
---

> 原文：[00_COURSE/01_context_retrieval_generation/00_overview.md](../../../00_COURSE/01_context_retrieval_generation/00_overview.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 上下文检索与生成
## 从静态提示词到动态知识编排

> **模块 01** | *上下文工程（Context Engineering）课程：从基础到前沿系统*
> 
> 基于[上下文工程综述](https://arxiv.org/pdf/2507.13334) | 推进 Software 3.0 范式

---

## 学习目标

学完本模块后，你将理解并实现：

- **高级提示词工程**：从基础提示词到复杂的推理模板
- **外部知识集成**：RAG 基础与动态知识检索
- **动态上下文装配**：实时组合多来源信息
- **策略性上下文编排**：优化信息载荷，最大化模型效能

---

## 概念演进：从静态文本到智能知识编排

可以将上下文生成理解为向问题解决者提供信息的方式不断演进：从递给对方一份文档，到组织一座研究图书馆，再到配备一位清楚该收集哪些信息、如何呈现信息的智能研究助手。

### 阶段 1：静态提示词工程
```
"Solve this problem: [problem description]"
```
**上下文**：就像给对方一张指令单。简单直接，但受限于单份文档所能容纳的内容。

### 阶段 2：增强型提示词模式
```
"Let's think step by step:
1. First, understand the problem...
2. Then consider approaches...
3. Finally implement the solution..."
```
**上下文**：就像提供一套结构化方法。它能够引导思考过程，因此更有效，但仍受静态内容限制。

### 阶段 3：外部知识集成
```
[Retrieved relevant information from knowledge base]
"Given the following context: [external knowledge]
Now solve: [problem]"
```
**上下文**：就像能够使用一座研究图书馆。它可以纳入工作记忆无法容纳的专业知识和最新信息，因此能力强得多。

### 阶段 4：动态上下文装配
```
Context = Assemble(
    task_instructions + 
    relevant_retrieved_knowledge + 
    user_history + 
    domain_expertise + 
    real_time_data
)
```
**上下文**：就像有一位研究助手，从多个来源收集恰当的信息，并针对你的具体任务进行最优组织。

### 阶段 5：智能上下文编排
```
Adaptive Context System:
- Understands your goals and constraints
- Monitors your progress and adapts information flow
- Learns from outcomes to improve future context assembly
- Balances relevance, completeness, and cognitive load
```
**上下文**：就像有一位 AI 研究伙伴，不仅理解你需要知道什么，还理解你如何思考和学习，并持续优化信息环境，以获得最大效能。

---

## 数学基础

### 上下文形式化框架
根据我们的核心数学基础：
```
C = A(cinstr, cknow, ctools, cmem, cstate, cquery)
```

本模块主要关注 **cknow**（外部知识）和装配函数 **A**，具体为：

```
cknow = R(cquery, K)
```

其中：
- **R** 是检索函数
- **cquery** 是用户当前的请求
- **K** 是外部知识库

### 信息论优化
最优检索函数使相关信息最大化：
```
R* = arg max_R I(Y*; cknow | cquery)
```

其中，**I(Y*; cknow | cquery)** 是给定查询 **cquery** 时，目标响应 **Y*** 与检索所得知识 **cknow** 之间的互信息。

**直观解释**：我们希望检索到最能揭示正确答案应当是什么的信息。这就像一位熟练的图书管理员，不只是找到与你的主题有关的书，而是找到包含你所需确切见解的特定书籍。

### 动态装配优化
```
A*(cinstr, cknow, cmem, cquery) = arg max_A P(Y* | A(...)) × Efficiency(A)
```

满足以下约束：
- `|A(...)| ≤ Lmax`（上下文窗口限制）
- `Quality(cknow) ≥ threshold`（信息质量阈值）
- `Relevance(cknow, cquery) ≥ min_relevance`（相关性阈值）

**直观解释**：装配函数就像一位资深编辑，知道如何将不同信息整合成连贯、有效的简报，在实际限制内尽可能提高获得优质响应的概率。

---

## 架构可视化：上下文工程技术栈

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTEXT ASSEMBLY LAYER                  │
│  ┌─────────────────┬────────────────┬─────────────────────┐ │
│  │   INSTRUCTIONS  │    KNOWLEDGE   │      ORCHESTRATION  │ │
│  │                 │                │                     │ │
│  │  • Task specs   │  • Retrieved   │  • Assembly logic  │ │
│  │  • Constraints  │    documents   │  • Prioritization  │ │
│  │  • Examples     │  • Real-time   │  • Formatting      │ │
│  │  • Format rules │    data        │  • Length mgmt     │ │
│  └─────────────────┴────────────────┴─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ▲
┌─────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE RETRIEVAL LAYER                │
│  ┌─────────────────┬────────────────┬─────────────────────┐ │
│  │   QUERY PROC    │   RETRIEVAL    │    KNOWLEDGE BASES  │ │
│  │                 │                │                     │ │
│  │  • Query anal   │  • Vector      │  • Documents       │ │
│  │  • Intent extr  │    search      │  • Databases       │ │
│  │  • Expansion    │  • Semantic    │  • APIs            │ │
│  │  • Filtering    │    matching    │  • Real-time       │ │
│  └─────────────────┴────────────────┴─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ▲
┌─────────────────────────────────────────────────────────────┐
│                    PROMPT ENGINEERING LAYER                │
│  ┌─────────────────┬────────────────┬─────────────────────┐ │
│  │  BASIC PROMPTS  │   TEMPLATES    │   REASONING CHAINS  │ │
│  │                 │                │                     │ │
│  │  • Direct inst │  • Reusable    │  • Chain-of-thought │ │
│  │  • Few-shot     │    patterns    │  • Tree-of-thought  │ │
│  │  • Zero-shot    │  • Domain      │  • Self-consistency │ │
│  │  • Role-based   │    specific    │  • Reflection       │ │
│  └─────────────────┴────────────────┴─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```
> 图：上下文工程的分层技术栈 —— CONTEXT ASSEMBLY LAYER / KNOWLEDGE RETRIEVAL LAYER / PROMPT ENGINEERING LAYER

**从基础理解**：这个技术栈展示了上下文工程如何从基础提示词逐层发展为复杂的信息编排。每一层都增加了新的能力：
- **底层**：核心提示词工程——如何与 LLM 有效沟通
- **中层**：知识检索——如何找到并访问相关的外部信息
- **顶层**：上下文装配——如何最优地整合所有内容

---

## Software 3.0 范式 1：提示词（策略模板）

上下文工程中的提示词超越了简单指令，成为用于信息收集和推理的策略模板。

### 高级推理模板
```markdown
# Chain-of-Thought Reasoning Framework

## Context Assessment
You are tasked with [specific_task] requiring deep analysis and step-by-step reasoning.
Consider the complexity, available information, and reasoning requirements.

## Information Inventory
**Available Context**: {context_summary}
**Missing Information**: {information_gaps}
**Assumptions Required**: {necessary_assumptions}
**Reasoning Type**: {deductive|inductive|abductive|analogical}

## Structured Reasoning Process

### Step 1: Problem Decomposition
Break down the main question into sub-questions:
1. {subquestion_1}
2. {subquestion_2}  
3. {subquestion_3}

### Step 2: Evidence Analysis
For each sub-question, analyze available evidence:
- **Supporting Evidence**: [list relevant supporting information]
- **Contradicting Evidence**: [list conflicting information]
- **Evidence Quality**: [assess reliability and relevance]
- **Evidence Gaps**: [identify missing crucial information]

### Step 3: Reasoning Chain Construction
Build logical connections between evidence and conclusions:

Premise 1: [statement with evidence]
    ├─ Supporting detail A
    ├─ Supporting detail B
    └─ Confidence level: [high/medium/low]

Premise 2: [statement with evidence] 
    ├─ Supporting detail C
    ├─ Supporting detail D
    └─ Confidence level: [high/medium/low]

Intermediate Conclusion: [logical inference from premises]
    └─ Reasoning: [explain the logical connection]


### Step 4: Alternative Hypothesis Consideration
What other explanations or solutions are possible?
- **Alternative 1**: [different interpretation/approach]
  - Strengths: [what supports this alternative]
  - Weaknesses: [what argues against it]
- **Alternative 2**: [another interpretation/approach]
  - Strengths: [supporting factors]
  - Weaknesses: [limiting factors]

### Step 5: Synthesis and Conclusion
**Primary Conclusion**: [main answer/solution]
**Confidence Level**: [percentage or qualitative assessment]
**Key Reasoning**: [the most critical logical steps that led to this conclusion]
**Limitations**: [what could make this conclusion wrong]
**Next Steps**: [what additional information would strengthen the conclusion]

## Quality Assurance
- [ ] Have I addressed all sub-questions?
- [ ] Are my logical connections explicit and valid?
- [ ] Have I considered major alternative explanations?
- [ ] Is my confidence assessment realistic?
- [ ] Can someone else follow my reasoning chain?
```

**从基础理解**：这个模板将简单的「让我们逐步思考」转化为完整的推理方法。它就像一位逻辑大师引导你的思考过程，确保你考虑各个角度、明确建立联系，并评估自身推理的质量。

### 动态知识集成模板
```xml
<knowledge_integration_template>
  <intent>Systematically integrate external knowledge with user query for optimal response</intent>
  
  <context_analysis>
    <user_query>
      <main_intent>{primary_user_goal}</main_intent>
      <sub_intents>
        <intent priority="high">{critical_sub_goal}</intent>
        <intent priority="medium">{important_sub_goal}</intent>
        <intent priority="low">{optional_sub_goal}</intent>
      </sub_intents>
      <complexity_level>{simple|moderate|complex|expert}</complexity_level>
      <domain_context>{specific_field_or_general}</domain_context>
    </user_query>
    
    <information_needs>
      <critical_info>Information absolutely required for accurate response</critical_info>
      <supporting_info>Information that would improve response quality</supporting_info>
      <contextual_info>Information that provides helpful background</contextual_info>
    </information_needs>
  </context_analysis>
  
  <knowledge_retrieval_strategy>
    <search_approach>
      <primary_search>{most_likely_to_find_critical_info}</primary_search>
      <secondary_search>{backup_approach_for_comprehensive_coverage}</secondary_search>
      <tertiary_search>{specialized_or_edge_case_coverage}</tertiary_search>
    </search_approach>
    
    <quality_filters>
      <relevance_threshold>How closely information must match query intent</relevance_threshold>
      <credibility_threshold>Minimum source reliability standard</credibility_threshold>
      <recency_weight>How much to prioritize recent vs authoritative information</recency_weight>
    </quality_filters>
  </knowledge_retrieval_strategy>
  
  <context_assembly>
    <information_hierarchy>
      <tier_1>Core facts directly answering main question</tier_1>
      <tier_2>Supporting evidence and explanations</tier_2>
      <tier_3>Background context and related information</tier_3>
    </information_hierarchy>
    
    <assembly_constraints>
      <max_context_length>{token_limit_consideration}</max_context_length>
      <cognitive_load_limit>Maximum information complexity for user comprehension</cognitive_load_limit>
      <coherence_requirement>How information should connect logically</coherence_requirement>
    </assembly_constraints>
    
    <assembly_process>
      <step name="prioritize">Rank retrieved information by relevance and importance</step>
      <step name="filter">Remove redundant, outdated, or low-quality information</step>
      <step name="structure">Organize information for logical flow and comprehension</step>
      <step name="integrate">Weave information into coherent narrative addressing user query</step>
      <step name="validate">Ensure assembled context supports accurate, helpful response</step>
    </assembly_process>
  </context_assembly>
  
  <response_optimization>
    <tailoring>
      <user_expertise_level>Adjust technical depth appropriately</user_expertise_level>
      <communication_style>Match user's preferred interaction mode</communication_style>
      <information_density>Balance comprehensiveness with clarity</information_density>
    </tailoring>
    
    <quality_assurance>
      <accuracy_check>Verify information correctness and context alignment</accuracy_check>
      <completeness_check>Ensure all critical user needs are addressed</completeness_check>
      <coherence_check>Confirm logical flow and clear communication</coherence_check>
    </quality_assurance>
  </response_optimization>
</knowledge_integration_template>
```

**从基础理解**：这个 XML 模板将查找和集成外部知识的复杂过程结构化。它就像一套研究方法，确保你不仅找到相关信息，还能针对具体用户和任务，以最有效的方式组织和呈现信息。

---

## Software 3.0 范式 2：编程（检索算法）

编程为智能上下文检索与装配提供计算机制。

### 语义检索引擎

```python
import numpy as np
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod
import sqlite3
import json
from datetime import datetime, timedelta

@dataclass
class RetrievalCandidate:
    """A piece of information that could be relevant to the query"""
    content: str
    source: str
    relevance_score: float
    credibility_score: float
    recency_score: float
    content_type: str  # 'fact', 'procedure', 'example', 'definition'
    metadata: Dict
    
class KnowledgeRetriever(ABC):
    """Abstract base for different knowledge retrieval strategies"""
    
    @abstractmethod
    def retrieve(self, query: str, max_results: int = 10) -> List[RetrievalCandidate]:
        """Retrieve relevant knowledge for the given query"""
        pass
    
    @abstractmethod
    def update_relevance_feedback(self, query: str, candidate: RetrievalCandidate, 
                                 helpful: bool):
        """Learn from user feedback about retrieval quality"""
        pass

class SemanticVectorRetriever(KnowledgeRetriever):
    """Retrieval using semantic similarity via embeddings"""
    
    def __init__(self, embedding_model, vector_database):
        self.embedding_model = embedding_model
        self.vector_db = vector_database
        self.feedback_history = []
        
    def retrieve(self, query: str, max_results: int = 10) -> List[RetrievalCandidate]:
        """Retrieve semantically similar content"""
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode(query)
        
        # Search vector database
        raw_results = self.vector_db.similarity_search(
            query_embedding, 
            top_k=max_results * 2  # Get more candidates for filtering
        )
        
        # Convert to RetrievalCandidates with scoring
        candidates = []
        for result in raw_results:
            candidate = RetrievalCandidate(
                content=result.content,
                source=result.source,
                relevance_score=self._calculate_relevance_score(query, result),
                credibility_score=self._calculate_credibility_score(result),
                recency_score=self._calculate_recency_score(result),
                content_type=self._classify_content_type(result.content),
                metadata=result.metadata
            )
            candidates.append(candidate)
        
        # Apply learning from feedback history
        candidates = self._apply_feedback_learning(query, candidates)
        
        # Rank and filter
        ranked_candidates = self._rank_candidates(candidates)
        
        return ranked_candidates[:max_results]
    
    def _calculate_relevance_score(self, query: str, result) -> float:
        """Calculate how relevant the content is to the query"""
        
        # Base semantic similarity
        base_score = result.similarity_score
        
        # Adjust based on content type match
        content_type_bonus = self._get_content_type_bonus(query, result.content)
        
        # Adjust based on query specificity
        specificity_factor = self._calculate_query_specificity_factor(query, result)
        
        # Combine factors
        relevance_score = base_score * (1 + content_type_bonus) * specificity_factor
        
        return min(1.0, max(0.0, relevance_score))
    
    def _calculate_credibility_score(self, result) -> float:
        """Assess source credibility and information quality"""
        
        # Source authority (academic, government, established organization)
        source_authority = self._get_source_authority_score(result.source)
        
        # Content quality indicators (length, structure, citations)
        content_quality = self._assess_content_quality(result.content)
        
        # Cross-reference validation (how well it aligns with other sources)
        cross_reference_score = self._calculate_cross_reference_score(result)
        
        # Combine factors
        credibility = (source_authority * 0.4 + 
                      content_quality * 0.3 + 
                      cross_reference_score * 0.3)
        
        return credibility
    
    def _calculate_recency_score(self, result) -> float:
        """Score based on information recency (more recent = higher score)"""
        if 'date' not in result.metadata:
            return 0.5  # Neutral score for undated content
            
        content_date = datetime.fromisoformat(result.metadata['date'])
        days_old = (datetime.now() - content_date).days
        
        # Exponential decay: score decreases as content gets older
        # Half-life of 365 days (information relevance decreases by half each year)
        half_life = 365
        recency_score = 0.5 ** (days_old / half_life)
        
        return recency_score
    
    def _classify_content_type(self, content: str) -> str:
        """Classify content as fact, procedure, example, or definition"""
        
        # Simple heuristic classification (in practice, use ML classifier)
        content_lower = content.lower()
        
        if any(phrase in content_lower for phrase in ['step', 'first', 'then', 'finally', 'procedure']):
            return 'procedure'
        elif any(phrase in content_lower for phrase in ['for example', 'such as', 'instance']):
            return 'example'
        elif any(phrase in content_lower for phrase in ['is defined as', 'refers to', 'means']):
            return 'definition'
        else:
            return 'fact'
    
    def _rank_candidates(self, candidates: List[RetrievalCandidate]) -> List[RetrievalCandidate]:
        """Rank candidates using composite scoring"""
        
        for candidate in candidates:
            # Composite score balancing multiple factors
            candidate.composite_score = (
                candidate.relevance_score * 0.5 +      # Relevance is most important
                candidate.credibility_score * 0.3 +    # Credibility is very important  
                candidate.recency_score * 0.2          # Recency matters but less
            )
        
        # Sort by composite score
        ranked = sorted(candidates, key=lambda c: c.composite_score, reverse=True)
        
        return ranked
    
    def update_relevance_feedback(self, query: str, candidate: RetrievalCandidate, 
                                 helpful: bool):
        """Learn from feedback to improve future retrieval"""
        
        feedback_entry = {
            'query': query,
            'candidate_source': candidate.source,
            'candidate_type': candidate.content_type,
            'helpful': helpful,
            'timestamp': datetime.now().isoformat()
        }
        
        self.feedback_history.append(feedback_entry)
        
        # Update retrieval parameters based on feedback patterns
        self._update_retrieval_parameters()
    
    def _apply_feedback_learning(self, query: str, candidates: List[RetrievalCandidate]) -> List[RetrievalCandidate]:
        """Adjust candidate scores based on learned feedback patterns"""
        
        if not self.feedback_history:
            return candidates
        
        # Analyze feedback patterns
        feedback_patterns = self._analyze_feedback_patterns(query)
        
        # Adjust scores based on patterns
        for candidate in candidates:
            adjustment = self._calculate_feedback_adjustment(candidate, feedback_patterns)
            candidate.relevance_score = min(1.0, max(0.0, candidate.relevance_score + adjustment))
        
        return candidates
    
    def _analyze_feedback_patterns(self, query: str) -> Dict:
        """Analyze historical feedback to identify useful patterns"""
        
        patterns = {
            'helpful_sources': [],
            'helpful_content_types': [],
            'unhelpful_sources': [],
            'unhelpful_content_types': []
        }
        
        # Group feedback by helpfulness
        for feedback in self.feedback_history[-100:]:  # Recent feedback
            if self._is_similar_query(query, feedback['query']):
                if feedback['helpful']:
                    patterns['helpful_sources'].append(feedback['candidate_source'])
                    patterns['helpful_content_types'].append(feedback['candidate_type'])
                else:
                    patterns['unhelpful_sources'].append(feedback['candidate_source'])
                    patterns['unhelpful_content_types'].append(feedback['candidate_type'])
        
        return patterns

class HybridKnowledgeRetriever(KnowledgeRetriever):
    """Combines multiple retrieval strategies for comprehensive results"""
    
    def __init__(self, retrievers: List[KnowledgeRetriever], weights: List[float] = None):
        self.retrievers = retrievers
        self.weights = weights or [1.0] * len(retrievers)
        self.performance_history = {i: [] for i in range(len(retrievers))}
        
    def retrieve(self, query: str, max_results: int = 10) -> List[RetrievalCandidate]:
        """Retrieve from multiple sources and intelligently combine results"""
        
        all_candidates = []
        
        # Retrieve from each strategy
        for i, retriever in enumerate(self.retrievers):
            try:
                candidates = retriever.retrieve(query, max_results)
                
                # Weight candidates based on retriever performance
                weight = self.weights[i] * self._get_dynamic_weight(i, query)
                
                for candidate in candidates:
                    candidate.composite_score *= weight
                    candidate.metadata['retriever_id'] = i
                
                all_candidates.extend(candidates)
                
            except Exception as e:
                print(f"Retriever {i} failed: {e}")
                continue
        
        # Remove duplicates and merge similar content
        unique_candidates = self._deduplicate_candidates(all_candidates)
        
        # Rank final candidates
        final_candidates = self._rank_hybrid_candidates(unique_candidates)
        
        return final_candidates[:max_results]
    
    def _get_dynamic_weight(self, retriever_id: int, query: str) -> float:
        """Calculate dynamic weight based on retriever performance for similar queries"""
        
        if not self.performance_history[retriever_id]:
            return 1.0  # Default weight for new retrievers
        
        # Calculate recent performance average
        recent_performance = self.performance_history[retriever_id][-10:]  # Last 10 queries
        avg_performance = sum(recent_performance) / len(recent_performance)
        
        # Dynamic weight based on performance (better performers get higher weight)
        return max(0.1, min(2.0, avg_performance))
    
    def _deduplicate_candidates(self, candidates: List[RetrievalCandidate]) -> List[RetrievalCandidate]:
        """Remove duplicate and very similar candidates"""
        
        unique_candidates = []
        content_hashes = set()
        
        for candidate in sorted(candidates, key=lambda c: c.composite_score, reverse=True):
            # Simple deduplication based on content similarity
            content_hash = hash(candidate.content[:200])  # Hash first 200 chars
            
            if content_hash not in content_hashes:
                content_hashes.add(content_hash)
                unique_candidates.append(candidate)
        
        return unique_candidates
    
    def update_relevance_feedback(self, query: str, candidate: RetrievalCandidate, helpful: bool):
        """Update feedback for the specific retriever that provided this candidate"""
        
        retriever_id = candidate.metadata.get('retriever_id')
        if retriever_id is not None:
            # Update performance history
            performance_score = 1.0 if helpful else 0.0
            self.performance_history[retriever_id].append(performance_score)
            
            # Forward feedback to specific retriever
            self.retrievers[retriever_id].update_relevance_feedback(query, candidate, helpful)

class DynamicContextAssembler:
    """Assembles optimal context from retrieved knowledge and other sources"""
    
    def __init__(self, max_context_length: int = 4000):
        self.max_context_length = max_context_length
        self.assembly_history = []
        
    def assemble_context(self, query: str, retrieved_candidates: List[RetrievalCandidate],
                        instructions: str = "", user_context: str = "",
                        task_type: str = "general") -> str:
        """Dynamically assemble optimal context from available information"""
        
        # Analyze query to understand information needs
        info_needs = self._analyze_information_needs(query, task_type)
        
        # Select optimal subset of candidates
        selected_candidates = self._select_optimal_candidates(
            retrieved_candidates, info_needs, self.max_context_length
        )
        
        # Structure and format context
        assembled_context = self._structure_context(
            instructions, selected_candidates, user_context, query, info_needs
        )
        
        # Validate and optimize final context
        optimized_context = self._optimize_context(assembled_context, query)
        
        return optimized_context
    
    def _analyze_information_needs(self, query: str, task_type: str) -> Dict:
        """Analyze what types of information are needed for this query"""
        
        needs = {
            'definitions': 0.0,
            'facts': 0.0,
            'procedures': 0.0,
            'examples': 0.0,
            'background': 0.0
        }
        
        query_lower = query.lower()
        
        # Heuristic analysis of information needs
        if any(word in query_lower for word in ['what is', 'define', 'meaning', 'definition']):
            needs['definitions'] = 1.0
            needs['examples'] = 0.7
            
        elif any(word in query_lower for word in ['how to', 'steps', 'procedure', 'process']):
            needs['procedures'] = 1.0
            needs['examples'] = 0.8
            
        elif any(word in query_lower for word in ['why', 'explain', 'reason', 'cause']):
            needs['facts'] = 1.0
            needs['background'] = 0.8
            
        elif 'example' in query_lower:
            needs['examples'] = 1.0
            needs['procedures'] = 0.5
            
        else:
            # General query - balanced information needs
            for key in needs:
                needs[key] = 0.6
        
        # Adjust based on task type
        if task_type == "analytical":
            needs['facts'] *= 1.3
            needs['background'] *= 1.2
        elif task_type == "practical":
            needs['procedures'] *= 1.3
            needs['examples'] *= 1.2
        elif task_type == "creative":
            needs['examples'] *= 1.2
            needs['background'] *= 1.1
        
        return needs
    
    def _select_optimal_candidates(self, candidates: List[RetrievalCandidate],
                                  info_needs: Dict, max_length: int) -> List[RetrievalCandidate]:
        """Select optimal subset of candidates based on information needs and length constraints"""
        
        # Score candidates based on information needs alignment
        for candidate in candidates:
            content_type_score = info_needs.get(candidate.content_type, 0.5)
            candidate.need_alignment_score = (
                candidate.composite_score * 0.7 + 
                content_type_score * 0.3
            )
        
        # Use greedy knapsack-style selection
        selected = []
        total_length = 0
        remaining_candidates = sorted(candidates, key=lambda c: c.need_alignment_score, reverse=True)
        
        for candidate in remaining_candidates:
            candidate_length = len(candidate.content)
            
            if total_length + candidate_length <= max_length * 0.8:  # Reserve 20% for formatting
                selected.append(candidate)
                total_length += candidate_length
            elif len(selected) < 2:  # Ensure we have at least 2 candidates
                # Truncate content to fit
                available_space = max_length * 0.8 - total_length
                if available_space > 100:  # Only if we can fit meaningful content
                    truncated_candidate = RetrievalCandidate(
                        content=candidate.content[:int(available_space)],
                        source=candidate.source,
                        relevance_score=candidate.relevance_score,
                        credibility_score=candidate.credibility_score,
                        recency_score=candidate.recency_score,
                        content_type=candidate.content_type,
                        metadata=candidate.metadata
                    )
                    selected.append(truncated_candidate)
                    break
        
        return selected
    
    def _structure_context(self, instructions: str, candidates: List[RetrievalCandidate],
                          user_context: str, query: str, info_needs: Dict) -> str:
        """Structure the context for optimal comprehension and utility"""
        
        context_parts = []
        
        # Add instructions if provided
        if instructions.strip():
            context_parts.append(f"## Instructions\n{instructions}\n")
        
        # Add user context if provided
        if user_context.strip():
            context_parts.append(f"## Context\n{user_context}\n")
        
        # Group candidates by type for better organization
        candidates_by_type = {}
        for candidate in candidates:
            if candidate.content_type not in candidates_by_type:
                candidates_by_type[candidate.content_type] = []
            candidates_by_type[candidate.content_type].append(candidate)
        
        # Add retrieved information in logical order
        type_order = ['definitions', 'facts', 'procedures', 'examples']
        type_labels = {
            'definition': 'Key Definitions',
            'fact': 'Relevant Information', 
            'procedure': 'Procedures and Methods',
            'example': 'Examples and Case Studies'
        }
        
        context_parts.append("## Retrieved Knowledge\n")
        
        for content_type in type_order:
            if content_type in candidates_by_type:
                candidates_of_type = candidates_by_type[content_type]
                section_label = type_labels.get(content_type, content_type.title())
                
                context_parts.append(f"### {section_label}\n")
                
                for i, candidate in enumerate(candidates_of_type, 1):
                    source_note = f" (Source: {candidate.source})" if candidate.source else ""
                    context_parts.append(f"{i}. {candidate.content.strip()}{source_note}\n")
                
                context_parts.append("")  # Add spacing
        
        # Add the user's specific query
        context_parts.append(f"## Current Query\n{query}\n")
        
        return "\n".join(context_parts)
    
    def _optimize_context(self, context: str, query: str) -> str:
        """Final optimization of assembled context"""
        
        # Remove excessive whitespace
        optimized = "\n".join(line.strip() for line in context.split("\n"))
        
        # Remove duplicate information (simple approach)
        lines = optimized.split("\n")
        unique_lines = []
        seen_content = set()
        
        for line in lines:
            if line.strip():
                # Check for substantial duplicates (not just headers)
                line_content = line.lower().strip()
                if len(line_content) > 20:  # Only check substantial lines
                    if line_content not in seen_content:
                        seen_content.add(line_content)
                        unique_lines.append(line)
                else:
                    unique_lines.append(line)
            else:
                unique_lines.append(line)
        
        return "\n".join(unique_lines)

# Example usage demonstrating the complete retrieval and assembly pipeline
class ContextGenerationDemo:
    """Demonstration of complete context generation pipeline"""
    
    def __init__(self):
        # Initialize retrievers (mock implementations for demo)
        self.semantic_retriever = SemanticVectorRetriever(
            embedding_model=MockEmbeddingModel(),
            vector_database=MockVectorDatabase()
        )
        
        self.hybrid_retriever = HybridKnowledgeRetriever([
            self.semantic_retriever,
            # Add other retrievers as needed
        ])
        
        self.context_assembler = DynamicContextAssembler(max_context_length=4000)
    
    def generate_context(self, query: str, instructions: str = "", 
                        user_context: str = "", task_type: str = "general") -> str:
        """Complete context generation pipeline"""
        
        print(f"Generating context for query: '{query}'")
        
        # Step 1: Retrieve relevant knowledge
        print("Step 1: Retrieving knowledge...")
        candidates = self.hybrid_retriever.retrieve(query, max_results=10)
        print(f"Retrieved {len(candidates)} candidates")
        
        # Step 2: Assemble optimal context
        print("Step 2: Assembling context...")
        context = self.context_assembler.assemble_context(
            query, candidates, instructions, user_context, task_type
        )
        
        print(f"Step 3: Generated context ({len(context)} characters)")
        
        return context

# Mock classes for demonstration
class MockEmbeddingModel:
    def encode(self, text: str) -> np.ndarray:
        # Simplified mock embedding
        return np.random.rand(384)

class MockVectorDatabase:
    def __init__(self):
        self.mock_results = [
            MockResult("Machine learning is a subset of artificial intelligence...", "wikipedia.org", 0.85),
            MockResult("To implement a neural network: 1. Define architecture...", "tutorial.com", 0.78),
            MockResult("For example, a simple classification model...", "examples.org", 0.72)
        ]
    
    def similarity_search(self, query_embedding: np.ndarray, top_k: int = 10):
        return self.mock_results[:top_k]

@dataclass 
class MockResult:
    content: str
    source: str
    similarity_score: float
    metadata: Dict = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {"date": "2024-01-01"}
```

**从基础理解**：这个检索系统就像配备了多位各有专长的研究助手，以及一位知道如何将他们的发现整合成理想简报的资深编辑。`HybridKnowledgeRetriever` 从多个来源获取输入，`DynamicContextAssembler` 对所有内容进行最优组织，而系统则通过反馈不断学习，逐步改进。

---

## Software 3.0 范式 3：协议（自适应装配协议壳）

协议提供能够根据实际效能不断演进的自修改上下文生成模式。

### 自适应上下文生成协议

```
/context.generate.adaptive{
    intent="Dynamically generate optimal context by learning from usage patterns and adapting assembly strategies",
    
    input={
        user_query=<immediate_user_request>,
        task_context={
            domain=<subject_area_or_field>,
            complexity_level=<simple|moderate|complex|expert>,
            user_expertise=<novice|intermediate|advanced|expert>,
            time_constraints=<available_processing_time>,
            quality_requirements=<accuracy_completeness_specificity_needs>
        },
        available_sources={
            knowledge_bases=<accessible_information_repositories>,
            real_time_data=<current_information_streams>,
            user_history=<relevant_past_interactions>,
            domain_expertise=<specialized_knowledge_sources>
        }
    },
    
    process=[
        /analyze.information_needs{
            action="Deep analysis of what information is required for optimal response",
            method="Multi-dimensional need assessment with learning integration",
            analysis_dimensions=[
                {factual_requirements="What facts, data, or evidence are needed?"},
                {conceptual_requirements="What concepts, definitions, or frameworks are needed?"},
                {procedural_requirements="What processes, methods, or steps are needed?"},
                {contextual_requirements="What background or situational information is needed?"},
                {example_requirements="What illustrations, cases, or demonstrations are needed?"}
            ],
            learning_integration="Apply patterns learned from similar successful query contexts",
            output="Comprehensive information need specification with priority weighting"
        },
        
        /orchestrate.multi_source_retrieval{
            action="Intelligently coordinate retrieval from multiple information sources",
            method="Parallel retrieval with strategic source selection and result fusion",
            retrieval_strategies=[
                {semantic_search="Vector similarity matching against knowledge embeddings"},
                {keyword_expansion="Query expansion with domain-specific terminology"},
                {contextual_filtering="Filter by relevance to user context and expertise level"},
                {temporal_prioritization="Weight recent vs authoritative information appropriately"},
                {cross_reference_validation="Verify consistency across multiple sources"}
            ],
            fusion_algorithm="Intelligent combination of results with deduplication and relevance ranking",
            output="Ranked collection of high-quality information candidates"
        },
        
        /optimize.context_assembly{
            action="Assemble retrieved information into optimal context structure",
            method="Dynamic assembly optimization with cognitive load management",
            assembly_strategies=[
                {information_hierarchy="Structure information from most to least critical"},
                {cognitive_chunking="Group related information to reduce cognitive load"},
                {logical_flow="Organize information in natural reasoning progression"},
                {length_optimization="Maximize information value within context window constraints"},
                {user_customization="Adapt presentation style to user expertise and preferences"}
            ],
            optimization_criteria=[
                {relevance_maximization="Ensure every piece of information serves the user's goal"},
                {coherence_enhancement="Create logical connections between information pieces"},
                {clarity_optimization="Present information at appropriate complexity level"},
                {actionability_focus="Emphasize information that enables user action"}
            ],
            output="Optimally structured context ready for model consumption"
        },
        
        /monitor.effectiveness{
            action="Track context generation effectiveness and identify improvement opportunities",
            method="Multi-metric effectiveness assessment with learning integration",
            effectiveness_metrics=[
                {response_quality="How well does the generated context enable high-quality responses?"},
                {user_satisfaction="How satisfied are users with responses generated from this context?"},
                {task_completion="How effectively does the context enable task completion?"},
                {efficiency_measures="Context generation speed and resource utilization"},
                {learning_indicators="Evidence of improved performance over time"}
            ],
            feedback_integration=[
                {explicit_feedback="Direct user ratings and comments on response quality"},
                {implicit_feedback="User behavior patterns indicating satisfaction/dissatisfaction"},
                {outcome_tracking="Long-term success metrics for tasks involving generated contexts"},
                {comparative_analysis="Performance comparison with alternative context generation approaches"}
            ],
            output="Comprehensive effectiveness assessment with specific improvement recommendations"
        }
    ],
    
    output={
        generated_context={
            assembled_information=<optimally_structured_context_ready_for_model>,
            information_sources=<attribution_and_credibility_information>,
            assembly_rationale=<explanation_of_context_construction_decisions>,
            quality_indicators=<confidence_scores_and_completeness_measures>
        },
        
        optimization_metadata={
            retrieval_performance=<metrics_on_information_gathering_effectiveness>,
            assembly_efficiency=<metrics_on_context_construction_performance>,
            predicted_effectiveness=<estimated_quality_of_generated_context>,
            alternative_approaches=<other_context_generation_strategies_considered>
        },
        
        learning_updates={
            pattern_discoveries=<new_effective_patterns_identified>,
            strategy_refinements=<improvements_to_existing_approaches>,
            feedback_integration=<how_user_feedback_influenced_context_generation>,
            knowledge_base_updates=<improvements_to_underlying_information_sources>
        }
    },
    
    // Self-improvement mechanisms
    adaptation_triggers=[
        {condition="user_satisfaction < 0.7", action="analyze_context_assembly_weaknesses"},
        {condition="response_quality_decline_detected", action="audit_information_source_quality"},
        {condition="new_domain_patterns_identified", action="integrate_domain_specific_optimizations"},
        {condition="efficiency_below_threshold", action="optimize_retrieval_and_assembly_performance"}
    ],
    
    meta={
        context_generation_version="adaptive_v2.1",
        learning_integration_level="advanced",
        adaptation_frequency="continuous_with_batch_updates",
        quality_assurance="multi_dimensional_effectiveness_monitoring"
    }
}
```

**从基础理解**：这个协议构建了一个自我改进的上下文生成系统。它就像一个研究团队，每次开展项目时都会更善于查找和组织信息，并学会哪些信息对于不同类型的问题和用户最有价值。

---

## 集成与实际应用

### 案例研究：医疗诊断支持的上下文生成

```python
def medical_diagnosis_context_example():
    """Demonstrate context generation for medical diagnosis support"""
    
    # Simulated medical query
    query = "Patient presents with chest pain, shortness of breath, and elevated troponin levels. What are the differential diagnoses and recommended diagnostic workup?"
    
    # Medical-specific context generation
    medical_context_generator = ContextGenerationDemo()
    
    # Generate specialized medical context
    context = medical_context_generator.generate_context(
        query=query,
        instructions="""
        You are providing medical decision support. Focus on:
        1. Evidence-based differential diagnoses
        2. Appropriate diagnostic workup recommendations  
        3. Risk stratification considerations
        4. Latest clinical guidelines and protocols
        
        Always emphasize the need for clinical judgment and direct patient evaluation.
        """,
        user_context="Emergency department setting, adult patient, no known allergies",
        task_type="analytical"
    )
    
    print("Medical Diagnosis Support Context:")
    print("=" * 50)
    print(context)
    
    return context
```

### 性能评估框架

```python
class ContextGenerationEvaluator:
    """Comprehensive evaluation of context generation effectiveness"""
    
    def __init__(self):
        self.evaluation_metrics = {
            'relevance': self._evaluate_relevance,
            'completeness': self._evaluate_completeness,
            'clarity': self._evaluate_clarity,
            'efficiency': self._evaluate_efficiency,
            'adaptability': self._evaluate_adaptability
        }
    
    def evaluate_context_generation(self, query: str, generated_context: str, 
                                   response_quality: float, user_feedback: Dict) -> Dict:
        """Comprehensive evaluation of context generation performance"""
        
        results = {}
        for metric_name, metric_function in self.evaluation_metrics.items():
            score = metric_function(query, generated_context, response_quality, user_feedback)
            results[metric_name] = score
        
        # Calculate overall effectiveness
        results['overall_effectiveness'] = self._calculate_overall_effectiveness(results)
        
        # Generate improvement recommendations
        results['improvement_recommendations'] = self._generate_improvement_recommendations(results)
        
        return results
    
    def _evaluate_relevance(self, query: str, context: str, response_quality: float, feedback: Dict) -> float:
        """Evaluate how relevant the generated context is to the query"""
        
        # Analyze semantic alignment between query and context
        query_terms = set(query.lower().split())
        context_terms = set(context.lower().split())
        
        term_overlap = len(query_terms.intersection(context_terms)) / len(query_terms.union(context_terms))
        
        # Factor in response quality as indicator of context relevance
        relevance_score = (term_overlap * 0.3 + response_quality * 0.7)
        
        return min(1.0, max(0.0, relevance_score))
    
    def _evaluate_completeness(self, query: str, context: str, response_quality: float, feedback: Dict) -> float:
        """Evaluate whether context contains all necessary information"""
        
        # Simple heuristic: longer contexts are generally more complete
        # But also consider user feedback about missing information
        
        context_length_score = min(1.0, len(context) / 2000)  # Normalize to reasonable length
        
        # Check feedback for missing information indicators
        missing_info_penalty = 0.0
        if feedback.get('missing_information', False):
            missing_info_penalty = 0.3
        
        completeness_score = max(0.0, context_length_score - missing_info_penalty)
        
        return completeness_score
    
    def _calculate_overall_effectiveness(self, metric_scores: Dict) -> float:
        """Calculate weighted overall effectiveness score"""
        
        weights = {
            'relevance': 0.30,
            'completeness': 0.25,
            'clarity': 0.20,
            'efficiency': 0.15,
            'adaptability': 0.10
        }
        
        overall = sum(metric_scores[metric] * weight 
                     for metric, weight in weights.items() 
                     if metric in metric_scores)
        
        return overall
```

**从基础理解**：这个评估框架就像一个全面的质量控制系统，从多个角度审视上下文生成：不仅检查是否奏效，还检查效果如何，以及可以怎样改进。

---

## 实践练习与后续步骤

### 练习 1：构建自己的检索系统
**目标**：实现一个基础语义检索系统

```python
# Your implementation template
class BasicRetriever:
    def __init__(self):
        # TODO: Initialize your retrieval system
        self.knowledge_base = {}
        self.embedding_cache = {}
    
    def add_document(self, doc_id: str, content: str):
        # TODO: Add document to knowledge base
        pass
    
    def retrieve(self, query: str, max_results: int = 5) -> List[str]:
        # TODO: Implement retrieval logic
        pass

# Test your retriever
retriever = BasicRetriever()
# Add some test documents
# Test retrieval with different queries
```

### 练习 2：上下文装配优化
**目标**：创建一个能够优化信息组织方式的上下文装配器

```python
class ContextOptimizer:
    def __init__(self, max_length: int = 2000):
        # TODO: Initialize context optimizer
        self.max_length = max_length
    
    def optimize_context(self, information_pieces: List[str], query: str) -> str:
        # TODO: Implement optimal context assembly
        pass
```

---

## 总结与后续步骤

**已掌握的核心概念**：
- 从静态提示词到动态上下文编排的演进
- 知识检索的信息论优化
- 多来源检索策略与结果融合
- 融入学习机制的自适应上下文装配
- 对上下文生成效能的全面评估

**Software 3.0 集成**：
- **提示词**：用于推理和知识集成的策略模板
- **编程**：复杂的检索与装配算法
- **协议**：自我改进的上下文生成系统

**实现技能**：
- 使用嵌入和向量数据库进行语义检索
- 通过认知负荷优化实现动态上下文装配
- 多来源信息融合与去重
- 效能评估与持续改进系统

**研究依据**：直接实现上下文生成研究（§4.1），并创新性地扩展到自适应装配、多来源融合和自我改进的上下文编排。

**下一模块**：[01_prompt_engineering.md](01_prompt_engineering.md)——深入学习高级提示技术，在上下文生成基础上掌握与 LLM 沟通的艺术与科学。

---

*本模块为智能上下文工程奠定基础，将「提示词」这一简单概念转化为复杂的动态知识编排与最优信息装配系统。*
