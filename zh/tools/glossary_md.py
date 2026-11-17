#!/usr/bin/env python3
"""zh/GLOSSARY.yaml → zh/GLOSSARY.md（人读版）。

YAML 是唯一真相；本脚本只做投影。手工改 GLOSSARY.md 会在下次运行时被覆盖。

用法：
    python zh/tools/glossary_md.py           # 写文件
    python zh/tools/glossary_md.py --stdout  # 只打印
    python zh/tools/glossary_md.py --check   # 与现有文件比对，不一致退出 1
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zyaml  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
YAML = os.path.join(REPO, "zh", "GLOSSARY.yaml")
MD = os.path.join(REPO, "zh", "GLOSSARY.md")

SECTIONS = [
    ("核心概念", "上下文工程的基本词汇。出现在几乎每一篇里，最先要稳定下来。"),
    ("记忆与认知层级", "Atoms → Molecules → Cells → Organs 的层级隐喻，以及记忆系统的各个部件。"),
    ("智能体与工具", "智能体、工具调用、协议壳与编排。"),
    ("场论与涌现", "本书最具理论色彩的部分。多数词在中文语境里没有既有译法，本表的译法即规范。"),
    ("模式与递归", "可复用的结构、递归、元层操作。"),
    ("学习范式", "提示词工程的演进路径与教学用语。"),
    ("质量与运维", "评估、预算、可观测性。"),
]


def split_sections(text):
    """按 `# ─── 标题 ───` 切分 YAML 原文，返回 [(标题, 段落文本)]。"""
    out, cur, buf = [], "核心概念", []
    for line in text.splitlines():
        m = re.match(r"^# ─── (.+?) ─+$", line)
        if m:
            if buf:
                out.append((cur, "\n".join(buf)))
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if buf:
        out.append((cur, "\n".join(buf)))
    return out


def render():
    raw = open(YAML, encoding="utf-8").read()
    parts = split_sections(raw)
    total = sum(len(zyaml.load(body) or []) for _, body in parts)

    L = []
    L.append("---")
    L.append("title: 术语表")
    L.append("status: active")
    L.append("generated_by: zh/tools/glossary_md.py")
    L.append("source: zh/GLOSSARY.yaml")
    L.append("terms: %d" % total)
    L.append("rule: 本文件由脚本生成，禁止手改；改 zh/GLOSSARY.yaml 后重跑")
    L.append("---")
    L.append("")
    L.append("# 术语表")
    L.append("")
    L.append("> 唯一真相是 [`GLOSSARY.yaml`](GLOSSARY.yaml)，本页是它的只读投影。")
    L.append("> 机器（CI 的 G1 检查、翻译 agent）读 YAML；人读本页。")
    L.append(">")
    L.append("> 共 **%d** 条。带「歧义」标记的词有多个译法，按语境选择。" % total)
    L.append("")

    L.append("## 速查")
    L.append("")
    L.append("| 英文 | 中文 | 说明 |")
    L.append("|---|---|---|")
    for title, body in parts:
        for t in zyaml.load(body) or []:
            note = t.get("note") or ""
            if t.get("ambiguity"):
                note = ("⚠ " + note) if note else "⚠ 一词多义，见下文"
            L.append("| %s | **%s** | %s |" % (t["en"], t["zh"], note.replace("|", "\\|")))
    L.append("")

    for title, body in parts:
        terms = zyaml.load(body) or []
        if not terms:
            continue
        desc = dict(SECTIONS).get(title, "")
        L.append("## %s" % title)
        L.append("")
        if desc:
            L.append(desc)
            L.append("")
        for t in terms:
            L.append("### %s → %s" % (t["en"], t["zh"]))
            L.append("")
            if t.get("first_use"):
                L.append("- **首次出现写法**：`%s`" % t["first_use"])
            if t.get("forbid"):
                L.append("- **禁用译法**：%s" % "、".join("`%s`" % x for x in t["forbid"]))
            if t.get("note"):
                L.append("- **说明**：%s" % t["note"])
            if t.get("ambiguity"):
                L.append("- **一词多义**：")
                L.append("")
                L.append("  | 语境 | 译法 |")
                L.append("  |---|---|")
                for a in t["ambiguity"]:
                    L.append("  | %s | `%s` |" % (a["mean"], a["zh"]))
                L.append("")
            L.append("")
    return "\n".join(L).rstrip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="GLOSSARY.yaml → GLOSSARY.md")
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    md = render()
    if args.stdout:
        sys.stdout.write(md)
        return 0
    if args.check:
        if not os.path.isfile(MD):
            print("zh/GLOSSARY.md 不存在，请运行 python zh/tools/glossary_md.py", file=sys.stderr)
            return 1
        cur = open(MD, encoding="utf-8").read()
        if cur != md:
            print("zh/GLOSSARY.md 与 YAML 不一致，请重跑 glossary_md.py", file=sys.stderr)
            return 1
        print("zh/GLOSSARY.md 与 YAML 一致")
        return 0
    with open(MD, "w", encoding="utf-8") as fh:
        fh.write(md)
    n = md.count("\n### ")
    print("写入 zh/GLOSSARY.md（%d 条术语）" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
