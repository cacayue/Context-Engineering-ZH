---
title: zh/ 中文化计划（唯一执行文档）
status: active
version: v3.0
created: 2026-11-17
base_commit: 6158def
supersedes: [PLAN_v0.md, PLAN_v2.md, BUILD.md]
rule: 奥卡姆剃刀 —— 能少则少，一个事实只存一处
---

# zh/ 中文化计划

> 本文件是唯一执行文档。此前三份（`PLAN_v0.md`、`PLAN_v2.md`、`BUILD.md`）已合并于此并删除。

## 0. 目标与范围

### 0.1 目标

**完整学习本书。全部正文都要有中文翻译；研究性内容可以排后，但同样要翻译。翻译由 AI 执行。**

### 0.2 什么算"正文"

仓库 8.92 MB 中 **63.0% 是代码块与 ASCII 图**，需翻译的部分只占 **37.0%**。若把全部字节当"正文"，工作量高估 1.7 倍，且代码会被译坏。

| 内容类型 | 实测体量 | 占比 | 块数 | 处理 |
|---|---:|---:|---:|---|
| 散文（段落、列表、引用、标题、表格） | **1.86 MB** | 20.9% | — | **全译** |
| 无标记纯文本块（提示词、示例、对话） | **1.44 MB** | 16.1% | 1377 | **全译** |
| 含框线 ASCII 图（无标记块） | **1.79 MB** | 20.1% | 915 | **不译**，图下加中文图注 |
| 围栏代码块（全部语言） | **3.83 MB** | 42.9% | 1303 | 不译；仅译注释中的自然语言 |
| **合计** | **8.92 MB** | 100% | 3595 | 需译 3.30 MB |

代码块内部：`python` 3.13 MB / 870 块（最大宗）、`yaml` 0.23 MB、`json` 0.20 MB、
`xml` 0.13 MB、`markdown`+`md` 0.21 MB、`javascript` 0.06 MB、其余零散。

`md`/`markdown` 标记的块多是嵌套的示例文档，按内容判定：含中文说明的译，
纯代码或纯配置的留原文。

`{{...}}` 占位符全仓 60+ 处（`{{task_description}}` 20、`{{reasoning_template}}` 10、
`{{output_specifications}}` 10、`{{additional_questions_as_needed}}` 10、`{{problem}}` 9 等），
一律**原样保留**，由 G4 检查。

**需翻译总量 = 1.86 + 1.44 = 3.30 MB ≈ 36.1 万英文词 ≈ 57.7 万字中文**

### 0.3 30 个空文件是"写作"不是"翻译"

实测 30 个 `.md` 只有 1 字节（仅换行），无原文可译：`00_COURSE` 各模块 README（10 个）、`exercises/` 与 `labs/` 各 1、`50_contrib/`、`60_protocols/schemas/`、`60_protocols/shells/`、`70_agents/`、`80_field_integration/`、`context-schemas/`、`cognitive-tools/` 及 4 个子目录、`NOCODE/` 6 个、`SECURITY_RESEARCH/SYSTEM_PROMPTS/`、`.github/workflows/README.md`。

标记 `status: authored`，由 AI 依同目录正文撰写中文导读，**不计入翻译覆盖率**。

---

## 1. 实测基线（base_commit 6158def）

| 项目 | 数值 |
|---|---|
| `.md` 文件 | 242（不含 `zh/`） |
| `.md` 总字节 | 8.92 MB，其中代码块与 ASCII 图 5.62 MB（2218 块，63.0%） |
| 散文 | 1.86 MB（20.9%） |
| 可译文本块 | 1.44 MB（1377 块） |
| ASCII 图块 | 1.79 MB（915 块） |
| `.py` | 31 个 / 1.48 MB（仅译注释） |
| `.json` + `.yaml` | 17 个 / 414 KB（仅译 description/title） |
| `.mp4` | 3 个 / 36 MB（PODCASTS，只做摘要） |
| 占位空文件 | 30 个 |
| 翻译段数 | **676**（每文件 max(1, ⌈可译字节/6144⌉) 累加） |

### 代码块语言分布

```
(无标记·纯文本)  1377 块 / 1.44 MB   → 译
(无标记·含框线)   915 块 / 1.79 MB   → 不译，加图注
python            870 块 / 2.99 MB
yaml              112 块 / 0.22 MB
json               99 块 / 0.19 MB
markdown           60 块 / 0.10 MB
md                 68 块 / 0.10 MB
javascript         23 块 / 0.06 MB
xml                22 块 / 0.13 MB
ascii             22 块 / 0.02 MB
bash                8 块 / 0.00 MB
math                8 块 / 0.00 MB
mermaid             5 块 / 0.01 MB
bibtex              4 块 / 0.00 MB
text                2 块 / 0.00 MB

> 围栏块总数 3595。解析器必须支持：`~~~` 围栏、4 个及以上反引号、`>`/列表内缩进围栏、
> 未闭合围栏（按到文末处理）。有 7 个文件含未闭合围栏。
```

