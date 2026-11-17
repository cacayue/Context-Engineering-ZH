# LAUNCH — M1 入口层

你是接手的执行 agent。**先读 `zh/prompts/M1_entry.md`，它是完整任务卡**
（含逐文件清单、六条模块专坑、九项门禁、完成判据、执行顺序）。本文件只是启动指令，不重复细节。

## 一句话任务

在 `/home/cacayue/Documents/Learning/AI_Engineer/Context-Engineering` 里，
把 M1 入口层的 **23 篇 / 40 段**英文原文译成中文，放到 `zh/` 镜像路径下。
从 `masterclass_content/` 的 8 篇开始（各 1 段，最小的完整闭环）。

## 硬约束（违反即返工）

| 约束 | 说明 |
|---|---|
| 分支 `zh/main` | 不要切到 `main`，不要开 PR |
| 只写 `zh/` 内文件 | 其他路径只读，包括 `zh/PLAN/PLAN.md`、`zh/STYLE.md`、`zh/GLOSSARY.yaml`、`zh/tools/*.py` |
| 推 `origin` 不推 `upstream` | `upstream` 是上游原项目，只读 |
| 代码块原样 | 24 块，含 `CLAUDE/GEMINI` 的 json 块；只译块内自然语言说明 |
| ASCII 图原样 | 40 块，图内一个字不动；图下可加中文图注 |
| 双语锚点不要手写 | `assemble.py` 按目录深度自动生成 |
| 不删内部链接 | 指向未译文件时 G5 会自动计入「待译」 |

## 数字验收

```
M1  23 篇   40 段   0 空
M1-01 5篇/11段   M1-02 2篇/8段   M1-03 5篇/8段   M1-04 8篇/8段   M1-05 3篇/5段
可译 170,007 B   图 40 块   代码 24 块   相对链接 28 处   {{...}} 0 处
```

## 必须跑的校验（全绿才算完成）

```bash
python zh/tools/manifest.py --check    # 无漂移
python zh/tools/digits.py              # 数字一致
python zh/tools/check.py --module M1   # G1–G9 全绿
python zh/tools/progress.py            # PROGRESS.md 的 M1 五行变 published
```

## 工具用法（唯一入口，别自己造）

```bash
python zh/tools/plan_chunks.py README.md            # 切分计划：行号区间 + 段 sha
python zh/tools/plan_chunks.py README.md --json     # 同上，机器读
python zh/tools/assemble.py README.md               # chunk → 单文件，自动插入锚点
python zh/tools/assemble.py README.md --verify      # 结构指纹比对
python zh/tools/check.py zh/README.md               # 单文件九项
python zh/tools/check.py zh/README.md --only G3,G9   # 只跑结构
```

chunk 放 `zh/.chunks/<源路径>/chunk-01.md`（已被 `.gitignore` 忽略，不要提交）。

## 六个最容易踩的坑（详版见任务卡 §6）

| 坑 | 一句话 |
|---|---|
| `CITATIONS` 三份不是副本 | v1 328 行 / v2 363 / v3 407，v2→v3 只重叠 1%，三份都要全译 |
| `CLAUDE.md` / `GEMINI.md` 不是重复文件 | H2 只有 1 个相同，行重叠 19%，差异部分才是内容 |
| `masterclass_content` 8 篇是 H1 + 3×H3，没有 H2 | 标题层级数量错会被 G3 抓 |
| `README.md` 前 6 个 H2 是徽章 | `[![alt](img)](url)` 结构原样，只译 `alt` |
| `STRUCTURE_v3.md` 有 14 张 ASCII 图 | 图内不动，图下加图注 |
| 指向 M2 的链接（14 处） | 照写，G5 会显示「待译 14 处」，这是对的 |

## 报告

按任务卡 §10 的格式：交付表 + 校验表 + 偏差 + 术语建议 + 下一步。
术语建议写进报告，**不要直接改 `zh/GLOSSARY.yaml`**——M1 是全书术语基准，
改动要人工确认。
