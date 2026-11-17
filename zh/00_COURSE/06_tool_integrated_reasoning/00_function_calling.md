---
title: 函数调用基础——工具集成推理
source: 00_COURSE/06_tool_integrated_reasoning/00_function_calling.md
module: M4
task: M4-03
chunks: 2
chunks_done: [1, 2]
status: published
source_sha256: 22c16bd9aadb523b7113d027bb8e59d0b5c1d98a091c2d8ca22076be305c877f
---

> 原文：[00_COURSE/06_tool_integrated_reasoning/00_function_calling.md](../../../00_COURSE/06_tool_integrated_reasoning/00_function_calling.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 函数调用基础——工具集成推理

## 引言：使用工具为 LLM 编程

> **Software 3.0 范式**：「LLM 是一种新型计算机，你用*英语*为它们编程。」—— Andrej Karpathy

函数调用（function calling）标志着智能系统架构方式的根本转变。我们不再期望 LLM 仅凭推理解决所有问题，而是通过提供对外部工具、函数和系统的结构化访问来扩展其能力。由此形成一种新范式：LLM 成为负责编排（orchestration）的智能核心，能够动态选择、组合并执行专用工具，以解决复杂问题。

## 函数调用的数学基础

### 面向工具集成的上下文工程（Context Engineering）

在基础框架 C = A(c₁, c₂, ..., cₙ) 之上，函数调用引入了专门的上下文组件：

```
C_tools = A(c_instr, c_tools, c_state, c_query, c_results)
```

其中：
- **c_tools**: 可用的函数定义与签名
- **c_state**: 当前执行状态与上下文（context）
- **c_results**: 此前函数调用的结果
- **c_instr**: 工具使用的系统指令
- **c_query**: 用户当前的请求

### 函数调用优化

优化问题变为寻找最优函数调用序列 F*，使任务完成程度最大化，同时使资源使用最小化：

```
F* = arg max_{F} Σ(Reward(f_i) × Efficiency(f_i)) - Cost(f_i)
```

约束条件如下：
- 资源限制： Σ Cost(f_i) ≤ Budget
- 安全约束： Safe(f_i) = True ∀ f_i
- 依赖解析： Dependencies(f_i) ⊆ Completed_functions

## 核心概念

### 1. 函数签名与模式（schema）

函数调用需要精确的接口定义，使 LLM 能够理解并可靠地使用这些接口：

```python
# Example: Mathematical calculation function
{
    "name": "calculate",
    "description": "Perform mathematical calculations with step-by-step reasoning",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate"
            },
            "show_steps": {
                "type": "boolean",
                "description": "Whether to show intermediate calculation steps",
                "default": True
            }
        },
        "required": ["expression"]
    }
}
```

### 2. 函数调用流程

```ascii
┌─────────────────┐
│   User Query    │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐     ┌──────────────────┐
│ Intent Analysis │────▶│ Function Selection│
└─────────────────┘     └─────────┬────────┘
                                  │
                                  ▼
┌─────────────────┐     ┌──────────────────┐
│Parameter Extract│◀────│ Parameter Mapping│
└─────────┬───────┘     └──────────────────┘
          │
          ▼
┌─────────────────┐     ┌──────────────────┐
│Function Execute │────▶│  Result Process  │
└─────────────────┘     └─────────┬────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │ Response Generate│
                        └──────────────────┘
```
> 图：从用户查询到函数执行与响应生成的流程 —— Function Call Flow

### 3. 函数调用类型

#### **同步调用**
- 直接执行函数并立即获得结果
- 适用于：计算、数据转换、简单查询

#### **异步调用**
- 针对耗时操作的非阻塞执行
- 适用于：网络请求、文件处理、复杂计算

#### **并行调用**
- 同时执行多个函数
- 适用于：独立操作、从多个来源收集数据

#### **顺序调用**
- 以输出作为后续输入的链式函数执行
- 适用于：多步工作流、复杂推理链

## 函数定义模式

### 基本函数模式

```json
{
    "name": "function_name",
    "description": "Clear, specific description of what the function does",
    "parameters": {
        "type": "object",
        "properties": {
            "param1": {
                "type": "string|number|boolean|array|object",
                "description": "Parameter description",
                "enum": ["optional", "allowed", "values"],
                "default": "optional_default_value"
            }
        },
        "required": ["list", "of", "required", "parameters"]
    }
}
```

### 复杂函数模式

```json
{
    "name": "research_query",
    "description": "Perform structured research using multiple sources",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Research question or topic"
            },
            "sources": {
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": ["web", "academic", "news", "books", "patents"]
                },
                "description": "Information sources to use"
            },
            "max_results": {
                "type": "integer",
                "minimum": 1,
                "maximum": 50,
                "default": 10,
                "description": "Maximum number of results per source"
            },
            "filters": {
                "type": "object",
                "properties": {
                    "date_range": {
                        "type": "string",
                        "pattern": "^\\d{4}-\\d{2}-\\d{2}:\\d{4}-\\d{2}-\\d{2}$",
                        "description": "Date range in format YYYY-MM-DD:YYYY-MM-DD"
                    },
                    "language": {
                        "type": "string",
                        "default": "en"
                    }
                }
            }
        },
        "required": ["query", "sources"]
    }
}
```

## 实现策略

### 1. 函数注册表模式

用于管理可用函数的集中式注册表：

```python
class FunctionRegistry:
    def __init__(self):
        self.functions = {}
        self.categories = {}
        
    def register(self, func, category=None, **metadata):
        """Register a function with metadata"""
        self.functions[func.__name__] = {
            'function': func,
            'signature': self._extract_signature(func),
            'category': category,
            'metadata': metadata
        }
        
    def get_available_functions(self, category=None):
        """Get functions available for the current context"""
        if category:
            return {name: info for name, info in self.functions.items() 
                   if info['category'] == category}
        return self.functions
        
    def call(self, function_name, **kwargs):
        """Execute a registered function safely"""
        if function_name not in self.functions:
            raise ValueError(f"Function {function_name} not found")
            
        func_info = self.functions[function_name]
        return func_info['function']( **kwargs)
```

### 2. 参数校验策略

```python
from jsonschema import validate, ValidationError

def validate_parameters(function_schema, parameters):
    """Validate function parameters against schema"""
    try:
        validate(instance=parameters, schema=function_schema['parameters'])
        return True, None
    except ValidationError as e:
        return False, str(e)

def safe_function_call(function_name, parameters, registry):
    """Safely execute function with validation"""
    func_info = registry.get_function(function_name)
    
    # Validate parameters
    is_valid, error = validate_parameters(func_info['schema'], parameters)
    if not is_valid:
        return {"error": f"Parameter validation failed: {error}"}
    
    try:
        result = registry.call(function_name, **parameters)
        return {"success": True, "result": result}
    except Exception as e:
        return {"error": f"Function execution failed: {str(e)}"}
```

### 3. 上下文感知的函数选择

```python
def select_optimal_functions(query, available_functions, context):
    """Select the most appropriate functions for a given query"""
    
    # Analyze query intent
    intent = analyze_intent(query)
    
    # Score functions based on relevance
    scored_functions = []
    for func_name, func_info in available_functions.items():
        relevance_score = calculate_relevance(
            intent, 
            func_info['description'],
            func_info['category']
        )
        
        # Consider context constraints
        context_score = evaluate_context_fit(func_info, context)
        
        total_score = relevance_score * context_score
        scored_functions.append((func_name, total_score))
    
    # Return top-ranked functions
    return sorted(scored_functions, key=lambda x: x[1], reverse=True)
```

## 高级函数调用模式

### 1. 函数组合

```json
{
    "name": "composed_research_analysis",
    "description": "Compose multiple functions for comprehensive analysis",
    "workflow": [
        {
            "function": "research_query",
            "parameters": {"query": "{input.topic}", "sources": ["web", "academic"]},
            "output_name": "research_results"
        },
        {
            "function": "summarize_content",
            "parameters": {"content": "{research_results.data}"},
            "output_name": "summary"
        },
        {
            "function": "extract_insights",
            "parameters": {"summary": "{summary.text}"},
            "output_name": "insights"
        }
    ]
}
```

### 2. 条件式函数执行

```json
{
    "name": "adaptive_problem_solving",
    "description": "Conditionally execute functions based on intermediate results",
    "workflow": [
        {
            "function": "analyze_problem",
            "parameters": {"problem": "{input.problem}"},
            "output_name": "analysis"
        },
        {
            "condition": "analysis.complexity > 0.7",
            "function": "break_down_problem",
            "parameters": {"problem": "{input.problem}", "analysis": "{analysis}"},
            "output_name": "subproblems"
        },
        {
            "condition": "analysis.requires_research",
            "function": "research_query",
            "parameters": {"query": "{analysis.research_queries}"},
            "output_name": "research_data"
        }
    ]
}
```

### 3. 错误处理与重试逻辑

```python
def robust_function_call(function_name, parameters, max_retries=3):
    """Execute function with retry logic and error handling"""
    
    for attempt in range(max_retries):
        try:
            result = execute_function(function_name, parameters)
            
            # Validate result
            if validate_result(result):
                return {"success": True, "result": result, "attempts": attempt + 1}
            else:
                # Invalid result, try with adjusted parameters
                parameters = adjust_parameters(parameters, result)
                
        except TemporaryError as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            else:
                return {"error": f"Max retries exceeded: {str(e)}"}
                
        except PermanentError as e:
            return {"error": f"Permanent error: {str(e)}"}
    
    return {"error": "Max retries exceeded without success"}
```

## 函数调用的提示词（prompt）模板

### 基本函数调用模板

```
FUNCTION_CALLING_TEMPLATE = """
You have access to the following functions:

{function_definitions}

When you need to use a function, respond with a function call in this format:
```function_call
{
    "function": "function_name",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
    }
}