### 上游既有缺陷（必须在本版修复，不原样搬运）

内部相对链接 **197 个，36 个失效**，涉及 16 个文件：

```
40_reference/README.md          → ./boundary_operations.md ./quantum_semantic_metrics.md ./unified_field_operations.md
20_templates/README.md          → ./resonance_measurement.py（实为 field_resonance_measure.py）./attractor_detection.py ./symbolic_residue_tracker.py
60_protocols/README.md          → ../../00_foundations/08_neural_fields_foundations.md（层级应为 ../）等 3 条
60_protocols/digests/README.md  → ./recursive.emergence.digest.md ./recursive.memory.digest.md ./field.resonance.digest.md
60_protocols/digests/attractor.co.emerge.digest.md → ../shells/attractor.co.emerge.shell 等 3 条
cognitive-tools/README.md       → ../../.github/CONTRIBUTING.md
cognitive-tools/cognitive-templates/composition.md → ../integration/with-rag.md ../integration/with-memory.md
cognitive-tools/cognitive-programs/basic-programs.md → ./program-examples.ipynb
00_COURSE/05_memory_systems/README.md → 03_reconstructive_memory.md（实为 04_）
00_COURSE/07_multi_agent_systems/03_emergent_behaviors.md → ../08_field_integration/（实为 08_field_theory_integration/）
00_foundations/05_cognitive_tools.md → [parameters]（伪链接）
```

另有 **20+ 个 `.ipynb` 被引用但只有 `.py`**：`01_min_prompt` `02_expand_context` `03_control_loops` `04_rag_recipes` `05_prompt_programs` `05_protocol_bootstrap` `06_protocol_token_budget` `06_schema_design` `07_recursive_patterns` `07_streaming_context` `08_emergence_detection` `08_neural_fields` `09_residue_tracking` `10_attractor_formation` `11_quantum_context_operations` `12_meta_recursive_loops` `13_interpretability_tools` `14_multimodal_context`。

`STRUCTURE/TREE.md` 中列出的 `.ipynb` 全部不存在。

### 上游 CI 不可复用

```
.github/workflows/ci.yml    paths-ignore: ['**.md','docs/**']
.github/workflows/eval.yml  同上，且与 ci.yml 逐字节相同
.github/workflows/protocol_tests.yml 监听 tests/ 90_meta_recursive/ —— 两目录均不存在
```

→ 纯 Markdown 变更零校验。必须新增 `zh_checks.yml`。

### 代码可运行性现状

```
无 requirements.txt / pyproject.toml / setup.py / environment.yml
10_guides_zero_to_hero/ 7 个 .py，6 个真实 import openai
20_templates/control_loop.py 同时 import openai 与 anthropic
30_examples/00_toy_chatbot/ 5 个文件全是 .md 形式（chatbot_core.py.md 等）
```

`10_guides_zero_to_hero/01_min_prompt.py` 自带 `SimpleLLM` 假实现，可离线跑。

---

## 2. 架构：奥卡姆剃刀

| 编号 | 约束 | 含义 |
|---|---|---|
| O1 | **一处真相** | 进度只存在译文 front matter，不另建台账 |
| O2 | **文件即单元** | 一个源文件 → 一个 zh 文件，不拆不合 |
| O3 | **生成而非手写** | 统计、清单、进度表全由脚本生成 |

### 只需 5 类文件

| 类 | 路径 | 数量 | 谁写 |
|---|---|---:|---|
| 计划 | `zh/PLAN/PLAN.md` | 1 | 人 |
| 规范 | `zh/GLOSSARY.yaml` `zh/STYLE.md` `zh/NOTICE` | 3 | 人 |
| 正文 | `zh/<原路径>` | 242 | AI |
| 生成 | `zh/manifest.json` `zh/PROGRESS.md` `zh/KNOWN_ISSUES.md` | 3 | 脚本 |
| 工具 | `zh/tools/*.py` `.github/workflows/zh_checks.yml` | 6 | 人 |

### 剃刀砍掉的

| 砍掉 | 理由 |
|---|---|
| `ROADMAP.md` / `TODO.md` | 与 `PROGRESS.md` 重复 |
| `SYNC.md` | 上游基线写在 `manifest.json` 的 `base_commit` |
| `DECISIONS.md` | 术语决策写进 `GLOSSARY.yaml` 的 `note` 字段 |
| 每文件 `.meta.json` | front matter 已够用 |
| 索引页 / 目录导航 | `PROGRESS.md` 即导航 |
| 双语对照文件 | 译文开头放原文相对链接即可 |
| 拆 chunk 文件 | 单文件内嵌注释，242 文件而非 676 |

