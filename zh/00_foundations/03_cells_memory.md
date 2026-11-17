---
title: 细胞：增加记忆与状态
source: 00_foundations/03_cells_memory.md
module: M2
task: M2-02
chunks: 1
chunks_done:
  - 1
status: published
source_sha256: dabf0a515282bd84d6889aa180c121c2860b32cf8794a0fde49e12ba34acd039
---

> 原文：[00_foundations/03_cells_memory.md](../../00_foundations/03_cells_memory.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# 细胞：增加记忆与状态

> 「我们即我们的记忆，我们是那座变幻形状的奇幻博物馆，那堆破碎的镜子。」—— 豪尔赫·路易斯·博尔赫斯

## 从分子到细胞

我们已经探讨了**原子（atom）**（单一指令）与**分子（molecule）**（带示例的指令）。现在，我们上升到**细胞（cell）**——带有**记忆（memory）**、能在多次交互中持续存在的上下文（context）结构。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  CELL = [INSTRUCTIONS] + [EXAMPLES] + [MEMORY/STATE] + [CURRENT INPUT]      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
> 图：细胞的组成 —— CELL = [INSTRUCTIONS] + [EXAMPLES] + [MEMORY/STATE] + [CURRENT INPUT]

正如生物细胞在与环境交互时维持内部状态一样，我们的上下文「细胞」在与 LLM 的多次交互中保留信息。

## 记忆问题

默认情况下，LLM 没有记忆。每个请求都被独立处理：

```
┌───────────────────────┐      ┌───────────────────────┐
│ Request 1             │      │ Request 2             │
├───────────────────────┤      ├───────────────────────┤
│ "My name is Alex."    │      │ "What's my name?"     │
│                       │      │                       │
│                       │      │                       │
└───────────────────────┘      └───────────────────────┘
          │                              │
          ▼                              ▼
┌───────────────────────┐      ┌───────────────────────┐
│ Response 1            │      │ Response 2            │
├───────────────────────┤      ├───────────────────────┤
│ "Hello Alex, nice     │      │ "I don't have access  │
│  to meet you."        │      │  to previous          │
│                       │      │  conversations..."    │
└───────────────────────┘      └───────────────────────┘
```
> 图：无记忆时请求相互独立 —— Request 1 / Request 2 / Response 1 / Response 2

没有记忆，LLM 会遗忘先前交互中的信息，造成支离破碎、令人沮丧的用户体验。

## 细胞方案：对话记忆

最简单的细胞结构是在上下文中加入对话历史：

```
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  SYSTEM PROMPT: "You are a helpful assistant..."                      │
│                                                                       │
│  CONVERSATION HISTORY:                                                │
│  User: "My name is Alex."                                             │
│  Assistant: "Hello Alex, nice to meet you."                           │
│                                                                       │
│  CURRENT INPUT: "What's my name?"                                     │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```
> 图：对话记忆细胞的结构 —— SYSTEM PROMPT + CONVERSATION HISTORY + CURRENT INPUT

现在 LLM 可以访问先前的交互并保持连贯性。

## 记忆的词元预算问题

随着对话增长，上下文窗口会被填满。我们需要记忆管理策略：

```
          [Context Window Tokens]
          ┌─────────────────────────────────────────────┐
          │                                             │
Turn 1    │ System Instructions       User Input 1      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 2    │ System    History 1       User Input 2      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 3    │ Sys  History 1  History 2  User Input 3     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 4    │ S  History 1-3             User Input 4     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 5    │ History 2-4                User Input 5     │
          │                                             │
          └─────────────────────────────────────────────┘
                                       ▲
                                       │
                        Eventually, something has to go
```
> 图：上下文窗口随轮次被填满 —— [Context Window Tokens] / Turn 1-5

## 记忆管理策略

有若干策略有助于优化有限上下文窗口的使用：

```
┌───────────────────────────────────────────────────────────────────┐
│ MEMORY MANAGEMENT STRATEGIES                                      │
├────────────────────┬──────────────────────────────────────────────┤
│ Windowing          │ Keep only the most recent N turns            │
├────────────────────┼──────────────────────────────────────────────┤
│ Summarization      │ Compress older turns into summaries          │
├────────────────────┼──────────────────────────────────────────────┤
│ Key-Value Storage  │ Extract and store important facts separately │
├────────────────────┼──────────────────────────────────────────────┤
│ Priority Pruning   │ Remove less important turns first            │
├────────────────────┼──────────────────────────────────────────────┤
│ Semantic Chunking  │ Group related exchanges together             │
└────────────────────┴──────────────────────────────────────────────┘
```
> 图：记忆管理策略 —— Windowing / Summarization / Key-Value Storage / Priority Pruning / Semantic Chunking

## 窗口化：滑动上下文

最简单的记忆管理方法是只保留最近的对话轮次：

```
                    ┌───────────────────────────┐
Turn 1              │ System + Turn 1           │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 2              │ System + Turn 1-2         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 3              │ System + Turn 1-3         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 4              │ System + Turn 2-4         │ ← Turn 1 dropped
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 5              │ System + Turn 3-5         │ ← Turn 2 dropped
                    └───────────────────────────┘
```
> 图：滑动窗口的轮次演进 —— System + Turn 1 / System + Turn 2-4 / System + Turn 3-5

这种方法简单，但会遗忘较早轮次的信息。

## 摘要：压缩记忆

更复杂的方法是把较早的轮次压缩成摘要：

```
                    ┌────────────────────────────────────────────┐
Turn 1-3            │ System + Turn 1-3                          │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 4              │ System + Summary(Turn 1-2) + Turn 3-4      │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 5              │ System + Summary(Turn 1-3) + Turn 4-5      │
                    └────────────────────────────────────────────┘
```
> 图：将较早轮次压缩为摘要 —— Summary(Turn 1-2) / Summary(Turn 1-3)

摘要在降低词元（token）数量的同时保留关键信息。

## 键值记忆：结构化状态

为了获得更强的控制力，我们可以以结构化格式提取并存储重要事实：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT WINDOW                                                      │
│                                                                     │
│  SYSTEM PROMPT: "You are a helpful assistant..."                    │
│                                                                     │
│  MEMORY:                                                            │
│  {                                                                  │
│    "user_name": "Alex",                                             │
│    "favorite_color": "blue",                                        │
│    "location": "Toronto",                                           │
│    "last_topic": "vacation plans"                                   │
│  }                                                                  │
│                                                                     │
│  RECENT CONVERSATION:                                               │
│  User: "What activities would you recommend?"                       │
│  Assistant: "Given your location in Toronto and interest in..."     │
│                                                                     │
│  CURRENT INPUT: "How about something indoors? It's cold."           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
> 图：以键值格式结构化存储记忆 —— MEMORY / RECENT CONVERSATION / CURRENT INPUT

这种结构化方法能够精确控制保留哪些信息。

## 超越对话：有状态应用

细胞能做的远不止维持连贯的对话。它们支持有状态应用，其中 LLM 可以：

1. 记住先前的交互
2. 更新并维护变量
3. 跟踪多步流程的进度
4. 在先前输出的基础上继续构建

让我们看一个简单的计算器示例：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STATEFUL CALCULATOR                                                 │
│                                                                     │
│ SYSTEM: "You are a calculator assistant that maintains a running    │
│          total. Follow the user's math operations step by step."    │
│                                                                     │
│ STATE: { "current_value": 0 }                                       │
│                                                                     │
│ User: "Start with 5"                                                │
│ Assistant: "Starting with 5. Current value is 5."                   │
│ STATE: { "current_value": 5 }                                       │
│                                                                     │
│ User: "Multiply by 3"                                               │
│ Assistant: "5 × 3 = 15. Current value is 15."                       │
│ STATE: { "current_value": 15 }                                      │
│                                                                     │
│ User: "Add 7"                                                       │
│ Assistant: "15 + 7 = 22. Current value is 22."                      │
│ STATE: { "current_value": 22 }                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
> 图：有状态计算器示例 —— STATEFUL CALCULATOR / current_value

状态变量跨轮次持续存在，从而实现连续计算。

## 长期记忆：超越上下文窗口

要实现真正持久的记忆，我们需要外部存储：

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   User Input                                                             │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐                                                         │
│  │ Extract     │                                                         │
│  │ Key Info    │                                                         │
│  └─────────────┘                                                         │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐      ┌────────────────────┐                             │
│  │ Update      │◄─────┤ External Memory    │                             │
│  │ Memory      │      │ (Vector DB,        │                             │
│  │             │─────►│  Document DB, etc) │                             │
│  └─────────────┘      └────────────────────┘                             │
│       │                        ▲                                         │
│       │                        │                                         │
│       ▼                        │                                         │
│  ┌─────────────┐      ┌────────────────────┐                             │
│  │ Construct   │      │ Retrieve Relevant  │                             │
│  │ Context     │◄─────┤ Memory             │                             │
│  │             │      │                    │                             │
│  └─────────────┘      └────────────────────┘                             │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐                                                         │
│  │             │                                                         │
│  │ LLM         │                                                         │
│  │             │                                                         │
│  └─────────────┘                                                         │
│       │                                                                  │
│       ▼                                                                  │
│   Response                                                               │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```
> 图：长期记忆与外部存储架构 —— Extract Key Info / External Memory / Retrieve Relevant Memory / LLM

该架构通过以下方式实现近乎无限的记忆：
1. 从对话中提取关键信息
2. 将其存入外部数据库
3. 在需要时检索相关上下文
4. 将该上下文纳入提示词

## 细胞实现：记忆管理器

以下是一个实现基础记忆管理的 Python 类：

```python
class ContextCell:
    """A context cell that maintains memory across interactions."""
    
    def __init__(self, system_prompt, max_turns=10, memory_strategy="window"):
        """
        Initialize the context cell.
        
        Args:
            system_prompt (str): The system instructions
            max_turns (int): Maximum conversation turns to keep
            memory_strategy (str): 'window', 'summarize', or 'key_value'
        """
        self.system_prompt = system_prompt
        self.max_turns = max_turns
        self.memory_strategy = memory_strategy
        self.conversation_history = []
        self.key_value_store = {}
        
    def add_exchange(self, user_input, assistant_response):
        """Add a conversation exchange to history."""
        self.conversation_history.append({
            "user": user_input,
            "assistant": assistant_response
        })
        
        # Apply memory management if needed
        if len(self.conversation_history) > self.max_turns:
            self._manage_memory()
    
    def extract_info(self, key, value):
        """Store important information in key-value store."""
        self.key_value_store[key] = value
    
    def _manage_memory(self):
        """Apply the selected memory management strategy."""
        if self.memory_strategy == "window":
            # Keep only the most recent turns
            self.conversation_history = self.conversation_history[-self.max_turns:]
        
        elif self.memory_strategy == "summarize":
            # Summarize older turns (would use an LLM in practice)
            to_summarize = self.conversation_history[:-self.max_turns + 1]
            summary = self._create_summary(to_summarize)
            
            # Replace old turns with summary
            self.conversation_history = [{"summary": summary}] + \
                                       self.conversation_history[-(self.max_turns-1):]
    
    def _create_summary(self, exchanges):
        """Create a summary of conversation exchanges."""
        # In practice, this would call an LLM to create the summary
        # For this example, we'll use a placeholder
        return f"Summary of {len(exchanges)} previous exchanges"
    
    def build_context(self, current_input):
        """Build the full context for the next LLM call."""
        context = f"{self.system_prompt}\n\n"
        
        # Add key-value memory if we have any
        if self.key_value_store:
            context += "MEMORY:\n"
            for key, value in self.key_value_store.items():
                context += f"{key}: {value}\n"
            context += "\n"
        
        # Add conversation history
        if self.conversation_history:
            context += "CONVERSATION HISTORY:\n"
            for exchange in self.conversation_history:
                if "summary" in exchange:
                    context += f"[Previous exchanges: {exchange['summary']}]\n\n"
                else:
                    context += f"User: {exchange['user']}\n"
                    context += f"Assistant: {exchange['assistant']}\n\n"
        
        # Add current input
        context += f"User: {current_input}\nAssistant:"
        
        return context
```

## 衡量细胞效率

与分子一样，衡量效率对细胞同样至关重要：

```
┌─────────────────────────────────────────────────────────────────┐
│ MEMORY STRATEGY COMPARISON                                      │
├──────────────────┬──────────────┬─────────────┬─────────────────┤
│ Strategy         │ Token Usage  │ Information │ Implementation  │
│                  │              │ Retention   │ Complexity      │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ No Memory        │ Lowest       │ None        │ Trivial         │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Full History     │ Highest      │ Complete    │ Trivial         │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Windowing        │ Controlled   │ Recent Only │ Easy            │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Summarization    │ Moderate     │ Good        │ Moderate        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Key-Value Store  │ Low          │ Selective   │ Moderate        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ External Store   │ Very Low     │ Extensive   │ Complex         │
└──────────────────┴──────────────┴─────────────┴─────────────────┘
```
> 图：记忆策略对比 —— MEMORY STRATEGY COMPARISON

不同策略针对不同优先级进行优化。选择合适的方法取决于你的具体应用需求。

## 高级技巧：记忆编排

对于复杂应用，多个记忆系统可以协同工作：

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MEMORY ORCHESTRATION                           │
│                                                                     │
│  ┌─────────────────┐    ┌─────────────────┐   ┌─────────────────┐   │
│  │                 │    │                 │   │                 │   │
│  │ Short-term      │    │ Working         │   │ Long-term       │   │
│  │ Memory          │    │ Memory          │   │ Memory          │   │
│  │                 │    │                 │   │                 │   │
│  │ • Recent turns  │    │ • Current task  │   │ • User profile  │   │
│  │ • Immediate     │    │ • Active        │   │ • Historical    │   │
│  │   context       │    │   variables     │   │   facts         │   │
│  │ • Last few      │    │ • Task progress │   │ • Learned       │   │
│  │   exchanges     │    │ • Mid-task      │   │   preferences   │   │
│  │                 │    │   state         │   │                 │   │
│  └─────────────────┘    └─────────────────┘   └─────────────────┘   │
│         ▲ ▼                   ▲ ▼                   ▲ ▼             │
│         │ │                   │ │                   │ │             │
│  ┌──────┘ └───────────────────┘ └───────────────────┘ └──────┐      │
│  │                                                           │      │
│  │                    Memory Manager                         │      │
│  │                                                           │      │
│  └───────────────────────────────┬───────────────────────────┘      │
│                                  │                                  │
│                                  ▼                                  │
│                        ┌─────────────────┐                          │
│                        │                 │                          │
│                        │   Context       │                          │
│                        │   Builder       │                          │
│                        │                 │                          │
│                        └─────────────────┘                          │
│                                  │                                  │
│                                  ▼                                  │
│                        ┌─────────────────┐                          │
│                        │                 │                          │
│                        │      LLM        │                          │
│                        │                 │                          │
│                        └─────────────────┘                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
> 图：记忆编排架构 —— Short-term / Working / Long-term Memory → Memory Manager → Context Builder → LLM

该架构映照了人类的记忆系统，包括：
- **短期记忆**：最近的对话轮次
- **工作记忆**：当前的任务状态与变量
- **长期记忆**：持久的用户信息与偏好

记忆管理器编排这些系统，决定在每个上下文中纳入哪些信息。

## 记忆与减少幻觉

记忆细胞最有价值的好处之一是减少幻觉：

```
┌─────────────────────────────────────────────────────────────────────┐
│ HALLUCINATION REDUCTION STRATEGIES                                  │
├─────────────────────────────────────────────────────────────────────┤
│ 1. Explicitly store facts extracted from previous exchanges         │
│ 2. Tag information with source/certainty levels                     │
│ 3. Include relevant facts in context when similar topics arise      │
│ 4. Detect and correct contradictions between memory and responses   │
│ 5. Periodically verify important facts through user confirmation    │
└─────────────────────────────────────────────────────────────────────┘
```
> 图：减少幻觉的策略 —— HALLUCINATION REDUCTION STRATEGIES

通过以记忆中一致的事实为依据，我们大幅提升了可靠性。

## 超越文本：结构化状态

高级细胞维护的不只是文本历史，还有结构化状态：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STRUCTURED STATE EXAMPLES                                           │
├─────────────────────────┬───────────────────────────────────────────┤
│ Progression State       │ {"step": 3, "completed_steps": [1, 2],    │
│                         │  "next_action": "validate_input"}         │
├─────────────────────────┼───────────────────────────────────────────┤
│ User Profile            │ {"name": "Alex", "preferences": {         │
│                         │  "communication_style": "concise",        │
│                         │  "expertise_level": "beginner"}}          │
├─────────────────────────┼───────────────────────────────────────────┤
│ Application State       │ {"current_view": "dashboard",             │
│                         │  "filters": ["active", "high_priority"],  │
│                         │  "sort_by": "deadline"}                   │
├─────────────────────────┼───────────────────────────────────────────┤
│ Environmental Context   │ {"location": "Toronto",                   │
│                         │  "weather": "snowing",                    │
│                         │  "time": "evening"}                       │
└─────────────────────────┴───────────────────────────────────────────┘
```
> 图：结构化状态示例 —— Progression / User Profile / Application / Environmental Context

这种结构化方法能够精确控制上下文，并支持更复杂的应用。

## 记忆反馈回路

复杂的细胞会创建反馈回路，让 LLM 帮助管理自己的记忆：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  User: "I'm planning a trip to Japan next month."                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY EXTRACTION]                                    ││
│  │ Important facts to remember:                                    ││
│  │ - User is planning a trip to Japan                              ││
│  │ - Trip is scheduled for next month                              ││
│  │ Confidence: High                                                ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  Assistant: "That's exciting! Japan is beautiful. Are you           │
│  interested in cities like Tokyo and Kyoto, or more rural areas?"   │
│                                                                     │
│  User: "Definitely Tokyo, and maybe Osaka too."                     │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY UPDATE]                                        ││
│  │ Updated facts:                                                  ││
│  │ - User is planning a trip to Japan next month                   ││
│  │ - User is interested in Tokyo and Osaka                         ││
│  │ - User may not be interested in rural areas (confidence: medium)││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
> 图：记忆反馈回路 —— INTERNAL MEMORY EXTRACTION / INTERNAL MEMORY UPDATE

