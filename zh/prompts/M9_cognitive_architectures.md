# M9_cognitive_architectures — 认知架构（自包含任务卡）

## 0 你的处境
仓库根 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering`。分支 **`zh/main`**（不切 main、不开 PR），推 `git push origin zh/main`，禁推 upstream、禁改 zh/ 外文件。前置 M0–M6 全 published；M2 冻结译法、M3–M6 沿用译法 M9 必须沿用。Python 3。

## 1 先读哪几份文件
1. `zh/prompts/M6_engineering_assets.md`（术语基准 + 六步流程 + 段锚点坑 + authored 导读写法 + G2 围栏坑）
2. `zh/PLAN/PLAN.md` §「M9 认知架构（33 段）」+ §0.3 空文件 authored 约定 + 「上游既有缺陷」表
3. `zh/STYLE.md`、`zh/GLOSSARY.md`、`zh/KNOWN_ISSUES.md`
4. 范文：任一 M6 译文 + 任一 M6 authored 导读（`zh/60_protocols/shells/README.md`）

## 2 交付物
- 21 篇 zh/ 镜像译文：M9-01 架构总览 9 篇、M9-02 模式与模板 10 篇、M9-03 程序库 2 篇
- 4 篇 authored 空 README 中文导读：`cognitive-tools/cognitive-architectures/README.md`、`cognitive-schemas/README.md`、`cognitive-templates/README.md`、`cognitive-programs/README.md`

## 3 关键数字
M9 **25 篇 / 33 段 / 4 空**（21 篇译 33 段 + 4 篇 authored）；ASCII 图（无 lang 块）**103** 块；带 lang 代码块 **328** 块。段锚点由 assemble 自动管理。`{{...}}` 无。

## 4 文件清单
各篇 sha256 / 段数 / task 见 `zh/manifest.json` 的 `module=M9` 条目；预切分元数据在 `/tmp/m9_segments/<源路径>/_meta.json`。

| 任务 | 目录 | 篇/段 | 特点 |
|---|---|---|---|
| M9-01 | `cognitive-tools/README.md` + `cognitive-architectures/` | 10/17 | 9 篇架构（interpretability 3 段最大），1 authored |
| M9-02 | `cognitive-schemas/` 7 篇 + `cognitive-templates/` 5 篇 | 12/14 | schema/template 定义，2 authored |
| M9-03 | `cognitive-programs/` 3 篇 | 3/2 | 2 篇实体 + 1 authored |

## 5 术语
M2–M8 冻结译法全部沿用。核心锚点：context=上下文、prompt=提示词、token=词元、memory=记忆、agent=智能体、cognitive tool=认知工具、architecture=架构、schema=模式、template=模板、field=场、attractor=吸引子、quantum=量子、interpretability=可解释性、reconstruction=重构、orchestration=编排（orchestra=交响乐团例外）、resonance=共振、self-repair=自修复、emergence=涌现、feedback loop=反馈回路。首次「中文（English）」，之后纯中文。

## 6 特别处理
1. **带 lang 块（json/yaml/python/md）**：语言标记原样（G3），块内自然语言可译、代码语法/键名/占位符原样（M2 `zh/CLAUDE.md` 先例）。
2. **无 lang 块（含 ASCII 图/示例）**：整块原样保留英文/框图，G2 检查块内不得有全角字符；图注放块外一行 `> 图：<中文说明> —— <原文关键词短语>`。
3. **G2 上游缺陷先例**：若原文把英文标题（如 `## Variations`）包在无 lang 围栏内，worker 译成中文会触发 G2——必须还原英文（`/tmp/m6_restore_chunk.py` 按序号用原文块体替换 chunk 中含 CJK 块）。**修复必须落实到 chunk 文件**，否则全量 assemble 会覆盖译文修复。
4. **H2 数量对齐**：标题译半角 `##`，不得用全角 `＃＃`（M6 踩过 G9 FAIL）。
5. **4 篇 authored 空 README**：front matter `chunks:0`/`chunks_done:[]`/`status:authored`/`source_sha256=01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b`（换行符哈希）；导读正文**不用 `##`**（源 0 个 H2，G9 判多出）——用 H1 + 加粗段落 + 列表。双语锚点：本模块在 `zh/cognitive-tools/<子目录>/`，原文锚点 `../../../cognitive-tools/<子目录>/README.md`，GLOSSARY `../../GLOSSARY.md`。
6. **段锚点坑**：assemble 插段锚点使 G6 FAIL，assemble 后用正则删。
7. **多段文件 chunks_done 列全**：interpretability 3 段、多数 2 段，front matter `chunks_done` 列全。

## 7 质量门禁
G1–G9 全适用，硬指标 **0 FAIL**；G7 WARN 允许（代码/DSL 原样所致）。每篇 `assemble.py --verify` PASS。4 篇 authored 导读同样 9 PASS / 0 FAIL。

## 8 不要做的事
不改 `zh/GLOSSARY.yaml`（术语建议写报告由人工定）；不碰 `zh/tools/`、`zh/PLAN/PLAN.md`、`zh/STYLE.md`；不改上游原文；不手写双语锚点、不删内部链接。`.py` 注释不在交付范围。

## 9 完成判据
- `python zh/tools/manifest.py --check` 无漂移（242 篇 / 676 段 / 30 空）
- `python zh/tools/digits.py` 一致
- `python zh/tools/check.py --module M9` 25 文件 9 PASS / 0 FAIL
- `python zh/tools/progress.py` → M9 三行 published（P3 published）
- check 全绿但 progress todo 时跑 `python zh/tools/manifest.py`（不带 --check）重算 status
- 数字：25 篇 / 33 段 / 4 空；图 103 / 码 328

## 10 报告格式
`## 交付`（表）+ `## 校验`（四命令表）+ `## 偏差`（逐条）+ `## 术语建议`（不自行改 YAML）+ `## 下一步`。

## 11 建议顺序
1 读 §1 → 2 写 4 篇 authored 导读 → 3 派 worker 只写 chunk（chunk-01 含完整 front matter, chunks_done 列全）→ 4 主 agent 统一装配（m9_assemble.py）→ 5 修 G1/G2/G9 → 6 四门禁 + manifest 重算 → 7 §10 报告 → 8 提交 `feat(zh): 翻译 M9 认知架构 21 篇 + 4 篇导读（M9-01/02/03）` 推 origin/zh/main。
