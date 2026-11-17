#!/usr/bin/env python3
"""G1–G9 九项质量门禁，单一入口。

用法：
    python zh/tools/check.py zh/00_foundations/01_atoms_prompting.md
    python zh/tools/check.py --module M2
    python zh/tools/check.py --all
    python zh/tools/check.py <path> --only G2,G4
    python zh/tools/check.py --self-test

退出码：全通过 0，否则 1。
仅用标准库。
"""

import argparse
import json
import os
import re
import sys
import unicodedata
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mdfence
import zmap
import zyaml

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GLOSSARY = os.path.join(REPO, "zh", "GLOSSARY.yaml")
MANIFEST = os.path.join(REPO, "zh", "manifest.json")
KNOWN_ISSUES = os.path.join(REPO, "zh", "KNOWN_ISSUES.md")

ALL_CHECKS = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
CHECK_NAMES = {
    "G1": "术语一致性",
    "G2": "ASCII 图完整性",
    "G3": "代码围栏",
    "G4": "占位符保全",
    "G5": "内部链接",
    "G6": "front matter",
    "G7": "英文残留",
    "G8": "双语锚点",
    "G9": "结构对齐",
}
PASS, WARN, FAIL, SKIP = "PASS", "WARN", "FAIL", "SKIP"


def _pad(text, width):
    """按显示宽度补空格（CJK 记 2 列），让中文列在终端里对齐。"""
    w = sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)
    return text + " " * max(0, width - w)

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
H2_ALLOWED_EXTRA = {"小结", "延伸阅读"}


# ─── 公共工具 ────────────────────────────────────────────────────────────


def split_front_matter(text):
    """返回 (front_matter_dict|None, body)。"""
    m = FM_RE.match(text)
    if not m:
        return None, text
    fm = {}
    for raw in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip("'\"")
    return fm, text[m.end():]


def body_without_fm(text):
    return split_front_matter(text)[1]


class Ctx:
    """一次检查所需的全部上下文。"""

    def __init__(self, target_path, target_text, source_path, source_text, repo=REPO):
        self.target_path = target_path  # 仓库根相对，如 zh/xx.md
        self.target_text = target_text
        self.source_path = source_path  # 仓库根相对
        self.source_text = source_text
        self.repo = repo

    @property
    def abs_target(self):
        return os.path.join(self.repo, self.target_path)

    def fmt(self, line=None, msg=""):
        loc = self.target_path + (":%d" % line if line else "")
        return "%s  %s" % (loc, msg) if msg else loc


def load_glossary(path=GLOSSARY):
    if not os.path.isfile(path):
        return []
    return zyaml.load_file(path) or []


def load_known_links(path=KNOWN_ISSUES):
    """从 KNOWN_ISSUES.md 解析白名单链接。

    只读「## 明细」章节的表格，取第 2 列（失效链接）。
    这样「## 统计」等其它表格不会污染白名单（否则会多出 10 条噪声）。
    """
    out = set()
    if not os.path.isfile(path):
        return out
    in_detail = False
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("## "):
                in_detail = "明细" in line
                continue
            if not in_detail or not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            link = cells[1].strip("` ")
            if not link or link in ("失效链接", "---") or set(link) <= {"-", ":"}:
                continue
            out.add(link)
    return out


# ─── G1 术语一致性 ────────────────────────────────────────────────────────


def check_g1(ctx, glossary):
    """禁用译法在散文区零命中。"""
    entries = glossary
    if not entries:
        return SKIP, "GLOSSARY.yaml 缺失或为空"
    text = mdfence.strip_fences(body_without_fm(ctx.target_text))
    # 先遮蔽规范译法，避免「提示词」被「提示」误伤
    canon = sorted({e["zh"] for e in entries if e.get("zh")}, key=len, reverse=True)
    masked = text
    for i, z in enumerate(canon):
        masked = masked.replace(z, "\x00%d\x00" % i)
    hits = []
    for e in entries:
        for bad in e.get("forbid") or []:
            if not bad:
                continue
            idx = masked.find(bad)
            if idx >= 0:
                line = masked[:idx].count("\n") + 1
                hits.append((line, e["en"], bad, e.get("zh")))
    if hits:
        line, en, bad, good = sorted(hits)[0]
        return FAIL, ctx.fmt(line, "禁用译法「%s」（%s 应为「%s」），共 %d 处" % (bad, en, good, len(hits)))
    return PASS, "禁用译法零命中"


