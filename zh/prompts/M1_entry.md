---
title: M1 入口层 · 任务卡
for_agent: fresh context（无历史）
status: ready
depends_on: M0
produces: zh/ 下 23 个文件
blocks: M2（M2 复用 M1 冻结的术语）
---

# 任务：翻译 M1 入口层（23 篇 / 40 段）

## 0. 你的处境

你是一个全新会话，没有历史上下文。以下是全部你需要知道的事。

| 项 | 值 |
|---|---|
| 仓库根 | `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering` |
| 分支 | `zh/main`（**不要切到 main，不要开 PR**） |
| 推送 | `git push origin zh/main` |
| `origin` | `git@github.com:cacayue/Context-Engineering-ZH.git` |
| `upstream` | `jasontang-ai/Context-Engineering`（只读，**永不推送**） |
| Python | 3.14.4，仅标准库 |
| 工作区现状 | M0 已完成并推送，工具链全绿，`zh/` 内无任何译文 |

**背景一句话**：仓库是英文《Context Engineering》课程/知识库（242 篇 / 8.92 MB），
M0 已建成切分→译→装配→校验的工具链。你要译的是 **M1 入口层**：根文档、
仓库手册、结构说明、大师课、导航页。它是读者最先看到的部分，也是 M2 之后
所有模块的术语基准来源。

## 1. 先读这四份文件（不要跳过）

```
zh/PLAN/PLAN.md        计划书。必读 §0.2 §3 §5 §6 §7 §8 §10.1
zh/STYLE.md            文风规范。R1–R7 与排版细则，逐条照做
zh/GLOSSARY.yaml       84 条术语。M1 用到的约 30 条，见 §5
zh/PROGRESS.md         §2 的 M1-01 … M1-05 五行是你的验收目标
```

`PLAN.md` 是唯一规范来源。**本任务卡只补充它没写死的部分**（逐文件清单、
本模块特有的坑、执行顺序）。两者冲突时以 `PLAN.md` 为准，并在报告里指出冲突。

## 2. 交付物（23 个文件）

全部落在 `zh/` 下，路径 = `zh/` + 源路径。用 `zh/tools/manifest.py` 生成的
`zh/manifest.json` 里 `module == "M1"` 的 23 条记录即为准。

| 任务 | 篇 | 段 | 源文件 |
|---|---:|---:|---|
| `M1-01` | 5 | 11 | `README.md` `CITATIONS.md` `CITATIONS_v2.md` `CITATIONS_v3.md` `Complete_Guide.md` |
| `M1-02` | 2 | 8 | `CLAUDE.md` `GEMINI.md` |
| `M1-03` | 5 | 8 | `STRUCTURE/README.md` `STRUCTURE/STRUCTURE.md` `_v2.md` `_v3.md` `TREE.md` |
| `M1-04` | 8 | 8 | `masterclass_content/01_…08_*.md` |
| `M1-05` | 3 | 5 | `00_COURSE/README.md` `00_foundations/README.md` `30_examples/README.md` |
| **合计** | **23** | **40** | |

**先做 M1-04**。8 篇各 1 段，合计 8 段，是全仓最小的完整闭环。用它把
「切分 → 译 → 装配 → G1–G9」全流程走通一次；流程跑通后再做 M1-01/02/03/05。

## 3. 关键数字（必须精确复现）

```
M1 篇数            23
M1 段数            40
M1 空文件          0
可译字节           170,007 B = 0.162 MB（源 23 篇共 303,341 B）
ASCII 图块          40 块（全部原样，图下加中文图注）
有语言标记代码块    24 块（全部原样）
{{...}} 占位符      0 处（M1 没有，别自己造）
相对内部链接        28 处（必须改为 zh 内可达路径）
```

做完后自查：

```bash
python zh/tools/digits.py            # 文档数字与 manifest 一致
python zh/tools/check.py --module M1  # G1–G9 全绿
python zh/tools/manifest.py           # 重算，M1 覆盖率应为 40/40
python zh/tools/progress.py           # 重写 PROGRESS.md
```

## 4. 逐文件清单

`段` 是 `max(1, ⌈可译字节/6144⌉)`；`图/码` 是该文件里不可动的 ASCII 图块数与
代码块数；`坑` 见 §6。

