#!/usr/bin/env python3
"""单文件切分计划。

用法：
    python zh/tools/plan_chunks.py 00_foundations/02_molecules_context.md
    python zh/tools/plan_chunks.py 00_foundations/02_molecules_context.md --json
    python zh/tools/plan_chunks.py --module M2 --summary

切分规则（任务卡 §7.5）：
    1. 以 ^## 为一级切分点，^### 为二级
    2. 累计字节达到 6144 即切
    3. 遇到代码块/表格/ASCII 图不切——宁可超限
    4. 单段 < 512 字节时并入下一段
    5. 文件头（front matter 之后、首个 ## 之前）单独成段，无内容则并入第 1 段

**段数权威 = manifest.json 的 chunks 值**（= max(1, ⌈可译字节/6144⌉)）。
plan 的切分点数受此约束：切分在语义边界（H2/H3/空行）上做，
但段数与 manifest 保持一致，所以 `--summary` 可以逐文件交叉验证。
仅用标准库。
"""

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mdfence
import zmap

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFEST = os.path.join(REPO, "zh", "manifest.json")
CHUNK_BYTES = 6144
MIN_CHUNK_BYTES = 512

H2_RE = re.compile(r"^ {0,3}##[ \t]+\S")
H3_RE = re.compile(r"^ {0,3}###[ \t]+\S")
FM_END_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.S)


def line_ledger(text):
    """逐行可译字节台账。

    返回 (lines, tbytes)：
      lines   = text.splitlines(keepends=True)
      tbytes[k] = 该行贡献的可译字节
                  （有语言标记块整行 0；含框线块仅块体行 0；
                    纯文本块与散文行按 UTF-8 字节计）
    """
    fences, lines = mdfence.scan_fences(text)
    tbytes = [len(line.encode("utf-8")) for line in lines]
    for f in fences:
        if f.kind == "code":
            span = range(f.start, f.end + 1)
        elif f.kind == "art":
            span = range(f.start + 1, f.end + 1)
        else:
            continue
        for k in span:
            if 0 <= k < len(tbytes):
                tbytes[k] = 0
    return lines, tbytes


def _inside_fence_set(text):
    fences, _ = mdfence.scan_fences(text)
    inside = set()
    for f in fences:
        inside.update(range(f.start, f.end + 1))
    return inside


def _fm_line_count(text):
    m = FM_END_RE.match(text)
    return text[: m.end()].count("\n") if m else 0


def semantic_units(text):
    """按 H2 切出的语义单元：[(start, end, title)]，行号 0 基闭区间。

    文件头（front matter 之后、首个 H2 之前）作为 level-0 单元，
    若其中无任何可译字节则丢弃（并入第 1 段）。
    """
    lines, tbytes = line_ledger(text)
    inside = _inside_fence_set(text)
    h2 = []
    for k, line in enumerate(lines):
        if k in inside:
            continue
        if H2_RE.match(line.rstrip("\r\n")):
            h2.append((k, line.strip()))

    if not h2:
        return [(0, len(lines) - 1, "")]

    units = []
    head_start = _fm_line_count(text)
    head_end = h2[0][0] - 1
    if head_end >= head_start and sum(tbytes[head_start: head_end + 1]) > 0:
        units.append((head_start, head_end, ""))

    starts = [k for k, _ in h2]
    for i, (start, title) in enumerate(h2):
        end = (starts[i + 1] - 1) if i + 1 < len(starts) else len(lines) - 1
        units.append((start, end, title))
    return units


def _cut_points(lines, inside, start, end):
    """可作为切分点的行（0 基）：围栏外的空行、或 H2/H3 标题行。"""
    pts = []
    for k in range(start + 1, end + 1):
        if k in inside:
            continue
        s = lines[k].rstrip("\r\n")
        if not s.strip() or H2_RE.match(s) or H3_RE.match(s):
            pts.append(k)
    return pts


