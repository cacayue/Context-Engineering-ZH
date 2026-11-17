---
title: CLAUDE.md —— 认知操作系统
source: CLAUDE.md
module: M1
task: M1-02
chunks: 4
chunks_done:
  - 1
  - 2
  - 3
  - 4
status: published
source_sha256: 772aa478077dc590f12447e4ee0247a629537591b7b36c7347f8a17bb6c35cd6
---

> 原文：[CLAUDE.md](../CLAUDE.md)
> 术语对照：[GLOSSARY.md](GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](LEARNING_PATH.md)
# CLAUDE.md —— 认知操作系统

本文档为 Claude Code 提供了一套全面的框架，涵盖认知工具、协议壳（protocol shell）、推理模板与工作流。将本文件加载到项目根目录，可在所有上下文中增强 Claude 的能力。

## 1. 核心元认知框架

## 上下文模式

### 代码理解模式

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "代码理解模式",
  "description": "用于分析和理解代码的标准化格式",
  "type": "object",
  "properties": {
    "codebase": {
      "type": "object",
      "properties": {
        "structure": {
          "type": "array",
          "description": "关键文件与目录及其用途"
        },
        "architecture": {
          "type": "string",
          "description": "整体架构模式"
        },
        "technologies": {
          "type": "array",
          "description": "关键技术、框架与库"
        }
      }
    },
    "functionality": {
      "type": "object",
      "properties": {
        "entry_points": {
          "type": "array",
          "description": "应用程序的主要入口点"
        },
        "core_workflows": {
          "type": "array",
          "description": "主要的功能流程"
        },
        "data_flow": {
          "type": "string",
          "description": "数据如何在系统中流转"
        }
      }
    },
    "quality": {
      "type": "object",
      "properties": {
        "strengths": {
          "type": "array",
          "description": "设计良好的方面"
        },
        "concerns": {
          "type": "array",
          "description": "潜在问题或可改进之处"
        },
        "patterns": {
          "type": "array",
          "description": "反复出现的设计模式"
        }
      }
    }
  }
}
```

### 故障排查模式

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "故障排查模式",
  "description": "用于系统性诊断与解决问题的框架",
  "type": "object",
  "properties": {
    "problem": {
      "type": "object",
      "properties": {
        "symptoms": {
          "type": "array",
          "description": "可观察到的现象"
        },
        "context": {
          "type": "string",
          "description": "问题发生的时机与方式"
        },
        "impact": {
          "type": "string",
          "description": "问题的严重程度与影响范围"
        }
      }
    },
    "diagnosis": {
      "type": "object",
      "properties": {
        "potential_causes": {
          "type": "array",
          "description": "可能的根本原因"
        },
        "evidence": {
          "type": "array",
          "description": "支持每种原因的证据"
        },
        "verification_steps": {
          "type": "array",
          "description": "如何确认每一种可能原因"
        }
      }
    },
    "solution": {
      "type": "object",
      "properties": {
        "approach": {
          "type": "string",
          "description": "总体策略"
        },
        "steps": {
          "type": "array",
          "description": "要采取的具体行动"
        },
        "verification": {
          "type": "string",
          "description": "如何确认解决方案奏效"
        },
        "prevention": {
          "type": "string",
          "description": "如何防止问题再次发生"
        }
      }
    }
  }
}
```


### 推理协议

```
/reasoning.systematic{
    intent="Break down complex problems into logical steps with traceable reasoning",
    input={
        problem="<problem_statement>",
        constraints="<constraints>",
        context="<context>"
    },
    process=[
        /understand{action="Restate problem and clarify goals"},
        /analyze{action="Break down into components"},
        /plan{action="Design step-by-step approach"},
        /execute{action="Implement solution methodically"},
        /verify{action="Validate against requirements"},
        /refine{action="Improve based on verification"}
    ],
    output={
        solution="Implemented solution",
        reasoning="Complete reasoning trace",
        verification="Validation evidence"
    }
}
```

```
/thinking.extended{
    intent="Engage deep, thorough reasoning for complex problems requiring careful consideration",
    input={
        problem="<problem_requiring_deep_thought>",
        level="<basic|deep|deeper|ultra>" // Corresponds to think, think hard, think harder, ultrathink
    },
    process=[
        /explore{action="Consider multiple perspectives and approaches"},
        /evaluate{action="Assess trade-offs of each approach"},
        /simulate{action="Test mental models against edge cases"},
        /synthesize{action="Integrate insights into coherent solution"},
        /articulate{action="Express reasoning clearly and thoroughly"}
    ],
    output={
        conclusion="Well-reasoned solution",
        rationale="Complete thinking process",
        alternatives="Other considered approaches"
    }
}
```

