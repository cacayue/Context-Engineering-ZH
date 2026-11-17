# M6_engineering_assets — 工程资产（自包含任务卡）

## 0 你的处境

- 仓库根 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering`
- 分支 **`zh/main`**（不切 `main`、不开 PR）；推送 `git push origin zh/main`；禁推 `upstream`、禁改 `zh/` 外文件。
- 前置 M0–M5 全 published。M2 冻结、M3/M4/M5 沿用的译法，M6 必须沿用。
- Python 3。本卡为交付留档 + 复现指南。

## 1 先读哪几份文件

1. `zh/prompts/M5_course_frontier.md` 全文（术语基准 + 六步流程 + 段锚点坑 + authored 导读写法）
2. `zh/PLAN/PLAN.md` §「M6 工程资产（89 段）」+ §0.3 空文件 authored 约定 + 「上游既有缺陷」表
3. `zh/STYLE.md`、`zh/GLOSSARY.md`、`zh/KNOWN_ISSUES.md`（G5 白名单）
4. 范文：任一 M5 译文 + `zh/00_COURSE/10_orchestration_capstone/README.md`（authored 导读样式）

## 2 交付物

- 61 篇 zh/ 镜像译文：M6-01 模板库 27 篇、M6-02 协议壳 10 篇、M6-03 零到一指南 1 篇、M6-04 示例工程 6 篇、M6-05 命令集 17 篇
- 2 篇 authored 空 README 中文导读：`60_protocols/schemas/README.md`、`60_protocols/shells/README.md`（`status: authored`，不计入覆盖率）

## 3 关键数字

M6 **63 篇 / 89 段 / 2 空**（61 篇译 89 段 + 2 篇 authored）；ASCII 图（无标记块）**275** 块；带 lang 代码块 **384** 块；6 篇围栏≥20。`{{...}}` 无。段锚点由 assemble 自动管理。

## 4 文件清单

各篇 sha256 / 段数 / 任务号见 `zh/manifest.json` 的 `module=M6` 条目；预切分元数据在 `/tmp/m6_segments/<源路径>/_meta.json`（含 sha256 全值）。

| 任务 | 目录 | 篇/段 | 特点 |
|---|---|---|---|
| M6-01 | `20_templates/PROMPTS/` | 27/37 | 26 个 `.agent.md`（`## [meta]` json 块 + `## [instructions]` md 块 + ASCII 图），`expert_guides.md` 8 段最大 |
| M6-02 | `60_protocols/` | 12/27 | `shells/*.shell.md` 各 2–4 段、33 块无 lang 围栏；2 篇 authored |
| M6-03 | `10_guides_zero_to_hero/` | 1/1 | README |
| M6-04 | `30_examples/00_toy_chatbot/` | 6/6 | 5 个 `.py.md`（源大、可译字节小 2–6KB） |
| M6-05 | `.claude/commands/` | 17/18 | 16 个 `.agent.md`（各 500–700B 可译） |

## 5 术语

M2–M5 冻结译法全部沿用。核心锚点：context=上下文（禁语境/情景）、prompt=提示词、token=词元、memory=记忆（禁内存）、agent=智能体（禁代理）、orchestration=编排（禁管弦/协奏，但 orchestra=交响乐团、concerto=协奏曲 是音乐术语例外）、retrieval=检索（禁召回）、chunk=片段、shell=协议壳、schema=模式、protocol=协议、field=场、attractor=吸引子、emergence=涌现（禁突现）、evaluation=评估（禁评测）、pattern=模式（禁图案）、feedback loop=反馈回路（禁反馈循环）。首次「中文（English）」，之后纯中文。

## 6 特别处理

1. **带 lang 块（json/yaml/python/md）**：语言标记原样（G3 比对语言序列），块内自然语言（如 `prompt_goal`、`description`）可译为中文（M2 `zh/CLAUDE.md` 先例），代码语法/变量/键名原样。
2. **无 lang 块（含 text kind、ASCII 图）**：整块原样保留英文/框图，G2 检查块内不得有全角字符。图注 `> 图：<中文说明> —— <原文关键词短语>` 放块**外**。`expert_guides.md` 33 块全无 lang——只译块外散文。
3. **`.agent.md` 结构**：`## [meta]` 内 json 块（prompt_goal 等自然语言译中文）、`## [instructions]` 内 md 块（自然语言可译）、`## [ascii_diagrams]` 无标记块（原样）。标题里的 `[meta]`/`[instructions]` 保留。
4. **伪链接坑**：`dict[key](args)` 被 G5 LINK_RE 误判，原文固有则在 `](` 后加半角空格破匹配（Python 语义不变）。
5. **2 篇 authored 空 README**：依同目录正文撰写中文导读。front matter `chunks:0`/`chunks_done:[]`/`status:authored`/`source_sha256=01ba4719…`。导读正文**不用 `##`**（源 0 个 H2，G9 判多出）——用 H1 + 加粗段落 + 列表。双语锚点：`60_protocols/schemas/README.md` 在 `zh/60_protocols/schemas/`，原文锚点 `../../../60_protocols/schemas/README.md`，GLOSSARY `../../GLOSSARY.md`（shells 同理）。
6. **段锚点坑**：assemble 插 `<a id="chunk-N"></a>` 与 `<!-- chunk N/M | ... -->` 使 G6 FAIL，assemble 后用正则删这两类行。
7. **多段文件 chunks_done 列全**：`expert_guides.md` 8 段、shells 各 4 段，front matter `chunks_done` 列全所有段号。

## 7 质量门禁

G1–G9 全适用，硬指标 **0 FAIL**；G7 WARN 允许（代码/DSL 原样所致，退出码 0）。每篇 `assemble.py --verify` 须 PASS。2 篇 authored 导读同样 9 PASS / 0 FAIL。

## 8 不要做的事

不改 `zh/GLOSSARY.yaml`（术语建议写报告由人工定）；不碰 `zh/tools/`、`zh/PLAN/PLAN.md`、`zh/STYLE.md`；不改上游原文；不手写双语锚点、不删内部链接。`.py` 注释不在交付范围（PLAN 提及但不计入验收数字）。

## 9 完成判据

- `python zh/tools/manifest.py --check` 无漂移
- `python zh/tools/digits.py` 一致（242 篇 / 676 段 / 30 空）
- `python zh/tools/check.py --module M6` 63 文件 9 PASS / 0 FAIL
- `python zh/tools/progress.py` → M6 五行 published（P3 published）
- 若 check 全绿但 progress 仍 todo：跑 `python zh/tools/manifest.py`（不带 --check）重算 status 缓存再 progress
- 数字：63 篇 / 89 段 / 2 空；图 275 / 码 384

## 10 报告格式

`## 交付`（表）+ `## 校验`（四命令表）+ `## 偏差`（逐条）+ `## 术语建议`（不自行改 YAML）+ `## 下一步`。

## 11 建议顺序

1 读 §1 → 2 写 2 篇 authored 导读 → 3 派 worker 只写 chunk（chunk-01 含完整 front matter, chunks_done 列全段号）→ 4 主 agent 统一装配（m6_assemble.py）→ 5 修 G1/G2/G9 → 6 四门禁 + manifest 重算 → 7 §10 报告 → 8 提交 `feat(zh): 翻译 M6 工程资产 61 篇 + 2 篇导读（M6-01/02/03/04/05）` 推 origin/zh/main。