def _segments(text):
    """把全文切成"可在任意两个相邻片段之间断开"的最小片段序列。

    片段 = (start, end, tbytes)。切分点只落在 _cut_points 给出的行上。
    """
    lines, tbytes = line_ledger(text)
    inside = _inside_fence_set(text)
    units = semantic_units(text)
    out = []
    for start, end, _title in units:
        cuts = _cut_points(lines, inside, start, end)
        bounds = [start] + cuts + [end + 1]
        for a, b in zip(bounds, bounds[1:]):
            if a > end:
                continue
            seg_end = min(b - 1, end)
            out.append((a, seg_end, sum(tbytes[a: seg_end + 1])))
    # 去掉空片段，避免 0 字节段干扰切分
    return [s for s in out if s[1] >= s[0]], lines, tbytes


def _pack(segments, target):
    """贪心装箱：累计达到 target 即切。"""
    groups, cur, acc = [], [], 0
    for seg in segments:
        cur.append(seg)
        acc += seg[2]
        if acc >= target:
            groups.append(cur)
            cur, acc = [], 0
    if cur:
        groups.append(cur)
    return groups


def _merge_small(groups, min_bytes):
    """规则 4：单段 < min_bytes 时并入相邻段（优先并入前一段）。"""
    if len(groups) <= 1:
        return groups
    out = [list(g) for g in groups]
    i = 0
    while i < len(out) - 1:
        size = sum(s[2] for s in out[i])
        if size < min_bytes:
            out[i + 1] = out[i] + out[i + 1]
            del out[i]
            continue
        i += 1
    return out


