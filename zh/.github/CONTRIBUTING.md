---
title: 为上下文工程贡献力量
source: .github/CONTRIBUTING.md
module: M10
task: M10-04
chunks: 2
chunks_done: [1, 2]
status: published
source_sha256: 32e71825933f9e5bd3c2dbd32885da68789afbab868896e08e6a93bca3a676fd
---

> 原文：[.github/CONTRIBUTING.md](../../.github/CONTRIBUTING.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../LEARNING_PATH.md)
# 为上下文工程贡献力量

> *「上下文工程（Context Engineering）是一门精细的艺术与科学：在上下文窗口（context window）中填入恰好适合下一步的信息。」* —— Andrej Karpathy

感谢你有兴趣为上下文工程仓库做贡献！本文介绍参与本项目的流程与准则。本项目旨在运用第一性原理和可视化，将最新的上下文（context）研究转化为可操作的方法。

##  核心理念

我们的上下文工程方法采用复杂度逐步提升的生物学隐喻：

```
atoms → molecules → cells → organs → neural systems → neural fields
  │        │         │         │             │              │
single    few-     memory/    multi-    cognitive tools + context = fields +
prompt    shot      agents    agents     prompt programs   persistence & resonance
```
> 图：从单个提示词到持久共振场的演进 —— atoms → molecules → cells → organs → neural systems → neural fields

所有贡献都应符合我们的实施策略：

1. **分层方法**：从基础概念逐步构建到高级集成
2. **注重实践**：确保所有理论都有相应的实践实现
3. **模块化设计**：创建可组合、可重新搭配的组件
4. **渐进复杂度**：从简单开始，逐步增加精细程度
5. **强调集成**：关注组件如何协同工作，而不只是单独运行
6. **自我改进**：构建能够提升自身能力的系统
7. **透明性**：即使复杂度提高，也确保操作可以理解
8. **协作**：面向有效的人类与 AI 合作进行设计
9. **模态灵活性**：支持跨不同模态的统一理解

##  贡献类型

我们欢迎以下几类贡献：

### 1. 理论框架
- 理解上下文工程的新模型
- 对现有框架的扩展
- 整合认知科学、语言学或 AI 研究

### 2. 代码实现
- 展示上下文工程原理的示例
- 上下文管理（context management）与优化工具
- 用于上下文工程操作的库

### 3. 文档与教程
- 解释核心概念的指南
- 分步教程
- 展示上下文工程实践的案例研究

### 4. 视觉资产
- 说明上下文工程概念的图示
- 上下文动力学的可视化
- 交互式演示

### 5. 研究整合
- 相关学术论文的摘要
- 研究成果的实现
- 连接研究与实际应用的桥梁

##  贡献流程

### 入门

1. **复刻仓库**
   - 点击仓库页面右上角的「Fork」按钮

