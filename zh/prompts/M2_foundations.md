# M2_foundations — 概念地基（自包含任务卡）

## 0 你的处境

- 仓库根 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering`
- 分支 **`zh/main`**（不要切 `main`，不要开 PR）；推送 `git push origin zh/main`；禁止推 `upstream`、改 `zh/` 之外文件。
- 前置：M0（工具链）、M1（入口层，已 published）。M1 定下的译法被本书沿用，M2 必须对齐。
- Python 3；工作区干净。本卡经过实际执行验证（M2 已 published，本卡为交付留档 + 复现指南）。

## 1 先读哪几份文件

1. `zh/PLAN/PLAN.md` §「M2 概念地基（11 段）」+ §6 占位符保全 + 「上游既有缺陷」表
2. `zh/prompts/M1_entry.md` §3–§5（术语约定 / STYLE R1–R7 / 基准译法必须沿用）
3. `zh/STYLE.md` 全文、`zh/GLOSSARY.md` 全文（84 条，G1 查禁用译法零命中）
4. `zh/KNOWN_ISSUES.md`（G5 白名单，35 条去重）
5. 范文 `zh/masterclass_content/01_chain_of_thought_module.md`（ATOM→MOLECULE→CELL→ORGAN 同一套概念，术语直接对齐）

## 2 交付物

7 个 zh/ 镜像文件：`zh/00_foundations/01_atoms_prompting.md` 至 `07_prompt_programming.md`。

## 3 关键数字

M2 **7 篇 / 11 段 / 0 空**；可译 47,199 B；ASCII 图 **84** 块；代码 **20** 块；相对链接 **27** 处；`{{...}}` 占位符 1 处（`{{problem}}`，G4 保全）。段锚点由 assemble 自动管理，不手写。

## 4 文件清单

| ID | 任务 | 文件 | 段 | 行区间 | sha256 | 图/码 |
|---|---|---|---:|---|---|---|
| M2-01 | 原子与分子 | `01_atoms_prompting.md` | 1 | 1-241 | d8d05ceaf3efc8b7de28f2ee88deab8bdd28f3357b69745669483c6eb7e2d82b | 图9 码1py |
| M2-01 | 原子与分子 | `02_molecules_context.md` | 1 | 1-298 | dc5e6c881b6e63ea8dbbaf44dadd18d7233d9a37b3bdc2e5acb6e0a180b85ab7 | 图9 码1py |
| M2-02 | 细胞与器官 | `03_cells_memory.md` | 1 | 1-584 | dabf0a515282bd84d6889aa180c121c2860b32cf8794a0fde49e12ba34acd039 | 图16 码1py |
| M2-02 | 细胞与器官 | `04_organs_applications.md` | 2 | 1-960 / 961-1002 | 33e09f94a490c8c6c0a2709a28af2a0d2ed28ea608afdc0ba53af807acd48ee6 | 图22 码2py |
| M2-03 | 工具与编程 | `05_cognitive_tools.md` | 2 | 1-409 / 410-496 | 9447185ed630033a6e6ba1631b3b268da4e81a090b4d77c72946c075a5a22abf | 图7 码2(md/py) |
| M2-03 | 工具与编程 | `06_advanced_applications.md` | 1 | 1-1268 | 3e43e083696bd85e32e9289f5dd295db582ec6de968cd407a3a3795b9d38cc46 | 图8 码4py |
| M2-03 | 工具与编程 | `07_prompt_programming.md` | 3 | 1-305 / 306-773 / 774-994 | 6f494f6eee9e03aa950db75bd8dd563d393198d5f1d1e9ccd637a7c4a61e6303 | 图13 码9(py8/json1) |

## 5 术语

M2 是**全库术语密度最高、译法基准**模块（M7/M8 复用）。GLOSSARY 84 条全部适用。核心锚点：atom=原子 / molecule=分子 / cell=细胞 / organ=器官；context=上下文（禁语境/情景）；prompt=提示词（禁提示语）；token=词元；memory=记忆（禁内存）；agent=智能体（禁代理）；orchestration=编排；shell=协议壳（CLI 语境保留 shell）；emergence=涌现（禁突现）；symbolic residue=符号残差；chain of thought=思维链；context assembly=上下文装配。M1 已冻结译法一律沿用。

## 6 特别处理

1. **ASCII 图 84 块**：图内一字不动（含图内英文 prompt 文本），图下紧跟一行 `> 图：<中文说明> —— <原文关键词短语>`，不留空行。这是全库图最密集的入口模块之一。
2. **`05_cognitive_tools.md` 的 `[parameters]` 伪链接**：原文 `program [Name]([parameters]) {` 位于 `kind=text` 无框线块，G5 会把 `[parameters]` 当失效链接。PLAN「上游缺陷」表明确要求"必须在本版修复，不原样搬运"。处理：在 `(` 后补一个半角空格 → `program [Name]( [parameters]) {`（LINK_RE 的 `([^)\s]+)` 不再匹配），无全角字符（G2 通过），属最小修复。
3. **段锚点坑**：assemble 在每段前插 `<a id="chunk-N"></a>` 与 `<!-- chunk N/M | ... -->`，会使 G6「front matter 在文件首行」FAIL（范文也无段锚点）。assemble 后用正则删这两类行。
4. **多段文件 chunks_done 列全**：04(2段)、05(2段)、07(3段) 的 front matter `chunks_done` 必须列全所有段号，漏列会导致进度少算（M1 曾踩坑）。
5. **G7 WARN 属预期**：`07_prompt_programming.md` 有 5 个无语言标记的过程式 DSL 块被计为英文散文，英文占比 52%；代码按要求原样保留故无法消除，check 退出码仍为 0。

## 7 质量门禁

G1–G9 全部适用。硬指标 **0 FAIL**；G7 WARN 允许（DSL 块原样保留所致）。每篇 `assemble.py --verify` 须 PASS 往返无损。

## 8 不要做的事

不改 `zh/GLOSSARY.yaml`（术语建议写进报告由人工定）；不碰 `zh/tools/`、`zh/PLAN/PLAN.md`、`zh/STYLE.md`；不改上游原文；不手写双语锚点、不删内部链接（未译目标计 pending 是对的）。

## 9 完成判据

- `python zh/tools/manifest.py --check` 无漂移
- `python zh/tools/digits.py` 一致（242 篇 / 676 段 / 30 空）
- `python zh/tools/check.py --module M2` 7 文件 9 PASS / 0 FAIL（当前 1 WARN）
- `python zh/tools/progress.py` → M2 四行 + 汇总行 published（P1 里程碑 published）
- 数字：7 篇 / 11 段 / 0 空；图 84 / 码 20 / 相对链接 27 / `{{...}}` 1 处

## 10 报告格式

`## 交付`（表：任务 / 文件 / 段 / 状态）+ `## 校验`（四命令表）+ `## 偏差`（逐条说明与 PLAN 不一致原因）+ `## 术语建议`（GLOSSARY 应增补/修改词 + 理由，不自行改 YAML）+ `## 下一步`（建议模块 + 遗留问题）。

## 11 建议顺序

1 读 §1 五份文件 + `python zh/tools/digits.py --list` 看数字 → 2 按任务组并行译（M2-01 两篇 / M2-02 两篇 / M2-03 三篇，07 单列因 3 段最重）→ 3 每篇走六步：写 chunk（chunk-01 含完整 front matter, chunks_done 列全段号）→ `assemble.py --out` → 正则删段锚点 → `assemble.py --verify` → `check.py` → 4 主 agent 全模块回归四命令 → 5 按 §10 报告 → 6 提交 `feat(zh): 翻译 M2 概念地基 7 篇（M2-01/02/03）` 并推 `origin/zh/main`。
