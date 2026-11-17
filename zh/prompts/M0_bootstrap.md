---
title: M0 基础设施 · 任务卡
for_agent: fresh context（无历史）
status: ready
depends_on: 无
produces: zh/GLOSSARY.yaml zh/STYLE.md zh/NOTICE zh/tools/*.py .github/workflows/zh_checks.yml
blocks: M1–M11 全部
---

# 任务：构建 zh/ 中文化基础设施（M0）

## 0. 你的处境

你是一个全新会话，没有历史上下文。以下是全部你需要知道的事。

| 项 | 值 |
|---|---|
| 仓库根 | `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering` |
| 分支 / commit | `main` / `6158def` |
| `origin` | `git@github.com:cacayue/Context-Engineering-ZH.git`（个人 fork） |
| `upstream` | `https://github.com/jasontang-ai/Context-Engineering.git`（上游，**只读，不要推**） |
| 工作区现状 | `zh/` 为未跟踪目录，内含 `zh/PLAN/PLAN.md`、`zh/PROGRESS.md`、18 个带 `.gitkeep` 的空目录 |
| Python | 3.14.4，仅用标准库，**禁止引入第三方依赖** |

**背景一句话**：这个仓库是英文的《Context Engineering》课程/知识库（242 篇 Markdown，8.92 MB）。目标是把全部正文译成中文，放进 `zh/` 镜像目录。翻译由 AI 执行，所以先要有**可切分、可校验、可断点续跑**的工具链。你要做的就是这套工具链。

## 1. 先读这两份文件（不要跳过）

```
zh/PLAN/PLAN.md    计划书，688 行。至少读 §1 §3 §4 §5 §6 §7 §8
zh/PROGRESS.md     进度表，含 42 个任务的篇/段数（你的工具必须复现这些数字）
```

`PLAN.md` 是唯一规范来源。**本任务卡只补充它没写死的部分**（CLI 契约、JSON schema、模块映射算法）。两者冲突时以 `PLAN.md` 为准，并在报告里指出冲突。

## 2. 交付物（10 件，缺一不算完成）

| # | 路径 | 内容 |
|---|---|---|
| 1 | `zh/GLOSSARY.yaml` | 60–100 条术语 |
| 2 | `zh/STYLE.md` | 文风规范（R1–R7 + 排版细则） |
| 3 | `zh/NOTICE` | MIT + 上游署名 |
| 4 | `zh/tools/manifest.py` | 扫描 → `zh/manifest.json` |
| 5 | `zh/tools/plan_chunks.py` | 单文件切分计划 |
| 6 | `zh/tools/assemble.py` | 合并 chunk → 单文件，往返无损 |
| 7 | `zh/tools/check.py` | G1–G9 九项检查，单一入口 |
| 8 | `zh/tools/progress.py` | 重写 `zh/PROGRESS.md` |
| 9 | `zh/tools/glossary_md.py` | `GLOSSARY.yaml` → `GLOSSARY.md` 人读版 |
| 10 | `.github/workflows/zh_checks.yml` | CI，仅监听 `zh/**` |

## 3. 关键数字（你的工具必须精确复现）

```
源 .md 文件        242
总段数             676    ← max(1, ceil(可译字节 / 6144)) 按文件累加
可译字节总量       3.30 MB（散文 1.86 MB + 无标记纯文本块 1.44 MB）
不译的代码块       5.63 MB
  其中含框线 ASCII 图  915 块 / 1.79 MB
  其中有语言标记      1303 块 / 3.83 MB（python 870 块 / 2.99 MB）
围栏块总数         3595
空文件（1 字节）    30     ← status: authored，不计入覆盖率
未闭合围栏文件      7
```

**为什么是 676 而不是 567 或 563**：
- `总体积 ÷ 6144 = 563` — 错，忽略了"每个文件至少一次调用"
- `按模块聚合取整 = 567` — 错，小文件被合并
- `max(1, ⌈可译字节/6144⌉) 按文件累加 = 676` — 对，这是真实调用次数

段数分布：0 段 30 篇、1 段 80 篇、2 段 43、3 段 24、4 段 25、5 段 7、6 段 3、7 段 4、
8 段 6、9 段 11、10 段 3、11 段 1、12 段 1、14 段 3、15 段 1。最大单文件
`40_reference/retrieval_indexing.md` 15 段。

## 4. 模块映射算法（必须严格照此实现）

按顺序匹配，首个命中即采用。路径均为仓库根相对。

```
M1   根目录 7 个 .md：README.md CLAUDE.md GEMINI.md Complete_Guide.md
     CITATIONS.md CITATIONS_v2.md CITATIONS_v3.md
     + STRUCTURE/**
     + masterclass_content/**
     + 00_foundations/README.md
     + 00_COURSE/README.md
     + 30_examples/README.md
M2   00_foundations/0[1-7]_*.md
M3   00_COURSE/0[0-3]_*.md 及其子目录全部
M4   00_COURSE/0[4-6]_*.md 及其子目录全部
M5   00_COURSE/(07|08|09|10)_*.md 及其子目录全部
M6   20_templates/** 60_protocols/** .claude/** 10_guides_zero_to_hero/**
     30_examples/**（README.md 除外，已归 M1）
M7   40_reference/**
M8   NOCODE/**
M9   cognitive-tools/**
M10  00_foundations/(08|09|1[0-4])_*.md  00_EVIDENCE/**  SECURITY_RESEARCH/**
     PODCASTS/**  .github/**
M11  50_contrib/** 70_agents/** 80_field_integration/** context-schemas/**
```

校验（必须全部通过）：

```
M1  23 篇   M2   7 篇   M3  27 篇   M4  17 篇   M5  17 篇   M6  63 篇
M7  13 篇   M8  32 篇   M9  25 篇   M10 14 篇   M11  4 篇
合计 242 篇 / 676 段
```

## 5. 任务映射算法（42 个任务）

模块内再细分。同样按序匹配。

```
M1-02  CLAUDE.md GEMINI.md          ← 必须先判，否则 CLAUDE/GEMINI 会被 M1-01 吃掉
M1-01  根目录其余 .md（README/CITATIONS*/Complete_Guide）
M1-03  STRUCTURE/**
M1-04  masterclass_content/**
M1-05  00_foundations/README.md 00_COURSE/README.md 30_examples/README.md
M2-01  00_foundations/0[12]_*      M2-02  0[34]_*      M2-03  0[567]_*
M3-01  00_COURSE/00_*   M3-02  01_*   M3-03  02_*   M3-04  03_*
M4-01  00_COURSE/04_*   M4-02  05_*   M4-03  06_*
M5-01  00_COURSE/07_*   M5-02  08_*   M5-03  09_*   M5-04  10_*
M6-01  20_templates/**       M6-02  60_protocols/**
M6-03  10_guides_zero_to_hero/**  M6-04  30_examples/**（README 除外）
M6-05  .claude/**
M7-01  README 之外的 retrieval*/latent*      M7-02  *residue*/emergence*
M7-03  *attractor*/field_mapping*            M7-04  其余（patterns/cognitive_patterns/token_budgeting/eval_checklist）
M7-05  README.md 及 *schema*
M8-01  NOCODE/00_foundations/**    M8-02  NOCODE/10_mental_models/**
M8-03  NOCODE/20_practical_protocols/**
M8-04  NOCODE/(30_field_techniques|40_protocol_design)/**
M8-05  NOCODE/** 其余
M9-01  cognitive-tools/README.md + cognitive-architectures/**
M9-02  cognitive-schemas/** + cognitive-templates/**
M9-03  cognitive-programs/**
M10-01 00_foundations/(08|09|11|12)_*    M10-02  00_foundations/(10|13|14)_*
M10-03 00_EVIDENCE/** + SECURITY_RESEARCH/**    M10-04  PODCASTS/** + .github/**
M11-01 50_contrib/** 70_agents/** 80_field_integration/** context-schemas/**
```

校验（必须与 `zh/PROGRESS.md` §2 的 42 行完全一致）：

| 任务 | 篇 | 段 | 任务 | 篇 | 段 | 任务 | 篇 | 段 |
|---|---:|---:|---|---:|---:|---|---:|---:|
| M1-01 | 5 | 11 | M2-01 | 2 | 2 | M3-01 | 7 | 23 |
| M1-02 | 2 | 8 | M2-02 | 2 | 3 | M3-02 | 8 | 27 |
| M1-03 | 5 | 8 | M2-03 | 3 | 6 | M3-03 | 6 | 15 |
| M1-04 | 8 | 8 | | | | M3-04 | 6 | 14 |
| M1-05 | 3 | 5 | | | | | | |

（其余 42 行的期望值见 `zh/PROGRESS.md` §2，逐行核对。）

## 6. 可译字节的定义（决定段数，必须精确）

对每个 `.md`：

```
0. 围栏解析必须支持：``` 与 ~~~ 两种；3 个及以上反引号/波浪号；
   允许 0–3 空格缩进；info string 可含字母数字；未闭合则按到文末处理
1. 用 ^ {0,3}```(\w*)\s*$ 开启围栏，同字符数或更多时为关闭
2. 分类关闭时的块：
   lang 非空                          → 不可译（代码）
   lang 为空 且 含框线字符             → 不可译（ASCII 图）
   lang 为空 且 不含框线字符           → 可译（纯文本块）
3. 框线字符集：─│┌┐└┘├┤┬┴┼╭╮╰╯╔╗╚╝║═
4. 可译字节 = 文件总字节 − Σ不可译块字节 + Σ可译块字节
   即：prose_bytes + plain_text_block_bytes
5. chunks = max(1, ceil(可译字节 / 6144))
6. 文件字节 < 5 → 空文件，chunks = 0，status = authored
```

## 7. 各交付物的详细规格

### 7.1 `zh/GLOSSARY.yaml`

```yaml
- en: Context Engineering
  zh: 上下文工程
  first_use: 上下文工程（Context Engineering）
  scope: doc
  forbid: [语境工程]
```

字段：`en`（必填）、`zh`（必填）、`scope`（必填，固定 `doc`）、`first_use`（可选）、`forbid`（可选，禁用译法列表）、`ambiguity`（可选，一词多义）、`note`（可选）。

**必须包含**这些真实歧义词，每条给出消歧规则：

| en | 歧义 | 约定 |
|---|---|---|
| `field` | 神经场 / 数据字段 | 场（正文）；`field`（YAML/JSON key） |
| `memory` | 记忆系统 / 程序变量 | 记忆（正文）；`memory`（代码） |
| `agent` | 智能体 / `.agent.md` 文件 | 智能体；文件名保留 |
| `shell` | 协议壳 / bash shell | 协议壳；`shell` 保留 |
| `protocol` | 协议壳规范 / 通信协议 | 协议（按上下文） |
| `residue` | 符号残差 / 代码残留 | 残差；残留 |
| `pattern` | 设计模式 / 正则模式 | 模式 |

**必须覆盖**的核心术语（至少这些，可再加）：context, prompt, context window, token, embedding, retrieval, retrieval-augmented generation (RAG), chunk, memory, working memory, long-term memory, semantic memory, episodic memory, agent, multi-agent, tool use, function calling, orchestration, protocol, shell, schema, template, atom, molecule, cell, organ, field, attractor, emergence, resonance, residue, recursive, meta-recursive, prompt programming, chain of thought, few-shot, zero-shot, in-context learning, context engineering, context management, context processing, latent space, attention, quantization, distillation, evaluation, benchmark, grounding, hallucination, guardrail, observability, trace, feedback loop, token budget, compression, summarization, reranking, vector store, knowledge graph。

`GLOSSARY.md`（人读版）**不需要**现在生成，`progress.py` 或后续任务会做。M0 只产出 `.yaml`。

### 7.2 `zh/STYLE.md`

必须包含：

```
1. R1–R7 七条规则（逐字取自 zh/PLAN/PLAN.md §5「七条不可协商规则」）
2. 中文与拉丁字母/数字之间加半角空格
3. 标点：正文用全角，代码/路径/命令内用半角
4. 代码块与 ASCII 图前后各留一个空行
5. 图注格式：> 图：<中文说明> —— <原文关键词>
6. 标题：只译文字，保留 # 数量与原文一致
7. 链接文字译，URL 不动
8. 表格：表头译，分隔行不动
9. 引号：中文用「」，嵌套用『』；原文用 " " 时改「」
10. 数字与单位保留原文（如 128K、3.5%）
11. 列表符号与缩进保持原样
12. 不译：变量名、函数名、文件名、CLI flag、JSON key、URL
```

### 7.3 `zh/NOTICE`

```
本目录（zh/）是 Context-Engineering 的中文译本。
原文：https://github.com/jasontang-ai/Context-Engineering
原作者：davidkimai
许可：MIT（全文见仓库根 LICENSE）
本译本同样以 MIT 许可发布。
原文版权归原作者所有；译文版权归译者所有。
```

### 7.4 `zh/tools/manifest.py`

```
python zh/tools/manifest.py             # 扫描全部，写 zh/manifest.json
python zh/tools/manifest.py --check     # 只比对，不写；有漂移则退出码 1
python zh/tools/manifest.py --module M2 # 只处理该模块
```

输出的 `zh/manifest.json`：

```json
{
  "base_commit": "6158def",
  "generated_at": "2026-11-17T00:00:00Z",
  "chunk_bytes": 6144,
  "totals": {"files": 242, "chunks": 676, "chunks_done": 0, "authored": 30, "published": 0},
  "files": [
    {
      "source": "00_foundations/01_atoms_prompting.md",
      "target": "zh/00_foundations/01_atoms_prompting.md",
      "module": "M2",
      "task": "M2-01",
      "source_bytes": 11761,
      "source_sha256": "<64 hex>",
      "todo_bytes": 11400,
      "chunks": 2,
      "chunks_done": [],
      "status": "todo",
      "authored": false
    }
  ]
}
```

状态读取规则：

```
zh 目标文件不存在           → status = "authored"（若空文件）或 "todo"
zh 目标文件存在但无 front matter → "draft"
zh 目标文件有 front matter   → 取其 status；chunks_done 取其值
```

排序：`files` 按 `source` 字典序。

### 7.5 `zh/tools/plan_chunks.py`

```
python zh/tools/plan_chunks.py 00_foundations/02_molecules_context.md
python zh/tools/plan_chunks.py 00_foundations/02_molecules_context.md --json
python zh/tools/plan_chunks.py --module M2 --summary
```

默认输出 Markdown，每段一块：

```markdown
### chunk 1/3  lines 1-118  sha 4b1c8e2a  bytes 5900
## 引言
## 上下文即分子

### chunk 2/3  lines 119-260  sha 9f2d01bb  bytes 6050
## 组合示例
```

切分规则：

```
1. 以 ^##  为一级切分点，^###  为二级
2. 累计字节达到 6144 即切
3. 遇到代码块/表格/ASCII 图不切——宁可超限
4. 单段 < 512 字节时并入下一段
5. 文件头（front matter 之后、首个 ## 之前）单独成段，若无内容则并入第 1 段
```

### 7.5b `zh/tools/assemble.py`

```
python zh/tools/assemble.py <源文件路径> --out zh/<路径>   # 从 .chunks/ 合并
python zh/tools/assemble.py <源文件路径> --verify          # 只校验：往返无损
```

合并规则：

```
1. 读 .chunks/<路径>.chunk-NN.md（若存在），按编号顺序拼接
2. 在每段前插入 <a id="chunk-N"></a> 与 <!-- chunk N/M | source_lines A-B | sha xxxx -->
3. 第一段已含 front matter → 直接前置
4. 第一段无 front matter → 生成最简 front matter（title 取首个 H1，source/chunks/status=todo）
5. --verify：合并结果去掉 chunk 注释后，与原文逐字节比对的**结构**（围栏数、H2 数、
   {{占位符}}多重集、代码块语言序列）必须相等；不等则打印首个差异位置并退出 1
```

`--verify` 不做逐字节比对（译文本来就不同），只比对**结构指纹**。这与 G3/G4/G9 同源。

### 7.6 `zh/tools/check.py`

```
python zh/tools/check.py zh/00_foundations/01_atoms_prompting.md
python zh/tools/check.py --module M2
python zh/tools/check.py --all
python zh/tools/check.py <path> --only G2,G4
python zh/tools/check.py --self-test
```

输出格式，每项一行：

```
G1 术语一致性     PASS
G2 ASCII 图完整性 FAIL  zh/40_reference/attractor_dynamics.md:142  框线块含全角字符
G3 代码围栏       PASS
...
汇总 7 PASS / 2 FAIL
```

退出码：全通过 0，否则 1。`--self-test` 用内置的正/反样例自检九项检查，必须全绿。

九项检查定义见 `zh/PLAN/PLAN.md` §7。补充实现细节：

```
G1  读 zh/GLOSSARY.yaml 的 forbid 列表，在译文散文区搜索；命中即 FAIL
    （代码块内不搜）
G2  对每个无语言标记块，若匹配 [\u4e00-\u9fff\u3000-\u303f\uff00-\uffef] 则 FAIL
G3  ``` 计数为偶数；块的语言标记与源文件同序同值
G4  正则 \{\{[^}]+\}\} 提取后排序比对，多重集必须相等
G5  相对链接目标存在；白名单见 §8
G6  front matter 含 title/source/module/task/chunks/status/source_sha256；
    source_sha256 与当前源文件一致
G7  代码块之外，英文行（含 ASCII 字母且无 CJK 的行）占比 > 30% → WARN（不 FAIL）
G8  L1/L2 文件首 20 行内必须含 "> 原文：" 与 "GLOSSARY"
G9  H2 数量与源文件一致（允许译文多出「小结」「延伸阅读」各一节）
```

### 7.7 `zh/tools/progress.py`

```
python zh/tools/progress.py            # 读 manifest.json，重写 zh/PROGRESS.md
python zh/tools/progress.py --stdout   # 不写文件，只打印
```

必须**逐字保持** `zh/PROGRESS.md` 现有的结构（1 个 H1 + 7 个 H2 + 6 个表格），只替换数字与状态。当前文件是手写的样板，你的脚本要能生成与它结构相同的结果（数值当前全为 0）。

`zh/PROGRESS.md` front matter 的 `generated_at` 更新为当前时间。

### 7.8 `.github/workflows/zh_checks.yml`

```yaml
name: zh checks
on:
  push:
    paths: ['zh/**']
  pull_request:
    paths: ['zh/**']
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: python zh/tools/manifest.py --check
      - run: python zh/tools/check.py --all
```

**注意**：不得使用 `paths-ignore: ['**.md']`——上游两个 workflow 都这么写，导致 Markdown 变更零校验，这正是要修的。

## 8. 已知失效链接白名单（G5 用）

实测 36 条失效。写入 `zh/KNOWN_ISSUES.md`：

```
00_COURSE/05_memory_systems/README.md               03_reconstructive_memory.md        → 04_reconstructive_memory.md
00_COURSE/07_multi_agent_systems/03_emergent_behaviors.md  ../08_field_integration/     → ../08_field_theory_integration/
00_COURSE/09_evaluation_methodologies/00_evaluation_frameworks.md  10_orchestration_capstone.md  → 不存在
20_templates/README.md          resonance_measurement.py / attractor_detection.py / symbolic_residue_tracker.py
                                meta_recursive_patterns.py / unified_field_engine.py / interpretability_scaffolding.py
                                collaborative_evolution_framework.py / cross_modal_context_bridge.py        → 全部不存在
40_reference/README.md          boundary_operations.md / quantum_semantic_metrics.md / unified_field_operations.md
                                meta_recursive_patterns.md / interpretability_metrics.md
                                collaborative_evolution_guide.md / cross_modal_context_handbook.md          → 全部不存在
40_reference/README.md          ../../.github/CONTRIBUTING.md      → 不存在
60_protocols/README.md          ../../00_foundations/08_neural_fields_foundations.md 等 4 条（层级应为 ../）
60_protocols/README.md          ../../70_agents/01_residue_scanner/                  → 不存在
60_protocols/digests/README.md  recursive.emergence.digest.md / recursive.memory.digest.md / field.resonance.digest.md
                                field.self_repair.digest.md / context.memory.digest.md → 全部不存在
60_protocols/digests/attractor.co.emerge.digest.md  ../shells/attractor.co.emerge.shell
                                ../../../00_foundations/11_...md  ../../../20_templates/field_resonance_measure.py
cognitive-tools/README.md       ../../.github/CONTRIBUTING.md
cognitive-tools/cognitive-programs/basic-programs.md  ./program-examples.ipynb
cognitive-tools/cognitive-templates/composition.md    ../integration/with-rag.md ../integration/with-memory.md
```

这些是**上游**的问题，不是你造成的。M0 只负责记录到 `zh/KNOWN_ISSUES.md` 并让 G5 读取白名单；修复发生在 M1–M11 翻译时（R7：改为 zh 内可达路径）。

## 9. 不要做的事

| 禁止 | 原因 |
|---|---|
| 翻译任何正文内容 | 那是 M1–M11 的任务 |
| 修改 `zh/` 以外的任何文件（除 `.github/workflows/zh_checks.yml`） | 上游文件只读 |
| 引入第三方依赖（pyyaml 等） | 仅标准库。YAML 用手写解析或极简 parser |
| commit / push | 完成后报告即可，由人工审查后再提交 |
| 推送到 `upstream` | 只读上游 |
| 改写 `zh/PLAN/PLAN.md` | 它是规范。发现错误在报告里写，不要改 |

## 10. 完成判据

全部满足才算完成：

```
[ ] 9 个交付物全部存在
[ ] python zh/tools/manifest.py 输出 242 files / 676 chunks / 30 authored
[ ] manifest.json 的模块分布与 §4 校验表一致（11 个模块，篇数逐个相等）
[ ] manifest.json 的任务分布与 zh/PROGRESS.md §2 的 42 行一致（篇/段/空 三列全等）
[ ] python zh/tools/check.py --self-test 九项全绿
[ ] python zh/tools/check.py --all 在空 zh/ 上不报 crash（应报"无译文，跳过"）
[ ] python zh/tools/progress.py 生成的 zh/PROGRESS.md 与原文件章节结构一致
[ ] python zh/tools/plan_chunks.py 00_foundations/02_molecules_context.md 输出的段数
    等于 manifest.json 中该文件的 chunks
[ ] zh/GLOSSARY.yaml 条目数 ≥ 60，7 个歧义词全部有 ambiguity 字段
[ ] zh/STYLE.md 含 R1–R7 与 12 条排版细则
[ ] .github/workflows/zh_checks.yml 不含 paths-ignore
[ ] git status 中除上述 8 件 + zh/KNOWN_ISSUES.md 外无其他改动
```

## 11. 报告格式

完成后按此结构回复（不要长篇复述代码）：

```markdown
## 交付

| 文件 | 行数 | 说明 |
|---|---:|---|
| zh/GLOSSARY.yaml | N | 条目数 |
| zh/STYLE.md | N | |
| zh/NOTICE | N | |
| zh/tools/manifest.py | N | |
| zh/tools/plan_chunks.py | N | |
| zh/tools/assemble.py | N | |
| zh/tools/check.py | N | |
| zh/tools/progress.py | N | |
| .github/workflows/zh_checks.yml | N | |
| zh/KNOWN_ISSUES.md | N | 36 条失效链接 |

## 校验

manifest: 242 files / 676 chunks / 30 authored
模块分布: M1 23 M2 7 M3 27 M4 17 M5 17 M6 63 M7 13 M8 32 M9 25 M10 14 M11 4
self-test: 9/9 PASS
check --all: 无 crash

## 与 PLAN.md 的偏差
（若有，逐条列出：位置、原文说法、实测结果、建议）

## 下一步建议
（M1 从哪个任务开始，为什么）
```

## 12. 建议执行顺序

```
1. 读 zh/PLAN/PLAN.md 与 zh/PROGRESS.md
2. 写 manifest.py（先跑通 242/676 这两个数字，它们是一切的基准）
3. 写 check.py 的 G3 G9（最容易验证），再补 G1 G2 G4 G6 G8，最后 G5 G7
4. 写 plan_chunks.py，用 manifest.py 的 chunks 值交叉验证
5. 写 assemble.py，用 --verify 的结构指纹做往返验证
6. 写 progress.py，让输出与原 zh/PROGRESS.md 结构一致
7. 写 GLOSSARY.yaml / STYLE.md / NOTICE / KNOWN_ISSUES.md
8. 写 zh_checks.yml
9. 跑一遍 §10 的全部判据
```

不要跳步。第 2 步的数字不对，后面全错。

## 13. 围栏解析的三个陷阱（实测已踩）

写 `manifest.py` 的围栏扫描时，朴素实现 `^```(\w*)$` 会算错段数。必须处理：

| 陷阱 | 实测样例 | 后果 |
|---|---|---|
| 缩进围栏（0–3 空格） | `CITATIONS_v2.md:157` 起 3 个块缩进 3 空格 | 该文件从 2 段错算成 3 段 |
| 4 个及以上反引号 | `.claude/commands/legal.agent.md`、`lit.agent.md`、`20_templates/PROMPTS/pipeline.agent.md` | 围栏提前闭合，后续正文被吞 |
| `~~~` 围栏 | `40_reference/latent_mapping.md` | 整块代码被当成散文计入可译量 |
| 未闭合围栏 | `20_templates/PROMPTS/few_shot_learning.md`、`verification_loop.md`、`40_reference/token_budgeting.md`、`NOCODE/20_practical_protocols/07_interpretability_protocols.md`、`SECURITY_RESEARCH/SYSTEM_PROMPTS/claude_code_system_prompt.md`、`STRUCTURE/TREE.md`、`cognitive-tools/cognitive-programs/advanced-programs.md` | 其后全文被当成代码 → 严重少算 |

正确实现见 §6 第 0 步。用 `zh/manifest.json` 的 `totals.chunks == 676` 做验收即可——
算错一个文件，总数就变。

朴素实现的实际偏差（已实测，不是理论值）：

| 错误实现 | 得到的段数 |
|---|---:|
| 只认 ```，不认 `~~~` | 1076 |
| art 块整块扣除（含围栏行） | 675 |
| code 块只扣块体、不扣围栏行 | 669 |
| 未闭合围栏跳过不算 | 707 |
| **正确：code 扣整块 + art 只扣块体** | **676** |

676 是唯一自洽的口径，不是"约等于"。