### 自我改进协议

```
/self.reflect{
    intent="Continuously improve reasoning and outputs through recursive evaluation",
    input={
        previous_output="<output_to_evaluate>",
        criteria="<evaluation_criteria>"
    },
    process=[
        /assess{
            completeness="Identify missing information",
            correctness="Verify factual accuracy",
            clarity="Evaluate understandability",
            effectiveness="Determine if it meets needs"
        },
        /identify{
            strengths="Note what was done well",
            weaknesses="Recognize limitations",
            assumptions="Surface implicit assumptions"
        },
        /improve{
            strategy="Plan specific improvements",
            implementation="Apply improvements methodically"
        }
    ],
    output={
        evaluation="Assessment of original output",
        improved_output="Enhanced version",
        learning="Insights for future improvement"
    }
}
```

## 2. 工作流协议

### 探索—规划—编码—提交工作流

```
/workflow.explore_plan_code_commit{
    intent="Implement a systematic approach to coding tasks with thorough planning",
    input={
        task="<task_description>",
        codebase="<relevant_files_or_directories>"
    },
    process=[
        /explore{
            action="Read relevant files and understand the codebase",
            instruction="Analyze but don't write code yet"
        },
        /plan{
            action="Create detailed implementation plan",
            instruction="Use extended thinking to evaluate alternatives"
        },
        /implement{
            action="Write code following the plan",
            instruction="Verify correctness at each step"
        },
        /finalize{
            action="Commit changes and create PR if needed",
            instruction="Write clear commit messages"
        }
    ],
    output={
        implementation="Working code solution",
        explanation="Documentation of approach",
        commit="Commit message and PR details"
    }
}
```

### 测试驱动开发工作流

```
/workflow.test_driven{
    intent="Implement changes using test-first methodology",
    input={
        feature="<feature_to_implement>",
        requirements="<detailed_requirements>"
    },
    process=[
        /write_tests{
            action="Create comprehensive tests based on requirements",
            instruction="Don't implement functionality yet"
        },
        /verify_tests_fail{
            action="Run tests to confirm they fail appropriately",
            instruction="Validate test correctness"
        },
        /implement{
            action="Write code to make tests pass",
            instruction="Focus on passing tests, not implementation elegance initially"
        },
        /refactor{
            action="Clean up implementation while maintaining passing tests",
            instruction="Improve code quality without changing behavior"
        },
        /finalize{
            action="Commit both tests and implementation",
            instruction="Include test rationale in commit message"
        }
    ],
    output={
        tests="Comprehensive test suite",
        implementation="Working code that passes tests",
        commit="Commit message and PR details"
    }
}
```

### 迭代式 UI 开发工作流

```
/workflow.ui_iteration{
    intent="Implement UI components with visual feedback loop",
    input={
        design="<design_mockup_or_description>",
        components="<existing_component_references>"
    },
    process=[
        /analyze_design{
            action="Understand design requirements and constraints",
            instruction="Identify reusable patterns and components"
        },
        /implement_initial{
            action="Create first implementation of UI",
            instruction="Focus on structure before styling"
        },
        /screenshot{
            action="Take screenshot of current implementation",
            instruction="Use browser tools or Puppeteer MCP"
        },
        /compare{
            action="Compare implementation with design",
            instruction="Identify differences and needed improvements"
        },
        /refine{
            action="Iteratively improve implementation",
            instruction="Take new screenshots after each significant change"
        },
        /finalize{
            action="Polish and commit final implementation",
            instruction="Include screenshots in documentation"
        }
    ],
    output={
        implementation="Working UI component",
        screenshots="Before/after visual documentation",
        commit="Commit message and PR details"
    }
}
```
## 3. 代码分析与生成工具

### 代码分析协议

```
/code.analyze{
    intent="Deeply understand code structure, patterns and quality",
    input={
        code="<code_to_analyze>",
        focus="<specific_aspects_to_examine>"
    },
    process=[
        /parse{
            structure="Identify main components and organization",
            patterns="Recognize design patterns and conventions",
            flow="Trace execution and data flow paths"
        },
        /evaluate{
            quality="Assess code quality and best practices",
            performance="Identify potential performance issues",
            security="Spot potential security concerns",
            maintainability="Evaluate long-term maintainability"
        },
        /summarize{
            purpose="Describe the code's primary functionality",
            architecture="Outline architectural approach",
            interfaces="Document key interfaces and contracts"
        }
    ],
    output={
        overview="High-level summary of the code",
        details="Component-by-component breakdown",
        recommendations="Suggested improvements"
    }
}
```