| 源文件 | 任务 | 段 | 图 | 码 | 链接 | 坑 |
|---|---|---:|---:|---:|---:|---|
| `masterclass_content/01_chain_of_thought_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/02_atoms_of_prompting_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/03_molecules_of_context_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/04_cells_of_memory_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/05_organs_and_applications_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/06_cognitive_tools_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/07_advanced_applications_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `masterclass_content/08_prompt_programming_module.md` | M1-04 | 1 | 0 | 0 | 0 |  |
| `Complete_Guide.md` | M1-01 | 1 | 0 | 0 | 8 | 链接 |
| `README.md` | M1-01 | 3 | 4 | 2 | 6 | 徽章 |
| `CITATIONS.md` | M1-01 | 2 | 2 | 6 | 0 | 引用 |
| `CITATIONS_v2.md` | M1-01 | 2 | 2 | 5 | 0 | 引用·与 v1 重叠 24% |
| `CITATIONS_v3.md` | M1-01 | 3 | 1 | 6 | 0 | 引用·与 v2 几乎不同 |
| `CLAUDE.md` | M1-02 | 4 | 0 | 2 | 0 | 长·协议体 |
| `GEMINI.md` | M1-02 | 4 | 0 | 2 | 0 | 长·与 CLAUDE 重叠 19% |
| `STRUCTURE/README.md` | M1-03 | 1 | 1 | 0 | 0 |  |
| `STRUCTURE/STRUCTURE.md` | M1-03 | 2 | 3 | 0 | 0 | 与 v2 重叠 37% |
| `STRUCTURE/STRUCTURE_v2.md` | M1-03 | 3 | 1 | 0 | 0 | 与 v1 重叠 37% |
| `STRUCTURE/STRUCTURE_v3.md` | M1-03 | 1 | 14 | 0 | 0 | 14 张图 |
| `STRUCTURE/TREE.md` | M1-03 | 1 | 1 | 0 | 0 | 路径清单 |
| `00_COURSE/README.md` | M1-05 | 2 | 6 | 0 | 0 | 6 张图 |
| `00_foundations/README.md` | M1-05 | 2 | 5 | 1 | 14 | 14 链接 |
| `30_examples/README.md` | M1-05 | 1 | 0 | 0 | 0 | 仅 208 B |
| **合计** | | **40** | **40** | **24** | **28** | |

逐文件取切分计划（含行号区间与段 sha，必须照它切，否则装配会失败）：

```bash
python zh/tools/plan_chunks.py README.md          # 人读
python zh/tools/plan_chunks.py README.md --json   # 机器读
python zh/tools/plan_chunks.py --module M1 --summary  # 全模块一行一篇
```

## 5. 术语（M1 用到的子集）

从 `zh/GLOSSARY.yaml` 取，不要自创。M1 高频的是这 24 条：

```
context / context engineering / prompt / prompt engineering / prompt programming
atoms / molecules / cells / organs / memory / cognitive tools
chain of thought / few-shot / protocol / protocol shell / schema
agent / field / emergence / attractor / residue / orchestration
evaluation / token budget
```

规则（`STYLE.md` 已写，这里重申三条最容易违的）：

| 规则 | 做法 | 反例 |
|---|---|---|
| R5 中英之间加空格 | `使用 context window 管理上下文` | `使用context window管理上下文` |
| R6 首次出现双语 | `上下文窗口（context window）` | 全篇只写中文，无法追溯原文 |
| R6 二次出现纯中文 | 后文一律 `上下文窗口` | 每处都带英文，读者被淹 |

M1 是全书第一批译文，**你在这里定下的译法会被 M2–M11 沿用**。译完若发现
`GLOSSARY.yaml` 缺词或有更好的译法，**不要直接改 YAML**，在报告 §5 里列出
建议，由人工决定（改了会影响已译文件）。

## 6. 本模块特有的坑（六条，逐条照做）

### 6.1 `CITATIONS*.md`：学术引用不译

三份 CITATIONS 是论文索引。规则：

- **论文标题、作者、期刊、年份、DOI、URL 一律原样**，不译不加书名号。
- `**Source:**` 与 `**Key Concepts:**` 这类标签译成中文（`**来源：**` `**核心概念：**`）。
- 每条下面的解释性文字要译。
- 三份是**不同版本**，不是副本：`CITATIONS.md` 328 行、`v2` 363 行、`v3` 407 行；
  v1→v2 行重叠 24%，v2→v3 只有 1%。**三份都要完整译**，但可以先译 v3
  （内容最全），再译 v1/v2 时复用已确认的译法。

### 6.2 `CLAUDE.md` / `GEMINI.md`：不是重复文件

两者都叫「Cognitive Operating System」，但 **H2 标题只有 1 个相同**
（`Context Schemas`），行重叠 19%。它们是给不同模型的两套协议：
`CLAUDE.md` 927 行（Explore-Plan-Code-Commit、TDD、UI 迭代等 8 类工作流），
`GEMINI.md` 748 行（Terminal-Specific Protocols、Project Navigation 等）。

**不要因为「看起来一样」就跳过或缩写**。两者的差异部分正是内容。

两份都含大量 ```` ```json ```` 与伪代码块（各 2 块），**原样不动**；
其中的 `"description": "..."` 字符串如果是自然语言说明，**要译**（这是少数
需要进代码块的情况，见 `STYLE.md` 的「代码块内自然语言」条款）。