---

## 3. 模块划分（12 模块）

模块 = 可独立交付、可独立验收的最小集合。

| 模块 | 名称 | 源目录 | 篇 | 段 | 万字 | 空 | ASCII KB | 依赖 |
|---|---|---|---:|---:|---:|---:|---:|---|
| **M0** | 基础设施 | `zh/tools/` `GLOSSARY.yaml` `STYLE.md` `NOTICE` `zh_checks.yml` | 6 | 0 | 0 | — | — | — |
| **M1** | 入口层 | 根文档 + `STRUCTURE/` + `masterclass_content/` | 23 | 40 | 3.0 | 0 | 106 | M0 |
| **M2** | 概念地基 | `00_foundations/01–07` + `README` | 7 | 11 | 0.9 | 0 | 165 | M1 |
| **M3** | 课程·基础 | `00_COURSE/00–03` | 27 | 79 | 6.9 | 6 | 87 | M2 |
| **M4** | 课程·进阶 | `00_COURSE/04–06` | 17 | 35 | 2.6 | 2 | 42 | M3 |
| **M5** | 课程·前沿 | `00_COURSE/07–10` | 17 | 52 | 4.8 | 4 | 47 | M4 |
| **M6** | 工程资产 | `20_templates` `60_protocols` `.claude` `10_guides` `30_examples` | 63 | 89 | 5.5 | 2 | 77 | M2 |
| **M7** | 参考手册 | `40_reference/` | 13 | **104** | 10.9 | 0 | 587 | M2 |
| **M8** | 无代码 | `NOCODE/` | 32 | **204** | 18.0 | 6 | 405 | M2 |
| **M9** | 认知架构 | `cognitive-tools/` | 25 | 33 | 2.5 | 4 | 276 | M6 |
| **M10** | 研究篇 | `00_foundations/08–14` `00_EVIDENCE` `SECURITY_RESEARCH` `PODCASTS` `.github` | 14 | 29 | 2.6 | 2 | 45 | M2 |
| **M11** | 空目录写作 | `50_contrib` `70_agents` `80_field_integration` `context-schemas` | 4 | 0 | 0 | 4 | 0 | M1 |
| | **合计**（源 .md 242 + M0 工具 6） | | **242** | **676** | **57.7** | **30** | **1841** | |

> **段 = max(1, ⌈可译字节 ÷ 6144⌉)，按文件累加 = 676。**
> 不能用「总体积 ÷ 6144」= 563 或「按模块聚合」= 567，因为每个文件至少一次调用；
> 676 才是真实的 AI 调用次数，也是进度单位。
> 段数分布：0 段 30 篇、1 段 80 篇、2 段 43、3 段 24、4 段 25、5 段 7、6 段 3、7 段 4、
> 8 段 6、9 段 11、10 段 3、11 段 1、12 段 1、14 段 3、15 段 1。
> M11 的 4 篇 + 其余模块内 26 篇空 README = 30 篇 `authored`，不计入覆盖率。

---

## 4. 任务项总表

任务 = 一次可交付、可验收的动作。

### M0 基础设施

| ID | 任务 | 产出 | 验收 |
|---|---|---|---|
| M0-01 | 术语表 | `zh/GLOSSARY.yaml` + `zh/GLOSSARY.md` + `zh/tools/glossary_md.py` | 84 词；7 个歧义词有 `ambiguity`；MD 由 YAML 生成 |
| M0-02 | 文风规范 | `zh/STYLE.md`（含 R1–R7） | 与第 5 节一致 |
| M0-03 | 许可署名与导航 | `zh/NOTICE` + `zh/LEARNING_PATH.md` | NOTICE 含 `davidkimai` 与 MIT；LEARNING_PATH 收拢三套矛盾的阅读顺序 |
| M0-04 | 扫描与清单 | `zh/tools/manifest.py` → `manifest.json` | 242 条，sha 全记录 |
| M0-05 | 切分与装配 | `zh/tools/plan_chunks.py` `assemble.py` | 单文件往返无损；锚点按深度自动生成 |
| M0-06 | 九项检查 | `zh/tools/check.py`（G1–G9 合一） | 自测 9/9；G8 实际解析锚点路径 |
| M0-07 | 进度生成 | `zh/tools/progress.py` → `PROGRESS.md` | 与 manifest 一致；M0 状态按交付物存在判定 |
| M0-08 | 上游缺陷清单 | `zh/KNOWN_ISSUES.md` | 36 条失效链接，G5 白名单来源 |
| M0-09 | CI | `.github/workflows/zh_checks.yml` | `paths: ['zh/**']`，无 `paths-ignore`，4 个 job |