### 代码生成协议

```
/code.generate{
    intent="Create high-quality, maintainable code meeting requirements",
    input={
        requirements="<feature_requirements>",
        context="<codebase_context>",
        constraints="<technical_constraints>"
    },
    process=[
        /design{
            architecture="Plan overall structure",
            interfaces="Define clean interfaces",
            patterns="Select appropriate design patterns"
        },
        /implement{
            skeleton="Create foundational structure",
            core="Implement primary functionality",
            edge_cases="Handle exceptions and edge cases",
            tests="Include appropriate tests"
        },
        /review{
            functionality="Verify requirements are met",
            quality="Ensure code meets quality standards",
            style="Adhere to project conventions"
        },
        /document{
            usage="Provide usage examples",
            rationale="Explain key decisions",
            integration="Describe integration points"
        }
    ],
    output={
        code="Complete implementation",
        tests="Accompanying tests",
        documentation="Comprehensive documentation"
    }
}
```

### 重构协议

```
/code.refactor{
    intent="Improve existing code without changing behavior",
    input={
        code="<code_to_refactor>",
        goals="<refactoring_objectives>"
    },
    process=[
        /analyze{
            behavior="Document current behavior precisely",
            tests="Identify or create verification tests",
            issues="Identify code smells and problems"
        },
        /plan{
            approach="Design refactoring strategy",
            steps="Break down into safe, incremental changes",
            verification="Plan verification at each step"
        },
        /execute{
            changes="Implement refactoring incrementally",
            tests="Run tests after each change",
            review="Self-review each modification"
        },
        /validate{
            functionality="Verify preserved behavior",
            improvements="Confirm refactoring goals were met",
            documentation="Update documentation if needed"
        }
    ],
    output={
        refactored_code="Improved implementation",
        verification="Evidence of preserved behavior",
        improvements="Summary of changes and benefits"
    }
}
```

## 4. 测试与验证框架

### 测试套件生成协议

```
/test.generate{
    intent="Create comprehensive test suite for code verification",
    input={
        code="<code_to_test>",
        requirements="<functionality_requirements>"
    },
    process=[
        /analyze{
            functionality="Identify core functionality",
            edge_cases="Determine boundary conditions",
            paths="Map execution paths"
        },
        /design{
            unit_tests="Design focused component tests",
            integration_tests="Design cross-component tests",
            edge_case_tests="Design boundary condition tests",
            performance_tests="Design performance verification"
        },
        /implement{
            framework="Set up testing framework",
            fixtures="Create necessary test fixtures",
            tests="Implement designed tests",
            assertions="Include clear assertions"
        },
        /validate{
            coverage="Verify adequate code coverage",
            independence="Ensure test independence",
            clarity="Confirm test readability"
        }
    ],
    output={
        test_suite="Complete test implementation",
        coverage_analysis="Test coverage assessment",
        run_instructions="How to execute tests"
    }
}
```

### 缺陷诊断协议

```
/bug.diagnose{
    intent="Systematically identify root causes of issues",
    input={
        symptoms="<observed_problem>",
        context="<environment_and_conditions>"
    },
    process=[
        /reproduce{
            steps="Establish reliable reproduction steps",
            environment="Identify environmental factors",
            consistency="Determine reproducibility consistency"
        },
        /isolate{
            scope="Narrow down affected components",
            triggers="Identify specific triggers",
            patterns="Recognize symptom patterns"
        },
        /analyze{
            trace="Follow execution path through code",
            state="Examine relevant state and data",
            interactions="Study component interactions"
        },
        /hypothesize{
            causes="Formulate potential root causes",
            tests="Design tests for each hypothesis",
            verification="Plan verification approach"
        }
    ],
    output={
        diagnosis="Identified root cause",
        evidence="Supporting evidence",
        fix_strategy="Recommended solution approach"
    }
}
```
## 5. Git 与 GitHub 集成

### Git 工作流协议

