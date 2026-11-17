# LAUNCH — M0 基础设施

你是接手的执行 agent。**先读 `zh/prompts/M0_bootstrap.md`，它是完整任务卡**（500 行，含全部规格、CLI 契约、JSON schema、映射算法、验收判据）。本文件只是启动指令，不重复细节。

## 一句话任务

在 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering` 里建成 `zh/` 的中文化工具链：9 个文件，不写任何译文。

## 硬约束（违反即返工）

| 约束 | 说明 |
|---|---|
| 只写 `zh/` 内文件 + `.github/workflows/zh_checks.yml` | 其他路径一律只读，包括 `zh/PLAN/PLAN.md` |
| 仅标准库 | Python 3.14.4，禁止 pyyaml 等第三方依赖 |
| 不 commit / 不 push | 完成后交人工审查 |
| `upstream` 只读 | 只推 `origin`（且本任务不推） |
| 不译正文 | 那是 M1–M11 |

## 数字验收（算错就全错）

```
242 篇 .md        676 段        30 个空文件
M1 40  M2 11  M3 79  M4 35  M5 52  M6 89  M7 104  M8 204  M9 33  M10 29  M11 0
```

段 = `max(1, ceil(可译字节 / 6144))` 按文件累加。
可译字节 = 文件字节 − 有语言标记块 − 含框线 ASCII 图块。
围栏解析必须支持 `~~~`、4+ 反引号、0–3 空格缩进、未闭合（按到文末）。

## 交付清单

```
zh/GLOSSARY.yaml              60–100 词，7 个歧义词带 ambiguity
zh/STYLE.md                   R1–R7 + 12 条排版细则
zh/NOTICE                     MIT + davidkimai 署名
zh/tools/manifest.py          → zh/manifest.json
zh/tools/plan_chunks.py       单文件切分计划
zh/tools/assemble.py          chunk → 单文件，结构指纹往返校验
zh/tools/check.py             G1–G9，--self-test 必须 9/9
zh/tools/progress.py          → 重写 zh/PROGRESS.md（结构不变，数值替换）
zh/KNOWN_ISSUES.md            36 条失效链接
.github/workflows/zh_checks.yml   只监听 zh/**，禁 paths-ignore
```

## 执行顺序

```
1 读 zh/PLAN/PLAN.md §3 §5 §6 §7 + zh/PROGRESS.md §2（42 行期望值）
2 manifest.py  → 先跑通 242/676
3 check.py     → G3 G9 先做，再 G1 G2 G4 G6 G8，最后 G5 G7
4 plan_chunks.py + assemble.py → 段数与 manifest 交叉验证
5 progress.py  → 与现 zh/PROGRESS.md 章节结构一致
6 GLOSSARY.yaml / STYLE.md / NOTICE / KNOWN_ISSUES.md
7 zh_checks.yml
8 跑 §10 全部判据
```

## 报告

按 `zh/prompts/M0_bootstrap.md` §11 的格式：交付表 + 校验数字 + 与 PLAN.md 的偏差 + 下一步建议。不要复述代码。
