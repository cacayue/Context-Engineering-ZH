# M4_course_advanced — 课程·进阶（自包含任务卡）

## 0 你的处境

- 仓库根 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering`
- 分支 **`zh/main`**（不要切 `main`，不要开 PR）；推送 `git push origin zh/main`；禁止推 `upstream`、改 `zh/` 之外文件。
- 前置：M0–M3 均已 published。M2 冻结的译法、M3 沿用并新增的词，M4 必须沿用。
- Python 3。本卡为实际执行的交付留档 + 复现指南。

## 1 先读哪几份文件

1. `zh/prompts/M3_course_core.md` 全文（术语基准 + 六步流程 + 段锚点坑 + authored 导读写法）
2. `zh/PLAN/PLAN.md` §「M4 课程·进阶（35 段）」+ §0.3 空文件 authored 约定 + 「上游既有缺陷」表
3. `zh/STYLE.md` 全文、`zh/GLOSSARY.md` 全文（G1 查禁用译法零命中）
4. `zh/KNOWN_ISSUES.md`（G5 白名单）
5. 范文 `zh/00_COURSE/05_memory_systems/README.md`（**唯一实体 README 译文**）+ 任一 M3 译文（front matter + 图注 + 双语锚点样式）

## 2 交付物

- 15 个 zh/ 镜像译文：M4-01 RAG 5 篇、M4-02 记忆 6 篇（含**实体 README**）、M4-03 工具推理 4 篇
- 2 篇 authored 空 README 的中文导读（RAG 模块 README、工具推理模块 README；`status: authored`，不计入覆盖率）

## 3 关键数字

M4 **17 篇 / 35 段 / 2 空**（15 篇译 35 段 + 2 篇 authored）；可译 164,788 B；ASCII 图 **98** 块；代码 **152** 块；相对链接照写（未译目标计 pending 是对的）。段锚点由 assemble 自动管理，不手写。`{{...}}` 无。

## 4 文件清单

| 文件（相对仓库根） | 任务 | 段 | 行区间 | sha256 | 图/码 |
|---|---|---:|---|---|---|
| `00_COURSE/04_retrieval_augmented_generation/00_rag_fundamentals.md` | M4-01 | 2 | 1-542 / 543-562 | `82c7bd53fb4c655efd7c2e57d2e3df53aa4c8e13aaf51654d60956c8a782b18e` | 图9 码11 |
| `00_COURSE/04_retrieval_augmented_generation/01_modular_architectures.md` | M4-01 | 3 | 1-288 / 289-735 / 736-790 | `123d7185c2569f9473273fa7971b2843f41d073b49f39bc29f6e8daac88e9e5d` | 图12 码5 |
| `00_COURSE/04_retrieval_augmented_generation/02_agentic_rag.md` | M4-01 | 3 | 1-461 / 462-737 / 738-971 | `fba4ac74c434ac4125f46058c82d201bdd35a6314592bc69fa002eb5bd11e0b3` | 图10 码5 |
| `00_COURSE/04_retrieval_augmented_generation/03_graph_enhanced_rag.md` | M4-01 | 3 | 1-477 / 478-988 / 989-1006 | `e9d6dda5abda8466ffd0bb7a2f0768fc322ef2831b382a00b6294d792bca8ce7` | 图10 码5 |
| `00_COURSE/04_retrieval_augmented_generation/04_advanced_applications.md` | M4-01 | 2 | 1-802 / 803-818 | `18f4f538757978efdc1f7190137ea3e2553cdc3313219a5d358e7723e69e2416` | 图7 码8 |
| `00_COURSE/04_retrieval_augmented_generation/README.md` | M4-01 | 0 | authored | `01ba4719…`（换行符） | 导读 |
| `00_COURSE/05_memory_systems/00_memory_architectures.md` | M4-02 | 2 | 1-491 / 492-542 | `afcfbf7ce2fc751b6d55a7815d347048132d818fb7357ed78da18e5f1b2dae8a` | 图8 码7 |
| `00_COURSE/05_memory_systems/01_persistent_memory.md` | M4-02 | 2 | 1-1059 / 1060-1131 | `5ac1437b4d18107cd356fa51538156c1924ff81d8c43184e352c00ab524941e9` | 图8 码8 |
| `00_COURSE/05_memory_systems/02_memory_enhanced_agents.md` | M4-02 | 3 | 1-1054 / 1055-1197 / 1198-1450 | `578de95b0a34a048c27e7d48559962d946414c9ceddb0c098fac048c3995eaa5` | 图8 码11 |
| `00_COURSE/05_memory_systems/03_evaluation_challenges.md` | M4-02 | 3 | 1-351 / 352-839 / 840-949 | `24c78f9e66e24fbf3e27f2719f2f75eea71eefdada2ec522d7a22ea2bd74ff30` | 图7 码10 |
| `00_COURSE/05_memory_systems/04_reconstructive_memory.md` | M4-02 | 2 | 1-864 / 865-895 | `1e36ae91375f54add11217e7025b6d900c3775b22d61a61bc1c8f6526fc58d18` | 图2 码12 |
| `00_COURSE/05_memory_systems/README.md` | M4-02 | 2 | 1-144 / 145-190 | `2ea35f316a49d938241529f3a905974a2113b8e945202034f1630e54c02b3d38` | 图0 码0（**实体 README，按原文翻译**） |
| `00_COURSE/06_tool_integrated_reasoning/00_function_calling.md` | M4-03 | 2 | 1-540 / 541-605 | `22c16bd9aadb523b7113d027bb8e59d0b5c1d98a091c2d8ca22076be305c877f` | 图5 码14 |
| `00_COURSE/06_tool_integrated_reasoning/01_tool_integration.md` | M4-03 | 2 | 1-837 / 838-884 | `95b606f1723871d80607952821254debba72dad43566a21a5adebae26d952906` | 图4 码16 |
| `00_COURSE/06_tool_integrated_reasoning/02_agent_environment.md` | M4-03 | 2 | 1-1628 / 1629-1677 | `995d42578b559a6e7d3ec7318c121fa1e000e2bfed4c0467ad5b7a769669a8df` | 图4 码24 |
| `00_COURSE/06_tool_integrated_reasoning/03_reasoning_frameworks.md` | M4-03 | 2 | 1-1356 / 1357-1396 | `c4f23429a4abe808368809f1e66799f35a2571f325f4e42f132c2e18bf60e401` | 图4 码16 |
| `00_COURSE/06_tool_integrated_reasoning/README.md` | M4-03 | 0 | authored | `01ba4719…`（换行符） | 导读 |

## 5 术语

M2/M3 冻结译法全部沿用。新增高频：retrieval-augmented generation=检索增强生成、RAG=检索增强生成（缩写保留 RAG）、retrieval=检索（禁召回）、chunk=片段、chunking=上下文切分、embedding=嵌入、rerank=重排、grounding=落地依据、memory=记忆（禁内存）、persistent memory=持久记忆、attractor=吸引子、function calling=函数调用、tool=工具、agent=智能体（禁代理）。核心锚点：context=上下文（禁语境/情景）；prompt=提示词；token=词元；orchestration=编排；emergence=涌现。首次出现可「中文（English）」，之后纯中文。

## 6 特别处理

1. **代码块语言多样（152 块）**：python/json/markdown 等原样保留标记与块内内容（含英文注释/prompt 模板），只译块外散文。G3 比对语言序列。
2. **ASCII 图 98 块**：图内一字不动（含图内英文），图下紧跟一行 `> 图：<中文说明> —— <原文关键词短语>`，不留空行。
3. **无标记围栏（含 text kind）原样保留英文**：G2 检查所有无语言标记围栏内不得有全角字符。M3 曾在 `domain_specific_prompting.md` 踩坑——worker 把 text 围栏内英文译成中文并把图注塞进块内导致 G2 FAIL。若图注，必须放在围栏**外**。
4. **唯一实体 README**：`05_memory_systems/README.md` 有原文（190 行/2 段），按译文流程正常翻译；另两个 README 是 1 字节空文件（authored 导读）。
5. **2 篇 authored 空 README**：依同目录正文撰写中文导读。front matter：`chunks: 0` / `chunks_done: []` / `status: authored` / source_sha256 用换行符哈希 `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b`。导读正文**不能用 `##` 标题**（源 0 个 H2，G9 判多出未授权 H2）——用 H1 + 加粗段落 + 列表。首 20 行须含原文锚点与 GLOSSARY 链接（层级从译文目录回到 zh/，本模块在 `zh/00_COURSE/04_xxx/`，原文锚点用 `../../../00_COURSE/04_xxx/README.md`，GLOSSARY 用 `../../GLOSSARY.md`）。
6. **段锚点坑**：assemble 在每段前插 `<a id="chunk-N"></a>` 与 `<!-- chunk N/M | ... -->`，使 G6 FAIL。assemble 后用正则删这两类行。
7. **多段文件 chunks_done 列全**：最多 3 段，front matter `chunks_done` 必须列全所有段号。