### M1 入口层（40 段）

| ID | 任务 | 覆盖 |
|---|---|---|
| M1-01 | 根文档 | `README.md` `Complete_Guide.md` `CITATIONS.md` `CITATIONS_v2.md` `CITATIONS_v3.md` |
| M1-02 | 仓库手册 | `CLAUDE.md` `GEMINI.md` |
| M1-03 | 结构说明 | `STRUCTURE/README.md` `STRUCTURE.md` `TREE.md` `STRUCTURE_v2.md` `STRUCTURE_v3.md` |
| M1-04 | 大师课 8 篇 | `masterclass_content/01–08`（仅 29 KB，全仓最省力入口） |
| M1-05 | 导航页 | `00_foundations/README.md` `00_COURSE/README.md` `30_examples/README.md` |

### M2 概念地基（11 段）

| ID | 任务 | 文件 |
|---|---|---|
| M2-01 | 原子与分子 | `01_atoms_prompting.md`(11.8K) `02_molecules_context.md`(20.0K) |
| M2-02 | 细胞与器官 | `03_cells_memory.md`(41.4K) `04_organs_applications.md`(73.3K) |
| M2-03 | 工具与编程 | `05_cognitive_tools.md`(30.0K) `06_advanced_applications.md`(59.4K) `07_prompt_programming.md`(49.6K) |

### M3 课程·基础（79 段）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M3-01 | 数学基础 | `00_mathematical_foundations/` 7 篇 + `exercises/math_foundations_lab.py` 注释 | 2 |
| M3-02 | 检索与生成 | `01_context_retrieval_generation/` 8 篇 + `labs/` 4 个 .py + `case_studies/` `templates/` | 2 |
| M3-03 | 上下文处理 | `02_context_processing/` 6 篇 + `labs/` `implementations/` `benchmarks/` | 1 |
| M3-04 | 上下文管理 | `03_context_management/` 6 篇 + `labs/memory_management_lab.py` | 1 |

### M4 课程·进阶（35 段）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M4-01 | RAG | `04_retrieval_augmented_generation/` 6 篇 | 1 |
| M4-02 | 记忆系统 | `05_memory_systems/` 6 篇（唯一有实体 README 的模块） | 0 |
| M4-03 | 工具推理 | `06_tool_integrated_reasoning/` 5 篇 | 1 |

### M5 课程·前沿（52 段）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M5-01 | 多智能体 | `07_multi_agent_systems/` 5 篇 | 1 |
| M5-02 | 场论集成 | `08_field_theory_integration/` 5 篇（277 KB） | 1 |
| M5-03 | 评估方法 | `09_evaluation_methodologies/` 5 篇（375 KB，最重模块） | 1 |
| M5-04 | 编排毕业设计 | `10_orchestration_capstone/` 2 篇 | 1 |

### M6 工程资产（89 段）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M6-01 | 模板库 | `20_templates/` 27 篇（含 `PROMPTS/` 26 个 `.agent.md`） | 0 |
| M6-02 | 协议壳 | `60_protocols/` 12 篇（`shells/` `digests/` `schemas/`） | 2 |
| M6-03 | 零到一指南 | `10_guides_zero_to_hero/` README + 7 个 .py 注释 | 0 |
| M6-04 | 示例工程 | `30_examples/` 7 篇（`00_toy_chatbot/` 5 个 `.py.md`） | 0 |
| M6-05 | 命令集 | `.claude/commands/` 17 篇 | 0 |

### M7 参考手册（104 段 · 最大密度）

| ID | 任务 | 文件 |
|---|---|---|
| M7-01 | 检索与索引 | `retrieval_indexing.md`(185K) `latent_mapping.md` `advanced_latent_mapping.md`(143K) |
| M7-02 | 残差与涌现 | `symbolic_residue_types.md`(122K, 1218 行图) `emergence_signatures.md`(121K, 760 行图) |
| M7-03 | 吸引子与场 | `attractor_dynamics.md`(123K, 838 行图) `field_mapping.md` |
| M7-04 | 模式与预算 | `patterns.md`(84K) `cognitive_patterns.md`(77K) `token_budgeting.md`(56K) `eval_checklist.md`(68K) |
| M7-05 | Schema 与索引 | `schema_cookbook.md`(77K) `README.md`(20K) |

### M8 无代码（204 段 · 最大工作量）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M8-01 | 基础篇 | `NOCODE/00_foundations/` 10 篇（582 KB） | 0 |
| M8-02 | 心智模型 | `NOCODE/10_mental_models/` 6 篇（含 `05_alchemy_model.md` 123K） | 1 |
| M8-03 | 实用协议 | `NOCODE/20_practical_protocols/` 10 篇（458 KB） | 1 |
| M8-04 | 场域技法 | `NOCODE/30_field_techniques/` + `40_protocol_design/` | 2 |
| M8-05 | 高级集成 | `NOCODE/50_advanced_integration/` + `resources/` + `README.md` | 2 |