# ─── G2 ASCII 图完整性 ────────────────────────────────────────────────────


def check_g2(ctx, **_):
    """无标记块内不得出现全角字符。"""
    fences, lines = mdfence.scan_fences(ctx.target_text)
    bad = []
    for f in fences:
        if f.lang:
            continue
        body = "".join(lines[f.start + 1:f.end])
        if mdfence.CJK_RE.search(body):
            m = mdfence.CJK_RE.search(body)
            line = f.start + 2 + body[:m.start()].count("\n")
            bad.append((line, m.group(0)))
    if bad:
        line, ch = sorted(bad)[0]
        return FAIL, ctx.fmt(line, "框线块含全角字符「%s」，共 %d 块" % (ch, len(bad)))
    return PASS, "无标记块内无全角字符"


# ─── G3 代码围栏 ──────────────────────────────────────────────────────────


def check_g3(ctx, **_):
    """围栏配对；语言标记与原文同序同值。"""
    src_fences, _ = mdfence.scan_fences(ctx.source_text)
    dst_fences, _ = mdfence.scan_fences(ctx.target_text)
    src_seq = [f.lang for f in src_fences]
    dst_seq = [f.lang for f in dst_fences]
    src_odd = sum(1 for f in src_fences if not f.closed) > 0
    dst_odd = sum(1 for f in dst_fences if not f.closed) > 0
    if not src_odd and dst_odd:
        f = [f for f in dst_fences if not f.closed][0]
        return FAIL, ctx.fmt(f.start + 1, "围栏未闭合（原文已闭合）")
    if len(src_seq) != len(dst_seq):
        return FAIL, ctx.fmt(
            None, "围栏块数 %d != 原文 %d" % (len(dst_seq), len(src_seq))
        )
    for i, (a, b) in enumerate(zip(src_seq, dst_seq)):
        if a != b:
            return FAIL, ctx.fmt(
                dst_fences[i].start + 1,
                "第 %d 块语言标记 %r != 原文 %r" % (i + 1, b, a),
            )
    return PASS, "围栏配对，%d 块语言序列一致" % len(dst_seq)


# ─── G4 占位符保全 ────────────────────────────────────────────────────────


def check_g4(ctx, **_):
    """{{...}} 多重集相等。"""
    src = mdfence.placeholders(ctx.source_text)
    dst = mdfence.placeholders(ctx.target_text)
    if src == dst:
        return PASS, "占位符 %d 个，多重集一致" % len(dst)
    missing = [p for p in src if src.count(p) > dst.count(p)]
    extra = [p for p in dst if dst.count(p) > src.count(p)]
    detail = []
    if missing:
        detail.append("缺 %s" % ", ".join(sorted(set(missing))[:3]))
    if extra:
        detail.append("多 %s" % ", ".join(sorted(set(extra))[:3]))
    return FAIL, ctx.fmt(None, "占位符多重集不等：%s" % "；".join(detail))


# ─── G5 内部链接 ──────────────────────────────────────────────────────────


def check_g5(ctx, whitelist=None, strict=False, **_):
    """相对链接目标存在；已知失效走白名单；指向未译文件的算 pending。

    三种状态必须分开，否则要么逼译者删链接，要么放过真正写错的路径：

    - 可达                     → 通过
    - 指向 zh/ 内尚不存在的路径，但上游源文件存在 → `pending`（该模块还没译）
    - 以上都不是               → 真失效，FAIL

    `strict=True`（`--strict-links`）把 pending 也算 FAIL，用于全库译完后的终检。
    """
    whitelist = whitelist or set()
    text = body_without_fm(ctx.target_text)
    base = os.path.dirname(ctx.abs_target)
    bad, pending, known = [], [], 0
    for m in LINK_RE.finditer(text):
        href = m.group(1)
        if re.match(r"^[a-zA-Z][\w+.-]*:", href) or href.startswith("#"):
            continue
        if href.startswith("mailto:"):
            continue
        target = href.split("#", 1)[0]
        if not target:
            continue
        dest = os.path.normpath(os.path.join(base, target))
        if os.path.exists(dest):
            continue
        if href in whitelist or target in whitelist:
            known += 1
            continue

        # 译文缺失但源文件在 → 该模块尚未翻译，链接本身没写错
        zh_root = os.path.normpath(os.path.join(ctx.repo, "zh"))
        rel = os.path.relpath(dest, zh_root)
        src_guess = None
        if not rel.startswith(".."):
            src_guess = os.path.join(ctx.repo, rel)
        if src_guess and os.path.exists(src_guess):
            pending.append((text[: m.start()].count("\n") + 1, href))
            continue

        bad.append((text[: m.start()].count("\n") + 1, href))

    if bad:
        line, href = sorted(bad)[0]
        return FAIL, ctx.fmt(line, "链接失效：%s（共 %d 处）" % (href, len(bad)))
    if pending and strict:
        line, href = sorted(pending)[0]
        return FAIL, ctx.fmt(
            line, "链接指向未译文件：%s（共 %d 处，--strict-links 下计为失败）" % (href, len(pending))
        )
    bits = []
    if known:
        bits.append("白名单 %d 处" % known)
    if pending:
        bits.append("待译 %d 处" % len(pending))
    note = "链接全部可达" + ("（" + "，".join(bits) + "）" if bits else "")
    return PASS, note