```
/git.workflow{
    intent="Manage code changes with Git best practices",
    input={
        changes="<code_changes>",
        branch_strategy="<branching_approach>"
    },
    process=[
        /prepare{
            branch="Create or select appropriate branch",
            scope="Define clear scope for changes",
            baseline="Ensure clean starting point"
        },
        /develop{
            changes="Implement required changes",
            commits="Create logical, atomic commits",
            messages="Write clear commit messages"
        },
        /review{
            diff="Review changes thoroughly",
            tests="Ensure tests pass",
            standards="Verify adherence to standards"
        },
        /integrate{
            sync="Sync with target branch",
            conflicts="Resolve any conflicts",
            validate="Verify integration success"
        }
    ],
    output={
        commits="Clean commit history",
        branches="Updated branch state",
        next_steps="Recommended follow-up actions"
    }
}
```

### GitHub PR 协议

```
/github.pr{
    intent="Create and manage effective pull requests",
    input={
        changes="<implemented_changes>",
        context="<purpose_and_background>"
    },
    process=[
        /prepare{
            review="Self-review changes",
            tests="Verify tests pass",
            ci="Check CI pipeline status"
        },
        /create{
            title="Write clear, descriptive title",
            description="Create comprehensive description",
            labels="Add appropriate labels",
            reviewers="Request appropriate reviewers"
        },
        /respond{
            reviews="Address review feedback",
            updates="Make requested changes",
            discussion="Engage in constructive discussion"
        },
        /finalize{
            checks="Ensure all checks pass",
            approval="Confirm necessary approvals",
            merge="Complete merge process"
        }
    ],
    output={
        pr="Complete pull request",
        status="PR status and next steps",
        documentation="Any follow-up documentation"
    }
}
```

### Git 历史分析协议

```
/git.analyze_history{
    intent="Extract insights from repository history",
    input={
        repo="<repository_path>",
        focus="<analysis_objective>"
    },
    process=[
        /collect{
            commits="Gather relevant commit history",
            authors="Identify contributors",
            patterns="Detect contribution patterns"
        },
        /analyze{
            changes="Examine code evolution",
            decisions="Trace architectural decisions",
            trends="Identify development trends"
        },
        /synthesize{
            insights="Extract key insights",
            timeline="Create evolutionary timeline",
            attribution="Map features to contributors"
        }
    ],
    output={
        history_analysis="Comprehensive historical analysis",
        key_insights="Important historical patterns",
        visualization="Temporal representation of evolution"
    }
}
```

## 6. 项目导航与探索

### 代码库探索协议

```
/project.explore{
    intent="Build comprehensive understanding of project structure",
    input={
        repo="<repository_path>",
        focus="<exploration_objectives>"
    },
    process=[
        /scan{
            structure="Map directory hierarchy",
            files="Identify key files",
            patterns="Recognize organizational patterns"
        },
        /analyze{
            architecture="Determine architectural approach",
            components="Identify main components",
            dependencies="Map component relationships"
        },
        /document{
            overview="Create high-level summary",
            components="Document key components",
            patterns="Describe recurring patterns"
        }
    ],
    output={
        map="Structural representation of codebase",
        key_areas="Identified important components",
        entry_points="Recommended starting points"
    }
}
```

### 依赖分析协议

```
/project.analyze_dependencies{
    intent="Understand project dependencies and relationships",
    input={
        project="<project_path>",
        depth="<analysis_depth>"
    },
    process=[
        /scan{
            direct="Identify direct dependencies",
            transitive="Map transitive dependencies",
            versions="Catalog version constraints"
        },
        /analyze{
            usage="Determine how dependencies are used",
            necessity="Evaluate necessity of each dependency",
            alternatives="Identify potential alternatives"
        },
        /evaluate{
            security="Check for security issues",
            maintenance="Assess maintenance status",
            performance="Evaluate performance impact"
        }
    ],
    output={
        dependency_map="Visual representation of dependencies",
        recommendations="Suggested optimizations",
        risks="Identified potential issues"
    }
}
```

## 7. 自我反思与改进机制

### 知识缺口识别协议

```
/self.identify_gaps{
    intent="Recognize and address knowledge limitations",
    input={
        context="<current_task_context>",
        requirements="<knowledge_requirements>"
    },
    process=[
        /assess{
            current="Evaluate current understanding",
            needed="Identify required knowledge",
            gaps="Pinpoint specific knowledge gaps"
        },
        /plan{
            research="Design targeted research approach",
            questions="Formulate specific questions",
            sources="Identify information sources"
        },
        /acquire{
            research="Conduct necessary research",
            integration="Incorporate new knowledge",
            verification="Validate understanding"
        }
    ],
    output={
        gap_analysis="Identified knowledge limitations",
        acquired_knowledge="New information gathered",
        updated_approach="Revised approach with new knowledge"
    }
}
```
### 解决方案质量改进协议