> **一致性约束**：M8-01 与 M2 概念重叠（Atoms→Molecules→Cells→Organs）。**以 M2 为权威译法**，M8-01 复用术语、只译差异段落，文首注明「概念译法见 00_foundations」。

### M9 认知架构（33 段）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M9-01 | 架构总览 | `README.md` + `cognitive-architectures/` 9 篇（859 KB） | 1 |
| M9-02 | 模式与模板 | `cognitive-schemas/` 7 篇 + `cognitive-templates/` 5 篇 | 2 |
| M9-03 | 程序库 | `cognitive-programs/` 3 篇 | 1 |

### M10 研究篇（29 段）

| ID | 任务 | 文件 | 空 |
|---|---|---|---:|
| M10-01 | 场论与符号 | `00_foundations/08_neural_fields_foundations.md` `09_persistence_and_resonance.md` `11_emergence_and_attractor_dynamics.md` `12_symbolic_mechanisms.md` | 0 |
| M10-02 | 统一场论与语义 | `00_foundations/10_field_orchestration.md` `13_quantum_semantics.md` `14_unified_field_theory.md` | 0 |
| M10-03 | 证据与安全 | `00_EVIDENCE/README.md` + `SECURITY_RESEARCH/` 3 篇（`claude_code_system_prompt.md` 149K） | 1 |
| M10-04 | 播客与 CI | `PODCASTS/README.md` + `Deep Dive Transcript.txt` 摘要 + `.github/` 2 篇 | 1 |

### M11 空目录写作（4 篇 · authored，0 段）

单任务 `M11-01` 覆盖 4 个空目录。均为 1 字节文件，无原文可译，须依同目录/同级正文原创中文导读。

| ID | 任务 | 目标 | 依据 |
|---|---|---|---|
| M11-01 | 空目录写作 | 4 个 README | 见下表 |

| 目标 | 依据 |
|---|---|
| `zh/50_contrib/README.md` | `.github/CONTRIBUTING.md` |
| `zh/70_agents/README.md` | `20_templates/PROMPTS/` 26 个 `.agent.md` |
| `zh/80_field_integration/README.md` | `00_COURSE/08_field_theory_integration/` |
| `zh/context-schemas/README.md` | `context-schemas/context_v*.json` |

> 任务总数校验：M1–M11 共 **42** 个任务（M1 5 + M2 3 + M3 4 + M4 3 + M5 4 + M6 5 + M7 5 + M8 5 + M9 3 + M10 4 + M11 1）。
> 加 M0 的 9 个基础设施任务 = 51，与 `zh/PROGRESS.md` 的「任务 0 / 42」口径区分：**进度只统计 M1–M11**。

---

## 5. 单文档构建流程

唯一日常动作，与模块无关。

| 步 | 动作 | 产出 | 判定 |
|---:|---|---|---|
| 1 | 登记 | manifest 条目（脚本自动） | `sha` 已记录 |
| 2 | 切分 | 按 H2/H3 切成 N 段，每段 ≤6 KB | N = ⌈可译字节/6144⌉ |
| 3 | 首段 | front matter + 双语锚点 + 术语子集 | `check_frontmatter` 通过 |
| 4 | 逐段译 | 散文全译、文本块全译、代码块原样、ASCII 图原样 | 段级 sha 写入注释 |
| 5 | 装配 | 合并为单文件，插 chunk 注释 | 段数与 N 一致 |
| 6 | 自检 | `python zh/tools/check.py <文件>` | G1–G9 全绿 |
| 7 | 定稿 | `status: draft` → `published` | manifest 重算覆盖率 |

### 切分规则

```
1. 以 H2（## ）为一级切分；单 H2 超 8 KB 时按 H3 再切
2. 单块目标 4–8 KB 源文本（约 1,500–3,000 中文输出 token）
3. 代码块、ASCII 图、表格不可切断——宁可超限
4. 每块携带：文件路径 + H2 标题 + 上块摘要（≤100 字）+ 术语子集
5. 全文首块额外携带：front matter、术语表全量、文风示例
```

### 翻译单元输入模板

```text
[文件] 00_foundations/02_molecules_context.md
[段] 2/3   原文行 120-310   sha 4b1c
[术语] context=上下文  few-shot=少样本  molecule=分子
[上段摘要] 本节说明分子级上下文由示例构成…
[规则] 代码块原样；含框线图原样+图注；{{...}} 原样；中英之间加空格
[任务] 只输出该段的中文 Markdown，不加解释
```