# ─── G6 front matter ─────────────────────────────────────────────────────


REQUIRED_FM = ["title", "source", "module", "task", "chunks", "status", "source_sha256"]


def check_g6(ctx, **_):
    """front matter 字段齐全；source_sha256 与当前源文件一致。"""
    import hashlib

    fm, _ = split_front_matter(ctx.target_text)
    if fm is None:
        return FAIL, ctx.fmt(1, "缺少 front matter")
    missing = [k for k in REQUIRED_FM if not fm.get(k)]
    if missing:
        return FAIL, ctx.fmt(1, "front matter 缺字段：%s" % ", ".join(missing))
    want = hashlib.sha256(ctx.source_text.encode("utf-8")).hexdigest()
    got = fm.get("source_sha256", "")
    if got and got != want:
        return FAIL, ctx.fmt(
            1, "source_sha256 不匹配（译文 %s… 源 %s…）" % (got[:8], want[:8])
        )
    src_field = fm.get("source", "")
    if ctx.source_path and src_field not in ("null", "-", ctx.source_path):
        return FAIL, ctx.fmt(
            1, "source 字段 %r != %r" % (src_field, ctx.source_path)
        )
    return PASS, "front matter 完整"


# ─── G7 英文残留（WARN） ─────────────────────────────────────────────────


def check_g7(ctx, **_):
    """代码块之外，英文行占比 > 30% → WARN。"""
    prose = mdfence.strip_fences(body_without_fm(ctx.target_text))
    lines = [ln for ln in prose.splitlines() if ln.strip()]
    if not lines:
        return SKIP, "无正文行"
    english = 0
    for ln in lines:
        has_ascii = re.search(r"[A-Za-z]", ln)
        has_cjk = re.search(r"[\u4e00-\u9fff]", ln)
        if has_ascii and not has_cjk:
            english += 1
    ratio = english / len(lines)
    if ratio > 0.30:
        return WARN, ctx.fmt(None, "英文行占比 %.0f%%（%d/%d），疑似中英夹杂" % (ratio * 100, english, len(lines)))
    return PASS, "英文行占比 %.0f%%" % (ratio * 100)


# ─── G8 双语锚点 ─────────────────────────────────────────────────────────


