# M3_course_core — 课程·基础（自包含任务卡）

## 0 你的处境

- 仓库根 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering`
- 分支 **`zh/main`**（不要切 `main`，不要开 PR）；推送 `git push origin zh/main`；禁止推 `upstream`、改 `zh/` 之外文件。
- 前置：M0（工具链）、M1（入口层）、M2（概念地基，术语基准）均已 published。M2 冻结的译法 M3 必须沿用。
- Python 3。本卡为实际执行的交付留档 + 复现指南。

## 1 先读哪几份文件

1. `zh/prompts/M2_foundations.md` 全文（术语基准 + 六步流程 + 段锚点坑）
2. `zh/PLAN/PLAN.md` §「M3 课程·基础（79 段）」+ §0.3 空文件 authored 约定 + 「上游既有缺陷」表
3. `zh/STYLE.md` 全文、`zh/GLOSSARY.md` 全文（84 条，G1 查禁用译法零命中）
4. `zh/KNOWN_ISSUES.md`（G5 白名单）
5. 范文 `zh/00_foundations/01_atoms_prompting.md`（front matter + 图注 + 双语锚点样式）

## 2 交付物

- 21 个 zh/ 镜像译文：`zh/00_COURSE/00_*` ~ `03_*` 四个子目录下的 `.md`
- 6 篇 authored 空 README 的中文导读（`status: authored`，不计入覆盖率）：四个模块 README + `exercises/README.md` + `labs/README.md`

## 3 关键数字

M3 **27 篇 / 79 段 / 6 空**（其中 21 篇译 79 段 + 6 篇 authored）；可译 424,242 B；ASCII 图 **68** 块；代码 **151** 块（python116/markdown16/xml11/yaml6/json2）；`{{...}}` 占位符 1 处（`{{query}}`，在 01_prompt_engineering.md，G4 保全）。相对链接照写（未译目标计 pending 是对的）。段锚点由 assemble 自动管理，不手写。

## 4 文件清单

| 文件（相对仓库根） | 任务 | 段 | 行区间 | sha256 | 图/码 |
|---|---|---:|---|---|---|
| `00_COURSE/00_mathematical_foundations/00_introduction.md` | M3-01 | 4 | 1-216 / 217-532 / 533-710 / 711-783 | ee875422d3b2ee8084d419e238d93465ef35e81307079d4af1867d218a65f0e5 | 图5 码4py |
| `00_COURSE/00_mathematical_foundations/01_context_formalization.md` | M3-01 | 5 | 1-682 / 683-852 / 853-1454 / 1455-1500 / 1501-1569 | f16d4cbf816367214127676b40daefe41cd66812dd74c4746801ee53deb6f0b2 | 图2 码9 |
| `00_COURSE/00_mathematical_foundations/02_optimization_theory.md` | M3-01 | 5 | 1-222 / 223-1192 / 1193-1233 / 1234-1351 / 1352-1376 | 47660bf429a075a0fc11d10daa11b795959a7549b9828da3d99ef9fd27080575 | 图1 码7 |
| `00_COURSE/00_mathematical_foundations/03_information_theory.md` | M3-01 | 4 | 1-897 / 898-1068 / 1069-1117 / 1118-1253 | 252c4b9c87ed0e26498d8d20b7659faac5b12f0de45d9fa97417fc4c607228dc | 图1 码7 |
| `00_COURSE/00_mathematical_foundations/04_bayesian_inference.md` | M3-01 | 5 | 1-196 / 197-1116 / 1117-1298 / 1299-1405 / 1406-1458 | 986f7ba7652fbb58eab3e6e30413dcb7d8b59192547a24ede4e45a72bf0133c5 | 图2 码7 |
| `00_COURSE/01_context_retrieval_generation/00_overview.md` | M3-02 | 3 | 1-109 / 110-1017 / 1018-1214 | a5b81f50d6a8d7186efb8af5a6d44ede051fb57790268dc110fd833ee0af6b1b | 图1 码7 |
| `00_COURSE/01_context_retrieval_generation/01_prompt_engineering.md` | M3-02 | 4 | 1-487 / 488-1100 / 1101-2755 / 2756-2794 | bc473bfb24495590def2097997f4b65ca786df2cb16e04955516c0eee65bf7c8 | 图0 码16 |
| `00_COURSE/01_context_retrieval_generation/02_external_knowledge.md` | M3-02 | 4 | 1-219 / 220-1033 / 1034-1574 / 1575-1578 | 9b1897cf265444076dce28375cbb13563894cfc836201e8159c76d12a28ae0ef | 图1 码8 |
| `00_COURSE/01_context_retrieval_generation/03_dynamic_assembly.md` | M3-02 | 3 | 1-371 / 372-1514 / 1515-1583 | 52afc520ab1c139af2f89252d9b0ad240a9304583c04ad71db1808ec51663dcf | 图1 码8 |
| `00_COURSE/01_context_retrieval_generation/case_studies/domain_specific_prompting.md` | M3-02 | 7 | 1-154 / 155-611 / 612-798 / 799-1516 / 1517-2026 / 2027-2130 / 2131-2248 | 2e4995c5048b5180d300c92d07c985c2d6e177a1d8620f61bed521a353168498 | 图13 码21 |
| `00_COURSE/01_context_retrieval_generation/case_studies/retrieval_optimization.md` | M3-02 | 6 | 1-129 / 130-838 / 839-1289 / 1290-2035 / 2036-2132 / 2133-2150 | f307fb41dfdd0987d4705989ed6304549cedfdb9e045735925761c2fd82e5bf7 | 图13 码16 |
| `00_COURSE/02_context_processing/00_overview.md` | M3-03 | 2 | 1-226 / 227-269 | 773a5c04bf1029633563cefb8e518c6b87f64201288e45f7ae3a3087a6e84e50 | 图5 码0 |
| `00_COURSE/02_context_processing/01_long_context_processing.md` | M3-03 | 4 | 1-132 / 133-513 / 514-1556 / 1557-2178 | b73c0e27dc264ac1a663b3a2a44dcec563e6b20a0f12732502a475cfb3a23056 | 图2 码5 |
| `00_COURSE/02_context_processing/02_self_refinement.md` | M3-03 | 4 | 1-155 / 156-615 / 616-1901 / 1902-2523 | 4f4355784f6765b7420fd878a7100b1b2936cff2380b85063012e7015bc9152a | 图2 码5 |
| `00_COURSE/02_context_processing/03_multimodal_context.md` | M3-03 | 2 | 1-1908 / 1909-1954 | 462c895d59ae312d9177285bcf656417d2f35c28b93284aedae34ca88c44517a | 图4 码3 |
| `00_COURSE/02_context_processing/04_structured_context.md` | M3-03 | 3 | 1-218 / 219-1251 / 1252-1313 | 80d758cfe76d627e45929650c1d9f61173464d3011e741836eb57060a547e2b7 | 图3 码2 |
| `00_COURSE/03_context_management/00_overview.md` | M3-04 | 3 | 1-243 / 244-657 / 658-779 | 5c5a34c467fa41b879707856ed0addca00110234396f88f61eee895ef66d6230 | 图2 码5 |
| `00_COURSE/03_context_management/01_fundamental_constraints.md` | M3-04 | 3 | 1-377 / 378-582 / 583-612 | 733238ef055ac18e94edb54620e3da793779011eed4b74fbcd10f42e7818f7a6 | 图2 码5 |
| `00_COURSE/03_context_management/02_memory_hierarchies.md` | M3-04 | 2 | 1-837 / 838-955 | eff4a37ffdce16718e8a2a71feb6a36db7fbf2438fc7e7789d641744e1cd3517 | 图1 码3 |
| `00_COURSE/03_context_management/03_compression_techniques.md` | M3-04 | 3 | 1-841 / 842-1193 / 1194-1212 | 51d8b7fe0dd3c57c612dfe8e96b017800abc42ab14539b6abbd19639c2777458 | 图6 码10 |
| `00_COURSE/03_context_management/04_optimization_strategies.md` | M3-04 | 3 | 1-867 / 868-1006 / 1007-1024 | 88c5d2b24655d106c05bcc08ef9d37eb8be3cfad1cbae62a3c4b5c9584b3f4ab | 图1 码3 |

## 5 术语

M2 冻结的译法全部沿用。GLOSSARY 84 条适用。课程正文新增高频：optimization=优化 / gradient=梯度 / entropy=熵 / bayesian=贝叶斯 / inference=推断 / retrieval=检索 / chunking=上下文切分 / compression=压缩 / assembly=装配。核心锚点：context=上下文（禁语境/情景）；prompt=提示词；token=词元；memory=记忆（禁内存）；agent=智能体；orchestration=编排；emergence=涌现；context assembly=上下文装配。

## 6 特别处理

1. **代码块语言多样（151 块）**：python/markdown/xml/yaml/json 全部原样保留标记与块内内容（含英文注释/prompt 模板），只译块外散文。G3 比对语言序列。
2. **ASCII 图 68 块**：图内一字不动（含图内英文），图下紧跟一行 `> 图：<中文说明> —— <原文关键词短语>`，不留空行。
3. **`{{query}}` 占位符**：`01_prompt_engineering.md` 1 处，G4 校验多重集相等，原样保留。
4. **6 篇 authored 空 README**：源为 1 字节换行（sha256 `01ba4719…`），依同目录正文撰写中文导读。front matter：`chunks: 0` / `chunks_done: []` / `status: authored` / source_sha256 用换行符哈希。**导读正文不能用 `##` 标题**（源 0 个 H2，G9 会判多出未授权 H2）——用 H1 + 加粗段落 + 列表。首 20 行须含原文锚点与 GLOSSARY 链接（层级从译文目录回到 zh/）。
5. **段锚点坑**：assemble 在每段前插 `<a id="chunk-N"></a>` 与 `<!-- chunk N/M | ... -->`，会使 G6 FAIL。assemble 后用正则删这两类行。
6. **多段文件 chunks_done 列全**：最多 7 段（domain_specific_prompting.md），front matter `chunks_done` 必须列全所有段号，漏列导致进度少算。