2. **将复刻仓库克隆到本地**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Context-Engineering.git
   cd Context-Engineering
   ```

3. **为贡献创建新分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### 开发准则

#### 代码贡献

1. **遵循现有结构**
   - 根据仓库结构，将新代码放入合适的目录
   - 遵循既定的命名约定

2. **文档**
   - 为所有函数和类提供文档字符串
   - 添加注释解释复杂部分
   - 更新相关 README 文件

3. **测试**
   - 为新功能添加测试
   - 确保现有测试通过

4. **示例**
   - 提供展示如何使用贡献内容的实际示例
   - 包含预期输出或行为

#### 文档贡献

1. **遵循文档风格**
   - 所有文档均使用 Markdown
   - 保持格式一致
   - 使用清晰、简洁的语言

2. **渐进呈现**
   - 从基本概念开始
   - 逐步引入更复杂的思想
   - 同时解释「如何做」与「为什么」

3. **视觉辅助**
   - 在有帮助时加入图示
   - 简单示意使用 ASCII 图
   - 复杂概念添加 mermaid 图

### 提交流程

1. **提交更改**
   ```bash
   git add .
   git commit -m "Add feature X" -m "Detailed description of changes"
   ```

2. **推送到你的复刻仓库**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **创建拉取请求**
   - 前往原始仓库
   - 点击「New Pull Request」
   - 选择「compare across forks」
   - 选择你的复刻仓库和分支
   - 填写 PR 模板

4. **处理反馈**
   - 回复评审者的意见
   - 完成要求的更改
   - 向分支推送后续提交

##  贡献标准

### 代码标准

- **Python**：遵循 PEP 8 风格指南
- **JavaScript**：遵循 Airbnb JavaScript 风格指南
- **Jupyter notebook**：提交前清除输出
- **依赖**：尽量减少外部依赖

### 文档标准

- **语言**：清晰、简洁、易懂
- **结构**：渐进呈现概念
- **示例**：为所有概念提供实际示例
- **参考资料**：引用相关研究与来源

### 视觉标准

- **图示**：简单、清晰、信息充分
- **颜色**：使用一致的配色方案
- **无障碍**：确保色盲用户也能理解视觉内容
- **格式**：尽可能优先使用矢量格式（SVG）

##  仓库结构

请了解仓库结构，以便妥善放置贡献内容：

```
context-engineering/
├── 00_foundations/           # First-principles theory
├── 10_guides_zero_to_hero/   # Hands-on tutorials
├── 20_templates/             # Reusable components
├── 30_examples/              # Practical implementations
├── 40_reference/             # Deep-dive documentation
├── 50_contrib/               # Community contributions
├── 60_protocols/             # Protocol shells and frameworks
├── 70_agents/                # Agent demonstrations
├── 80_field_integration/     # Complete field projects
├── 90_meta_recursive/        # Meta-level systems
└── cognitive-tools/          # Advanced cognitive framework
```
> 图：按用途组织的仓库目录 —— Repository Structure

添加新内容时，请根据其复杂度和用途放入合适目录。

##  社区准则

### 沟通

- 尊重他人，兼容并包
- 讨论思想，而非针对个人
- 提供建设性反馈
- 通过提问澄清，而非质疑他人
- 慷慨分享知识

### 协作

- 帮助他人成功
- 注明原创思想和工作的来源
- 重大变更寻求共识
- 拆解复杂任务，方便参与贡献
- 尽可能指导新贡献者

## 🔍 评审流程

### 评审标准

所有贡献都将依据以下标准评审：

1. 与项目理念和目标的**一致性**
2. 实现或文档的**质量**
3. **实用性**和易用性
4. 解释的**清晰度**
5. 与现有组件的**集成程度**
6. 适合所在章节的**渐进复杂度**
7. 操作与解释的**透明性**

### 评审时间安排

- 初次评审：7 天内
- 后续评审：3 天内
- 最终决定：首次提交后 30 天内

##  贡献认可

贡献者将通过以下方式获得认可：

- 加入仓库及 CONTRIBUTORS.md 文件
- 在发布说明中提及
- 在相关文档中致谢
- 持续贡献者有机会更深入地参与项目

##  贡献者资源

### 学习资源

- 阅读 `00_foundations/` 目录，了解核心概念
- 完成 `10_guides_zero_to_hero/`，获得实践经验
- 查阅 CITATIONS.md 中的相关学术论文

### 开发设置

1. **环境设置**
   ```bash
   # 创建虚拟环境
   python -m venv venv
   source venv/bin/activate  # Windows 上使用：venv\Scripts\activate
   
   # 安装依赖
   pip install -r requirements.txt
   
   # 安装开发依赖
   pip install -r requirements-dev.txt
   ```

2. **编辑器配置**
   - 基本设置见 `.editorconfig`
   - 推荐的 VS Code 扩展列于 `.vscode/extensions.json`

3. **提交前钩子**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## ❓ 问题与支持

- 一般问题请创建 issue
- 在 [GitHub Discussions](https://github.com/davidkimai/Context-Engineering/discussions) 参与社区讨论
- 复杂讨论请给维护者发送邮件（见 MAINTAINERS.md）

## 🚩 Issue 标签

- `good first issue`：适合新手
- `documentation`：文档改进
- `enhancement`：新功能或改进
- `bug`：某处无法正常工作
- `research`：研究相关主题
- `visualization`：视觉组件
- `theory`：理论概念
- `implementation`：代码实现

##  贡献路径

我们为不同背景的贡献者设计了多条路径：

### 研究者
- 添加研究摘要
- 实现论文成果
- 创建基于研究的示例
- 开发评估（evaluation）指标

### 开发者
- 实现核心功能
- 创建库和工具
- 优化现有代码
- 添加测试框架

### 教育者
- 开发教程
- 创建解释性内容
- 设计交互式示例
- 构建可视化工具

### 实践者
- 添加真实案例研究
- 分享实践见解
- 制定最佳实践
- 创建应用模板（template）

##  结语

你的贡献对推动上下文工程领域的发展至关重要。遵循这些准则，你将帮助社区建立连贯、实用且有影响力的资源。

请记住我们的核心原则：
> *「认知工具（cognitive tool）、符号机制、量子语义（quantum semantics）以及记忆（memory）与推理协同的融合，代表着智能系统工程方式的范式转变——从简单的提示词工程（prompt engineering），走向全面的上下文工程与认知架构设计。」*

感谢你参与这段旅程！

---

这份 CONTRIBUTING.md 本身也是持续演进的文档。如果你有改进建议，请创建 issue 或提交拉取请求。