def check_g8(ctx, **_):
    """双语锚点：原文链接与 GLOSSARY 链接都必须真实可达且指向正确。

    只查关键词出现是不够的——锚点写错相对层级是最常见的复制粘贴错误。
    """
    head = "\n".join(body_without_fm(ctx.target_text).splitlines()[:20])
    if "> 原文：" not in head:
        return FAIL, ctx.fmt(1, "首 20 行缺「> 原文：」锚点")
    if "GLOSSARY" not in head:
        return FAIL, ctx.fmt(1, "首 20 行缺 GLOSSARY 链接")

    base = os.path.dirname(ctx.abs_target)
    rel_target = os.path.relpath(base, ctx.repo).replace(os.sep, "/")

    src_line = next((l for l in head.splitlines() if l.startswith("> 原文：")), "")
    m = re.search(r"\[([^\]]*)\]\(([^)\s]+)\)", src_line)
    if not m:
        return FAIL, ctx.fmt(2, "「> 原文：」后没有 Markdown 链接")
    href = m.group(2).split("#", 1)[0]
    dest = os.path.normpath(os.path.join(base, href))
    want = os.path.normpath(os.path.join(ctx.repo, ctx.source_path))
    if not os.path.exists(dest):
        return FAIL, ctx.fmt(
            2,
            "原文锚点失效：%s（在 %s 下解析为仓库根之外的 %s；该目录深度 %d，需要 %s）"
            % (href, rel_target, os.path.relpath(dest, ctx.repo), base.count(os.sep),
               "../" * base.count(os.sep) + ctx.source_path),
        )
    if dest != want:
        return FAIL, ctx.fmt(
            2,
            "原文锚点指错：%s 解析到 %s，应为 %s"
            % (href, os.path.relpath(dest, ctx.repo), ctx.source_path),
        )

    g_line = next((l for l in head.splitlines() if "GLOSSARY" in l), "")
    gm = re.search(r"\[GLOSSARY[^\]]*\]\(([^)\s]+)\)", g_line)
    if not gm:
        return FAIL, ctx.fmt(3, "GLOSSARY 未写成 Markdown 链接")
    ghref = gm.group(1).split("#", 1)[0]
    gdest = os.path.normpath(os.path.join(base, ghref))
    gwant = os.path.join(ctx.repo, "zh", "GLOSSARY.md")
    if not os.path.exists(gdest):
        return FAIL, ctx.fmt(
            3, "GLOSSARY 锚点失效：%s 解析到 %s（应为 zh/GLOSSARY.md）"
            % (ghref, os.path.relpath(gdest, ctx.repo)),
        )
    if os.path.normpath(gdest) != os.path.normpath(gwant):
        return FAIL, ctx.fmt(
            3, "GLOSSARY 锚点指错：%s 解析到 %s，应为 zh/GLOSSARY.md"
            % (ghref, os.path.relpath(gdest, ctx.repo)),
        )
    return PASS, "双语锚点齐全且可达"


# ─── G9 结构对齐 ─────────────────────────────────────────────────────────


def check_g9(ctx, **_):
    """H2 数量与原文一致（允许多出「小结」「延伸阅读」各一节）。"""
    src = mdfence.h2_titles(ctx.source_text)
    dst = mdfence.h2_titles(ctx.target_text)
    extra = dst[len(src):] if len(dst) > len(src) else []
    allowed = 0
    for t in extra:
        title = t.lstrip("#").strip()
        if any(a in title for a in H2_ALLOWED_EXTRA):
            allowed += 1
    if len(dst) < len(src):
        return FAIL, ctx.fmt(None, "H2 数量 %d < 原文 %d（疑似漏译标题）" % (len(dst), len(src)))
    if len(dst) - allowed > len(src):
        bad = [t for t in extra if not any(a in t for a in H2_ALLOWED_EXTRA)]
        return FAIL, ctx.fmt(None, "多出未授权 H2：%s" % (bad[:2],))
    return PASS, "H2 数量 %d == 原文 %d" % (len(dst) - allowed, len(src))


CHECK_FUNCS = {
    "G1": check_g1,
    "G2": check_g2,
    "G3": check_g3,
    "G4": check_g4,
    "G5": check_g5,
    "G6": check_g6,
    "G7": check_g7,
    "G8": check_g8,
    "G9": check_g9,
}


# ─── 驱动 ────────────────────────────────────────────────────────────────


def run_one(ctx, checks, glossary, whitelist, strict=False):
    results = {}
    for gid in checks:
        fn = CHECK_FUNCS[gid]
        kwargs = {}
        if gid == "G1":
            kwargs["glossary"] = glossary
        if gid == "G5":
            kwargs["whitelist"] = whitelist
            kwargs["strict"] = strict
        try:
            results[gid] = fn(ctx, **kwargs)
        except Exception as exc:  # 单项异常不应拖垮整体
            results[gid] = (FAIL, "检查异常：%s" % exc)
    return results


def load_manifest_map():
    if not os.path.isfile(MANIFEST):
        return {}
    with open(MANIFEST, encoding="utf-8") as fh:
        data = json.load(fh)
    return {e["target"]: e for e in data.get("files", [])}