Current task: {user_query}

Think step by step about what functions you need to use and in what order.
"""
```

### 多步推理模板

```
MULTI_STEP_FUNCTION_TEMPLATE = """
You are a reasoning agent with access to specialized tools. For complex tasks, break them down into steps and use the appropriate functions for each step.

Available functions:
{function_definitions}

Task: {user_query}

Approach this systematically:
1. Analyze what needs to be done
2. Identify which functions are needed
3. Plan the sequence of function calls
4. Execute the plan step by step
5. Synthesize the results

Begin your reasoning:
"""
```

### 错误恢复模板

```
ERROR_RECOVERY_TEMPLATE = """
The previous function call failed with error: {error_message}

Function that failed: {failed_function}
Parameters used: {failed_parameters}

Available alternatives:
{alternative_functions}

Please:
1. Analyze why the function call might have failed
2. Suggest an alternative approach
3. Retry with corrected parameters or use a different function

Continue working toward the goal: {original_goal}
"""
```

## 安全与防护考量

### 1. 函数访问控制

```python
class SecureFunctionRegistry(FunctionRegistry):
    def __init__(self):
        super().__init__()
        self.access_policies = {}
        self.audit_log = []
        
    def set_access_policy(self, function_name, policy):
        """Set access control policy for a function"""
        self.access_policies[function_name] = policy
        
    def call(self, function_name, context=None, **kwargs):
        """Execute function with security checks"""
        # Check access permissions
        if not self._check_access(function_name, context):
            raise PermissionError(f"Access denied to {function_name}")
        
        # Log the function call
        self._log_call(function_name, kwargs, context)
        
        # Execute with resource limits
        return self._execute_with_limits(function_name, **kwargs)
```

### 2. 输入清理

```python
def sanitize_function_input(parameters):
    """Sanitize function parameters to prevent injection attacks"""
    sanitized = {}
    
    for key, value in parameters.items():
        if isinstance(value, str):
            # Remove potentially dangerous characters
            sanitized[key] = re.sub(r'[<>"\';]', '', value)
        elif isinstance(value, dict):
            sanitized[key] = sanitize_function_input(value)
        elif isinstance(value, list):
            sanitized[key] = [sanitize_function_input(item) if isinstance(item, dict) 
                            else item for item in value]
        else:
            sanitized[key] = value
            
    return sanitized
```

### 3. 资源限制

```python
import signal
from contextlib import contextmanager

@contextmanager
def timeout(seconds):
    """Context manager for function timeout"""
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Function execution timed out after {seconds} seconds")
    
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

def execute_with_resource_limits(function, max_time=30, max_memory=None):
    """Execute function with resource constraints"""
    with timeout(max_time):
        if max_memory:
            # Set memory limit (implementation depends on platform)
            resource.setrlimit(resource.RLIMIT_AS, (max_memory, max_memory))
        
        return function()
```

## 最佳实践与指南

### 1. 函数设计原则

- **单一职责**: 每个函数应有一个明确的用途
- **清晰的接口**: 参数和返回值应明确定义
- **错误处理**: 函数应妥善处理错误
- **文档**: 提供全面的说明，便于 LLM 理解
- **幂等性**: 尽可能确保函数可以安全重试

### 2. 函数调用策略

- **渐进式披露**: 从简单函数开始，按需增加复杂度
- **上下文感知**: 选择函数时考虑对话状态
- **结果校验**: 继续执行前校验函数输出
- **错误恢复**: 制定处理函数失败的策略
- **性能监控**: 跟踪函数使用情况与性能

### 3. 集成模式

- **注册表模式**: 集中式函数管理
- **工厂模式**: 根据上下文动态创建函数
- **责任链模式**: 顺序执行函数
- **观察者模式**: 函数调用监控与日志记录
- **策略模式**: 可插拔的函数执行策略

## 评估与测试

### 函数调用质量指标

```python
def evaluate_function_calling(test_cases):
    """Evaluate function calling performance"""
    metrics = {
        'success_rate': 0,
        'parameter_accuracy': 0,
        'function_selection_accuracy': 0,
        'error_recovery_rate': 0,
        'efficiency_score': 0
    }
    
    for test_case in test_cases:
        result = execute_test_case(test_case)
        
        # Update metrics based on result
        metrics['success_rate'] += result.success
        metrics['parameter_accuracy'] += result.parameter_accuracy
        metrics['function_selection_accuracy'] += result.selection_accuracy
        
    # Normalize metrics
    total_tests = len(test_cases)
    for key in metrics:
        metrics[key] /= total_tests
        
    return metrics
```

## 未来方向

### 1. 自适应函数发现
- 能够发现并学习新函数的 LLM
- 自动组合与优化函数
- 自我改进的函数调用策略

### 2. 多模态函数集成
- 处理文本、图像、音频和视频的函数
- 跨模态推理与函数串联
- 面向不同工具类型的统一接口

### 3. 协作式函数执行
- 多智能体（multi-agent）函数调用协调
- 分布式函数执行
- 基于共识的函数选择

## 结论

函数调用基础为 Software 3.0 范式中的工具集成推理奠定了根基。通过让 LLM 以结构化方式访问外部能力，我们将其从孤立的推理引擎转变为具备编排能力的智能系统，能够解决复杂的现实问题。

成功实现函数调用的关键在于：
1. **清晰的接口设计**: 明确定义的函数签名与模式
2. **稳健执行**: 安全可靠地执行函数，并妥善处理错误
3. **智能选择**: 上下文感知的函数选择与组合
4. **安全意识**: 恰当的访问控制与输入校验
5. **持续改进**: 监控、评估与优化

随着我们继续学习工具集成策略、智能体与环境交互以及推理框架，这些基础知识将为构建复杂的工具增强智能提供稳固根基。

---

*这些基础使 LLM 能够超越训练边界，通过结构化的工具集成，成为真正有能力协助解决复杂动态问题的伙伴。*
