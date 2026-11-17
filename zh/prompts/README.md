# zh/prompts — Agent 任务卡索引

每个文件是一张**自包含**任务卡，可直接投喂给无历史上下文的 agent。
任务卡只补充 `zh/PLAN/PLAN.md` 未写死的部分（CLI 契约、JSON schema、映射算法、校验数字）。
两者冲突时以 `PLAN.md` 为准。

| 任务卡 | 模块 | 篇 | 段 | 依赖 | 状态 |
|---|---|---:|---:|---|---|
| `M0_bootstrap.md` | M0 基础设施 | 0 | 0 | 无 | **ready** |
| `M1_entry.md` | M1 入口层 | 23 | 43 | M0 | 待写 |
| `M2_foundations.md` | M2 概念地基 | 7 | 11 | M0 | 待写 |
| `M3_course_core.md` | M3 课程基础 | 27 | 80 | M0 | 待写 |
| `M4_course_adv.md` | M4 课程进阶 | 17 | 35 | M0 | 待写 |
| `M5_course_frontier.md` | M5 课程前沿 | 17 | 52 | M0 | 待写 |
| `M6_assets.md` | M6 工程资产 | 63 | 90 | M0 | 待写 |
| `M7_reference.md` | M7 参考手册 | 13 | 104 | M0 | 待写 |
| `M8_nocode.md` | M8 无代码 | 32 | 204 | M0 + M2 术语冻结 | 待写 |
| `M9_cognitive.md` | M9 认知架构 | 25 | 35 | M0 | 待写 |
| `M10_research.md` | M10 研究篇 | 14 | 51 | M0 | 待写 |
| `M11_write.md` | M11 空目录写作 | 4 | 0 | M0 | 待写 |

## 启动顺序

```
M0 → M1 → M2 → M3 → M4 → M6 → M9 → M5 → M7 → M8 → M10 → M11
      └ P1 ┘  └── P2 ──┘  └─ P3 ─┘  └── P4 ──┘  └ P5 ┘  └── P6 ──┘
```

M8 必须在 M2 之后：NOCODE 与 00_foundations 讲同一套 Atoms→Molecules→Cells→Organs，
M2 译完即冻结术语，M8 复用同一译法，否则两处必然分叉。

## 并行约束

| 同批最多 | 原因 |
|---|---|
| 3 个 agent | 写同一个 `zh/manifest.json` 会冲突 → 任务卡要求各自只读、不改 manifest |
| 1 个 agent 改 `zh/tools/` | 工具是共享依赖，改动期间其他 agent 的校验结果不可信 |

安全并行方式：每批 3 个 agent，模块互不重叠，全部完成后由人跑一次
`python zh/tools/manifest.py && python zh/tools/check.py --all && python zh/tools/progress.py`。

## 单任务卡的固定骨架

写后续任务卡时照抄这 12 节，保证 agent 拿到的是同一套契约：

```
0 你的处境        仓库根 / 分支 / remote / 工作区现状 / Python 版本
1 先读哪几份文件  PLAN.md 章节号 + PROGRESS.md §2 的对应行
2 交付物          本模块的 N 个 zh/ 文件路径
3 关键数字        篇数 / 段数 / 空文件数 / 可译字节
4 文件清单        逐文件一行：源路径 ｜ 段数 ｜ 可译字节 ｜ 备注
5 术语            本模块专属术语，引用 GLOSSARY.yaml 的 key
6 特别处理        本模块特有的坑（见下）
7 质量门禁        本模块需额外通过的 G1–G9 子集
8 不要做的事      禁止越界
9 完成判据        checklist
10 报告格式       表格 + 偏差 + 下一步
11 建议顺序       分步执行顺序
```

## 各模块已知的坑（写任务卡时直接抄进 §6）

| 模块 | 坑 |
|---|---|
| M1 | `README.md` / `CLAUDE.md` / `GEMINI.md` 三份有大量重复段落，先译一份，其余复用 |
| M2 | 术语密度最高，是全库的译法基准；译完须回头核对 GLOSSARY.yaml 并增补 |
| M3 | 6 个模块 README 是 1 字节空文件，属 `status: authored`，要写不译 |
| M4 | `05_memory_systems/README.md` 有 9,862B 实体内容，是唯一非空的模块 README |
| M5 | `09_evaluation_methodologies/01_component_assessment.md` 127KB，单篇 23 段，是全库最大单文件 |
| M6 | `30_examples/00_toy_chatbot/` 下 5 个文件是 `.md` 形式的代码（`*.py.md`），按代码块处理不译正文 |
| M7 | ASCII 图最密集（585KB），`symbolic_residue_types.md` 1218 行框线、`attractor_dynamics.md` 838 行，必须走「图内不动、图注另译」 |
| M8 | 与 M2 内容重叠；`00_foundations/10_cross_model.md` 156KB / 1061 行框线 |
| M9 | 25 篇中 4 个是空目录 README；`quantum-architecture.md` 184KB |
| M10 | `SECURITY_RESEARCH/SYSTEM_PROMPTS/claude_code_system_prompt.md` 148KB 是他人系统提示词原文，只译导言不译正文 |
| M11 | 4 个空目录（`50_contrib` `70_agents` `80_field_integration` `context-schemas`）没有任何源内容，是写作任务，须先与人工确认范围 |