### 6.3 `STRUCTURE/` 四份：版本演进，全部译

`STRUCTURE.md` 384 行 → `_v2` 443 行 → `_v3` 462 行，v1→v2 重叠 37%，
v2→v3 只有 1%。`_v3` 有 **14 张 ASCII 图**，是 M1 图最密的一篇。

`TREE.md` 是纯路径清单（目录树），**路径不译**，只译注释与说明性文字。
若整篇只有路径，保留原样并在开头加一行中文说明。

### 6.4 `README.md`：徽章与外部链接

前 6 个 H2 全是徽章/外链（DeepWiki、DeepGraph、NotebookLM、Discord、
Course Under Construction、Agent Commands）。规则：

- `[![alt](img)](url)` 结构**原样保留**，`alt` 文本译成中文（它是无障碍文本）。
- 徽章 `name` 参数（`?badge=...`）不动。
- 指向 `github.com/davidkimai/...` 或 `jasontang-ai/...` 的外链**保持原 URL**，
  不要改成本 fork 地址。

### 6.5 内部相对链接：28 处必须改对

R7 要求内部链接指向 **zh 内可达路径**。M1 的 28 处集中在三个文件：

| 文件 | 链接数 | 典型 |
|---|---:|---|
| `00_foundations/README.md` | 14 | `./01_atoms_prompting.md` → `./01_atoms_prompting.md`（同目录，路径本身不变，但要确认 zh 侧文件已存在） |
| `Complete_Guide.md` | 8 | `./masterclass_content/01_...md` → `./masterclass_content/01_...md` |
| `README.md` | 6 | `00_foundations/01_atoms_prompting.md` → `00_foundations/01_atoms_prompting.md` |

路径形态不变（`zh/` 是镜像），**但要逐条确认路径写对了**。

M1 的链接大多指向**尚未翻译**的 M2 文件（如 `./01_atoms_prompting.md`）。
`check.py` 的 G5 对这种情况有专门状态：

| 情形 | G5 结果 |
|---|---|
| 目标存在 | PASS，计入「可达」 |
| 目标不存在，但对应源文件存在 | PASS，计入「待译 N 处」 |
| 目标不存在，源文件也不存在 | **FAIL** |

所以 M1 做完时 `00_foundations/README.md` 会显示
`PASS  链接全部可达（待译 14 处）`，这是正确状态。**不要为了消警删链接**，
那会让读者在 M2 译完后找不到入口。

全库译完后的终检用 `python zh/tools/check.py --all --strict-links`，
那时「待译」会被计为失败。

### 6.6 `masterclass_content/`：8 篇同构，用同一套模板

8 篇结构完全相同：`# Module N: 标题` → `### Module Summary` → `### Key Takeaways`
→ `### Your Turn: Mini-Challenge`。**注意是 H1 + 三个 H3，没有 H2**。

译法必须一致：

| 原文 | 译法 |
|---|---|
| `### Module Summary` | `### 模块摘要` |
| `### Key Takeaways` | `### 关键要点` |
| `### Your Turn: Mini-Challenge` | `### 动手练习：小挑战` |

第一篇定下来后 8 篇照抄，`check.py` 的 G3（标题层级）会比对数量，标题文字
不一致不算错，但**层级数量必须与原文一致**（1 个 H1 + 3 个 H3）。

## 7. 质量门禁

```bash
python zh/tools/check.py --module M1        # G1–G9 全绿才算完成
python zh/tools/check.py zh/README.md       # 单文件
python zh/tools/check.py zh/README.md --only G3,G9   # 只跑结构类
```

九项检查的含义（`PLAN.md` §7 有完整定义）：