def collect_targets(module=None, only_all=False):
    """收集待检译文（zh/**/*.md，排除 zh/prompts、zh/PLAN、zh/tools 等元文件）。"""
    mans = load_manifest_map()
    out = []
    for target in mans:
        if module and mans[target]["module"] != module:
            continue
        path = os.path.join(REPO, target)
        if os.path.isfile(path):
            out.append((target, mans[target]["source"]))
    if not out and not only_all:
        return []
    return sorted(out)


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def run_checks(pairs, checks, title=None, strict=False):
    glossary = load_glossary()
    whitelist = load_known_links()
    agg = {g: (PASS, "全部通过", 0) for g in checks}  # (status, msg, failcount)
    severity = {PASS: 0, SKIP: 1, WARN: 2, FAIL: 3}
    checked = 0
    for target, source in pairs:
        tpath = os.path.join(REPO, target)
        spath = os.path.join(REPO, source)
        if not os.path.isfile(tpath):
            continue
        checked += 1
        ctx = Ctx(target, read_text(tpath), source, read_text(spath))
        res = run_one(ctx, checks, glossary, whitelist, strict)
        for g, (st, msg) in res.items():
            cur_st, cur_msg, cnt = agg[g]
            if st == FAIL:
                cnt += 1
            if severity[st] > severity[cur_st]:
                agg[g] = (st, msg, cnt if st != FAIL else cnt)
            elif st == FAIL:
                agg[g] = (cur_st, cur_msg, cnt)
    if checked == 0:
        print("无译文，跳过（zh/ 尚无对应译文文件）")
        return 0
    npass = nfail = nwarn = 0
    for g in checks:
        st, msg, cnt = agg[g]
        if st == FAIL:
            nfail += 1
        elif st == WARN:
            nwarn += 1
            npass += 1
        elif st == SKIP:
            npass += 1
        else:
            npass += 1
        print("%s %s %s  %s" % (g, _pad(CHECK_NAMES[g], 16), st, msg))
    print("汇总 %d PASS / %d FAIL%s（%d 文件）" % (npass, nfail, " / %d WARN" % nwarn if nwarn else "", checked))
    return 0 if nfail == 0 else 1


# ─── 自检：内置正/反样例 ──────────────────────────────────────────────────

_SRC_SAMPLE = """---
title: Atoms
---

# Atoms

## First Section

Some prose about context with {{task_description}} placeholder.

```python
print("hello")
```

```
+-----+
| box |
+-----+
```

## Second Section

More prose with {{task_description}} and {{problem}}.
"""

_GOOD_TARGET = """---
title: 原子
source: demo/sample.md
module: M2
task: M2-01
chunks: 1
status: draft
source_sha256: {sha}
---

# 原子

> 原文：[demo/sample.md](../../demo/sample.md)
> 术语对照：[GLOSSARY.md](../GLOSSARY.md)

## 第一节

关于上下文的一些散文，含 {{{{task_description}}}} 占位符。

```python
print("hello")
```

```
+-----+
| box |
+-----+
```

## 第二节

更多散文，含 {{{{task_description}}}} 与 {{{{problem}}}}。

见 [术语表](../GLOSSARY.md)。
"""