### 七条不可协商规则

| # | 规则 | 违背后果 |
|---|---|---|
| R1 | `{{...}}` 原样，不译不改大小写 | 模板失效 |
| R2 | ```python```/```yaml```/```json```/```xml``` 原样 | 示例不可运行 |
| R3 | 含框线（`─│┌`）的无标记块原样 + 图注 | 915 块图错位 |
| R4 | 标题层级数量与原文一致 | 无法判断是否漏译 |
| R5 | 中文与拉丁字母/数字间加空格 | 排版不统一 |
| R6 | 首次出现用「中文（English）」 | 术语无法追溯 |
| R7 | 内部链接改为 zh 内可达路径 | 在 36 处既有失效外再新增 |

### 文件契约

```yaml
---
title: 原子：提示的基本单位
source: 00_foundations/01_atoms_prompting.md   # 仓库根相对路径；空文件写 null
source_sha256: 3f9a1c...                        # 脚本写入
source_commit: 6158def                          # 脚本写入
module: M2
chunks: 2                                       # 脚本写入
chunks_done: [1, 2]                             # AI 写入，每完成一段追加
status: published                               # todo|draft|review|published|authored|sync-needed
translator: ai
reviewer: null
version: v0.1
---
```

双语锚点（每个 L1/L2 文件开头）：

```markdown
> 原文：[00_foundations/01_atoms_prompting.md](../../00_foundations/01_atoms_prompting.md)
> 术语对照：[GLOSSARY.md](../../GLOSSARY.md) ｜ 阅读路径：[LEARNING_PATH.md](../../LEARNING_PATH.md)
```

段级锚点（长文件）：

```markdown
<a id="chunk-2"></a>
<!-- chunk 2/3 | source_lines 120-310 | sha 4b1c... -->
```

---

## 6. 术语体系

### 机器可读：`zh/GLOSSARY.yaml`

CI 与 AI 都读它，`zh/GLOSSARY.md` 由它生成（人读版）。首批 **60–100 词**。

```yaml
- en: Context Engineering
  zh: 上下文工程
  first_use: 上下文工程（Context Engineering）
  scope: doc
- en: context
  zh: 上下文
  forbid: [语境, 情景, 脉络]
  scope: doc
- en: field
  zh: 场
  ambiguity:
    - mean: 神经场 / 场论
      zh: 场
    - mean: 数据字段（YAML/JSON key）
      zh: field
  note: M2 与 M10 统一用「场」；配置文件内保留 field
  scope: doc
```

### 必须覆盖的一词多义

| 词 | 歧义 | 规则 |
|---|---|---|
| `field` | 神经场 vs 数据字段 | 场 / `field` 保留 |
| `memory` | 记忆系统 vs 程序变量 | 记忆 / `memory` 保留 |
| `agent` | 智能体 vs `.agent.md` 提示词文件 | 智能体 / 保留文件名 |
| `shell` | 协议壳 vs bash shell | 协议壳 / `shell` 保留 |
| `protocol` | 协议壳规范 vs 通信协议 | 协议（按上下文） |
| `residue` | 符号残差 vs 代码残留 | 残差 / 残留 |
| `pattern` | 设计模式 vs 正则模式 | 模式 |

### 禁用译法（CI 强制）

```
语境 / 情景 / 脉络 → 上下文
提示工程           → 提示词工程
令牌               → token
注意力吸引点       → 吸引子
```

### ASCII 图三档规则

| 档 | 适用范围 | 做法 |
|---|---|---|
| A（默认） | 全部含框线图 | **原图不动**，图下加中文图注 |
| B（M1/M2 概念图） | 信息密度低 | 改写为 Mermaid（中文标签），原图入 `<details>` |
| C | 纯表格型框图 | 转 Markdown 表格（中文表头），原图入 `<details>` |

B/C 档必须保留原图。图注格式：

```markdown
> 图：原子提示的组成 —— 任务 + 约束 + 输出格式（TASK + CONSTRAINTS + OUTPUT FORMAT）
```

### 占位符保全

```
{{task_description}}               20 次
{{reasoning_template}}             10 次
{{output_specifications}}          10 次
{{additional_questions_as_needed}} 10 次
{{problem}}                         9 次
{{verification_template}}           6 次
{{topic}} / {{concept_2}}           各 6 次
```

---

## 7. 质量门禁（9 项）