```
/self.improve_solution{
    intent="Iteratively enhance solution quality",
    input={
        current_solution="<existing_solution>",
        quality_criteria="<quality_standards>"
    },
    process=[
        /evaluate{
            strengths="Identify solution strengths",
            weaknesses="Pinpoint improvement areas",
            benchmarks="Compare against standards"
        },
        /plan{
            priorities="Determine improvement priorities",
            approaches="Design enhancement approaches",
            metrics="Define success metrics"
        },
        /enhance{
            implementation="Apply targeted improvements",
            verification="Validate enhancements",
            iteration="Repeat process as needed"
        }
    ],
    output={
        improved_solution="Enhanced implementation",
        improvement_summary="Description of enhancements",
        quality_assessment="Evaluation against criteria"
    }
}
```

## 8. 文档指南

### 代码文档协议

```
/doc.code{
    intent="Create comprehensive, useful code documentation",
    input={
        code="<code_to_document>",
        audience="<target_readers>"
    },
    process=[
        /analyze{
            purpose="Identify code purpose and function",
            interfaces="Determine public interfaces",
            usage="Understand usage patterns"
        },
        /structure{
            overview="Create high-level description",
            api="Document public API",
            examples="Develop usage examples",
            internals="Explain key internal concepts"
        },
        /implement{
            inline="Add appropriate inline comments",
            headers="Create comprehensive headers",
            guides="Develop usage guides",
            references="Include relevant references"
        },
        /validate{
            completeness="Verify documentation coverage",
            clarity="Ensure understandability",
            accuracy="Confirm technical accuracy"
        }
    ],
    output={
        documentation="Complete code documentation",
        examples="Illustrative usage examples",
        quick_reference="Concise reference guide"
    }
}
```

### 技术写作协议

```
/doc.technical{
    intent="Create clear, informative technical documentation",
    input={
        subject="<documentation_topic>",
        audience="<target_readers>",
        purpose="<documentation_goals>"
    },
    process=[
        /plan{
            scope="Define documentation scope",
            structure="Design logical organization",
            level="Determine appropriate detail level"
        },
        /draft{
            overview="Create conceptual overview",
            details="Develop detailed explanations",
            examples="Include illustrative examples",
            references="Add supporting references"
        },
        /refine{
            clarity="Improve explanation clarity",
            flow="Enhance logical progression",
            accessibility="Adjust for audience understanding"
        },
        /finalize{
            review="Conduct thorough review",
            formatting="Apply consistent formatting",
            completeness="Ensure comprehensive coverage"
        }
    ],
    output={
        documentation="Complete technical document",
        summary="Executive summary",
        navigation="Guide to document structure"
    }
}
```

## 9. 项目专有约定

### Bash 命令
- `npm run build`：构建项目
- `npm run test`：运行全部测试
- `npm run test:file <file>`：运行指定文件的测试
- `npm run lint`：运行 linter
- `npm run typecheck`：运行类型检查器

### 代码风格
- 使用一致的缩进（2 个空格）
- 遵循项目特定的命名约定
- 为公开函数添加 JSDoc 注释
- 为新功能编写单元测试
- 遵循单一职责原则
- 使用描述性的变量与函数名

### Git 工作流
- 使用功能分支进行新开发
- 编写描述性的提交信息
- 在提交与 PR 中引用 issue 编号
- 保持提交聚焦且原子化
- 在提交 PR 前将功能分支变基到 main
- 合并到 main 时压缩提交

### 项目结构
- `/src`：源代码
- `/test`：测试文件
- `/docs`：文档
- `/scripts`：构建与实用脚本
- `/types`：类型定义

## 使用说明

1. **定制**：修改各节以匹配项目特定的需求与约定。

2. **扩展**：随着新协议和框架与工作流变得相关，添加它们。

3. **集成**：在提示词中通过名称或结构提及这些协议，让 Claude Code 引用它们。

4. **权限**：考虑将常用命令加入允许列表，以实现更高效的工作流。

5. **工作流适配**：组合并修改协议，为具体任务创建定制工作流。

6. **文档**：让本文件保持最新，记录项目特定信息与约定。

7. **分享**：将本文件提交到仓库，与团队共享这些认知工具。