## 7 质量门禁

G1–G9 全部适用。硬指标 **0 FAIL**；G7 WARN 允许（代码块/DSL 原样保留所致，check 退出码 0）。每篇 `assemble.py --verify` 须 PASS 往返无损。6 篇 authored 导读同样须 9 PASS / 0 FAIL。

## 8 不要做的事

不改 `zh/GLOSSARY.yaml`（术语建议写进报告由人工定）；不碰 `zh/tools/`、`zh/PLAN/PLAN.md`、`zh/STYLE.md`；不改上游原文；不手写双语锚点、不删内部链接。`exercises/*.py`、`labs/*.py` 不在交付范围（manifest 收录 0 个 .py）。

## 9 完成判据

- `python zh/tools/manifest.py --check` 无漂移
- `python zh/tools/digits.py` 一致（242 篇 / 676 段 / 30 空）
- `python zh/tools/check.py --module M3` 27 文件 9 PASS / 0 FAIL
- `python zh/tools/progress.py` → M3 五行 published
- 数字：27 篇 / 79 段 / 6 空；图 68 / 码 151 / `{{...}}` 1 处

## 10 报告格式

`## 交付`（表：任务 / 文件 / 段 / 状态）+ `## 校验`（四命令表）+ `## 偏差`（逐条说明与 PLAN 不一致原因）+ `## 术语建议`（GLOSSARY 应增补/修改词 + 理由，不自行改 YAML）+ `## 下一步`（建议模块 + 遗留问题）。

## 11 建议顺序

1 读 §1 五份文件 + `python zh/tools/digits.py --list` 看数字 → 2 按任务组并行译 21 篇（M3-01 五篇 / M3-02 六篇 / M3-03 五篇 / M3-04 五篇），大文件单列 → 3 每篇走六步：写 chunk（chunk-01 含完整 front matter, chunks_done 列全段号）→ `assemble.py --out` → 正则删段锚点 → `assemble.py --verify` → `check.py` → 4 主 agent 写 6 篇 authored 导读 → 5 全模块回归四命令 → 6 按 §10 报告 → 7 提交 `feat(zh): 翻译 M3 课程·基础 21 篇 + 6 篇导读（M3-01/02/03/04）` 并推 `origin/zh/main`。