## 7 质量门禁

G1–G9 全部适用。硬指标 **0 FAIL**；G7 WARN 允许（代码块/DSL 原样保留所致，check 退出码 0）。每篇 `assemble.py --verify` 须 PASS 往返无损。2 篇 authored 导读同样须 9 PASS / 0 FAIL。

## 8 不要做的事

不改 `zh/GLOSSARY.yaml`（术语建议写进报告由人工定）；不碰 `zh/tools/`、`zh/PLAN/PLAN.md`、`zh/STYLE.md`；不改上游原文；不手写双语锚点、不删内部链接。`.py` 不在交付范围。

## 9 完成判据

- `python zh/tools/manifest.py --check` 无漂移
- `python zh/tools/digits.py` 一致（242 篇 / 676 段 / 30 空）
- `python zh/tools/check.py --module M4` 17 文件 9 PASS / 0 FAIL
- `python zh/tools/progress.py` → M4 任务行 published
- **重要**：check 全绿但 progress 仍 todo 时，须跑 `python zh/tools/manifest.py`（不带 --check）重算 manifest.json 的 status 缓存，再跑 progress.py。
- 数字：17 篇 / 35 段 / 2 空；图 98 / 码 152

## 10 报告格式

`## 交付`（表：任务 / 文件 / 段 / 状态）+ `## 校验`（四命令表）+ `## 偏差`（逐条说明与 PLAN 不一致原因）+ `## 术语建议`（GLOSSARY 应增补/修改词 + 理由，不自行改 YAML）+ `## 下一步`（建议模块 + 遗留问题）。

## 11 建议顺序

1 读 §1 五份文件 → 2 预切分 15 篇到 seg（复用 m3_split.py 改 M4）→ 3 派 worker 只写 chunk（chunk-01 含完整 front matter, chunks_done 列全段号）→ 4 主 agent 统一装配（assemble --out → 正则删段锚点 → --verify → check.py）→ 5 主 agent 写 2 篇 authored 导读 → 6 全模块回归四命令 + manifest 重算 → 7 按 §10 报告 → 8 提交 `feat(zh): 翻译 M4 课程·进阶 15 篇 + 2 篇导读（M4-01/02/03）` 并推 `origin/zh/main`。
