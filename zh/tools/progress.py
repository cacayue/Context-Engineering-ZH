#!/usr/bin/env python3
"""读 zh/manifest.json，重写 zh/PROGRESS.md（任务卡 §7.7）。

用法：
    python zh/tools/progress.py            # 读 manifest.json，重写 zh/PROGRESS.md
    python zh/tools/progress.py --stdout   # 不写文件，只打印

约束：逐字保持 zh/PROGRESS.md 现有的章节结构与表格列（§0–§6），
只替换数字与状态。数值唯一来源 = manifest.json（其源头是各译文 front matter
的 chunks_done / status）。

仅用标准库。
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import zmap

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFEST = os.path.join(REPO, "zh", "manifest.json")
PROGRESS = os.path.join(REPO, "zh", "PROGRESS.md")

# 模块 → 任务数（M0 的 9 个任务是工具链自身，不入 manifest）
MODULE_TASKS = {"M0": 9}
for _t in zmap.TASK_NAMES:
    _m = _t.split("-")[0]
    MODULE_TASKS[_m] = MODULE_TASKS.get(_m, 0) + 1

M0_DELIVERABLES = [
    "zh/GLOSSARY.yaml",
    "zh/GLOSSARY.md",
    "zh/STYLE.md",
    "zh/NOTICE",
    "zh/LEARNING_PATH.md",
    "zh/KNOWN_ISSUES.md",
    "zh/manifest.json",
    "zh/tools/manifest.py",
    "zh/tools/plan_chunks.py",
    "zh/tools/assemble.py",
    "zh/tools/check.py",
    "zh/tools/progress.py",
    "zh/tools/glossary_md.py",
    ".github/workflows/zh_checks.yml",
]


def _m0_complete():
    """M0 完工判据 = 全部交付物存在。"""
    return all(os.path.exists(os.path.join(REPO, p)) for p in M0_DELIVERABLES)


# §2「备注」列：编辑性文字，非数值。手写一次，随规范演进。
TASK_NOTES = {
    "M1-04": "**推荐起点**",
    "M3-01": "2 篇 `authored`",
    "M3-02": "2 篇 `authored`",
    "M3-03": "1 篇 `authored`",
    "M3-04": "1 篇 `authored`",
    "M4-01": "1 篇 `authored`",
    "M4-03": "1 篇 `authored`",
    "M5-01": "1 篇 `authored`",
    "M5-02": "1 篇 `authored`",
    "M5-03": "1 篇 `authored`",
    "M5-04": "1 篇 `authored`",
    "M6-01": "含 26 个 `.agent.md`",
    "M6-02": "2 篇 `authored`",
    "M6-03": "+ 7 个 .py 注释",
    "M6-04": "含 5 个 `.py.md`",
    "M7-01": "4 篇 >120KB",
    "M7-02": "1218+760 行图",
    "M7-03": "838 行图",
    "M8-01": "与 M2 重叠，复用术语",
    "M8-02": "含 123KB 单篇",
    "M8-03": "最大单任务",
    "M8-04": "全部 `authored`",
    "M8-05": "2 篇 `authored`",
    "M10-03": "149KB 系统提示词（正文仅 2KB 可译）",
    "M11-01": "全部 `authored`",
}

# §3 里程碑：阶段 → 模块组合
MILESTONES = [
    ("P1", ["M1", "M2"]),
    ("P2", ["M3", "M4"]),
    ("P3", ["M6", "M9"]),
    ("P4", ["M5", "M7"]),
    ("P5", ["M8"]),
    ("P6", ["M10", "M11"]),
]

# 入口推荐：P1 之前先把「最省力入口」做掉（规范 §0 的既定顺序）
PREFERRED_START = "M1-04"

STATUS_COUNTED = ("draft", "review", "published")


# ─── 数据 ──────────────────────────────────────────────────────────────────
def load_manifest(path=MANIFEST):
    if not os.path.isfile(path):
        print("缺少 %s，请先运行 python zh/tools/manifest.py" % os.path.relpath(path, REPO), file=sys.stderr)
        raise SystemExit(2)
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def aggregate(data):
    """按模块 / 任务聚合 篇 段 空 完成段 状态。"""
    per_mod = {m: {"files": 0, "chunks": 0, "empty": 0, "done": 0, "statuses": {}} for m in zmap.MODULES}
    per_task = {
        t: {"files": 0, "chunks": 0, "empty": 0, "done": 0, "statuses": {}}
        for t in zmap.TASK_NAMES
    }
    for e in data["files"]:
        done = len(e.get("chunks_done") or [])
        for bucket in (per_mod.get(e["module"]), per_task.get(e["task"])):
            if bucket is None:
                continue
            bucket["files"] += 1
            bucket["chunks"] += e["chunks"]
            bucket["empty"] += 1 if e.get("authored") else 0
            bucket["done"] += done
            st = e.get("status") or "todo"
            bucket["statuses"][st] = bucket["statuses"].get(st, 0) + 1
    return per_mod, per_task


def rollup_status(bucket):
    """模块/任务的汇总状态（与 §4 状态机一致）。

    规则：全部 published → published；一段未动且无发布 → todo；
    段已译完但未全发布 → review 或 draft；其余 → draft。
    `authored`（无原文）不计入完成，所以全 authored 的任务仍是 todo。
    """
    st = bucket["statuses"]
    files = sum(st.values())
    pub = st.get("published", 0)
    rev = st.get("review", 0)
    if st.get("sync-needed"):
        return "sync-needed"
    if files and pub == files:
        return "published"
    if bucket["done"] == 0 and pub == 0:
        return "todo"
    if bucket["chunks"] and bucket["done"] >= bucket["chunks"]:
        return "review" if rev else "published"
    return "draft"


def pct(done, total):
    if total <= 0:
        return "0%"
    return "%.0f%%" % (100.0 * done / total)


def overall(data, per_mod, per_task):
    files = data["totals"]["files"]
    chunks = data["totals"]["chunks"]
    authored = data["totals"]["authored"]
    done = data["totals"]["chunks_done"]
    published = data["totals"]["published"]
    mods_done = sum(1 for m in zmap.MODULES if per_mod[m]["done"] >= per_mod[m]["chunks"] and per_mod[m]["chunks"] > 0)
    tasks_done = sum(
        1 for t, b in per_task.items() if b["chunks"] > 0 and b["done"] >= b["chunks"]
    )
    return {
        "files": files,
        "chunks": chunks,
        "authored": authored,
        "done": done,
        "published": published,
        "writable": files - authored,
        "coverage": (100.0 * done / chunks) if chunks else 0.0,
        "mods_done": mods_done,
        "mods_total": len(zmap.MODULES),
        "tasks_done": tasks_done,
        "tasks_total": len(zmap.TASK_NAMES),
    }


def next_task(per_task):
    """下一步：优先既定入口，完成后取里程碑序内「段数最小且未完成」的任务。"""
    pref = per_task.get(PREFERRED_START)
    if pref and pref["done"] < pref["chunks"]:
        return PREFERRED_START, "全仓最省力入口"
    for stage, mods in MILESTONES:
        cands = [
            (t, b)
            for t, b in per_task.items()
            if t.split("-")[0] in mods and b["chunks"] > b["done"] and b["chunks"] > 0
        ]
        if cands:
            cands.sort(key=lambda kv: (kv[1]["chunks"], kv[0]))
            return cands[0][0], "%s 里程碑内最小任务" % stage
    return None, ""


# ─── 渲染 ──────────────────────────────────────────────────────────────────
def render(data, per_mod, per_task, prev_history=None):
    ov = overall(data, per_mod, per_task)
    today = datetime.now().strftime("%Y-%m-%d")
    gen_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    base = data.get("base_commit") or ""
    L = []

    L.append("---")
    L.append("title: 中文化进度表")
    L.append("status: active")
    L.append("version: v1.0")
    L.append("generated_by: zh/tools/progress.py")
    L.append("generated_at: %s" % gen_at)
    L.append("created: 2026-11-17")
    L.append("base_commit: %s" % base)
    L.append("rule: 本文件由脚本生成，禁止手改；手改后与 manifest.json 脱节即失效")
    L.append("---")
    L.append("")
    L.append("# 中化进度表")
    L.append("")
    L.append("> 唯一真相 = 每个译文 front matter 的 `chunks_done` + `status`。")
    L.append("> 本表是它的只读投影。手改无效，下一次 `progress.py` 会覆盖。")
    L.append("")

    # ── §0 ──
    nxt, hint = next_task(per_task)
    L.append("## 0. 一眼看全局")
    L.append("")
    L.append("| 指标 | 当前 | 目标 |")
    L.append("|---|---:|---:|")
    L.append("| 源文件 | %d | %d |" % (ov["files"], ov["files"]))
    L.append("| 总段数 | **%d** | %d |" % (ov["chunks"], ov["chunks"]))
    L.append("| 已完成段 | **%d** | %d |" % (ov["done"], ov["chunks"]))
    L.append("| 覆盖率 | **%.1f%%** | 100%% |" % ov["coverage"])
    L.append("| 已发布文件 | %d | %d |" % (ov["published"], ov["writable"]))
    L.append("| 待写作（`authored`） | %d | %d |" % (
        sum(1 for e in data["files"] if e.get("authored") and e.get("status") == "published"),
        ov["authored"],
    ))
    L.append("| 模块完成 | %d / %d | %d / %d |" % (ov["mods_done"], ov["mods_total"], ov["mods_total"], ov["mods_total"]))
    L.append(
        "| 任务完成 | %d / %d | %d / %d |"
        % (ov["tasks_done"], ov["tasks_total"], ov["tasks_total"], ov["tasks_total"])
    )
    L.append(
        "| 工具链任务（M0） | %d / %d | %d / %d |"
        % (MODULE_TASKS.get("M0", 0), MODULE_TASKS.get("M0", 0),
           MODULE_TASKS.get("M0", 0), MODULE_TASKS.get("M0", 0))
    )
    L.append("")
    if nxt:
        b = per_task[nxt]
        L.append(
            "**下一步**：`%s` %s（%d 段，%s）"
            % (nxt, zmap.TASK_NAMES.get(nxt, ""), b["chunks"], hint)
        )
    else:
        L.append("**下一步**：**全部完成**")
    L.append("")
    L.append("---")
    L.append("")

    # ── §1 ──
    L.append("## 1. 模块进度")
    L.append("")
    L.append("| 模块 | 名称 | 任务 | 篇 | 段 | 空 | 段完成 | 进度 | 状态 |")
    L.append("|---|---|---:|---:|---:|---:|---:|---:|---|")
    m0_done = _m0_complete()
    L.append(
        "| **M0** | %s | %d | — | 0 | — | 0 | — | `%s` |"
        % (
            zmap.MODULE_NAMES.get("M0", ""),
            MODULE_TASKS.get("M0", 0),
            "done" if m0_done else "todo",
        )
    )
    tot_files = tot_chunks = tot_empty = tot_done = 0
    tot_tasks = MODULE_TASKS.get("M0", 0)  # 合计含 M0 的 9 个工具链任务
    for m in zmap.MODULES:
        b = per_mod[m]
        tot_tasks += MODULE_TASKS.get(m, 0)
        tot_files += b["files"]
        tot_chunks += b["chunks"]
        tot_empty += b["empty"]
        tot_done += b["done"]
        L.append(
            "| **%s** | %s | %d | %d | %d | %d | %d | %s | `%s` |"
            % (
                m,
                zmap.MODULE_NAMES.get(m, ""),
                MODULE_TASKS.get(m, 0),
                b["files"],
                b["chunks"],
                b["empty"],
                b["done"],
                pct(b["done"], b["chunks"]),
                rollup_status(b),
            )
        )
    L.append(
        "| | **合计** | **%d** | **%d** | **%d** | **%d** | **%d** | **%s** | |"
        % (tot_tasks, tot_files, tot_chunks, tot_empty, tot_done, pct(tot_done, tot_chunks))
    )
    L.append("")
    L.append("> 段 = max(1, ⌈可译字节 ÷ 6144⌉)，按文件累加 = **%d**。" % tot_chunks)
    L.append("> 不用「总体积 ÷ 6144」= 563（忽略\"每文件至少一次调用\"），也不用按模块聚合 = 567。")
    L.append("> **%d 是真实调用次数，也是唯一进度口径。**" % tot_chunks)
    L.append("")
    L.append("---")
    L.append("")

    # ── §2 ──
    L.append("## 2. 任务进度（%d 项）" % len(zmap.TASK_NAMES))
    L.append("")
    L.append("| 任务 | 名称 | 篇 | 段 | 空 | 完成段 | 状态 | 备注 |")
    L.append("|---|---|---:|---:|---:|---:|---|---|")
    for t in zmap.TASK_NAMES:
        b = per_task[t]
        note = TASK_NOTES.get(t, "")
        L.append(
            "| `%s` | %s | %d | %d | %d | %d / %d | `%s` | %s|"
            % (
                t,
                zmap.TASK_NAMES[t],
                b["files"],
                b["chunks"],
                b["empty"],
                b["done"],
                b["chunks"],
                rollup_status(b),
                (note + " ") if note else "",
            )
        )
    L.append("")
    L.append("---")
    L.append("")

    # ── §3 ──
    L.append("## 3. 里程碑")
    L.append("")
    L.append("| 阶段 | 模块 | 段 | 累计 | 状态 |")
    L.append("|---|---|---:|---:|---|")
    acc = 0
    for stage, mods in MILESTONES:
        segs = [per_mod[m]["chunks"] for m in mods]
        acc += sum(segs)
        if len(segs) == 1:
            seg_txt = str(segs[0])
        else:
            seg_txt = " + ".join(str(s) for s in segs) + " = %d" % sum(segs)
        done = sum(per_mod[m]["done"] for m in mods)
        st = "published" if done >= sum(segs) else ("draft" if done else "todo")
        L.append("| %s | %s | %s | %d | `%s` |" % (stage, " + ".join(mods), seg_txt, acc, st))
    L.append("")
    L.append("> P1 完成 = 可以开始中文学习（入口 + 概念地基齐全）。")
    L.append("")
    L.append("---")
    L.append("")

    # ── §4 状态机（静态） ──
    L.append("## 4. 状态机")
    L.append("")
    L.append("```text")
    L.append("todo ──▶ draft ──▶ review ──▶ published")
    L.append("  ▲                       │")
    L.append("  └──── sync-needed ◀─────┘   (上游 sha 变化)")
    L.append("authored：无原文，todo ──▶ published")
    L.append("```")
    L.append("")
    L.append("| 状态 | 含义 | 计入覆盖率 |")
    L.append("|---|---|---|")
    L.append("| `todo` | 未开始 | 否 |")
    L.append("| `draft` | 段已译完，未自检 | 是 |")
    L.append("| `review` | 自检通过，待二次校对 | 是 |")
    L.append("| `published` | 校对完成 | 是 |")
    L.append("| `authored` | 无原文，AI 原创 | 否 |")
    L.append("| `sync-needed` | 上游变了，原译文保留 | 否 |")
    L.append("")
    L.append("---")
    L.append("")

    # ── §5 取活规则（静态） ──
    L.append("## 5. 取活规则")
    L.append("")
    L.append("```text")
    L.append("1. 读本文件 §0 → 取「下一步」指向的任务")
    L.append("2. 读 zh/manifest.json → 取该任务内第一个 status == todo 的文件")
    L.append("3. 若 chunks_done 非空 → 从 max(chunks_done)+1 继续（断点续跑）")
    L.append("4. 每完成一段：写 chunk 注释 + 追加 chunks_done")
    L.append("5. 全部段完成：python zh/tools/check.py <文件> → 绿则 status: review")
    L.append("6. 会话结束：python zh/tools/progress.py 重新生成本文件")
    L.append("```")
    L.append("")
    L.append("`进度表 → 任务 → 文件 → 段` 四级寻址，任一级都能中断与恢复。")
    L.append("")
    L.append("---")
    L.append("")

    # ── §6 更新记录 ──
    L.append("## 6. 更新记录")
    L.append("")
    L.append("| 日期 | 事件 | 段 |")
    L.append("|---|---|---:|")
    history = list(prev_history or [])
    row = (today, "初始化：%d 任务 / %d 篇 / %d 段 / %d 完成" % (len(zmap.TASK_NAMES), ov["files"], ov["chunks"], ov["done"]), ov["done"])
    if not history:
        history = [row]
    elif history[-1][2] != ov["done"]:
        history.append((today, "进度更新：%d → %d 段" % (history[-1][2], ov["done"]), ov["done"]))
    for d, ev, seg in history:
        L.append("| %s | %s | %d |" % (d, ev, seg))
    L.append("")
    return "\n".join(L)


# ─── 历史表读取（保留上一次的更新记录行） ──────────────────────────────────
HIST_ROW_RE = re.compile(r"^\| (\d{4}-\d{2}-\d{2}) \| (.+?) \| (\d+) \|$")


def read_history(path=PROGRESS):
    if not os.path.isfile(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = HIST_ROW_RE.match(line.rstrip("\n"))
            if m:
                rows.append((m.group(1), m.group(2), int(m.group(3))))
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description="从 manifest.json 生成 zh/PROGRESS.md")
    ap.add_argument("--stdout", action="store_true", help="不写文件，只打印")
    ap.add_argument("--manifest", default=MANIFEST, help=argparse.SUPPRESS)
    ap.add_argument("--out", default=PROGRESS, help=argparse.SUPPRESS)
    args = ap.parse_args(argv)

    data = load_manifest(args.manifest)
    per_mod, per_task = aggregate(data)
    text = render(data, per_mod, per_task, read_history(args.out))

    if args.stdout:
        sys.stdout.write(text)
        return 0

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    ov = overall(data, per_mod, per_task)
    print(
        "写入 %s（%d 篇 / %d 段 / 完成 %d 段 / 覆盖率 %.1f%%）"
        % (os.path.relpath(args.out, REPO), ov["files"], ov["chunks"], ov["done"], ov["coverage"])
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
