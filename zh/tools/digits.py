#!/usr/bin/env python3
"""文档数字守卫：PLAN / PROGRESS / prompts 里的统计数字必须与 manifest.json 一致。

为什么需要它：这些数字（242 篇 / 676 段 / 30 空 / 各模块段数）被引用在 4 个文件里，
每次口径变化都要手改。已经发生过三次漂移（705→676 后 prompts/README.md 仍写 43/80/90/35/51）。
本脚本把「抄错数字」变成 CI 失败，而不是靠人眼。

只校验能机械判定的部分：模块表的「篇 / 段」、合计行、任务卡索引表。
散文式描述（"约 57.7 万字"）不校验，避免误报。

用法：
    python zh/tools/digits.py          # 检查，失败退出 1
    python zh/tools/digits.py --list   # 打印 manifest 真值，供对照
"""

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFEST = os.path.join(REPO, "zh", "manifest.json")


def load_truth():
    d = json.load(open(MANIFEST, encoding="utf-8"))
    mod = {}
    for f in d["files"]:
        m = mod.setdefault(f["module"], {"files": 0, "chunks": 0, "authored": 0})
        m["files"] += 1
        m["chunks"] += f["chunks"]
        if f["chunks"] == 0:
            m["authored"] += 1
    return d["totals"], mod


def check_module_table(path, truth_mod):
    """匹配 `| **M1** | 名称 | ... | 23 | 40 | ...` 形式的行。

    列位置因文件而异，故用「模块名 + 该行全部整数」的宽松匹配：
    取该行中出现的整数序列，要求其中包含 (篇, 段) 这对相邻值。
    """
    errs = []
    text = open(path, encoding="utf-8").read()
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        m = re.match(r"\*{0,2}(M\d+)\*{0,2}$", cells[0])
        if not m:
            continue
        mod = m.group(1)
        if mod not in truth_mod:
            continue
        t = truth_mod[mod]
        nums = []
        for c in cells[1:]:
            nums.extend(int(x) for x in re.findall(r"\b\d+\b", c))
        pair = (t["files"], t["chunks"])
        if t["chunks"] == 0:
            continue  # M11：段数为 0，行内数字不构成可判定对
        if not any(nums[i] == pair[0] and nums[i + 1] == pair[1] for i in range(len(nums) - 1)):
            errs.append(
                "%s: %s 行内未找到「篇=%d, 段=%d」（该行数字：%s）"
                % (os.path.relpath(path, REPO), mod, pair[0], pair[1], nums)
            )
    return errs


def check_prompt_index(path, truth_mod):
    """`| `M1_entry.md` | M1 入口层 | 23 | 40 | M0 | 待写 |` 形式。"""
    errs = []
    text = open(path, encoding="utf-8").read()
    pat = re.compile(
        r"^\|\s*`(M\d+)_[^`]*`\s*\|[^|]*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", re.M
    )
    seen = 0
    for m in pat.finditer(text):
        mod, files, chunks = m.group(1), int(m.group(2)), int(m.group(3))
        if mod not in truth_mod:
            continue
        seen += 1
        t = truth_mod[mod]
        if mod == "M11":
            continue
        if (files, chunks) != (t["files"], t["chunks"]):
            errs.append(
                "%s: %s 索引行写 %d 篇 / %d 段，manifest 是 %d 篇 / %d 段"
                % (
                    os.path.relpath(path, REPO),
                    mod,
                    files,
                    chunks,
                    t["files"],
                    t["chunks"],
                )
            )
    if seen == 0:
        errs.append("%s: 未匹配到任何任务卡索引行（格式可能已变）" % os.path.relpath(path, REPO))
    return errs


def check_totals(path, totals):
    """合计行里的 242 / 676 / 30 三件套。"""
    errs = []
    text = open(path, encoding="utf-8").read()
    want = [totals["files"], totals["chunks"], totals["authored"]]
    for line in text.splitlines():
        if "合计" not in line or not line.startswith("|"):
            continue
        # 只认模块表/任务表的合计行：它们一定提到 M0（工具链）或「任务」。
        # 内容类型表（散文/代码块/ASCII 图）也有「合计」，但那是体量口径，不是篇/段口径。
        if "M0" not in line and "任务" not in line:
            continue
        nums = [int(x) for x in re.findall(r"\b\d+\b", line)]
        if not nums:
            continue
        # 合计行必须同时出现这三个数（顺序不限，允许夹杂工具数等其它数字）
        missing = [w for w in want if w not in nums]
        if missing:
            errs.append(
                "%s: 合计行缺 %s（该行数字：%s）"
                % (os.path.relpath(path, REPO), missing, nums)
            )
    return errs


def main(argv=None):
    ap = argparse.ArgumentParser(description="文档数字守卫")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args(argv)

    totals, truth_mod = load_truth()
    if args.list:
        print("合计: %d 篇 / %d 段 / %d 空" % (totals["files"], totals["chunks"], totals["authored"]))
        for k in sorted(truth_mod, key=lambda x: int(x[1:])):
            t = truth_mod[k]
            print("%-4s %3d 篇  %3d 段  %2d 空" % (k, t["files"], t["chunks"], t["authored"]))
        return 0

    errs = []
    for rel in ("zh/PLAN/PLAN.md", "zh/PROGRESS.md"):
        p = os.path.join(REPO, rel)
        if not os.path.isfile(p):
            errs.append("%s 不存在" % rel)
            continue
        errs += check_module_table(p, truth_mod)
        errs += check_totals(p, totals)
    p = os.path.join(REPO, "zh/prompts/README.md")
    if os.path.isfile(p):
        errs += check_prompt_index(p, truth_mod)

    if errs:
        print("数字漂移 %d 处：" % len(errs), file=sys.stderr)
        for e in errs:
            print("  " + e, file=sys.stderr)
        print("\n真值用 `python zh/tools/digits.py --list` 查看。", file=sys.stderr)
        return 1
    print("文档数字与 manifest 一致（%d 篇 / %d 段 / %d 空）"
          % (totals["files"], totals["chunks"], totals["authored"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