def _adjust(groups, n, segments):
    """把段数微调到 n：不足则对半拆最长段，过多则合并最短相邻对。"""
    groups = [list(g) for g in groups]
    guard = 0
    while len(groups) < n and guard < 10000:
        guard += 1
        idx = max(range(len(groups)), key=lambda i: sum(s[2] for s in groups[i]))
        grp = groups[idx]
        if len(grp) < 2:
            break
        h = len(grp) // 2
        groups[idx: idx + 1] = [grp[:h], grp[h:]]
    while len(groups) > n and len(groups) > 1 and guard < 20000:
        guard += 1
        sizes = [sum(s[2] for s in g) for g in groups]
        i = min(range(len(groups) - 1), key=lambda k: sizes[k] + sizes[k + 1])
        groups[i: i + 2] = [groups[i] + groups[i + 1]]
    # 段数仍不足（片段太少）：退化为按片段均分
    if len(groups) < n and len(segments) >= n:
        total = sum(s[2] for s in segments)
        per = max(1, total // n)
        groups = _adjust(_pack(segments, per), n, segments)
    return groups


def plan(text, chunk_bytes=CHUNK_BYTES):
    """返回 (chunks, lines, total)。

    chunks: [(start_line, end_line, tbytes, [H2 titles])]，行号 1 基闭区间。
    """
    file_bytes = len(text.encode("utf-8"))
    total = mdfence.translatable_bytes(text)
    lines, tbytes = line_ledger(text)
    if file_bytes < 5:
        return [], lines, total

    n = mdfence.chunks_for(total, file_bytes, chunk_bytes)
    segments, _, _ = _segments(text)

    if n <= 1 or len(segments) <= 1:
        titles = [
            ln.strip()
            for k, ln in enumerate(lines)
            if k not in _inside_fence_set(text) and H2_RE.match(ln.rstrip("\r\n"))
        ]
        return [(1, max(1, len(lines)), total, titles)], lines, total

    per = max(1, -(-total // n))
    groups = _pack(segments, per)
    groups = _merge_small(groups, MIN_CHUNK_BYTES)
    # 二分目标值，使装箱段数尽量接近 n
    lo, hi = 1, max(per * 3, total)
    best = groups
    while lo <= hi:
        mid = (lo + hi) // 2
        cand = _merge_small(_pack(segments, mid), MIN_CHUNK_BYTES)
        if len(cand) > n:
            lo = mid + 1
        elif len(cand) < n:
            best = cand if abs(len(cand) - n) < abs(len(best) - n) else best
            hi = mid - 1
        else:
            best = cand
            break
    groups = _adjust(best, n, segments)

    out = []
    for grp in groups:
        if not grp:
            continue
        a, b = grp[0][0], grp[-1][1]
        tb = sum(s[2] for s in grp)
        titles = [t for s in grp for t in [lines[s[0]].strip()] if H2_RE.match(lines[s[0]].rstrip("\r\n"))]
        out.append((a + 1, b + 1, tb, titles))
    return out, lines, total


def _sha8(text, a, b):
    lines = text.splitlines(keepends=True)
    return hashlib.sha256("".join(lines[a - 1:b]).encode("utf-8")).hexdigest()[:8]


def render_markdown(rel, text, chunks, total, source_bytes, expected=None):
    out = ["# 切分计划：%s" % rel, ""]
    note = "源文件 %d 字节，可译 %d 字节，%d 段（目标 ≤ %d 可译字节/段）" % (
        source_bytes,
        total,
        len(chunks),
        CHUNK_BYTES,
    )
    if expected is not None:
        note += "，manifest 段数 %d（%s）" % (expected, "一致" if expected == len(chunks) else "不一致")
    out.append(note)
    out.append("")
    for i, (a, b, tb, titles) in enumerate(chunks, 1):
        out.append(
            "### chunk %d/%d  lines %d-%d  sha %s  bytes %d"
            % (i, len(chunks), a, b, _sha8(text, a, b), tb)
        )
        for t in titles:
            out.append(t)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="单文件切分计划")
    ap.add_argument("path", nargs="?", help="源文件，仓库根相对")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--module", metavar="M2", help="整模块")
    ap.add_argument("--summary", action="store_true", help="每文件一行摘要（与 manifest 交叉验证）")
    args = ap.parse_args(argv)

    if args.path:
        targets = [args.path.replace(os.sep, "/")]
    elif args.module:
        targets = [p for p in zmap.walk_sources(REPO) if zmap.module_of(p) == args.module]
    else:
        ap.error("需要 <path> 或 --module")

    manifest_chunks = {}
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as fh:
            data = json.load(fh)
        manifest_chunks = {e["source"]: e["chunks"] for e in data["files"]}

    rc = 0
    summaries = []
    for rel in targets:
        full = os.path.join(REPO, rel)
        if not os.path.isfile(full):
            print("文件不存在：%s" % rel, file=sys.stderr)
            return 2
        with open(full, "rb") as fh:
            raw = fh.read()
        text = raw.decode("utf-8", errors="replace")
        chunks, lines, total = plan(text)
        expect = manifest_chunks.get(rel)
        if expect is not None and expect != len(chunks):
            rc = 1
        if args.json:
            print(
                json.dumps(
                    {
                        "source": rel,
                        "source_bytes": len(raw),
                        "todo_bytes": total,
                        "chunks": len(chunks),
                        "manifest_chunks": expect,
                        "matches_manifest": None if expect is None else expect == len(chunks),
                        "plan": [
                            {
                                "index": i,
                                "lines": [a, b],
                                "bytes": tb,
                                "sha8": _sha8(text, a, b),
                                "titles": titles,
                            }
                            for i, (a, b, tb, titles) in enumerate(chunks, 1)
                        ],
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
        elif args.summary:
            summaries.append((rel, len(chunks), expect))
        else:
            sys.stdout.write(render_markdown(rel, text, chunks, total, len(raw), expect))

    if args.summary:
        print("| 文件 | plan 段 | manifest 段 | 结果 |")
        print("|---|---:|---:|---|")
        for rel, got, exp in summaries:
            ok = "OK" if exp is None or exp == got else "MISMATCH"
            print("| `%s` | %d | %s | %s |" % (rel, got, "—" if exp is None else exp, ok))
        bad = sum(1 for _, g, e in summaries if e is not None and e != g)
        print("\n合计 %d 文件，%d 处不一致" % (len(summaries), bad))
    return rc


if __name__ == "__main__":
    sys.exit(main())
