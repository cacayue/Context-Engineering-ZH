---
title: 验证模板
source: cognitive-tools/cognitive-templates/verification.md
module: M9
task: M9-02
chunks: 1
chunks_done: [1]
status: published
source_sha256: bd281a013b06843bfa1769fda0506ef2b04ac5cc37ccf4a7a9e07abcb136c8d7
---

> 原文：[cognitive-tools/cognitive-templates/verification.md](../../../cognitive-tools/cognitive-templates/verification.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 验证模板

> 「信任，但要核实。」—— 俄罗斯谚语

## 概述

验证模板帮助语言模型检查自己的工作、发现错误并确保输出质量。这些模板对于提升可靠性、减少幻觉和提高整体准确率至关重要。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  VERIFICATION PROCESS                                        │
│                                                              │
│  Solution → Check Logic → Test Assumptions → Correct → Final │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

## 基础模板

### 1. 解答验证

检查解答或答案的基础模板。

```markdown
# Solution Verification Template

Task: Verify the correctness of the following solution.

Problem: {{problem}}
Proposed Solution: {{solution}}

Please follow this verification process:
1. **Restate the Problem**: Confirm understanding of what was asked.
2. **Check Methodology**: Is the approach used appropriate for this problem?
3. **Verify Calculations**: Check all mathematical operations for accuracy.
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
5. **Test with Examples**: Test the solution with specific examples or edge cases.
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
7. **Final Assessment**: State whether the solution is:
   - Correct: The solution is completely accurate
   - Partially Correct: The solution has minor errors (specify)
   - Incorrect: The solution has major flaws (specify)

If errors are found, explain them clearly and suggest corrections.
```

**词元（token）数**：约 160 token（仅模板）

**使用示例**：
- 用于数学解答
- 用于检查逻辑论证
- 用于任何准确性至关重要的输出

### 2. 事实核查

用于核实事实性主张和陈述。

```markdown
# Fact Checking Template

Task: Verify the accuracy of the following statement(s).

Statement(s): {{statements}}

Please follow this verification process:
1. **Break Down Claims**: Identify each distinct factual claim.
2. **Assess Knowledge Base**: Determine if you have reliable information about each claim.
3. **Verify Each Claim**:
   - Claim 1: [Restate the claim]
     - Assessment: [Accurate / Inaccurate / Partially Accurate / Uncertain]
     - Explanation: [Provide relevant facts and context]
     - Confidence: [High / Medium / Low]
   - Claim 2: [Continue for each claim]
4. **Check for Omissions**: Identify any relevant context that's missing.
5. **Overall Assessment**: Summarize the overall accuracy.
6. **Knowledge Limitations**: Note any claims you cannot verify with confidence.

Provide corrections for any inaccurate information.
```

**词元数**：约 150 token（仅模板）

**使用示例**：
- 用于检查历史或科学主张
- 用于核实摘要中的信息
- 用于任何包含事实性断言的输出

### 3. 一致性检查

用于确保内容内部一致。

```markdown
# Consistency Check Template

Task: Check the following content for internal consistency.

Content: {{content}}

Please follow this verification process:
1. **Identify Key Elements**: Note the main claims, definitions, and arguments.
2. **Create Consistency Map**:
   - Element 1: [Description]
   - Element 2: [Description]
   - [Continue for all important elements]
3. **Check for Contradictions**:
   - Between Elements: Compare each element with others for compatibility
   - Within Elements: Check each element for internal contradictions
4. **Temporal Consistency**: Ensure events and developments follow a logical timeline.
5. **Terminology Consistency**: Verify that terms are used consistently throughout.
6. **Logical Flow**: Check that conclusions follow from premises.
7. **Final Assessment**: Summarize any inconsistencies found.

For each inconsistency, explain the contradiction and suggest a resolution.
```

**词元数**：约 160 token（仅模板）

**使用示例**：
- 用于长篇内容
- 用于检查复杂论证
- 用于任何建立在多个前提之上的输出

## 高级模板

### 4. 全面错误分析

用于从多个维度详细审查潜在错误。

```markdown
# Comprehensive Error Analysis Template

Task: Perform a thorough error analysis on the following content.

Content: {{content}}
Context: {{context}}

Please examine for these error types:
1. **Factual Errors**:
   - Incorrect statements: [Identify and correct]
   - Outdated information: [Identify and update]
   - Misattributed statements: [Identify and correct]

2. **Logical Errors**:
   - False equivalences: [Identify]
   - Non sequiturs: [Identify]
   - Circular reasoning: [Identify]
   - Hasty generalizations: [Identify]

3. **Mathematical/Computational Errors**:
   - Calculation mistakes: [Identify and correct]
   - Formula application errors: [Identify and correct]
   - Unit conversion issues: [Identify and correct]

4. **Contextual Errors**:
   - Misunderstanding of context: [Clarify]
   - Inappropriate assumptions: [Identify]
   - Missing relevant information: [Supply]

5. **Linguistic Errors**:
   - Ambiguous statements: [Clarify]
   - Incorrect terminology: [Correct]
   - Inconsistent language: [Standardize]

6. **Structural Errors**:
   - Organizational problems: [Identify]
   - Missing components: [Identify]
   - Redundancies: [Identify]

For each error found, explain:
- What the error is
- Why it's problematic
- How it should be corrected

Conclude with an overall assessment of the content's accuracy and reliability.
```

**词元数**：约 240 token（仅模板）

**使用示例**：
- 用于对重要内容进行批判性审查
- 用于要求最高准确性的情况
- 用于同行评审或编辑流程

### 5. 替代视角分析

用于检查偏见并探索其他观点。

```markdown
# Alternative Perspective Analysis Template

Task: Analyze the following content from alternative perspectives to check for bias or blind spots.

Content: {{content}}

Please follow this process:
1. **Identify the Content's Perspective**: What worldview, assumptions, or values underlie the content?

2. **Explore Alternative Perspectives**:
   - Perspective A: [Description of a different viewpoint]
     - How would this perspective view the content?
     - What would it critique or question?
     - What additional considerations would it raise?
   
   - Perspective B: [Description of another different viewpoint]
     - How would this perspective view the content?
     - What would it critique or question?
     - What additional considerations would it raise?
   
   - [Continue with additional relevant perspectives]

3. **Identify Blind Spots**: What important considerations are missing from the original content?

4. **Check for Unstated Assumptions**: What does the content take for granted that might be questioned?

5. **Balance Assessment**: Is the content fair and balanced, or does it favor certain perspectives?

6. **Recommendations**: Suggest modifications that would make the content more comprehensive and balanced.

This analysis helps ensure that the content accounts for diverse viewpoints and avoids unintentional bias.
```

**词元数**：约 220 token（仅模板）

**使用示例**：
- 用于政策分析
- 用于检查文化或意识形态偏见
- 用于任何涉及争议话题的内容

### 6. 实施验证

用于检查解决方案能否真正实施。

```markdown
# Implementation Verification Template

Task: Verify that the following solution can be practically implemented.

Proposed Solution: {{solution}}
Implementation Context: {{context}}

Please follow this verification process:
1. **Feasibility Assessment**:
   - Technical feasibility: Can this be built with available technology?
   - Resource requirements: What resources (time, money, skills) would be needed?
   - Scalability: Would the solution work at the required scale?

2. **Constraints Check**:
   - Technical constraints: Does the solution respect technical limitations?
   - Regulatory constraints: Does it comply with relevant regulations?
   - Operational constraints: Can it be implemented within operational parameters?

3. **Risk Analysis**:
   - Implementation risks: What could go wrong during implementation?
   - Operational risks: What could go wrong once implemented?
   - Mitigation strategies: How could these risks be addressed?

4. **Dependency Analysis**:
   - External dependencies: What does this solution depend on?
   - Critical path: Which dependencies are on the critical path?
   - Vulnerability points: Where could dependencies cause problems?

5. **Testing Approach**:
   - Validation methods: How could the implementation be tested?
   - Success criteria: How would success be measured?
   - Failure scenarios: How would failures be detected and addressed?

6. **Overall Assessment**: Is the solution implementable as described? What modifications would improve implementability?

This verification ensures that solutions are not just theoretically sound but practically viable.
```

**词元数**：约 240 token（仅模板）

**使用示例**：
- 用于工程解决方案
- 用于评估项目提案
- 用于任何需要实际实施的解决方案

## 实现模式

下面是实现解答验证模板的简单 Python 函数：

```python
def verify_solution(problem, solution):
    """
    Create a prompt that verifies a proposed solution.
    
    Args:
        problem (str): The original problem
        solution (str): The proposed solution to verify
        
    Returns:
        str: A formatted prompt for solution verification
    """
    return f"""
Task: Verify the correctness of the following solution.

Problem: {problem}
Proposed Solution: {solution}

Please follow this verification process:
1. **Restate the Problem**: Confirm understanding of what was asked.
2. **Check Methodology**: Is the approach used appropriate for this problem?
3. **Verify Calculations**: Check all mathematical operations for accuracy.
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
5. **Test with Examples**: Test the solution with specific examples or edge cases.
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
7. **Final Assessment**: State whether the solution is:
   - Correct: The solution is completely accurate
   - Partially Correct: The solution has minor errors (specify)
   - Incorrect: The solution has major flaws (specify)

If errors are found, explain them clearly and suggest corrections.
"""
```

## 自我纠正回路

验证模板最强大的应用之一是自我纠正回路：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Initial Solution                                                   │
│       │                                                             │
│       ▼                                                             │
│  Apply Verification Template                                        │
│       │                                                             │
│       ▼                                                             │
│  Errors Found?                                                      │
│       │                                                             │
│       ├─────────────Yes─────────────┐                               │
│       │                             │                               │
│       ▼                             ▼                               │
│  No   │                        Apply Corrections                    │
│       │                             │                               │
│       ▼                             ▼                               │
│  Final Verified Solution ◄──────────┘                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
> 图：认知流程与结构示意 —— Cognitive architecture

实现示例：

```python
def self_correction_loop(problem, max_iterations=3):
    """
    Implement a self-correction loop for problem solving.
    
    Args:
        problem (str): The problem to solve
        max_iterations (int): Maximum number of correction iterations
        
    Returns:
        dict: The final solution and verification history
    """
    # Initial solution
    solution = llm.generate(f"Solve this problem: {problem}")
    
    history = [{"type": "solution", "content": solution}]
    iteration = 0
    
    while iteration < max_iterations:
        # Verify the current solution
        verification = llm.generate(verify_solution(problem, solution))
        history.append({"type": "verification", "content": verification})
        
        # Check if corrections are needed
        if "Correct: The solution is completely accurate" in verification:
            break
        
        # Generate corrected solution
        correction_prompt = f"""
        Based on the verification feedback below, provide a corrected solution to the original problem.
        
        Original Problem: {problem}
        
        Previous Solution: {solution}
        
        Verification Feedback: {verification}
        
        Please provide a fully corrected solution that addresses all issues identified in the verification.
        """
        
        corrected_solution = llm.generate(correction_prompt)
        history.append({"type": "correction", "content": corrected_solution})
        
        # Update solution for next iteration
        solution = corrected_solution
        iteration += 1
    
    return {
        "problem": problem,
        "final_solution": solution,
        "verification_history": history,
        "iterations": iteration
    }
```

## 衡量与优化

使用验证模板时，可通过以下指标衡量效果：

1. **错误检出率**：能发现多大比例的注入错误？
2. **误报率**：正确元素被错误标记的频率是多少？
3. **纠正质量**：建议的纠正措施有多有效？
4. **迭代效率**：需要多少次迭代才能得到正确解答？

可通过以下方式优化模板：
- 为专业领域添加领域特定的验证步骤
- 根据准确性的重要程度调整审查力度
- 聚焦特定任务中常见的错误类型

## 与其他工具结合

验证模板使认知工作流形成闭环：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
          ▲                                                │
          │                                                │
          └────────────────────────────────────────────────┘
                        (Correction Loop)
```
> 图：认知流程与结构示意 —— Cognitive architecture

由此构成完整的认知系统，能够：
1. 理解问题
2. 生成解答
3. 验证并纠正解答
4. 持续迭代，直至获得满意结果

## 后续步骤

- 探索 [composition.md](./composition.md)，了解组合多个模板的方法
- 参阅 [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md)，了解如何将这些模板集成到完整认知程序中
- 通过 [../cognitive-architectures/solver-architecture.md](../cognitive-architectures/solver-architecture.md) 了解完整认知架构