| 门禁 | 查什么 | M1 的风险点 |
|---|---|---|
| G1 | 术语与 `GLOSSARY.yaml` 一致、无禁用译法 | 24 条高频术语 |
| G2 | 代码块语言标记与数量不变 | 32 块，`CLAUDE/GEMINI` 各 2 |
| G3 | 标题层级数量与原文一致 | `masterclass` 是 H1+3×H3，无 H2 |
| G4 | `{{...}}` 占位符原样 | M1 为 0，出现即错 |
| G5 | 内部链接可达（未译目标计入「待译」，不判 FAIL） | 28 处，多数指向 M2 |
| G6 | 段数与 manifest 一致 | 40 段 |
| G7 | 中文行占比 ≥ 阈值 | 引用类文件标题多，注意别只译标题 |
| G8 | 双语锚点（`> 原文：` + GLOSSARY 链接）可达 | 由 `assemble.py` 自动生成 |
| G9 | 结构指纹（围栏数、H2 数、占位符、语言序列） | 全模块 |

## 8. 不要做的事

| 禁止 | 原因 |
|---|---|
| 改 `zh/` 之外任何文件（`zh_checks.yml` 除外） | CI `scope` job 会失败；改上游原文会让 `git pull upstream main` 冲突 |
| 改 `zh/PLAN/PLAN.md` / `zh/STYLE.md` / `zh/GLOSSARY.yaml` | 它们是规范。有异议写进报告 |
| 改 `zh/tools/*.py` | 工具已验收。发现 bug 写进报告，不要顺手改 |
| 推 `upstream` | 无权限且不应改原项目 |
| 开 PR | 这是个人学习分支 |
| 为了「好看」合并段落 | G9 结构指纹会失败 |
| 译代码块里的标识符/URL/路径 | 示例会失效 |
| 用 `~~~/````` 等变体改写围栏 | G2/G9 会失败 |
| 跳过 CITATIONS 的 v1/v2「因为 v3 更全」 | 三份都是读者会看到的内容 |

## 9. 完成判据

按顺序全绿才算完成：

```bash
python zh/tools/manifest.py --check   # 无漂移
python zh/tools/digits.py             # 数字一致
python zh/tools/check.py --module M1  # G1–G9 全绿，0 FAIL
python zh/tools/progress.py           # PROGRESS.md 中 M1 五行全部 published
git status --short                    # 只有 zh/ 下的新文件与 manifest/PROGRESS 改动
```

`PROGRESS.md` 的 M1 五行应变为：

```
| M1-01 | 根文档 | 5 | 11 | 0 | 11 / 11 | published |
| M1-02 | 仓库手册 | 2 | 8 | 0 | 8 / 8 | published |
| M1-03 | 结构说明 | 5 | 8 | 0 | 8 / 8 | published |
| M1-04 | 大师课 8 篇 | 8 | 8 | 0 | 8 / 8 | published |
| M1-05 | 导航页 | 3 | 5 | 0 | 5 / 5 | published |
```

## 10. 报告格式

完成后按此格式回复，不要复述代码：

```markdown
## 交付
| 任务 | 文件 | 段 | 状态 |
|---|---:|---:|---|

## 校验
| 命令 | 结果 |
|---|---|
| manifest.py --check | |
| digits.py | |
| check.py --module M1 | |
| progress.py | |

## 偏差
（与 PLAN.md / 本任务卡不一致之处，逐条说明原因）

## 术语建议
（GLOSSARY.yaml 应该增补或修改的词，附理由；不要自行修改）

## 下一步
（建议下一个模块，以及本模块遗留问题）
```

## 11. 建议执行顺序

```
1  读 §1 的四份文件，跑 python zh/tools/digits.py --list 看清全模块数字
2  M1-04 第一篇 01_chain_of_thought_module.md：
   plan_chunks.py → 逐段译 → assemble.py → check.py 单文件
   这一段是流程验证，把它走细，后面 7 篇是复制
3  M1-04 其余 7 篇（同构，模板复用）
4  check.py --module M1 --only G3,G9  确认 8 篇结构一致
5  M1-01 Complete_Guide.md（8 链接，先做最短的）
6  M1-01 README.md（徽章 + 4 图 + 6 链接，坑最多）
7  M1-01 CITATIONS_v3 → v1 → v2（v3 最全，先定术语）
8  M1-03 STRUCTURE_v3（14 图）→ STRUCTURE.md → v2 → README → TREE
9  M1-02 CLAUDE.md → GEMINI.md（最长，4 段/篇，放最后避免疲劳）
10 M1-05 三篇导航页（含 14 链接的 00_foundations/README.md）
11 全模块回归：manifest → digits → check --module M1 → progress
12 分组提交（建议：M1-04 一个提交，M1-01/03/05 各一个，M1-02 一个）
```

提交消息沿用仓库风格：`feat(zh): 翻译 M1-04 大师课 8 篇`。
一个模块一个提交；若 M1 分多次提交，每次都要把 `manifest.json` 与
`PROGRESS.md` 一并带上（CI 的 `progress` job 会检查）。
