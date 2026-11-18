---
title: 阅读路径
status: active
version: v1.0
created: 2026-11-17
base_commit: 6158def
rule: 本文件是人工整理的学习导航；进度见 PROGRESS.md，计划见 PLAN/PLAN.md
---

# 阅读路径

上游仓库里有**三套互相矛盾**的阅读顺序：根 `README.md:217` 的 Learning Path、
`00_foundations/README.md:276` 的 Reading Order（按读者类型分 4 种）、
`00_COURSE/README.md` 的 12 周 4 阶段课程。三者覆盖范围不同，混用会绕路。

本文件把它们收拢成**一条主线 + 三条支线**，并标明每站的译文进度。

想离线阅读？[下载中文 PDF 或从当前译文重新导出](PDF.md)。

## 一句话

想快速能用 → 走 **A 线**（30 段，约 12 小时）。
想系统学会 → 走 **B 线**（主线全走完，676 段）。
想查某个概念 → 直接跳 **C 线**（参考手册，按需）。

## A 线 · 最快形成手感（30 段）

目标：能写出比「随便问一句」明显更好的提示词，理解为什么。

| 步 | 读什么 | 段 | 为什么 |
|---:|---|---:|---|
| 1 | `00_foundations/01_atoms_prompting.md` | 1 | 最小单元：任务 + 约束 + 输出格式 |
| 2 | `00_foundations/02_molecules_context.md` | 1 | 加示例，从「说」到「示范」 |
| 3 | `00_foundations/03_cells_memory.md` | 1 | 让模型记住上一轮 |
| 4 | `00_foundations/05_cognitive_tools.md` | 2 | 把推理过程外化成结构 |
| 5 | `20_templates/README.md` | 1 | 挑一个模板套自己的任务 |
| 6 | `30_examples/README.md` | 1 | 看完整项目长什么样 |
| 7 | `masterclass_content/` 8 篇 | 8 | 全库最省力的闭环，每篇 1 段 |
| 8 | `NOCODE/00_foundations/` 前 3 篇 | 15 | 无代码版，概念讲得更慢 |

合计 **30 段**，约全库 4.4%。走完再决定要不要走 B 线。

另外跑两个脚本（不占译文段数，代码原样保留）：
`10_guides_zero_to_hero/01_min_prompt.py`（自带假 LLM，可离线跑）、
`02_expand_context.py`（需 OpenAI key）。

**为什么不从 `00_COURSE/` 开始**：它是 62 篇 / 79 段的完整课程，第 1 篇就是数学基础。
A 线的目的不是学全，是先跑通一次。

## B 线 · 系统学完（676 段）

按 `zh/PLAN/PLAN.md` 的 P1–P6 阶段走，每阶段内部按模块顺序。

| 阶段 | 模块 | 段 | 累计 | 学完能做什么 |
|---|---|---:|---:|---|
| P1 | M1 入口 + M2 概念地基 | 51 | 51 | 知道这本书在讲什么，术语不再卡壳 |
| P2 | M3 课程基础 + M4 课程进阶 | 114 | 165 | 掌握检索、处理、管理、RAG、记忆五大块 |
| P3 | M6 工程资产 + M9 认知架构 | 122 | 287 | 有可复用的模板、协议、架构 |
| P4 | M5 课程前沿 + M7 参考手册 | 156 | 443 | 多智能体、场论、评估；查得到细节 |
| P5 | M8 无代码 | 204 | 647 | 不写代码也能落地 |
| P6 | M10 研究篇 + M11 写作 | 29 | 676 | 理论前沿与边界 |

**M8 为什么排 P5**：它 204 段占全库 30%，且与 M2 内容重叠（同一套
Atoms→Molecules→Cells→Organs）。M2 译完术语即冻结，M8 复用同一译法；
若先译 M8，M2 会被迫跟它的译法走，而 M2 是更权威的概念定义处。

## C 线 · 查阅（不进主线）

| 想查 | 去哪 |
|---|---|
| 某个术语怎么译 | [`GLOSSARY.md`](GLOSSARY.md) |
| 提示词模板 | `20_templates/` |
| 协议壳写法 | `60_protocols/` |
| 检索/索引细节 | `40_reference/retrieval_indexing.md` |
| 残差与涌现信号 | `40_reference/symbolic_residue_types.md`、`emergence_signatures.md` |
| 吸引子动力学 | `40_reference/attractor_dynamics.md` |
| token 预算 | `40_reference/token_budgeting.md` |
| 评估清单 | `40_reference/eval_checklist.md` |
| 字段 schema | `40_reference/schema_cookbook.md` |

## 三条线的关系

```
A 线 ──跑通一次──▶ 有手感
                    │
                    ▼
B 线 ──系统学完──▶ 能设计系统
                    │
                    ▼
C 线 ──按需查阅──▶ 能查漏补缺
```

A 线 30 段 ≈ 全库 4.4%。走完 A 线再决定要不要走 B 线，比一开始就下决心走完
676 段更现实。

## 阅读时配合做三件事

| 做法 | 为什么 |
|---|---|
| 每读完一篇，用自己的话写 3 行摘要 | 本书概念密度高，不输出就会「读完了但说不出来」 |
| 遇到代码块，先只读注释和输出样例 | 代码块占全库 43%，逐行读会淹没重点 |
| 遇到 ASCII 图，先看中文图注再看原图 | 图的框线是英文排版，中文图注给出结构 |

## 进度

实时进度见 [`PROGRESS.md`](PROGRESS.md)。本文件只给路线，不记进度。