| ID | 检查 | 通过条件 |
|---|---|---|
| G1 | 术语一致性 | `GLOSSARY.yaml` 规范译法出现；禁用词零命中 |
| G2 | ASCII 图完整性 | 无标记块内无全角字符（`[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]`） |
| G3 | 代码围栏 | ``` 配对；语言标记与原文一致 |
| G4 | 占位符保全 | `{{...}}` 多重集 == 原文 |
| G5 | 内部链接 | 目标存在；36 处已知失效走白名单并注明已修 |
| G6 | front matter | schema 校验；`source_sha256` 与原文一致 |
| G7 | 英文残留 | 代码块外 >30% 行英文 → 标 `draft` 不标 `published` |
| G8 | 双语锚点 | 每个 L1/L2 文件含原文链接与术语表链接 |
| G9 | 结构对齐 | H2 数量与原文一致（允许新增「小结」，不允许丢标题） |

> G9 专治「译了前半篇就标完成」——AI 批量翻译最典型的失败模式。
> G7 专治「中英夹杂」。

### CI

```yaml
# .github/workflows/zh_checks.yml
on:
  push:         { paths: ['zh/**'] }
  pull_request: { paths: ['zh/**'] }
# 不得使用 paths-ignore: '**.md'
```

---

## 8. 工具链

```
zh/tools/
├── manifest.py          扫描原文 + 译文 → zh/manifest.json（路径/大小/sha256/status/chunks）
├── plan_chunks.py       按 H2/H3 切分，输出 chunk 计划
├── assemble.py          合并 chunk 输出，补 front matter 与锚点
├── check.py             G1–G9 单一入口，--only Gx / --module Mx
├── progress.py          从 manifest 生成 zh/PROGRESS.md
├── mock_llm.py          OpenAI 兼容的本地假实现（复用 SimpleLLM 思路）
└── verify_examples.py   用 mock 跑 10_guides 的 7 个脚本
```

合并 9 个检查脚本为 1 个：一个命令一次跑完，CI 配置更短。

B3 前必须补齐：

```
1. requirements.txt（固定版本）
2. mock_llm.py（零成本验证）
3. 30_examples 明确为「阅读型示例」，不承诺可运行
```

---

## 9. 进度跟踪

### 进度表不在本文件

进度是高频变更数据，计划是低频稳定文档。二者混在一起会导致：

```
每次改进度 → 计划文件 diff 变大 → 看不出计划本身变了什么
每次改计划 → 进度表被顺带覆盖 → 进度丢失
```

因此 **进度表独立成文件：`zh/PROGRESS.md`**。

| 文件 | 性质 | 更新频率 | 谁写 |
|---|---|---|---|
| `zh/PLAN/PLAN.md`（本文件） | 计划：目标、模块、任务定义、规则、门禁 | 月度 | 人 |
| `zh/PROGRESS.md` | 进度：模块/任务/段 的实时状态 | **每次会话** | 脚本 |

### 唯一真相

front matter 的 `chunks_done` + `status`。不另建台账。

```yaml
module: M2
task: M2-01
chunks: 2
chunks_done: [1, 2]
status: published
```

### 状态机

```text
todo ──▶ draft ──▶ review ──▶ published
  ▲                       │
  └──── sync-needed ◀─────┘   (上游 sha 变化)
authored：无原文，todo ──▶ published
```

| 状态 | 含义 | 计入 coverage |
|---|---|---|
| `todo` | 未开始 | 否 |
| `draft` | 段已译完，未自检 | 是 |
| `review` | 自检通过，待二次校对 | 是 |
| `published` | 校对完成 | 是 |
| `authored` | 无原文，AI 原创 | 否 |
| `sync-needed` | 上游变了，原译文保留 | 否 |

### 指标公式

| 指标 | 计算 | 目标 |
|---|---|---|
| `segs_done` | Σ `len(chunks_done)` | **676** |
| `files_published` | Σ `status == published` | 212 |
| `files_authored` | Σ `status == authored` | 30 |
| `coverage` | `segs_done / 676` | 100% |

### 四级寻址：进度表 → 任务 → 文件 → 段

```text
zh/PROGRESS.md §0  「下一步：M1-04」
      ↓
zh/manifest.json   取 M1-04 内第一个 status == todo 的文件
      ↓
该文件 front matter 若 chunks_done 非空 → 从 max+1 续跑
```

任一级都能中断与恢复。

### 断点续跑

chunk 级 sha 校验，只重译 `sha(current) != sha_recorded` 的段。上游未变则不重译。

---

## 10. 执行顺序

```text
M0 ──┬─▶ M1 ──▶ M2 ──┬─▶ M3 ──▶ M4 ──▶ M5
     │                ├─▶ M6 ──▶ M9
     │                ├─▶ M7
     │                ├─▶ M8
     │                └─▶ M10
     └─▶ M11
