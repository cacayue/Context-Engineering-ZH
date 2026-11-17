---
title: 验证回路模板
source: 20_templates/PROMPTS/verification_loop.md
module: M6
task: M6-01
chunks: 2
chunks_done: [1, 2]
status: published
source_sha256: 9eb9c62099cc9565f3903938ee031a599ff385f933ee83872b3a39f90fdef478
---

> 原文：[20_templates/PROMPTS/verification_loop.md](../../../20_templates/PROMPTS/verification_loop.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 验证回路模板

## 概述
此模板通过结构化检查机制实现自验证过程，以发现错误、验证结果并提高整体可靠性。

## 上下文与应用
当准确性至关重要，且你希望在推理过程中加入显式验证时，可使用此模板。验证回路鼓励在确定最终结果前系统检查假设、计算和结论，从而减少错误。

此模板适用于：
- 错误可能造成高昂代价的高风险任务
- 复杂计算或逻辑推理链
- 容易出现常见推理谬误的情况
- 周全程度比速度更重要的情况
- 任何重视结果可验证性的任务

## 模板结构

```
# Task: {{task_description}}

## Approach
Complete this task using a verification loop:

1. Initial Solution
   - {{solution_approach}}
   - Develop your initial answer

2. Verification Process
   - Check assumptions: {{assumption_verification}}
   - Verify calculations/logic: {{process_verification}}
   - Test edge cases: {{edge_case_verification}}
   - Consider alternatives: {{alternative_verification}}

3. Error Correction
   - Identify any issues found during verification
   - Make necessary corrections

4. Final Answer
   - Present your verified solution
   - Note any uncertainty or limitations

## Expected Output
Show your complete process including initial solution, verification steps, any corrections, and final verified answer.
```

## 参数

- `{{task_description}}`: 清晰描述待完成的任务
- `{{solution_approach}}`: 初始求解使用的方法（例如，“使用代数方程”）
- `{{assumption_verification}}`: 如何验证假设（例如，“确认所有变量均被正确解释”）
- `{{process_verification}}`: 如何检查计算或逻辑（例如，“使用不同方法重新计算”）
- `{{edge_case_verification}}`: 需要检查的具体边界情况（例如，“使用边界值测试”）
- `{{alternative_verification}}`: 验证结果的替代方法（例如，“使用不同技术求解”）

## 示例

### 示例 1：数学问题验证

```
# Task: Calculate the future value of an investment of $10,000 with an annual interest rate of 5% compounded monthly over 10 years.

## Approach
Complete this task using a verification loop:

1. Initial Solution
   - Use the compound interest formula: P(1 + r/n)^(nt)
   - Calculate the result with the given values

2. Verification Process
   - Check assumptions: Verify the formula is appropriate for this problem
   - Verify calculations: Recalculate step by step, checking each arithmetic operation
   - Test edge cases: Calculate for 1 year and confirm it matches expected growth
   - Consider alternatives: Calculate using the FV = P * e^(rt) formula as a cross-check

3. Error Correction
   - Identify any discrepancies between the two calculation methods
   - Check for common errors (decimal place mistakes, incorrect exponents)
   - Make corrections if needed

4. Final Answer
   - Present the verified future value
   - Express with appropriate precision and units

## Expected Output
Show your complete process including initial solution, verification steps, any corrections, and final verified answer.
```

### 示例 2：代码评审验证

```
# Task: Review the following Python function that calculates the factorial of a number and identify any bugs or issues.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

## Approach
Complete this task using a verification loop:

1. Initial Review
   - Analyze the code line by line
   - Identify any potential issues in the implementation

2. Verification Process
   - Check assumptions: Verify the recursive approach is appropriate
   - Verify logic: Trace the execution for sample inputs (n=3, n=0)
   - Test edge cases: Consider negative numbers, large inputs, and non-integer inputs
   - Consider alternatives: Compare with an iterative implementation

3. Issue Identification
   - List any bugs, edge cases, or performance issues found
   - Categorize issues by severity (critical, moderate, minor)

4. Final Assessment
   - Provide a verified assessment of the code quality
   - Suggest specific improvements or fixes

## Expected Output
Show your complete process including initial review, verification steps, issues found, and final assessment with recommendations.
```

## Variations

### Triple Check Verification
For critical tasks requiring multiple verification approaches:

```
# Task: {{task_description}}

## Approach
Complete this task with triple verification:

1. Initial Solution
   - {{solution_approach}}

2. First Verification: Alternative Method
   - Solve the same problem using a different approach
   - Compare results with initial solution

3. Second Verification: Error Analysis
   - Identify potential error sources in both methods
   - Check for these specific errors

4. Third Verification: Test Cases
   - Test with {{test_case_1}}
   - Test with {{test_case_2}}

5. Final Answer
   - Reconcile any differences between verification methods
   - Present final verified solution

## Expected Output
Complete process with all three verification approaches and final reconciled answer.
```

### Peer Review Simulation
For stimulating different perspectives on the same problem:

```
# Task: {{task_description}}

## Approach
Simulate a peer review process:

1. Initial Solution
   - Solve the problem using {{primary_method}}

2. Reviewer A Perspective
   - Critically examine the solution from the perspective of {{reviewer_A_expertise}}
   - Identify potential issues or improvements

3. Reviewer B Perspective
   - Examine the solution from the perspective of {{reviewer_B_expertise}}
   - Identify different potential issues or improvements

4. Reconciliation
   - Address all raised concerns
   - Incorporate valid suggestions

5. Final Solution
   - Present the improved solution after review

## Expected Output
Initial solution, both reviewer perspectives, reconciliation process, and final improved solution.
```

### Progressive Refinement Verification
For iteratively improving solutions:

```
# Task: {{task_description}}

## Approach
Use progressive refinement:

1. Draft Solution (Version 1)
   - Quick first attempt at the problem

2. Analysis of Version 1
   - Identify weaknesses and improvement areas

3. Refined Solution (Version 2)
   - Address identified issues

4. Verification of Version 2
   - Test against original requirements
   - Check for new issues introduced

5. Final Solution (Version 3)
   - Make final refinements
   - Verify completeness and correctness

## Expected Output
All three versions with analyses and verification steps between versions.
```

## Best Practices

- **Use different methods for verification** than for the initial solution
- **Include both conceptual and computational verification** - check both the approach and the execution
- **Anticipate common errors** specific to the task type and verify against them
- **For mathematical problems**, verify with different formulas or approximation methods
- **For logical arguments**, check for fallacies and test with counterexamples
- **For complex tasks**, verify components separately before verifying the whole
- **Document verification steps explicitly** - don't just say "verified" but explain how
- **Consider both false positives and false negatives** in your verification
- **Use order-of-magnitude checks** for numerical problems to catch major errors
- **For critical tasks**, implement multiple independent verification methods

## Related Templates

- **Chain of Thought Template**: The foundation that verification loops build upon
- **Task Decomposition Template**: Useful for breaking complex verification into manageable parts
- **Adversarial Thinking Template**: For verification through challenging assumptions
- **递归自我改进模板**：迭代增强验证过程
