# M5_course_frontier — 课程·前沿（自包含任务卡）

## 0 你的处境

- 仓库根 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering`
- 分支 **`zh/main`**（不要切 `main`，不要开 PR）；推送 `git push origin zh/main`；禁止推 `upstream`、改 `zh/` 之外文件。
- 前置：M0–M4 均已 published。M2 冻结、M3/M4 沿用的译法，M5 必须沿用。
- Python 3。本卡为实际执行的交付留档 + 复现指南。

## 1 先读哪几份文件

1. `zh/prompts/M4_course_advanced.md` 全文（术语基准 + 六步流程 + 段锚点坑 + authored 导读写法）
2. `zh/PLAN/PLAN.md` §「M5 课程·前沿（52 段）」+ §0.3 空文件 authored 约定 + 「上游既有缺陷」表
3. `zh/STYLE.md` 全文、`zh/GLOSSARY.md` 全文（G1 查禁用译法零命中）
4. `zh/KNOWN_ISSUES.md`（G5 白名单）
5. 范文：任一 M4 译文（front matter + 图注 + 双语锚点样式）+ `zh/00_COURSE/04_retrieval_augmented_generation/README.md`（authored 导读样式）

## 2 交付物

- 13 个 zh/ 镜像译文：M5-01 多智能体 4 篇、M5-02 场论 4 篇、M5-03 评估 4 篇、M5-04 编排毕业设计 1 篇
- 4 篇 authored 空 README 的中文导读（每个模块 README；`status: authored`，不计入覆盖率）

## 3 关键数字

M5 **17 篇 / 52 段 / 4 空**（13 篇译 52 段 + 4 篇 authored）；可译 282,097 B；ASCII 图 **23** 块；代码 **111** 块；相对链接照写（未译目标计 pending 是对的）。段锚点由 assemble 自动管理，不手写。`{{...}}` 无。

## 4 文件清单

| 文件（相对仓库根） | 任务 | 段 | 行区间 | sha256 | 图/码 |
|---|---|---:|---|---|---|
| `00_COURSE/07_multi_agent_systems/00_communication_protocols.md` | M5-01 | 1 | 1-529 | `9d5c9be74702cc19f8dc1fe60fce757fe853b63a88ece85af5c9cee4f7801854` | 图7 码17 |
| `00_COURSE/07_multi_agent_systems/01_orchestration_mechanisms.md` | M5-01 | 4 | 1-223/224-676/677-1100/1101-1210 | `46a9aca3fc5b0db351787ba3c82bb88a3635dafb04c008a71b684d5d608a5112` | 图2 码12 |
| `00_COURSE/07_multi_agent_systems/02_coordination_strategies.md` | M5-01 | 4 | 1-178/179-857/858-1866/1867-1987 | `bf539aab05de47c31c9f3f8f4c4c2fb199950a67d38cea3a7afda3f8455c0c0d` | 图0 码13 |
| `00_COURSE/07_multi_agent_systems/03_emergent_behaviors.md` | M5-01 | 3 | 1-1089/1090-2766/2767-2830 | `dd83c22008bf3508dfda3dfbc5d3b6ece7d769045dd0d61fcfb87912e31f53d2` | 图0 码12 |
| `00_COURSE/07_multi_agent_systems/README.md` | M5-01 | 0 | authored | `01ba4719…`（换行符） | 导读 |
| `00_COURSE/08_field_theory_integration/00_neural_field_foundations.md` | M5-02 | 5 | 1-236/237-1118/1119-1327/1328-1810/1811-1814 | `a2d58b746bcafa77656794120d84d2384bd56e496afa71e47c0893d8717a19dd` | 图0 码7 |
| `00_COURSE/08_field_theory_integration/01_attractor_dynamics.md` | M5-02 | 4 | 1-57/58-118/119-1519/1520-1621 | `45484a98b487549df281d8e8f4fcb4007737e4c714a6aa1289617aaaf546ae7f` | 图0 码6 |
| `00_COURSE/08_field_theory_integration/02_field_resonance.md` | M5-02 | 4 | 1-87/88-1118/1119-1258/1259-1264 | `be6c38cbd78243c68c0ea8e9f85a0c4c573d34fa9bbfebd33b992d555b98edb2` | 图0 码6 |
| `00_COURSE/08_field_theory_integration/03_boundary_management.md` | M5-02 | 3 | 1-87/88-1327/1328-1473 | `4fcdcac6f65e50224b138abd201572c0051a4cac5c4dabffbc4627b3a090f8e5` | 图0 码6 |
| `00_COURSE/08_field_theory_integration/README.md` | M5-02 | 0 | authored | `01ba4719…`（换行符） | 导读 |
| `00_COURSE/09_evaluation_methodologies/00_evaluation_frameworks.md` | M5-03 | 5 | 1-96/97-1296/1297-1458/1459-2168/2169-2548 | `5146bd84ebdbd6ef70cee62b58f1eab564bf2c72f9379f7fa596cd4dbde56a95` | 图2 码12 |
| `00_COURSE/09_evaluation_methodologies/01_component_assessment.md` | M5-03 | 4 | 1-84/85-1632/1633-2854/2855-2858 | `d711e18f78bda5568e5405ee052bc7355c29f198d610d0507c5d17b5fecd87de` | 图1 码7 |
| `00_COURSE/09_evaluation_methodologies/02_system_integration.md` | M5-03 | 3 | 1-96/97-306/307-1489 | `3d1e4290e3ba57d6000688c36e24801f53cb91accecf122ab3521ea1446fb26b` | 图1 码5 |
| `00_COURSE/09_evaluation_methodologies/03_benchmark_design.md` | M5-03 | 4 | 1-73/74-1001/1002-1334/1335-1338 | `44a53d5e9d96d1dcb9ae200f470dcd232162222942c625340742f9c3b91bbc9f` | 图1 码3 |
| `00_COURSE/09_evaluation_methodologies/README.md` | M5-03 | 0 | authored | `01ba4719…`（换行符） | 导读 |
| `00_COURSE/10_orchestration_capstone/00_capstone_overview.md` | M5-04 | 8 | 1-221/222-637/638-923/924-1055/1056-1170/1171-1229/1230-1306/1307-1324 | `be29ff6be862b8ef11def6a5eaf93bf01d6bf085506c68a79a475c897bd6ec70` | 图9 码5 |
| `00_COURSE/10_orchestration_capstone/README.md` | M5-04 | 0 | authored | `01ba4719…`（换行符） | 导读 |

## 5 术语

M2/M3/M4 冻结译法全部沿用。新增高频：multi-agent system=多智能体系统、communication protocol=通信协议、orchestration=编排、coordination=协调、emergence=涌现（禁突现）、attractor=吸引子、neural field=神经场、field resonance=场共振、boundary management=边界管理、evaluation=评估（禁评测/评价）、benchmark=基准、metric=指标、grounding=落地依据、capstone=毕业设计、agent=智能体（禁代理）、shell=协议壳、context assembly=上下文装配。核心锚点：context=上下文（禁语境/情景）；prompt=提示词；token=词元；retrieval=检索（禁召回）；chunk=片段。首次出现可「中文（English）」，之后纯中文。

## 6 特别处理

1. **代码块语言多样（111 块）**：python/json/markdown 等原样保留标记与块内内容（含英文注释/prompt 模板），只译块外散文。G3 比对语言序列。
2. **ASCII 图 23 块**：图内一字不动（含图内英文），图下紧跟一行 `> 图：<中文说明> —— <原文关键词短语>`，不留空行。
3. **无标记围栏（含 text kind）原样保留英文**：G2 检查所有无语言标记围栏内不得有全角字符。若图注，必须放在围栏**外**。
4. **伪链接坑**：Python `dict[key](args)`（如 `protocols[protocol_name](**kwargs)`）会被 G5 的 LINK_RE 误判为失效链接。原文固有，按 M2/M4 先例在 `](` 后加半角空格（Python 语义不变）破匹配。
5. **4 篇 authored 空 README**：依同目录正文撰写中文导读。front matter：`chunks: 0` / `chunks_done: []` / `status: authored` / source_sha256 用换行符哈希 `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b`。导读正文**不能用 `##` 标题**（源 0 个 H2，G9 判多出未授权 H2）——用 H1 + 加粗段落 + 列表。首 20 行须含原文锚点与 GLOSSARY 链接（层级从译文目录回到 zh/，本模块在 `zh/00_COURSE/0X_xxx/`，原文锚点用 `../../../00_COURSE/0X_xxx/README.md`，GLOSSARY 用 `../../GLOSSARY.md`）。
6. **段锚点坑**：assemble 在每段前插 `<a id="chunk-N"></a>` 与 `<!-- chunk N/M | ... -->`，使 G6 FAIL。assemble 后用正则删这两类行。
7. **多段文件 chunks_done 列全**：最多 8 段（capstone_overview），front matter `chunks_done` 必须列全所有段号。

## 7 质量门禁

G1–G9 全部适用。硬指标 **0 FAIL**；G7 WARN 允许（代码块/DSL 原样保留所致，check 退出码 0）。每篇 `assemble.py --verify` 须 PASS 往返无损。4 篇 authored 导读同样须 9 PASS / 0 FAIL。

## 8 不要做的事

不改 `zh/GLOSSARY.yaml`（术语建议写进报告由人工定）；不碰 `zh/tools/`、`zh/PLAN/PLAN.md`、`zh/STYLE.md`；不改上游原文；不手写双语锚点、不删内部链接。`.py` 不在交付范围。

## 9 完成判据

- `python zh/tools/manifest.py --check` 无漂移
- `python zh/tools/digits.py` 一致（242 篇 / 676 段 / 30 空）
- `python zh/tools/check.py --module M5` 17 文件 9 PASS / 0 FAIL
- `python zh/tools/progress.py` → M5 任务行 published
- **重要**：check 全绿但 progress 仍 todo 时，须跑 `python zh/tools/manifest.py`（不带 --check）重算 manifest.json 的 status 缓存，再跑 progress.py。
- 数字：17 篇 / 52 段 / 4 空；图 23 / 码 111

## 10 报告格式

`## 交付`（表：任务 / 文件 / 段 / 状态）+ `## 校验`（四命令表）+ `## 偏差`（逐条说明与 PLAN 不一致原因）+ `## 术语建议`（GLOSSARY 应增补/修改词 + 理由，不自行改 YAML）+ `## 下一步`（建议模块 + 遗留问题）。

## 11 建议顺序

1 读 §1 五份文件 → 2 预切分 13 篇到 seg（复用 m4_split.py 改 M5）→ 3 派 worker 只写 chunk（chunk-01 含完整 front matter, chunks_done 列全段号）→ 4 主 agent 统一装配（assemble --out → 正则删段锚点 → --verify → check.py）→ 5 主 agent 写 4 篇 authored 导读 → 6 全模块回归四命令 + manifest 重算 → 7 按 §10 报告 → 8 提交 `feat(zh): 翻译 M5 课程·前沿 13 篇 + 4 篇导读（M5-01/02/03/04）` 并推 `origin/zh/main`。
