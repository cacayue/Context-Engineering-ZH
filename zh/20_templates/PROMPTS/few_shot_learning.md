---
title: 少样本（Few-Shot）学习模板
source: 20_templates/PROMPTS/few_shot_learning.md
module: M6
task: M6-01
chunks: 1
chunks_done: [1]
status: published
source_sha256: fb21e5b41c4390d2c650b6f2920fb8dfe1182e2f310715409ac90e3080fcb2b3
---

> 原文：[20_templates/PROMPTS/few_shot_learning.md](../../../20_templates/PROMPTS/few_shot_learning.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
# 少样本（Few-Shot）学习模板

## 摘要
通过示例教导 AI 系统，使其无需明确指令即可学习模式（Pattern）并应用于新案例的模板。

## 上下文（Context）与应用
当你希望 AI 从示例而非明确规则或指令中学习时，使用此模板。少样本学习通过展示而非讲述发挥作用，使 AI 能够推断模式并应用于新情况。

此模板非常适合：
- 难以解释但易于演示的任务
- 示例比规则更能传达模式的模式型任务
- 希望格式或风格一致的情况
- 教授细致的判断或分类

## 模板结构

```
# Task: {{task_description}}

## Examples

### Example 1
Input: {{input_1}}
Output: {{output_1}}

### Example 2
Input: {{input_2}}
Output: {{output_2}}

### Example 3
Input: {{input_3}}
Output: {{output_3}}

## Your Turn
Input: {{new_input}}
Output:
```

## 参数

- `{{task_description}}`：简述要执行的任务（例如「对这些评论进行情感分类」）
- `{{input_X}}`：展示模式的输入示例（建议 3-5 个示例）
- `{{output_X}}`：对应的输出，展示各输入的预期响应
- `{{new_input}}`：希望 AI 运用所学模式处理的新案例

## 示例

### 示例 1：情感分类

```
# Task: Classify the sentiment of customer feedback as positive, negative, or neutral

## Examples

### Example 1
Input: "The product arrived on time and works perfectly. Couldn't be happier with my purchase!"
Output: Positive

### Example 2
Input: "Delivery was quick but the product has several scratches on the surface."
Output: Neutral

### Example 3
Input: "Terrible customer service. Had to call three times and still haven't resolved my issue."
Output: Negative

## Your Turn
Input: "Package was delivered two days late, but the quality of the item exceeded my expectations."
Output:
```

### 示例 2：数据转换

```
# Task: Convert the given product information into a standardized JSON format

## Examples

### Example 1
Input: 
Product: Wireless Headphones
Brand: SoundCore
Price: $79.99
Features: Noise cancellation, 30-hour battery, Bluetooth 5.0

Output:
```json
{
  "product_name": "Wireless Headphones",
  "manufacturer": "SoundCore",
  "price_usd": 79.99,
  "specifications": [
    "Noise cancellation",
    "30-hour battery",
    "Bluetooth 5.0"
  ]
}
```

### Example 2
Input:
Product: Smart Watch Pro
Brand: TechFit
Price: $129.95
Features: Heart rate monitor, GPS tracking, Water resistant

Output:
```json
{
  "product_name": "Smart Watch Pro",
  "manufacturer": "TechFit",
  "price_usd": 129.95,
  "specifications": [
    "Heart rate monitor",
    "GPS tracking",
    "Water resistant"
  ]
}
```

## Your Turn
Input:
Product: Portable Bluetooth Speaker
Brand: AudioMax
Price: $45.50
Features: Waterproof, 12-hour playback, Built-in microphone

Output:
```

## Variations

### Zero-Shot Extension
For when you have no examples but can describe the pattern:

```
# Task: {{task_description}}

## Pattern
{{detailed_pattern_description}}

## Format
{{output_format_specification}}

## Your Turn
Input: {{new_input}}
Output:
```

### One-Shot Learning
For simple patterns that can be communicated with a single example:

```
# Task: {{task_description}}

## Example
Input: {{input_example}}
Output: {{output_example}}

## Your Turn
Input: {{new_input}}
Output:
```

### Many-Shot Learning
For complex patterns requiring many examples:

```
# Task: {{task_description}}

## Examples
[Examples 1-10 formatted as input/output pairs]

## Test Cases
[Additional examples to validate understanding]

## Your Turn
Input: {{new_input}}
Output:
```

## Best Practices

- **Use diverse examples** that cover different cases and edge conditions
- **Order examples strategically** from simple to complex to build understanding
- **Include 3-5 examples** for most tasks (fewer for simple patterns, more for complex ones)
- **Ensure consistency** in formatting across all examples
- **Choose representative examples** that clearly demonstrate the pattern
- **Make examples distinct enough** to highlight the pattern rather than superficial similarities
- **For classification tasks**, include examples of all possible categories
- **For generative tasks**, show range in style, length, and content as appropriate
- **Test the pattern** by trying different inputs to ensure the AI has properly learned it

## Related Templates

- **Minimal Context Template**: When examples aren't necessary and direct instructions suffice
- **Chain of Thought Template**: When you need to demonstrate reasoning processes step-by-step
- **模式与反模式模板**：用于正反示例有助于明确预期的情况