```

| 阶段 | 模块 | 段 | 累计 | 理由 |
|---|---|---:|---:|---|
| P0 | M0 | 0 | 0 | 必须先绿，否则 57.7 万字无法验收 |
| P1 | M1 + M2 | 40 + 11 = 51 | 51 | 最小可学闭环 |
| P2 | M3 + M4 | 79 + 35 = 114 | 165 | 课程主体 00–06 |
| P3 | M6 + M9 | 89 + 33 = 122 | 287 | 模板/协议前移，可立即上手 |
| P4 | M5 + M7 | 52 + 104 = 156 | 443 | 前沿 + 参考 |
| P5 | **M8** | 204 | 647 | 独占一阶段，可整体外包 |
| P6 | M10 + M11 | 29 + 0 = 29 | 676 | 研究篇与空目录收尾 |

先「能学」→ 再「能练」→ 后「能查」与「能研」。M8 虽大但不阻塞主线。

---

## 11. 方案分析

### 11.1 段数分布

| 区间 | 模块 | 段 | 占比 |
|---|---|---:|---:|
| 大块 >90 | M8 204、M7 104 | 308 | **46%** |
| 中块 30–90 | M6 89、M3 79、M5 52、M1 40、M4 35、M9 33 | 328 | 49% |
| 小块 <30 | M10 29、M2 11、M11 0 | 40 | 6% |

**一半工作量集中在 M8 + M7。** 二者应单独排期，不与主线混跑。

### 11.2 为什么按模块不按目录

| 按目录（11 个顶层） | 按模块（12 个） |
|---|---|
| `00_COURSE` 一桶 20.2 万字，无法分批验收 | 拆 M3/M4/M5，最大 9.8 万字 |
| `00_foundations` 混装地基（1.2 万）与研究篇（4 篇难文） | M2/M10 分离，难度不混 |
| `20_templates`+`60_protocols`+`.claude` 分散 3 处 | 合 M6，一次交付 |
| 空文件散落，统计失真 | 集中 M11，单标 `authored` |

### 11.3 三个结构性风险

| 风险 | 数据 | 对策 |
|---|---|---|
| ASCII 图错位 | 915 块 / 1.79 MB，占代码块 21%；M7 独占 587 KB | R3 硬规则 + G2 拦全角字符 |
| 术语分叉 | M2 与 M8-01 讲同一套 Atoms→Organs；M6 的 `PROMPTS/` 与 `CLAUDE.md` 概念重叠 | 定 M2 为权威；M8 只译差异 + 交叉引用 |
| 空文件虚高 | 30 篇 1 字节文件会虚增 12% 覆盖率 | `authored` 单列，不计入 coverage |

### 11.4 剃刀取舍账

| 决策 | 放弃 | 换来 |
|---|---|---|
| front matter 即状态 | 不能一次 grep 全局统计 | 台账永不与正文脱节 |
| chunk 内嵌注释，不拆文件 | 单段不可独立 diff | 242 文件而非 676 |
| 不建索引页 | 静态导航 | `PROGRESS.md` 自动即导航 |
| 不做双语对照文件 | 逐句对照 | 文件数减半，术语靠 GLOSSARY 追溯 |
| 9 检查合并为 1 脚本 | 单条不能独立跑 | 一命令跑完，CI 更短 |
| 单份 PLAN.md | 多版本并存 | 无决策歧义 |

### 11.5 成本

```
676 段 × 均 4.9 KB = 3.30 MB，中文输出约 57.7 万字 ≈ 0.5M token
输出 token（估）：翻译 0.5M / +校对 1.4M / +术语统一 2.3M
按 $3/M 输出：约 $2 / $4 / $7
```

成本不是瓶颈，**一致性才是**。故 M0 的 `GLOSSARY.yaml` + G1 是硬前置。

---

## 12. 验收标准

```
1. 242 个 .md 全部存在于 zh/ 对应路径（30 个为 authored）
2. 翻译覆盖率 = 100%（散文 + 可译文本块），由 manifest 统计
3. G1–G9 全部通过，CI 绿灯
4. 36 处失效链接全部修复并在 KNOWN_ISSUES.md 有记录
5. 每文件 front matter 完整，source_sha256 与 base_commit 匹配
6. zh/PROGRESS.md 显示 11 个模块均 100%
7. M0–M6 全部 status: published（经二次校对）
```

### 单模块独立验收

| 检查 | 命令 | 通过条件 |
|---|---|---|
| 结构 | `python zh/tools/check.py --module M8 --only G9` | H2 数量与原文一致 |
| 术语 | `... --only G1` | 禁用词 0 命中 |
| 图 | `... --only G2` | 框线块内无全角字符 |
| 占位符 | `... --only G4` | `{{...}}` 多重集相等 |
| 链接 | `... --only G5` | 无新增失效 |
| 覆盖率 | `python zh/tools/progress.py` | 该模块段数 100% |