LLM 自身提取并更新需要记住的重要信息，形成一个自我改进的记忆系统。

## 关键要点

1. **记忆细胞**在多次交互中增加状态持久性
2. **词元预算管理**在对话增长时至关重要
3. **记忆策略**包括窗口化、摘要与键值存储
4. **外部记忆**在上下文窗口之外实现无限且持久的存储
5. **结构化状态**支持超越简单对话的复杂应用
6. **记忆编排**组合多个记忆系统以获得最佳性能
7. **自我改进的记忆**利用 LLM 帮助管理其自身记忆

## 实践练习

1. 实现一个带窗口化的简单对话记忆系统
2. 在同一段长对话上比较不同的记忆策略
3. 构建一个从对话中提取重要事实的键值存储
4. 试验使用 LLM 对较早的对话轮次生成摘要
5. 为特定应用领域创建结构化状态管理器

## 下一步

下一节我们将探讨**器官（organ）**——由多个上下文细胞协同解决复杂问题的多智能体（multi-agent）系统。

[继续阅读 04_organs_applications.md →](04_organs_applications.md)

---

## 深入探究：记忆抽象

记忆可以按多个抽象层次组织：

```
┌────────────────────────────────────────────────────────────────────┐
│ MEMORY ABSTRACTION LAYERS                                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│   ┌─────────────────┐                                              │
│   │ Episodic Memory │  Specific conversation exchanges and events  │
│   └─────────────────┘                                              │
│           ▲                                                        │
│           │                                                        │
│   ┌─────────────────┐                                              │
│   │ Semantic Memory │  Facts, concepts, and structured knowledge   │
│   └─────────────────┘                                              │
│           ▲                                                        │
│           │                                                        │
│   ┌─────────────────┐                                              │
│   │ Conceptual      │  High-level patterns, preferences, goals     │
│   │ Memory          │                                              │
│   └─────────────────┘                                              │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```
> 图：记忆抽象层 —— Episodic / Semantic / Conceptual Memory

这种分层方法使系统能够在具体细节与对交互上下文的高层理解之间取得平衡。