def _build_self_case(tmpdir, sha):
    src = os.path.join(tmpdir, "demo")
    os.makedirs(src, exist_ok=True)
    with open(os.path.join(src, "sample.md"), "w", encoding="utf-8") as fh:
        fh.write(_SRC_SAMPLE)
    zhdemo = os.path.join(tmpdir, "zh", "demo")
    os.makedirs(zhdemo, exist_ok=True)
    # 锚点写作 ../GLOSSARY.md（zh/demo/ → zh/GLOSSARY.md），故 zh/GLOSSARY.md 需真实存在
    with open(os.path.join(tmpdir, "zh", "GLOSSARY.md"), "w", encoding="utf-8") as fh:
        fh.write("# 术语表\n")
    good = _GOOD_TARGET.format(sha=sha)
    path = os.path.join(zhdemo, "sample.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(good)
    return "zh/demo/sample.md", "demo/sample.md", tmpdir


def self_test():
    import hashlib

    glossary = load_glossary()
    whitelist = set()
    sha = hashlib.sha256(_SRC_SAMPLE.encode("utf-8")).hexdigest()
    with tempfile.TemporaryDirectory() as tmp:
        tgt, src, repo = _build_self_case(tmp, sha)
        good_ctx = Ctx(tgt, _GOOD_TARGET.format(sha=sha), src, _SRC_SAMPLE, repo=repo)
        base = run_one(good_ctx, ALL_CHECKS, glossary, whitelist)
        results = []
        for g in ALL_CHECKS:
            st = base[g][0]
            ok_pos = st in (PASS, SKIP)
            # 反例：针对每项构造一个"应 FAIL"的变体
            bad_text = _mutate(g, _GOOD_TARGET.format(sha=sha), sha)
            if bad_text is None:
                results.append((g, ok_pos, False, "无反例样本"))
                continue
            bad_ctx = Ctx(tgt, bad_text, src, _SRC_SAMPLE, repo=repo)
            st_bad = run_one(bad_ctx, [g], glossary, whitelist)[g][0]
            ok_neg = st_bad in (FAIL, WARN)
            results.append((g, ok_pos, ok_neg, st_bad))
        for g, ok_pos, ok_neg, _ in results:
            good = ok_pos and ok_neg
            print("%s %s %s  正例%s / 反例%s" % (
                g, _pad(CHECK_NAMES[g], 16), PASS if good else FAIL,
                "过" if ok_pos else "挂", "捕获" if ok_neg else "漏"))
    n = sum(1 for _, a, b, _ in results if a and b)
    print("self-test: %d/9 %s" % (n, "PASS" if n == 9 else "FAIL"))
    return 0 if n == 9 else 1


def _mutate(gid, good, sha):
    """为每项检查返回一个应当失败的样本。"""
    if gid == "G1":
        return good.replace("关于上下文的一些散文", "关于语境的一些散文")
    if gid == "G2":
        return good.replace("| box |", "| 框 |")
    if gid == "G3":
        return good.replace("```python", "```javascript", 1)
    if gid == "G4":
        return good.replace("{{problem}}", "{{problemX}}")
    if gid == "G5":
        return good.replace("见 [术语表](../GLOSSARY.md)", "见 [术语表](../MISSING.md)")
    if gid == "G6":
        return good.replace(sha, "0" * 64)
    if gid == "G7":
        body = good.rsplit("## 第二节", 1)[0]
        body += "## 第二节\n\n" + "This line is pure English without any Chinese.\n" * 20
        return body
    if gid == "G8":
        return good.replace("> 原文：", "> source: ")
    if gid == "G9":
        return good.replace("## 第二节", "### 第二节")
    return None


# ─── main ────────────────────────────────────────────────────────────────


def main(argv=None):
    ap = argparse.ArgumentParser(description="G1–G9 质量门禁")
    ap.add_argument("path", nargs="?", help="译文路径，如 zh/00_foundations/01_atoms_prompting.md")
    ap.add_argument("--module", metavar="M2", help="只检查该模块")
    ap.add_argument("--all", action="store_true", help="检查全部译文")
    ap.add_argument("--only", metavar="G2,G4", help="只跑指定检查")
    ap.add_argument("--self-test", action="store_true", help="内置正反样例自检九项检查")
    ap.add_argument(
        "--strict-links",
        action="store_true",
        help="G5 把「指向未译文件」也计为失败（全库译完后的终检用）",
    )
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    checks = ALL_CHECKS
    if args.only:
        checks = [c.strip().upper() for c in args.only.split(",") if c.strip()]
        unknown = [c for c in checks if c not in CHECK_FUNCS]
        if unknown:
            print("未知检查项：%s" % ", ".join(unknown), file=sys.stderr)
            return 2

    mans = load_manifest_map()
    pairs = []
    if args.path:
        tpath = args.path.replace(os.sep, "/")
        if not os.path.isabs(args.path):
            cand = os.path.normpath(os.path.join(os.getcwd(), args.path))
            if os.path.isfile(cand):
                tpath = os.path.relpath(cand, REPO).replace(os.sep, "/")
        if tpath not in mans:
            print("不在 manifest 中：%s" % tpath, file=sys.stderr)
            return 2
        pairs = [(tpath, mans[tpath]["source"])]
    elif args.module or args.all:
        pairs = collect_targets(args.module, only_all=True)
    else:
        # 无参数：等同 --all
        pairs = collect_targets(None, only_all=True)

    return run_checks(pairs, checks, strict=args.strict_links)


if __name__ == "__main__":
    sys.exit(main())
